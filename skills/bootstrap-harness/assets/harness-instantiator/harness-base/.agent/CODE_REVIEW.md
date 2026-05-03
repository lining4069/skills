# Code Review

## Review Priorities

Review for these issues first:

1. contract violations
2. silent state corruption
3. unbounded retries, loops, or budgets
4. policy or approval bypass paths
5. traces, logs, or audits that lose actionable debugging information
6. runtime transitions that skip required states
7. memory writes that blur temporary context and durable state

## Review Questions

- can bad input enter trusted state
- can a denied action still look successful
- can a retry or loop exceed its declared budget
- is every terminal state explicit
- would an operator know why the system failed from the recorded state
- did this change alter runtime or verification semantics without updating the matching docs
- did this change create a new durable-memory behavior without documenting the memory strategy
