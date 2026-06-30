# Prism Research Workflow

Use this workflow for literature reviews, related-work sections, survey drafts, and paper-grounded manuscript edits.

## 1. Research Frame

Record these decisions before broad search:

1. Research question.
2. Target field and venue expectations.
3. Inclusion and exclusion criteria.
4. Time range.
5. Required source types, such as peer-reviewed papers, arXiv preprints, official datasets, repositories, benchmarks, or standards.
6. Definition of done for coverage.

If the user gives a vague topic, create a narrow first pass and label it as a working scope.

## 2. Search Strategy

Track queries in `search_strategy.md`. For each source, record:

1. Query string.
2. Source searched.
3. Date searched.
4. Inclusion rule.
5. Exclusion rule.
6. Notes about likely blind spots.

For negative claims, such as "no prior work does X", record the exact search path and uncertainty. Prefer "I did not find evidence under this search strategy" over categorical absence.

## 3. Corpus Triage

Add every candidate to `corpus/papers.jsonl`. Do not rely on chat history as the corpus. For each paper, set `status` to `candidate`, `included`, `excluded`, `background`, or `needs-review`.

Use exclusion notes for papers that are close but out of scope. These notes are useful when the user later asks why a paper was omitted.

## 4. Evidence Extraction

Extract evidence into `evidence/evidence.jsonl` before writing strong claims. Each evidence item should have:

1. Stable evidence ID.
2. Paper ID.
3. Locator.
4. Short quote only when allowed.
5. Paraphrase.
6. Supported or contradicted claim IDs.
7. Certainty.

When a paper conflicts with another paper, keep both evidence items and mark the claim as contested.

## 5. Synthesis

Use `evidence/claim_ledger.md` as the bridge between evidence and prose. For each claim, identify:

1. Claim text.
2. Evidence IDs.
3. Status.
4. Scope limit.
5. Known counter-evidence.

Only then draft the related-work or literature-review prose.

## 6. Citation And BibTeX

Use `scripts/arxiv_bibtex.py` for arXiv entries when the source is on arXiv. For publisher papers, prefer official BibTeX from the publisher or DOI metadata when available.

After editing LaTeX, run `scripts/check_citations.py`. Fix missing and duplicate keys before reporting manuscript readiness.

## 7. LaTeX Compile Loop

Run `scripts/compile_latex.py`. If no engine is installed, report the environment blocker. If compilation fails, use the log in `artifacts/compile_log.txt`, make the smallest fix, and rerun.

Do not replace a semantic review with compile success. Compile success proves syntax and build environment only.

## 8. Review And Recap

Run `scripts/check_claims.py` and `scripts/make_recap.py`. Use the recap to explain:

1. Corpus size.
2. Evidence count.
3. Claim grounding status.
4. Citation status.
5. Compile status.
6. Residual risks.

For a handoff, include the path to `artifacts/prism_recap.html`.
