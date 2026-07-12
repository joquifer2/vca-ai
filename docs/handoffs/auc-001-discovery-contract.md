# AUC-001 Discovery Contract

## Metadata

| Field | Value |
|---|---|
| Contract ID | VCA-AUC-001-DISC-001 |
| Contract Name | AUC-001 Discovery Contract |
| Contract Category | Discovery Contract |
| Analytical Use Case | AUC-001 - Meta Lead Quality Analysis |
| Related Base Contract | VCA-DISC-001 |
| Status | Revised after source-table review |
| Version | 1.1.0 |
| Last Updated | 2026-07-12 |
| Owner | Equipo VCA |
| Backing Task | T-019 revision |

---

## Purpose

Formalizar el Discovery Model corregido de AUC-001 para la ejecucion de junio de 2026 antes de rehacer la preparacion analitica.

Este contract reemplaza la seleccion anterior de tablas como base de Discovery para T-020.

Este contract no prepara datos.

Este contract no produce evidencia analitica.

Este contract no interpreta resultados ni formula recomendaciones.

---

## Backing Task

| Field | Value |
|---|---|
| Task ID | T-019 |
| Task | Implementar el Discovery Contract del caso AUC-001 |
| Specifications | SPEC-001 Analytical Lifecycle; SPEC-002 Component Boundaries; SPEC-004 Transversal Contracts |
| Skill | meta-lead-quality-analysis |
| Acceptance Criterion | Existe un Discovery Contract que formaliza entidades, dimensiones, metricas y limitaciones observadas antes de la preparacion |
| Revision trigger | User confirmed source tables before T-022 |

---

## Source Table Decision

The following tables are the approved Discovery basis for AUC-001 after corrective review:

| Table | Role | Status |
|---|---|---|
| `datamart-vca-494114.intermediate.int_faro_lead_scoring` | Lead-level FARO scoring, form answers, campaign/adset/ad references and `lead_tier` | Approved source table |
| `datamart-vca-494114.marts.fct_lead_enriched` | Mart-level enriched lead fact with FARO scores, campaign/adset/ad references, concept/version/angle and offline candidate fields | Approved source table |
| `datamart-vca-494114.marts.fct_spend` | Spend fact by `spend_period`, `ad_id`, concept/version/angle, account and `campaign_signal` | Approved source table |

Tables used previously as the main preparation base, especially `fct_performance_daily`, are no longer the primary Discovery basis for this AUC-001 path.

---

## Discovery Scope

| Field | Value |
|---|---|
| execution_id | VCA-AUC-001-EXEC-2026-06 |
| period | 2026-06-01 to 2026-06-30 |
| channel | Meta Ads / Meta Lead Ads |
| campaign_scope | All Meta Lead Ads campaigns, ad sets and creatives with spend or leads during the period |
| campaign_signal_filter | `campaign_signal = COMMERCIAL` where exposed, currently in `fct_spend` |
| lead_quality_definition | Qualified Lead according to FARO, equivalent to Lead Tier A or B |
| geographic_filter | No additional geographic filter |
| source_table_review | [AUC-001 Source Table Review](auc-001-source-table-review.md) |

---

## Source Coverage Checks

| Source | Total Rows | June 2026 Rows | June Main Checks |
|---|---:|---:|---|
| `intermediate.int_faro_lead_scoring` | 1432 | 772 | 772 distinct leads; 226 Lead Tier A/B |
| `marts.fct_lead_enriched` | 1432 | 772 | 772 distinct leads; 226 Lead Tier A/B; 0 invalid lead IDs |
| `marts.fct_spend` | 7333 | 4304 | 807.0600089999803 total spend; 496.5600089999888 commercial spend |

---

## Relevant Entities

| Entity | Source | Status | Notes |
|---|---|---|---|
| Lead | `int_faro_lead_scoring`; `fct_lead_enriched` | Verified | Lead-level records keyed by `lead_id` |
| Campaign | `int_faro_lead_scoring`; `fct_lead_enriched` | Verified for leads | `campaign_id`, `campaign_name`; 2 campaigns in June lead data |
| Ad set | `int_faro_lead_scoring`; `fct_lead_enriched` | Verified for leads | `adset_id`, `adset_name`; 2 ad sets in June lead data |
| Ad / creative reference | `int_faro_lead_scoring`; `fct_lead_enriched`; `fct_spend` | Verified as ad reference | `ad_id`, `ad_name`; 13 ads in June lead data; 10 commercial-spend ads |
| FARO lead quality | `int_faro_lead_scoring`; `fct_lead_enriched` | Verified | `lead_tier`, `lead_priority`, score fields and mapping flags |
| Spend | `fct_spend` | Verified | `spend_amount`, `currency_code`, `campaign_signal`, `account_id` |
| Concept | `fct_lead_enriched`; `fct_spend` | Verified | 3 concepts observed in June leads and commercial spend |
| Version | `fct_lead_enriched`; `fct_spend` | Verified | Available as `version_id` |
| Angle | `fct_lead_enriched`; `fct_spend` | Verified | 8 angles observed in June leads and commercial spend |
| Campaign signal | `fct_spend` | Verified for spend | COMMERCIAL/ACTIVATION/ATTENTION exposed in June spend |

---

## Relevant Dimensions

| Dimension | Source | Status | Notes |
|---|---|---|---|
| Lead date | `int_faro_lead_scoring.lead_date`; `fct_lead_enriched.day` | Verified | Used for lead-period filtering |
| Spend period | `fct_spend.spend_period` | Verified | Used for spend-period filtering |
| Campaign | Lead tables | Verified for lead quality | Not exposed directly in `fct_spend` |
| Ad set | Lead tables | Verified for lead quality | Not exposed directly in `fct_spend` |
| Ad / creative reference | Lead tables and `fct_spend` | Verified structurally | Relationship across lead/spend requires preparation validation |
| Concept / version / angle | `fct_lead_enriched`; `fct_spend` | Verified structurally | Relationship across lead/spend requires preparation validation |
| Lead tier | Lead tables | Verified | Lead Tier A/B defines qualified lead for this execution |
| Campaign signal | `fct_spend` | Verified for spend | Commercial filter applies directly to spend only |
| Geography | Not observed in selected tables | Not included | No geographic filter requested |

---

## Relevant Metrics Observed

### Lead Quality Space

| Metric | Value | Source |
|---|---:|---|
| June lead rows | 772 | `fct_lead_enriched`; `int_faro_lead_scoring` |
| June distinct leads | 772 | `fct_lead_enriched`; `int_faro_lead_scoring` |
| Invalid lead ID rows | 0 | `fct_lead_enriched` |
| Qualified leads A/B | 226 | `lead_tier IN ('A','B')` |
| Campaigns with leads | 2 | `fct_lead_enriched` |
| Ad sets with leads | 2 | `fct_lead_enriched` |
| Ads with leads | 13 | `fct_lead_enriched` |
| Concepts with leads | 3 | `fct_lead_enriched` |
| Angles with leads | 8 | `fct_lead_enriched` |

### Spend Space

| campaign_signal | spend_rows | spend_amount | ads | concepts | angles |
|---|---:|---:|---:|---:|---:|
| ACTIVATION | 72 | 153.79999999999998 | 6 | 1 | 3 |
| ATTENTION | 73 | 156.7 | 7 | 2 | 6 |
| COMMERCIAL | 4159 | 496.5600089999888 | 10 | 3 | 8 |

---

## Relationships

| Relationship | Status | Basis | Preparation Constraint |
|---|---|---|---|
| `int_faro_lead_scoring` -> `fct_lead_enriched` | Verified equivalent coverage for June | Both expose 772 June leads and 226 A/B leads | T-020 may choose mart or intermediate as lead-quality base, but must avoid double counting |
| Lead -> campaign/adset/ad | Verified within lead tables | Lead tables expose campaign/adset/ad IDs and names | Valid for lead-quality reporting |
| Lead -> FARO score and tier | Verified within lead tables | `lead_tier`, `lead_priority`, score fields and mapping flags | Valid for lead-quality reporting |
| Spend -> campaign_signal | Verified within `fct_spend` | `campaign_signal` and commercial spend values are exposed | Valid for spend filtering |
| Spend -> ad/concept/version/angle | Verified within `fct_spend` | Fields exposed structurally | Valid for spend reporting |
| Lead quality -> spend | Validated by normalized `ad_id` with partial coverage | Literal `ad_id` mismatch is caused by `ag:` prefix in lead tables; after normalization, 8 of 10 commercial-spend ads match lead data | T-020 must normalize lead `ad_id` with `REGEXP_REPLACE(ad_id, r'^ag:', '')` before alignment |
| Campaign/adset -> spend | UNKNOWN | `fct_spend` does not expose campaign/adset fields | Requires mapping or separate reporting |
| Campaign signal -> lead | UNKNOWN | Lead tables do not expose `campaign_signal` directly | Commercial lead quality must not be asserted as direct lead-level field |

---


### Ad ID Alignment Validation

| Check | Value |
|---|---:|
| commercial_spend_ads | 10 |
| spend_ads_matching_leads_after_ad_id_normalization | 8 |
| spend_ads_without_leads_after_ad_id_normalization | 2 |
| commercial_spend | 496.5600089999987 |
| spend_matching_leads | 494.3600089999987 |
| spend_without_leads | 2.200000000000001 |
| lead_ads | 13 |
| lead_ads_matching_commercial_spend | 8 |
| lead_ads_without_commercial_spend | 5 |
| lead_rows_matching_spend | 680 |
| lead_rows_without_commercial_spend | 92 |
| qualified_ab_matching_spend | 191 |
| qualified_ab_without_commercial_spend | 35 |

