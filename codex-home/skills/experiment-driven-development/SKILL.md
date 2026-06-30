---
name: experiment-driven-development
description: "Use when the task is ambiguous, exploratory, or likely to require multiple attempts, such as unclear bugs, risky refactors, performance work, or features where the right implementation path is not obvious. This skill keeps Codex in a disciplined loop of hypothesis, small experiment, evidence, and adjustment instead of making large speculative edits."
---

# Experiment Driven Development

## Overview

Use this skill to handle tasks where the first solution is unlikely to be the right one. It forces small, evidence-driven iterations so progress stays measurable and mistakes stay cheap.

## When to Use

- The user wants a bug fixed but the root cause is unclear.
- The feature has multiple plausible implementations and no obvious best path.
- A refactor, migration, or optimization is risky and should be validated in stages.
- The task benefits from learning through targeted experiments instead of one large change.

## Core Loop

For each iteration:

1. State the current hypothesis in one sentence.
2. Design the smallest experiment that can confirm or reject it.
3. Run the experiment and collect evidence.
4. Decide whether to continue, adjust direction, or stop.
5. Only then make the next change.

## Experiment Design Rules

- Prefer one-variable experiments. Do not change several independent things at once.
- Start with read-only experiments when possible: logs, traces, file inspection, targeted tests, repro scripts.
- If a code change is needed to test an idea, make the smallest reversible change.
- Prefer targeted validation over full-suite runs until the direction looks correct.
- If an experiment disproves the hypothesis, say so explicitly and move on instead of defending the old path.

## Implementation Rules

- Keep diffs small while exploring.
- Separate instrumentation changes from production fixes when practical.
- Do not mix "try to understand" edits with broad cleanup.
- When a likely fix emerges, convert from exploration mode into normal implementation and validation mode.

## Evidence to Prefer

- Exact repro steps.
- Targeted test output.
- Stack traces and error logs.
- Before and after behavior from a small command or script.
- Browser evidence or screenshots for UI changes.
- Timing numbers for performance claims.

## Stop Conditions

Stop exploring and move to finalization when one of these is true:

- The hypothesis is strongly supported by evidence and the remaining work is straightforward.
- A proposed direction is disproved and should be abandoned.
- The task is blocked by missing inputs, secrets, or external systems.
- The cost of more exploration exceeds the value of added certainty.

## Final Output

At handoff, include:

- The winning hypothesis.
- The experiments run.
- What failed and what was learned.
- The implemented fix or chosen approach.
- The validation evidence that supports the result.

## Anti-Patterns

- Jumping straight into a large patch before the problem is understood.
- Running broad commands repeatedly when a smaller experiment would answer the question faster.
- Treating guesses as findings.
- Hiding failed attempts instead of learning from them.
- Declaring success without evidence tied to the user-visible problem.

## Example Triggers

- "Investigate this flaky test and figure out what is really happening."
- "Refactor this area, but do it safely and verify each step."
- "Optimize this page without guessing."
- "Try a few approaches and keep the one that actually works."
