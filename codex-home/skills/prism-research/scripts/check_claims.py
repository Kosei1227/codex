#!/usr/bin/env python3
"""Check evidence IDs and claim grounding in a Prism workspace."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


EVIDENCE_RE = re.compile(r"\bEV-[A-Za-z0-9_-]+\b")
CLAIM_RE = re.compile(r"\bCL-[A-Za-z0-9_-]+\b")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", default=".", help="Prism project root.")
    parser.add_argument("--evidence", default="evidence/evidence.jsonl")
    parser.add_argument("--claim-ledger", default="evidence/claim_ledger.md")
    parser.add_argument("--scan", nargs="*", default=["manuscript", "reviews", "evidence"])
    parser.add_argument("--out-json", default="artifacts/claim_check.json")
    parser.add_argument("--out-md", default="artifacts/claim_check.md")
    return parser.parse_args()


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def load_evidence(path: Path) -> tuple[dict[str, dict], list[dict], list[str]]:
    evidence: dict[str, dict] = {}
    malformed: list[dict] = []
    duplicates: list[str] = []
    if not path.exists():
        return evidence, [{"line": 0, "error": "evidence file does not exist"}], duplicates

    for line_no, line in enumerate(read_text(path).splitlines(), start=1):
        stripped = line.strip()
        if not stripped:
            continue
        try:
            item = json.loads(stripped)
        except json.JSONDecodeError as exc:
            malformed.append({"line": line_no, "error": str(exc)})
            continue
        evidence_id = str(item.get("id", "")).strip()
        if not evidence_id:
            malformed.append({"line": line_no, "error": "missing id"})
            continue
        if evidence_id in evidence and evidence_id not in duplicates:
            duplicates.append(evidence_id)
        evidence[evidence_id] = item
    return evidence, malformed, duplicates


def collect_text_files(project: Path, scan_roots: list[str]) -> list[Path]:
    files: list[Path] = []
    for root_name in scan_roots:
        root = project / root_name
        if root.is_file():
            files.append(root)
        elif root.exists():
            for suffix in ("*.md", "*.tex", "*.txt"):
                files.extend(root.rglob(suffix))
    return sorted(set(path.resolve() for path in files))


def scan_references(files: list[Path]) -> dict[str, list[str]]:
    refs: dict[str, list[str]] = {}
    for path in files:
        text = read_text(path)
        for match in EVIDENCE_RE.finditer(text):
            refs.setdefault(match.group(0), []).append(str(path))
    return refs


def scan_claim_ledger(path: Path) -> tuple[list[dict], list[dict]]:
    claims: list[dict] = []
    ungrounded: list[dict] = []
    if not path.exists():
        return claims, [{"line": 0, "claim_id": "", "text": "claim ledger does not exist"}]

    for line_no, line in enumerate(read_text(path).splitlines(), start=1):
        claim_match = CLAIM_RE.search(line)
        if not claim_match:
            continue
        claim_id = claim_match.group(0)
        evidence_ids = sorted(set(EVIDENCE_RE.findall(line)))
        record = {"line": line_no, "claim_id": claim_id, "evidence_ids": evidence_ids, "text": line.strip()}
        claims.append(record)
        if not evidence_ids:
            ungrounded.append(record)
    return claims, ungrounded


def write_reports(project: Path, report: dict, out_json: Path, out_md: Path) -> None:
    json_path = project / out_json
    md_path = project / out_md
    json_path.parent.mkdir(parents=True, exist_ok=True)
    md_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")

    lines = [
        "# Claim Check",
        "",
        f"Status: {'ok' if report['ok'] else 'needs attention'}",
        f"Evidence items: {len(report['evidence_ids'])}",
        f"Claims found: {len(report['claims'])}",
        "",
    ]
    sections = [
        ("Malformed Evidence", report["malformed_evidence"]),
        ("Duplicate Evidence IDs", report["duplicate_evidence_ids"]),
        ("Missing Evidence References", report["missing_evidence_ids"]),
        ("Ungrounded Claims", report["ungrounded_claims"]),
    ]
    for title, values in sections:
        if not values:
            continue
        lines.append(f"## {title}")
        for value in values:
            if isinstance(value, dict):
                lines.append(f"- {json.dumps(value, ensure_ascii=False)}")
            else:
                lines.append(f"- {value}")
        lines.append("")
    md_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main() -> int:
    args = parse_args()
    project = Path(args.project).expanduser().resolve()
    evidence_path = project / args.evidence
    ledger_path = project / args.claim_ledger

    evidence, malformed, duplicates = load_evidence(evidence_path)
    files = collect_text_files(project, args.scan)
    refs = scan_references(files)
    claims, ungrounded = scan_claim_ledger(ledger_path)
    known_evidence_ids = set(evidence)
    referenced_evidence_ids = set(refs)
    for claim in claims:
        referenced_evidence_ids.update(claim["evidence_ids"])
    missing = sorted(referenced_evidence_ids - known_evidence_ids)

    report = {
        "ok": not malformed and not duplicates and not missing and not ungrounded,
        "project": str(project),
        "evidence_file": str(evidence_path),
        "claim_ledger": str(ledger_path),
        "evidence_ids": sorted(known_evidence_ids),
        "referenced_evidence_ids": sorted(referenced_evidence_ids),
        "missing_evidence_ids": missing,
        "duplicate_evidence_ids": duplicates,
        "malformed_evidence": malformed,
        "claims": claims,
        "ungrounded_claims": ungrounded,
        "reference_locations": refs,
        "scanned_files": [str(path) for path in files],
    }
    write_reports(project, report, Path(args.out_json), Path(args.out_md))
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
