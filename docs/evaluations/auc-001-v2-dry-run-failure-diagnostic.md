# AUC-001 v2 Dry Run Failure Diagnostic

## Scope

This diagnostic investigates the rejected AUC-001 v2 queries only. It does not rerun AUC-001, does not execute real BigQuery queries, and does not modify MCP code, configuration, allowlist, IAM, ADC, Skill, Runbook, contracts, or tests.

Allowed execution used:

- `ReadOnlySqlGuard.validate_and_qualify()` locally, without BigQuery access.
- `GoogleBigQueryGateway(settings).dry_run(qualified_sql)` only.
- No `job.result()`.
- No row data returned.

Runtime configuration used for the direct dry runs:

```yaml
workspace_id: vca
project: datamart-vca-494114
datasets:
  - intermediate
  - marts
location: EU
workspace_file: C:\Workspace\VCA\vca-ai\configs\workspaces.json
gateway: GoogleBigQueryGateway
operation: dry_run_only
```

## Summary

```yaml
total_failed_queries: 15
exact_sql_recovered: 15
policy_rejections: 1
bigquery_sql_errors: 14
gateway_or_runtime_errors: 0
unknown: 0
```

Root cause distribution:

```yaml
invalid_agent_sql: 14
policy_limitation: 1
provider_or_gateway: 0
unknown: 0
```

The dry-run failures were not caused by ADC, IAM, location, BigQuery provider instability, or the gateway implementation. They were caused by SQL generated during AUC-001 v2:

- 13 queries used `AS rows`, and BigQuery rejected `ROWS` as an unexpected keyword.
- 1 query, q022, used `COALESCE(leads, 0)` where `leads` resolved as a STRUCT/table alias rather than the numeric output alias.
- q021 was correctly rejected by SQL Policy because it contains a comma in the `FROM` clause: `FROM \`...\`, spend`.

## Recovered Queries and Classification

### q003

```yaml
query_id: q003
request_id: codex-vca-auc001-v2-q003-lead-quality-base-20260715
trace_id: trc-09bc75694f18419a9e463bc38a0fd9e6
sql_recovered: true
execution_context:
  project_id: datamart-vca-494114
  dataset_id: marts
  max_bytes_billed: 1073741824
original_error_code: ERR_DRY_RUN_FAILED
policy_status: accepted
resources:
  - datamart-vca-494114.marts.fct_lead_enriched
dry_run_exception_type: BadRequest
dry_run_http_code: 400
dry_run_reason: invalidQuery
dry_run_message_sanitized: "Syntax error: Unexpected keyword ROWS at [1:118]"
classification: INVALID_SQL_SYNTAX
root_cause: "Agent-generated alias `AS rows` is invalid in BigQuery."
```

```sql
SELECT COALESCE(lead_tier, 'UNKNOWN') AS lead_tier, COALESCE(lead_priority, 'UNKNOWN') AS lead_priority, COUNT(1) AS rows, COUNT(DISTINCT lead_id) AS distinct_leads, COUNTIF(is_qualified_for_meta_offline) AS qualified_offline_rows, COUNTIF(tiene_billetes) AS tiene_billetes_rows, AVG(score_inicial) AS avg_score_inicial, MIN(day) AS min_day, MAX(day) AS max_day FROM `datamart-vca-494114.marts.fct_lead_enriched` WHERE day <= DATE '2026-06-30' GROUP BY lead_tier, lead_priority ORDER BY lead_tier, lead_priority
```

### q003b

```yaml
query_id: q003b
request_id: codex-vca-auc001-v2-q003b-lead-quality-base-20260715
trace_id: trc-dad161eb94804a709e0fb18ab883daa0
sql_recovered: true
execution_context:
  project_id: datamart-vca-494114
  dataset_id: marts
  max_bytes_billed: 1073741824
original_error_code: ERR_DRY_RUN_FAILED
policy_status: accepted
resources:
  - datamart-vca-494114.marts.fct_lead_enriched
dry_run_exception_type: BadRequest
dry_run_http_code: 400
dry_run_reason: invalidQuery
dry_run_message_sanitized: "Syntax error: Unexpected keyword ROWS at [1:118]"
classification: INVALID_SQL_SYNTAX
root_cause: "Agent-generated alias `AS rows` is invalid in BigQuery."
```

