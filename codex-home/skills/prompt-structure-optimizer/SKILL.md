---
name: prompt-structure-optimizer
description: Use when reviewing, redesigning, or refactoring runtime LLM prompts that have become long, brittle, flat, or patch-like. Applies to product prompts for planning, extraction, routing, judging, tool arguments, semantic validation, or repair. Focuses on hierarchical prompt structure, authority boundaries, instruction/data separation, prompt contracts, eval-backed changes, and avoiding failure-by-failure prompt accretion.
---

# Prompt Structure Optimizer

Use this skill when a runtime product prompt is failing because it has become a flat list of accumulated rules, task-specific patches, or unclear priority layers.

Do not use this skill to add another local prompt rule. Use it to restructure the prompt contract so the model can distinguish authority, inputs, context, decision procedure, output schema, and repair behavior.

## Core Principle

A prompt is a versioned product interface. Optimize its information architecture before changing its wording.

Good prompt structure makes these layers explicit:

1. Component contract.
2. Authority boundary.
3. Non-goals.
4. Input hierarchy.
5. Trusted contracts versus untrusted task data.
6. Decision procedure.
7. Domain-specific subcontracts.
8. Output schema.
9. Uncertainty and abstain behavior.
10. Repair contract.
11. Eval cases and rollout gate.

## Mandatory Workflow

1. Inventory the prompt.
   Identify component name, prompt version, model, trigger, input variables, output schema, validators, and evals.

2. Classify every instruction.
   Put each line into one bucket: core contract, authority boundary, input hierarchy, domain-specific contract, output contract, repair rule, example, counterexample, validator responsibility, or obsolete patch.

3. Build the hierarchy.
   Move high-authority rules before domain rules. Keep instructions separate from task data. Use explicit section headers or XML-style tags.

4. Remove flat accretion.
   Do not append more rules to the bottom. Merge duplicates, remove validator-owned instructions, and replace repeated negatives with a positive decision procedure.

5. Preserve policy boundaries.
   Prompts may guide semantic interpretation. Deterministic code must still enforce schema, allowed IDs, provenance, permissions, side effects, and fail-closed behavior.

6. Add eval coverage.
   Every prompt change must map to at least one regression case, ambiguity case, or blocker case.

7. Produce a refactor report.
   Use `templates/prompt-refactor-report.md` when the change is non-trivial.

## Preferred Prompt Skeleton

```xml
<component_contract>
  <component_name>...</component_name>
  <prompt_version>...</prompt_version>
  <task>Smallest job this component performs.</task>
  <authority>What the model may propose.</authority>
  <non_goals>What the model must not decide.</non_goals>
</component_contract>

<input_hierarchy>
  <trusted_contracts>Schemas, allowed IDs, product contracts.</trusted_contracts>
  <semantic_evidence>User task, extracted facts, documents, UI evidence.</semantic_evidence>
  <prior_outputs>Previous model outputs, only if explicitly allowed.</prior_outputs>
</input_hierarchy>

<decision_procedure>
  <step id="1">...</step>
  <step id="2">...</step>
</decision_procedure>

<domain_specific_contracts>
  <domain name="...">Only domain rules for this component.</domain>
</domain_specific_contracts>

<output_contract>
  Exact schema, allowed values, evidence refs, blockers, abstain behavior.
</output_contract>

<repair_contract>
  Repair only validator-identified fields. Do not introduce new goals.
</repair_contract>
```

## Review Questions

Before accepting a prompt change, answer:

1. Which component owns this semantic decision?
2. Is this line a core rule, a domain rule, a repair rule, or a validator rule?
3. Does this line duplicate another line?
4. Does this line encode one observed failure too specifically?
5. Would a deterministic validator be a better owner?
6. Does the output schema expose uncertainty or blockers?
7. Which eval proves the change helped without degrading adjacent cases?

## References

Read only when needed:

- `references/prompt-hierarchy-patterns.md` for hierarchy and anti-patterns.

## Templates

- `templates/prompt-refactor-report.md` for reviewable prompt refactor proposals.
