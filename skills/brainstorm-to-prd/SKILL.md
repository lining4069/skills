---
name: brainstorm-to-prd
description: "Turn a raw project idea into an approved `PRD.md` for the `project-bootstrap` workflow. Use this whenever a repo does not yet have an approved `PRD.md`, when a project concept is still fuzzy, or when an existing PRD needs revision before bootstrap documents can be generated."
---

# Brainstorm To PRD

This skill is the Stage A gate for the `project-bootstrap` workflow.

Its job is to turn a raw or partially formed idea into a repository-root `PRD.md` that can be explicitly approved and then used as the only upstream source of truth for bootstrap.

## Hard boundaries

- Do not write application code.
- Do not generate `PRODUCT_SPEC.md`.
- Do not generate `HARNESS_BOOTSTRAP.md`.
- Do not instantiate any harness files.
- Stop after `PRD.md` is approved or explicitly left in `Status: Draft` or `Status: Needs Review`.
- Ask one question at a time when clarifying.

## Required output

Produce or update:

- `PRD.md`

Use the shape from [PRD_TEMPLATE.md](references/PRD_TEMPLATE.md).

Use [SECTION_GUIDE.md](references/SECTION_GUIDE.md) when deciding what each PRD section should contain.

## Approval contract

`PRD.md` uses exactly these states:

- `Status: Draft`
- `Status: Needs Review`
- `Status: Approved`

Rules:

- start new PRDs in `Status: Draft`
- if the user requests substantive changes after a reviewable draft exists, move to `Status: Needs Review`
- only set `Status: Approved` after explicit user approval
- after approval, stop and hand the repo back to the next stage of `project-bootstrap`

## When to use this skill

Use this skill when:

- a new project starts from a raw idea
- `PRD.md` is missing
- `PRD.md` exists but is not approved
- `PRD.md` needs revision before bootstrap

## Workflow

### 1. Explore local context first

Before asking questions:

- inspect the current repo root
- read any existing `PRD.md`
- read `README.md` or other obvious top-level context files if present
- check whether the repo already contains partial bootstrap files that should not be treated as approved fact

The goal is to avoid asking questions whose answers already exist locally.

### 2. Assess scope

If the idea clearly contains multiple independent systems, say so early and decompose it.

Do not force one PRD to cover an obviously too-large platform.

If decomposition is needed:

- identify the candidate subprojects
- recommend which subproject should become the first PRD
- keep the current cycle focused on that first subproject

### 3. Clarify through dialogue

Ask one question at a time.

Prefer questions that help fill the PRD's missing decision points:

- what problem is being solved
- who the user is
- what this phase must ship
- what is out of scope
- what technical constraints already exist
- what first milestone should be used after bootstrap

If multiple-choice phrasing will reduce ambiguity, prefer it.

### 4. Propose 2-3 approaches

Before finalizing the PRD, present 2-3 ways to frame the project or phase.

This is not a UI mockup exercise. The goal is to choose the right project framing.

Examples of useful approach differences:

- narrow vertical slice vs broader foundation
- service-first vs workflow-first
- local-only MVP vs integration-ready MVP

Lead with your recommendation and explain why.

### 5. Present the PRD structure

Once the project framing is clear, present the PRD in sections scaled to the project's complexity.

Cover at least:

- problem
- target users
- goals
- non-goals
- current phase
- scope for this phase
- success criteria
- product constraints
- technical constraints
- architecture considerations
- first milestone candidate
- open questions

If a section is still uncertain, say so explicitly instead of inventing details.

### 6. Write or update `PRD.md`

When the conversation has produced enough clarity:

- write or update `PRD.md`
- keep it in `Status: Draft` until the user confirms it is ready for review
- use `Status: Needs Review` when the user asked for revisions to an already reviewable draft

### 7. Approval gate

After the user explicitly approves the PRD:

- update `PRD.md` to `Status: Approved`
- stop

Do not continue into bootstrap generation in the same uninterrupted push unless the user clearly asks to continue.

## Writing rules

- keep `PRD.md` product-facing and phase-aware
- make the first milestone concrete enough for later bootstrap
- keep non-goals explicit
- do not mix bootstrap mechanics into the PRD; that belongs in `HARNESS_BOOTSTRAP.md`
- if architecture intent matters, record it as a candidate, not a silently approved rule
- preserve useful existing wording when revising an existing PRD instead of rewriting it gratuitously

## If information is missing

If a blocking fact is missing and cannot be inferred safely:

- call it out as a short clarification point
- keep the relevant PRD section explicit about the uncertainty

Do not silently fabricate:

- target users
- first milestone
- external integration assumptions
- auth or approval needs

## Output report

When using this skill, report:

1. whether the repo was in raw-idea, draft-PRD, or revision mode
2. which PRD sections were clarified or revised
3. the current `PRD.md` status
4. whether the workflow must stop for review or is ready for approval
