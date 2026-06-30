---
name: html-artifact
description: "Create self-contained HTML artifacts that communicate richer information than Markdown through layout, color, tables, SVG diagrams, annotated code, and optional lightweight interaction. Use when Codex should produce an implementation blueprint, architecture explainer, report, PR review artifact, design exploration, side-by-side comparison, prototype, or throwaway editor that is easier to read, review, or share in a browser."
---

# HTML Artifact

## Overview

Use this skill to turn dense plans, reports, explainers, or comparisons into browser-readable HTML instead of long Markdown. Default to a single self-contained `.html` file with inline CSS, inline SVG, and only the minimum JavaScript needed for clarity or interaction.

## Output Contract

Default to these constraints unless the user asks otherwise:

1. Produce a single HTML file that opens locally without a build step.
2. Inline CSS and JavaScript. Avoid external CDNs, fonts, or frameworks.
3. Optimize for one-pass comprehension rather than raw completeness.
4. Use real visual structure: panels, callouts, comparison grids, diagrams, timelines, or tabs when they materially improve readability.
5. Keep interaction lightweight and purposeful. If nothing needs interaction, keep it static.
6. Make it responsive enough to read on laptop and mobile widths.
7. Preserve the repo or product visual language when working from an existing design system. Otherwise choose a clean, intentional style rather than generic defaults.

## Workflow

### 1. Classify the artifact

Choose the lightest artifact shape that fits the request:

- Implementation blueprint
- Report or explainer
- PR review or code walkthrough
- Design exploration or side-by-side comparison
- Prototype or animation playground
- Throwaway editor with export actions

If the request is ambiguous, infer the most likely artifact shape from the user's goal and state the assumption briefly.

For pattern selection and section recipes, read `references/artifact-patterns.md`.

### 2. Gather source material

Before writing HTML:

1. Read the code, notes, diffs, plans, or research that should appear in the artifact.
2. Extract only the evidence needed to support the artifact's claims.
3. Separate confirmed facts from assumptions, recommendations, and open questions.
4. Prefer exact snippets, labels, IDs, commands, or paths when they improve trust.

Do not invent architecture, product behavior, or data flow details just to fill space.

### 3. Design the reading experience

Structure for scanning first, depth second:

1. Put the highest-value summary near the top.
2. Group related content into visually distinct sections.
3. Use side-by-side layouts for comparisons and tradeoffs.
4. Use SVG for flows, architecture, timelines, dependency maps, and process diagrams.
5. Use code blocks with annotations when explaining implementation details.
6. Add jump navigation only when the artifact is long enough to need it.

Prefer dense but readable composition over long vertical prose.

### 4. Build the artifact

When generating the HTML:

1. Use semantic HTML.
2. Define CSS variables for color, spacing, radius, and typography.
3. Keep styling intentional and legible. Do not rely on plain browser defaults.
4. Keep JavaScript small, local, and inspectable.
5. If interaction exists, make the state visible and reversible.
6. If the artifact is an editor or playground, include an explicit export action such as copy as JSON, copy as Markdown, or copy prompt.

### 5. Check quality before delivery

Review the file as a document, not only as code:

1. Confirm the hierarchy is obvious at a glance.
2. Confirm colors and emphasis encode meaning consistently.
3. Confirm diagrams are readable without zooming on a normal laptop width.
4. Confirm code snippets are relevant and not decorative.
5. Confirm every interactive control has a visible purpose.
6. Confirm the file still makes sense with JavaScript disabled unless interaction is essential.

For the detailed checklist, read `references/html-quality-checklist.md`.

## Artifact-Specific Guidance

### Implementation blueprints

Bias toward decision support and execution clarity:

1. Include the goal, scope, constraints, and acceptance criteria.
2. Show architecture or data flow visually.
3. Call out files, modules, APIs, or services likely to change.
4. Include a rollout or validation plan when relevant.
5. Show code snippets only where they clarify the plan.

### Reports and explainers

Bias toward evidence and synthesis:

1. Start with the key finding or takeaway.
2. Show the supporting evidence with charts, timelines, callouts, or diagrams.
3. Separate facts, interpretation, and recommendation.
4. Keep long source dumps out of the main reading flow.

### PR review and code understanding

Bias toward comprehension of the change:

1. Focus on the riskier or less obvious parts of the diff.
2. Use severity-colored annotations sparingly and consistently.
3. Explain control flow, backpressure, ownership, or state transitions visually when the raw diff is hard to parse.
4. Keep findings tied to exact files, code blocks, or behaviors.

### Design explorations and comparisons

Bias toward contrast:

1. Show multiple distinct options in one frame when comparison is the goal.
2. Label each option with its tradeoff, tone, or product bet.
3. Avoid six variants that all feel the same.
4. Prefer visible contrast in layout, density, typography, and interaction.

### Throwaway editors and playgrounds

Bias toward user control and export:

1. Build only the controls needed for this one decision.
2. Keep the UI local and self-contained.
3. End with a copy or export button that converts the edited state back into a prompt, JSON diff, Markdown summary, or other reusable text.
4. Make dependencies and invalid combinations visible if they matter.

## Reference Files

- Read `references/artifact-patterns.md` when choosing sections or interaction patterns for a specific artifact type.
- Read `references/html-quality-checklist.md` before finishing an artifact that will be shared, reviewed, or used as a decision document.
