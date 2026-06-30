# Runtime LLM Failure Taxonomy

Workflow or component:

Observed failure:

Evidence:

- Command:
- Log:
- Trace:
- Screenshot:
- Artifact:
- User-visible effect:

Failure category:

- input_ambiguity
- missing_context
- retrieval_miss
- stale_context
- prompt_gap
- schema_failure
- tool_contract_failure
- policy_violation
- permission_violation
- model_reasoning_error
- hallucinated_fact
- hallucinated_id
- wrong_candidate
- unsafe_side_effect
- latency_or_cost
- orchestration_bug
- product_state_mismatch
- eval_gap
- browser_action_without_effect_evidence
- heuristic_masking_root_cause

Root-cause classification:

- Code bug:
- Contract gap:
- Evidence gap:
- Model uncertainty:
- Tool-state mismatch:
- Product-state mismatch:
- Authority-boundary gap:
- Eval gap:

Containment:

- Temporary containment used:
- Trigger condition:
- Scope:
- Trace field:
- Removal or promotion criterion:

Permanent fix path:

Regression case to add:

Residual risk:
