# AUC-001 Evidence Set

## Metadata

| Field | Value |
|---|---|
| Artifact ID | VCA-AUC-001-EVD-SET-001 |
| Artifact Type | Evidence Set |
| Analytical Use Case | AUC-001 - Meta Lead Quality Analysis |
| Analytical Model ID | VCA-AUC-001-AM-001 |
| Analytical Contract ID | VCA-AUC-001-ANL-001 |
| Status | Documented |
| Version | 1.0.0 |
| Last Updated | 2026-07-12 |
| Owner | Equipo VCA |
| Backing Task | T-022 |

---

## Purpose

Registrar los hallazgos observables producidos desde el Analytical Model corregido de AUC-001.

Este Evidence Set contiene evidencia observable y evidencia derivada desde `ad_quality_spend_model`.

Este artefacto no interpreta causas.

Este artefacto no produce insights, hipotesis, conclusiones ni recomendaciones.

---

## Backing Task

| Field | Value |
|---|---|
| Task ID | T-022 |
| Task | Implementar el Evidence Set de AUC-001 |
| Specifications | SPEC-001 Analytical Lifecycle; SPEC-002 Component Boundaries |
| Skill | meta-lead-quality-analysis |
| Acceptance Criterion | Existe un Evidence Set con hallazgos observables separados de interpretacion y trazados a su modelo analitico |
| Implementation basis | T-021 corrected Analytical Contract |

---

## Evidence Scope

| Field | Value |
|---|---|
| execution_id | VCA-AUC-001-EXEC-2026-06 |
| period | 2026-06-01 to 2026-06-30 |
| channel | Meta Ads / Meta Lead Ads |
| source_model | `ad_quality_spend_model` |
| model_grain | normalized `ad_id` (`ad_id_norm`) |
| source_tables | `marts.fct_lead_enriched`; `intermediate.int_faro_lead_scoring`; `marts.fct_spend` |
| lead_quality_rule | Qualified Lead = `lead_tier IN ('A', 'B')` |
| spend_filter | `campaign_signal = 'COMMERCIAL'` |
| coverage_states | `matched`; `lead_only`; `spend_only` |

---

## Evidence Queries

The Evidence Set uses the model defined by [AUC-001 Analytical Contract](auc-001-analytical-contract.md):

1. Aggregate `fct_lead_enriched` by normalized `ad_id` for leads and FARO Lead Tier A/B.
2. Aggregate `fct_spend` by `ad_id` for June 2026 commercial spend.
3. Full outer join both aggregates by normalized `ad_id`.
4. Classify rows as `matched`, `lead_only` or `spend_only`.
5. Produce observable summaries by coverage state, ad reference and lead-side campaign/adset metadata.

---

## Observable Finding Set

### EVD-001 - Model Coverage By Status

| coverage_status | ad_count | lead_rows | distinct_leads | qualified_ab | lead_tier_a | lead_tier_b | spend_amount | spend_per_lead | spend_per_qualified_ab | qualified_rate_ab |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| lead_only | 5 | 92 | 92 | 35 | 9 | 26 | 0.0 | 0.0 | 0.0 | 0.3804347826086957 |
| matched | 8 | 680 | 680 | 191 | 22 | 169 | 494.3600089999987 | 0.7270000132352922 | 2.5882722984293123 | 0.28088235294117647 |
| spend_only | 2 | 0 | 0 | 0 | 0 | 0 | 2.200000000000001 | UNKNOWN | UNKNOWN | UNKNOWN |

Traceability: `coverage_status`, `lead_rows`, `distinct_leads`, `qualified_ab`, `lead_tier_a`, `lead_tier_b`, `spend_amount`, `spend_per_lead`, `spend_per_qualified_ab`, `qualified_rate_ab` from `VCA-AUC-001-AM-001`.

### EVD-002 - Prepared Model Totals

| Metric | Value |
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

Traceability: prepared totals from `ad_quality_spend_model`.

