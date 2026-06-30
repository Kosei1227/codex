# Engineering Rubric

Load this reference when a task needs a quality gate, handoff, review, or long-horizon checkpoint.

Score each item from 0 to 2:

0 means missing or unsafe.
1 means partially handled.
2 means handled with concrete evidence.

## Outcome Fit

Check whether the work satisfies the user's real goal, not only the literal text.

Score 2 when:

1. Acceptance criteria are explicit or reasonably inferred.
2. Non-goals and user constraints are respected.
3. The chosen scope is neither too narrow to be useful nor too broad to be safe.

## Context Grounding

Check whether decisions came from the real repo, environment, or source material.

Score 2 when:

1. Relevant instructions, configs, entrypoints, tests, and existing patterns were inspected.
2. Factual claims are either verified or clearly labeled as assumptions.
3. Current external facts were checked from authoritative sources when needed.

## Architecture Judgment

Check whether the design optimizes medium-term product quality.

Score 2 when:

1. The implementation fits existing boundaries.
2. It avoids unnecessary abstractions.
3. Tradeoffs in correctness, maintainability, security, latency, cost, and operations were considered.

## Implementation Scope

Check whether edits are coherent and contained.

Score 2 when:

1. Files changed are directly tied to the goal.
2. User edits and generated artifacts are preserved.
3. No unrelated cleanup or accidental behavior change is mixed in.

## Runtime LLM Integration

Use this category only when the product itself calls an LLM at runtime.

Score 2 when:

1. Each LLM call has a named component role.
2. Authority, input trust, output contract, validation, fallback, evals, and observability are explicit.
3. Code owns permissions, identity, schemas, allowed actions, side effects, and final enforcement.

## Validation Strength

Check whether evidence proves the changed behavior.

Score 2 when:

1. Validation is the closest meaningful command or artifact check.
2. UI, document, graph, or generated artifact changes are visually or structurally inspected where appropriate.
3. Failures are attributed accurately and not hidden.

## Autonomy Safety

Check whether Codex used initiative without crossing boundaries.

Score 2 when:

1. Codex proceeded without unnecessary questions on reversible local work.
2. Codex stopped before destructive, costly, credentialed, or irreversible actions.
3. Checkpoints were written or reported for long work.

## Reporting Quality

Check whether the final answer lets the user act.

Score 2 when:

1. Changed files are named exactly.
2. Validation commands and results are stated.
3. Remaining risk, blockers, or follow-up are concrete.

## Pass Rule

For normal implementation, require no zero scores in outcome fit, context grounding, implementation scope, and validation strength.

For architecture-sensitive or runtime LLM work, also require no zero scores in architecture judgment and runtime LLM integration.

For unattended work, also require no zero score in autonomy safety.
