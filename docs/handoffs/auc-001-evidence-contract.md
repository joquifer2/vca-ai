# AUC-001 Evidence Contract

## Metadata

| Field | Value |
|---|---|
| Contract ID | VCA-AUC-001-EVD-001 |
| Contract Name | AUC-001 Evidence Contract |
| Contract Category | Evidence Contract |
| Analytical Use Case | AUC-001 - Meta Lead Quality Analysis |
| Related Base Contract | VCA-EVD-001 |
| Evidence Set ID | VCA-AUC-001-EVD-SET-001 |
| Analytical Contract ID | VCA-AUC-001-ANL-001 |
| Analytical Model ID | VCA-AUC-001-AM-001 |
| Status | Documented |
| Version | 1.0.0 |
| Last Updated | 2026-07-12 |
| Owner | Equipo VCA |
| Backing Task | T-023 |

---

## Purpose

Formalizar el Evidence Set de AUC-001 como handoff contractual entre la Analytical Layer y la Reasoning Layer.

Este contract estructura los hallazgos observables y la evidencia derivada producida desde `ad_quality_spend_model`.

Este contract no interpreta causas.

Este contract no produce insights, hipotesis, conclusiones ni recomendaciones.

---

## Backing Task

| Field | Value |
|---|---|
| Task ID | T-023 |
| Task | Implementar el Evidence Contract del caso AUC-001 |
| Specifications | SPEC-001 Analytical Lifecycle; SPEC-002 Component Boundaries; SPEC-004 Transversal Contracts |
| Skill | meta-lead-quality-analysis |
| Acceptance Criterion | Existe un Evidence Contract que formaliza los hallazgos observables y su trazabilidad al modelo analitico |
| Implementation basis | T-022 Evidence Set |

---

## Producer And Consumer

| Role | Value |
|---|---|
| Producer | Analytical Layer / Phase 3 Analysis |
| Consumer | Reasoning Layer / Phase 4 Reasoning |
| Framework role | Validate evidence readiness before reasoning |
| Downstream artifact | T-024 Reasoning Layer output |

---

## Inputs

| Input | Artifact | Status |
|---|---|---|
| Context Definition | [AUC-001 Context Definition](auc-001-context-definition.md) | Validated |
| Execution Context | [AUC-001 Execution Context](auc-001-execution-context.md) | Validated |
| Data Contract | [AUC-001 Data Contract](auc-001-data-contract.md) | Documented with verified exposure |
| Discovery Contract | [AUC-001 Discovery Contract](auc-001-discovery-contract.md) | Completed after source-table correction |
| Analytical Contract | [AUC-001 Analytical Contract](auc-001-analytical-contract.md) | Completed |
| Evidence Set | [AUC-001 Evidence Set](auc-001-evidence-set.md) | Completed |
| AUC-001 | [Meta Lead Quality Analysis](/analytical_use_cases/meta_lead_quality_analysis.md) | Available |
| Skill | [meta-lead-quality-analysis](/.github/skills/meta-lead-quality-analysis/SKILL.md) | Available |

---

## Evidence Scope

| Field | Value |
|---|---|
| evidence_set_id | VCA-AUC-001-EVD-SET-001 |
| execution_id | VCA-AUC-001-EXEC-2026-06 |
| context_contract_id | VCA-AUC-001-CTX-DEF-2026-06 |
| analytical_contract_id | VCA-AUC-001-ANL-001 |
| analytical_model_id | VCA-AUC-001-AM-001 |
| source_model | `ad_quality_spend_model` |
| model_grain | normalized `ad_id` (`ad_id_norm`) |
| period | 2026-06-01 to 2026-06-30 |
| channel | Meta Ads / Meta Lead Ads |
| source_tables | `marts.fct_lead_enriched`; `intermediate.int_faro_lead_scoring`; `marts.fct_spend` |
| lead_quality_rule | Qualified Lead = `lead_tier IN ('A', 'B')` |
| spend_filter | `campaign_signal = 'COMMERCIAL'` |
| evidence_blocks | EVD-001, EVD-002, EVD-003, EVD-004 |

---

## Contracted Evidence Blocks

