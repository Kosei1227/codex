---
name: overnight-engineer
description: "Use when Codex should run or prepare bounded unattended engineering work, overnight coding sessions, scheduled automations, codex exec jobs, long-running bug fixes, PR-only implementation loops, isolated worktree runs, validation-backed morning reports, or any request to let AI work while the user is away. Coordinates intake, risk bounds, worktree isolation, implementation, validation, reviewer pass, checkpointing, and stop conditions."
---

# Overnight Engineer

Use this skill for unattended or semi-unattended engineering work. The target is a reviewable branch, patch, draft PR, or evidence-backed report. The target is not direct production change.

## Hard Boundaries

1. Work only inside the explicitly chosen repository, branch, or worktree.
2. Prefer `workspace-write` or worktree-isolated execution. Do not use `full_autonomy` or `danger-full-access` unless the user explicitly asks for broad local machine access.
3. Do not deploy, modify secrets, change billing, alter external services, or touch production data during unattended runs.
4. Do not push to protected branches or merge PRs during unattended runs.
5. Do not permanently delete user artifacts, generated evidence, screenshots, logs, graph artifacts, configs, or project files.
6. Do not continue through unclear requirements by guessing product direction. Convert uncertainty into a blocker or a morning question.
7. Do not weaken acceptance criteria, skip validation, or claim success without command output, logs, tests, screenshots, or other concrete evidence.

## Intake

Before starting an unattended run, identify these fields. If the user has not provided enough information for unattended execution, prepare the run plan instead of editing code.

1. Objective and success criteria.
2. Repository path and target branch or worktree policy.
3. Allowed files, modules, or product areas.
4. Forbidden actions and files.
5. Validation commands and expected evidence.
6. Maximum runtime, diff size, or task count.
7. Completion artifact: branch, draft PR, patch, report, or checkpoint.

Use `references/task-intake-template.md` when preparing a reusable task card or task queue item.

## Operating Loop

1. Ground the repo: read local instructions, inspect git status, identify the base branch, and find nearby tests or validation commands.
2. Isolate the work: prefer a Codex worktree, Git worktree, or dedicated branch. If the checkout is dirty with user changes, do not edit over them.
3. Plan the smallest coherent change: define acceptance criteria, write scope, validation path, and stop conditions.
4. Implement in small cycles: avoid broad refactors, dependency changes, generated churn, or formatting-only edits unless explicitly required.
5. Validate with the closest meaningful commands first. For UI work, run browser or screenshot validation when available.
6. Review before handoff: check the diff for unrelated changes, missing tests, architecture drift, data loss risk, and unsupported claims.
7. Report precisely: changed files, validations, failures, blockers, residual risk, and the next human decision.

Coordinate with other skills only when they fit the work:

1. Use `$repo-context-bootstrap` for unfamiliar repositories.
2. Use `$implement-and-validate` for direct implementation loops.
3. Use `$systematic-debugging` for bugs and regressions.
4. Use `$experiment-driven-development` for unclear or risky implementation paths.
5. Use `$architecture-quality` for structural or refactoring-heavy work.
6. Use `$production-audit` before release-sensitive changes.
7. Use `$ai-regression-testing` when AI-written code needs bug-lock tests or contract assertions.

## Stop Conditions

Stop and write a checkpoint when any of these occur:

1. Credentials, secrets, approval, payment, or production access is required.
2. Validation fails twice with the same unresolved cause.
3. The branch is already too broad or mixed to safely extend.
4. The task requires permanent deletion, destructive git operations, deployment, or external side effects.
5. Requirements are ambiguous enough that implementation would encode a product guess.
6. The run exceeds the configured runtime, diff, file-count, or cost budget.

For a blocked stop, include exact commands run, outputs or artifact paths, current hypothesis, changed files, and the safest next step.

## Automation Prompt

When creating a recurring Codex Automation or `codex exec` task for overnight work, read `references/automation-prompt.md` and adapt it to the target repo. Keep the task-specific prompt short, explicit, and bounded.

## Morning Report

When reporting unattended work, read `references/morning-report-template.md`. Always separate confirmed facts, assumptions, validation evidence, blockers, and recommendations.
