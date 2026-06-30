# Runtime Patterns

Use this reference to choose how LLM components should be composed inside the product.

## Pattern Selection Rule

Use the simplest pattern that satisfies the product behavior and risk level.

Prefer deterministic workflows when the task path is known. Use agentic control only when the product truly needs dynamic decision-making over steps or tools.

## Patterns

### Classify Then Route

Use when the product has known paths and the LLM only needs to identify which path applies.

Controls:

1. Closed enum.
2. Ambiguous state.
3. Deterministic router.
4. Regression evals for boundary cases.

### Extract Then Validate

Use when turning messy text, documents, emails, receipts, logs, or forms into structured fields.

Controls:

1. Field-level schema.
2. Evidence references.
3. Type and range checks.
4. Human review for high-impact fields.

### Retrieve Then Ground

Use when answering from documents, databases, policies, tickets, or knowledge bases.

Controls:

1. Source attribution.
2. Context freshness.
3. Retrieval quality metrics.
4. Refusal when evidence is missing.
5. Prompt-injection isolation for retrieved text.

### Rank Then Select

Use when candidates are already known and the model ranks or chooses among them.

Controls:

1. Candidate IDs supplied by code.
2. No invented candidates.
3. Tie and ambiguity behavior.
4. Evidence for ranking factors.

### Plan Then Execute Deterministically

Use when a task has multiple steps but each action should be executed by code.

Controls:

1. Allowed action set.
2. Plan schema.
3. State-machine validation.
4. Step budget.
5. Human approval for high-impact plans.

### Propose Tool Arguments Then Authorize

Use when the LLM maps user intent to a tool call.

Controls:

1. Strict tool schema.
2. Permission checks.
3. Allowed IDs and destinations.
4. Dry-run or preview.
5. Confirmation for high-risk tools.

### Generate Then Check

Use when producing user-facing content, drafts, reports, code snippets, summaries, or messages.

Controls:

1. Output policy checks.
2. Factuality or grounding checks when factual.
3. Style and format validators when needed.
4. Human edit path for important content.

### Judge Then Calibrate

Use when an LLM evaluates outputs, traces, retrieved evidence, or user satisfaction.

Controls:

1. Rubric.
2. Judge prompt version.
3. Human-labeled calibration set.
4. Precision and recall tracking.
5. Disagreement review.

### Parallel Judgments Then Reduce

Use when independent perspectives improve quality or when work can be split safely.

Controls:

1. Independent shards or dimensions.
2. Stable source order.
3. Deterministic reducer when possible.
4. Conflict state.
5. Arbitration policy.

### Human Review As A Tool

Use when the system needs approval, missing information, expert judgment, or accountability.

Controls:

1. Review payload with evidence and proposed action.
2. Clear approve, reject, edit, or request-info outcomes.
3. Durable audit trail.
4. Feedback captured for evals.

### Shadow Mode Then Promote

Use when changing model, prompt, retrieval, planner, or authority level.

Controls:

1. Run new behavior without changing live outcome.
2. Compare against current behavior.
3. Review disagreements.
4. Promote only after eval and product gates pass.

### Agent As Stateless Reducer

Use when the LLM must repeatedly choose the next step from accumulated events.

Controls:

1. External durable state.
2. Event log.
3. Narrow tools.
4. Step budget.
5. Idempotent tool execution.
6. Resume and pause APIs.
7. Human escalation.

## Anti-Pattern: One Prompt Owns Everything

Avoid one prompt that performs intent detection, retrieval, planning, tool calling, permission checking, final response generation, and self-evaluation.

Split into components when:

1. Different parts need different evals.
2. Different parts have different authority.
3. Different failures need different recovery paths.
4. The trace is hard to inspect.
5. The prompt grows because it absorbs edge cases.
