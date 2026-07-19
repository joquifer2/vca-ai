# AUC-001 Cost Limit Blockage Architectural Diagnostic

## Metadata

| Field | Value |
|---|---|
| Diagnostic ID | VCA-AUC-001-DIAG-COST-20260719 |
| Role | Architect Agent |
| Scope | Diagnose `ERR_COST_LIMIT_EXCEEDED` during a new AUC-001 execution to 2026-06-30 |
| Status | Documented |
| Date | 2026-07-19 |
| Repository | `vca-ai` |
| Implementation changes | None |
| BigQuery CLI used | No |
| Historical evidence reused as analytical input | No |

---

## 1. Executive Decision

Conclusion:

```yaml
classification: TRANSIENT / OPERATIONAL ISSUE
secondary_architectural_observation: MCP rejection taxonomy conflates byte-cost excess and daily quota exhaustion under ERR_COST_LIMIT_EXCEEDED
root_cause_most_probable: BigQuery MCP in-memory daily quota exhausted before query dry-run
confidence: High
```

The immediate blockage is not caused by the word "analitico" in the user request. The request activated the same AUC-001 full-execution route required for:

```text
Haz un analisis de la calidad de los leads hasta el 30 de junio de 2026.
```

The current failure occurred after valid AUC-001 metadata discovery and before usable evidence acquisition. A follow-up `discover_metadata` probe was also rejected with `ERR_COST_LIMIT_EXCEEDED`; metadata discovery does not dry-run SQL or scan BigQuery tables. That makes table scan cost, `LIMIT 1`, partition pruning or SQL shape insufficient as the primary explanation.

---

## 2. Reconstructed Flow

### 2.1 AUC-001 route

The request:

```text
Haz un analisis analitico de la calidad de los leads hasta el 30 de junio de 2026.
```

matches AUC-001 because it concerns Meta lead quality analysis. The canonical flow is defined by `.github/skills/meta-lead-quality-analysis/RUNBOOK.md`.

Resolved execution context:

| Field | Value |
|---|---|
| Execution mode | Full execution with new evidence |
| Cutoff | 2026-06-30 |
| Period start | `PENDING_START_FROM_PROVIDER_COVERAGE` |
| Workspace | `vca` |
| Project | `datamart-vca-494114` |
| Provider | BigQuery MCP Server |
| CLI fallback | Prohibited |

The word "analitico" may influence Presentation Projection later, but the blockage happened before Presentation Layer, during Data Provider Validation / coverage resolution. Therefore it did not materially change data acquisition.

### 2.2 Authorized workspace and policy

`configs/workspaces.json` defines:

| Field | Value |
|---|---|
| workspace_id | `vca` |
| project_id | `datamart-vca-494114` |
| datasets | `intermediate`, `marts` |
| allowed tables | `intermediate.int_faro_lead_scoring`; `marts.fct_lead_enriched`; `marts.fct_spend`; `marts.dim_campaign_signal` |
| auth_mode | `service_account_adc_readonly` |
| cost_limit_bytes | `1073741824` |
| dry_run_required | `true` |
| daily_request_quota | `50` |
| deny_by_default | `true` |

### 2.3 Data Provider Validation result

The following canonical `discover_metadata` calls succeeded before the blockage:

| Resource | Status |
|---|---|
| `workspace:vca` | success |
| `dataset:intermediate` | success |
| `dataset:marts` | success |
| `table:intermediate.int_faro_lead_scoring` | success |
| `table:marts.fct_spend` | success |
| `table:marts.fct_lead_enriched` | success |
| `table:marts.dim_campaign_signal` | success |

This validates provider availability, identity, allowlist and schema access up to that point.

---

## 3. Rejected SQL Patterns

The rejected coverage and sample queries were reconstructed from the live execution. They used the closed AUC-001 execution context:

```yaml
project_id: datamart-vca-494114
dataset_id: marts|intermediate
max_bytes_billed: 1073741824
```

### 3.1 Coverage leads

```sql
SELECT
  MIN(day) AS min_day,
  MAX(day) AS max_day,
  COUNT(*) AS lead_count,
  COUNT(DISTINCT lead_id) AS distinct_lead_count
FROM `datamart-vca-494114.marts.fct_lead_enriched`
WHERE day <= DATE '2026-06-30'
```

| Attribute | Value |
|---|---|
| Table | `marts.fct_lead_enriched` |
| Temporal column | `day` |
| Joins | None |
| Aggregations | `MIN`, `MAX`, `COUNT`, `COUNT DISTINCT` |
| LIMIT | None |
| Result | rejected, `ERR_COST_LIMIT_EXCEEDED` |
| Estimated bytes | Not exposed (`null`) |

