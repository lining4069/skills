# AGENTS.md

## Mission

Describe the project mission here.

Recommended prompts:

- What is this repository trying to prove or deliver?
- What does the current phase need to ship?
- Why does this project benefit from explicit harness rules?

Example placeholder:

- build `[PROJECT_NAME]` with repository-visible contracts, bounded execution, and explicit verification

## Non-Goals

List what the repository explicitly does not aim to provide in the current phase.

Examples:

- no multi-agent orchestration in the initial phase
- no production-grade auth in the initial phase
- no long-term memory before the runtime contract is stable

## Bootstrap Inputs

If these files exist, they are part of the project's initial intent:

1. `PRODUCT_SPEC.md`
2. `HARNESS_BOOTSTRAP.md`

`PRODUCT_SPEC.md` explains product or project intent.

`HARNESS_BOOTSTRAP.md` explains how the harness was supposed to be instantiated and what the first milestone is.

## Required Reading Before Work

Always read these before making non-trivial changes:

1. `PRODUCT_SPEC.md` if present
2. `HARNESS_BOOTSTRAP.md` if present and the work is still near bootstrap scope
3. `.agent/ARCHITECTURE.md`
4. `.agent/INVARIANTS.md`
5. `.agent/IMPLEMENTATION_STATUS.md`
6. `.agent/PLANS.md`
7. `.agent/TESTING.md`
8. `.agent/RUNTIME.md`
9. `.agent/MEMORY.md`
10. `docs/api/API_CONTRACT.md` when touching API behavior, parameter semantics, or user-facing flow
11. `docs/data/DATA_CONTRACT.md` when touching schema, persistence semantics, migrations, or rollback expectations
12. `docs/runtime/RUNTIME_BASELINE.md` when touching execution model, retries, scheduling, approval, or tracing behavior
13. `docs/ops/AUTHORIZATION_BASELINE.md` when touching permissions, approvals, MCP scopes, workspace boundaries, or third-party auth behavior
14. `docs/ops/VERIFICATION_BASELINE.md` when touching logs, metrics, evals, audits, or release gates
15. the active plan in `.agent/active-plans/` if one exists
16. the nearest nested `AGENTS.md` in the directory you are editing

Delete or adjust entries that do not apply to the new project.

## Change Levels

Use these levels to decide how much process is required:

- `L0`: text-only or behavior-neutral cleanup with no contract change
- `L1`: local implementation work inside one subsystem with no API, runtime, data, or verification contract change
- `L2`: cross-module or contract-level change, including API semantics, runtime contract changes, memory behavior changes, or new failure classes
- `L3`: high-risk governance or infrastructure change, including schema or migration work, approval or policy systems, permissions, automations, background execution, or new enforcing automation

Expected process intensity:

- `L0` usually does not require an active plan or full change report
- `L1` can use a lighter work note and targeted tests
- `L2` requires an active plan, explicit contract impact, and related doc updates
- `L3` requires an active plan, rollback notes, contract docs, and explicit human approval before implementation

## When Planning Is Mandatory

You must write or update an execution plan before coding when any of the following is true:

- the change is `L2` or `L3`
- the change spans more than one subsystem
- the runtime contract changes
- the memory strategy changes
- a new tool type or integration is introduced
- a new failure mode or recovery path is introduced
- verification or release-gate behavior changes
- the change requires more than one test file

Use `.agent/PLANS.md` as the format contract and keep active plans in `.agent/active-plans/`.

## Project-Specific Architecture Rules

Write the architecture rules that truly belong to this project.

Examples:

- `async boundary + sync core`
- `only adapters may cross third-party network boundaries`
- `runtime owns retries and checkpoints`
- `workers own external effects`

If the project has no special rule yet, write `No project-specific architecture rule has been approved yet.`

## Documentation As Harness

Text contract documentation is part of the harness, not an optional afterthought.

Atomic rules:

- if API semantics change, update `docs/api/API_CONTRACT.md` in the same change
- if schema, migration, or persistence semantics change, update `docs/data/DATA_CONTRACT.md` in the same change
- if runtime execution behavior changes, update `docs/runtime/RUNTIME_BASELINE.md` and `.agent/RUNTIME.md` in the same change
- if memory strategy changes, update `.agent/MEMORY.md` in the same change
- if permission or approval boundaries change, update `docs/ops/AUTHORIZATION_BASELINE.md` in the same change
- if verification or release-gate behavior changes, update `docs/ops/VERIFICATION_BASELINE.md` in the same change
- if governance rules change, update the relevant `.agent/` or `AGENTS.md` files in the same change

