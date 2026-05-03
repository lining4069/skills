# Data Contract

Date: `[YYYY-MM-DD]`

## Purpose

This file is the repository's text contract for persistence semantics.

It exists so schema work, storage behavior, and migration work are governed by an explicit contract rather than hidden in implementation details.

## Scope

Update this file when work changes:

- schema shape or field meaning
- persistence boundaries
- schema version expectations
- migration behavior
- backward compatibility expectations
- rollback expectations
- backfill expectations

## Core Rules

### Schema Version

- describe how the project versions persistence changes

### Migration

- describe how schema changes are introduced and reviewed

### Backward Compatibility

- describe what compatibility means for this repository

### Rollback

- describe what rollback means for high-risk persistence changes

### Backfill

- describe when and how backfill is allowed

## Current Baseline

Describe the current persistence baseline.

Examples:

- database choice
- snapshot vs normalized storage
- whether migrations exist yet

## Planned Evolution

List the most likely next persistence changes.

## Relationship To Other Documents

- `AGENTS.md` defines when this file must be updated
- `docs/api/API_CONTRACT.md` covers interface semantics, not persistence semantics
- `docs/specs/*.md` capture approved design decisions for specific schema changes
