# Architecture

## Intent

This file explains how the repository is shaped and which boundaries matter.

Keep it structural. Do not turn it into a changelog.

## Harness Versus Runtime

Treat these as related but distinct:

- `harness`: the repository-visible control system around the agent or codebase
- `runtime`: the execution substrate that carries work over time

Examples of harness concerns:

- instructions
- plans
- contracts
- review priorities
- invariants

Examples of runtime concerns:

- execution model
- retries
- checkpoints
- background work
- scheduling
- approvals
- tracing

Projects can have a strong harness before they have a sophisticated runtime.

## Bootstrap Inputs

If present, these files explain why the repository exists and how it was first instantiated:

- `PRODUCT_SPEC.md`
- `HARNESS_BOOTSTRAP.md`

## Control Plane

The control plane lives in repository files:

- `AGENTS.md` defines the top-level operating contract
- `.agent/*.md` define planning, architecture, testing, invariant, runtime, memory, tool, and review expectations
- `.agent/IMPLEMENTATION_STATUS.md` tracks what is implemented, partial, or planned
- `docs/api/API_CONTRACT.md` defines text interface semantics
- `docs/data/DATA_CONTRACT.md` defines schema, migration, rollback, and persistence semantics
- `docs/runtime/RUNTIME_BASELINE.md` defines runtime behavior expectations
- `docs/ops/AUTHORIZATION_BASELINE.md` defines auth, permission, and workspace-boundary expectations
- `docs/ops/VERIFICATION_BASELINE.md` defines verification and release-gate expectations
- `docs/specs/` stores approved design decisions

## Control-Plane Taxonomy

Use these categories:

- stable governance rules: `AGENTS.md`, `.agent/ARCHITECTURE.md`, `.agent/TESTING.md`, `.agent/TOOLS.md`, `.agent/RUNTIME.md`, `.agent/MEMORY.md`
- temporary execution artifacts: `.agent/active-plans/*.md`
- current-state artifacts: `.agent/IMPLEMENTATION_STATUS.md`
- design and contract artifacts: `docs/specs/*.md`, `docs/api/API_CONTRACT.md`, `docs/data/DATA_CONTRACT.md`, `docs/runtime/RUNTIME_BASELINE.md`, `docs/ops/AUTHORIZATION_BASELINE.md`, `docs/ops/VERIFICATION_BASELINE.md`

This split helps prevent high-drift facts from polluting stable rules.

## Six-Layer Harness Model

Use this model unless the project has a better documented alternative:

### Control Plane

- root instructions
- planning rules
- invariants
- review rules

### Contract Plane

- API contract
- data contract
- design specs

### Runtime Plane

- execution model
- retries
- pause or resume
- background work
- approval or HITL
- tracing

### Capability Plane

- tools
- MCP
- adapters
- third-party APIs
- plugins
- authorization boundaries

### Authorization And Boundary Layer

- permission model
- approval model
- workspace boundary
- high-risk capability policy

### Memory Plane

- working memory
- session memory
- project memory
- durable memory

### Verification Plane

- regression tests
- contract tests
- evals
- logs
- metrics
- audits

## Project Architecture Rules

Document the project's real architecture rules here.

Examples:

- `async boundary + sync core`
- `read path stays side-effect free`
- `external effects only happen through workers`
- `runtime owns retries and checkpoint transitions`

If not decided yet, say so explicitly.

## Repository Layer Map

Describe the actual layers of the repository.

Template:

### Interface Layer

- list the directories or files
- explain what enters or leaves the system here

### Core Logic Layer

- list the directories or files
- explain which state transitions or business rules live here

### Capability Layer

- list the directories or files
- explain how tools or external capabilities are invoked

### State And Persistence Layer

- list the directories or files
- explain what is stored and at which boundary

### Runtime And Coordination Layer

- list the directories or files
- explain where retries, approvals, scheduling, and execution orchestration live

### Verification Layer

- list the directories or files
- explain which contracts the tests protect

## First-Version Choices

List the major scoping choices that define the current project phase.

Examples:

- single agent only
- no distributed workers yet
- local database first
- deterministic stubs before live integrations
- no durable memory before runtime contract stabilizes
