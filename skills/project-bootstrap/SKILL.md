---
name: project-bootstrap
description: "Orchestrate the pre-coding workflow for a new project: raw idea -> approved `PRD.md` -> `PRODUCT_SPEC.md` and `HARNESS_BOOTSTRAP.md` -> harness instantiation -> first action plan. Use this whenever a user wants to start a repository from an idea, prepare AI-coding bootstrap documents, or resume a partially bootstrapped repo without guessing the next step."
---

# Project Bootstrap

This is the public entry-point skill for the `project-bootstrap` workflow.

Its job is to detect the current stage of a project and drive it forward to the next valid artifact.

## Hard boundaries

- Do not write application code.
- Stop at the first action plan.
- Do not skip the PRD brainstorming gate when there is no approved `PRD.md`.
- Do not instantiate harness files before `PRODUCT_SPEC.md` and `HARNESS_BOOTSTRAP.md` exist.

## Canonical artifact chain

1. raw idea
2. `PRD.md`
3. `PRODUCT_SPEC.md`
4. `HARNESS_BOOTSTRAP.md`
5. instantiated harness
6. first action plan

The chain has one upstream source of truth:

- `PRD.md`

## PRD approval convention

`PRD.md` is only approved when one of the first 40 lines contains the exact text:

`Status: Approved`

Use these states:

- `Status: Draft`
- `Status: Needs Review`
- `Status: Approved`

If the file exists but is not approved, treat the project as still being in the PRD stage.

Use [PRD_TEMPLATE.md](references/PRD_TEMPLATE.md) for the expected document shape.

## Stage detection

Inspect the current project root and classify it into one stage only.

### Stage A: Idea -> PRD

Use this stage when:

- `PRD.md` does not exist, or
- `PRD.md` exists but is not approved

Required action:

- use the `brainstorm-to-prd` skill as a hard gate
- create or update `PRD.md`
- keep it at `Status: Draft` or `Status: Needs Review` until the user explicitly approves it
- after explicit user approval, update it to `Status: Approved`

Stop after the PRD is approved. Do not continue into bootstrap generation in the same uninterrupted push unless the user clearly wants to continue.

### Stage B: PRD -> Bootstrap Docs

Use this stage when:

- `PRD.md` is approved, and
- either `PRODUCT_SPEC.md` or `HARNESS_BOOTSTRAP.md` is missing

Required action:

- invoke the `prd-to-bootstrap` skill

### Stage C: Bootstrap Docs -> Harness

Use this stage when:

- `PRD.md` is approved
- `PRODUCT_SPEC.md` exists
- `HARNESS_BOOTSTRAP.md` exists
- the repo does not yet contain a fully instantiated harness

Treat the harness as missing if any of these are absent:

- `AGENTS.md`
- `.agent/ARCHITECTURE.md`
- `.agent/PLANS.md`
- `.agent/INVARIANTS.md`
- `.agent/RUNTIME.md`
- `.agent/MEMORY.md`
- `docs/api/API_CONTRACT.md`
- `docs/data/DATA_CONTRACT.md`
- `docs/runtime/RUNTIME_BASELINE.md`
- `docs/ops/AUTHORIZATION_BASELINE.md`
- `docs/ops/VERIFICATION_BASELINE.md`

Required action:

- invoke the `bootstrap-harness` skill

### Stage D: Harness -> First Action Plan

Use this stage when:

- the harness is fully instantiated, and
- `.agent/active-plans/` has no real plan yet

Treat the first plan as missing when there is no `.md` file under `.agent/active-plans/` other than copied examples or placeholders.

Required action:

- invoke the `first-plan-seeder` skill

### Stage E: Flow Complete

Use this stage when:

- `PRD.md` is approved
- bootstrap docs exist
- harness exists
- at least one real plan exists under `.agent/active-plans/`

Required action:

- report that the workflow is complete
- summarize the current state
- tell the user the repo is ready for normal harness-guided development

## Operating rules

- always read the current repo before choosing the stage
- never jump ahead by guessing missing artifacts
- preserve existing approved artifacts unless the user asks to revise them
- if the repo contains both `PROJECT_SPEC.md` and `PRODUCT_SPEC.md`, treat `PRODUCT_SPEC.md` as canonical and call out the mismatch
- treat helper skills as implementation details of this workflow; the user can install them separately, but this skill is the recommended public starting point

## Output format

When using this skill, report back in this format:

1. detected stage
2. artifacts found
3. missing artifacts or blocking decisions
4. next action taken
5. current stop point