| Evidence ID | Evidence Type | Content | Source Metric Links | Status |
|---|---|---|---|---|
| EVD-001 | Observable summary | Model coverage by `coverage_status` | `coverage_status`, `lead_rows`, `distinct_leads`, `qualified_ab`, `lead_tier_a`, `lead_tier_b`, `spend_amount`, prepared ratios | Contracted |
| EVD-002 | Observable totals | Prepared model totals | `prepared_ads`, `lead_rows`, `distinct_leads`, `qualified_ab`, `spend_amount`, prepared ratios | Contracted |
| EVD-003 | Observable detail | Ad reference evidence by `ad_id_norm` and `ad_name` | ad reference dimensions, coverage state, lead quality metrics, spend metrics, prepared ratios | Contracted |
| EVD-004 | Observable aggregation | Campaign/adset evidence where lead-side metadata exists | campaign/adset dimensions, coverage state, lead quality metrics, spend metrics | Contracted with limitation |

---

## Observable Findings

The observable findings are defined in [AUC-001 Evidence Set](auc-001-evidence-set.md):

| Evidence ID | Finding Location | Contract Status |
|---|---|---|
| EVD-001 | `AUC-001 Evidence Set` / `Model Coverage By Status` | Usable for reasoning with limitations |
| EVD-002 | `AUC-001 Evidence Set` / `Prepared Model Totals` | Usable for reasoning with limitations |
| EVD-003 | `AUC-001 Evidence Set` / `Ad Reference Evidence` | Usable for reasoning with limitations |
| EVD-004 | `AUC-001 Evidence Set` / `Campaign And Adset Evidence Where Available` | Usable for reasoning with campaign/adset limitations |

This contract does not restate every evidence row as a new analytical output; it contracts the Evidence Set and preserves the evidence identifiers for downstream traceability.

---

## Derived Evidence

| Derived Evidence | Contract Status | Boundary |
|---|---|---|
| Cost ratios (`spend_per_lead`, `spend_per_qualified_ab`) | Contracted | Derived from prepared model; no efficiency conclusion is included |
| Quality ratio (`qualified_rate_ab`) | Contracted | Derived from prepared model; no quality interpretation is included |
| Coverage state counts | Contracted | Derived from model alignment state; no causality is included |
| Campaign/adset aggregations | Contracted with limitation | Only where lead-side campaign/adset metadata exists |
| Ad reference rows | Contracted | Ad reference only; not creative asset metadata |

---

## Source Metric Links

| Evidence Field | Analytical Model Field | Source Basis |
|---|---|---|
| `ad_id_norm` | `ad_id_norm` | Normalized lead `ad_id` aligned to `fct_spend.ad_id` |
| `ad_name` | `ad_name` | Lead-side ad name or spend-side fallback |
| `campaign_name` | `campaign_name` | Lead-side metadata only |
| `adset_name` | `adset_name` | Lead-side metadata only |
| `coverage_status` | `coverage_status` | Prepared model classification |
| `lead_rows` | `lead_rows` | `fct_lead_enriched` aggregated by `ad_id_norm` |
| `distinct_leads` | `distinct_leads` | Distinct `lead_id` in `fct_lead_enriched` |
| `qualified_ab` | `qualified_ab` | `lead_tier IN ('A', 'B')` |
| `lead_tier_a` | `lead_tier_a` | `lead_tier = 'A'` |
| `lead_tier_b` | `lead_tier_b` | `lead_tier = 'B'` |
| `spend_amount` | `spend_amount` | `fct_spend` filtered by `campaign_signal = 'COMMERCIAL'` |
| `spend_per_lead` | `spend_per_lead` | Prepared `SAFE_DIVIDE` metric |
| `spend_per_qualified_ab` | `spend_per_qualified_ab` | Prepared `SAFE_DIVIDE` metric |
| `qualified_rate_ab` | `qualified_rate_ab` | Prepared `SAFE_DIVIDE` metric |

---

## Critical Fields

| Field | Status | Notes |
|---|---|---|
| contract_id | Present | `VCA-AUC-001-EVD-001` |
| context_contract_id | Present | `VCA-AUC-001-CTX-DEF-2026-06` |
| analytical_contract_id | Present | `VCA-AUC-001-ANL-001` |
| evidence_scope | Present | June 2026 Meta Lead Ads evidence from `ad_quality_spend_model` |
| observable_findings | Present | EVD-001 through EVD-004 |
| derived_evidence | Present | Prepared ratios, coverage states and aggregations |
| source_metric_links | Present | Mapped above |
| limitations | Present | Contracted below |
| uncertainty_notes | Present | Contracted below |
| excluded_interpretations | Present | Contracted below |
| traceability_links | Present | Listed below |
| transition_status | Present | T-024 ready with limitations |

---

## Limitations

