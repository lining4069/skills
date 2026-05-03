# Authorization Baseline

Date: `[YYYY-MM-DD]`

## Purpose

This file is the repository's text baseline for authorization, permission boundaries, and approval-sensitive capability use.

It exists so auth and permission behavior do not remain implicit inside tool code, MCP configuration, or operator memory.

## When To Update This File

Update this file when work changes:

- auth boundary
- permission model
- approval requirement
- high-risk capability policy
- MCP scope or trust boundary
- workspace boundary rules
- third-party API access rules

## Baseline Questions

Each repository should answer these questions:

1. Which capabilities are allowed by default
2. Which capabilities are deny-by-default
3. Which actions require approval or HITL
4. Which external boundaries require auth scopes
5. Whether MCP is enabled and how its scope is bounded
6. What workspace boundary the agent must treat as trusted

## Current Baseline

Describe the current authorization baseline in plain language.

Template:

### Permission Model

- describe the current allow, deny, or review model

### Approval Model

- describe what requires explicit approval

### External Capability Scope

- describe which APIs, MCP servers, or integrations are allowed

### Workspace Boundary

- describe which directories or resources are in scope

### High-Risk Actions

- describe which classes of actions are blocked or require review

## Planned Evolution

List the next expected changes to auth, approval, or permission boundaries.

## Relationship To Other Documents

- `AGENTS.md` defines when this file must be updated
- `.agent/TOOLS.md` defines tool and integration rules
- `docs/runtime/RUNTIME_BASELINE.md` defines execution semantics, not permission semantics
- `docs/ops/VERIFICATION_BASELINE.md` defines how authorization behavior is verified
