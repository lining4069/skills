---
name: bootstrap-harness
description: "Instantiate a repo harness from `PRODUCT_SPEC.md`, `HARNESS_BOOTSTRAP.md`, and a `harness-instantiator` source or bundled snapshot. Use this in the `project-bootstrap` workflow whenever bootstrap docs exist and you need to create the repo control plane, contracts, runtime baselines, authorization baseline, verification baseline, and optional Claude/Copilot/Cursor compatibility files without touching application code."
---

# Bootstrap Harness

This skill turns bootstrap documents into a real repository harness.

## Hard boundaries

- treat the `harness-instantiator` as read-only
- only write inside the target repo
- do not generate application code in v1
- if `code skeleton now: yes` appears in `HARNESS_BOOTSTRAP.md`, defer that work into the first action plan instead of writing code now

## Required inputs

- `PRODUCT_SPEC.md`
- `HARNESS_BOOTSTRAP.md`
- either a readable `harness-instantiator` source or the bundled `assets/harness-instantiator/` snapshot shipped with this skill

If either bootstrap document is missing, stop and route back to `prd-to-bootstrap`.

## Resolving the instantiator source

Resolve the source in this order:

1. `instantiator source path` from `HARNESS_BOOTSTRAP.md`
2. the bundled snapshot at `assets/harness-instantiator/` inside the installed skill directory
3. a sibling directory named `harness-instantiator/`
4. a parent-sibling directory named `../harness-instantiator/`

If none of these exist, stop and report the missing source path instead of guessing.

## Files to instantiate

Create or update these repo files:

- `AGENTS.md`
- `.agent/ARCHITECTURE.md`
- `.agent/PLANS.md`
- `.agent/TESTING.md`
- `.agent/INVARIANTS.md`
- `.agent/IMPLEMENTATION_STATUS.md`
- `.agent/TOOLS.md`
- `.agent/RUNTIME.md`
- `.agent/MEMORY.md`
- `docs/api/API_CONTRACT.md`
- `docs/data/DATA_CONTRACT.md`
- `docs/runtime/RUNTIME_BASELINE.md`
- `docs/ops/AUTHORIZATION_BASELINE.md`
- `docs/ops/VERIFICATION_BASELINE.md`

Create the directory `.agent/active-plans/`, but do not copy example action plans into the target repo.

## Projectization rules

When instantiating:

- fill mission and non-goals from `PRODUCT_SPEC.md`
- fill current phase and first milestone from `HARNESS_BOOTSTRAP.md`
- fill architecture rule candidates from `HARNESS_BOOTSTRAP.md`
- fill permission and approval boundaries from `HARNESS_BOOTSTRAP.md` section `6.1`
- preserve any existing project-specific repo text unless it is still a raw template placeholder

## Optional compatibility outputs

Only generate these when `HARNESS_BOOTSTRAP.md` explicitly asks for them:

- root `CLAUDE.md`
- `.github/copilot-instructions.md`
- `.cursor/rules/project-bootstrap.mdc`

Use templates from the resolved `harness-instantiator/templates/` directory when available. If a project-local source is absent, use the bundled snapshot.

## Authorization and approval requirements

The authorization layer is mandatory in this workflow.

Do not leave `docs/ops/AUTHORIZATION_BASELINE.md` as a blank shell if:

- the project will call third-party APIs
- the project will use MCP
- the project will introduce high-risk write actions
- the project will need approval gates

If these decisions are not known yet, record that explicitly rather than leaving them ambiguous.

## Completion criteria

The harness is considered instantiated only when all required files exist and are projectized enough that they are no longer raw templates.

## Output report

When finished, report:

1. which files were created or updated
2. which optional compatibility files were generated
3. any deferred `code skeleton now` request
4. whether the repo is ready for `first-plan-seeder`
