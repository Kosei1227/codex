# Evidence-First Technical Slide Style Guide

## Source Basis

This guide is distilled from analysis of a 66-slide GUI-agent technical progress deck. Reuse the style principles, not the source deck's branded assets.

Important correction: Matsuo Institute logo, wordmark, copyright, and top-right mark are source-deck-specific artifacts. They are not reusable style preferences.

## Overall Identity

The preferred deck style is internal technical reporting:

* Engineering progress report.
* Validation ledger.
* Architecture memo.
* Benchmark and cost summary.
* Screenshot-based execution proof.
* Roadmap or delivery plan.

The deck should feel grounded in real work. It should not feel like a marketing landing page.

## Reusable Archetypes

### Title Slide

Use a sparse title slide with a large subject title and date or context line. Keep it quiet. Do not add decorative art or inherited source branding unless explicitly requested.

### Roadmap Timeline

Use for schedule or phase gating:

* Month or phase bars across the top.
* Phase boxes underneath.
* Dotted boundary for future or uncertain stages.
* Bottom milestone axis when useful.
* Blue as the primary phase color.

### Schedule Table

Use for workstream delivery planning:

* Left column for workstream or agent role.
* Middle columns for tasks.
* Right side for calendar or Gantt-like blue cells.
* Keep dates and ownership explicit.

### Progress Report Checklist

Use as a recurring navigation/status anchor:

* Dark navy header row.
* Two major columns, usually item and detail.
* Current items in dark text.
* Future or inactive items greyed.
* Checkbox and bullet hierarchy is acceptable when it mirrors the actual work breakdown.

### Accuracy Or Evaluation Table

Use for validation results:

* Show task, success rate, average time, average cost, recall, precision, model, or run count.
* Use red for failed rows, low scores, or critical exceptions.
* Include units. Do not hide cost/time units.
* If table density is high, crop to the important rows or split into appendix.

### Screenshot Walkthrough

Use for UI execution proof:

* Use real screenshots.
* Crop to the relevant region.
* Pair with task text and outcome.
* Use red rectangles for exact UI locations.
* Use colored numbered callouts for ordered steps.
* Do not generate fake screenshots or pseudo-official UI.

### Architecture Or Process Diagram

Use for system reasoning:

* Show responsibility boundaries.
* Show before/after when explaining a fix.
* Show validation loops and failure containment.
* Use simple native shapes, thin connectors, and restrained labels.
* Keep node style plain: white or light grey fill, thin black or grey lines.
* Avoid decorative system diagrams that do not explain a decision.

### Appendix Development Operation Slide

Use for Codex, LLM, or development process guidance:

* Black or dark section bars can be used for headings.
* Grey pill-like labels can be used for principle lists.
* Include benchmark chart, operating constraints, validation loop, and result impact.
* Keep the slide factual and auditable.

## Layout Grammar

Default content-slide layout:

* White canvas.
* Top-left title at roughly 20 pt.
* Bold lead statement directly below the title.
* Light grey lead band when the lead statement needs emphasis.
* Body content begins below the lead band.
* Around 0.5 inches left margin.
* Leave edge breathing room, but do not reserve space for source-deck logos.
* One dominant evidence object per slide where possible.

## Typography

Use a practical sans-serif style:

* Arial-like fonts are acceptable for main content.
* Noto Sans is acceptable for cleaner appendix or dashboard-like slides.
* Monospace such as Roboto Mono is useful for operation catalogs, IDs, code-like examples, prompts, or structured input.
* Bold text is common for lead claims, table headers, key labels, and conclusions.
* Avoid oversized hero type except on title slides.

## Color

Primary palette:

* Black and near-black for main text.
* Grey for secondary text, inactive items, and neutral panels.
* White background.
* Navy for progress headers and strong structural bars.
* Light blue for schedules, selected sections, and positive emphasis.
* Red only for failures, risks, failed rows, and exact UI callouts.

Avoid:

* Purple/blue marketing gradients.
* Beige editorial palettes.
* Decorative background blobs.
* Heavy multi-color palettes without semantic meaning.

## Information Density

High density is acceptable only when it carries proof:

* Dense table of validation results.
* Full task list with outcome metrics.
* Graph topology or architecture dependency map.
* Prompt or task example required to prove the claim.

Do not use high density to avoid thinking. If a slide cannot be read, split it or crop the evidence.

## Language Style

Use concise Japanese technical reporting when working in Japanese:

* Topic-first title.
* Direct lead claim.
* Concrete numbers.
* Specific failure modes.
* Technical English terms left intact when they are natural: Graph, Agent, Planner, Executor, Subflow, Chat UI, validation, deterministic, bounded decision.

Avoid vague claims such as "大幅改善" unless the metric is visible.

## Evidence Rules

For each strong claim, include one of:

* Metric table.
* Run result.
* Screenshot.
* Artifact path.
* Code/runtime fact.
* Citation or source.
* Before/after comparison.

If evidence is missing, write the claim as an assumption, hypothesis, or next validation target.

## Anti-Patterns

Do not:

* Copy source-deck logos, wordmarks, copyright, or brand chrome.
* Use marketing hero layouts for internal technical reports.
* Replace evidence with decorative illustrations.
* Generate fake UI screenshots.
* Use red as decoration.
* Shrink graph labels until unreadable.
* Overlay new content over inherited placeholders.
* Treat a successful command exit as proof of semantic UI success.
* Present reference docs, best practices, and internal execution logs as the same type of evidence.
