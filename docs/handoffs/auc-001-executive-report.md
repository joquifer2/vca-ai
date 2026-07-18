# AUC-001 Executive Report

## Metadata

| Field | Value |
|---|---|
| Artifact ID | VCA-AUC-001-OUT-001 |
| Artifact Type | Selected Presentation Projection / Executive Report |
| Analytical Use Case | AUC-001 - Meta Lead Quality Analysis |
| Presentation Contract ID | VCA-AUC-001-PRS-001 |
| Presentation Mode | Executive |
| Selected Presentation Projection | Executive Report |
| Context Definition ID | VCA-AUC-001-CTX-DEF-2026-06 |
| Evidence Contract ID | VCA-AUC-001-EVD-001 |
| Knowledge Contract ID | VCA-AUC-001-KNW-001 |
| Recommendation Contract ID | VCA-AUC-001-REC-001 |
| Status | Documented |
| Version | 1.1.0 |
| Last Updated | 2026-07-13 |
| Owner | Equipo VCA |
| Backing Task | T-031 |
| Alignment Task | T-045 |

---

## Purpose

Presentar el resultado ejecutivo trazable de AUC-001 para la ejecucion de junio de 2026 como Executive Report seleccionado.

Este Executive Report consume el Presentation Contract `VCA-AUC-001-PRS-001` y presenta contexto, evidencia, conocimiento, recomendaciones, limitaciones y trazabilidad ya aprobados.

Este artefacto no crea evidencia nueva.

Este artefacto no introduce nueva interpretacion.

Este artefacto no altera prioridades ni formula recomendaciones adicionales.

Este artefacto es una proyeccion ejecutiva del mismo contenido canonico aprobado por Evidence, Knowledge y Recommendation Sets.

Este artefacto no deriva de una proyeccion analitica. Cualquier proyeccion analitica futura debe tratarse como representacion hermana, no como fuente previa de este Executive Report.

Las recomendaciones presentadas aqui son sugerencias documentales aprobadas; no constituyen autorizacion operativa por si mismas.

---

## Projection Alignment

| Field | Value |
|---|---|
| Presentation mode | Executive |
| Selected presentation projection | Executive Report |
| Projection source | Context Definition, Output Request and AUC-001 Presentation Contract |
| Canonical content consumed | Evidence Set, Knowledge Set and Recommendation Set already approved for AUC-001 |
| Relationship to analytical projection | Sibling representation; not derived from an analytical projection |
| Boundary status | No new evidence, no new interpretation, no new recommendations and no priority rewrite |

Trazabilidad: SPEC-010; VCA-AUC-001-ARCH-002; VCA-AUC-001-PRS-001.

---

## Executive Summary

La ejecucion AUC-001 de junio de 2026 analiza calidad de leads de Meta Lead Ads con el modelo corregido `ad_quality_spend_model`, a grano `ad_id_norm` y con Qualified Lead definido como Lead Tier A o B.

El modelo preparado contiene 15 referencias de anuncio, 772 leads, 226 leads cualificados A/B y 496.5600089999987 de inversion comercial. La tasa preparada de cualificacion A/B es 0.2927461139896373 y el coste preparado por lead cualificado A/B es 2.197168181415923. Estos valores pertenecen al modelo preparado y deben leerse dentro de sus limites documentados. Trazabilidad: EVD-002; CON-001.

Los valores numericos se muestran con la precision recibida desde la evidencia para preservar trazabilidad. Si se requiere una presentacion redondeada, debe definirse mediante una regla de formato controlada sin alterar los valores fuente.

La evidencia se organiza en tres estados de cobertura: `matched`, `lead_only` y `spend_only`. El estado `matched` contiene 8 referencias de anuncio, 680 leads, 191 leads cualificados A/B y 494.3600089999987 de inversion comercial. El estado `lead_only` contiene 5 referencias de anuncio, 92 leads y 35 leads cualificados A/B sin inversion comercial emparejada en el modelo aprobado. El estado `spend_only` contiene 2 referencias de anuncio y 2.200000000000001 de inversion comercial sin leads emparejados. Trazabilidad: EVD-001.