```sql
SELECT COALESCE(lead_tier, 'UNKNOWN') AS lead_tier, COALESCE(lead_priority, 'UNKNOWN') AS lead_priority, COUNT(1) AS rows, COUNT(DISTINCT lead_id) AS distinct_leads, SUM(CASE WHEN is_qualified_for_meta_offline THEN 1 ELSE 0 END) AS qualified_offline_rows, SUM(CASE WHEN tiene_billetes THEN 1 ELSE 0 END) AS tiene_billetes_rows, SUM(score_inicial) AS sum_score_inicial, MIN(day) AS min_day, MAX(day) AS max_day FROM `datamart-vca-494114.marts.fct_lead_enriched` WHERE day <= DATE '2026-06-30' GROUP BY 1, 2 ORDER BY 1, 2
```

### q003c

```yaml
query_id: q003c
request_id: codex-vca-auc001-v2-q003c-lead-tier-minimal-20260715
trace_id: trc-e1fc0ab2981640c09a35eb933c89eac7
sql_recovered: true
execution_context:
  project_id: datamart-vca-494114
  dataset_id: marts
  max_bytes_billed: 1073741824
original_error_code: ERR_DRY_RUN_FAILED
policy_status: accepted
resources:
  - datamart-vca-494114.marts.fct_lead_enriched
dry_run_exception_type: BadRequest
dry_run_http_code: 400
dry_run_reason: invalidQuery
dry_run_message_sanitized: "Syntax error: Unexpected keyword ROWS at [1:31]"
classification: INVALID_SQL_SYNTAX
root_cause: "Agent-generated alias `AS rows` is invalid in BigQuery."
```

```sql
SELECT lead_tier, COUNT(1) AS rows FROM `datamart-vca-494114.marts.fct_lead_enriched` WHERE day <= DATE '2026-06-30' GROUP BY lead_tier ORDER BY rows DESC
```

### q003d

```yaml
query_id: q003d
request_id: codex-vca-auc001-v2-q003d-score-minimal-20260715
trace_id: trc-008e79f6757f4e8288b902a20945769f
sql_recovered: true
execution_context:
  project_id: datamart-vca-494114
  dataset_id: marts
  max_bytes_billed: 1073741824
original_error_code: ERR_DRY_RUN_FAILED
policy_status: accepted
dry_run_message_sanitized: "Syntax error: Unexpected keyword ROWS at [1:35]"
classification: INVALID_SQL_SYNTAX
```

```sql
SELECT score_inicial, COUNT(1) AS rows FROM `datamart-vca-494114.marts.fct_lead_enriched` WHERE day <= DATE '2026-06-30' GROUP BY score_inicial ORDER BY score_inicial
```

### q003e

```yaml
query_id: q003e
request_id: codex-vca-auc001-v2-q003e-qualified-minimal-20260715
trace_id: trc-c829aa72ad654cc8880796b233cf9150
sql_recovered: true
execution_context:
  project_id: datamart-vca-494114
  dataset_id: marts
  max_bytes_billed: 1073741824
original_error_code: ERR_DRY_RUN_FAILED
policy_status: accepted
dry_run_message_sanitized: "Syntax error: Unexpected keyword ROWS at [1:51]"
classification: INVALID_SQL_SYNTAX
```

```sql
SELECT is_qualified_for_meta_offline, COUNT(1) AS rows FROM `datamart-vca-494114.marts.fct_lead_enriched` WHERE day <= DATE '2026-06-30' GROUP BY is_qualified_for_meta_offline ORDER BY is_qualified_for_meta_offline
```

### q003f

