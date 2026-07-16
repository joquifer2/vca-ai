# AUC-001 Analytical Contract

## Metadata

| Field | Value |
|---|---|
| Contract ID | VCA-AUC-001-ANL-001 |
| Contract Name | AUC-001 Analytical Contract |
| Contract Category | Analytical Contract |
| Analytical Use Case | AUC-001 - Meta Lead Quality Analysis |
| Related Base Contract | VCA-ANL-001 |
| Analytical Model ID | VCA-AUC-001-AM-001 |
| Status | Documented |
| Version | 2.0.0 |
| Last Updated | 2026-07-12 |
| Owner | Equipo VCA |
| Backing Task | T-021 |

---

## Purpose

Formalizar el Analytical Model corregido de AUC-001 despues de la aprobacion de T-020.

Este contract describe el modelo preparado, su grano, entidades, dimensiones, metricas, transformaciones, validaciones y limitaciones.

Este contract no produce hallazgos observables.

Este contract no interpreta resultados.

Este contract no formula conclusiones ni recomendaciones.

---

## Backing Task

| Field | Value |
|---|---|
| Task ID | T-021 |
| Task | Implementar el Analytical Contract del caso AUC-001 |
| Specifications | SPEC-001 Analytical Lifecycle; SPEC-002 Component Boundaries; SPEC-004 Transversal Contracts |
| Skill | meta-lead-quality-analysis |
| Acceptance Criterion | Existe un Analytical Contract que formaliza el modelo preparado y sus transformaciones relevantes para analisis |
| Implementation basis | Approved T-020 corrected Analytical Preparation |

---

## Producer And Consumer

| Role | Value |
|---|---|
| Producer | Analytical Layer / Phase 2 Preparation |
| Consumer | Analytical Layer / Phase 3 Analysis |
| Framework role | Validate readiness before Evidence Set production |
| Downstream artifact | T-022 Evidence Set |

---

## Inputs

| Input | Artifact | Status |
|---|---|---|
| Context Definition | [AUC-001 Context Definition](auc-001-context-definition.md) | Validated |
| Analysis Request | [AUC-001 Analysis Request](auc-001-analysis-request.md) | Validated |
| Execution Context | [AUC-001 Execution Context](auc-001-execution-context.md) | Validated |
| Data Contract | [AUC-001 Data Contract](auc-001-data-contract.md) | Documented with verified exposure |
| Evidence Acquisition | [AUC-001 Evidence Acquisition](auc-001-evidence-acquisition.md) | Completed with limitations |
| Source Table Review | [AUC-001 Source Table Review](auc-001-source-table-review.md) | Resolved for T-019/T-020/T-021 |
| Discovery Contract | [AUC-001 Discovery Contract](auc-001-discovery-contract.md) | Completed after source-table correction |
| Analytical Preparation | [AUC-001 Analytical Preparation](auc-001-analytical-preparation.md) | Approved |

---

## Analytical Model Declaration

| Field | Value |
|---|---|
| analytical_model_id | VCA-AUC-001-AM-001 |
| analytical_model_name | `ad_quality_spend_model` |
| analytical_scope | AUC-001 June 2026 Meta Lead Ads quality and commercial spend preparation |
| period | 2026-06-01 to 2026-06-30 |
| channel | Meta Ads / Meta Lead Ads |
| model_grain | normalized `ad_id` (`ad_id_norm`) |
| source_tables | `marts.fct_lead_enriched`; `intermediate.int_faro_lead_scoring`; `marts.fct_spend` |
| primary_lead_source | `marts.fct_lead_enriched` |
| lead_validation_source | `intermediate.int_faro_lead_scoring` |
| primary_spend_source | `marts.fct_spend` |
| quality_definition | Qualified Lead = Lead Tier A or B |
| commercial_spend_filter | `campaign_signal = 'COMMERCIAL'` |
| coverage_states | `matched`; `lead_only`; `spend_only` |

---

## Included Entities

| Entity | Contract Status | Source |
|---|---|---|
| Lead | Included | `fct_lead_enriched` |
| FARO lead quality | Included | `fct_lead_enriched`; validated against `int_faro_lead_scoring` |
| Ad / creative reference | Included as ad reference | `fct_lead_enriched`; `fct_spend` |
| Campaign | Included where lead-side metadata exists | `fct_lead_enriched` |
| Ad set | Included where lead-side metadata exists | `fct_lead_enriched` |
| Spend | Included | `fct_spend` |
| Creative asset metadata | Not included | Not exposed in approved source tables |
| Raw Meta impressions/clicks | Not included | Outside approved source-table set for this corrected model |

