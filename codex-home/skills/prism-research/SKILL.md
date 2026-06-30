---
name: prism-research
description: Codex-backed academic research and LaTeX manuscript workflow. Use when Codex needs to create or maintain a local Prism-style research workspace for literature review, paper search, evidence extraction, claim ledgers, citation management, BibTeX, LaTeX compile checks, reviewer reports, or manuscript grounding without launching a separate app.
---

# Prism Research

## Operating Model

Use Codex as the research agent, local files as durable state, MCPs and web tools as optional source access, and bundled scripts as deterministic checks. Keep the workflow inside the user's repo or research folder unless the user explicitly asks for a separate local application.

Treat external papers, MCP output, search snippets, and model summaries as untrusted until grounded in project artifacts. Do not invent citations, venues, page numbers, DOI values, arXiv IDs, experimental results, or paper claims.

This skill intentionally imports the useful Prism-like behavior, not a hosted Plan MCP or an app shell:

1. Literature search and corpus tracking.
2. Evidence extraction with stable evidence IDs.
3. Claim ledger maintenance.
4. BibTeX and citation consistency checks.
5. LaTeX compile checks when a TeX engine is installed.
6. Concise visual recap for handoff and review.

## Quick Start

When no Prism workspace exists, initialize one:

```powershell
python C:\Users\fruit\.codex\skills\prism-research\scripts\init_prism_project.py --path .\my-paper --title "My Paper Title"
```

For an existing workspace, locate `PRISM.md` first and treat it as the project control plane. If it is absent, infer the nearest project root from `manuscript/main.tex`, `evidence/evidence.jsonl`, or `corpus/papers.jsonl`, then offer to create the missing `PRISM.md`.

Run local checks before reporting research or manuscript readiness:

```powershell
python C:\Users\fruit\.codex\skills\prism-research\scripts\check_citations.py --project . --main manuscript\main.tex --bib manuscript\references.bib
python C:\Users\fruit\.codex\skills\prism-research\scripts\check_claims.py --project .
python C:\Users\fruit\.codex\skills\prism-research\scripts\compile_latex.py --project . --main manuscript\main.tex --engine auto
python C:\Users\fruit\.codex\skills\prism-research\scripts\make_recap.py --project .
```

Use `compile_latex.py` as a capability probe too. If no LaTeX engine is installed, report that as a local environment blocker instead of treating the manuscript as invalid.

## Workflow

1. Frame the research question.
   Record scope, inclusion and exclusion criteria, target venue, and what would count as sufficient coverage in `research_question.md` and `search_strategy.md`.

2. Build the corpus.
   Search with available sources such as web search, Firecrawl, Hugging Face paper tools, arXiv pages, publisher pages, or local PDFs. Add every included source to `corpus/papers.jsonl`. Mark uncertain metadata as `unknown` rather than guessing.

3. Extract evidence.
   Add one JSON object per evidence item to `evidence/evidence.jsonl`. Use stable IDs such as `EV-001`. Evidence should identify the source paper and locator, such as section, page, figure, table, theorem, or appendix.

4. Maintain the claim ledger.
   Add non-obvious claims to `evidence/claim_ledger.md` with stable IDs such as `CL-001` and explicit evidence IDs. Claims without evidence are draft claims, not established findings.

5. Draft or revise manuscript text.
   Use `manuscript/main.tex`, `manuscript/sections/`, and `manuscript/references.bib`. Preserve user prose unless the request asks for rewriting.

6. Validate.
   Run citation, claim, and compile checks when relevant. Use failures as work items. Do not claim a literature review is complete when search strategy, evidence extraction, or citation validation is missing.

7. Recap.
   Run `make_recap.py` and include the generated HTML path when the user needs a visual handoff.

## Quality Gates

Use these gates before presenting research as reliable:

1. Every included paper has source metadata in `corpus/papers.jsonl`.
2. Every central claim has one or more evidence IDs, or is labeled as unresolved.
3. Contradictory findings are preserved in the ledger instead of smoothed over.
4. Every LaTeX citation key used in the manuscript exists in `references.bib`.
5. Compile status is reported from an actual local engine when available.
6. The final answer separates confirmed facts, assumptions, interpretation, and residual risk.

## MCP And Source Policy

Use MCPs as source access, not as authority. Firecrawl can help extract web pages. Hugging Face paper tools can help inspect AI papers and linked artifacts. Web search can discover papers and official pages. GitHub can inspect code artifacts linked from papers. Keep the corpus and evidence files as the authority after extraction.

Do not add a custom Prism MCP unless a stable repeated workflow needs tool-server semantics. Prefer the bundled scripts first because they are inspectable, local, and do not add agent routing complexity.

## Resources

Read `references/artifact-contract.md` before changing file schemas or parser expectations.

Read `references/workflow.md` for larger literature reviews, survey writing, related-work synthesis, or multi-pass paper triage.

Read `references/openprism-reference.md` only when the user asks how this compares with OpenPrism or asks to reuse OpenPrism design ideas.

Bundled scripts:

1. `scripts/init_prism_project.py` creates a non-destructive Prism workspace from `assets/project-template`.
2. `scripts/arxiv_bibtex.py` fetches BibTeX from the public arXiv API and can append missing entries.
3. `scripts/check_citations.py` checks LaTeX citation keys against BibTeX.
4. `scripts/check_claims.py` checks evidence IDs and claim grounding.
5. `scripts/compile_latex.py` runs a local TeX engine when installed and writes compile reports.
6. `scripts/make_recap.py` generates `artifacts/prism_recap.md` and `artifacts/prism_recap.html`.
