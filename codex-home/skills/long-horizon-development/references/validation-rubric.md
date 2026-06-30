# Validation Rubric

Choose validation based on the acceptance claim.

## Validation Levels

- Syntax validation: proves files parse or compile at a basic level.
- Static validation: proves type, lint, formatting, or schema contracts.
- Unit tests: prove local function or module behavior.
- Integration tests: prove module boundaries or service contracts.
- Build: proves packaging, bundling, or typegraph consistency.
- Dry run: proves command wiring and argument parsing.
- Plancheck: proves an execution plan is coherent before running it.
- Live execution: proves behavior against the real app, browser, service, or workflow.
- Artifact inspection: proves generated outputs match the intended structure and quality.
- Repeated run comparison: proves stability across independent executions.

## Invalid Claim Upgrades

Do not upgrade claims across levels without evidence:

- Syntax success does not prove runtime behavior.
- Unit tests do not prove live execution.
- Plancheck does not prove execution.
- Artifact existence does not prove artifact quality.
- One successful run does not prove stability.

## Final Acceptance

A final acceptance report must name:

- validation command or live action
- exit status or observed result
- artifact path or log path
- remaining unverified areas

If final validation cannot run, mark the task as incomplete or blocked.
