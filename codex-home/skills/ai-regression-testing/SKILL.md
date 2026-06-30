---
name: ai-regression-testing
description: Design regression tests for AI-assisted code changes, especially where the same model may write and review code. Focuses on bug-lock tests, sandbox or mock parity, contract assertions, and blind spots that ordinary review can miss.
---

# AI Regression Testing

Use this skill when a change was made by an AI agent, when a recurring bug has been fixed, or when review alone is not enough proof that the same failure will not return.

## When To Use

Use this skill for:

- Bugs that were fixed after an AI-generated or AI-assisted change.
- API routes, background jobs, browser flows, or LLM workflows where shape drift is likely.
- Sandbox, mock, fixture, or test-mode behavior that must stay equivalent to production behavior.
- Cases where the author and reviewer may share the same blind spot.

Do not use this skill to chase generic coverage percentages. The goal is targeted regression prevention.

## Core Principle

Turn the discovered failure into an executable contract. The test should fail against the old bug and pass against the fixed behavior.

## Common AI Blind Spots

- Sandbox path and production path return different shapes.
- New response fields are added in one code path but not another.
- Database `select` lists miss newly expected columns.
- Optimistic UI updates do not roll back on failure.
- Error state leaves stale data visible.
- Retry logic hides a deterministic failure.
- Browser automation confirms a click but not the intended product effect.
- LLM output is accepted without schema, allowed IDs, confidence, or evidence validation.
- New enum, status, tier, route, action, or provider values are added without updating every consumer, filter, display, persistence, and validation path.
- Review accepts "tests pass" without a bug-lock assertion for the exact field, row, event, state transition, UI destination, or side effect that failed.

## Workflow

1. Reconstruct the bug:
   - Identify the exact input, state, command, request, or UI action that failed.
   - Identify the expected observable output.
   - Locate the source path responsible for the behavior.
2. Choose the test boundary:
   - Unit test for pure logic.
   - Contract test for API shape or structured output.
   - Integration test for cross-module state.
   - E2E test when only browser-visible behavior proves the fix.
3. Write the smallest regression test:
   - Assert the field, state, event, row, file, or UI effect that was previously wrong.
   - Prefer deterministic fixtures over sleeps or broad retries.
   - For LLM-integrated behavior, validate schema failures, ambiguous output, missing evidence, and unknown IDs.
   - For enum, API, schema, or status changes, assert all sibling values and every newly added value at the consumer boundary that would have missed it.
4. Run the closest meaningful validation command.
5. Report whether the test would have caught the original bug.

## Review-Derived Contracts

When a review finds SQL risk, race risk, shell injection, unsafe LLM output,
API shape drift, migration risk, or enum incompleteness, convert the finding
into one executable contract where feasible. The preferred test is the one that
would fail on the original diff, not the one that merely increases coverage.

## Sandbox Or Mock Parity

When a project has sandbox or mock mode, compare it to the production contract:

- Same required fields.
- Same error semantics.
- Same authorization and validation checks where applicable.
- Same persistence or side-effect boundary, or an explicit documented difference.

Do not make test mode more permissive than production unless the difference is intentional and documented.

## Output

Report:

- The regression risk being locked down.
- The test file and assertion added or recommended.
- The validation command run.
- Whether the test proves the intended behavior or only narrows risk.
