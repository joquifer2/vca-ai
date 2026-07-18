# Data Provider Validation

## Decision

PASS

## Provider

| Field | Value |
|---|---|
| provider | BigQuery MCP Server |
| workspace | vca |
| project_id | datamart-vca-494114 |
| max_bytes_billed | 1073741824 |
| fallback_used | No |
| BigQuery CLI used | No |

## Metadata Discovery

| request_id | resource | status | trace_reference |
|---|---|---|---|
| auc-001-pci-001-discover-workspace | workspace:vca | success | trc-8ec40ff7ec2549289d10ae1a5c237ed1 |
| auc-001-pci-001-discover-dataset-intermediate | dataset:intermediate | success | trc-a00c26e2665f48cc876450d747059c86 |
| auc-001-pci-001-discover-dataset-marts | dataset:marts | success | trc-f6eef7ce37d644ac81cbdcf5603910b0 |
| auc-001-pci-001-discover-table-leads | table:marts.fct_lead_enriched | success | trc-569ac15a984c47718e709c05beef23b7 |
| auc-001-pci-001-discover-table-spend | table:marts.fct_spend | success | trc-d70da4889d404cc6b2c3546979343741 |
| auc-001-pci-001-discover-table-scoring | table:intermediate.int_faro_lead_scoring | success | trc-d82eb30da38943af8ebd67e6821920ca |
| auc-001-pci-001-discover-table-campaign-signal | table:marts.dim_campaign_signal | success | trc-1f0980d6f8424b429bb1c1ecedb5b923 |

## Coverage Validation

| request_id | source | min_day | max_day | row_count | distinct_entity_count | missing_ad_id_count | trace_reference |
|---|---|---:|---:|---:|---:|---:|---|
| auc-001-pci-001-coverage-leads | marts.fct_lead_enriched | 2026-04-18 | 2026-06-30 | 1329 | 1329 leads | 0 | trc-682400537fba4c61989043614795f1ed |
| auc-001-pci-001-coverage-spend | marts.fct_spend | 2026-04-18 | 2026-06-30 | 7332 | 23 ads | 0 | trc-e339d032ebd94304aae30b665aa2da76 |
| auc-001-pci-001-coverage-scoring | intermediate.int_faro_lead_scoring | 2026-04-18 | 2026-06-30 | 1329 | 1329 leads | 0 | trc-b9cec8e1d414480995a897ad630a811d |

## Notes

- One cross-dataset validation query was rejected by MCP scope policy and was not used as evidence.
- Validation was completed through separate allowlisted dataset reads and deterministic comparison outside the provider.
- No historical output was used to validate expected values.
