---
name: first-plan-seeder
description: "Generate the first `.agent/active-plans/...` plan after a repo harness is instantiated. Use this whenever bootstrap is complete but the repo still lacks its first action plan, especially to convert the approved first milestone into a concrete `L2` execution plan before any coding starts."
---

# First Plan Seeder

This skill creates the first executable plan after harness instantiation.

## Hard boundaries

- do not write application code
- create one focused first plan only
- keep the plan centered on the first milestone
- do not spill second-phase work into the first plan

## Preconditions

These must exist before you continue:

- `PRODUCT_SPEC.md`
- `HARNESS_BOOTSTRAP.md`
- `AGENTS.md`
- `.agent/PLANS.md`
- `.agent/ARCHITECTURE.md`
- `.agent/TESTING.md`
- `.agent/RUNTIME.md`
- `.agent/MEMORY.md`
- `docs/api/API_CONTRACT.md`
- `docs/data/DATA_CONTRACT.md`
- `docs/runtime/RUNTIME_BASELINE.md`
- `docs/ops/AUTHORIZATION_BASELINE.md`
- `docs/ops/VERIFICATION_BASELINE.md`

If the harness is incomplete, stop and route back to `bootstrap-harness`.

## Existing-plan rule

If `.agent/active-plans/` already contains a real `.md` plan, do not create a second bootstrap plan.

Instead:

- report that the repo already has a first action plan
- summarize its filename
- stop

## Plan target

Create:

`.agent/active-plans/YYYY-MM-DD-first-action-plan.md`

Use the current local date in the filename.

## Required reading before writing the plan

Read these in order:

1. `HARNESS_BOOTSTRAP.md`
2. `PRODUCT_SPEC.md`
3. `AGENTS.md`
4. `.agent/PLANS.md`
5. `.agent/ARCHITECTURE.md`
6. `.agent/TESTING.md`
7. `.agent/RUNTIME.md`
8. `.agent/MEMORY.md`
9. runtime, authorization, and verification baselines

## Plan defaults

Default the first action plan to `L2`.

Use these defaults unless the milestone clearly requires stronger settings:

- `change_level: L2`
- `contract_changed: true`
- `tests_required: true`
- `approval_required: false`
- `rollback_required: false`

Choose these fields from milestone scope:

- `api_doc_required: true` only if the first milestone changes or creates a public interface
- `data_doc_required: true` only if persistence, schema, or migration behavior is part of the milestone
- `runtime_doc_required: true` if the first milestone changes execution model, retries, jobs, scheduling, or agent-loop behavior
- `authorization_doc_required: true` if the first milestone touches approval, permissions, MCP, external APIs, or high-risk writes
- `verification_doc_required: true` for the first plan by default

If the milestone is clearly infrastructure-heavy enough to be `L3`, say so explicitly and explain why.

## Content rules

The plan must conform to `.agent/PLANS.md`.

At minimum it must include:

- goal
- scope and non-goals
- change metadata
- affected files
- runtime or system contract impact
- API impact
- data impact
- authorization impact
- verification impact
- test plan
- implementation sequence
- rollback or containment notes

## Milestone source

Take the first milestone from `HARNESS_BOOTSTRAP.md`.

If it is vague, refine it using the current phase goal in `PRODUCT_SPEC.md`.

If it is still too vague to produce a deterministic plan, stop and return a short clarification request instead of inventing.

## Output report

When finished, report:

1. the new plan path
2. the chosen change level
3. the first milestone the plan targets
4. any assumptions you had to lock to make the first plan deterministic
