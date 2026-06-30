---
name: llm-integration-engineering
description: "Use when designing, implementing, debugging, or reviewing product systems that use LLM calls at runtime as part of application behavior, including RAG, extraction, classification, planning, tool use, agent workflows, semantic validation, document processing, workflow automation, or LLM-based decision support. Focus on LLM components as production subsystems: component inventory, authority boundaries, trust boundaries, structured contracts, prompt contracts, deterministic validation, metacognitive uncertainty handling, evals, observability, fallback behavior, human escalation, and safe rollout. Do not use this for ordinary AI-assisted coding advice unless the code being built embeds LLM calls into product behavior."
---

# LLM Integration Engineering

Use this skill when an LLM is part of a product's runtime behavior.

Do not treat an LLM call as a prompt hidden inside code. Treat it as a probabilistic product component with a contract, authority boundary, trust boundary, metacognitive control loop, eval surface, and observability plan.

The goal is not to make the model sound better. The goal is to make product behavior reliable, inspectable, recoverable, and safe.

Prompts are not safety boundaries or product contracts by themselves. A runtime prompt is one versioned part of the LLM component contract and must be paired with schemas, validators, traces, evals, fallbacks, and authority checks.

## Core Rule

LLMs may interpret, classify, extract, rank, retrieve, summarize, judge, plan, or propose. They must not silently acquire authority.

Deterministic software must own permissions, identity, allowed actions, business invariants, schema validation, policy enforcement, side effects, persistence, auditability, and final enforcement.

## Workflow

Follow this sequence before changing prompts, orchestration, tools, model choice, or validators:

1. Identify the product behavior affected by the LLM.
2. Inventory the runtime LLM components.
3. Classify each component's authority and trust boundaries.
4. Define the component contract and prompt contract.
5. Define the metacognitive control loop.
6. Choose a runtime integration pattern.
7. Define evals, traces, monitoring, and rollout gates.
8. Implement or review the code against the contract.

If any step cannot be answered, stop and produce the missing design artifact instead of patching prompts.

## Reference Files

Read only the relevant reference files:

1. `references/component-inventory.md`
   Use when mapping existing LLM calls, designing a new LLM-powered feature, or diagnosing unknown LLM behavior across a codebase.

2. `references/authority-boundaries.md`
   Use when the LLM can select tools, propose actions, affect product state, influence money, expose data, contact users, or trigger irreversible work.

3. `references/component-contracts.md`
   Use when adding or reviewing any LLM call, structured output, function call, tool argument, RAG answer, evaluator, or planner.

4. `references/prompt-design.md`
   Use when designing, reviewing, versioning, or debugging runtime prompts, developer messages, examples, context assembly, tool descriptions, structured-output instructions, evidence requirements, refusal behavior, or prompt-change evals.

5. `references/metacognitive-control-loop.md`
   Use when a component must detect uncertainty, recover from failures, ask for help, retry, self-check, escalate, or improve from traces.

6. `references/runtime-patterns.md`
   Use when choosing the shape of the system: workflow, router, extractor, planner, tool caller, judge, parallel reducer, human review path, or agent.

7. `references/evals-observability.md`
   Use when defining tests, regression suites, trace schemas, LLM-as-judge, human review, production monitoring, or release gates.

8. `references/security-trust-boundaries.md`
   Use when inputs include user text, retrieved documents, web pages, emails, files, database rows, tool results, plugins, skills, secrets, or regulated data.

## Templates

Use these templates when the task needs a durable design or review artifact:

1. `templates/component-contract.md`
   Use before implementing or changing a runtime LLM call.

2. `templates/eval-plan.md`
   Use when defining release gates, regression cases, golden cases, LLM-as-judge checks, or production monitoring.

3. `templates/failure-taxonomy.md`
   Use when failures are being hidden by retries, fallbacks, heuristics, UI automation, or unclear root-cause labels.

4. `templates/runtime-llm-review.md`
   Use after implementation to review authority boundaries, schema validation, traces, eval coverage, and heuristic debt.

## Component Lens

Analyze LLM-integrated products as collections of LLM components, not as one large agent.

For each component, identify:

