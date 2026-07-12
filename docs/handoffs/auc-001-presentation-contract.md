# AUC-001 Presentation Contract

## Metadata

| Field | Value |
|---|---|
| Contract ID | VCA-AUC-001-PRS-001 |
| Contract Name | AUC-001 Presentation Contract |
| Contract Category | Presentation Contract |
| Analytical Use Case | AUC-001 - Meta Lead Quality Analysis |
| Related Base Contract | VCA-PRS-001 |
| Context Definition ID | VCA-AUC-001-CTX-DEF-2026-06 |
| Evidence Contract ID | VCA-AUC-001-EVD-001 |
| Knowledge Contract ID | VCA-AUC-001-KNW-001 |
| Recommendation Contract ID | VCA-AUC-001-REC-001 |
| Recommendation Set ID | VCA-AUC-001-REC-SET-001 |
| Status | Documented |
| Version | 1.0.0 |
| Last Updated | 2026-07-12 |
| Owner | Equipo VCA |
| Backing Task | T-030 |

---

## Purpose

Delimitar el contenido aprobado que puede consumir la capa de presentacion para construir el Output Artifact de AUC-001.

Este contract autoriza secciones, fuentes, limitaciones, conocimiento y recomendaciones ya validadas para presentacion.

Este contract no crea evidencia nueva.

Este contract no introduce interpretaciones nuevas.

Este contract no reordena prioridades ni cambia recomendaciones.

Este contract no construye el informe ejecutivo final.

---

## Backing Task

| Field | Value |
|---|---|
| Task ID | T-030 |
| Task | Implementar el Presentation Contract del caso AUC-001 |
| Specifications | SPEC-002 Component Boundaries; SPEC-004 Transversal Contracts |
| Skill | meta-lead-quality-analysis |
| Acceptance Criterion | Existe un Presentation Contract que delimita el contenido aprobado para la capa de presentacion sin nueva interpretacion |
| Implementation basis | T-029 confirmed Recommendation Set; T-028 Recommendation Contract; base Presentation Contract |

---

## Producer And Consumer

| Role | Value |
|---|---|
| Producer | Framework after confirmed Recommendation Set and Recommendation Contract |
| Consumer | Presentation Layer / T-031 executive report constructor |
| Framework role | Validate output readiness before building the final artifact |
| Downstream artifact | T-031 Executive Output Artifact |

---

## Inputs

| Input | Artifact | Status |
|---|---|---|
| Context Definition | [AUC-001 Context Definition](auc-001-context-definition.md) | Validated |
| Evidence Contract | [AUC-001 Evidence Contract](auc-001-evidence-contract.md) | Completed |
| Evidence Set | [AUC-001 Evidence Set](auc-001-evidence-set.md) | Completed |
| Knowledge Contract | [AUC-001 Knowledge Contract](auc-001-knowledge-contract.md) | Completed |
| Knowledge Set | [AUC-001 Knowledge Set](auc-001-knowledge-set.md) | Confirmed |
| Recommendation Contract | [AUC-001 Recommendation Contract](auc-001-recommendation-contract.md) | Completed |
| Recommendation Set | [AUC-001 Recommendation Set](auc-001-recommendation-set.md) | Confirmed |
| Base Presentation Contract | [VCA-PRS-001 Presentation Contract](../contracts/presentation.contract.md) | Documented |
| AUC-001 | [Meta Lead Quality Analysis](../../analytical_use_cases/meta_lead_quality_analysis.md) | Available |
| Skill | [meta-lead-quality-analysis](../../.github/skills/meta-lead-quality-analysis/SKILL.md) | Available |

---

## Presentation Scope

| Field | Value |
|---|---|
| presentation_contract_id | VCA-AUC-001-PRS-001 |
| context_contract_id | VCA-AUC-001-CTX-DEF-2026-06 |
| evidence_contract_id | VCA-AUC-001-EVD-001 |
| knowledge_contract_id | VCA-AUC-001-KNW-001 |
| recommendation_contract_id | VCA-AUC-001-REC-001 |
| period | 2026-06-01 to 2026-06-30 |
| output_request | Informe ejecutivo trazable |
| audience | Analista de negocio, direccion, responsable de Marketing, especialistas de Meta Ads y equipo Comercial |
| source_model | `ad_quality_spend_model` |
| presentation_boundary | Presentation content scoping only; no final narrative, no new evidence, no new reasoning, no new recommendations |

---

## Required Sections

