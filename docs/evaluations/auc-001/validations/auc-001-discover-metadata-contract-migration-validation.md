# AUC-001 discover_metadata Contract Migration Validation

## Metadata

| Field | Value |
|---|---|
| Validation date | 2026-07-17 |
| Scope | AUC-001 Phase 05 - Data Provider Validation |
| MCP server observed | BigQuery Read-Only MCP v1.28.1 |
| Contract reference | `docs/contracts/bigquery-mcp-discover-metadata.contract.md` |
| Result | PASS |

## Objective

Validate that `vca-ai` consumes the canonical `discover_metadata` selector contract exposed by `bigquery-mcp-server`, without using legacy selector conventions or exploratory retries during AUC-001 Data Provider Validation.

## Repository Updates Validated

| Area | Evidence |
|---|---|
| Canonical reference | `docs/contracts/bigquery-mcp-discover-metadata.contract.md` records the observed external schema from MCP `tools/list`. |
| Runbook | `.github/skills/meta-lead-quality-analysis/RUNBOOK.md` Phase 05 requires canonical selectors, deterministic error handling, and PASS / PASS WITH OBSERVATION / FAIL outcomes. |
| Checklist | `.github/skills/meta-lead-quality-analysis/CHECKLIST.md` verifies canonical selector use, absence of exploratory retries, and error interpretation. |
| Tooling | `tools/vca_mcp_smoke.py` now uses `workspace:vca`, `dataset:<dataset_id>`, and `table:<dataset_id>.<table_id>` through `tools/vca_mcp_contract.py`. |
| Tests | `tests/evals/auc_001_discover_metadata_contract_tests.ps1` covers canonical selectors, legacy rejection, error mapping, fallback prohibition and Phase 05 statuses. |

## MCP Schema Evidence

`tools/list` exposed `discover_metadata` with:

- required `request_id` string;
- required `scope_request` enum: `workspace`, `dataset`, `table`;
- required `resource_selector` string;
- optional `auth_context` defaulting to `server_adc`.

The server description explicitly accepts:

- `workspace:<workspace_id>`;
- `dataset:<dataset_id>`;
- `table:<dataset_id>.<table_id>`.

It explicitly rejects legacy FQN examples such as:

- `datamart-vca-494114`;
- `datamart-vca-494114.marts`;
- `datamart-vca-494114.marts.fct_spend`;
- `fct_spend`;
- `*`.

## Integrated MCP Validation

All calls below used `discover_metadata` with one canonical selector per resource and did not attempt alternate selector formats.

| Request ID | Selector | Result | Trace |
|---|---|---|---|
| `auc001-discover-contract-validation-workspace-20260717` | `scope_request=workspace`, `resource_selector=workspace:vca` | success; datasets `intermediate`, `marts` | `trc-22d3fb5c942d44d7ad510da9d38f36d0` |
| `auc001-discover-contract-validation-dataset-intermediate-20260717` | `scope_request=dataset`, `resource_selector=dataset:intermediate` | success; table `int_faro_lead_scoring` | `trc-4f79f25e78c24094b5c80534747b0532` |
| `auc001-discover-contract-validation-dataset-marts-20260717` | `scope_request=dataset`, `resource_selector=dataset:marts` | success; tables `dim_campaign_signal`, `fct_lead_enriched`, `fct_spend` | `trc-e3f2b9738424464ca4e70e453df488e5` |
| `auc001-discover-contract-validation-table-int-faro-20260717` | `scope_request=table`, `resource_selector=table:intermediate.int_faro_lead_scoring` | success; schema available | `trc-299d622273b54d9b8ff0cde315ffdeda` |
| `auc001-discover-contract-validation-table-fct-lead-enriched-20260717` | `scope_request=table`, `resource_selector=table:marts.fct_lead_enriched` | success; schema available | `trc-88700e96e728416891c590aac745a1d3` |
| `auc001-discover-contract-validation-table-fct-spend-20260717` | `scope_request=table`, `resource_selector=table:marts.fct_spend` | success; schema available | `trc-36c265f23c3c48338b45b34183bd3cad` |
| `auc001-discover-contract-validation-table-dim-campaign-signal-20260717` | `scope_request=table`, `resource_selector=table:marts.dim_campaign_signal` | success; schema available | `trc-79660b06e5874808873c77d2b0281208` |

## Negative Selector Validation

| Request ID | Selector | Result | Trace |
|---|---|---|---|
| `auc001-discover-contract-validation-invalid-legacy-selector-20260717` | legacy project-prefixed table selector, details intentionally omitted from current guidance | rejected with `ERR_SELECTOR_INVALID`; selector guidance returned by server | `trc-bddd3e390d224710a2bb0d55eb9f96d6` |

Interpretation: the server now distinguishes invalid selector format from authentication and allowlist failures. AUC-001 must stop on this error during normal analytical execution.

## Automated Test Evidence

Command:

```powershell
powershell -ExecutionPolicy Bypass -File tests\evals\auc_001_discover_metadata_contract_tests.ps1
```

Result:

```text
All AUC-001 discover_metadata contract tests passed: 7
```

Covered controls:

1. canonical selector reference;
2. legacy selector rejection;
3. `ERR_SELECTOR_INVALID`;
4. `ERR_SCOPE_TOO_BROAD`;
5. `ERR_RESOURCE_NOT_ALLOWLISTED`;
6. `ERR_AUTH_REQUIRED`;
7. successful `discover_metadata` contract markers;
8. absence of any current server-published functional discovery limitation code;
9. no fallback outside MCP;
10. absence of exploratory selector retries in smoke script;
11. user authorization only for local state changes;
12. `PASS`;
13. `PASS WITH OBSERVATION`;
14. `FAIL`.

## Observations

- `python tools\vca_mcp_smoke.py` timed out once at 64 seconds during local stdio execution before producing output. The integrated MCP validation above was completed through the active MCP tool surface and confirmed the same canonical selectors.
- `tests/evals/auc_001_traceability_tests.ps1` was later realigned to the restructured AUC-001 validation path `docs/evaluations/auc-001/validations/auc-001-development-entry-readiness-evidence.md`; this remains unrelated to the `discover_metadata` migration.
- Historical outputs and old validation records are marked as superseded for selector-contract guidance; current execution guidance is only `docs/contracts/bigquery-mcp-discover-metadata.contract.md`.

## Final Decision

Data Provider Validation contract migration: PASS

AUC-001 can now validate the BigQuery MCP Data Provider deterministically using canonical `discover_metadata` selectors, with no legacy selector fallback and no exploratory retry sequence.