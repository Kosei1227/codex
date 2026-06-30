#!/usr/bin/env python3
"""Generate a local Markdown and HTML recap for a Prism workspace."""

from __future__ import annotations

import argparse
import html
import json
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", default=".", help="Prism project root.")
    parser.add_argument("--out-md", default="artifacts/prism_recap.md")
    parser.add_argument("--out-html", default="artifacts/prism_recap.html")
    return parser.parse_args()


def read_text(path: Path, default: str = "") -> str:
    return path.read_text(encoding="utf-8", errors="replace") if path.exists() else default


def load_json(path: Path) -> dict:
    if not path.exists():
        return {}
    try:
        return json.loads(read_text(path))
    except json.JSONDecodeError:
        return {"ok": False, "reason": "report JSON was malformed"}


def count_jsonl(path: Path) -> int:
    if not path.exists():
        return 0
    return sum(1 for line in read_text(path).splitlines() if line.strip())


def status_label(report: dict, missing: str = "not run") -> str:
    if not report:
        return missing
    if report.get("ok"):
        return "ok"
    if report.get("blocked"):
        return "blocked"
    return "needs attention"


def clean_focus(text: str) -> str:
    lines = [line.rstrip() for line in text.splitlines()]
    while lines and not lines[0].strip():
        lines.pop(0)
    if lines and lines[0].lstrip().startswith("#"):
        lines.pop(0)
    return "\n".join(lines).strip()


def write_markdown(project: Path, path: Path, data: dict) -> None:
    lines = [
        "# Prism Recap",
        "",
        f"Project: {project}",
        f"Title: {data['title']}",
        "",
        "## Snapshot",
        "",
        f"- Papers: {data['paper_count']}",
        f"- Evidence items: {data['evidence_count']}",
        f"- Claims: {data['claim_count']}",
        f"- Citation check: {data['citation_status']}",
        f"- Claim check: {data['claim_status']}",
        f"- Compile check: {data['compile_status']}",
        "",
        "## Current Focus",
        "",
        data["research_question"] or "No research question recorded yet.",
        "",
        "## Residual Risk",
        "",
    ]
    risks = data["risks"] or ["No generated risk items. Manual review is still required."]
    lines.extend(f"- {risk}" for risk in risks)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def write_html(project: Path, path: Path, data: dict) -> None:
    cards = [
        ("Corpus", str(data["paper_count"]), "papers tracked"),
        ("Evidence", str(data["evidence_count"]), "evidence items"),
        ("Claims", str(data["claim_count"]), "claims found"),
        ("Citations", data["citation_status"], "key consistency"),
        ("Grounding", data["claim_status"], "evidence coverage"),
        ("Compile", data["compile_status"], "local LaTeX"),
    ]
    card_html = "\n".join(
        f"<section class='card'><h2>{html.escape(title)}</h2><strong>{html.escape(value)}</strong><p>{html.escape(note)}</p></section>"
        for title, value, note in cards
    )
    risk_html = "\n".join(f"<li>{html.escape(risk)}</li>" for risk in data["risks"])
    if not risk_html:
        risk_html = "<li>No generated risk items. Manual review is still required.</li>"

    doc = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Prism Recap</title>
  <style>
    :root {{
      color-scheme: light;
      --ink: #17202a;
      --muted: #5b6472;
      --line: #d9dee7;
      --paper: #f7f7f4;
      --panel: #ffffff;
      --accent: #0f766e;
      --accent-2: #8b5cf6;
      --warn: #b45309;
    }}
    body {{
      margin: 0;
      font-family: Arial, sans-serif;
      background: var(--paper);
      color: var(--ink);
    }}
    main {{
      max-width: 1120px;
      margin: 0 auto;
      padding: 32px 20px 44px;
    }}
    header {{
      border-bottom: 1px solid var(--line);
      padding-bottom: 18px;
      margin-bottom: 22px;
    }}
    h1 {{
      font-size: 32px;
      line-height: 1.15;
      margin: 0 0 8px;
      letter-spacing: 0;
    }}
    .meta {{
      color: var(--muted);
      overflow-wrap: anywhere;
    }}
    .grid {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
      gap: 12px;
      margin: 22px 0;
    }}
    .card {{
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 14px;
      min-height: 116px;
    }}
    .card h2 {{
      font-size: 13px;
      text-transform: uppercase;
      color: var(--muted);
      margin: 0 0 12px;
      letter-spacing: 0;
    }}
    .card strong {{
      display: block;
      font-size: 22px;
      line-height: 1.2;
      color: var(--accent);
      overflow-wrap: anywhere;
    }}
    .card p {{
      margin: 8px 0 0;
      color: var(--muted);
      font-size: 13px;
    }}
    .band {{
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 18px;
      margin-top: 14px;
    }}
    .band h2 {{
      margin: 0 0 10px;
      font-size: 18px;
    }}
    .flow {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(130px, 1fr));
      gap: 10px;
    }}
    .step {{
      border-left: 4px solid var(--accent-2);
      background: #fbfbff;
      padding: 10px;
      min-height: 64px;
    }}
    ul {{
      margin: 0;
      padding-left: 20px;
    }}
  </style>
</head>
<body>
  <main>
    <header>
      <h1>{html.escape(data['title'])}</h1>
      <div class="meta">{html.escape(str(project))}</div>
    </header>
    <section class="grid">
      {card_html}
    </section>
    <section class="band">
      <h2>Research Question</h2>
      <p>{html.escape(data['research_question'] or 'No research question recorded yet.')}</p>
    </section>
    <section class="band">
      <h2>Workflow</h2>
      <div class="flow">
        <div class="step">Question</div>
        <div class="step">Corpus</div>
        <div class="step">Evidence</div>
        <div class="step">Claims</div>
        <div class="step">Manuscript</div>
        <div class="step">Validation</div>
      </div>
    </section>
    <section class="band">
      <h2>Residual Risk</h2>
      <ul>{risk_html}</ul>
    </section>
  </main>
</body>
</html>
"""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(doc, encoding="utf-8")


def main() -> int:
    args = parse_args()
    project = Path(args.project).expanduser().resolve()
    prism = read_text(project / "PRISM.md")
    title = "Prism Research Workspace"
    for line in prism.splitlines():
        if line.startswith("# "):
            title = line[2:].strip()
            break

    citation_report = load_json(project / "artifacts" / "citation_check.json")
    claim_report = load_json(project / "artifacts" / "claim_check.json")
    compile_report = load_json(project / "artifacts" / "compile_report.json")
    risks: list[str] = []
    if status_label(citation_report) != "ok":
        risks.append("Citation check is not clean.")
    if status_label(claim_report) != "ok":
        risks.append("Claim grounding check is not clean.")
    if status_label(compile_report) != "ok":
        risks.append("Compile check is not clean or has not run successfully.")

    data = {
        "title": title,
        "paper_count": count_jsonl(project / "corpus" / "papers.jsonl"),
        "evidence_count": count_jsonl(project / "evidence" / "evidence.jsonl"),
        "claim_count": len(claim_report.get("claims", [])) if claim_report else 0,
        "citation_status": status_label(citation_report),
        "claim_status": status_label(claim_report),
        "compile_status": status_label(compile_report),
        "research_question": clean_focus(read_text(project / "research_question.md")),
        "risks": risks,
    }
    md_path = project / args.out_md
    html_path = project / args.out_html
    write_markdown(project, md_path, data)
    write_html(project, html_path, data)
    print(json.dumps({"ok": True, "markdown": str(md_path), "html": str(html_path)}, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
