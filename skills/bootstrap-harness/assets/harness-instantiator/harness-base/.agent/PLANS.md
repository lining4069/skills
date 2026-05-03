# Execution Plans

Use this file as the contract for any active plan stored under `.agent/active-plans/`.

## When A Plan Is Required

Create or update a plan when:

- the change is `L2` or `L3`
- touching multiple subsystems
- changing policies, budgets, retries, approvals, or failure handling
- changing runtime behavior or scheduling semantics
- changing memory strategy
- adding or changing tools, adapters, MCP integrations, or other capability boundaries
- changing API contracts
- changing data contracts
- changing verification or release-gate rules
- introducing new regression coverage across more than one test file

`L0` changes usually do not require an active plan.

`L1` changes can use a shorter work note when they stay inside one subsystem and do not change API, runtime, data, memory, or verification contracts.

`L2` and `L3` changes require an active plan in `.agent/active-plans/`.

## Required Sections

Every plan should contain:

1. Goal
2. Scope and non-goals
3. Change metadata
4. Affected files
5. Runtime or system contract impact
6. API or user-facing contract impact
7. Data or persistence contract impact
8. Authorization or permission-boundary impact
9. Verification impact
10. Test plan
11. Step-by-step implementation sequence
12. Rollback or containment notes

## Structured Change Metadata

Every `L2` or `L3` active plan should include these fields:

- `change_level`
- `contract_changed`
- `api_doc_required`
- `data_doc_required`
- `runtime_doc_required`
- `authorization_doc_required`
- `verification_doc_required`
- `tests_required`
- `approval_required`
- `rollback_required`

Recommended defaults:

- `L2` and `L3` changes default to `contract_changed=true`
- API work defaults to `api_doc_required=true`
- schema or migration work defaults to `data_doc_required=true`
- runtime changes default to `runtime_doc_required=true`
- permission or auth-boundary changes default to `authorization_doc_required=true`
- verification or release-gate changes default to `verification_doc_required=true`
- `L3` changes default to `approval_required=true`
- infrastructure work should strongly consider `rollback_required=true`

## Plan Rules

- keep plans implementation-facing, not aspirational
- name the invariant or contract each step protects
- prefer small ordered steps over broad themes
- update the plan if reality changes
- do not mark a step complete until the relevant tests pass
- if HTTP contract or user-facing flow changes, update `docs/api/API_CONTRACT.md` before closing the plan
- if schema or persistence semantics change, update `docs/data/DATA_CONTRACT.md` before closing the plan
- if runtime behavior changes, update `docs/runtime/RUNTIME_BASELINE.md` and `.agent/RUNTIME.md` before closing the plan
- if auth or permission boundaries change, update `docs/ops/AUTHORIZATION_BASELINE.md` before closing the plan
- if verification or release-gate rules change, update `docs/ops/VERIFICATION_BASELINE.md` before closing the plan
- if a new invariant or failure class is introduced, register it in `.agent/INVARIANTS.md`
