#!/usr/bin/env python3
"""Fetch BibTeX entries from the public arXiv API."""

from __future__ import annotations

import argparse
import re
import sys
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path


ATOM = "{http://www.w3.org/2005/Atom}"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("ids", nargs="+", help="arXiv IDs or arXiv URLs.")
    parser.add_argument("--append", default=None, help="Append entries to a BibTeX file if missing.")
    return parser.parse_args()


def normalize_arxiv_id(value: str) -> str:
    value = value.strip()
    if "arxiv.org" in value:
        parsed = urllib.parse.urlparse(value)
        value = parsed.path.rstrip("/").split("/")[-1]
    if value.lower().endswith(".pdf"):
        value = value[:-4]
    value = value.replace("arXiv:", "").replace("arxiv:", "")
    if not re.match(r"^[A-Za-z0-9./-]+$", value):
        raise ValueError(f"Invalid arXiv ID: {value}")
    return value


def fetch_entry(arxiv_id: str) -> dict[str, object]:
    url = "https://export.arxiv.org/api/query?id_list=" + urllib.parse.quote(arxiv_id)
    with urllib.request.urlopen(url, timeout=30) as response:
        data = response.read()
    root = ET.fromstring(data)
    entry = root.find(f"{ATOM}entry")
    if entry is None:
        raise RuntimeError(f"No arXiv entry found for {arxiv_id}")

    def text(name: str) -> str:
        node = entry.find(f"{ATOM}{name}")
        return " ".join((node.text or "").split()) if node is not None else ""

    authors = []
    for author in entry.findall(f"{ATOM}author"):
        name = author.find(f"{ATOM}name")
        if name is not None and name.text:
            authors.append(" ".join(name.text.split()))

    published = text("published")
    return {
        "arxiv_id": arxiv_id,
        "title": text("title"),
        "authors": authors,
        "year": published[:4] if published else "unknown",
        "url": text("id"),
    }


def bib_escape(value: str) -> str:
    return value.replace("{", "\\{").replace("}", "\\}")


def bib_key(arxiv_id: str) -> str:
    return "arxiv_" + re.sub(r"[^A-Za-z0-9]+", "_", arxiv_id).strip("_")


def to_bibtex(entry: dict[str, object]) -> str:
    authors = entry["authors"]
    author_text = " and ".join(authors) if isinstance(authors, list) and authors else "unknown"
    arxiv_id = str(entry["arxiv_id"])
    return "\n".join(
        [
            f"@article{{{bib_key(arxiv_id)},",
            f"  title={{{bib_escape(str(entry['title']))}}},",
            f"  author={{{bib_escape(author_text)}}},",
            f"  journal={{arXiv preprint arXiv:{bib_escape(arxiv_id)}}},",
            f"  year={{{bib_escape(str(entry['year']))}}},",
            f"  url={{{bib_escape(str(entry['url']))}}}",
            "}",
        ]
    )


def append_missing(path: Path, entries: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    existing = path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""
    with path.open("a", encoding="utf-8", newline="\n") as handle:
        for entry in entries:
            key_match = re.search(r"@\w+\{([^,]+),", entry)
            key = key_match.group(1) if key_match else ""
            if key and key in existing:
                continue
            if existing and not existing.endswith("\n"):
                handle.write("\n")
            handle.write(entry.rstrip() + "\n\n")
            existing += "\n" + entry


def main() -> int:
    args = parse_args()
    entries: list[str] = []
    for raw in args.ids:
        arxiv_id = normalize_arxiv_id(raw)
        entry = fetch_entry(arxiv_id)
        entries.append(to_bibtex(entry))

    output = "\n\n".join(entries)
    print(output)
    if args.append:
        append_missing(Path(args.append).expanduser().resolve(), entries)
        print(f"Appended missing entries to {args.append}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