---

## Included Dimensions

| Dimension | Field | Handling |
|---|---|---|
| Normalized ad identifier | `ad_id_norm` | Primary model grain |
| Ad / creative label | `ad_name` | Lead-side value preferred; spend-side fallback for spend-only ads |
| Campaign identifier | `campaign_id` | Present for matched and lead-only ads when available |
| Campaign name | `campaign_name` | Present for matched and lead-only ads when available |
| Ad set identifier | `adset_id` | Present for matched and lead-only ads when available |
| Ad set name | `adset_name` | Present for matched and lead-only ads when available |
| Coverage state | `coverage_status` | `matched`, `lead_only` or `spend_only` |

---

## Included Metrics

| Metric | Definition | Status |
|---|---|---|
| `lead_rows` | Count lead rows by `ad_id_norm` | Included |
| `distinct_leads` | Count distinct `lead_id` by `ad_id_norm` | Included |
| `qualified_ab` | Count leads where `lead_tier IN ('A', 'B')` | Included as derived canonical prepared measure for this source set |
| `lead_tier_a` | Count leads where `lead_tier = 'A'` | Included |
| `lead_tier_b` | Count leads where `lead_tier = 'B'` | Included |
| `spend_amount` | Sum commercial spend by `ad_id` | Included |
| `spend_rows` | Count commercial spend records by `ad_id` | Included |
| `spend_per_lead` | `SAFE_DIVIDE(spend_amount, NULLIF(lead_rows, 0))` | Included as prepared metric |
| `spend_per_qualified_ab` | `SAFE_DIVIDE(spend_amount, NULLIF(qualified_ab, 0))` | Included as prepared metric |
| `qualified_rate_ab` | `SAFE_DIVIDE(qualified_ab, NULLIF(lead_rows, 0))` | Included as prepared metric |
| `qualified_leads` | Published metric field | Not available in approved source tables |

---

## Transformations

| Transformation | Rule | Rationale |
|---|---|---|
| Lead ad ID normalization | `REGEXP_REPLACE(ad_id, r'^ag:', '')` | Align lead-side IDs with `fct_spend.ad_id` |
| Lead aggregation | Aggregate `fct_lead_enriched` by `ad_id_norm` for June 2026 | Produce the ad-level lead quality side of the model |
| Spend aggregation | Aggregate `fct_spend` by `ad_id` for June 2026 where `campaign_signal = 'COMMERCIAL'` | Produce the commercial spend side of the model |
| Lead quality derivation | `qualified_ab = COUNTIF(lead_tier IN ('A', 'B'))` | Apply approved execution quality definition |
| Full outer alignment | Join lead and spend aggregates by `ad_id_norm` | Preserve matched, lead-only and spend-only ads |
| Coverage classification | Derive `coverage_status` from lead/spend presence | Make model coverage explicit for analysis |
| Ratio preparation | Use `SAFE_DIVIDE` and `NULLIF` for rates and cost ratios | Avoid invalid division in sparse coverage states |

---

## Validation Summary

### Source Equivalence Validation

| Validation | Value |
|---|---:|
| compared_ads between `fct_lead_enriched` and `int_faro_lead_scoring` | 13 |
| matching_ads | 13 |
| mismatching_ads | 0 |
| rows_enriched | 772 |
| rows_scoring | 772 |
| qualified_ab_enriched | 226 |
| qualified_ab_scoring | 226 |

### Model Coverage Validation

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

These values are model validation totals. They are not Evidence Set findings and must not be interpreted in this contract.

---

## Critical Fields

