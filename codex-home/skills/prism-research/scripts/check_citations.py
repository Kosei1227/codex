#!/usr/bin/env python3
"""Check LaTeX citation keys against a BibTeX file."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


CITE_RE = re.compile(
    r"\\(?:cite\w*|autocite|parencite|textcite|nocite)(?:\s*\[[^\]]*\]){0,2}\s*\{([^}]+)\}",
    re.IGNORECASE,
)
BIB_RE = re.compile(r"@\w+\s*\{\s*([^,\s]+)", re.IGNORECASE)
INPUT_RE = re.compile(r"\\(?:input|include)\s*\{([^}]+)\}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", default=".", help="Prism project root.")
    parser.add_argument("--main", default="manuscript/main.tex", help="Main TeX file relative to project.")
    parser.add_argument("--bib", default="manuscript/references.bib", help="BibTeX file relative to project.")
    parser.add_argument("--out-json", default="artifacts/citation_check.json")
    parser.add_argument("--out-md", default="artifacts/citation_check.md")
    return parser.parse_args()


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def collect_tex_files(main: Path) -> list[Path]:
    files = {main.resolve()}
    root = main.parent
    if root.exists():
        files.update(path.resolve() for path in root.rglob("*.tex"))
    return sorted(files)


def extract_citations(tex_files: list[Path]) -> dict[str, list[str]]:
    found: dict[str, list[str]] = {}
    for path in tex_files:
        if not path.exists():
            continue
        text = read_text(path)
        for match in CITE_RE.finditer(text):
            for raw_key in match.group(1).split(","):
                key = raw_key.strip()
                if key:
                    found.setdefault(key, []).append(str(path))
    return found


def extract_bib_keys(bib_path: Path) -> tuple[set[str], list[str]]:
    text = read_text(bib_path) if bib_path.exists() else ""
    keys: list[str] = [match.group(1).strip() for match in BIB_RE.finditer(text)]
    seen: set[str] = set()
    duplicates: list[str] = []
    for key in keys:
        if key in seen and key not in duplicates:
            duplicates.append(key)
        seen.add(key)
    return seen, duplicates


def write_reports(project: Path, report: dict, out_json: Path, out_md: Path) -> None:
    json_path = project / out_json
    md_path = project / out_md
    json_path.parent.mkdir(parents=True, exist_ok=True)
    md_path.parent.mkdir(parents=True, exist_ok=True)
    json_path.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")

    lines = [
        "# Citation Check",
        "",
        f"Status: {'ok' if report['ok'] else 'needs attention'}",
        f"Cited keys: {len(report['cited_keys'])}",
        f"BibTeX keys: {len(report['bib_keys'])}",
        "",
    ]
    if report["missing_bib_keys"]:
        lines.append("## Missing BibTeX Keys")
        lines.extend(f"- {key}" for key in report["missing_bib_keys"])
        lines.append("")
    if report["unused_bib_keys"]:
        lines.append("## Unused BibTeX Keys")
        lines.extend(f"- {key}" for key in report["unused_bib_keys"])
        lines.append("")
    if report["duplicate_bib_keys"]:
        lines.append("## Duplicate BibTeX Keys")
        lines.extend(f"- {key}" for key in report["duplicate_bib_keys"])
        lines.append("")
    md_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def main() -> int:
    args = parse_args()
    project = Path(args.project).expanduser().resolve()
    main_tex = (project / args.main).resolve()
    bib_path = (project / args.bib).resolve()
    tex_files = collect_tex_files(main_tex)

    citations = extract_citations(tex_files)
    bib_keys, duplicate_bib_keys = extract_bib_keys(bib_path)
    cited_keys = set(citations)
    missing = sorted(cited_keys - bib_keys)
    unused = sorted(bib_keys - cited_keys)

    report = {
        "ok": not missing and not duplicate_bib_keys and bib_path.exists(),
        "project": str(project),
        "main": str(main_tex),
        "bib": str(bib_path),
        "bib_exists": bib_path.exists(),
        "tex_files": [str(path) for path in tex_files],
        "cited_keys": sorted(cited_keys),
        "bib_keys": sorted(bib_keys),
        "missing_bib_keys": missing,
        "unused_bib_keys": unused,
        "duplicate_bib_keys": duplicate_bib_keys,
        "citation_locations": citations,
    }

    write_reports(project, report, Path(args.out_json), Path(args.out_md))
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