```yaml
query_id: q003f
request_id: codex-vca-auc001-v2-q003f-ticket-status-minimal-20260715
trace_id: trc-26b197c8342043c0a64bb720da924a48
sql_recovered: true
execution_context:
  project_id: datamart-vca-494114
  dataset_id: marts
  max_bytes_billed: 1073741824
original_error_code: ERR_DRY_RUN_FAILED
policy_status: accepted
dry_run_message_sanitized: "Syntax error: Unexpected keyword ROWS at [1:35]"
classification: INVALID_SQL_SYNTAX
```

```sql
SELECT ticket_status, COUNT(1) AS rows FROM `datamart-vca-494114.marts.fct_lead_enriched` WHERE day <= DATE '2026-06-30' GROUP BY ticket_status ORDER BY rows DESC
```

### q005

```yaml
query_id: q005
request_id: codex-vca-auc001-v2-q005-scoring-mapping-20260715
trace_id: trc-72c3e6dcdac34b4fa1e2d3f5a3e31e2c
sql_recovered: true
execution_context:
  project_id: datamart-vca-494114
  dataset_id: intermediate
  max_bytes_billed: 1073741824
original_error_code: ERR_DRY_RUN_FAILED
policy_status: accepted
resources:
  - datamart-vca-494114.intermediate.int_faro_lead_scoring
dry_run_exception_type: BadRequest
dry_run_http_code: 400
dry_run_reason: invalidQuery
dry_run_message_sanitized: "Syntax error: Unexpected keyword ROWS at [1:65]"
classification: INVALID_SQL_SYNTAX
root_cause: "Agent-generated alias `AS rows` is invalid in BigQuery."
```

```sql
SELECT COALESCE(lead_tier, 'UNKNOWN') AS lead_tier, COUNT(1) AS rows, SUM(CASE WHEN is_q_tiene_billetes_mapped THEN 1 ELSE 0 END) AS mapped_billetes, SUM(CASE WHEN is_q_cuando_viaja_mapped THEN 1 ELSE 0 END) AS mapped_cuando_viaja, SUM(CASE WHEN is_q_num_personas_mapped THEN 1 ELSE 0 END) AS mapped_num_personas, SUM(CASE WHEN is_q_tipo_experiencia_mapped THEN 1 ELSE 0 END) AS mapped_tipo_experiencia, SUM(CASE WHEN is_form_origen_mapped THEN 1 ELSE 0 END) AS mapped_form_origen, COUNTIF(unmapped_reason IS NOT NULL) AS rows_with_unmapped_reason FROM `datamart-vca-494114.intermediate.int_faro_lead_scoring` WHERE lead_date <= DATE '2026-06-30' GROUP BY 1 ORDER BY 1
```

### q006

```yaml
query_id: q006
request_id: codex-vca-auc001-v2-q006-lead-platform-product-20260715
trace_id: trc-b1fbb991a9204fbbb6c6e4e2ea0cb4ef
sql_recovered: true
execution_context:
  project_id: datamart-vca-494114
  dataset_id: marts
  max_bytes_billed: 1073741824
original_error_code: ERR_DRY_RUN_FAILED
policy_status: accepted
dry_run_message_sanitized: "Syntax error: Unexpected keyword ROWS at [1:147]"
classification: INVALID_SQL_SYNTAX
```

```sql
SELECT COALESCE(platform, 'UNKNOWN') AS platform, COALESCE(product, 'UNKNOWN') AS product, COALESCE(is_organic, FALSE) AS is_organic, COUNT(1) AS rows, COUNT(DISTINCT lead_id) AS distinct_leads, SUM(CASE WHEN lead_tier IN ('A','B') THEN 1 ELSE 0 END) AS qualified_tier_ab_rows FROM `datamart-vca-494114.marts.fct_lead_enriched` WHERE day <= DATE '2026-06-30' GROUP BY 1, 2, 3 ORDER BY rows DESC
```

### q007