Normalization rule: lead-table `ad_id` values may include the `ag:` prefix. T-020 must derive `ad_id`_norm = REGEXP_REPLACE(ad_id, r'^ag:', '')` before joining to `fct_spend.ad_id`.
---

## Granularity Statement

| Source | Observed Grain | Effect |
|---|---|---|
| `int_faro_lead_scoring` | Lead-level scoring grain, with campaign/adset/ad/form and FARO question fields | Best source for detailed lead quality and campaign/adset/ad lead attribution |
| `fct_lead_enriched` | Lead-level mart grain, enriched with concept/version/angle, FARO scoring and offline candidate fields | Best mart source for lead quality and creative/concept dimensions |
| `fct_spend` | Spend-period grain by ad/concept/version/angle/account/campaign_signal | Best source for spend and commercial investment |

The validated AUC-001 alignment key between lead quality and spend is normalized `ad_id`.

The corrected Discovery supports a primary ad-level preparation model using normalized `ad_id` as the alignment key. The model must preserve three coverage states: `matched`, `lead_only` and `spend_only`.

---

## Excluded Or Deferred Elements

| Element | Status | Reason |
|---|---|---|
| `fct_performance_daily` as primary model base | Deferred | No longer selected as the main source path after user-confirmed table correction |
| Direct ad-level quality-spend model | Ready with constraints | Use normalized `ad_id` and preserve `matched`, `lead_only` and `spend_only` coverage states |
| Campaign/adset spend attribution | UNKNOWN | `fct_spend` lacks campaign/adset fields |
| Raw Meta ad-insight metrics | Deferred | AUC-001 source-table correction identified `fct_spend` and lead-scoring/enriched tables as suitable tables; raw metrics require separate authorization if needed |
| Test and duplicate exclusion fields | Partially verified | Valid lead IDs are verified; explicit test/duplicate flags remain unmapped in selected tables |

---

## Limitations

| Limitation | Impact | Handling |
|---|---|---|
| Lead tables do not expose `campaign_signal` | Commercial quality cannot be asserted directly at lead level | Keep as UNKNOWN unless T-020 validates an authorized mapping |
| `fct_spend` does not expose campaign/adset fields | Spend cannot be directly reported by campaign/adset from this table alone | Prepare spend by exposed fields or request/validate mapping |
| Literal `ad_id` values differ between lead and spend tables | Direct literal join returns zero matches | T-020 must normalize lead `ad_id` by removing the `ag:` prefix before joining to `fct_spend.ad_id` |
| Raw Meta impressions/clicks are outside the confirmed suitable table set | AUC-001 evidence families for clicks/impressions may remain incomplete | Mark as limitation unless source scope is expanded |
| Explicit duplicate/test filters are not mapped | Full exclusion policy cannot be validated from selected tables alone | Preserve as limitation |

---

## Validation Rules Applied

| Rule | Result | Evidence |
|---|---|---|
| Context dependency | Pass | AUC-001 execution context is defined |
| Data dependency | Pass with revision | Source-table review corrected the source-table basis |
| No preparation | Pass | This contract does not join, normalize or consolidate tables |
| No evidence creation | Pass | Metrics are exposure checks for Discovery, not Evidence Set findings |
| No interpretation | Pass | No insight, conclusion or recommendation is made |
| Limitation propagation | Pass | Relationship gaps are explicit for T-020 |
| Unknown explicitness | Pass | Unvalidated joins and campaign_signal-to-lead relationship are marked UNKNOWN |

---

## Transition Status

| Target | Status | Reason |
|---|---|---|
| T-019 revision | Completed | Discovery source tables, entities, dimensions, metrics, relationships and limitations are corrected |
| T-020 revision | Ready with constraints | Preparation must use normalized `ad_id` as the AUC-001 alignment key and preserve unmatched lead-only/spend-only ads |
| T-021 revision | Not authorized | Requires corrected T-020 first |
| T-022 Evidence Set | Blocked | Requires corrected T-020 and T-021 |

---

## Traceability

- [T-019 in docs/tasks.md](../tasks.md)
- [AUC-001 Source Table Review](auc-001-source-table-review.md)
- [AUC-001 Context Definition](auc-001-context-definition.md)
- [AUC-001 Execution Context](auc-001-execution-context.md)
- [AUC-001 Data Contract](auc-001-data-contract.md)
- [AUC-001 Evidence Acquisition](auc-001-evidence-acquisition.md)
- [VCA-DISC-001 Base Discovery Contract](../contracts/discovery.contract.md)
- [SPEC-001 Analytical Lifecycle](../../specs/spec-001-analytical-lifecycle.md)
- [SPEC-002 Component Boundaries](../../specs/spec-002-component-boundaries.md)
- [SPEC-004 Transversal Contracts](../../specs/spec-004-transversal-contracts.md)
- [AUC-001 Meta Lead Quality Analysis](../../analytical_use_cases/meta_lead_quality_analysis.md)
- [Meta Lead Quality Analysis Skill](../../.github/skills/meta-lead-quality-analysis/SKILL.md)

---

## Completion Statement

T-019 revision is complete.

The corrected Discovery Contract uses `fct_spend`, `int_faro_lead_scoring` and `fct_lead_enriched` as the approved source-table basis for AUC-001.

T-020 must now be redone using this Discovery and must use normalized `ad_id` as the AUC-001 alignment key between lead quality and spend.