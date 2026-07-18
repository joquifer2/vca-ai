# AUC-001-PCI-001 Context Definition

## Metadata

| Field | Value |
|---|---|
| execution_id | AUC-001-PCI-001-2026-06-30 |
| iteration_id | AUC-001-PCI-001 |
| parent_auc | AUC-001 |
| execution_date | 2026-06-30 |
| executed_at_utc | 2026-07-18 |
| output_namespace | outputs/auc-001/pci-001/2026-06-30/ |
| provider | BigQuery MCP Server |
| provider_mode | MCP-only |
| historical_outputs_policy | outputs/auc-001/2026-06-30/ is immutable and was not used as expected values |

## Stabilized Scope

Execute the post-closure canonical cost-quality model for AUC-001 as a separated iteration.

This execution does not reopen the original AUC-001 experimental cycle and does not modify historical outputs.

## Period

| Field | Value |
|---|---|
| period_start | 2026-04-18 |
| period_end | 2026-06-30 |
| period_resolution | Provider coverage resolved the start date |

## Authorized Sources

| Source | Role |
|---|---|
| datamart-vca-494114.marts.fct_lead_enriched | Canonical lead count and quality source |
| datamart-vca-494114.intermediate.int_faro_lead_scoring | Lead-side validation source |
| datamart-vca-494114.marts.fct_spend | Canonical spend source |
| datamart-vca-494114.marts.dim_campaign_signal | Campaign signal domain source |

## Thresholds Config

| Threshold | Value |
|---|---:|
| descriptive_min_matched_leads | 1 |
| ranking_min_matched_leads | 10 |
| recommendation_min_matched_leads | 20 |
| recommendation_min_matched_ab_leads | 5 |

## Restrictions Applied

- BigQuery MCP Server was the only data provider used.
- Historical outputs were not read as expected values.
- Historical Knowledge and Recommendations were not reused as sources.
- The original namespace `outputs/auc-001/2026-06-30/` was not modified.
- All new artifacts are persisted only under `outputs/auc-001/pci-001/2026-06-30/`.
