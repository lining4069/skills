# PRD Section Guide

Use this guide when drafting or revising `PRD.md`.

## Section intent

### Title

Use a stable, human-readable project or phase name.

### Problem

State the problem in outcome terms:

- what is painful today
- why now
- what goes wrong if nothing changes

### Target Users

Identify the primary user first.

For personal tools, it is acceptable to say the primary user is the solo developer, but still explain what result they want.

### Goals

List the outcomes the current project should achieve.

Goals are not implementation tasks.

### Non-Goals

Say what this phase will not do.

This is especially important for keeping later bootstrap and first plans bounded.

### Current Phase

Describe the repository's current stage, not the full long-term vision.

### Scope For This Phase

List the deliverables or capabilities expected before the phase is complete.

### Success Criteria

Prefer observable completion signals:

- a contract exists
- an endpoint works
- a test suite passes
- a milestone artifact exists

### Product Constraints

List product or workflow constraints, such as:

- single-user first
- local-only first
- service-only first

### Technical Constraints

List concrete technical decisions already known and likely to affect bootstrap.

### Architecture Considerations

Record architecture intent that later phases may turn into approved project rules.

Do not over-specify if the user has not decided yet.

### First Milestone Candidate

This section must be specific enough that `HARNESS_BOOTSTRAP.md` can point to a first implementation milestone without guessing.

### Open Questions

Keep unresolved but important questions visible.

### Approval Notes

Record how or when the PRD was approved, revised, or re-scoped.