When API work changes:

- endpoint purpose
- parameter semantics
- response semantics
- runtime behavior
- failure behavior
- user-facing flow

you must update `docs/api/API_CONTRACT.md` before calling the work complete.

When schema or persistence work changes:

- storage shape or meaning
- migration behavior
- schema version expectations
- rollback expectations
- backfill expectations

you must update `docs/data/DATA_CONTRACT.md` before calling the work complete.

When runtime work changes:

- execution model
- retries or budgets
- background or scheduled execution
- pause or resume behavior
- approval or HITL gates
- trace identity or run lifecycle

you must update `docs/runtime/RUNTIME_BASELINE.md` before calling the work complete.

## Project Invariants

List the repository's non-negotiable invariants here in short form.

Examples:

- every request must have an explicit budget or timeout
- invalid external payloads must never enter trusted state
- denied actions must never look like success
- terminal states must be explicit
- runtime traces must preserve machine-readable failure identity

The authoritative registry for named invariants lives in `.agent/INVARIANTS.md`.

## Validation Checklist

Before considering work complete:

1. run the targeted regression tests first
2. run the full test suite if a contract changed
3. verify the public interface still reflects internal state faithfully
4. update `.agent/` docs if architecture, runtime, memory, or workflow changed
5. update `docs/api/API_CONTRACT.md` if API behavior, semantics, or user flow changed
6. update `docs/data/DATA_CONTRACT.md` if schema, persistence semantics, migration, rollback, or backfill expectations changed
7. update `docs/runtime/RUNTIME_BASELINE.md` if execution model, retries, scheduling, approval, or tracing semantics changed
8. update `docs/ops/AUTHORIZATION_BASELINE.md` if permission, approval, MCP scope, or workspace-boundary semantics changed
9. update `docs/ops/VERIFICATION_BASELINE.md` if verification expectations or release gates changed
10. record any new invariant or failure class in `.agent/INVARIANTS.md` and tests before adding more features

## Change Reporting Format

When reporting work, include:

1. what contract or invariant changed
2. what tests were added or updated
3. what runtime, memory, or system paths were affected
4. what remains intentionally out of scope

For `L0` changes, a short summary is enough if no contract changed.

## Directory Map

Describe the actual top-level project layout here.

Template:

- `src/` or `[MAIN_CODE_DIR]/`: main application code
- `tests/`: tests
- `.agent/`: repository control-plane documents
- `docs/api/`: text API contract documents
- `docs/data/`: text data contract documents
- `docs/runtime/`: text runtime baseline documents
- `docs/ops/`: verification and operations baseline documents
- `docs/specs/`: approved design documents

## Control-Plane Index

- `.agent/ARCHITECTURE.md`: architecture layers and repository boundaries
- `.agent/INVARIANTS.md`: named invariants and their test mappings
- `.agent/IMPLEMENTATION_STATUS.md`: current coverage of the target architecture
- `.agent/PLANS.md`: plan contract for multi-step work
- `.agent/TESTING.md`: contract testing strategy
- `.agent/TOOLS.md`: tool and integration design rules
- `.agent/RUNTIME.md`: repository-level runtime governance
- `.agent/MEMORY.md`: repository-level memory strategy
- `.agent/CODE_REVIEW.md`: review priorities
- `docs/api/API_CONTRACT.md`: text interface contract
- `docs/data/DATA_CONTRACT.md`: text data contract
- `docs/runtime/RUNTIME_BASELINE.md`: text runtime contract
- `docs/ops/AUTHORIZATION_BASELINE.md`: text authorization and permission baseline
- `docs/ops/VERIFICATION_BASELINE.md`: text verification contract

Add project-specific indexes after bootstrap.

## Local Overrides

List nested `AGENTS.md` files here only if they actually exist.

Example:

- `backend/AGENTS.md`
- `workers/AGENTS.md`

If there are none, write `No nested AGENTS.md files yet.`
