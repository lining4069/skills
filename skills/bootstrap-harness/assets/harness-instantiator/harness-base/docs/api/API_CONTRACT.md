# API Contract

Date: `[YYYY-MM-DD]`

## Purpose

This file is the repository's text contract for interface semantics.

It complements generated OpenAPI or Swagger output.

Generated docs explain shape.
This file explains meaning, flow, constraints, execution model, and failure behavior.

## When To Update This File

Update this file when any of the following changes:

- endpoint paths
- request or response fields
- field semantics
- execution logic
- user flow
- failure behavior
- status semantics
- caller sync versus async expectations
- approval or delayed-completion behavior

## Documentation Rules

Each interface should cover:

1. purpose
2. caller perspective
3. request parameters and field semantics
4. response semantics
5. internal execution flow
6. user-visible or operator-visible flow
7. success path
8. failure path
9. current limitations
10. code locations

## Global Conventions

Describe the conventions that apply across the entire public interface.

Examples:

- status enums
- verdict semantics
- failure classifications
- sync vs async caller expectations
- long-running task semantics

## Endpoint Index

Create a table like this:

| Method | Path | Purpose | Execution Model |
|------|------|------|-----------------|
| `POST` | `/example` | Replace with actual purpose | Replace with actual model |

## Endpoint Details

Repeat this section for each important endpoint.

### `[METHOD] [PATH]`

#### Purpose

Describe why this endpoint exists.

#### Caller Perspective

Describe when and why a caller should use it.

#### Request

Provide an example payload if applicable.

#### Field Semantics

Explain each important field.

#### Response Semantics

Explain the returned status and fields.

#### Internal Flow

Describe the relevant internal path at a high level.

#### User Or Operator Flow

Explain what the caller experiences.

#### Success Path

Describe the normal path.

#### Failure Path

Describe the failure modes.

#### Current Limitations

List what is intentionally not handled yet.

#### Code Locations

Point to the relevant files.