```yaml
query_id: q007
request_id: codex-vca-auc001-v2-q007-intermediate-tier-20260715
trace_id: trc-07e4fc70e3e2447095f6f3af0825b808
sql_recovered: true
execution_context:
  project_id: datamart-vca-494114
  dataset_id: intermediate
  max_bytes_billed: 1073741824
original_error_code: ERR_DRY_RUN_FAILED
policy_status: accepted
dry_run_message_sanitized: "Syntax error: Unexpected keyword ROWS at [1:46]"
classification: INVALID_SQL_SYNTAX
```

```sql
SELECT lead_tier, lead_priority, COUNT(1) AS rows, COUNT(DISTINCT lead_id) AS distinct_leads FROM `datamart-vca-494114.intermediate.int_faro_lead_scoring` WHERE lead_date <= DATE '2026-06-30' GROUP BY lead_tier, lead_priority ORDER BY rows DESC
```

### q008

```yaml
query_id: q008
request_id: codex-vca-auc001-v2-q008-intermediate-score-20260715
trace_id: trc-f6dd5c1adbd1406aa8b0d7d1b7987f85
sql_recovered: true
execution_context:
  project_id: datamart-vca-494114
  dataset_id: intermediate
  max_bytes_billed: 1073741824
original_error_code: ERR_DRY_RUN_FAILED
policy_status: accepted
dry_run_message_sanitized: "Syntax error: Unexpected keyword ROWS at [1:35]"
classification: INVALID_SQL_SYNTAX
```

```sql
SELECT score_inicial, COUNT(1) AS rows FROM `datamart-vca-494114.intermediate.int_faro_lead_scoring` WHERE lead_date <= DATE '2026-06-30' GROUP BY score_inicial ORDER BY score_inicial
```

### q009

```yaml
query_id: q009
request_id: codex-vca-auc001-v2-q009-intermediate-ticket-20260715
trace_id: trc-4f8ac8a774104d79b174a958f9141dd6
sql_recovered: true
execution_context:
  project_id: datamart-vca-494114
  dataset_id: intermediate
  max_bytes_billed: 1073741824
original_error_code: ERR_DRY_RUN_FAILED
policy_status: accepted
dry_run_message_sanitized: "Syntax error: Unexpected keyword ROWS at [1:51]"
classification: INVALID_SQL_SYNTAX
```

```sql
SELECT ticket_status, tiene_billetes, COUNT(1) AS rows, COUNT(DISTINCT lead_id) AS distinct_leads FROM `datamart-vca-494114.intermediate.int_faro_lead_scoring` WHERE lead_date <= DATE '2026-06-30' GROUP BY ticket_status, tiene_billetes ORDER BY rows DESC
```

### q012

```yaml
query_id: q012
request_id: codex-vca-auc001-v2-q012-leads-date-only-monthly-20260715
trace_id: trc-7983a05a8eb341dc935ca5091067ea45
sql_recovered: true
execution_context:
  project_id: datamart-vca-494114
  dataset_id: marts
  max_bytes_billed: 1073741824
original_error_code: ERR_DRY_RUN_FAILED
policy_status: accepted
resources:
  - datamart-vca-494114.marts.fct_lead_enriched
dry_run_exception_type: BadRequest
dry_run_http_code: 400
dry_run_reason: invalidQuery
dry_run_message_sanitized: "Syntax error: Unexpected keyword ROWS at [1:53]"
classification: INVALID_SQL_SYNTAX
root_cause: "Agent-generated alias `AS rows` is invalid in BigQuery."
```

```sql
SELECT DATE_TRUNC(day, MONTH) AS month, COUNT(1) AS rows, COUNT(DISTINCT lead_id) AS distinct_leads FROM `datamart-vca-494114.marts.fct_lead_enriched` WHERE day <= DATE '2026-06-30' GROUP BY month ORDER BY month
```

### q019