### 3.2 Coverage spend

```sql
SELECT
  MIN(spend_period) AS min_day,
  MAX(spend_period) AS max_day,
  COUNT(*) AS spend_record_count,
  SUM(spend_amount) AS spend_amount
FROM `datamart-vca-494114.marts.fct_spend`
WHERE spend_period <= DATE '2026-06-30'
```

| Attribute | Value |
|---|---|
| Table | `marts.fct_spend` |
| Temporal column | `spend_period` |
| Joins | None |
| Aggregations | `MIN`, `MAX`, `COUNT`, `SUM` |
| LIMIT | None |
| Result | rejected, `ERR_COST_LIMIT_EXCEEDED` |
| Estimated bytes | Not exposed (`null`) |

### 3.3 Coverage FARO

```sql
SELECT
  MIN(lead_date) AS min_day,
  MAX(lead_date) AS max_day,
  COUNT(*) AS scored_lead_count,
  COUNT(DISTINCT lead_id) AS distinct_scored_lead_count
FROM `datamart-vca-494114.intermediate.int_faro_lead_scoring`
WHERE lead_date <= DATE '2026-06-30'
```

| Attribute | Value |
|---|---|
| Table | `intermediate.int_faro_lead_scoring` |
| Temporal column | `lead_date` |
| Joins | None |
| Aggregations | `MIN`, `MAX`, `COUNT`, `COUNT DISTINCT` |
| LIMIT | None |
| Result | rejected, `ERR_COST_LIMIT_EXCEEDED` |
| Estimated bytes | Not exposed (`null`) |

### 3.4 Minimal sample with `LIMIT 1`

Representative pattern:

```sql
SELECT
  day,
  lead_id,
  lead_tier,
  ad_id
FROM `datamart-vca-494114.marts.fct_lead_enriched`
WHERE day <= DATE '2026-06-30'
LIMIT 1
```

| Attribute | Value |
|---|---|
| Table | `marts.fct_lead_enriched` |
| Temporal column | `day` |
| Joins | None |
| Aggregations | None |
| LIMIT | `1` |
| Result | rejected, `ERR_COST_LIMIT_EXCEEDED` |
| Estimated bytes | Not exposed (`null`) |

`LIMIT 1` can still require scanning enough storage to satisfy filters when no pruning path is available. However, it cannot explain the later rejection of `discover_metadata`, which performs no SQL dry-run.

---

## 4. Partitioning And Pruning Assessment

`discover_metadata` exposes schemas but does not expose partitioning, clustering or table storage metadata. The AUC-001 tables include date-like fields:

| Table | Filter field used | Partition metadata available via AUC-001 MCP discovery |
|---|---|---|
| `marts.fct_lead_enriched` | `day` | No |
| `intermediate.int_faro_lead_scoring` | `lead_date` | No |
| `marts.fct_spend` | `spend_period` | No |
| `marts.dim_campaign_signal` | Not temporal | No |

An MCP-only attempt to inspect `INFORMATION_SCHEMA.PARTITIONS` was rejected with the same `ERR_COST_LIMIT_EXCEEDED`. Therefore partition and clustering state remains unverified in this diagnostic.

The current evidence does not support classifying this as a BigQuery partitioning defect:

- previous equivalent AUC-001 MCP reads over the same tables processed small byte volumes;
- the latest rejection also affects `discover_metadata`, which is not a table scan;
- no dry-run estimated bytes were exposed for the rejected queries.

---

## 5. MCP Cost Policy Mechanics

Read-only inspection of the local BigQuery MCP Server implementation shows:

- `query_read_only` validates auth, consumes daily quota, validates execution context, validates SQL allowlist, performs dry-run, then executes.
- `discover_metadata` validates auth and also consumes the same daily quota before metadata discovery.
- `DailyQuotaGuard.consume()` raises `ERR_COST_LIMIT_EXCEEDED` when the per-principal daily count reaches the workspace limit.
- `CostGuard.validate()` also raises `ERR_COST_LIMIT_EXCEEDED` when dry-run estimated bytes exceed `max_bytes_billed`.

Therefore `ERR_COST_LIMIT_EXCEEDED` currently represents at least two different conditions:

1. query dry-run cost exceeds `max_bytes_billed`;
2. daily request quota is exhausted.

The public response does not distinguish these conditions. In both cases the user sees:

```text
ERR_COST_LIMIT_EXCEEDED
The request exceeds the configured cost policy.
```

The decisive probe was:

```yaml
request_id: auc-001-cost-block-diagnostic-quota-probe
operation: discover_metadata
selector: workspace:vca
status: rejected
error_code: ERR_COST_LIMIT_EXCEEDED
trace_reference: trc-c0a8fe760c9c49f2983f7ba78bdde3d0
```

