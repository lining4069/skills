# Invariants

This file is the named registry for invariants that the repository treats as non-negotiable.

Use stable IDs so plans, tests, reviews, and future enforcing automation can all refer to the same rule.

## Invariant Format

Each invariant entry should include:

- invariant id
- semantic meaning
- scope
- related tests
- related runtime or verification signals
- typical change types that should trigger a review of the invariant

## Template Entries

Replace these examples with project-specific invariants.

### INV-001 [Invariant Name]

- semantic meaning: describe the rule in one sentence
- scope: list the modules, boundaries, or workflows this applies to
- related tests: list the regression or contract tests that prove it
- related runtime or verification signals: list trace fields, logs, metrics, or audits that should reflect this invariant
- typical change types: list the kinds of changes that should force this invariant to be reviewed

### INV-002 [Invariant Name]

- semantic meaning: describe the rule in one sentence
- scope: list the modules, boundaries, or workflows this applies to
- related tests: list the regression or contract tests that prove it
- related runtime or verification signals: list trace fields, logs, metrics, or audits that should reflect this invariant
- typical change types: list the kinds of changes that should force this invariant to be reviewed

### INV-003 [Invariant Name]

- semantic meaning: describe the rule in one sentence
- scope: list the modules, boundaries, or workflows this applies to
- related tests: list the regression or contract tests that prove it
- related runtime or verification signals: list trace fields, logs, metrics, or audits that should reflect this invariant
- typical change types: list the kinds of changes that should force this invariant to be reviewed
