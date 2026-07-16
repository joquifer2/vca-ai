# AUC-001 Evidence Acquisition

## Metadata

| Field | Value |
|---|---|
| Artifact ID | VCA-AUC-001-EVD-ACQ-001 |
| Artifact Type | Evidence Acquisition Record |
| Analytical Use Case | AUC-001 - Meta Lead Quality Analysis |
| Related Data Contract | VCA-AUC-001-DATA-001 |
| Status | Completed with limitations |
| Version | 1.0.0 |
| Last Updated | 2026-07-12 |
| Owner | Equipo VCA |
| Backing Task | T-018 |

---

## Purpose

Registrar la adquisicion de evidencia reproducible desde BigQuery para AUC-001 junio 2026.

La verificacion de la exposicion de datos se realizo mediante BigQuery CLI sobre el proyecto `datamart-vca-494114`.
El acceso directo por BigQuery MCP Server sigue pendiente de validacion documental y tecnica.

Este artefacto expone origen, periodo, consultas, metricas agregadas y limitaciones observadas.

Este artefacto no interpreta datos.

Este artefacto no formula hallazgos, conclusiones ni recomendaciones.

---

## Backing Task

| Field | Value |
|---|---|
| Task ID | T-018 |
| Task | Implementar la adquisicion de evidencia desde BigQuery con verificacion de exposicion por CLI y MCP pendiente |
| Specifications | SPEC-001 Analytical Lifecycle; SPEC-002 Component Boundaries |
| Skill | meta-lead-quality-analysis |
| Acceptance Criterion | El Data Provider expone evidencia reproducible con origen, periodo, metricas y limitaciones explicitadas, con validacion directa del MCP Server pendiente |

---

## Upstream Artifacts

| Artifact | Relationship | Status |
|---|---|---|
| [AUC-001 Context Definition](auc-001-context-definition.md) | Scope and period | Validated |
| [AUC-001 Data Contract](auc-001-data-contract.md) | Requested data contract | Documented |
| [VCA-DATA-001 Base Data Contract](/docs/contracts/data.contract.md) | Contract rules | Documented |
| [AUC-001](/analytical_use_cases/meta_lead_quality_analysis.md) | Analytical use case | Available |
| [meta-lead-quality-analysis Skill](/.github/skills/meta-lead-quality-analysis/SKILL.md) | Execution rules | Available |

---

## Acquisition Scope

| Field | Value |
|---|---|
| execution_id | VCA-AUC-001-EXEC-2026-06 |
| period | 2026-06-01 to 2026-06-30 |
| provider | BigQuery CLI over project datamart-vca-494114 |
| project_detected | datamart-vca-494114 |
| account_detected | jordi@jordiquiroga.com |
| requested_scope | Meta Lead Ads campaigns, ad sets and creatives with investment or leads during the period |
| filters | campaign_signal = COMMERCIAL where exposed; exclude test records, duplicates and leads without valid identifier where exposed; no additional geographic filter |
| lead_quality_definition | Qualified Lead according to FARO, equivalent to Lead Tier A or B |

---

## Provider Availability Checks

| Check | Result | Evidence |
|---|---|---|
| BigQuery CLI installed | Pass | `bq.cmd` is available locally |
| Google Cloud SDK installed | Pass | `gcloud.ps1` is available locally |
| Dataset listing | Pass | BigQuery exposed datasets in project `datamart-vca-494114` |
| Candidate table listing | Pass | Tables/views exposed under `raw_meta`, `staging`, `intermediate`, `marts` |
| Schema access | Pass | Schemas read for `marts.fct_lead_enriched`, `marts.fct_performance_daily`, `marts.fct_spend`, `marts.dim_campaign_signal` |
| Aggregate query execution | Pass | Aggregated evidence queries returned results |
| Direct MCP access verification | Pending | `docs/context_refs.md` still marks BigQuery MCP Server documentation as PENDING |

---

## Dataset Exposure

| Dataset | Location | Role Observed |
|---|---|---|
| analytics_dev | EU | Available dataset; not selected as primary source for this acquisition |
| control | EU | Available dataset; not selected as primary source for this acquisition |
| intermediate | EU | Intermediate FARO/CLARO tables available |
| marts | EU | Primary marts selected for this acquisition |
| raw_meta | EU | Raw Meta Ads tables available |
| raw_sheets | EU | Raw sheets dataset available |
| reference | EU | Reference dataset available |
| staging | EU | Staging views available |

---

## Source Tables Used

