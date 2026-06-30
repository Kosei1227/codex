# Prompt Design For Runtime LLM Components

Use this reference when designing, reviewing, versioning, or debugging prompts used by product runtime LLM calls.

This is not a generic prompting guide. Use it only when the prompt affects application behavior through classification, extraction, RAG, planning, tool use, judging, semantic validation, repair, or user-facing generation.

## Table Of Contents

1. Core Rule
2. Prompt Contract Template
3. Prompt Anatomy
4. Context Assembly
5. Technique Selection
6. Reasoning Guidance
7. Tool Prompt Design
8. Judge Prompt Design
9. Repair Prompt Design
10. Security And Trust
11. Prompt Evals
12. Versioning And Rollout
13. Anti-Patterns
14. Review Checklist

## Core Rule

Design prompts as versioned product interfaces.

A runtime prompt must define the bounded job of one LLM component. It must not become the only place where the product enforces permissions, identity, schemas, business invariants, tool safety, or side-effect policy.

Prompts can guide behavior. Deterministic software must enforce behavior.

## Prompt Contract Template

Every non-trivial runtime prompt should have:

1. `component_name`
   Stable name used in code, traces, evals, and dashboards.

2. `prompt_version`
   Explicit version or content hash tied to eval results.

3. `product_behavior`
   The user-visible or system behavior affected by the prompt.

4. `authority_level`
   Advisory, classify, extract, rank, retrieve, judge, plan, tool-args, side-effect request, or autonomous action.

5. `model_or_model_class`
   Model, model snapshot, or capability class expected by the prompt.

6. `input_variables`
   Names, types, source, trust level, size limits, and required fields.

7. `context_policy`
   Which evidence, product state, memory, examples, previous outputs, or tool results can enter the prompt.

8. `output_contract`
   Schema, allowed enums, allowed IDs, required evidence fields, ambiguity state, refusal state, and explanation fields.

9. `tool_policy`
   Available tools, allowed arguments, missing-information behavior, non-use cases, and side-effect restrictions.

10. `evidence_policy`
   Required source IDs, quote spans, record IDs, or product-state references for claims and decisions.

11. `uncertainty_policy`
   When to return `ambiguous`, `unsupported`, `not_enough_evidence`, `conflicting_evidence`, or `needs_human_review`.

12. `validators`
   Deterministic checks that run after the model output.

13. `eval_cases`
   Fixture, adversarial, ambiguity, regression, and tool-call cases tied to this prompt.

14. `rollout_policy`
   Comparison baseline, review gate, shadow mode, rollback, or disable path.

## Prompt Anatomy

Prefer a prompt structure that makes boundaries explicit:

1. Task
   State the smallest job this component performs.

2. Non-goals
   State what this component must not do.

3. Authority
   State what the model may propose and what code must decide.

4. Inputs
   Name each input variable and whether it is trusted or untrusted.

5. Context
   Provide relevant evidence, product state, or prior state with source labels.

6. Output
   Require the exact schema or function-call shape expected by code.

7. Evidence
   Require evidence references when the decision depends on facts, retrieved text, documents, or product state.

8. Uncertainty
   Define abstain and ambiguity behavior.

9. Examples
   Include examples only when they clarify subtle boundaries that instructions alone do not capture.

10. Counterexamples
   Include counterexamples when adjacent labels, actions, or tools are commonly confused.

Do not add persona text unless it changes product behavior in a measurable way.

## Context Assembly

Design context as carefully as the prompt text.

For each context item, define:

1. Source.
2. Trust level.
3. Recency.
4. Relevance reason.
5. Visibility or permission status.
6. Maximum size.
7. Redaction rule.
8. Delimiter or serialization format.

Keep instructions separate from data. Mark untrusted text as data, but do not rely on delimiters as the security boundary.

Prefer context that is:

1. Minimal enough to reduce distraction.
2. Complete enough to support the decision.
3. Labeled enough to support evidence references.
4. Stable enough for eval replay.

Avoid context that is:

1. Arbitrary logs without source labels.
2. Retrieved text that can silently override policy.
3. Previous model output treated as fact.
4. Secrets or credentials.
5. Large unrelated history that increases ambiguity.

## Technique Selection

Choose prompting techniques by component need, not by habit.

### Direct Prompting

Use for simple bounded tasks with clear inputs and output schema.

Controls:

1. Precise task.
2. Explicit output format.
3. Abstain behavior.
4. Regression evals.

### Zero-Shot First

Try zero-shot before adding examples when the task is clear and the model family is strong enough.

Add examples only when evals show repeated boundary errors.

### Few-Shot Examples

Use examples for domain conventions, label boundaries, tone, format, or extraction edge cases.

Examples must:

1. Match the schema exactly.
2. Avoid conflicting with instructions.
3. Cover common boundary cases.
4. Include negative or ambiguous cases when important.

Do not add many examples to compensate for an unclear schema or weak validator.

### Counterexamples

Use counterexamples when the model confuses close categories or tools.

Good counterexamples show:

1. Similar-looking input.
2. Wrong tempting output.
3. Correct output.
4. Short reason tied to the contract.

### Structured Outputs

Use structured outputs or function calling for machine-consumed outputs.

Prompt text should explain semantics, but schema should enforce shape.

Do not parse application decisions from prose when a schema can represent them.

### Prompt Chaining

Split prompts when one component starts doing multiple jobs:

1. Extract then validate.
2. Classify then route.
3. Retrieve then ground.
4. Plan then execute deterministically.
5. Judge then calibrate.
6. Repair then revalidate.

Use chaining when different steps need different authority, context, evals, or failure policies.

### Retrieval-Grounded Prompting

Use when the model must answer or decide from documents, policies, records, or user data.

