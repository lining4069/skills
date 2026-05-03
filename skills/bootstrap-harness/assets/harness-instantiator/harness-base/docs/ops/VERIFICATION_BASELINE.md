# Verification Baseline

Date: `[YYYY-MM-DD]`

## Purpose

This file is the repository's text contract for the verification plane.

It explains how the project proves that its harness, runtime, and contracts have not drifted or silently failed.

## When To Update This File

Update this file when work changes:

- release gates
- regression expectations
- trace requirements
- log semantics
- metrics semantics
- audit expectations
- eval expectations
- authorization or approval verification expectations

## Verification Surfaces

Document which verification surfaces exist today:

- regression tests
- contract tests
- traces
- logs
- metrics
- audits
- evals

If a surface does not exist yet, say so explicitly.

## Core Rules

### Regression

- describe what must be covered first

### Traceability

- describe what runtime information must be machine-readable

### Logs And Metrics

- describe which operator signals matter in the current phase

### Audits

- describe what needs to be reviewable for risky actions

### Evals

- describe whether eval-style verification exists yet

## Minimum Release Gates

Describe what must happen before work is considered complete for this repository.

Examples:

- targeted tests pass
- full suite passes for contract changes
- relevant contract docs updated
- traces or logs still preserve failure identity

## Current Baseline

Describe the current verification baseline in plain language.

## Planned Evolution

List the next verification upgrades expected after the current phase.

## Relationship To Other Documents

- `AGENTS.md` defines when this file must be updated
- `.agent/TESTING.md` defines test strategy
- `.agent/INVARIANTS.md` defines the invariants that verification should protect
