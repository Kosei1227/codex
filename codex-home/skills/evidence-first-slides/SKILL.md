---
name: evidence-first-slides
description: "Evidence-first technical presentation style for PowerPoint, Google Slides-targeted decks, slide generation, slide editing, deck polishing, progress reports, architecture decks, validation summaries, AI-agent or GUI-agent project reports, benchmark slides, screenshot walkthroughs, and dense internal engineering presentations. Use with the standard presentations skill when Codex needs to create or edit slides in the user's preferred technical report style: compact titles, direct lead claims, tables, real screenshots, metrics, validation evidence, restrained colors, and no inherited source-deck logos unless explicitly supplied."
---

# Evidence First Slides

## Core Rule

Use this skill to steer slide judgment, not to replace the standard `$presentations` implementation workflow. When creating or editing a deck, first follow the `$presentations` skill for artifact-tool authoring, template following, rendering, and QA. Apply this skill as the user's house style for technical decks.

If the user supplies a brand template or reference deck, preserve that template's required layout and assets. If the only reference is the analyzed GUI-agent deck, reuse the evidence-first structure and rhythm but do not copy Matsuo Institute logos, wordmarks, copyright text, or branded chrome.

## Style Goal

Build internal technical report decks that make claims auditable. Prefer concrete evidence over decorative polish:

* State the main claim near the top of the slide.
* Show the evidence that proves or qualifies the claim on the same slide when possible.
* Use real screenshots, tables, task examples, benchmark numbers, cost/time/success metrics, and architecture/process diagrams.
* Keep visual polish restrained: consistency, alignment, rhythm, and readable density.
* Avoid marketing heroes, decorative gradients, stock imagery, abstract illustrations, and vague executive copy.

## Required Workflow

1. Identify the deck purpose: progress report, architecture explanation, validation summary, benchmark report, screenshot walkthrough, roadmap, appendix, or mixed deck.
2. Choose slide archetypes from `references/style-guide.md`.
3. For each slide, write a lead claim before designing details.
4. Pair every strong claim with evidence: metric, table row, screenshot callout, artifact path, code/runtime fact, or cited source.
5. Render and inspect all slides. Fix overlap, clipped text, unreadable table rows, accidental branding, and unsupported claims before delivery.

## Composition Rules

Use compact report-deck composition:

* White background.
* Top-left slide title.
* Bold lead statement under the title, often in a light grey band.
* One dominant evidence object per slide where possible: table, screenshot, process diagram, roadmap, or benchmark panel.
* Dense content is acceptable only when the density is evidence.
* Split a slide when density makes the proof unreadable.
* Prefer functional splits: before vs after, problem vs fix, current vs target, screenshot vs explanation, benchmark vs operating principle.

## Typography And Color

Default to the analyzed deck's restrained technical look unless the user supplies another template:

* Title: compact, approximately 20 pt, top-left.
* Lead statement: bold, approximately 12 to 14 pt, one to three lines.
* Body: 10 to 14 pt. Use smaller labels only for dense diagrams where still readable.
* Use black, near-black, grey, white, navy, and light blue as the dominant palette.
* Use red sparingly for failures, risks, failed rows, and screenshot callout rectangles.
* Use blue for selected sections, schedule/status emphasis, roadmap elements, and constructive emphasis.
* Use grey for secondary context, inactive items, neutral explanation panels, and lead bands.

## Evidence Discipline

Do not overstate. Separate confirmed facts from interpretation.

* Strong language requires visible evidence.
* If a result is directional, say it is directional.
* If a slide is based on a run, include the run/date/model/cost/time/success surface when useful.
* For runtime LLM or graph-agent slides, separate semantic LLM decisions, deterministic validation, planner/compiler/runtime boundaries, and UI effect evidence.
* Real screenshots are evidence. Do not replace them with generated or fake UI approximations.

## Branding Boundary

Do not reuse Matsuo Institute logo, wordmark, copyright text, top-right mark, or branded chrome from the analyzed deck unless the user explicitly requests that exact brand treatment or provides a template that requires it.

Use a generic, unobtrusive footer or page marker only when the deck context needs one.

## Reference

Read `references/style-guide.md` when designing or evaluating a deck in this style. It contains the slide archetypes, reusable preferences, and anti-patterns distilled from the analyzed GUI-agent deck.
