# Implementation Status

This file tracks how much of the target architecture is implemented in the current repository.

Status labels:

- `implemented`: working code or working repository behavior exists
- `partial`: a minimal or placeholder version exists
- `planned`: intentionally not implemented yet

## Target Architecture

Describe the target architecture for this project.

Template:

- control plane: instructions, plans, invariants, review rules
- contract plane: API, data, and design contracts
- runtime plane: execution model, retries, approvals, scheduling, tracing
- capability plane: tools, adapters, MCP, third-party integrations
- memory plane: working, session, project, and durable memory
- verification plane: tests, traces, logs, metrics, audits, evals

## Project Architecture Rule

Record the approved project-wide architecture rule here.

Examples:

- `async boundary + sync core`
- `workers own external effects`

## Harness Governance Status

| Governance Component | Status | Notes | Primary Locations |
|------|--------|-------|-------------------|
| Change level model | implemented | `L0` through `L3` are defined in the control plane | `AGENTS.md`, `.agent/PLANS.md` |
| Active plan metadata | implemented | `L2` and `L3` plans use structured governance fields | `.agent/PLANS.md`, `.agent/active-plans/` |
| Invariant registry | partial | Replace the template entries with project-specific invariants | `.agent/INVARIANTS.md`, `tests/` |
| Runtime baseline | partial | Replace the template runtime baseline with the actual execution model | `.agent/RUNTIME.md`, `docs/runtime/RUNTIME_BASELINE.md` |
| Authorization baseline | partial | Replace the template auth baseline with the actual permission and approval model | `docs/ops/AUTHORIZATION_BASELINE.md`, `.agent/TOOLS.md` |
| Memory strategy | partial | Replace the template memory baseline with project-specific rules | `.agent/MEMORY.md` |
| Verification baseline | partial | Replace the template verification baseline with project-specific release gates | `.agent/TESTING.md`, `docs/ops/VERIFICATION_BASELINE.md` |
| Automatic enforcing | planned | Add scripts or CI only after the manual workflow stabilizes | N/A |

## Status Matrix

Create the matrix that fits the repository.

Template:

| Plane | Component | Status | Notes | Primary Locations |
|------|-----------|--------|-------|-------------------|
| Control | Root instructions and governance | planned | Replace with actual status | `AGENTS.md`, `.agent/` |
| Contract | API and data contracts | planned | Replace with actual status | `docs/api/`, `docs/data/` |
| Runtime | Execution model and orchestration | planned | Replace with actual status | `docs/runtime/`, runtime code |
| Capability | Tools and integrations | planned | Replace with actual status | adapters, tools, integrations |
| Memory | Session, working, or durable memory | planned | Replace with actual status | `.agent/MEMORY.md`, code |
| Verification | Tests, logs, traces, metrics, evals | planned | Replace with actual status | `tests/`, `docs/ops/` |

## What Is Already Proven

List the minimum end-to-end path the repository can already prove today.

## What Is Intentionally Deferred

List the major items intentionally left for later.

## Near-Term Upgrade Path

List the most important next additions in recommended order.
