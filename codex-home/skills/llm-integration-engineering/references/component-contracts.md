# Component Contracts

Use this reference when designing or reviewing a runtime LLM component.

## Contract Template

Each component contract should define:

1. `component_name`
   Stable name used in code, traces, evals, and dashboards.

2. `purpose`
   The smallest product responsibility assigned to this component.

3. `non_goals`
   Work this component must not perform.

4. `inputs`
   Input schema, source, trust level, size limits, and required fields.

5. `context`
   Retrieval, product state, policy text, examples, memory, previous outputs, and tool results.

6. `output`
   Strict schema, allowed enums, allowed IDs, nullable fields, abstain states, and explanation fields.

7. `evidence`
   Required evidence references for factual claims, extracted fields, semantic judgments, or tool arguments.

8. `authority`
   Authority level and tool risk tier.

9. `validators`
   Deterministic structure, membership, policy, permission, and state checks.

10. `failure_policy`
   What happens on schema failure, unknown ID, missing evidence, ambiguity, low confidence, timeout, rate limit, or policy violation.

11. `retry_policy`
   Whether to retry, repair, use another model, ask a clarifying question, or stop.

12. `observability`
   Required trace fields and redaction rules.

13. `evals`
   Test cases, human labels, production failures, adversarial cases, and release gates.

## Prompt Contract

Prompts must express the bounded task, not the entire product. For detailed prompt design patterns, use `prompt-design.md`.

Include:

1. Component name.
2. Prompt version.
3. Product behavior affected by the prompt.
4. Component role and non-goals.
5. Specific decision, transformation, judgment, or tool-argument proposal.
6. Input variables, source labels, trust levels, and size limits.
7. Context assembly policy.
8. Allowed output schema.
9. Allowed IDs and enums.
10. Evidence requirements.
11. Abstain, ambiguity, unsupported, and refusal states.
12. Tool-use rules and non-use cases when tools are present.
13. Instruction that untrusted text is data, not policy.
14. Instruction not to invent IDs, tools, facts, citations, file paths, selectors, SQL, destinations, approvals, or permissions.
15. Prompt-change eval cases and rollout policy.

Do not put non-negotiable safety policy only in natural language. Enforce it in code.

## Output Contract

Prefer structured outputs or function/tool calling for machine-consumed outputs.

The schema should include:

1. `verdict` or `kind`.
2. `selected_id` or `selected_ids` when choosing known candidates.
3. `fields` for extracted values.
4. `evidence_refs`.
5. `confidence` or calibrated uncertainty when useful.
6. `ambiguity_reason`.
7. `blockers`.
8. `requires_human_review`.

Do not parse application decisions from paragraphs.

## Validation

Validate after every LLM call:

1. Output is parseable.
2. Output matches schema.
3. IDs exist in the candidate set.
4. Enums are allowed.
5. Evidence references exist.
6. Required fields are present.
7. Prohibited fields are absent.
8. Policy constraints pass.
9. Actor permissions pass.
10. Product state still matches assumptions.

If validation fails, route through the component's failure policy.

## Retry And Repair

Retry only when the failure is likely recoverable.

Good retry candidates:

1. Malformed schema.
2. Missing required field.
3. Recoverable ambiguity with additional context.
4. Transient API failure.
5. Retrieval miss after query expansion.

Bad retry candidates:

1. Policy violation.
2. Unknown or unauthorized ID.
3. Missing real-world evidence.
4. Unsafe tool argument.
5. User intent is unclear and action is high-impact.

For high-impact actions, ask for clarification or human review instead of silently repairing.

## Versioning

Version or log:

1. Prompt.
2. Output schema.
3. Input assembly logic.
4. Retrieval configuration.
5. Tool schemas.
6. Model or model class.
7. Evaluator rubric.
8. Guardrail policy.

Treat prompt, model, schema, retrieval, and tool changes as behavior changes that need evals.