La lectura ejecutiva aprobada es que AUC-001 permite razonar sobre calidad de lead e inversion comercial a nivel de referencia de anuncio dentro del modelo corregido, mientras que la lectura por campana/conjunto debe permanecer condicionada por cobertura. Trazabilidad: CON-001; CON-002.

---

## Context And Scope

| Field | Value |
|---|---|
| Period | 2026-06-01 to 2026-06-30 |
| Operational scope | Todas las campanas, conjuntos y creatividades de Meta Lead Ads con inversion o leads durante el periodo |
| Filters | `campaign_signal = COMMERCIAL`; excluir registros de prueba; excluir duplicados; excluir leads sin identificador valido; sin filtro geografico adicional |
| Lead quality definition | Qualified Lead segun FARO, equivalente a Lead Tier A o B |
| Audience | Analista de negocio, direccion, responsable de Marketing, especialistas de Meta Ads y equipo Comercial |
| Output request | Informe ejecutivo trazable |
| Presentation mode | Executive |
| Selected presentation projection | Executive Report |
| Projection relationship | Sibling representation from approved canonical content; not derived from analytical projection |

Trazabilidad: AUC-001 Context Definition; SEC-001.

---

## Source And Model Basis

| Element | Approved Basis |
|---|---|
| Source model | `ad_quality_spend_model` |
| Model grain | normalized `ad_id` (`ad_id_norm`) |
| Source tables | `marts.fct_lead_enriched`; `intermediate.int_faro_lead_scoring`; `marts.fct_spend` |
| Primary lead source | `marts.fct_lead_enriched` |
| Lead validation source | `intermediate.int_faro_lead_scoring` |
| Primary spend source | `marts.fct_spend` |
| Lead quality rule | `lead_tier IN ('A', 'B')` |
| Spend filter | `campaign_signal = 'COMMERCIAL'` |
| Coverage states | `matched`; `lead_only`; `spend_only` |

Trazabilidad: Analytical Contract `VCA-AUC-001-ANL-001`; Evidence Contract `VCA-AUC-001-EVD-001`; SEC-002.

---

## Evidence Summary

### EVD-001 - Model coverage by status

| coverage_status | ad_count | lead_rows | distinct_leads | qualified_ab | spend_amount | qualified_rate_ab |
|---|---:|---:|---:|---:|---:|---:|
| matched | 8 | 680 | 680 | 191 | 494.3600089999987 | 0.28088235294117647 |
| lead_only | 5 | 92 | 92 | 35 | 0.0 | 0.3804347826086957 |
| spend_only | 2 | 0 | 0 | 0 | 2.200000000000001 | UNKNOWN |

Boundary: `matched`, `lead_only` and `spend_only` must remain separate coverage states.

### EVD-002 - Prepared model totals

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

Boundary: totals are prepared-model totals, not a claim beyond approved scope.

### EVD-003 - Ad reference evidence

The largest matched ad reference in the approved Evidence Set is `120245828603090721` / `ViajeSinEstres_AlivioEmocional_ViajeSinEstres_Reel_v1`, with 519 lead rows, 152 qualified A/B leads and 374.79000799999875 spend.

This supports the contracted concentration insight, without causal or creative-asset claims. Trazabilidad: EVD-003; INS-001; HYP-001.

### EVD-004 - Campaign and adset evidence where available

| campaign_name | adset_name | coverage_status | ad_count | lead_rows | qualified_ab | spend_amount | qualified_rate_ab |
|---|---|---|---:|---:|---:|---:|---:|
| [META]_[CLP]_[CAPTACION]_[ABO] | [PR]_[NATIVE FORM]_[AVG+]_[ISLA] | matched | 8 | 680 | 191 | 494.3600089999987 | 0.28088235294117647 |
| [META]_[CLP]_[RTG]_[CBO] | [RTG]_[NATIVE FORM]_[INTERACCIONES + 50% VIDEO]_[DIASPORA] | lead_only | 5 | 92 | 35 | 0.0 | 0.3804347826086957 |
| UNKNOWN | UNKNOWN | spend_only | 2 | 0 | 0 | 2.200000000000001 | UNKNOWN |