1. Name.
2. Product purpose.
3. Trigger.
4. Input sources.
5. Input trust level.
6. Output consumer.
7. Authority level.
8. Output contract.
9. Prompt contract.
10. Evidence requirements.
11. Failure policy.
12. Eval surface.
13. Observability fields.

If the component cannot be named and contracted, it is not ready to be implemented as runtime product behavior.

## Authority Principle

Use the lowest authority level that satisfies the product goal.

Prefer:

1. Deterministic code for explicit business logic and safety rules.
2. LLM classification or extraction for bounded semantic interpretation.
3. LLM planning only when fixed workflows cannot cover the task.
4. LLM tool argument proposal only behind strict validators.
5. Human approval for high-impact, irreversible, ambiguous, or policy-sensitive actions.

Do not let model output directly mutate product state, execute arbitrary tools, grant permissions, select unrestricted destinations, create executable selectors, create SQL, create file paths, or bypass approval.

## Contract Principle

Every runtime LLM component needs a versioned contract:

1. Input schema.
2. Output schema.
3. Prompt contract.
4. Allowed IDs and enum values.
5. Required evidence references.
6. Abstain or ambiguous state.
7. Deterministic validators.
8. Retry and repair policy.
9. Fallback and escalation policy.
10. Logging fields.
11. Eval cases.

Free-form prose may be shown to users, but code must not rely on unvalidated prose as an integration boundary.

## Metacognitive Principle

Metacognition is the product's explicit control loop for observing, judging, and adapting LLM component behavior.

Implement metacognition through traces, validators, uncertainty states, failure categories, retries, fallbacks, human escalation, and eval updates. Do not treat unverified self-reflection as correctness.

Reflection can generate hypotheses, critiques, or repair proposals. External validators, product state, evidence, and evals decide whether behavior is acceptable.

## Trust Principle

Treat user input, retrieved documents, web pages, emails, files, database content, tool results, plugin output, skill text, and previous model output as untrusted data unless the system has a reason to trust them.

Untrusted data must not grant new instructions, permissions, tools, destinations, selectors, SQL, file paths, network targets, data visibility, approvals, or policy exceptions.

## Evaluation Principle

Validation must prove product behavior, not only JSON parsing.

Use a combination of:

1. Deterministic contract tests.
2. Golden semantic cases.
3. Known production failure regressions.
4. Adversarial and malformed inputs.
5. Human review.
6. Calibrated LLM judges.
7. End-to-end product outcome tests.
8. Production trace monitoring.

When using LLM-as-judge, validate the judge against human labels or trusted examples. Do not let an unvalidated judge define success.

## Observability Principle

Log enough to replay and diagnose behavior:

1. Component name.
2. Prompt version.
3. Schema version.
4. Model or model class.
5. Input digest.
6. Evidence IDs.
7. Tool calls proposed.
8. Tool calls executed.
9. Raw model output.
10. Parsed output.
11. Validation result.
12. Failure category.
13. Retry or fallback decision.
14. Latency and cost.
15. Human override.

Redact secrets and sensitive data according to product requirements.

## Anti-Patterns

Avoid:

1. One giant agent prompt that interprets, plans, authorizes, executes, validates, and explains.
2. Relying on prompt instructions as the only safety boundary.
3. Treating schema-valid output as semantically correct output.
4. Treating self-critique as proof.
5. Treating a single successful demo as stability.
6. Hiding LLM calls behind framework abstractions that make prompts, tools, traces, or failures hard to inspect.
7. Adding hardcoded synonyms instead of defining a semantic contract.
8. Giving the model broad tools when a narrow product API would work.
9. Shipping prompt or model changes without regression evals.
10. Letting retrieved or user-provided text override system policy.
11. Relying on magic phrases, generic persona text, or forced chain-of-thought instead of contract, context, schema, tool, and eval design.

## Output Expectations

When using this skill, produce one of these artifacts as appropriate:

1. LLM component inventory.
2. Component contract.
3. Prompt contract and prompt-change review.
4. Authority and trust-boundary review.
5. Runtime pattern recommendation.
6. Metacognitive control-loop design.
7. Eval and observability plan.
8. Implementation patch with validators, fallbacks, logs, and tests.
9. Review findings ordered by product risk.

Keep recommendations tied to concrete product behavior. Do not drift into generic prompt engineering or AI-assisted coding advice.
