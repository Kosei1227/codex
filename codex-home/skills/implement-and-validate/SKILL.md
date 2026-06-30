---
name: implement-and-validate
description: "Use when the user wants Codex to own the full implementation loop in a repo: inspect the codebase, make the scoped change, run the relevant install, lint, test, build, or dev commands, and verify the result. Trigger for requests such as 'implement this and make sure it works', 'run npm run dev and check the page', 'fix it end to end', or 'build this and validate the change'. If browser verification is needed, prefer an available in-app browser or computer-use capability, otherwise use the local `playwright` skill when possible."
---

# Implement And Validate

## Overview

Use this skill when Codex should do more than edit code. It should finish the loop by running the appropriate commands, checking the changed behavior, and reporting concrete evidence of success or failure.

## Workflow

1. Confirm the requested scope and avoid broad cleanup that was not asked for.
2. Inspect the repo to find the smallest set of files and commands relevant to the task.
3. Implement the change.
4. Validate with the most targeted checks first, then broaden only as needed.
5. If the task affects a UI or browser flow, verify it visually when the environment allows it.
6. Return a concise result with changed files, commands run, validation status, and any residual risk.

## Command Discovery

Before running commands, inspect the repo for the canonical developer workflow. Prefer repo-defined commands over guessing.

- JavaScript or TypeScript: check `package.json` scripts and lockfiles.
- Python: check `pyproject.toml`, `requirements.txt`, `uv.lock`, `poetry.lock`, `tox.ini`, and test config.
- Rust: check `Cargo.toml`.
- Go: check `go.mod`.
- Mixed repos: follow the package or service local to the task instead of running the whole monorepo blindly.

## Validation Order

Run validation in this order unless the repo clearly dictates otherwise:

1. Dependency install only if required for the requested task.
2. Targeted lint or typecheck nearest to the changed code.
3. Targeted tests nearest to the changed code.
4. Broader test suite only when the targeted checks pass and the repo expects it.
5. Build command for packaging or production safety when applicable.
6. Dev server for tasks that require running the app.

Prefer narrow commands first. For example, a single package test is better than a workspace-wide test run when only one package changed.

## Browser Verification

If the task changes a user-facing flow, verify behavior with a real browser when possible.

- If the Codex app exposes an in-app browser or computer-use capability, use that first.
- Otherwise, if the local `playwright` skill is available, invoke `$playwright` and drive the local app with a headed browser.
- If neither is available, validate with terminal output, test results, screenshots, logs, and build output, and state explicitly that no visual browser verification was performed.

For local browser checks:

1. Start the app with the repo's dev command.
2. Wait for the local URL to become ready.
3. Open the page and verify the changed flow only.
4. Capture a screenshot or equivalent evidence when useful.
5. Stop or clean up background processes when they are no longer needed.

## QA Evidence Loop

For user-facing changes, treat QA as an evidence loop, not a checklist of
commands. Prefer report-only diagnosis before broad fixes when the bug surface
is unclear.

1. Identify the user workflow and expected effect.
2. Exercise the workflow in the closest real environment available.
3. Record the observed effect, console or network errors, screenshots, logs, or test output.
4. Fix only issues tied to observed evidence or an explicit acceptance criterion.
5. Re-run the original workflow and the nearest regression check.

For deeper browser, UX, and regression evidence guidance, load
`references/qa-evidence-rubric.md`.

## Guardrails

- Keep changes scoped to the requested task.
- Do not fix unrelated failures unless they block the requested validation.
- If validation fails because of an unrelated repo issue, report that issue separately and do not misattribute it to the new change.
- If a command is expensive or long-running, prefer the smallest command that gives confidence.
- If the repo requires secrets, external services, or unavailable devices, report the blocker clearly.
- Do not auto-commit, push, merge, deploy, or open external PRs unless the user explicitly requested that action.

## Output Format

At the end of the task, report:

- What changed.
- Which commands were run.
- Whether the change was validated successfully.
- Whether browser verification was performed.
- Any remaining risk, blocker, or manual follow-up.

## Example Triggers

- "Implement this feature and make sure it works."
- "Fix the bug, run the tests, and verify the page."
- "Run `npm run dev` and check whether the UI change is correct."
- "Own this end to end and tell me what still needs manual review."

If the user only wants an explanation, brainstorming, or a plan without code execution, do not use this skill.