Boundary: campaign/adset values are usable where lead-side metadata exists; direct campaign/adset spend attribution is not available for spend-only rows.

---

## Knowledge Summary

### Insights

| Insight | Statement | Traceability | Boundary |
|---|---|---|---|
| INS-001 | Matched evidence is concentrated in one ad reference: `120245828603090721` / `ViajeSinEstres_AlivioEmocional_ViajeSinEstres_Reel_v1`. | EVD-001; EVD-002; EVD-003 | Concentration insight only; no causal superiority claim |
| INS-002 | Evidence separates matched CAPTACION/ABO from lead-only RTG/CBO coverage. | EVD-001; EVD-004 | Does not prove spend absence outside the approved model |
| INS-003 | Spend-only evidence is small in amount but structurally important because it cannot support lead-quality ratios. | EVD-001; EVD-003 | No spend-only cost-per-lead or quality-rate statement |

### Hypotheses and conclusions

| ID | Approved Statement | Traceability | Boundary |
|---|---|---|---|
| HYP-001 | The June 2026 observed lead-quality and commercial-spend signal may be concentrated around a limited subset of matched ad references. | EVD-001; EVD-003 | Model-based concentration hypothesis, not causal explanation |
| HYP-002 | RTG lead-quality evidence should be interpreted as a distinct coverage case from matched commercial-spend efficiency evidence. | EVD-001; EVD-004 | Not campaign-level spend attribution |
| CON-001 | AUC-001 has sufficient evidence to reason about ad-level lead quality and commercial spend within the corrected model. | EVD-001; EVD-002 | Excludes impressions, clicks, CTR, creative asset metadata and direct campaign/adset spend attribution |
| CON-002 | Campaign/adset-level reasoning is partially supported and must remain coverage-qualified. | EVD-004 | No direct campaign/adset spend mapping is available in the approved model |

### Reasoning priorities

| Priority ID | Approved Priority | Boundary |
|---|---|---|
| PRI-001 | Preserve ad-level matched evidence as the strongest reasoning base | Reasoning priority, not action priority |
| PRI-002 | Treat lead-only evidence as quality evidence without matched commercial spend | Do not infer absent spend behavior |
| PRI-003 | Keep campaign/adset reasoning coverage-qualified | Do not infer spend attribution |
| PRI-004 | Propagate missing impressions/clicks/creative asset metadata | Do not fill evidence gaps by assumption |

---

## Recommendations

| Priority | Recommendation | Approved Action | Traceability |
|---|---|---|---|
| P1 | REC-001 | Base any near-term efficiency discussion on matched ad-level evidence first, especially the 8 matched ad references where both lead quality and commercial spend are present. | CON-001; PRI-001; INS-001; HYP-001; EVD-001; EVD-003 |
| P1 | REC-002 | Report and reason about RTG lead-only evidence separately from matched commercial-spend efficiency evidence. | INS-002; HYP-002; PRI-002; CON-002; UNC-005; EVD-004 |
| P2 | REC-003 | Before issuing campaign-level spend recommendations, either validate an approved campaign/adset spend mapping or explicitly keep campaign/adset spend recommendations out of scope. | CON-002; PRI-003; RSK-002; UNC-002; EVD-004 |
| P2 | REC-004 | Frame any creative-related recommendation at `ad_id_norm` / `ad_name` reference level only, and avoid claims about media, format or asset attributes. | INS-001; HYP-001; RSK-003; UNC-004; EVD-003 |
| P2 | REC-005 | Carry the duplicate/test-record limitation into downstream recommendation and presentation artifacts, and avoid overstating lead-count certainty. | UNC-001; RSK-005; Evidence Contract uncertainty notes |
| P3 | REC-006 | Do not make recommendations based on impressions, clicks or CTR in the current AUC-001 output; mark them unavailable unless a future approved source expansion provides them. | PRI-004; UNC-003; CON-001; Evidence Contract limitations |

