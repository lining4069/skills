# Runtime Baseline

Date: `[YYYY-MM-DD]`

## Purpose

This file is the repository's text contract for runtime semantics.

Use it to make execution behavior visible in the repo instead of letting it live only in code or oral knowledge.

## When To Update This File

Update this file when work changes:

- execution model
- retry behavior
- budget behavior
- pause or resume behavior
- background or scheduled execution
- approval or HITL flow
- run lifecycle or trace identity
- concurrency assumptions
- lifecycle hooks or interceptors
- subagent or delegated-run behavior

## Runtime Contract Areas

Each repository should answer these topics in plain language.

### Execution Model

- request-response only
- async boundary plus sync core
- job or queue backed
- long-running background execution

### Retry And Budget

- who owns retries
- who owns budgets or timeouts
- what is bounded and how

### Pause, Resume, And Checkpoints

- whether these exist
- which state transitions are valid

### Approval Or HITL

- whether approval exists
- who blocks on approval
- what happens on deny, timeout, or missing approval

### Scheduling And Automations

- whether scheduled or repeated work exists
- what identity or state persists across runs

### Lifecycle Hooks Or Interceptors

- whether lifecycle hooks, middleware, or pre/post tool interceptors exist

### Subagents Or Delegated Runs

- whether role-specific agents or delegated runs exist
- what boundaries they must respect

### Concurrency

- whether multiple runs can overlap
- which layer owns coordination

### Trace And Run Identity

- what identifiers must exist
- what machine-readable failure information must be preserved

## Current Baseline

Describe the current runtime baseline in plain language.

If a runtime feature does not exist yet, say so explicitly rather than leaving the section ambiguous.

## Planned Evolution

List the next runtime upgrades expected after the current phase.

## Relationship To Other Documents

- `AGENTS.md` defines when this file must be updated
- `.agent/RUNTIME.md` defines repository-level runtime governance
- `docs/ops/VERIFICATION_BASELINE.md` covers how runtime behavior is observed and validated
- `docs/ops/AUTHORIZATION_BASELINE.md` covers permission boundaries, not execution behavior
