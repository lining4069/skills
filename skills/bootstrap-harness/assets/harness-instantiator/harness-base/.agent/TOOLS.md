# Tools

## Tool Philosophy

Tools and integrations are untrusted until their outputs pass validation, policy checks, and any relevant approval gates.

The system should trust schemas, policy decisions, recorded state, and explicit contracts, not free-form tool output.

## Tool Rules

- every tool or integration must have a stable name
- every tool or integration must declare a request and response shape
- boundaries that perform I/O should be explicit
- tools should be narrow and composable
- side effects should be explicit and reviewable
- high-risk tools should be deny-by-default in early versions
- MCP or third-party integrations should declare auth and scope expectations
- workspace boundaries should be explicit when tools can reach files or external systems
- if a capability can alter external state, note which approval or runtime gate owns that boundary

## Routing Rules

- planners or callers should select from an allowed capability set
- the policy layer can deny execution even if a tool is registered
- the routing layer should validate outputs before they reach trusted state
- failures must be classified, not hidden in prose
- keep pure transformation logic sync internally where possible
- record where retries belong: caller, runtime, or integration adapter

## Capability Boundary Questions

Use these questions when introducing a new capability:

- what external boundary does it cross
- what auth or approval scope does it require
- what workspace boundary must constrain it
- what invariant does it threaten if it fails badly
- what trace or audit data must be recorded
- should it be allowed in bootstrap or only after later milestones