These recommendations preserve the approved priority order P1, P2 and P3 from the Recommendation Contract.

These recommendations are documentary suggested actions only; they do not authorize operational execution by themselves.

---

## Limitations And Pending Items

| Limitation Or UNKNOWN | Required Handling | Traceability |
|---|---|---|
| Duplicate/test-record flags are not explicitly mapped | Keep visible when presenting lead counts and certainty | UNC-001; REC-005 |
| Spend-only campaign/adset metadata is UNKNOWN | Prevent campaign/adset spend conclusions for spend-only rows | UNC-002; REC-003 |
| Impressions, clicks and CTR are unavailable | Mark unavailable; no CTR or click/impression narrative | UNC-003; REC-006 |
| Creative asset metadata is unavailable | Keep creative discussion at ad-reference/name level | UNC-004; REC-004 |
| `campaign_signal` is spend-side only | Do not state that lead rows directly carry commercial signal | UNC-005; REC-002 |
| Lead-only spend is zero by model alignment | Preserve `lead_only` coverage state instead of inferring absent spend behavior | Evidence Contract |
| Spend-only ratios are UNKNOWN | Do not present cost-per-lead or quality-rate statements for spend-only rows | Evidence Contract |
| Campaign/adset values are lead-side metadata | Keep campaign/adset reasoning coverage-qualified | CON-002; PRI-003 |

---

## Traceability Matrix

| Output Section | Source IDs | Source Artifacts |
|---|---|---|
| Projection alignment | SPEC-010; ARCH-002; VCA-AUC-001-PRS-001 | Presentation Contract; Projection Architectural Decision |
| Context and scope | SEC-001 | Context Definition; Presentation Contract |
| Source and model basis | SEC-002 | Analytical Contract; Evidence Contract |
| Evidence summary | EVD-001; EVD-002; EVD-003; EVD-004 | Evidence Set; Evidence Contract |
| Knowledge summary | INS-001..INS-003; HYP-001..HYP-002; CON-001..CON-002; PRI-001..PRI-004 | Knowledge Set; Knowledge Contract |
| Recommendations | REC-001..REC-006 | Recommendation Set; Recommendation Contract |
| Limitations | UNC-001..UNC-005; Evidence Contract limitations | Knowledge Contract; Recommendation Contract; Presentation Contract |

---

## Projection Traceability

- [SPEC-010 Presentation Projection Selection](/specs/spec-010-presentation-projection-selection.md)
- [VCA-AUC-001-ARCH-002 Presentation Projection Decision](/docs/decisions/auc-001/auc-001-presentation-projection-architectural-decision.md)
- [T-043 Documentary Alignment Decision](/docs/decisions/auc-001/auc-001-documentary-alignment-decision.md)
- [T-044 Base Contracts Alignment Record](/docs/evaluations/auc-001/validations/auc-001-base-contracts-alignment-record.md)
- [AUC-001 Presentation Contract](auc-001-presentation-contract.md)
---

## Boundary Compliance

| Rule | Result | Evidence |
|---|---|---|
| Presentation Contract dependency | Pass | Consumes `VCA-AUC-001-PRS-001` |
| No new evidence | Pass | Uses EVD-001 through EVD-004 only |
| No new interpretation | Pass | Presents INS, HYP, CON and PRI items already contracted |
| No recommendation rewrite | Pass | Presents REC-001 through REC-006 with approved priorities |
| Limitation visibility | Pass | Required UNKNOWNs and limitations are explicit |
| Traceability preservation | Pass | Each section maps to upstream artifact IDs |
| Projection selection dependency | Pass | Metadata and Projection Alignment identify Executive Report as selected projection |
| Sibling projection preservation | Pass | Projection Alignment states that analytical projection and Executive Report are sibling representations |
| No projection derivation | Pass | Projection Alignment states this Executive Report is not derived from an analytical projection |

---

## Completion Statement

T-031 is complete.

This Executive Report presents context, evidence, reasoning, recommendations and limitations for AUC-001 under the Presentation Contract, without reintroducing evidence, interpretation, recommendations or projection derivation from an analytical output.