### EVD-003 - Ad Reference Evidence

| ad_id_norm | ad_name | coverage_status | campaign_name | adset_name | lead_rows | distinct_leads | qualified_ab | lead_tier_a | lead_tier_b | spend_amount | spend_per_lead | spend_per_qualified_ab | qualified_rate_ab |
|---|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 120245828603090721 | ViajeSinEstres_AlivioEmocional_ViajeSinEstres_Reel_v1 | matched | [META]_[CLP]_[CAPTACION]_[ABO] | [PR]_[NATIVE FORM]_[AVG+]_[ISLA] | 519 | 519 | 152 | 20 | 132 | 374.79000799999875 | 0.7221387437379552 | 2.4657237368420972 | 0.2928709055876686 |
| 120251257513780721 | ExperienciasUnicas_ViajesConAlma_BoriWine2026_Reel_v1 | matched | [META]_[CLP]_[CAPTACION]_[ABO] | [PR]_[NATIVE FORM]_[AVG+]_[ISLA] | 67 | 67 | 8 | 0 | 8 | 50.01000000000001 | 0.7464179104477614 | 6.2512500000000015 | 0.11940298507462686 |
| 120245829545180721 | ViajaComoInvitado_Identidad_ViajarComoLocal_Reel_v1 | matched | [META]_[CLP]_[CAPTACION]_[ABO] | [PR]_[NATIVE FORM]_[AVG+]_[ISLA] | 50 | 50 | 14 | 1 | 13 | 37.78000000000006 | 0.7556000000000012 | 2.698571428571433 | 0.28 |
| 120245407987440721 | FiltroBilletes_EscasezReal_3TipsDeViaje_Reel_v1 | matched | [META]_[CLP]_[CAPTACION]_[ABO] | [PR]_[NATIVE FORM]_[AVG+]_[ISLA] | 13 | 13 | 6 | 1 | 5 | 13.139999999999961 | 1.0107692307692278 | 2.1899999999999937 | 0.46153846153846156 |
| 120245407987450721 | FiltroBilletes_AutoSegmentacion_PrimeraVez_Reel_v1 | matched | [META]_[CLP]_[CAPTACION]_[ABO] | [PR]_[NATIVE FORM]_[AVG+]_[ISLA] | 9 | 9 | 2 | 0 | 2 | 5.929999999999973 | 0.6588888888888859 | 2.9649999999999865 | 0.2222222222222222 |
| 120251254823190721 | ExperienciasUnicas_OportunidadIrrepetible_EclipseSolar2026_Reel_v1 | matched | [META]_[CLP]_[CAPTACION]_[ABO] | [PR]_[NATIVE FORM]_[AVG+]_[ISLA] | 5 | 5 | 2 | 0 | 2 | 4.859999999999992 | 0.9719999999999984 | 2.429999999999996 | 0.4 |
| 120245829746630721 | ViajaComoInvitado_Estatus_ExperienciaCalidad_Reel_v1 | matched | [META]_[CLP]_[CAPTACION]_[ABO] | [PR]_[NATIVE FORM]_[AVG+]_[ISLA] | 8 | 8 | 4 | 0 | 4 | 4.350000999999986 | 0.5437501249999982 | 1.0875002499999964 | 0.5 |
| 120245829115590721 | ViajeSinEstres_PrevencionDeRiesgo_ErroresViaje_Reel_v1 | matched | [META]_[CLP]_[CAPTACION]_[ABO] | [PR]_[NATIVE FORM]_[AVG+]_[ISLA] | 9 | 9 | 3 | 0 | 3 | 3.4999999999999885 | 0.3888888888888876 | 1.1666666666666627 | 0.3333333333333333 |
| 120251249759480721 | ExperienciasUnicas_LugaresSorprendentes_CamposLavanda_Reel_v1 | spend_only | UNKNOWN | UNKNOWN | 0 | 0 | 0 | 0 | 0 | 1.2000000000000006 | UNKNOWN | UNKNOWN | UNKNOWN |
| 120251252180570721 | ExperienciasUnicas_ErroresPlanificacion_EclipseSolar2026_Reel_v1 | spend_only | UNKNOWN | UNKNOWN | 0 | 0 | 0 | 0 | 0 | 1.0000000000000002 | UNKNOWN | UNKNOWN | UNKNOWN |
| 120247352473020721 | FiltroBilletes_EscasezReal_3TipsDeViaje_Reel_v1 | lead_only | [META]_[CLP]_[RTG]_[CBO] | [RTG]_[NATIVE FORM]_[INTERACCIONES + 50% VIDEO]_[DIASPORA] | 71 | 71 | 25 | 8 | 17 | 0.0 | 0.0 | 0.0 | 0.352112676056338 |
| 120245823087500721 | MasCaroPorqueMejor_CalidadVsCantidad_ViajesConCalidad_Reel_v1 | lead_only | [META]_[CLP]_[RTG]_[CBO] | [RTG]_[NATIVE FORM]_[INTERACCIONES + 50% VIDEO]_[DIASPORA] | 16 | 16 | 8 | 1 | 7 | 0.0 | 0.0 | 0.0 | 0.5 |
| 120245823087510721 | FiltroBilletes_AutoSegmentacion_PrimeraVez_Reel_v1 | lead_only | [META]_[CLP]_[RTG]_[CBO] | [RTG]_[NATIVE FORM]_[INTERACCIONES + 50% VIDEO]_[DIASPORA] | 2 | 2 | 0 | 0 | 0 | 0.0 | 0.0 | UNKNOWN | 0.0 |
| 120251255543170721 | ExperienciasUnicas_OportunidadIrrepetible_EclipseSolar2026_Reel_v1 | lead_only | [META]_[CLP]_[RTG]_[CBO] | [RTG]_[NATIVE FORM]_[INTERACCIONES + 50% VIDEO]_[DIASPORA] | 2 | 2 | 2 | 0 | 2 | 0.0 | 0.0 | 0.0 | 1.0 |
| 120251255543160721 | ExperienciasUnicas_LugaresSorprendentes_CamposLavanda_Reel_v1 | lead_only | [META]_[CLP]_[RTG]_[CBO] | [RTG]_[NATIVE FORM]_[INTERACCIONES + 50% VIDEO]_[DIASPORA] | 1 | 1 | 0 | 0 | 0 | 0.0 | 0.0 | UNKNOWN | 0.0 |