| Limitation | Contracted Handling |
|---|---|
| Lead tables do not expose `campaign_signal` | Reasoning must not treat lead rows as directly commercial; commercial filtering applies to spend-side records |
| `fct_spend` does not expose campaign/adset fields | Reasoning must not infer spend attribution for spend-only rows by campaign/adset |
| Campaign/adset values are lead-side metadata | Campaign/adset evidence is usable only where `fct_lead_enriched` exposes metadata |
| Creative asset metadata is unavailable | Reasoning may use ad reference evidence only, not media/format/asset-level claims |
| Raw Meta impressions/clicks are outside the corrected source set | Reasoning must not discuss impressions, clicks or CTR from this evidence |
| Duplicate/test-record flags are not explicitly mapped | Reasoning must preserve this uncertainty when using lead counts |
| `qualified_ab` is derived from Lead Tier A/B | Reasoning must trace quality evidence to the approved execution quality rule |
| Spend-only ratios are UNKNOWN | Reasoning must not derive cost-per-lead or quality-rate statements for spend-only rows |
| Lead-only spend is zero by model alignment | Reasoning must preserve the `lead_only` coverage state rather than infer absent spend behavior |

---

## Uncertainty Notes

| Uncertainty | Effect On Downstream Reasoning |
|---|---|
| No full duplicate/test exclusion field mapping | Lead evidence is usable, but exclusion completeness remains limited |
| No campaign/adset metadata for spend-only ads | Spend-only evidence cannot support campaign/adset-level interpretation |
| No raw click/impression metrics | Funnel entry beyond lead and spend cannot be reasoned from this Evidence Contract |
| No creative asset metadata | Creative reasoning must remain at ad reference/name level |
| `campaign_signal` is spend-side only | Commercial lead quality must be reasoned as matched-model evidence, not as a lead table attribute |

---

## Excluded Interpretations

The following are excluded from this Evidence Contract and reserved for later phases only if supported by evidence:

- causal explanations;
- business conclusions;
- insights or hypotheses;
- quality judgments about ads, campaigns or ad sets;
- efficiency judgments;
- optimization opportunities;
- recommendations or action priorities;
- presentation-ready executive narrative.

---

## Validation Rules Applied

| Rule | Result | Evidence |
|---|---|---|
| Analytical dependency | Pass | Contract consumes `VCA-AUC-001-ANL-001` |
| Evidence Set dependency | Pass | Contract formalizes `VCA-AUC-001-EVD-SET-001` |
| Observable only | Pass | Contract points to observable counts, sums, ratios and coverage states |
| No reasoning | Pass | No causes, insights, hypotheses or conclusions are included |
| No recommendations | Pass | No action or priority is formulated |
| Evidence traceability | Pass | Evidence blocks map to model metrics and dimensions |
| Limitation propagation | Pass | Analytical and Evidence Set limitations are preserved |
| Unknown explicitness | Pass | UNKNOWN values and unavailable fields are contracted |
| Scope alignment | Pass | Evidence remains within June 2026 AUC-001 execution scope |

---

## Transition Status

| Target | Status | Reason |
|---|---|---|
| T-023 Evidence Contract | Completed | Evidence Set is formalized with traceability, limitations and UNKNOWN handling |
| T-024 Reasoning Layer | Ready to start with limitations | Reasoning may consume this contract but must preserve documented uncertainty |
| Recommendations | Not authorized | Require reasoning and downstream knowledge artifacts first |
| Presentation | Not authorized | Requires knowledge, recommendations and presentation contract first |

---

## Traceability

- [T-023 in docs/tasks.md](/docs/tasks.md)
- [AUC-001 Evidence Set](auc-001-evidence-set.md)
- [AUC-001 Analytical Contract](auc-001-analytical-contract.md)
- [AUC-001 Analytical Preparation](auc-001-analytical-preparation.md)
- [AUC-001 Discovery Contract](auc-001-discovery-contract.md)
- [AUC-001 Data Contract](auc-001-data-contract.md)
- [AUC-001 Context Definition](auc-001-context-definition.md)
- [VCA-EVD-001 Base Evidence Contract](/docs/contracts/evidence.contract.md)
- [SPEC-001 Analytical Lifecycle](/specs/spec-001-analytical-lifecycle.md)
- [SPEC-002 Component Boundaries](/specs/spec-002-component-boundaries.md)
- [SPEC-004 Transversal Contracts](/specs/spec-004-transversal-contracts.md)
- [AUC-001 Meta Lead Quality Analysis](/analytical_use_cases/meta_lead_quality_analysis.md)
- [Meta Lead Quality Analysis Skill](/.github/skills/meta-lead-quality-analysis/SKILL.md)

---

## Completion Statement

T-023 is complete.

The Evidence Contract formalizes the AUC-001 Evidence Set as the handoff from Analytical Layer to Reasoning Layer, preserving observable findings, source metric links, limitations, UNKNOWN values and excluded interpretations.

