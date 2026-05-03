# Testing

## Testing Strategy

This repository uses contract-first testing.

The first job of tests is not to prove that the system is impressive.
The first job is to prove that the system does not violate its own control rules, runtime rules, or verification expectations.

## Priority Order

1. regression tests for system invariants
2. focused tests for runtime and state transitions
3. public interface and contract tests
4. broader integration tests
5. eval-style or scenario tests when the system reaches enough maturity

Adjust this order if the project has a different risk profile, but write the reason down.

## Mandatory Invariants

The regression suite must cover the most dangerous failure boundaries in the project.

Examples:

- invalid input must not enter trusted state
- denied actions must not masquerade as success
- retries, budgets, or loops must remain bounded
- trace, logs, or audit records must preserve machine-readable failure information
- runtime transitions must not skip approval or terminal-state rules

The named source of truth for these invariants is `.agent/INVARIANTS.md`.

## Verification Plane Relationship

Tests are only one part of the verification plane.

Also consider:

- traces
- logs
- metrics
- audits
- evals

If these change meaningfully, update `docs/ops/VERIFICATION_BASELINE.md`.

## Test Design Rules

- prefer deterministic stubs over live integrations when proving contracts
- assert on contracts, state transitions, and failure identity
- keep failure reasons machine-readable
- do not couple tests to prompt wording
- when possible, map regression coverage back to invariant IDs from `.agent/INVARIANTS.md`
- when runtime behavior matters, assert on both final state and the execution trace

## Red-Green Discipline

- write the failing test first
- run it and confirm it fails for the expected reason
- implement the smallest change that makes it pass
- refactor only after green
