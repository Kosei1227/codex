# Prompt Hierarchy Patterns

## Why hierarchy matters

Flat prompts fail when the model cannot tell whether a sentence is a top-level authority rule, a domain exception, task data, validator feedback, or an example. The solution is not only shorter prompts. The solution is a stable information hierarchy.

## Evidence-backed principles

OpenAI guidance emphasizes putting instructions first, separating instructions from context, being specific about output format, and reducing vague wording.

Anthropic guidance emphasizes using structured tags to separate instructions, context, examples, and formatting, and nesting tags for hierarchical content.

Prompt chaining and decomposition research supports splitting complex tasks into smaller controllable steps. Inside one prompt, the same principle applies as a decision procedure with named stages.

Prompt pattern research supports treating prompts as reusable design patterns, not one-off piles of instructions.

## Useful patterns

### Contract First

Start with the component contract before examples or domain details.

Use when: the model is overreaching into adjacent layers.

### Authority Boundary

State what the model may propose and what deterministic code enforces.

Use when: LLM output can affect product state, tool use, graph execution, money, or persistence.

### Input Hierarchy

Separate trusted product contracts from untrusted user data and prior model outputs.

Use when: prompt injection, stale model output, or context confusion is possible.

### Decision Procedure

Give numbered or tagged steps that mirror the intended algorithm.

Use when: the model must perform multiple subdecisions.

### Domain Subcontract

Keep domain-specific rules under named domain tags instead of mixing them into the global rules.

Use when: one component supports several workflows or domains.

### Repair Contract

In retry prompts, show only validator blockers and define what may be changed.

Use when: retry prompts start becoming larger than the original prompt.

### Counterexample Pair

Use a small counterexample only when evals show repeated confusion between adjacent labels.

Use when: instruction-only fixes are too vague.

## Anti-patterns

1. Appending a new rule after every failed run.
2. Mixing examples with instructions without labels.
3. Hiding output contract in prose.
4. Using many negative instructions without saying the correct alternative.
5. Asking the model to enforce IDs or permissions that code should validate.
6. Letting a retry prompt reinterpret the task instead of repairing validator blockers.
7. Treating previous model output as fact.
8. Encoding one task name, station, date, or UI label as a general rule.

## Refactor sequence

1. Extract current prompt.
2. Label every line by role.
3. Delete duplicates and obsolete patches.
4. Move validator-owned rules into validator diagnostics.
5. Convert remaining semantic guidance into a decision procedure.
6. Add domain subcontracts after the core contract.
7. Add explicit abstain and blocker behavior.
8. Tie each changed behavior to evals.
