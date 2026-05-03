# Runtime

## Purpose

This file defines the repository-level runtime expectations.

Use it to explain how work executes over time, where retries and approvals live, and what the runtime is expected to preserve.

## Harness Versus Runtime

The harness is the repository-visible control system.
The runtime is the execution substrate.

The harness can exist before the runtime is sophisticated, but the repository should still record which runtime behaviors exist today.

## When To Update This File

Update this file when work changes:

- execution model
- sync versus async boundary decisions
- retry ownership
- budget ownership
- pause or resume behavior
- background or scheduled execution
- approval or HITL boundaries
- tracing or run lifecycle semantics
- lifecycle hooks or interceptors
- subagent or delegated-run boundaries

## Runtime Governance Questions

Document the answers for this repository:

1. What executes synchronously and what executes asynchronously
2. Which layer owns retries
3. Which layer owns budgets or timeouts
4. Whether pause or resume exists
5. Whether background execution exists
6. Whether scheduling or automations exist
7. Whether approval or HITL exists
8. What trace or run identity must be recorded
9. Whether lifecycle hooks or interceptors exist
10. Whether subagents or delegated roles exist

## Project Runtime Profile

Template:

### Execution Model

- describe the top-level execution model

### Retry And Budget Rules

- describe retry ownership
- describe budget ownership

### Pause, Resume, And Checkpoints

- describe whether these exist yet

### Approval Or HITL

- describe whether approval exists yet and where it is enforced

### Background Or Scheduled Work

- describe whether background work exists yet

### Lifecycle Hooks Or Interceptors

- describe whether lifecycle hooks, middleware, or tool interceptors exist yet

### Subagents Or Delegated Roles

- describe whether role-specific agents or delegated workers exist yet

### Trace Identity

- describe what execution metadata must be preserved

## Current Runtime Baseline

State the current runtime baseline in plain language.

Examples:

- request/response only, no background work yet
- async boundaries at API and adapter edges, sync core logic
- no pause or resume yet
- retries owned by the runtime loop

## Relationship To Other Files

- `AGENTS.md` defines when runtime changes require doc updates
- `docs/runtime/RUNTIME_BASELINE.md` is the text contract for runtime semantics
- `.agent/TESTING.md` describes how runtime invariants should be verified
