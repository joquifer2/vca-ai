# AUC-001 Analytical Preparation

## Metadata

| Field | Value |
|---|---|
| Artifact ID | VCA-AUC-001-AN-PREP-001 |
| Artifact Type | Analytical Preparation Record |
| Analytical Model ID | VCA-AUC-001-AM-001 |
| Analytical Use Case | AUC-001 - Meta Lead Quality Analysis |
| Status | Approved |
| Version | 1.1.0 |
| Last Updated | 2026-07-12 |
| Owner | Equipo VCA |
| Backing Task | T-020 revision - approved |

---

## Purpose

Registrar la preparacion analitica corregida de AUC-001 para transformar las tablas aprobadas en un Analytical Model coherente y apto para producir evidencia observable en fases posteriores.

Este artefacto reemplaza la preparacion anterior basada en `day + concept_id + version_id + angle_id`.

Este artefacto no produce hallazgos analiticos.

Este artefacto no interpreta resultados.

Este artefacto no formula conclusiones ni recomendaciones.

---

## Backing Task

| Field | Value |
|---|---|
| Task ID | T-020 |
| Task | Implementar la preparacion analitica del caso AUC-001 |
| Specifications | SPEC-001 Analytical Lifecycle; SPEC-002 Component Boundaries |
| Skill | meta-lead-quality-analysis |
| Acceptance Criterion | La capa analitica transforma los datos adquiridos en un Analytical Model coherente para el caso |
| Revision basis | T-019 revised Discovery Contract using normalized `ad_id`; cross-artifact review requested explicit metric, creative and validation decisions |

---

## Upstream Artifacts

| Artifact | Relationship | Status |
|---|---|---|
| [AUC-001 Context Definition](auc-001-context-definition.md) | Scope and execution constraints | Validated |
| [AUC-001 Data Contract](auc-001-data-contract.md) | Provider and exposed data structure | Documented with verified exposure |
| [AUC-001 Evidence Acquisition](auc-001-evidence-acquisition.md) | Acquired source evidence and reproducibility queries | Completed with limitations |
| [AUC-001 Source Table Review](auc-001-source-table-review.md) | Corrective source-table and `ad_id` review | Resolved for T-019 |
| [AUC-001 Discovery Contract](auc-001-discovery-contract.md) | Corrected source tables, relationships and grain | Revised after source-table review |
| [AUC-001](../../analytical_use_cases/meta_lead_quality_analysis.md) | Analytical use case | Available |
| [meta-lead-quality-analysis Skill](../../.github/skills/meta-lead-quality-analysis/SKILL.md) | Domain guardrails | Available |

---

## Preparation Scope

| Field | Value |
|---|---|
| execution_id | VCA-AUC-001-EXEC-2026-06 |
| period | 2026-06-01 to 2026-06-30 |
| channel | Meta Ads / Meta Lead Ads |
| approved_source_tables | `marts.fct_lead_enriched`; `intermediate.int_faro_lead_scoring`; `marts.fct_spend` |
| lead_quality_rule | Qualified Lead = `lead_tier IN ('A', 'B')` |
| spend_filter | `campaign_signal = 'COMMERCIAL'` in `fct_spend` |
| analytical_model_grain | normalized `ad_id` |
| coverage_states | `matched`; `lead_only`; `spend_only` |
| preparation_boundary | Aggregate, normalize and align data for later evidence production; no analytical interpretation |

---

## Source Role Selection

| Source | Preparation Role | Reason |
|---|---|---|
| `marts.fct_lead_enriched` | Primary lead-quality base | Mart-level lead fact with campaign/adset/ad metadata, FARO scores, Lead Tier and concept/version/angle fields |
| `intermediate.int_faro_lead_scoring` | Validation and fallback source | Intermediate FARO scoring table validated against `fct_lead_enriched` at normalized `ad_id` grain |
| `marts.fct_spend` | Primary spend base | Spend table exposing `campaign_signal`, `spend_amount`, `spend_period` and `ad_id` |

T-020 uses `fct_lead_enriched` as the model lead source and preserves `int_faro_lead_scoring` as a lineage-compatible validation source. The validation is query-backed and compares both sources at normalized `ad_id` grain.

