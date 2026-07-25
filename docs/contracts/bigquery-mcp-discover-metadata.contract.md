# BigQuery MCP discover_metadata Contract Reference

## Metadata

| Field | Value |
|---|---|
| Source | BigQuery MCP Server `tools/list` |
| Server name | BigQuery Read-Only MCP |
| Observed version | 1.28.1 |
| Observed date | 2026-07-17 |

## Purpose

This document records the external MCP tool schema observed by `vca-ai` for `discover_metadata`.

It is not a redefinition of the server contract. If the MCP server schema changes, this document must be refreshed from `tools/list` before any analytical execution relies on metadata discovery.

## Tool

`discover_metadata`

Description observed from the server:

```text
Discover allowlisted metadata using the canonical selector contract.
```

## Required Inputs

| Field | Type | Required | Allowed values / format |
|---|---|---|---|
| `request_id` | string | Yes | Stable request identifier for traceability |
| `scope_request` | string enum | Yes | `workspace`, `dataset`, `table` |
| `resource_selector` | string | Yes | Must match the selected scope format |
| `auth_context` | string | No | Defaults to `server_adc` |

## Canonical Selector Formats

| `scope_request` | `resource_selector` format | Valid VCA example |
|---|---|---|
| `workspace` | `workspace:<workspace_id>` | `workspace:vca` |
| `dataset` | `dataset:<dataset_id>` | `dataset:marts` |
| `table` | `table:<dataset_id>.<table_id>` | `table:marts.fct_spend` |

## Invalid Selector Categories


This document intentionally avoids preserving legacy selector strings as runnable examples.

## Error Interpretation

| Error code | Interpretation | Required behavior |
|---|---|---|
| `ERR_AUTH_REQUIRED` | Credentials are absent, invalid, not accepted, or the read-only identity cannot be validated. | Stop. Do not try other selectors. Do not run analytical queries. Request local intervention only if ADC renewal, server restart, or equivalent runtime maintenance is needed. |
| `ERR_SELECTOR_INVALID` | The selector type, fields, structure, or resource format is incompatible with the server contract. | Stop validation. Record the expected contract and selector sent. Treat as incompatibility between `vca-ai` and the server. |
| `ERR_SCOPE_TOO_BROAD` | The selector is valid but asks for a scope broader than allowed for that operation. | Apply at most one deterministic reduction documented before execution. Do not explore resources. |
| `ERR_RESOURCE_NOT_ALLOWLISTED` | The selector is valid but the resource is not in the authorized allowlist. | Stop for that resource. Do not seek alternative sources, use CLI, historical evidence, or modify allowlist during the analytical execution. |

The currently observed server schema does not publish a specific functional-unavailability error for `discover_metadata`. Therefore the `PASS WITH OBSERVATION` path is reserved for a future server-published code and is not active for current executions. If such a code is published later, Phase 05 may finish as `PASS WITH OBSERVATION` only when `query_read_only` validates the same allowlisted resources through MCP.

## Phase 05 Output States

| State | Meaning |
|---|---|
| `PASS` | `discover_metadata` works, identity is valid, resources are authorized, and schemas are available. |
| `PASS WITH OBSERVATION` | Reserved for a future server-published functional-unavailability code; no currently observed official code activates this path. |
| `FAIL` | Authentication is invalid, contract is incompatible, resource is not allowlisted, scope is not safely correctable, access is denied, or the MCP response is not safely interpretable. |