| Table | Type | Rows | Role In Acquisition |
|---|---|---:|---|
| `datamart-vca-494114.marts.fct_lead_enriched` | TABLE | 1432 | Lead volume, lead identifiers, lead tier, campaign/adset/ad references |
| `datamart-vca-494114.marts.fct_performance_daily` | TABLE | 393 | Commercial performance by day/concept/version/angle |
| `datamart-vca-494114.marts.fct_spend` | TABLE | 7333 | Spend records by period/ad/concept/version/angle and campaign_signal |
| `datamart-vca-494114.marts.dim_campaign_signal` | TABLE | 4 | Campaign signal domain values |

---

## Period Coverage Checks

| Source | Min Date | Max Date | Rows In June 2026 | Query Scope |
|---|---|---|---:|---|
| fct_lead_enriched | 2026-04-18 | 2026-07-12 | 772 | `day BETWEEN 2026-06-01 AND 2026-06-30` |
| fct_performance_daily | 2026-04-18 | 2026-07-12 | 220 | `day BETWEEN 2026-06-01 AND 2026-06-30` |
| fct_spend | 2026-04-18 | 2026-07-01 | 4304 | `spend_period BETWEEN 2026-06-01 AND 2026-06-30` |

---

## Acquired Aggregate Evidence

### Lead Volume And Quality

Origin: `datamart-vca-494114.marts.fct_lead_enriched`

Period: 2026-06-01 to 2026-06-30

| Metric | Value |
|---|---:|
| leads_total | 772 |
| distinct_leads | 772 |
| invalid_lead_id_rows | 0 |
| qualified_leads_ab | 226 |
| lead_tier_a | 31 |
| lead_tier_b | 195 |
| lead_tier_unknown | 0 |
| distinct_campaigns | 2 |
| distinct_adsets | 2 |
| distinct_ads | 13 |

### Commercial Performance

Origin: `datamart-vca-494114.marts.fct_performance_daily`

Period: 2026-06-01 to 2026-06-30

Filter: `campaign_signal = 'COMMERCIAL'`

| Metric | Value |
|---|---:|
| rows_total | 113 |
| leads | 638 |
| spend | 439.490009 |
| cpl | 0.6888558134796238 |
| billetes_yes | 86 |
| billetes_process | 164 |
| solo_mirando | 388 |
| distinct_concepts | 3 |
| distinct_versions | 1 |
| distinct_angles | 6 |

### Commercial Spend

Origin: `datamart-vca-494114.marts.fct_spend`

Period: 2026-06-01 to 2026-06-30

Filter: `campaign_signal = 'COMMERCIAL'`

| Metric | Value |
|---|---:|
| rows_total | 4159 |
| spend_amount | 496.5600089999888 |
| distinct_ads | 10 |
| distinct_concepts | 3 |
| distinct_versions | 1 |
| distinct_angles | 8 |
| distinct_accounts | 1 |

### Campaign Signal Domain

Origin: `datamart-vca-494114.marts.dim_campaign_signal`

| signal_code | signal_name |
|---|---|
| ACTIVATION | Activacion |
| ATTENTION | Atencion |
| COMMERCIAL | Comercial |
| UNKNOWN | Desconocido |

---

## Reproducibility Queries

### Period Coverage - Leads

```sql
SELECT
  MIN(day) AS min_day,
  MAX(day) AS max_day,
  COUNT(*) AS rows_total,
  COUNTIF(day BETWEEN DATE(2026, 6, 1) AND DATE(2026, 6, 30)) AS rows_june
FROM `datamart-vca-494114.marts.fct_lead_enriched`;
```

### Period Coverage - Performance

```sql
SELECT
  MIN(day) AS min_day,
  MAX(day) AS max_day,
  COUNT(*) AS rows_total,
  COUNTIF(day BETWEEN DATE(2026, 6, 1) AND DATE(2026, 6, 30)) AS rows_june
FROM `datamart-vca-494114.marts.fct_performance_daily`;
```

### Period Coverage - Spend

```sql
SELECT
  MIN(spend_period) AS min_day,
  MAX(spend_period) AS max_day,
  COUNT(*) AS rows_total,
  COUNTIF(spend_period BETWEEN DATE(2026, 6, 1) AND DATE(2026, 6, 30)) AS rows_june
FROM `datamart-vca-494114.marts.fct_spend`;
```

### Lead Volume And Quality

```sql
SELECT
  COUNT(*) AS leads_total,
  COUNT(DISTINCT lead_id) AS distinct_leads,
  COUNTIF(lead_id IS NULL OR lead_id = '') AS invalid_lead_id_rows,
  COUNTIF(lead_tier IN ('A', 'B')) AS qualified_leads_ab,
  COUNTIF(lead_tier = 'A') AS lead_tier_a,
  COUNTIF(lead_tier = 'B') AS lead_tier_b,
  COUNTIF(lead_tier IS NULL OR lead_tier = '') AS lead_tier_unknown,
  COUNT(DISTINCT campaign_id) AS distinct_campaigns,
  COUNT(DISTINCT adset_id) AS distinct_adsets,
  COUNT(DISTINCT ad_id) AS distinct_ads
FROM `datamart-vca-494114.marts.fct_lead_enriched`
WHERE day BETWEEN DATE(2026, 6, 1) AND DATE(2026, 6, 30);
```

