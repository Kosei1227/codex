# Component Inventory

Use this reference to map how LLMs participate in runtime product behavior.

## Goal

Create a concrete inventory before changing prompts, models, orchestration, tools, or validators.

LLM-integrated systems should be understood as collections of named components. A product can include many LLM components, such as an intent classifier, extraction step, RAG answerer, reranker, planner, validator, tool argument proposer, or human review assistant.

## Component Card

For each runtime LLM component, capture:

1. `name`
   Stable component name used in code, logs, evals, and docs.

2. `product_behavior`
   What user-visible or business behavior this component affects.

3. `trigger`
   What starts the component: user action, background job, webhook, cron, queue event, previous LLM result, or human review.

4. `input_sources`
   User input, database records, retrieved documents, files, tool results, previous model output, system state, or product config.

5. `input_trust_levels`
   Trusted, internal, user-provided, third-party, retrieved, model-generated, or unknown.

6. `output_consumer`
   UI, workflow router, database writer, tool executor, message sender, evaluator, planner, human reviewer, or another LLM component.

7. `authority_level`
   Use `references/authority-boundaries.md`.

8. `contract`
   Input schema, output schema, allowed IDs, allowed enums, evidence, abstain state, validators, and failure policy.

9. `dependencies`
   Models, prompts, retrieval indexes, tools, APIs, product state, policies, feature flags, and human review queues.

10. `failure_modes`
   Wrong classification, unsupported claim, malformed output, unsafe tool args, stale retrieval, missing evidence, hallucinated ID, policy violation, latency, cost, or silent degradation.

11. `eval_surface`
   Contract tests, semantic cases, adversarial cases, production trace review, human labels, LLM judge, or end-to-end product outcome.

12. `observability`
   Trace fields, metrics, alerts, dashboards, retained artifacts, and replay plan.

## Inventory Procedure

1. Search code for model SDK calls, agent frameworks, prompt templates, tool definitions, retrievers, evaluators, and structured-output parsers.
2. Trace each call forward to its output consumer.
3. Trace each call backward to its input and context assembly.
4. Identify whether the output affects product state, tool use, user-visible content, routing, permissions, or evaluation.
5. Group related calls into named components.
6. Mark components that lack contracts, validators, fallbacks, evals, or logging.
7. Prioritize high-authority and high-impact components first.

## Risk Signals

Treat these as design gaps:

1. A prompt is the only specification.
2. The same component handles classification, planning, execution, and validation.
3. The output is parsed from prose.
4. A model can invent IDs, tools, selectors, destinations, file paths, or SQL.
5. RAG context is treated as trusted instructions.
6. Tool results are appended to context without source labels.
7. Prompt or model versions are not logged.
8. Production failures cannot be replayed from traces.
9. Human reviewers see only the final answer, not the evidence and decision path.
10. No eval exists for known failures.

## Deliverable

For a repo review, produce:

1. Component list.
2. Product behavior each component affects.
3. Authority level.
4. Main trust-boundary risks.
5. Missing contracts or validators.
6. Missing evals or traces.
7. Highest-priority changes.