```yaml
query_id: q019
request_id: codex-vca-auc001-v2-q019-scoring-components-20260715
trace_id: trc-b896ed5cb8f54307afa29fee14b9cf96
sql_recovered: true
execution_context:
  project_id: datamart-vca-494114
  dataset_id: intermediate
  max_bytes_billed: 1073741824
original_error_code: ERR_DRY_RUN_FAILED
policy_status: accepted
resources:
  - datamart-vca-494114.intermediate.int_faro_lead_scoring
dry_run_exception_type: BadRequest
dry_run_http_code: 400
dry_run_reason: invalidQuery
dry_run_message_sanitized: "Syntax error: Unexpected keyword ROWS at [1:310]"
classification: INVALID_SQL_SYNTAX
root_cause: "Agent-generated alias `AS rows` is invalid in BigQuery."
```

```sql
SELECT SUM(score_billetes) AS sum_score_billetes, SUM(score_fecha_viaje) AS sum_score_fecha_viaje, SUM(score_tipo_experiencia) AS sum_score_tipo_experiencia, SUM(score_num_personas) AS sum_score_num_personas, SUM(score_formulario) AS sum_score_formulario, SUM(score_inicial) AS sum_score_inicial, COUNT(1) AS rows FROM `datamart-vca-494114.intermediate.int_faro_lead_scoring` WHERE lead_date <= DATE '2026-06-30'
```

### q022

```yaml
query_id: q022
request_id: codex-vca-auc001-v2-q022-normalized-ad-performance-20260715
trace_id: trc-823486a0918f411a8fe499802c126ad5
sql_recovered: true
execution_context:
  project_id: datamart-vca-494114
  dataset_id: marts
  max_bytes_billed: 1073741824
original_error_code: ERR_DRY_RUN_FAILED
policy_status: accepted
resources:
  - datamart-vca-494114.intermediate.int_faro_lead_scoring
  - datamart-vca-494114.marts.fct_spend
dry_run_exception_type: BadRequest
dry_run_http_code: 400
dry_run_reason: invalidQuery
dry_run_message_sanitized: "No matching signature for function COALESCE. Argument types: STRUCT<...>, INT64 at [1:1113]"
classification: TYPE_MISMATCH
root_cause: "In ORDER BY, `COALESCE(leads, 0)` resolves `leads` as the CTE/table alias STRUCT rather than the numeric selected alias. The query needs a non-conflicting column alias or qualified expression."
```

```sql
WITH leads AS (SELECT REPLACE(ad_id, 'ag:', '') AS ad_id, ANY_VALUE(ad_name) AS lead_ad_name, ANY_VALUE(campaign_name) AS lead_campaign_name, COUNT(1) AS leads, COUNTIF(lead_tier IN ('A','B')) AS qualified_leads, COUNTIF(tiene_billetes) AS tiene_billetes_leads FROM `datamart-vca-494114.intermediate.int_faro_lead_scoring` WHERE lead_date <= DATE '2026-06-30' AND ad_id IS NOT NULL GROUP BY ad_id), spend AS (SELECT ad_id, ANY_VALUE(ad_name) AS spend_ad_name, ANY_VALUE(campaign_signal) AS campaign_signal, SUM(spend_amount) AS spend_amount FROM `datamart-vca-494114.marts.fct_spend` WHERE spend_period <= DATE '2026-06-30' AND ad_id IS NOT NULL GROUP BY ad_id) SELECT COALESCE(leads.ad_id, spend.ad_id) AS ad_id, COALESCE(lead_ad_name, spend_ad_name) AS ad_name, lead_campaign_name, campaign_signal, leads, qualified_leads, tiene_billetes_leads, spend_amount, CASE WHEN leads.ad_id IS NOT NULL AND spend.ad_id IS NOT NULL THEN 'matched' WHEN leads.ad_id IS NOT NULL THEN 'lead_only' ELSE 'spend_only' END AS coverage_state FROM leads FULL OUTER JOIN spend USING (ad_id) ORDER BY COALESCE(spend_amount, 0) DESC, COALESCE(leads, 0) DESC LIMIT 15
```

