# Evidence Acquisition Record

## Decision

PASS

All usable metrics in this execution come from successful BigQuery MCP `query_read_only` calls over allowlisted sources.

## Successful Queries

| request_id | purpose | dataset_id | bytes_processed | trace_reference |
|---|---|---|---:|---|
| auc-001-pci-001-quality-summary | Lead quality summary | marts | 83660 | trc-f80394558917431bbff714cc93f5369f |
| auc-001-pci-001-spend-summary | Spend summary | marts | 490475 | trc-b6f02afafac249ccba428e6adba72e32 |
| auc-001-pci-001-scoring-summary | Scoring validation summary | intermediate | 83660 | trc-e8b42aac5d9b444fa25f053a55789f47 |
| auc-001-pci-001-lead-aggregate-compact | Lead aggregate by ad_id_norm | marts | 52802 | trc-420abdb50c1c4360bc69801db31d67c6 |
| auc-001-pci-001-spend-aggregate-compact | Spend aggregate by ad_id_norm and signal | marts | 490475 | trc-db30e82249fb4dbcbe12a07094c04259 |
| auc-001-pci-001-weekly-quality-summary | Weekly lead quality summary | marts | 52802 | trc-ec52b7d6643f4bf5961d31c00c4f1793 |

## Rejected Or Unusable Queries

| request_id | status | reason | evidence_use |
|---|---|---|---|
| auc-001-pci-001-lead-scoring-consistency | rejected | ERR_SCOPE_DENIED for cross-dataset query | Not used |
| auc-001-pci-001-acquire-lead-aggregate | unusable | Tool output exceeded model context and was truncated | Not used |

## Execution Context Contract

Every successful query used a closed execution context:

```yaml
project_id: datamart-vca-494114
dataset_id: marts|intermediate
max_bytes_billed: 1073741824
```

## SQL Scope

- Evidence acquisition used separate lead-side, scoring-side and spend-side reads.
- Coverage reconciliation was constructed after acquisition.
- No rejected query contributed values to the Evidence Set.
- No historical output namespace was read as expected values.