T-024 may now begin reasoning from this contract, without requerying sources or introducing unsupported facts.

## AUC-001 Post-Closure Cost-Quality Evidence Rules

Estas reglas aplican solo a la evolucion post-cierre `AUC-001-PCI-001` definida por SPEC-012. No reabren el ciclo experimental original ni modifican outputs historicos.

### Runtime Boundary

| Fase | Responsabilidad |
|---|---|
| Evidence Acquisition | Adquirir agregados lead-side y spend-side mediante BigQuery MCP, sin unir fuentes ni interpretar. |
| Analytical Preparation | Normalizar, limpiar, validar y agregar cada fuente de forma independiente. |
| Evidence Set Construction | Ejecutar full outer join determinista, asignar coverage states, reconciliar totales, calcular invariantes y construir el Evidence Set coste-calidad. |

### Canonical Model vs Executed Evidence Set

| Elemento | Regla |
|---|---|
| Canonical model | Reglas estables de fuentes, normalizacion, universos, metricas, invariantes y blockers. |
| Executed Evidence Set | Instancia para un periodo, execution_id, datos, resultados, limitaciones y trazabilidad especificos. |
| Historical outputs | Permanecen inmutables y no pueden sobrescribirse ni usarse como expected values. |
| Post-closure outputs | Para `AUC-001-PCI-001` deben declarar la iteracion y persistirse bajo `outputs/auc-001/pci-001/2026-06-30/`; futuras iteraciones usaran `outputs/auc-001/pci-00N/<execution-date>/`. |

### Coverage States

| Estado | Regla |
|---|---|
| `matched` | Lead-side valido y spend `COMMERCIAL` valido para el mismo `ad_id_norm`. |
| `lead_only` | Lead-side valido sin spend `COMMERCIAL` emparejado; no soporta CPL/CPQL. |
| `spend_only` | Spend `COMMERCIAL` valido sin lead-side emparejado; no implica cero leads reales ni ineficiencia automatica. |
| `UNKNOWN` | Clasificacion no fiable por ID invalido, colision, duplicidad, periodo incompatible, señal invalida, fuente no validada o estructura incompleta. |

### Economic Universes And Metrics

El Evidence Set post-cierre debe distinguir `total_spend_all_signals`, `commercial_spend`, `matched_commercial_spend`, `spend_only_commercial_spend`, `total_leads`, `matched_leads`, `lead_only_leads`, `total_ab_leads`, `matched_ab_leads`, `lead_only_ab_leads`, Tier A total/matched y Tier B total/matched.

Metricas permitidas: `cpl_commercial_matched`, `qualified_rate_ab_global`, `qualified_rate_ab_matched`, `cost_per_ab_commercial_matched`, `cost_per_tier_a_commercial_matched`, `spend_share_by_signal`, `spend_share_matched`, `lead_share_matched`, `ab_share_matched`, `commercial_spend_per_matched_lead_observed`.

Metricas prohibidas: `CPL` sin universo, `CPQL` sin universo/señal/coverage, CPL/CPQL sobre `lead_only`, CPL/CPQL sobre `spend_only`, coste-calidad mezclando señales, rankings por `ad_name`, ratios con denominador cero convertido a cero y metricas que usen historicos como expected values.

### Invariants And Precision

```text
commercial_spend = matched_spend + spend_only_spend
lead_total = matched_leads + lead_only_leads
ab_total = matched_ab_leads + lead_only_ab_leads
tier_a_total = matched_tier_a + lead_only_tier_a
tier_b_total = matched_tier_b + lead_only_tier_b
prepared_ad_count = matched_ad_count + lead_only_ad_count + spend_only_ad_count
```

Moneda EUR, tipo recomendado `NUMERIC`, sin redondeo intermedio, presentacion monetaria a 2 decimales, tolerancia monetaria 0.01 EUR por fila y agregado, denominador cero como `NULL`, desconocidos como `NULL` o `UNKNOWN` explicito.

### Publication Controls

| Condicion | Clasificacion |
|---|---|
| Invariantes incumplidas, colisiones de `ad_id_norm`, periodos incompatibles, señal invalida, mezcla de señales, ausencia de trazabilidad MCP o fuente canonica no validada | Blocking error |
| `spend_only` interpretado como cero leads reales sin sustentar recomendacion | Warning |
| Muestra insuficiente para ranking o recomendacion | Presentation limitation |

Todo blocking error debe detener la publicacion del Evidence Set completo, bloque afectado o metrica concreta segun el alcance definido en SPEC-012.