### q021

```yaml
query_id: q021
request_id: codex-vca-auc001-v2-q021-normalized-commercial-quality-efficiency-20260715
trace_id: trc-043653f090c4451093f81b45be748c5f
sql_recovered: true
execution_context:
  project_id: datamart-vca-494114
  dataset_id: marts
  max_bytes_billed: 1073741824
original_error_code: ERR_SCOPE_DENIED
policy_status: rejected
policy_error: ERR_SCOPE_DENIED
contains_comma_inside_from: true
dry_run_performed: false
classification: SQL_POLICY_LIMITATION
root_cause: "The current SQL Policy rejects commas in the FROM clause. q021 contains `FROM `datamart-vca-494114.intermediate.int_faro_lead_scoring`, spend WHERE ...`."
```

```sql
WITH commercial_ads AS (SELECT DISTINCT ad_id FROM `datamart-vca-494114.marts.fct_spend` WHERE spend_period <= DATE '2026-06-30' AND campaign_signal = 'COMMERCIAL'), spend AS (SELECT SUM(spend_amount) AS commercial_spend FROM `datamart-vca-494114.marts.fct_spend` WHERE spend_period <= DATE '2026-06-30' AND campaign_signal = 'COMMERCIAL') SELECT COUNT(1) AS leads_total, COUNTIF(lead_tier IN ('A','B')) AS qualified_total, COUNTIF(REPLACE(ad_id, 'ag:', '') IN (SELECT ad_id FROM commercial_ads)) AS leads_on_commercial_spend_ads, COUNTIF(REPLACE(ad_id, 'ag:', '') IN (SELECT ad_id FROM commercial_ads) AND lead_tier IN ('A','B')) AS qualified_on_commercial_spend_ads, ANY_VALUE(spend.commercial_spend) AS commercial_spend FROM `datamart-vca-494114.intermediate.int_faro_lead_scoring`, spend WHERE lead_date <= DATE '2026-06-30'
```

## SQL Policy Findings

All 14 `ERR_DRY_RUN_FAILED` SQL statements were accepted by `ReadOnlySqlGuard.validate_and_qualify()` and mapped only to allowlisted resources.

q021 was rejected before BigQuery access:

```yaml
query_id: q021
policy_status: rejected
policy_error: ERR_SCOPE_DENIED
confirmed_pattern: comma_inside_FROM
```

The relevant implementation rejects a comma found inside a `FROM` clause segment before `WHERE`, `GROUP`, `ORDER`, `HAVING`, `QUALIFY`, `LIMIT`, or `UNION`. q021 has exactly that shape.

## Direct Dry Run Findings

All direct dry runs used `GoogleBigQueryGateway(settings).dry_run(qualified_sql)`.

```yaml
dry_run_project: datamart-vca-494114
dry_run_location: EU
job_execution: dry_run_only
job_result_called: false
rows_returned: false
authentication_error: false
permission_error: false
location_error: false
provider_or_gateway_error: false
```

Direct dry run results:

| Query | Direct dry run result | Classification |
| --- | --- | --- |
| q003 | BigQuery `BadRequest 400 invalidQuery`, unexpected keyword `ROWS` | `INVALID_SQL_SYNTAX` |
| q003b | BigQuery `BadRequest 400 invalidQuery`, unexpected keyword `ROWS` | `INVALID_SQL_SYNTAX` |
| q003c | BigQuery `BadRequest 400 invalidQuery`, unexpected keyword `ROWS` | `INVALID_SQL_SYNTAX` |
| q003d | BigQuery `BadRequest 400 invalidQuery`, unexpected keyword `ROWS` | `INVALID_SQL_SYNTAX` |
| q003e | BigQuery `BadRequest 400 invalidQuery`, unexpected keyword `ROWS` | `INVALID_SQL_SYNTAX` |
| q003f | BigQuery `BadRequest 400 invalidQuery`, unexpected keyword `ROWS` | `INVALID_SQL_SYNTAX` |
| q005 | BigQuery `BadRequest 400 invalidQuery`, unexpected keyword `ROWS` | `INVALID_SQL_SYNTAX` |
| q006 | BigQuery `BadRequest 400 invalidQuery`, unexpected keyword `ROWS` | `INVALID_SQL_SYNTAX` |
| q007 | BigQuery `BadRequest 400 invalidQuery`, unexpected keyword `ROWS` | `INVALID_SQL_SYNTAX` |
| q008 | BigQuery `BadRequest 400 invalidQuery`, unexpected keyword `ROWS` | `INVALID_SQL_SYNTAX` |
| q009 | BigQuery `BadRequest 400 invalidQuery`, unexpected keyword `ROWS` | `INVALID_SQL_SYNTAX` |
| q012 | BigQuery `BadRequest 400 invalidQuery`, unexpected keyword `ROWS` | `INVALID_SQL_SYNTAX` |
| q019 | BigQuery `BadRequest 400 invalidQuery`, unexpected keyword `ROWS` | `INVALID_SQL_SYNTAX` |
| q022 | BigQuery `BadRequest 400 invalidQuery`, `COALESCE` STRUCT/INT64 mismatch | `TYPE_MISMATCH` |
| q021 | rejected by SQL Policy before dry run | `SQL_POLICY_LIMITATION` |

## Answers

1. Do the failures mainly come from incorrect SQL generated by Codex?

Yes. 14 of 15 rejected queries are invalid BigQuery SQL generated during AUC-001 v2. The dominant issue is aliasing counts as `rows`.

2. Is there any BigQuery-valid query incorrectly rejected by MCP?

Not confirmed. q021 may be semantically valid Standard SQL as a cross join form, but the current MCP SQL Policy intentionally rejects commas in `FROM`. That is a policy limitation, not evidence of a gateway or BigQuery defect.

3. Is there a functional gap in the server?

Yes, but it is observability and developer ergonomics, not query execution correctness. `CostGuard` wraps BigQuery `BadRequest` exceptions as `ERR_DRY_RUN_FAILED`, so the client loses the actionable syntax/type error.

4. Is the problem only observability?

No. Observability is insufficient, but the root cause of the rejected dry runs is invalid SQL generated by the agent. Better observability would have made this obvious earlier.

5. Does MCP need modification before the natural language test?

No hard blocker. The natural language test can proceed if the agent avoids invalid aliases such as `rows`, avoids ambiguous aliases/CTE names, and avoids comma joins. A minimal MCP improvement is recommended later: preserve sanitized BigQuery dry-run exception type/reason internally.

## Minimal Proposed Action, Not Implemented

For agent/query generation:

- Do not alias a column as `rows`; use `row_count`, `lead_rows`, `spend_rows`, or quote as backtick-escaped only when unavoidable.
- Do not reuse a CTE name as an output column alias.
- Do not use comma joins; use `CROSS JOIN` or a scalar subquery shape accepted by the SQL Policy.

For MCP observability:

- Log sanitized original exception type, reason, HTTP status, location, project, and SQL fingerprint before wrapping as `ERR_DRY_RUN_FAILED`.
- Keep public MCP contract unchanged.

## Final Result

```yaml
scope_denied_root_cause: "q021 contains a comma in FROM; ReadOnlySqlGuard rejects comma joins with ERR_SCOPE_DENIED."
dry_run_failure_distribution:
  invalid_agent_sql: 14
  policy_limitation: 1
  provider_or_gateway: 0
  unknown: 0
mcp_defect_confirmed: false
observability_gap_confirmed: true
skill_or_prompt_adjustment_needed: true
recommended_action: "Before the natural-language test, adjust prompting/query generation conventions to avoid reserved aliases (`rows`), CTE/column alias collisions, and comma joins. Optionally add sanitized internal dry-run exception logging later."
ready_for_natural_language_test: true
```