| Field | Status | Notes |
|---|---|---|
| contract_id | Present | `VCA-AUC-001-ANL-001` |
| context_contract_id | Present | `VCA-AUC-001-CTX-DEF-2026-06` |
| data_contract_id | Present | `VCA-AUC-001-DATA-001` |
| discovery_contract_id | Present | `VCA-AUC-001-DISC-001` |
| analytical_model_id | Present | `VCA-AUC-001-AM-001` |
| analytical_scope | Present | June 2026 Meta Lead Ads quality and commercial spend |
| included_entities | Present | Lead, FARO quality, ad reference, campaign/adset where available, spend |
| included_dimensions | Present | `ad_id_norm`, ad label, campaign/adset fields where available, coverage status |
| included_metrics | Present | Lead, quality, spend and prepared ratio metrics |
| transformations | Present | Normalization, aggregation, full outer alignment and prepared ratios |
| validation_summary | Present | Source equivalence, coverage states and prepared totals |
| limitations | Present | Propagated below |
| traceability_links | Present | Listed below |
| transition_status | Present | T-022 ready to start after T-021 completion |

---

## Limitations And Unknown Handling

| Limitation or Unknown | Handling For Analysis |
|---|---|
| Lead tables do not expose `campaign_signal` | Do not assert commercial status as a direct lead-level field |
| `fct_spend` does not expose campaign/adset fields | Campaign/adset spend attribution remains unavailable from this model |
| Spend-only ads lack campaign/adset metadata | Preserve `spend_only` status and null campaign/adset fields |
| Lead-only ads lack matched commercial spend | Preserve `lead_only` status and do not assign spend |
| Creative asset metadata is not available | Use `ad_id_norm` and `ad_name` only as ad/creative reference |
| Raw Meta impressions/clicks are outside approved corrected source set | Do not include click/impression findings in T-022 unless source scope is expanded |
| Duplicate/test-record flags are not explicitly mapped | Preserve as limitation; valid lead identifiers were checked but full exclusion policy is not fully mapped |
| Future published `qualified_leads` metric could appear in approved sources | Requires source-table decision or contract revision before replacing `qualified_ab` |

---

## Boundary Compliance

| Rule | Result | Evidence |
|---|---|---|
| Preparation formalization only | Pass | The contract formalizes the approved Analytical Model |
| No Evidence Set production | Pass | Validation totals are not framed as findings |
| No reasoning | Pass | No insight, hypothesis or conclusion is produced |
| No recommendation | Pass | No action or prioritization is formulated |
| Limitation propagation | Pass | Discovery and T-020 limitations are preserved |
| Contract metadata | Pass | SPEC-004 minimum metadata is present |

---

## Transition Status

| Target | Status | Reason |
|---|---|---|
| T-021 Analytical Contract | Completed | Corrected Analytical Model is formalized with transformations, validations and limitations |
| T-022 Evidence Set | Ready to start | Evidence production may use this contract while preserving documented constraints |
| Reasoning and recommendations | Not authorized | Require Evidence Set and downstream contracts first |

---

## Traceability

- [T-021 in docs/tasks.md](/docs/tasks.md)
- [AUC-001 Context Definition](auc-001-context-definition.md)
- [AUC-001 Analysis Request](auc-001-analysis-request.md)
- [AUC-001 Execution Context](auc-001-execution-context.md)
- [AUC-001 Data Contract](auc-001-data-contract.md)
- [AUC-001 Evidence Acquisition](auc-001-evidence-acquisition.md)
- [AUC-001 Source Table Review](auc-001-source-table-review.md)
- [AUC-001 Discovery Contract](auc-001-discovery-contract.md)
- [AUC-001 Analytical Preparation](auc-001-analytical-preparation.md)
- [VCA-ANL-001 Base Analytical Contract](/docs/contracts/analytical.contract.md)
- [SPEC-001 Analytical Lifecycle](/specs/spec-001-analytical-lifecycle.md)
- [SPEC-002 Component Boundaries](/specs/spec-002-component-boundaries.md)
- [SPEC-004 Transversal Contracts](/specs/spec-004-transversal-contracts.md)
- [AUC-001 Meta Lead Quality Analysis](/analytical_use_cases/meta_lead_quality_analysis.md)
- [Meta Lead Quality Analysis Skill](/.github/skills/meta-lead-quality-analysis/SKILL.md)

---

## Completion Statement

T-021 is complete.

The corrected Analytical Contract formalizes `ad_quality_spend_model` at normalized `ad_id` grain, using the approved source tables and preserving `matched`, `lead_only` and `spend_only` coverage states.

T-022 may now produce an Evidence Set from this contract, without introducing reasoning, conclusions or recommendations.