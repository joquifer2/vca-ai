# AUC-001 Knowledge Set

## Metadata

| Field | Value |
|---|---|
| Artifact ID | VCA-AUC-001-KNW-SET-001 |
| Artifact Type | Knowledge Set |
| Analytical Use Case | AUC-001 - Meta Lead Quality Analysis |
| Evidence Contract ID | VCA-AUC-001-EVD-001 |
| Evidence Set ID | VCA-AUC-001-EVD-SET-001 |
| Analytical Contract ID | VCA-AUC-001-ANL-001 |
| Status | Confirmed against Knowledge Contract |
| Version | 1.1.0 |
| Last Updated | 2026-07-12 |
| Owner | Equipo VCA |
| Backing Task | T-024; T-026 confirmation |

---

## Purpose

Registrar el razonamiento de AUC-001 a partir del Evidence Contract aprobado.

Este Knowledge Set transforma evidencia observable en conocimiento trazable: insights, hipotesis, conclusiones, prioridades de lectura, riesgos e incertidumbres.

Este artefacto queda confirmado contra `VCA-AUC-001-KNW-001` como salida trazable de Razonamiento para AUC-001.

Este artefacto no reconsulta fuentes.

Este artefacto no crea evidencia nueva.

Este artefacto no formula acciones sugeridas ni recomendaciones.

---

## Backing Task

| Field | Value |
|---|---|
| Task ID | T-024; T-026 |
| Task | T-024: Implementar la capa de razonamiento del caso AUC-001; T-026: Implementar el Knowledge Set de AUC-001 |
| Specifications | SPEC-001 Analytical Lifecycle; SPEC-002 Component Boundaries |
| Skill | meta-lead-quality-analysis |
| Acceptance Criterion | El flujo convierte la evidencia en insights, hipotesis y conclusiones respaldadas por evidencia identificable; existe un Knowledge Set trazable con hipotesis priorizadas e incertidumbres declaradas |
| Implementation basis | T-023 Evidence Contract; T-025 Knowledge Contract |

---

## Reasoning Scope

| Field | Value |
|---|---|
| evidence_contract_id | VCA-AUC-001-EVD-001 |
| evidence_blocks | EVD-001, EVD-002, EVD-003, EVD-004 |
| period | 2026-06-01 to 2026-06-30 |
| source_model | `ad_quality_spend_model` |
| model_grain | normalized `ad_id` (`ad_id_norm`) |
| reasoning_boundary | Interpret evidence and uncertainty only; no recommendations or execution plan |

---

## Evidence-To-Knowledge Map

| Knowledge ID | Type | Evidence Links | Reasoning Status |
|---|---|---|---|
| INS-001 | Insight | EVD-001, EVD-002, EVD-003 | Supported with limitations |
| INS-002 | Insight | EVD-001, EVD-004 | Supported with limitations |
| INS-003 | Insight | EVD-001, EVD-003 | Supported with limitations |
| HYP-001 | Hypothesis | EVD-003, EVD-004 | Plausible; not causal |
| HYP-002 | Hypothesis | EVD-001, EVD-004 | Plausible; requires coverage caution |
| CON-001 | Conclusion | EVD-001, EVD-002 | Supported within model scope |
| CON-002 | Conclusion | EVD-001, EVD-003, EVD-004 | Supported with explicit limitations |
| RSK-001 | Risk | Evidence Contract limitations | Material reasoning risk |
| UNC-001 | Uncertainty | Evidence Contract uncertainty notes | Must propagate downstream |

---

## Insights

### INS-001 - Matched evidence is concentrated in one ad reference

The Evidence Set shows one matched ad reference, `120245828603090721` / `ViajeSinEstres_AlivioEmocional_ViajeSinEstres_Reel_v1`, with 519 lead rows, 152 qualified A/B leads and 374.79000799999875 spend.

This is the largest observed row in EVD-003 for leads, qualified A/B leads and spend among matched ad references.

Traceability: EVD-003; EVD-002.

Boundary: this is a concentration insight, not a claim of causal superiority or a recommendation.

### INS-002 - Evidence separates two campaign/adset coverage states

EVD-004 exposes one matched campaign/adset row for `[META]_[CLP]_[CAPTACION]_[ABO]` / `[PR]_[NATIVE FORM]_[AVG+]_[ISLA]` and one lead-only campaign/adset row for `[META]_[CLP]_[RTG]_[CBO]` / `[RTG]_[NATIVE FORM]_[INTERACCIONES + 50% VIDEO]_[DIASPORA]`.

The matched row carries commercial spend and lead quality evidence. The lead-only row carries lead quality evidence without matched commercial spend in the approved model.

Traceability: EVD-001; EVD-004.

Boundary: this does not prove that the lead-only campaign/adset had no spend outside the approved model; it only reflects the corrected model alignment.

### INS-003 - Spend-only evidence is small but structurally important

EVD-001 and EVD-003 show two spend-only ad references with total commercial spend of 2.200000000000001 and no matched lead rows in the model.

