# Plan Hardening Checklist

Use this checklist before implementing non-trivial architecture, data, API, workflow, UI system, or runtime LLM changes.

## Required Passes

- Data flow: source, transformation, storage, side effects, output, and ownership.
- State machine: allowed states, invalid states, transitions, retries, idempotency, and recovery.
- Trust boundary: user input, auth, permissions, external APIs, files, shell, browser, LLM output, and generated artifacts.
- Contract surface: public APIs, schemas, prompts, events, storage keys, config keys, flags, and exported types.
- Failure behavior: timeout, partial success, duplicate action, stale state, low confidence, missing dependency, and rollback.
- Test matrix: unit, contract, integration, migration, browser, negative path, and replay or trace checks.

## Decision Rules

- Do not leave hard-to-reverse choices implicit.
- Use existing repo boundaries unless they are the source of the risk.
- Add an abstraction only when it protects a real variation or reduces real coupling.
- Prefer deterministic validation for boundaries and bounded LLM calls only for semantic decisions.
- If the plan cannot name validation evidence, it is not ready to implement.

## Review Output

Return:

- Architecture shape.
- Key contracts.
- Risky transitions or trust boundaries.
- Tests and validation needed.
- Overengineering risk.
- Open decisions requiring user input.