Traceability: ad reference rows from `ad_quality_spend_model`; campaign/adset values are lead-side metadata and remain UNKNOWN for spend-only rows.

### EVD-004 - Campaign And Adset Evidence Where Available

| campaign_name | adset_name | coverage_status | ad_count | lead_rows | distinct_leads | qualified_ab | lead_tier_a | lead_tier_b | spend_amount | qualified_rate_ab |
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| UNKNOWN | UNKNOWN | spend_only | 2 | 0 | 0 | 0 | 0 | 0 | 2.200000000000001 | UNKNOWN |
| [META]_[CLP]_[CAPTACION]_[ABO] | [PR]_[NATIVE FORM]_[AVG+]_[ISLA] | matched | 8 | 680 | 680 | 191 | 22 | 169 | 494.3600089999987 | 0.28088235294117647 |
| [META]_[CLP]_[RTG]_[CBO] | [RTG]_[NATIVE FORM]_[INTERACCIONES + 50% VIDEO]_[DIASPORA] | lead_only | 5 | 92 | 92 | 35 | 9 | 26 | 0.0 | 0.3804347826086957 |

Traceability: aggregation from `ad_quality_spend_model`; campaign/adset spend attribution is only available where lead-side metadata exists.

---

## Derived Evidence Boundaries