This spend-only state is materially small relative to the model total, but it is structurally relevant because it marks unmatched commercial spend that cannot support lead-quality ratios.

Traceability: EVD-001; EVD-003.

Boundary: the Evidence Contract forbids deriving spend-only cost-per-lead or quality-rate statements.

---

## Hypotheses

### HYP-001 - Lead quality and commercial spend may be concentrated around a limited matched ad subset

The matched coverage state contains 8 ad references, 680 lead rows, 191 qualified A/B leads and 494.3600089999987 spend. Within that state, EVD-003 shows one ad reference with the largest observed lead, qualified A/B and spend values.

Hypothesis: the June 2026 observed lead-quality and commercial-spend signal may be concentrated around a limited subset of matched ad references.

Traceability: EVD-001; EVD-003.

Validation condition: downstream reasoning must preserve that this is a model-based concentration hypothesis, not a causal explanation or creative-quality judgment.

### HYP-002 - Retargeting lead evidence requires separate treatment from matched commercial-spend evidence

EVD-004 shows the RTG campaign/adset only in `lead_only` coverage with 92 lead rows and 35 qualified A/B leads, while the commercial spend evidence appears in the matched CAPTACION/ABO row and spend-only rows.

Hypothesis: the RTG lead-quality evidence should be interpreted as a distinct coverage case from matched commercial-spend efficiency evidence.

Traceability: EVD-001; EVD-004.

Validation condition: this cannot be converted into campaign-level spend interpretation because `fct_spend` does not expose campaign/adset fields and lead tables do not expose `campaign_signal`.

---

## Conclusions

### CON-001 - AUC-001 has sufficient evidence to reason about ad-level lead quality and commercial spend within the corrected model

The Evidence Contract formalizes an Evidence Set with 15 prepared ad references, 772 lead rows, 226 qualified A/B leads and 496.5600089999987 commercial spend, all traced to `ad_quality_spend_model`.

This supports reasoning about ad-level lead quality and commercial spend under the documented coverage states.

Traceability: EVD-001; EVD-002; Evidence Contract source metric links.

Limitation: this conclusion applies only to the corrected model scope and does not cover impressions, clicks, CTR, creative asset metadata, or direct campaign/adset spend attribution.

### CON-002 - Campaign/adset-level reasoning is partially supported and must remain coverage-qualified

Campaign/adset evidence exists where lead-side metadata is present, but spend-only campaign/adset metadata is UNKNOWN and `fct_spend` lacks campaign/adset fields.

Therefore, campaign/adset-level reasoning can use EVD-004 only with coverage qualifiers and cannot assert full spend attribution by campaign/adset.

Traceability: EVD-004; Evidence Contract limitations.

Limitation: no direct campaign/adset spend mapping is available in the approved model.

---

## Reasoning Priorities

| Priority ID | Priority | Evidence Basis | Rationale | Boundary |
|---|---|---|---|---|
| PRI-001 | Preserve ad-level matched evidence as the strongest reasoning base | EVD-001, EVD-003 | Matched rows contain both lead quality and commercial spend | Does not imply action priority |
| PRI-002 | Treat lead-only evidence as quality evidence without matched commercial spend | EVD-001, EVD-004 | Lead-only rows contain lead metrics but no matched spend | Do not infer absent spend behavior |
| PRI-003 | Keep campaign/adset reasoning coverage-qualified | EVD-004, limitations | Campaign/adset metadata is lead-side only | Do not infer spend attribution |
| PRI-004 | Propagate missing impressions/clicks/creative asset metadata | Evidence Contract limitations | These evidence families are outside the corrected approved source set | Do not fill gaps by assumption |

---

## Risks

| Risk ID | Risk | Evidence Basis | Effect |
|---|---|---|---|
| RSK-001 | Treating matched spend as direct lead-level commercial classification | Evidence Contract limitations | Would overstate what lead tables expose |
| RSK-002 | Interpreting campaign/adset spend where metadata is absent | EVD-004; limitations | Would create unsupported campaign/adset conclusions |
| RSK-003 | Turning ad-reference concentration into creative causality | EVD-003; creative metadata limitation | Would infer causes or asset-level properties not evidenced |
| RSK-004 | Using lead-only rows for cost-efficiency conclusions | EVD-001; Evidence Contract limitations | Would ignore missing matched commercial spend |
| RSK-005 | Ignoring duplicate/test-record uncertainty | Evidence Contract uncertainty notes | Could overstate certainty of lead counts |

---

## Uncertainties

| Uncertainty ID | Unknown Or Limitation | Required Handling |
|---|---|---|
| UNC-001 | Duplicate/test-record flags are not explicitly mapped | Keep visible in Knowledge Contract and later output |
| UNC-002 | Spend-only campaign/adset metadata is UNKNOWN | Do not reason about campaign/adset identity for spend-only rows |
| UNC-003 | Impressions, clicks and CTR are unavailable | Do not create funnel-entry interpretations beyond leads and spend |
| UNC-004 | Creative asset metadata is unavailable | Keep creative reasoning at ad reference/name level only |
| UNC-005 | `campaign_signal` is spend-side only | Do not state that lead rows directly carry commercial signal |