---

## Metric Decision

| Question | Decision | Evidence |
|---|---|---|
| Does a published `qualified_leads` metric exist in approved source tables? | No | `fct_lead_enriched`, `int_faro_lead_scoring` and `fct_spend` do not expose a `qualified_leads` column |
| Should `qualified_ab` replace a published metric? | No | `qualified_ab` is the canonical prepared measure for this approved source set, derived from the execution rule |
| Is `qualified_ab` temporary? | No, within this approved source set | It is derived from `lead_tier IN ('A', 'B')`, which is the user-provided and documented AUC-001 quality definition; a published `qualified_leads` field can supersede it only if a future approved source exposes one |
| What happens if a future approved table exposes canonical `qualified_leads`? | Revalidate before Evidence Set | The metric can be superseded only through a new source-table decision or contract revision |

---

## Creative Scope Decision

| Item | Decision | Handling |
|---|---|---|
| Creative grain | Prepared as ad/creative reference through normalized `ad_id` and `ad_name` | `ad_id_norm` is the model grain; `ad_name` is retained as creative label |
| Creative asset metadata | Not available in approved source tables | Mark as unavailable; do not infer media, format or asset fields |
| Campaign/adset metadata | Available from lead-side source for matched and lead-only ads | Preserve when available; leave null for spend-only ads |
| Spend-only creatives | Prepared with `ad_id_norm`, `ad_name`, spend and `spend_only` coverage | Do not invent campaign/adset metadata |

---

## Source Validation Against int_faro_lead_scoring

| Validation | Value |
|---|---:|
| compared_ads | 13 |
| matching_ads | 13 |
| mismatching_ads | 0 |
| rows_enriched | 772 |
| rows_scoring | 772 |
| qualified_ab_enriched | 226 |
| qualified_ab_scoring | 226 |

Validation rule: compare `fct_lead_enriched` and `int_faro_lead_scoring` at normalized `ad_id` grain for row count, distinct leads, Lead Tier A/B, Lead Tier A and Lead Tier B.

---

## Prepared Analytical Model

### Model Name

`ad_quality_spend_model`

### Model Grain

| Field | Source | Preparation Rule |
|---|---|---|
| `ad_id_norm` | `fct_lead_enriched.ad_id`; `fct_spend.ad_id` | Normalize lead-side IDs with `REGEXP_REPLACE(ad_id, r'^ag:', '')`; join to `fct_spend.ad_id` |

### Dimensions

| Dimension | Source | Handling |
|---|---|---|
| `ad_name` | Lead or spend source | Use lead-side name when present; otherwise spend-side name; treated as creative label, not full creative asset metadata |
| `campaign_id` | `fct_lead_enriched` | Available for matched and lead-only ads; unavailable for spend-only ads |
| `campaign_name` | `fct_lead_enriched` | Available for matched and lead-only ads; unavailable for spend-only ads |
| `adset_id` | `fct_lead_enriched` | Available for matched and lead-only ads; unavailable for spend-only ads |
| `adset_name` | `fct_lead_enriched` | Available for matched and lead-only ads; unavailable for spend-only ads |
| `coverage_status` | Prepared model | `matched`, `lead_only` or `spend_only` |

### Measures

| Measure | Source | Preparation Rule |
|---|---|---|
| `lead_rows` | `fct_lead_enriched` | Count lead rows by `ad_id_norm` |
| `distinct_leads` | `fct_lead_enriched` | Count distinct `lead_id` by `ad_id_norm` |
| `qualified_ab` | `fct_lead_enriched` | Count leads where `lead_tier IN ('A', 'B')` |
| `lead_tier_a` | `fct_lead_enriched` | Count leads where `lead_tier = 'A'` |
| `lead_tier_b` | `fct_lead_enriched` | Count leads where `lead_tier = 'B'` |
| `spend_amount` | `fct_spend` | Sum commercial spend by `ad_id` |
| `spend_rows` | `fct_spend` | Count commercial spend records by `ad_id` |
| `spend_per_lead` | Prepared model | `SAFE_DIVIDE(spend_amount, NULLIF(lead_rows, 0))` |
| `spend_per_qualified_ab` | Prepared model | `SAFE_DIVIDE(spend_amount, NULLIF(qualified_ab, 0))` |
| `qualified_rate_ab` | Prepared model | `SAFE_DIVIDE(qualified_ab, NULLIF(lead_rows, 0))` |

