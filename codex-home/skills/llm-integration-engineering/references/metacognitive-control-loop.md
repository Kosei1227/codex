# Metacognitive Control Loop

Use this reference when an LLM component must reason about uncertainty, recovery, escalation, or improvement.

## Definition

Metacognition is the product-level control loop that observes LLM behavior, assesses uncertainty and evidence, chooses a safe recovery path, and feeds validated failures back into the system.

It is not the same as asking the model to think harder or critique itself.

## The Loop

Every non-trivial component should implement this loop:

1. `observe`
   Capture user input, context, retrieved evidence, product state, tool state, previous outputs, and constraints.

2. `interpret`
   Ask the LLM only the bounded question assigned to this component.

3. `validate`
   Check schema, allowed IDs, evidence references, permissions, policy, and product state.

4. `assess_uncertainty`
   Classify the result as confident, ambiguous, unsupported, incomplete, conflicting, unsafe, stale, or invalid.

5. `decide`
   Apply, retry, retrieve more, ask the user, request human review, use fallback, or stop.

6. `record`
   Log trace, inputs, evidence IDs, output, validators, uncertainty category, and selected recovery path.

7. `improve`
   Add important failures to evals, prompts, retrieval, tools, UX, documentation, or product constraints.

## Uncertainty States

Use explicit states rather than hidden heuristics:

1. `confident`
   Contract passes and evidence supports the result.

2. `ambiguous`
   Multiple interpretations or candidates remain plausible.

3. `unsupported`
   Output lacks required evidence.

4. `incomplete`
   More user input, product state, or tool results are needed.

5. `conflicting`
   Evidence sources disagree or product state changed.

6. `unsafe`
   Output violates policy, permissions, or side-effect constraints.

7. `invalid`
   Schema, IDs, enums, or validators failed.

8. `stale`
   Retrieval, cached context, or assumptions are outdated.

## Recovery Paths

Map each uncertainty state to a controlled path:

1. `retry_same_component`
   Use for malformed output or minor schema repair.

2. `retrieve_more_context`
   Use when evidence is incomplete and safe to expand.

3. `ask_user`
   Use when user intent is unclear and the product can ask a targeted question.

4. `human_review`
   Use for high-impact, ambiguous, unsafe, legal, financial, or irreversible decisions.

5. `safe_fallback`
   Use when deterministic behavior is acceptable.

6. `block`
   Use when policy, permission, safety, or evidence requirements fail.

7. `shadow_record`
   Use when evaluating a new model, prompt, or workflow without changing live behavior.

## Reflection Boundaries

Reflection can help generate:

1. Candidate failure explanations.
2. Repair proposals.
3. Alternative interpretations.
4. Questions to ask the user.
5. Candidate eval cases.

Reflection must not be accepted as proof.

Before using a reflected result:

1. Validate the new output against the component contract.
2. Check external evidence.
3. Preserve the original output and failure category.
4. Log the reflection prompt and result.
5. Avoid repeated self-revision loops without new evidence.

## Failure Taxonomy

Classify failures so the system can improve:

1. `input_ambiguity`
2. `missing_context`
3. `retrieval_miss`
4. `stale_context`
5. `prompt_gap`
6. `schema_failure`
7. `tool_contract_failure`
8. `policy_violation`
9. `permission_violation`
10. `model_reasoning_error`
11. `hallucinated_fact`
12. `hallucinated_id`
13. `wrong_candidate`
14. `unsafe_side_effect`
15. `latency_or_cost`
16. `orchestration_bug`
17. `product_state_mismatch`
18. `eval_gap`

## Design Tests

A metacognitive loop is not complete unless:

1. Ambiguity has a visible state.
2. Missing evidence has a visible state.
3. Unsafe outputs are blocked outside the model.
4. High-impact uncertainty reaches a human or stops.
5. Traces explain why the system chose its recovery path.
6. Production failures can become regression cases.