Because `discover_metadata` does not perform SQL dry-run, this rejection points to daily quota exhaustion rather than query bytes.

---

## 6. Comparison With Previous Executions

### 6.1 Previous MCP execution that worked

`outputs/auc-001/pci-001/2026-06-30/` records a successful AUC-001-PCI-001 execution through BigQuery MCP.

Coverage validation succeeded:

| Request | Source | Period | Row count | Trace |
|---|---|---:|---:|---|
| `auc-001-pci-001-coverage-leads` | `marts.fct_lead_enriched` | 2026-04-18 to 2026-06-30 | 1329 | `trc-682400537fba4c61989043614795f1ed` |
| `auc-001-pci-001-coverage-spend` | `marts.fct_spend` | 2026-04-18 to 2026-06-30 | 7332 | `trc-e339d032ebd94304aae30b665aa2da76` |
| `auc-001-pci-001-coverage-scoring` | `intermediate.int_faro_lead_scoring` | 2026-04-18 to 2026-06-30 | 1329 | `trc-b9cec8e1d414480995a897ad630a811d` |

Evidence acquisition processed low byte volumes:

| Request | Purpose | Dataset | Bytes processed |
|---|---|---|---:|
| `auc-001-pci-001-quality-summary` | Lead quality summary | `marts` | 83660 |
| `auc-001-pci-001-spend-summary` | Spend summary | `marts` | 490475 |
| `auc-001-pci-001-scoring-summary` | Scoring validation summary | `intermediate` | 83660 |
| `auc-001-pci-001-lead-aggregate-compact` | Lead aggregate by `ad_id_norm` | `marts` | 52802 |
| `auc-001-pci-001-spend-aggregate-compact` | Spend aggregate by `ad_id_norm` and signal | `marts` | 490475 |
| `auc-001-pci-001-weekly-quality-summary` | Weekly lead quality summary | `marts` | 52802 |

The previous execution therefore does not support the hypothesis that ordinary AUC-001 coverage/acquisition over these tables inherently exceeds 1 GiB.

### 6.2 Earlier dry-run failures

`docs/evaluations/auc-001/diagnostics/auc-001-v2-dry-run-failure-diagnostic.md` documents a different problem:

- invalid alias `AS rows`;
- one comma join rejected by SQL policy;
- no evidence of provider, IAM, location or gateway instability.

That diagnostic led to the Runbook conventions against `AS rows`, alias collisions and comma joins. The current rejected queries respected those conventions. This is a new operational blockage, not the same v2 SQL-generation defect.

### 6.3 Why previous executions could acquire evidence and this one could not

Most likely sequence:

1. The MCP runtime already had prior successful calls counted against the same in-memory UTC quota.
2. The new AUC-001 execution made seven successful `discover_metadata` calls.
3. Those calls brought the per-principal daily quota to its configured limit of 50.
4. Subsequent `query_read_only` calls were rejected before usable dry-run/evidence acquisition.
5. A later `discover_metadata` probe was also rejected, confirming a non-SQL quota/cost guard path.

No evidence indicates a change caused by the requested word "analitico", Presentation Policy, or analytical profile.

---

## 7. Alternatives Evaluated

| Alternative | Assessment | Owner |
|---|---|---|
| Use `INFORMATION_SCHEMA.PARTITIONS` for coverage | Architecturally sound, but currently blocked by the same MCP cost/quota response and not allowlisted as a stable AUC-001 metadata path. | BigQuery MCP Server / Data model |
| Expose provider coverage metadata in `discover_metadata` | Strong minimal design improvement: coverage can be resolved without SQL acquisition and without consuming analytical query budget. | BigQuery MCP Server |
| Add low-cost coverage aggregate views/tables | Useful if metadata coverage is insufficient; requires allowlist and Data Contract update. | BigQuery model / vca-ai |
| Use canonical partitioned queries | Still desirable, but not the minimum fix for this incident because `discover_metadata` is also blocked. | vca-ai |
| Reduce selected columns | Helpful for acquisition hygiene, but not sufficient for quota exhaustion. | vca-ai |
| Increase `cost_limit_bytes` | Not justified by evidence; previous successful execution processed far below 1 GiB. | Configuration / Owner |
| Increase or reset `daily_request_quota` | Operationally relevant. The current 50-call in-memory quota can block methodologically correct AUC-001 executions after discovery and diagnostics. | BigQuery MCP Server configuration |
| Split quota errors from byte-cost errors | Recommended technical correction; improves diagnosability and prevents false partition/cost conclusions. | BigQuery MCP Server |

