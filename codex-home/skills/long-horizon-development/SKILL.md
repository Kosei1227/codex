---
name: long-horizon-development
description: Use when the user asks Codex to perform long-horizon development, multi-hour implementation, phase completion, artifact-driven validation, stable pipeline work, overnight work, or "do not stop until" tasks. Enforce checkpointed execution, externalized state, strict stop conditions, user-change preservation, non-destructive cleanup, and validation based on real commands, logs, browser runs, or generated artifacts rather than unverified claims.
---

# Long Horizon Development

Use this skill to turn a broad implementation request into a controlled, restartable agent workflow. Long-horizon work is not one giant prompt. It is a loop of small changes, real observations, artifact checkpoints, and explicit acceptance checks.

## Core Rule

Keep the work state outside conversation memory. Record enough concrete state that another Codex session, a subagent, or a human can resume from files, logs, commands, artifact paths, and validation summaries.

## Start Protocol

1. Read the user's latest request and infer the intended outcome.
2. Classify the work as long-horizon if it involves multi-step implementation, phase completion, repeated validation, live browser execution, generated artifacts, migration, graph construction, or a "continue until accepted" instruction.
3. Inspect the local working state before editing:
   - `git status --short`
   - relevant repo instructions such as `AGENTS.md`
   - explicitly named docs, plans, logs, or artifacts
4. Separate existing user changes from changes you will make. Never revert user changes unless explicitly asked.
5. State or write the acceptance condition before substantial work.
6. Identify allowed files, forbidden operations, expected validation, and stop conditions.

When the user has not provided enough detail for a useful acceptance condition, infer a conservative one and label it as an assumption. Ask only if the missing information would make the work unsafe or unusable.

## Work Loop

Run the work as small evidence-backed loops:

1. Form one root-cause or implementation hypothesis.
2. Make the smallest coherent change for that hypothesis.
3. Run the narrowest meaningful validation.
4. Inspect actual output, logs, artifacts, browser state, or generated files.
5. Record what is proven, unproven, and blocked.
6. Continue only when the next step follows from evidence.

Do not accumulate speculative fixes. If local repair attempts fail, diagnose the global cause before adding more patches.

## Ultimate-Goal Mode

When the user explicitly asks for overnight work, phase completion, stable pipeline completion, "do not stop until accepted", or work until an ultimate goal is achieved, switch from ordinary long-horizon mode into ultimate-goal mode.

In ultimate-goal mode:

- Do not finish merely because the next correct step is a major architectural change, large refactor, or detailed plan rewrite.
- Treat repeated validation failure as a signal to diagnose, update the plan, and continue along the evidence-backed global fix.
- If local repairs fail, replace the local strategy with the architecture-level strategy rather than reporting final failure.
- Keep the original acceptance criteria intact. Do not weaken live-execution, artifact-proof, cross-run-stability, or user-specified validation requirements just to finish.
- Use subagents when the user allowed or requested them, especially for independent root-cause lanes, artifact inspection, and architecture-risk review.
- Write durable checkpoints before major pivots so the work remains restartable.

In this mode, only stop for hard blockers: explicit user stop or pause, destructive or irreversible actions, credentials or secrets needed, unsafe live-data risk, lack of permissions, or no defensible next step after evidence collection and root-cause diagnosis.

## Externalized State

For any long run, preserve concrete state identifiers:

- branch and starting `git status`
- changed file list
- command lines and exit codes
- stdout, stderr, audit logs, or browser traces
- artifact paths and IDs
- accepted artifacts and failed artifacts
- validation summary
- remaining blocker and next step

Prefer writing or preserving machine-readable summaries when the workflow already creates them, such as JSON, JSONL, reports, snapshots, screenshots, or manifests.

Use exact names. Avoid phrases like "latest graph", "the last log", "the second run", or "the successful bundle" unless you also provide the actual path or ID.

## Validation Discipline

Do not treat a weaker validation as proof of a stronger claim.

- Passing syntax checks does not prove behavior.
- Passing unit tests does not prove live browser execution.
- Passing plancheck does not prove live execution.
- Creating an artifact does not prove artifact quality.
- One successful run does not prove stability.

Select validation based on the actual acceptance condition. Use tests for debugging and regression protection, but use real artifacts, logs, browser runs, or live execution when those are required by the task.

If validation cannot be run, say exactly why and classify the claim as unproven.

For detailed validation categories, read `references/validation-rubric.md`.

## Checkpoints

Create a checkpoint before and after long commands, live traversal, major implementation phases, cleanup, or risky decisions.

A useful checkpoint contains:

- current goal
- completed step
- next step
- files changed
- commands run
- artifact paths
- proven claims
- unproven claims
- blockers
- whether any stop condition has been reached

For a reusable checkpoint format, read `references/checkpoint-template.md`.

When resuming after context loss, prefer the newest durable checkpoint over
conversation memory. Confirm the branch, dirty state, last validation command,
artifact paths, and next step before editing. If a checkpoint is absent, create
a read-only reconstruction summary before continuing.

## Stop Conditions

For ordinary long-horizon work, stop implementation and switch to a report when:

- the same validation fails twice after meaningful fixes
- the root cause remains unclear after two speculative branches
- the next step needs deletion, credential access, push, deploy, purchase, external posting, or irreversible migration
- the task requires weakening the acceptance condition
- the task requires violating project principles or user preferences
- continuing would overwrite or destroy important artifacts
- live systems or user data could be affected without explicit approval

For ultimate-goal mode, repeated validation failure or a major architectural pivot is not by itself a stop condition. It requires a new diagnosis, updated plan, checkpoint, and continued implementation toward the original acceptance criteria.

Stopping under a hard blocker is not failure. It preserves correctness and makes the next human decision clear.

## Subagents

Use subagents only when the user explicitly asks for subagents, delegation, or parallel agent work.

When subagents are allowed, use them for independent evidence lanes:

- read-only analysis of separate modules
- log or artifact inspection
- root-cause comparison across layers
- bounded code changes with disjoint ownership

Do not delegate the immediate blocker if your next action depends on the answer. Do not assign overlapping write scopes.

## Cleanup Policy

Never permanently delete user files, generated artifacts, graph artifacts, screenshots, logs, configs, or project files by default.

Before cleanup:

1. Identify artifacts required for reproduction.
2. Identify intermediate or failed artifacts.
3. Produce exact paths for cleanup candidates.
4. Ask for confirmation when artifacts are important or ambiguous.
5. Use Recycle Bin, archive, or quarantine rather than permanent deletion.

For cleanup details, read `references/cleanup-policy.md`.

## Prompt Template

When a long-horizon task needs a formal kickoff prompt, use `references/prompt-template.md`.

## Final Report

End long-horizon work with a concise report that separates:

- changed files
- commands run
- artifacts produced
- acceptance checks passed
- unverified claims
- residual risks
- next human decision

Tie every success claim to a command, artifact path, log, screenshot, browser result, or inspection report.
