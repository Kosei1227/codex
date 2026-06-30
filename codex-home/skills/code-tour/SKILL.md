---
name: code-tour
description: Create CodeTour `.tour` files with persona-targeted walkthroughs, real file anchors, and verification against the current repo. Use for onboarding tours, architecture walkthroughs, PR tours, RCA tours, and structured codebase explanations.
---

# Code Tour

Use this skill when the user wants a navigable walkthrough of a real codebase rather than a prose explanation. The output is a CodeTour `.tour` file under `.tours/` with steps anchored to actual files, directories, lines, patterns, or URLs.

## When To Use

Use this skill for:

- Onboarding a new engineer to a repo, service, module, or workflow.
- Explaining a PR, incident root cause, architecture decision, or runtime path.
- Creating a guided walkthrough that should be reusable outside the current chat.
- Turning "explain how this works" into a concrete artifact with source anchors.

Do not use this skill when the user only needs a short answer, a code review, or an implementation patch.

## Operating Rules

1. Inspect the actual repo before designing the tour.
2. Pick a persona and scope, such as backend maintainer, frontend engineer, reviewer, operator, or new joiner.
3. Keep tours focused. Prefer 6 to 12 steps unless the user asks for a deep walkthrough.
4. Anchor every step to a real file, directory, line, pattern, or external URL.
5. Verify that referenced local files exist before writing the tour.
6. Do not invent architecture. If a path is uncertain, label it as an assumption or leave it out.

## Tour Structure

Create files at:

```text
.tours/<persona>-<focus>.tour
```

Use JSON compatible with the CodeTour format:

```json
{
  "$schema": "https://aka.ms/codetour-schema",
  "title": "Payment Flow Tour",
  "description": "A source-anchored walkthrough of how payment requests move through the service.",
  "steps": [
    {
      "file": "src/server.ts",
      "line": 12,
      "title": "Application Entry",
      "description": "The server starts here and wires the route modules."
    }
  ]
}
```

Valid step anchors include:

- `file` with optional `line`
- `directory`
- `pattern`
- `uri`

## Workflow

1. Discover entry points:
   - Read `README`, manifests, route files, package or service entry points, and repo-local `AGENTS.md`.
   - Use `rg` to trace named symbols, route handlers, event handlers, jobs, or config keys.
2. Select the narrative:
   - Name the target audience.
   - Identify the starting point, main flow, important branches, and ending condition.
3. Build the tour:
   - Use short, concrete step titles.
   - Explain why each anchor matters.
   - Mention local risks or invariants only when visible in source.
4. Validate:
   - Confirm every local path exists.
   - Confirm line anchors still point near the intended code.
   - Ensure the JSON parses.

## Output

Report:

- The created `.tour` file path.
- The persona and workflow covered.
- Any uncertain or omitted area that would need more repo evidence.