---

## 8. Architectural Decision

### 8.1 Cause root

The most probable cause is daily quota exhaustion inside the BigQuery MCP Server, surfaced through the generic `ERR_COST_LIMIT_EXCEEDED` error.

Evidence:

- `discover_metadata` succeeded for the seven canonical AUC-001 resources before the blockage.
- `query_read_only` calls were then rejected with `ERR_COST_LIMIT_EXCEEDED` and no usable estimated bytes.
- `INFORMATION_SCHEMA.PARTITIONS` checks were rejected the same way.
- A later `discover_metadata` call was rejected with `ERR_COST_LIMIT_EXCEEDED`, although it performs no SQL dry-run.
- MCP source code shows both `DailyQuotaGuard` and `CostGuard` raise `ERR_COST_LIMIT_EXCEEDED`.
- Previous AUC-001-PCI-001 MCP acquisition over the same tables processed only 52 KB to 490 KB per successful query.

### 8.2 Impact

| Area | Impact |
|---|---|
| Current AUC-001 execution | Blocked before Context Definition Stabilization and Evidence Acquisition |
| Evidence Set | Cannot be built from rejected outputs |
| Knowledge / Recommendations / Presentation | Must not proceed |
| P0 | Blocked for the requested new analysis until MCP quota/runtime is reset or quota semantics are corrected |
| P01 | Blocked if it depends on repeatable AUC-001 full execution in the same runtime/day; not blocked as a specification discussion if kept documentary |

### 8.3 Minimum solution

Immediate operational solution:

1. Reset the MCP runtime quota by restarting the BigQuery MCP Server, or wait until the UTC daily quota window resets.
2. Re-run AUC-001 as a new complete execution from Phase 01.
3. Use the same canonical selectors and MCP-only restrictions.
4. Do not increase `cost_limit_bytes` unless a fresh dry-run shows actual byte estimates above 1 GiB.

Minimum technical correction:

1. Split quota exhaustion from byte-cost excess in the MCP taxonomy, for example with `ERR_DAILY_QUOTA_EXCEEDED`.
2. Return a reason that distinguishes daily quota from dry-run byte estimate.
3. Consider exposing remaining quota or a non-consuming health/quota metadata check.
4. Consider whether `discover_metadata` should consume the same daily analytical query quota.

Potential data/model improvement:

1. Expose partition/coverage metadata through allowlisted metadata discovery or low-cost aggregate coverage views.
2. Keep acquisition queries compact and separated by dataset/source as in AUC-001-PCI-001.

### 8.4 Does this require a SPEC?

For `vca-ai` AUC-001 execution: no new SPEC is required to unblock the immediate run. This is an operational runtime quota condition.

For BigQuery MCP Server behavior: a small MCP-side specification or task is justified if changing the public error taxonomy, quota semantics, or metadata discovery contract. The change belongs primarily to the MCP Server, not to AUC-001 analytical logic.

### 8.5 Does this require a technical task?

Yes, recommended:

```text
Create a BigQuery MCP Server task to disambiguate daily quota exhaustion from dry-run byte cost excess, expose safer quota diagnostics, and decide whether metadata discovery should consume analytical query quota.
```

For `vca-ai`, create only a follow-up documentation/task reference if the team wants the Runbook to mention this operational blockage mode.

---

## 9. Next Agent

Recommended next agent:

```text
Implementation Agent for BigQuery MCP Server runtime maintenance or MCP-side task planning.
```

If the immediate goal is only to complete the AUC-001 analysis, the next action is operational rather than architectural: restart the MCP Server or wait for quota reset, then rerun the full AUC-001 workflow.

If the goal is to prevent recurrence, use Tasks Planner Agent in the BigQuery MCP Server repository to plan the taxonomy/quota diagnostic correction before implementation.

---

## 10. Residual Unknowns

| Unknown | Impact | Validation required |
|---|---|---|
| Exact quota count before this AUC-001 attempt | Medium | Inspect MCP audit sink or add quota visibility; current logs do not expose count |
| Partitioning/clustering state of the three AUC-001 fact tables | Medium | Add metadata support or allowlisted partition metadata route through MCP |
| Whether all future AUC-001 full executions fit comfortably below 1 GiB after data growth | Medium | Fresh dry-run after quota reset |
| Whether `discover_metadata` should consume the same quota as `query_read_only` | Important | MCP architecture decision |

---

## 11. Non-Actions Preserved

- No code was implemented.
- No cost limit was increased.
- No BigQuery CLI was used.
- No reports were regenerated.
- No historical Evidence Set was reused as analytical input.
- No new AUC-001 evidence was inferred from rejected queries.