| Boundary | Handling |
|---|---|
| Cost and quality ratios | Reported as derived evidence only; no performance conclusion is made |
| Highest or lowest values | Not labelled as better, worse, opportunity or risk in this artifact |
| Campaign/adset rows | Shown only where the model exposes metadata; spend-only rows remain UNKNOWN |
| Creative scope | Uses ad reference (`ad_id_norm`, `ad_name`), not creative asset metadata |
| Spend-only rows | Cost ratios and quality rates are UNKNOWN because denominator fields are zero or absent |
| Lead-only rows | Spend fields are zero because no matching commercial spend exists in the approved model |

---

## Evidence Limitations

| Limitation | Evidence Impact |
|---|---|
| Lead tables do not expose `campaign_signal` | Evidence cannot state that lead rows themselves are commercial; commercial filter applies to spend-side records |
| `fct_spend` does not expose campaign/adset fields | Spend-only rows cannot be attributed to campaign/adset in this Evidence Set |
| Creative asset metadata is not available | Evidence is by ad reference, not by media, format or creative asset attributes |
| Raw Meta impressions/clicks are outside the corrected approved source set | Evidence Set does not include impressions, clicks or CTR |
| Duplicate/test-record fields are not explicitly mapped | Evidence preserves the valid-lead-ID check but cannot fully evidence duplicate/test exclusion |
| `qualified_ab` is derived from Lead Tier A/B | Evidence depends on the approved execution quality rule, not on a published `qualified_leads` column |

---

## Excluded Interpretations

The following are explicitly outside T-022:

- why one ad, campaign or ad set has a given value;
- whether an ad, campaign or ad set is good, bad, efficient or inefficient;
- business conclusions;
- optimization opportunities;
- budget recommendations;
- prioritization of actions.

---

## Boundary Compliance

| Rule | Result | Evidence |
|---|---|---|
| Analytical dependency | Pass | Evidence Set consumes `VCA-AUC-001-ANL-001` |
| Observable only | Pass | Tables contain model-derived counts, sums and ratios |
| No reasoning | Pass | No cause, insight, conclusion or hypothesis is stated |
| No recommendation | Pass | No action is suggested |
| Traceability | Pass | Each evidence block links to `ad_quality_spend_model` fields |
| Limitation propagation | Pass | Analytical Contract limitations are preserved |
| Unknown explicitness | Pass | Unavailable fields and invalid ratios are marked UNKNOWN |

---

## Transition Status

| Target | Status | Reason |
|---|---|---|
| T-022 Evidence Set | Completed | Observable evidence has been produced from the corrected Analytical Contract |
| T-023 Evidence Contract | Ready to start | Evidence can now be formalized contractually |
| Reasoning and recommendations | Not authorized | Require T-023 Evidence Contract and downstream phases first |

---

## Traceability

- [T-022 in docs/tasks.md](../tasks.md)
- [AUC-001 Analytical Contract](auc-001-analytical-contract.md)
- [AUC-001 Analytical Preparation](auc-001-analytical-preparation.md)
- [AUC-001 Discovery Contract](auc-001-discovery-contract.md)
- [AUC-001 Data Contract](auc-001-data-contract.md)
- [AUC-001 Execution Context](auc-001-execution-context.md)
- [SPEC-001 Analytical Lifecycle](../../specs/spec-001-analytical-lifecycle.md)
- [SPEC-002 Component Boundaries](../../specs/spec-002-component-boundaries.md)
- [AUC-001 Meta Lead Quality Analysis](../../analytical_use_cases/meta_lead_quality_analysis.md)
- [Meta Lead Quality Analysis Skill](../../.github/skills/meta-lead-quality-analysis/SKILL.md)

---

## Completion Statement

T-022 is complete.

The Evidence Set contains observable evidence from `ad_quality_spend_model` at normalized `ad_id` grain, preserving coverage states, source limitations and UNKNOWN values.

T-023 may now formalize this Evidence Set in an Evidence Contract.