#!/usr/bin/env python3
"""Compile a LaTeX manuscript when a local TeX engine is available."""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
from pathlib import Path


AUTO_ENGINES = ["tectonic", "latexmk", "pdflatex", "xelatex", "lualatex"]
MULTIPASS_ENGINES = {"pdflatex", "xelatex", "lualatex"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", default=".", help="Prism project root.")
    parser.add_argument("--main", default="manuscript/main.tex", help="Main TeX file relative to project.")
    parser.add_argument("--engine", default="auto", choices=["auto", *AUTO_ENGINES])
    parser.add_argument("--out-dir", default="artifacts/compile")
    parser.add_argument("--max-runs", type=int, default=3)
    return parser.parse_args()


def choose_engine(requested: str) -> tuple[str | None, dict[str, str | None]]:
    available = {engine: shutil.which(engine) for engine in AUTO_ENGINES}
    if requested != "auto":
        return (requested if available.get(requested) else None), available
    for engine in AUTO_ENGINES:
        if available.get(engine):
            return engine, available
    return None, available


def run_command(command: list[str], cwd: Path) -> dict:
    proc = subprocess.run(command, cwd=str(cwd), text=True, capture_output=True)
    return {
        "command": command,
        "returncode": proc.returncode,
        "stdout": proc.stdout,
        "stderr": proc.stderr,
    }


def command_for(engine: str, main_name: str, out_dir: Path) -> list[str]:
    if engine == "tectonic":
        return ["tectonic", "--outdir", str(out_dir), main_name]
    if engine == "latexmk":
        return ["latexmk", "-pdf", "-interaction=nonstopmode", f"-outdir={out_dir}", main_name]
    return [engine, "-interaction=nonstopmode", "-halt-on-error", "-output-directory", str(out_dir), main_name]


def needs_biblatex(tex: str) -> bool:
    return "\\usepackage{biblatex}" in tex or "\\addbibresource" in tex


def has_bibliography(tex: str, project: Path) -> bool:
    return "\\bibliography" in tex or "\\addbibresource" in tex or (project / "manuscript" / "references.bib").exists()


def write_report(project: Path, out_dir: Path, report: dict) -> None:
    artifacts = project / "artifacts"
    artifacts.mkdir(parents=True, exist_ok=True)
    out_dir.mkdir(parents=True, exist_ok=True)
    (artifacts / "compile_report.json").write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")
    log_parts: list[str] = []
    for run in report.get("runs", []):
        log_parts.append("$ " + " ".join(run["command"]))
        if run.get("stdout"):
            log_parts.append(run["stdout"])
        if run.get("stderr"):
            log_parts.append(run["stderr"])
    (artifacts / "compile_log.txt").write_text("\n\n".join(log_parts), encoding="utf-8")


def main() -> int:
    args = parse_args()
    project = Path(args.project).expanduser().resolve()
    main_tex = (project / args.main).resolve()
    out_dir = (project / args.out_dir).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    engine, available = choose_engine(args.engine)
    if not main_tex.exists():
        report = {
            "ok": False,
            "blocked": True,
            "reason": f"Main TeX file not found: {main_tex}",
            "available_engines": available,
            "runs": [],
        }
        write_report(project, out_dir, report)
        print(json.dumps(report, indent=2, ensure_ascii=False))
        return 1

    if engine is None:
        report = {
            "ok": False,
            "blocked": True,
            "reason": "No supported LaTeX engine found. Install tectonic, latexmk, pdflatex, xelatex, or lualatex.",
            "available_engines": available,
            "runs": [],
        }
        write_report(project, out_dir, report)
        print(json.dumps(report, indent=2, ensure_ascii=False))
        return 1

    tex = main_tex.read_text(encoding="utf-8", errors="replace")
    runs: list[dict] = []
    cwd = main_tex.parent
    main_name = main_tex.name

    if engine in {"tectonic", "latexmk"}:
        runs.append(run_command(command_for(engine, main_name, out_dir), cwd))
    else:
        first = run_command(command_for(engine, main_name, out_dir), cwd)
        runs.append(first)
        if first["returncode"] == 0 and has_bibliography(tex, project):
            aux_stem = out_dir / main_tex.stem
            if needs_biblatex(tex) and shutil.which("biber"):
                runs.append(run_command(["biber", "--output-directory", str(out_dir), str(aux_stem)], cwd))
            elif shutil.which("bibtex"):
                runs.append(run_command(["bibtex", str(aux_stem)], cwd))
        while len([run for run in runs if run["command"][0] in MULTIPASS_ENGINES]) < max(2, args.max_runs):
            previous = runs[-1]
            if previous["returncode"] != 0:
                break
            runs.append(run_command(command_for(engine, main_name, out_dir), cwd))
            if len(runs) >= args.max_runs + 1:
                break

    pdf = out_dir / f"{main_tex.stem}.pdf"
    ok = bool(runs and runs[-1]["returncode"] == 0 and pdf.exists())
    report = {
        "ok": ok,
        "blocked": False,
        "project": str(project),
        "main": str(main_tex),
        "engine": engine,
        "available_engines": available,
        "pdf": str(pdf) if pdf.exists() else "",
        "runs": runs,
    }
    write_report(project, out_dir, report)
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