| Section ID | Required Section | Approved Content Source | Presentation Rule |
|---|---|---|---|
| SEC-001 | Context and scope | Context Definition | Present objective, period, operational scope, filters, lead quality definition, audience and output request without expanding scope |
| SEC-002 | Source and model basis | Evidence Contract; Analytical Contract | Present approved source tables, model grain, quality rule and spend filter without introducing new data sources |
| SEC-003 | Evidence summary | Evidence Set; Evidence Contract | Present EVD-001 through EVD-004 as observable evidence with limitations visible |
| SEC-004 | Knowledge summary | Knowledge Set; Knowledge Contract | Present contracted insights, hypotheses, conclusions, priorities, risks and uncertainties without reinterpreting them |
| SEC-005 | Recommendations | Recommendation Set; Recommendation Contract | Present REC-001 through REC-006 with approved priority, justification and constraints |
| SEC-006 | Limitations and UNKNOWNs | Evidence Contract; Knowledge Contract; Recommendation Contract | Keep material limitations, risks and uncertainties visible in the final output |
| SEC-007 | Traceability | All upstream contracts and sets | Preserve enough source references for reviewer and QA validation |

---

## Approved Evidence Content

| Evidence ID | Approved For Presentation | Required Boundary |
|---|---|---|
| EVD-001 | Model coverage by `coverage_status` | Must preserve matched, lead_only and spend_only distinctions |
| EVD-002 | Prepared model totals | Must present as prepared-model totals, not as complete business universe beyond approved scope |
| EVD-003 | Ad reference evidence by `ad_id_norm` and `ad_name` | Must remain ad-reference level; no creative asset interpretation |
| EVD-004 | Campaign/adset evidence where lead-side metadata exists | Must remain coverage-qualified; no unsupported campaign/adset spend attribution |

---

## Approved Knowledge Content

| Knowledge Category | Approved IDs | Presentation Rule |
|---|---|---|
| Insights | INS-001, INS-002, INS-003 | Present as contracted insights only |
| Hypotheses | HYP-001, HYP-002 | Present as hypotheses, not conclusions or causal explanations |
| Conclusions | CON-001, CON-002 | Preserve corrected-model and campaign/adset scope limits |
| Reasoning priorities | PRI-001, PRI-002, PRI-003, PRI-004 | Present as reading priorities, not execution priorities |
| Risks | RSK-001, RSK-002, RSK-003, RSK-004, RSK-005 | Keep visible where they constrain interpretation |
| Uncertainties | UNC-001, UNC-002, UNC-003, UNC-004, UNC-005 | Keep visible in limitations and relevant sections |

---

## Approved Recommendations

| Recommendation ID | Priority | Approved Presentation Summary | Required Constraint |
|---|---|---|---|
| REC-001 | P1 | Use matched ad-level evidence as the primary basis for efficiency-oriented decisions | Do not treat matched rows as the only valid quality evidence |
| REC-002 | P1 | Treat RTG lead-only evidence as a separate quality reading, not matched spend efficiency | Do not create RTG spend-efficiency claims |
| REC-003 | P2 | Validate or document campaign/adset spend mapping before campaign-level spend recommendations | Do not issue campaign/adset spend recommendations without mapping |
| REC-004 | P2 | Keep creative recommendations at ad-reference level unless creative asset metadata is added | Do not claim media, format or asset attributes |
| REC-005 | P2 | Preserve duplicate/test-record uncertainty in downstream decisions and final output | Do not overstate lead-count certainty |
| REC-006 | P3 | Exclude impressions, clicks and CTR from recommendations unless source scope is expanded | Do not add funnel-entry metrics in the current output |

---

## Required Limitations

| Limitation Or UNKNOWN | Source | Required Handling In Output Artifact |
|---|---|---|
| Duplicate/test-record flags are not explicitly mapped | UNC-001; Evidence Contract | Must remain visible when presenting lead counts and certainty |
| Spend-only campaign/adset metadata is UNKNOWN | UNC-002; Evidence Contract | Must prevent campaign/adset spend conclusions for spend-only rows |
| Impressions, clicks and CTR are unavailable | UNC-003; Evidence Contract | Must be marked unavailable; no CTR or click/impression narrative |
| Creative asset metadata is unavailable | UNC-004; Evidence Contract | Must keep creative discussion at ad-reference/name level |
| `campaign_signal` is spend-side only | UNC-005; Evidence Contract | Must avoid stating that lead rows directly carry commercial signal |
| Lead-only spend is zero by model alignment | Evidence Contract | Must preserve `lead_only` coverage state instead of inferring absent spend behavior |
| Spend-only ratios are UNKNOWN | Evidence Contract | Must not present cost-per-lead or quality-rate statements for spend-only rows |
| Campaign/adset values are lead-side metadata | Evidence Contract; Knowledge Contract | Must keep campaign/adset reasoning coverage-qualified |

