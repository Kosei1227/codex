# Evals And Observability

Use this reference to define how LLM product behavior is tested, monitored, debugged, and improved.

## Core Rule

Evals and traces are product infrastructure, not optional QA artifacts.

If a component cannot be evaluated or replayed, it cannot be reliably improved.

## Eval Types

Use a mix of:

1. `contract_tests`
   Schema, allowed IDs, enums, required evidence, prohibited fields, permission checks, and policy checks.

2. `golden_cases`
   Known examples with expected outputs or expected outcome properties.

3. `semantic_cases`
   Cases where correctness depends on meaning rather than exact string match.

4. `adversarial_cases`
   Prompt injection, malformed inputs, data exfiltration attempts, unsupported requests, and policy bypass attempts.

5. `retrieval_cases`
   Context recall, context precision, stale context, missing source, and conflicting source tests.

6. `tool_cases`
   Valid tool args, invalid tool args, unauthorized IDs, stale product state, and tool failure handling.

7. `human_labeled_cases`
   Domain-expert labels for quality, correctness, risk, and user satisfaction.

8. `llm_judge_cases`
   Automated evaluation calibrated against human labels.

9. `end_to_end_cases`
   Product workflows that verify the user-visible outcome, not only the component output.

10. `production_trace_regressions`
   Real failures converted into repeatable tests.

11. `prompt_change_cases`
   Cases that compare old and new prompt behavior for instruction following, functional correctness, schema adherence, evidence grounding, abstention quality, tool selection, tool argument precision, latency, and cost.

## Trace Schema

Trace every meaningful component call with:

1. Request or session ID.
2. Component name.
3. Product feature.
4. Prompt version.
5. Schema version.
6. Prompt content hash when available.
7. Model or model class.
8. Input digest.
9. Input source labels.
10. Retrieval query and evidence IDs.
11. Tool schemas available.
12. Tool calls proposed.
13. Tool calls executed.
14. Raw output.
15. Parsed output.
16. Validator results.
17. Uncertainty state.
18. Failure category.
19. Retry count.
20. Fallback path.
21. Human review decision.
22. Latency.
23. Cost.

Redact secrets and sensitive data. Preserve enough structure for replay.

## LLM-As-Judge

Use LLM judges for subjective, semantic, or expensive-to-code checks.

Do not trust a judge until it is calibrated.

Required controls:

1. Written rubric.
2. Versioned judge prompt.
3. Human-labeled calibration set.
4. Precision and recall tracking when classes are imbalanced.
5. Periodic human agreement checks.
6. Disagreement review.
7. Separate judge from the component being judged when practical.

Avoid letting the same model output, judge, and approve a high-impact decision without external validation.

## Release Gates

Before shipping prompt, model, retrieval, tool, or contract changes:

1. Run contract tests.
2. Run known regression cases.
3. Run representative semantic cases.
4. Run adversarial cases for exposed inputs.
5. Compare against current behavior.
6. Inspect important disagreements.
7. Confirm observability fields are present.
8. Confirm rollback or disable path.

For high-impact components, use shadow mode or staged rollout.

For prompt changes specifically:

1. Record the intended behavior change.
2. Compare old and new prompt versions on the same eval set.
3. Inspect regressions and important disagreements.
4. Confirm the change does not widen authority, tool scope, data exposure, or side-effect behavior without an explicit contract update.
5. Update prompt version, trace fields, and eval baselines together.

## Production Monitoring

Monitor:

1. Task success rate.
2. Validator failure rate.
3. Ambiguity rate.
4. Human escalation rate.
5. Retry rate.
6. Fallback rate.
7. LLM judge disagreement.
8. User corrections.
9. Latency.
10. Cost.
11. Retrieval quality.
12. Tool failure rate.
13. Policy violation attempts.

Quality monitoring should include sampled trace review. Metrics alone miss many LLM failures.

## Feedback Loop

When production reveals a failure:

1. Preserve the trace.
2. Classify the failure.
3. Identify the responsible component.
4. Decide whether the fix belongs in prompt, contract, retrieval, tool schema, validator, UX, policy, or product flow.
5. Add a regression eval.
6. Test the fix against old and new cases.
7. Update documentation and monitoring if the failure category is new.

Do not patch only the prompt if the real failure is missing context, weak tools, absent validation, unsafe authority, or unclear product behavior.
