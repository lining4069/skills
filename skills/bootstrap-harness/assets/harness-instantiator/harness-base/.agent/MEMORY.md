# Memory

## Purpose

This file defines the repository-level memory strategy.

Use it to explain what information may persist across steps, sessions, threads, or long-running work.

## Memory Categories

Document which categories exist in this project:

- working memory: temporary task-local state
- session memory: state that persists for one active session or run
- project memory: repository-visible rules, preferences, and stable facts
- durable memory: intentionally persisted facts across tasks or users

## Core Rules

- repository-visible rules belong in repo files, not hidden memory stores
- temporary execution context should not silently become durable memory
- durable memory requires explicit semantics, ownership, and review
- corrections or preferences that change behavior should be reviewable

## Questions To Answer

1. What information is allowed to persist across steps
2. What information is allowed to persist across sessions
3. What information must stay in repo-visible files instead of hidden memory
4. What durable memory is intentionally out of scope in the current phase
5. How should memory-affecting changes be tested or observed

## Project Memory Strategy

Template:

### Repository-Visible Memory

- list the files that act as stable project memory

### Session Or Runtime Memory

- describe what temporary or session state exists

### Durable Memory

- describe whether durable memory exists yet

### Preferences And Corrections

- describe where these belong and who may change them

## Current Baseline

State the current memory baseline in plain language.

Examples:

- only repository-visible memory and in-process working memory exist today
- no durable memory yet
- corrections should be written back to repo-visible docs instead of hidden stores