---

## Excluded Content

The following content is not authorized for the T-031 Output Artifact unless a future approved contract revision provides it:

- new BigQuery queries or new data extraction;
- new evidence blocks beyond EVD-001 through EVD-004;
- new metrics beyond the contracted source metric links and prepared ratios;
- causal explanations about ad, campaign, adset or creative performance;
- asset-level creative claims about media, format, visual elements or copy attributes;
- campaign/adset spend recommendations without approved spend mapping;
- impressions, clicks, CTR or funnel-entry interpretation;
- re-prioritized recommendations;
- execution plans, owner assignments or operational commitments;
- narrative claims that soften or hide material limitations and UNKNOWNs.

---

## Presentation Constraints

| Constraint | Rule |
|---|---|
| No new evidence | The final artifact may only present evidence already contracted in EVD-001 through EVD-004 |
| No reinterpretation | The final artifact may format or summarize, but must not alter meaning, confidence, scope or limitations |
| No priority rewrite | Recommendation priorities must remain P1, P2 and P3 as contracted |
| Limitation visibility | Required limitations and UNKNOWNs must be visible in the output, not relegated to implicit assumptions |
| Traceability preservation | The output must reference upstream contracts and evidence/knowledge/recommendation IDs sufficiently for review |
| Format containment | Executive wording may improve readability only if it preserves analytical meaning and boundaries |
| Scope containment | The output must remain within June 2026, Meta Lead Ads, approved filters and corrected source model |

---

## Transition Readiness

| Target | Status | Reason |
|---|---|---|
| T-030 Presentation Contract | Completed | Presentation content scope, required sections, approved recommendations, limitations and exclusions are documented |
| T-031 Executive Output Artifact | Completed | Output Artifact consumes this contract without adding evidence, reasoning or recommendations |
| New data acquisition | Not authorized | No downstream presentation need can reopen data acquisition without a new approved task/contract revision |

---

## Validation Rules Applied

| Rule | Result | Evidence |
|---|---|---|
| Recommendation dependency | Pass | Consumes `VCA-AUC-001-REC-001` and confirmed Recommendation Set |
| Knowledge dependency | Pass | Consumes `VCA-AUC-001-KNW-001` and confirmed Knowledge Set |
| Evidence dependency | Pass | Approved evidence limited to EVD-001 through EVD-004 |
| No new evidence | Pass | No metrics, rows, queries or evidence blocks introduced |
| No reinterpretation | Pass | Knowledge and recommendations are referenced by approved IDs and boundaries |
| No priority rewrite | Pass | REC-001 through REC-006 keep contracted priorities |
| Limitation visibility | Pass | Required limitations and UNKNOWNs are enumerated |
| Traceability preservation | Pass | Upstream artifacts are listed below |
| Format containment | Pass | Final narrative is deferred to T-031 |

---

## Traceability

- [T-030 in docs/tasks.md](../tasks.md)
- [AUC-001 Context Definition](auc-001-context-definition.md)
- [AUC-001 Evidence Contract](auc-001-evidence-contract.md)
- [AUC-001 Evidence Set](auc-001-evidence-set.md)
- [AUC-001 Knowledge Contract](auc-001-knowledge-contract.md)
- [AUC-001 Knowledge Set](auc-001-knowledge-set.md)
- [AUC-001 Recommendation Contract](auc-001-recommendation-contract.md)
- [AUC-001 Recommendation Set](auc-001-recommendation-set.md)
- [VCA-PRS-001 Base Presentation Contract](../contracts/presentation.contract.md)
- [SPEC-002 Component Boundaries](../../specs/spec-002-component-boundaries.md)
- [SPEC-004 Transversal Contracts](../../specs/spec-004-transversal-contracts.md)
- [AUC-001 Meta Lead Quality Analysis](../../analytical_use_cases/meta_lead_quality_analysis.md)
- [Meta Lead Quality Analysis Skill](../../.github/skills/meta-lead-quality-analysis/SKILL.md)

---

## Completion Statement

T-030 is complete.

The Presentation Contract delimits the approved content for the AUC-001 presentation layer. T-031 has built the executive output artifact under this contract without adding evidence, reasoning or recommendations.
