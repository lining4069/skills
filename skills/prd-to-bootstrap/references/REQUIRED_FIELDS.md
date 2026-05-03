# Required Fields For Bootstrap Generation

Use this file to decide whether `PRD.md` is sufficient to generate bootstrap docs.

## Blocking fields

If any of these are missing, stop and return `待澄清项`:

- current phase goal
- project type
- first milestone
- primary stack or implementation family
- non-goals for the current phase

## Usually discoverable from the environment

Do not ask the user first if these can be discovered:

- target repo path
- whether a bundled `bootstrap-harness` snapshot is available
- whether a sibling `harness-instantiator/` exists
- whether the repo already contains partial harness files

When bootstrap docs are generated from a normal installed workflow, prefer these semantic values instead of machine-specific absolute paths:

- `target repo path: current repo root`
- `product spec path: PRODUCT_SPEC.md`
- `instantiator source path: bundled skill asset`

## Safe defaults for first version

These defaults are allowed if the PRD does not contradict them:

- control plane: `yes`
- contract plane: `yes`
- runtime plane: `yes`
- capability plane: `yes`
- memory plane: `yes`
- verification plane: `yes`
- authorization baseline now: `yes`
- code skeleton now: `no`
