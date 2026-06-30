# QA Evidence Rubric

Use this rubric when a task affects UI, browser workflows, generated artifacts, or user-visible behavior.

## Evidence Targets

- User workflow: the exact path a user takes.
- Intended effect: the destination field, row, page state, saved record, rendered output, or external side effect.
- Failure signal: console error, network error, log line, failed assertion, visual mismatch, accessibility issue, or stale state.
- Regression guard: test, screenshot, trace, fixture, replay, or documented manual check.

## Browser And UI Checks

- Verify the final product effect, not only that a button was clicked.
- Capture screenshots when layout, visual state, or generated output matters.
- Check responsive or narrow viewport behavior when the changed UI can wrap, overlap, or hide controls.
- Inspect console and network errors when behavior depends on client-side code.
- Prefer stable selectors and repo-defined test helpers over coordinate clicks.

## Fix Loop

1. Observe and record the bug.
2. Trace it to the likely owner code.
3. Fix the smallest responsible surface.
4. Re-run the original workflow.
5. Add or update the nearest regression check when practical.
6. State what remains manual or unverified.