---

## Preparation SQL

```sql
WITH lead_ads AS (
  SELECT
    REGEXP_REPLACE(ad_id, r'^ag:', '') AS ad_id_norm,
    ANY_VALUE(ad_id) AS lead_ad_id_raw,
    ANY_VALUE(ad_name) AS ad_name,
    ANY_VALUE(campaign_id) AS campaign_id,
    ANY_VALUE(campaign_name) AS campaign_name,
    ANY_VALUE(adset_id) AS adset_id,
    ANY_VALUE(adset_name) AS adset_name,
    COUNT(*) AS lead_rows,
    COUNT(DISTINCT lead_id) AS distinct_leads,
    COUNTIF(lead_tier IN ('A', 'B')) AS qualified_ab,
    COUNTIF(lead_tier = 'A') AS lead_tier_a,
    COUNTIF(lead_tier = 'B') AS lead_tier_b
  FROM `datamart-vca-494114.marts.fct_lead_enriched`
  WHERE day BETWEEN DATE(2026, 6, 1) AND DATE(2026, 6, 30)
  GROUP BY ad_id_norm
),
spend_ads AS (
  SELECT
    ad_id AS ad_id_norm,
    ANY_VALUE(ad_id) AS spend_ad_id_raw,
    ANY_VALUE(ad_name) AS spend_ad_name,
    SUM(spend_amount) AS spend_amount,
    COUNT(*) AS spend_rows
  FROM `datamart-vca-494114.marts.fct_spend`
  WHERE spend_period BETWEEN DATE(2026, 6, 1) AND DATE(2026, 6, 30)
    AND campaign_signal = 'COMMERCIAL'
  GROUP BY ad_id_norm
)
SELECT
  COALESCE(l.ad_id_norm, s.ad_id_norm) AS ad_id_norm,
  COALESCE(l.ad_name, s.spend_ad_name) AS ad_name,
  l.campaign_id,
  l.campaign_name,
  l.adset_id,
  l.adset_name,
  COALESCE(l.lead_rows, 0) AS lead_rows,
  COALESCE(l.distinct_leads, 0) AS distinct_leads,
  COALESCE(l.qualified_ab, 0) AS qualified_ab,
  COALESCE(l.lead_tier_a, 0) AS lead_tier_a,
  COALESCE(l.lead_tier_b, 0) AS lead_tier_b,
  COALESCE(s.spend_amount, 0) AS spend_amount,
  COALESCE(s.spend_rows, 0) AS spend_rows,
  SAFE_DIVIDE(COALESCE(s.spend_amount, 0), NULLIF(COALESCE(l.lead_rows, 0), 0)) AS spend_per_lead,
  SAFE_DIVIDE(COALESCE(s.spend_amount, 0), NULLIF(COALESCE(l.qualified_ab, 0), 0)) AS spend_per_qualified_ab,
  SAFE_DIVIDE(COALESCE(l.qualified_ab, 0), NULLIF(COALESCE(l.lead_rows, 0), 0)) AS qualified_rate_ab,
  CASE
    WHEN l.ad_id_norm IS NOT NULL AND s.ad_id_norm IS NOT NULL THEN 'matched'
    WHEN l.ad_id_norm IS NOT NULL THEN 'lead_only'
    ELSE 'spend_only'
  END AS coverage_status
FROM lead_ads l
FULL OUTER JOIN spend_ads s USING(ad_id_norm);
```

---

## Validation Results

### Coverage By Status

| coverage_status | ad_count | lead_rows | distinct_leads | qualified_ab | lead_tier_a | lead_tier_b | spend_amount |
|---|---:|---:|---:|---:|---:|---:|---:|
| lead_only | 5 | 92 | 92 | 35 | 9 | 26 | 0.0 |
| matched | 8 | 680 | 680 | 191 | 22 | 169 | 494.3600089999987 |
| spend_only | 2 | 0 | 0 | 0 | 0 | 0 | 2.200000000000001 |