Require:

1. Evidence IDs.
2. Refusal when evidence is missing.
3. Conflict reporting.
4. Source-aware output fields.
5. Prompt-injection isolation for retrieved text.

### Self-Check Prompting

Use self-checks only to generate hypotheses, critiques, or repair proposals.

Do not treat self-check output as proof. External validators, product state, evidence, evals, or humans decide acceptability.

## Reasoning Guidance

Do not blindly force chain-of-thought.

Prefer:

1. Clear success criteria.
2. Required decision fields.
3. Evidence references.
4. Uncertainty labels.
5. Short rationale fields when useful for review or UX.
6. Internal reasoning effort or model settings when supported by the API and validated by evals.

Avoid:

1. "Think step by step" as a default.
2. Long hidden reasoning in user-visible outputs.
3. Requiring rationales that code later treats as truth.
4. Adding reasoning instructions without measuring latency, cost, and quality.

If reasoning guidance changes, run prompt-change evals before shipping.

## Tool Prompt Design

Tool descriptions are part of prompt design.

For each tool, define:

1. Name that reflects the action.
2. Clear purpose.
3. Allowed use cases.
4. Non-use cases.
5. Argument schema.
6. Argument descriptions.
7. Example calls.
8. Edge cases.
9. Required missing-information behavior.
10. Side effects.
11. Risk tier.
12. Approval requirements.

Make tool arguments hard to misuse:

1. Prefer IDs over names when selecting known records.
2. Prefer narrow tools over broad tools.
3. Prefer enums over free text.
4. Prefer absolute, validated references over relative paths when paths are required.
5. Prefer preview or dry-run tools before side effects.

Test how the model uses tools. Tool prompts that look clear to humans can still be ambiguous to the model.

## Judge Prompt Design

Use judge prompts for subjective, semantic, or expensive-to-code checks.

A judge prompt must include:

1. Evaluation objective.
2. Rubric.
3. Input fields.
4. Output schema.
5. Pass, fail, and unsure states.
6. Evidence requirements.
7. Known biases to watch for.
8. Human calibration set.

Prefer narrow judge prompts over broad quality scores.

Examples:

1. "Does the answer cite only provided evidence?"
2. "Did the tool call use the correct customer ID?"
3. "Does the summary omit any required field?"

Do not let an uncalibrated judge approve high-impact behavior.

## Repair Prompt Design

Use repair prompts only when the failure is recoverable.

Good repair cases:

1. Malformed JSON.
2. Missing optional field.
3. Wrong enum spelling.
4. Missing evidence reference when evidence exists.

Bad repair cases:

1. Unauthorized ID.
2. Missing real-world evidence.
3. Policy violation.
4. Unsafe tool argument.
5. Ambiguous user intent for a high-impact action.

Repair output must be revalidated. Log the original output, repair prompt version, repaired output, and validation result.

## Security And Trust

Prompt hardening is not enough for security.

Prompt design should still:

1. Label untrusted input.
2. State that untrusted text is data, not instruction.
3. Require refusal or escalation when data attempts to change policy.
4. Prevent the model from inventing tools, IDs, permissions, file paths, selectors, SQL, network targets, or approvals.
5. Avoid sending secrets.
6. Keep side-effect authority outside the model.

Security must be enforced outside the prompt with validators, permissions, scoped tools, approval gates, logging, and policy checks.

## Prompt Evals

Every non-trivial prompt needs eval coverage.

Minimum eval set:

1. Happy path.
2. Boundary cases.
3. Ambiguous cases.
4. Unsupported requests.
5. Prompt injection attempts.
6. Conflicting instruction cases.
7. Missing evidence cases.
8. Schema failure cases.
9. Tool selection cases.
10. Tool argument cases.
11. Production failure regressions.

Prompt evals should measure:

1. Instruction following.
2. Functional correctness.
3. Schema adherence.
4. Evidence grounding.
5. Abstention quality.
6. Tool selection accuracy.
7. Tool argument precision.
8. Latency.
9. Cost.
10. Regression against the previous prompt.

## Versioning And Rollout

Treat prompt changes as behavior changes.

Before shipping a prompt change:

1. Record old prompt version.
2. Record new prompt version.
3. Identify intended behavior change.
4. Run prompt-change evals.
5. Compare against current behavior.
6. Inspect disagreements.
7. Update trace fields if needed.
8. Confirm rollback or disable path.
9. Use shadow mode for high-impact components.

Do not ship prompt changes based only on one successful manual example.

## Anti-Patterns

Avoid:

1. One giant prompt that owns interpretation, planning, tools, validation, and final response.
2. Magic phrases such as generic expert personas without eval evidence.
3. Prompt-only safety policy.
4. Forced chain-of-thought as a default.
5. Hidden framework prompts that cannot be inspected.
6. Examples that contradict instructions.
7. Free-form prose consumed by code.
8. Asking the model to choose arbitrary IDs, paths, selectors, or destinations.
9. Repairing high-impact outputs without human review.
10. Prompt patches that hide missing context, weak tools, missing validators, or unclear product behavior.

## Review Checklist

Before approving a runtime prompt:

1. Is the component's job small and named?
2. Is the prompt versioned?
3. Are trusted and untrusted inputs separated?
4. Is the output schema explicit?
5. Are allowed IDs and enums closed by code?
6. Are evidence requirements explicit?
7. Are abstain and ambiguity states defined?
8. Are tool rules and non-use cases clear?
9. Are side effects authorized outside the model?
10. Are validators defined?
11. Are eval cases tied to known failure modes?
12. Are latency and cost acceptable?
13. Is rollback possible?
14. Is the prompt understandable without hidden framework behavior?
