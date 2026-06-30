#!/usr/bin/env python3
"""Initialize a local Codex-backed Prism research workspace."""

from __future__ import annotations

import argparse
import json
import shutil
from datetime import date
from pathlib import Path


TEXT_SUFFIXES = {".md", ".tex", ".bib", ".jsonl", ".txt"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--path", required=True, help="Target project directory.")
    parser.add_argument("--title", default=None, help="Project or paper title.")
    parser.add_argument("--date", default=None, help="Project date, defaults to today.")
    parser.add_argument(
        "--allow-existing",
        action="store_true",
        help="Allow an existing directory and copy only missing files.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite existing template files. Use only after reviewing local artifacts.",
    )
    return parser.parse_args()


def render_bytes(path: Path, raw: bytes, replacements: dict[str, str]) -> bytes:
    if path.suffix.lower() not in TEXT_SUFFIXES:
        return raw
    text = raw.decode("utf-8")
    for key, value in replacements.items():
        text = text.replace(key, value)
    return text.encode("utf-8")


def copy_template(src: Path, dst: Path, replacements: dict[str, str], overwrite: bool) -> dict[str, list[str]]:
    created: list[str] = []
    skipped: list[str] = []
    overwritten: list[str] = []

    for source in sorted(src.rglob("*")):
        rel = source.relative_to(src)
        target = dst / rel
        if source.is_dir():
            target.mkdir(parents=True, exist_ok=True)
            continue

        target.parent.mkdir(parents=True, exist_ok=True)
        if target.exists() and not overwrite:
            skipped.append(str(rel))
            continue

        raw = source.read_bytes()
        data = render_bytes(source, raw, replacements)
        if target.exists():
            overwritten.append(str(rel))
        else:
            created.append(str(rel))
        target.write_bytes(data)
        shutil.copystat(source, target)

    return {"created": created, "skipped": skipped, "overwritten": overwritten}


def main() -> int:
    args = parse_args()
    target = Path(args.path).expanduser().resolve()
    skill_root = Path(__file__).resolve().parents[1]
    template = skill_root / "assets" / "project-template"

    if not template.exists():
        raise SystemExit(f"Template directory not found: {template}")

    title = args.title or target.name
    project_date = args.date or date.today().isoformat()

    if target.exists():
        if not target.is_dir():
            raise SystemExit(f"Target exists and is not a directory: {target}")
        has_content = any(target.iterdir())
        if has_content and not args.allow_existing and not args.overwrite:
            raise SystemExit(
                "Target directory is not empty. Re-run with --allow-existing to copy only missing files."
            )
    else:
        target.mkdir(parents=True)

    replacements = {
        "{{TITLE}}": title,
        "{{DATE}}": project_date,
    }
    result = copy_template(template, target, replacements, args.overwrite)
    report = {
        "ok": True,
        "project": str(target),
        "title": title,
        "date": project_date,
        **result,
    }
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