### Prepared Model Totals

| Check | Value |
|---|---:|
| prepared_ads | 15 |
| lead_rows | 772 |
| distinct_leads | 772 |
| qualified_ab | 226 |
| lead_tier_a | 31 |
| lead_tier_b | 195 |
| spend_amount | 496.5600089999987 |
| spend_per_lead | 0.64321244689119 |
| spend_per_qualified_ab | 2.197168181415923 |
| qualified_rate_ab | 0.2927461139896373 |

---

## Prepared Model Constraints

| Constraint | Handling |
|---|---|
| Lead-side `ad_id` contains `ag:` prefix | Normalize with `REGEXP_REPLACE(ad_id, r'^ag:', '')` before alignment |
| `campaign_signal` exists only in `fct_spend` | Commercial classification is derived only for spend-side records and matched ads |
| Spend-only ads lack campaign/adset metadata | Preserve `spend_only` status and do not invent campaign/adset fields |
| Lead-only ads lack commercial spend | Preserve `lead_only` status and do not assign spend |
| `int_faro_lead_scoring` and `fct_lead_enriched` have equivalent June coverage | Use one lead source in the prepared model to avoid double counting |
| Raw Meta impressions/clicks are outside the approved source-table set for this revision | Leave impressions/clicks unavailable in this prepared model unless scope is explicitly expanded |
| Duplicate/test-record flags are not explicitly mapped | Preserve limitation from Discovery |

---

## Analytical Model Outputs

| Output | Status | Description |
|---|---|---|
| `ad_quality_spend_model` | Prepared | Ad-level model aligned by normalized `ad_id`, with lead quality, commercial spend and coverage status |
| `matched_ads` | Prepared subset | Ads with both lead quality and commercial spend |
| `lead_only_ads` | Prepared subset | Ads with lead quality but no matching commercial spend |
| `spend_only_ads` | Prepared subset | Commercial spend ads without matching lead quality records |

---

## Boundary Compliance

| Rule | Result | Evidence |
|---|---|---|
| Analytical preparation only | Pass | The artifact defines aggregation, normalization, alignment and validation rules |
| No reasoning | Pass | No business insight, hypothesis or conclusion is produced |
| No recommendation | Pass | No suggested action is formulated |
| No presentation logic | Pass | No report structure or executive narrative is produced |
| Limitation propagation | Pass | Discovery limitations are preserved as model constraints |
| Traceability | Pass | Sources, SQL, coverage states and validation totals are documented |

---

## Transition Status

| Target | Status | Reason |
|---|---|---|
| T-020 revision | Completed | Corrected preparation has been approved after review |
| T-021 Analytical Contract revision | Authorized | Requires formalization of the approved corrected Analytical Model |
| T-022 Evidence Set | Ready to start | Requires the corrected T-021 Analytical Contract as input |
| Reasoning and recommendations | Not authorized | Downstream phases require evidence and knowledge contracts first |

---

## Traceability

- [T-020 in docs/tasks.md](../tasks.md)
- [AUC-001 Source Table Review](auc-001-source-table-review.md)
- [AUC-001 Context Definition](auc-001-context-definition.md)
- [AUC-001 Data Contract](auc-001-data-contract.md)
- [AUC-001 Evidence Acquisition](auc-001-evidence-acquisition.md)
- [AUC-001 Discovery Contract](auc-001-discovery-contract.md)
- [SPEC-001 Analytical Lifecycle](../../specs/spec-001-analytical-lifecycle.md)
- [SPEC-002 Component Boundaries](../../specs/spec-002-component-boundaries.md)
- [AUC-001 Meta Lead Quality Analysis](../../analytical_use_cases/meta_lead_quality_analysis.md)
- [Meta Lead Quality Analysis Skill](../../.github/skills/meta-lead-quality-analysis/SKILL.md)

---

## Completion Statement

T-020 revision is complete and approved.

The corrected analytical preparation defines `ad_quality_spend_model` at normalized `ad_id` grain, using `fct_lead_enriched` for lead quality and `fct_spend` for commercial spend.

T-021 may now formalize this corrected Analytical Model.