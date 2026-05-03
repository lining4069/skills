---
name: prd-to-bootstrap
description: "Generate `PRODUCT_SPEC.md` and `HARNESS_BOOTSTRAP.md` from an approved `PRD.md`. Use this as the document-derivation stage inside the `project-bootstrap` workflow whenever a repo already has an approved PRD but lacks bootstrap docs, or when the bootstrap docs need to be backfilled from the PRD without guessing missing decisions."
---

# PRD To Bootstrap

This skill converts an approved `PRD.md` into the two bootstrap artifacts that directly feed harness instantiation.

## Hard boundaries

- `PRD.md` must exist.
- `PRD.md` must include `Status: Approved`.
- If the PRD is missing critical decisions, return a `待澄清项` list first.
- Do not invent high-impact decisions.
- Do not overwrite approved or user-edited content wholesale.

## Preferred template sources

Use template sources in this order:

1. the bundled references in this skill:
   - [PRODUCT_SPEC_TEMPLATE.md](references/PRODUCT_SPEC_TEMPLATE.md)
   - [HARNESS_BOOTSTRAP_TEMPLATE.md](references/HARNESS_BOOTSTRAP_TEMPLATE.md)
2. a project-local `harness-instantiator/templates/` directory if it is discoverable from the current workspace

## Required precondition

If `PRD.md` does not contain `Status: Approved`, stop and send the workflow back to the `project-bootstrap` stage.

## What each output is for

### `PRODUCT_SPEC.md`

This is the distilled product or project execution document.

Keep:

- project goal
- current phase goal
- scope
- non-goals
- functional requirements
- non-functional requirements
- technical constraints
- success criteria

Do not turn it into a second PRD.

### `HARNESS_BOOTSTRAP.md`

This is the harness instantiation document.

Keep:

- target repo path
- instantiator source path
- project type
- primary stack
- instantiate scope
- architecture rule candidates
- permissions and approval boundaries
- first milestone
- bootstrap constraints

Do not duplicate broad product discussion here.

## Missing-decision rules

Before writing either file, inspect whether these decisions are available from the PRD or current repo context:

- project type
- primary stack
- current phase goal
- first milestone
- main non-goals

Use [REQUIRED_FIELDS.md](references/REQUIRED_FIELDS.md) to decide what is blocking.

If any blocking field is missing:

- do not generate final bootstrap docs
- return a short `待澄清项` section
- explain why each missing decision blocks deterministic doc generation

## Update behavior

- if one bootstrap file already exists, only fill missing sections or fix clearly templated placeholders
- if both files already exist, do not overwrite them unless the user explicitly asked for regeneration
- preserve approved repo-specific wording where possible

## Recommended writing process

1. Read `PRD.md`.
2. Read any existing `PRODUCT_SPEC.md` or `HARNESS_BOOTSTRAP.md`.
3. Extract only the facts needed for each target document.
4. Fill `PRODUCT_SPEC.md`.
5. Fill `HARNESS_BOOTSTRAP.md`.
6. If there are non-blocking unresolved questions, add a short `Known Open Questions` section at the end of `HARNESS_BOOTSTRAP.md`.

## Output report

When finished, report:

1. whether the PRD was approved
2. what files were created or updated
3. any `待澄清项`
4. whether the repo is now ready for harness instantiation
