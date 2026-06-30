---
name: agent-introspection-debugging
description: Diagnose repeated AI agent failures using capture, classification, contained recovery, and an evidence-backed introspection report. Use when Codex loops, repeats failed commands, loses the root cause, or burns context without progress.
---

# Agent Introspection Debugging

Use this skill when the agent itself appears to be the failure surface. The goal is to stop the loop, classify the failure, and choose a smaller evidence-backed recovery path.

## When To Use

Use this skill for:

- Repeated tool calls with no new evidence.
- The same command failing multiple times without changed hypothesis.
- Context overflow, stale assumptions, or degraded reasoning.
- Conflicting local state, such as wrong working directory, stale branch, missing files, or changed artifacts.
- Validation loops where action completion is mistaken for product success.

## Operating Rules

1. Pause the failing loop.
2. Capture current evidence before trying another fix.
3. Classify the failure mode.
4. Reduce scope to the next falsifiable check.
5. Do not hide the problem behind broad retries, sleeps, fallback parsing, or new heuristics.
6. Report what changed in the plan.

## Failure Categories

- `wrong-surface`: working in the wrong repo, branch, service, process, browser tab, or file.
- `missing-precondition`: dependency, server, credential, env var, migration, or data fixture is absent.
- `bad-assumption`: the current hypothesis is not supported by source or runtime evidence.
- `tool-loop`: repeated commands or tool calls are not producing new information.
- `context-debt`: too much old context or low-signal output is driving stale decisions.
- `validation-gap`: the validation command does not prove the intended behavior.
- `authority-gap`: an LLM or automation is making a decision that deterministic code, policy, or a human should own.

## Workflow

1. Capture:
   - User goal.
   - Current working directory.
   - Git status or relevant artifact state.
   - Last failing command, tool, or validation.
   - Exact error or mismatch.
2. Classify:
   - Pick one primary failure category.
   - Name any secondary risk.
3. Reframe:
   - State the smallest next check that could falsify the current hypothesis.
   - Identify what file, command, trace, screenshot, or source doc would settle it.
4. Recover:
   - Run one targeted check.
   - Update the plan based on evidence.
   - Continue only if the next action is materially different from the failed loop.
5. Report:
   - Root cause if known.
   - What was unknown.
   - What evidence changed the plan.
   - Current next step or stop condition.

## Output

Use this shape:

```text
Failure category: <category>
Confirmed evidence: <paths, commands, or observed behavior>
Rejected assumption: <assumption that no longer holds>
Next check: <single targeted check>
Recovery action: <what changed in the plan>
Residual risk: <what remains unproven>
```
