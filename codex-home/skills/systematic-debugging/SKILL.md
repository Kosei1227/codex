---
name: systematic-debugging
description: "Use when the user reports a bug, regression, flaky test, incorrect behavior, production issue, or unexplained failure and wants a root-cause-focused fix. This skill forces Codex through a four-phase debugging process: reproduce, narrow, explain, and fix with validation."
---

# Systematic Debugging

## Overview

Use this skill to debug without thrashing. It prevents speculative fixes by requiring a reproducible symptom, a narrowed failure surface, a causal explanation, and a validated fix.

## When to Use

- Test failures with unclear cause.
- UI or API regressions.
- Production bugs reproduced from logs or user reports.
- Race conditions, flaky behavior, or state corruption.
- Cases where "just patch it" would likely hide the real issue.

## Four Phases

### 1. Reproduce

- Capture the exact symptom first.
- Identify the precise command, request, action, or scenario that shows the failure.
- If the issue cannot be reproduced, state what evidence exists and what is still missing.

### 2. Narrow

- Reduce the failure to the smallest meaningful scope.
- Identify the code path, state transition, dependency, or input shape involved.
- Use logs, targeted tests, instrumentation, and focused reads before making broad edits.

### 3. Explain

- Write a one-sentence root cause that connects symptom to mechanism.
- The explanation must be falsifiable and backed by evidence.
- If there are multiple plausible causes, rank them and test the strongest one first.

### 4. Fix and Guard

- Apply the smallest fix that addresses the actual cause.
- Add or update validation so the same failure would be caught again.
- Re-run the original repro and the nearest regression checks.

## Preferred Tools

- Repro commands and targeted tests.
- Stack traces, logs, and request traces.
- Grep or code search to trace ownership.
- Temporary instrumentation when necessary.
- Browser validation for UI bugs.

## Debugging Rules

- Do not fix before you can explain.
- Do not collapse several theories into one patch.
- Prefer one strong theory plus one confirming experiment.
- Keep instrumentation cheap and remove it if it is not part of the final fix.
- If the reported bug is actually a requirement mismatch, say so clearly.
- If two fixes fail against the same symptom, stop patching and re-open the investigation at the boundary map: caller, callee, state, persistence, external dependency, and validation target.
- Separate action completion from semantic success. For UI, browser, graph, and agent workflows, verify the intended product effect, not only that a click, command, or tool call completed.

## Investigation Notes

Maintain a small hypothesis log for difficult bugs:

- Symptom and reproduction.
- Current strongest hypothesis.
- Evidence that supports it.
- Evidence that would falsify it.
- Experiment run and result.
- Next narrowed step.

Use this log in the final report when the path was non-obvious or previous attempts failed.

## Validation Requirements

Before signoff, show evidence for:

- The original failure mode.
- The root cause.
- The exact fix.
- The post-fix validation.
- Any remaining edge cases or uncertainty.

## Anti-Patterns

- Guessing from code without reproducing the issue.
- Fixing a symptom while leaving the trigger untouched.
- Broad cleanup bundled into the debug patch.
- Using "works on my machine" as final validation.
- Reporting a likely cause as confirmed when it was not tested.

## Example Triggers

- "Debug this failing test without guessing."
- "Find the root cause of this regression."
- "Why is this endpoint timing out sometimes?"
- "Track down this UI bug and verify the actual fix."
