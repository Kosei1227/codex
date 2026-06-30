# Prism Artifact Contract

Use this contract when creating, repairing, or validating a Prism workspace.

## Required Layout

```text
PRISM.md
research_question.md
search_strategy.md
corpus/
  papers.jsonl
  sources.md
evidence/
  evidence.jsonl
  evidence_matrix.md
  claim_ledger.md
manuscript/
  main.tex
  sections/
    intro.tex
    related_work.tex
    method.tex
    experiments.tex
    conclusion.tex
  references.bib
reviews/
  literature_review.md
  citation_gaps.md
  reviewer_report.md
artifacts/
  run_log.md
```

Do not permanently delete or overwrite user artifacts. Add new reports under `artifacts/` or `reviews/` unless the user explicitly asks to revise an existing artifact.

## Corpus Schema

`corpus/papers.jsonl` is JSON Lines. Each line should be one paper object:

```json
{"id":"P-001","title":"Paper title","authors":["Author One"],"year":2026,"venue":"unknown","url":"https://example.com","doi":"unknown","arxiv_id":"unknown","bib_key":"unknown","status":"candidate","tags":[],"notes":""}
```

Use these status values when possible:

```text
candidate
included
excluded
background
needs-review
```

If metadata is unknown, write `unknown`. Do not infer metadata from memory.

## Evidence Schema

`evidence/evidence.jsonl` is JSON Lines. Each line should be one evidence object:

```json
{"id":"EV-001","paper_id":"P-001","locator":"section 2","quote":"","paraphrase":"","supports":["CL-001"],"contradicts":[],"certainty":"medium","notes":""}
```

Use `quote` only for short permitted excerpts. Prefer paraphrase plus locator for copyrighted sources. Keep direct quotes within applicable copyright limits.

Use these certainty values when possible:

```text
high
medium
low
unknown
```

## Claim Ledger

`evidence/claim_ledger.md` should contain one claim per substantive literature claim. A compact line format works well:

```text
CL-001 | Claim text | Evidence: EV-001, EV-002 | Status: supported | Notes: short note
```

Use these status values when possible:

```text
draft
supported
contested
weak
blocked
```

A claim without evidence is allowed while drafting, but it must not be presented as established.

## Manuscript

Use `manuscript/main.tex` as the LaTeX entrypoint. Keep section files under `manuscript/sections/`. Keep the bibliography in `manuscript/references.bib` unless the user is adapting a venue template with a different expected path.

## Reports

Generated reports should live under `artifacts/`:

```text
artifacts/citation_check.json
artifacts/citation_check.md
artifacts/claim_check.json
artifacts/claim_check.md
artifacts/compile_report.json
artifacts/compile_log.txt
artifacts/prism_recap.md
artifacts/prism_recap.html
```

Reviewer-facing prose can also be mirrored under `reviews/` when useful, but deterministic script output belongs in `artifacts/`.
