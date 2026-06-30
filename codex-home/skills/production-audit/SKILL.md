---
name: production-audit
description: Perform a local-evidence production readiness audit for apps, services, PRs, and pre-launch changes. Focuses on correctness, security, data integrity, operations, observability, rollback, and concrete ship or block recommendations.
---

# Production Audit

Use this skill when the user asks what could break in production, whether a change is launch-ready, or how to review a PR beyond style and local tests.

## Scope

This is a local-evidence audit. Inspect source files, config, deployment files, tests, logs, docs, and current diffs. Do not send repo data to external audit services. If external docs are needed, use primary sources and cite them.

## When To Use

Use this skill for:

- Pre-launch checks.
- Post-merge risk reviews.
- PRs that touch auth, billing, data writes, migrations, jobs, deployments, browser flows, or LLM runtime behavior.
- "What breaks in prod?" questions.

Do not use this skill for package release readiness only unless the user asks for packaging or distribution review.

## Audit Workflow

1. Identify the changed surface:
   - Git diff against the relevant base when available.
   - Entry points, routes, jobs, migrations, deployment config, and runtime feature flags.
2. Map failure categories:
   - Correctness and edge cases.
   - Security, auth, permissions, secrets, and input validation.
   - Data integrity, idempotency, migrations, and rollback.
   - Operational risk, observability, health checks, and alertability.
   - Performance, latency, rate limits, and cost.
   - User trust and supportability.
   - Runtime LLM contracts when applicable.
3. Verify evidence:
   - Read the source path that actually owns each risk.
   - Distinguish confirmed issue, plausible risk, and unknown.
   - Do not treat build success as proof of production readiness.
4. Produce a ship or block recommendation:
   - Name the highest-severity blockers first.
   - Include exact file paths and commands where useful.
   - Identify the smallest fixes that would change the recommendation.

## Runtime LLM Checks

For products that use LLMs at runtime, check:

- Strict output schemas.
- Allowed IDs or enums for side-effecting choices.
- Confidence, ambiguity, abstain, or block states.
- Evidence references and deterministic validators.
- Traceability of prompt version, model, input digest, raw output, parsed output, and accepted output.
- Fail-closed behavior for missing evidence, unknown IDs, and schema violations.

## Output

Lead with findings. Use severity labels:

- `Blocker`: should not ship until fixed.
- `High`: likely production incident or user harm.
- `Medium`: meaningful risk or maintenance burden.
- `Low`: cleanup or documentation gap.

Then include:

- Ship recommendation.
- Validation reviewed or run.
- Remaining unknowns.
- Smallest next fixes.