### Commercial Performance

```sql
SELECT
  campaign_signal,
  COUNT(*) AS rows_total,
  SUM(leads) AS leads,
  SUM(spend) AS spend,
  SAFE_DIVIDE(SUM(spend), NULLIF(SUM(leads), 0)) AS cpl,
  SUM(billetes_yes) AS billetes_yes,
  SUM(billetes_process) AS billetes_process,
  SUM(solo_mirando) AS solo_mirando,
  COUNT(DISTINCT concept_id) AS distinct_concepts,
  COUNT(DISTINCT version_id) AS distinct_versions,
  COUNT(DISTINCT angle_id) AS distinct_angles
FROM `datamart-vca-494114.marts.fct_performance_daily`
WHERE day BETWEEN DATE(2026, 6, 1) AND DATE(2026, 6, 30)
  AND campaign_signal = 'COMMERCIAL'
GROUP BY campaign_signal;
```

### Commercial Spend

```sql
SELECT
  campaign_signal,
  COUNT(*) AS rows_total,
  SUM(spend_amount) AS spend_amount,
  COUNT(DISTINCT ad_id) AS distinct_ads,
  COUNT(DISTINCT concept_id) AS distinct_concepts,
  COUNT(DISTINCT version_id) AS distinct_versions,
  COUNT(DISTINCT angle_id) AS distinct_angles,
  COUNT(DISTINCT account_id) AS distinct_accounts
FROM `datamart-vca-494114.marts.fct_spend`
WHERE spend_period BETWEEN DATE(2026, 6, 1) AND DATE(2026, 6, 30)
  AND campaign_signal = 'COMMERCIAL'
GROUP BY campaign_signal;
```

---

## Limitations

| Limitation | Impact | Handling |
|---|---|---|
| `fct_lead_enriched` does not expose `campaign_signal` directly | Commercial filter cannot be applied inside this table without an additional mapping/join | Propagate to Discovery for relationship validation |
| `fct_performance_daily` is aggregated by concept/version/angle, not campaign/adset/ad/creative | It supports commercial performance but not full campaign/adset/creative traceability by itself | Combine with source mapping during Discovery if required |
| `fct_spend` exposes commercial spend by ad/concept/version/angle but not lead quality | Spend and quality are exposed in separate tables | Discovery must validate relationships before preparation |
| Lead aggregate, performance aggregate and spend aggregate expose different totals and granularities | Values should not be merged without a validated relationship model | Propagate to Discovery Contract |
| Duplicate/test-record flags are not explicitly mapped in the acquired aggregate | The acquisition verifies `lead_id` validity but not full exclusion logic for tests/duplicates | Propagate as mapping gap to Discovery |
| Geographic filter is intentionally absent | No geography segmentation is applied in this execution | Preserve as execution constraint |
| BigQuery MCP Server documentation remains PENDING | Direct MCP execution was not verified in this acquisition | Validate separately if the task requires MCP-level access |

---

## Transition Status

| Target | Status | Reason |
|---|---|---|
| T-018 completion | Completed with limitations | Data Provider exposure was verified through BigQuery CLI for the June 2026 execution; direct MCP validation remains pending |
| T-019 Discovery Contract | Ready | Discovery can now formalize entities, dimensions, metrics, relationships and limitations observed during acquisition |
| Evidence Set | Not yet authorized | Evidence Set belongs to T-022 after Discovery, preparation and Analytical Contract steps |

---

## Traceability

- [T-018 in docs/tasks.md](/docs/tasks.md)
- [AUC-001 Data Contract](auc-001-data-contract.md)
- [AUC-001 Context Definition](auc-001-context-definition.md)
- [AUC-001 Execution Context](auc-001-execution-context.md)
- [SPEC-001 Analytical Lifecycle](/specs/spec-001-analytical-lifecycle.md)
- [SPEC-002 Component Boundaries](/specs/spec-002-component-boundaries.md)
- [AUC-001 Meta Lead Quality Analysis](/analytical_use_cases/meta_lead_quality_analysis.md)
- [Meta Lead Quality Analysis Skill](/.github/skills/meta-lead-quality-analysis/SKILL.md)
- [Context References](/docs/context_refs.md)

---

## Completion Statement

T-018 is complete with limitations.

The Data Provider exposure was verified through BigQuery CLI for the June 2026 execution, including origin tables, period coverage, core metrics and explicit limitations.

This artifact does not claim direct BigQuery MCP Server execution.

No analytical interpretation, conclusion or recommendation is made in this artifact.