---

## Excluded Recommendations

The following are explicitly outside T-024:

- budget allocation actions;
- campaign or adset optimization actions;
- creative production actions;
- lead handling or sales-process actions;
- execution priorities;
- implementation plans.

---

## Contract Confirmation

| Check | Result | Evidence |
|---|---|---|
| Knowledge Contract dependency | Pass | `VCA-AUC-001-KNW-001` formalizes this Knowledge Set |
| Insight coverage | Pass | INS-001 through INS-003 are present and traceable |
| Hypothesis coverage | Pass | HYP-001 and HYP-002 are present, non-causal and evidence-linked |
| Conclusion coverage | Pass | CON-001 and CON-002 are present with scope limits |
| Reasoning priorities | Pass | PRI-001 through PRI-004 are reasoning priorities, not action priorities |
| Risk coverage | Pass | RSK-001 through RSK-005 are present |
| Uncertainty coverage | Pass | UNC-001 through UNC-005 are present and must propagate downstream |
| Recommendation boundary | Pass | Recommendations, execution plans and action priorities remain excluded |

## Hypothesis Prioritization

| Hypothesis ID | Priority | Evidence Basis | Why This Priority | Validation Boundary |
|---|---|---|---|---|
| HYP-001 | P1 | EVD-001; EVD-003 | It concerns the main matched ad-level evidence base that contains both lead quality and commercial spend | Concentration hypothesis only; not causal and not an action priority |
| HYP-002 | P2 | EVD-001; EVD-004 | It affects how lead-only RTG evidence should be interpreted relative to matched spend evidence | Coverage-treatment hypothesis only; not campaign-level spend attribution |

These priorities are reasoning priorities. They do not authorize recommendations, budget allocation or execution sequencing.

## Confirmed Knowledge Inventory

| Category | Items | Status |
|---|---|---|
| Insights | INS-001, INS-002, INS-003 | Confirmed |
| Hypotheses | HYP-001, HYP-002 | Confirmed and prioritized for reasoning |
| Conclusions | CON-001, CON-002 | Confirmed with scope limits |
| Reasoning priorities | PRI-001, PRI-002, PRI-003, PRI-004 | Confirmed as non-action priorities |
| Risks | RSK-001, RSK-002, RSK-003, RSK-004, RSK-005 | Confirmed |
| Uncertainties | UNC-001, UNC-002, UNC-003, UNC-004, UNC-005 | Confirmed and propagated |

---
## Boundary Compliance

| Rule | Result | Evidence |
|---|---|---|
| Evidence dependency | Pass | Consumes `VCA-AUC-001-EVD-001` |
| No new evidence | Pass | Uses only EVD-001 through EVD-004 and contracted limitations |
| Evidence-backed reasoning | Pass | Every insight, hypothesis and conclusion links to evidence IDs |
| Correlation caution | Pass | Hypotheses are marked non-causal |
| No recommendations | Pass | No suggested action or execution plan is included |
| Uncertainty propagation | Pass | UNKNOWN and limitations are carried forward |

---

## Transition Status

| Target | Status | Reason |
|---|---|---|
| T-024 Reasoning Layer | Completed | Knowledge Set has been produced from the Evidence Contract |
| T-026 Knowledge Set confirmation | Completed | Knowledge Set has been confirmed against the Knowledge Contract |
| T-025 Knowledge Contract | Completed | Knowledge Set has been formalized contractually |
| Recommendation layer | Ready to start | T-025 and T-026 are complete; recommendation work must use the confirmed Knowledge Set |
| Presentation layer | Not authorized | Requires downstream recommendation and presentation contracts |

---

## Traceability

- [T-024 in docs/tasks.md](/docs/tasks.md)
- [T-026 in docs/tasks.md](/docs/tasks.md)
- [AUC-001 Knowledge Contract](auc-001-knowledge-contract.md)
- [AUC-001 Evidence Contract](auc-001-evidence-contract.md)
- [AUC-001 Evidence Set](auc-001-evidence-set.md)
- [AUC-001 Analytical Contract](auc-001-analytical-contract.md)
- [VCA-KNW-001 Base Knowledge Contract](/docs/contracts/knowledge.contract.md)
- [SPEC-001 Analytical Lifecycle](/specs/spec-001-analytical-lifecycle.md)
- [SPEC-002 Component Boundaries](/specs/spec-002-component-boundaries.md)
- [AUC-001 Meta Lead Quality Analysis](/analytical_use_cases/meta_lead_quality_analysis.md)
- [Meta Lead Quality Analysis Skill](/.github/skills/meta-lead-quality-analysis/SKILL.md)

---

## Completion Statement

T-024 and T-026 are complete.

The Knowledge Set converts the AUC-001 Evidence Contract into traceable insights, hypotheses, conclusions, priorities, risks and uncertainties without creating new evidence or recommendations. It has been confirmed against `VCA-AUC-001-KNW-001`.

T-027 may now begin recommendation-layer work from this confirmed Knowledge Set, without re-opening evidence or reasoning.