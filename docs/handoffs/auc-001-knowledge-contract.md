# AUC-001 Knowledge Contract

## Metadata

| Field | Value |
|---|---|
| Contract ID | VCA-AUC-001-KNW-001 |
| Contract Name | AUC-001 Knowledge Contract |
| Contract Category | Knowledge Contract |
| Analytical Use Case | AUC-001 - Meta Lead Quality Analysis |
| Related Base Contract | VCA-KNW-001 |
| Knowledge Set ID | VCA-AUC-001-KNW-SET-001 |
| Evidence Contract ID | VCA-AUC-001-EVD-001 |
| Status | Documented |
| Version | 1.0.0 |
| Last Updated | 2026-07-12 |
| Owner | Equipo VCA |
| Backing Task | T-025 |

---

## Purpose

Formalizar el Knowledge Set de AUC-001 como handoff contractual desde la fase de Razonamiento hacia las fases posteriores.

Este contract estructura insights, hipotesis, conclusiones, prioridades de lectura, riesgos e incertidumbres generadas desde el Evidence Contract.

Este contract no crea evidencia nueva.

Este contract no formula acciones sugeridas.

Este contract no define esfuerzo, dependencias operativas ni plan de ejecucion.

---

## Backing Task

| Field | Value |
|---|---|
| Task ID | T-025 |
| Task | Implementar el Knowledge Contract del caso AUC-001 |
| Specifications | SPEC-001 Analytical Lifecycle; SPEC-002 Component Boundaries; SPEC-004 Transversal Contracts |
| Skill | meta-lead-quality-analysis |
| Acceptance Criterion | Existe un Knowledge Contract con insights, hipotesis, prioridades e incertidumbres declaradas |
| Implementation basis | T-024 Knowledge Set |

---

## Producer And Consumer

| Role | Value |
|---|---|
| Producer | Reasoning Layer / Phase 4 Reasoning |
| Consumer | Reasoning Layer / Phase 5 Recommendations |
| Framework role | Validate readiness before recommendation work |
| Downstream artifact | T-026 Knowledge Set confirmation; later recommendation artifacts |

---

## Inputs

| Input | Artifact | Status |
|---|---|---|
| Context Definition | [AUC-001 Context Definition](auc-001-context-definition.md) | Validated |
| Evidence Contract | [AUC-001 Evidence Contract](auc-001-evidence-contract.md) | Completed |
| Evidence Set | [AUC-001 Evidence Set](auc-001-evidence-set.md) | Completed |
| Knowledge Set | [AUC-001 Knowledge Set](auc-001-knowledge-set.md) | Completed |
| AUC-001 | [Meta Lead Quality Analysis](../../analytical_use_cases/meta_lead_quality_analysis.md) | Available |
| Skill | [meta-lead-quality-analysis](../../.github/skills/meta-lead-quality-analysis/SKILL.md) | Available |

---

## Reasoning Scope

| Field | Value |
|---|---|
| knowledge_set_id | VCA-AUC-001-KNW-SET-001 |
| evidence_contract_id | VCA-AUC-001-EVD-001 |
| context_contract_id | VCA-AUC-001-CTX-DEF-2026-06 |
| period | 2026-06-01 to 2026-06-30 |
| source_model | `ad_quality_spend_model` |
| evidence_blocks | EVD-001, EVD-002, EVD-003, EVD-004 |
| reasoning_boundary | Knowledge formalization only; no recommendations or execution plan |

---

## Contracted Knowledge Items

| Knowledge ID | Category | Evidence Links | Contract Status | Boundary |
|---|---|---|---|---|
| INS-001 | Insight | EVD-001, EVD-002, EVD-003 | Contracted | Concentration insight; no causal claim |
| INS-002 | Insight | EVD-001, EVD-004 | Contracted | Coverage-state distinction; no spend inference outside model |
| INS-003 | Insight | EVD-001, EVD-003 | Contracted | Structural spend-only insight; no quality ratio for spend-only rows |
| HYP-001 | Hypothesis | EVD-001, EVD-003 | Contracted | Plausible concentration hypothesis; not causal |
| HYP-002 | Hypothesis | EVD-001, EVD-004 | Contracted | Separate treatment hypothesis; campaign/adset limitations preserved |
| CON-001 | Conclusion | EVD-001, EVD-002, source metric links | Contracted | Applies only to corrected model scope |
| CON-002 | Conclusion | EVD-004, Evidence Contract limitations | Contracted | Campaign/adset reasoning is partial and coverage-qualified |
| PRI-001 | Priority of reading | EVD-001, EVD-003 | Contracted | Strongest reasoning base, not action priority |
| PRI-002 | Priority of reading | EVD-001, EVD-004 | Contracted | Lead-only treated without matched spend |
| PRI-003 | Priority of reading | EVD-004, limitations | Contracted | Campaign/adset reasoning must be coverage-qualified |
| PRI-004 | Priority of reading | Evidence Contract limitations | Contracted | Missing evidence families must propagate |
| RSK-001..RSK-005 | Risks | Evidence Contract limitations and EVD blocks | Contracted | Risks condition downstream recommendations |
| UNC-001..UNC-005 | Uncertainties | Evidence Contract uncertainty notes | Contracted | Must propagate downstream |

---

## Insights

| Insight ID | Contracted Statement | Evidence Links | Limitations |
|---|---|---|---|
| INS-001 | Matched evidence is concentrated in one ad reference: `120245828603090721` / `ViajeSinEstres_AlivioEmocional_ViajeSinEstres_Reel_v1`. | EVD-001, EVD-002, EVD-003 | No causal superiority or recommendation is asserted |
| INS-002 | Evidence separates a matched CAPTACION/ABO campaign/adset row from a lead-only RTG/CBO campaign/adset row. | EVD-001, EVD-004 | Does not prove spend absence outside the approved model |
| INS-003 | Spend-only evidence is small in amount but structurally important because it cannot support lead-quality ratios. | EVD-001, EVD-003 | Spend-only cost-per-lead and quality-rate statements remain UNKNOWN |

---

## Hypotheses

| Hypothesis ID | Contracted Hypothesis | Evidence Links | Validation Condition |
|---|---|---|---|
| HYP-001 | The June 2026 observed lead-quality and commercial-spend signal may be concentrated around a limited subset of matched ad references. | EVD-001, EVD-003 | Preserve as model-based concentration hypothesis, not causal explanation |
| HYP-002 | RTG lead-quality evidence should be interpreted as a distinct coverage case from matched commercial-spend efficiency evidence. | EVD-001, EVD-004 | Do not convert into campaign-level spend interpretation without source expansion |

---

## Conclusions

| Conclusion ID | Contracted Conclusion | Evidence Links | Scope Limit |
|---|---|---|---|
| CON-001 | AUC-001 has sufficient evidence to reason about ad-level lead quality and commercial spend within the corrected model. | EVD-001, EVD-002, Evidence Contract source metric links | Excludes impressions, clicks, CTR, creative asset metadata and direct campaign/adset spend attribution |
| CON-002 | Campaign/adset-level reasoning is partially supported and must remain coverage-qualified. | EVD-004, Evidence Contract limitations | No direct campaign/adset spend mapping is available in the approved model |

---

## Priorities

| Priority ID | Contracted Priority | Evidence Basis | Priority Type | Boundary |
|---|---|---|---|---|
| PRI-001 | Preserve ad-level matched evidence as the strongest reasoning base. | EVD-001, EVD-003 | Reasoning priority | Not an action priority |
| PRI-002 | Treat lead-only evidence as quality evidence without matched commercial spend. | EVD-001, EVD-004 | Reasoning priority | Do not infer absent spend behavior |
| PRI-003 | Keep campaign/adset reasoning coverage-qualified. | EVD-004, limitations | Reasoning priority | Do not infer spend attribution |
| PRI-004 | Propagate missing impressions/clicks/creative asset metadata. | Evidence Contract limitations | Reasoning priority | Do not fill evidence gaps by assumption |

---

## Risks

| Risk ID | Contracted Risk | Evidence Basis | Required Handling |
|---|---|---|---|
| RSK-001 | Treating matched spend as direct lead-level commercial classification. | Evidence Contract limitations | Preserve spend-side-only `campaign_signal` boundary |
| RSK-002 | Interpreting campaign/adset spend where metadata is absent. | EVD-004; limitations | Avoid unsupported campaign/adset spend conclusions |
| RSK-003 | Turning ad-reference concentration into creative causality. | EVD-003; creative metadata limitation | Keep reasoning at ad-reference level |
| RSK-004 | Using lead-only rows for cost-efficiency conclusions. | EVD-001; Evidence Contract limitations | Preserve `lead_only` coverage status |
| RSK-005 | Ignoring duplicate/test-record uncertainty. | Evidence Contract uncertainty notes | Keep uncertainty visible downstream |

---

## Uncertainties

| Uncertainty ID | Contracted Uncertainty | Required Handling |
|---|---|---|
| UNC-001 | Duplicate/test-record flags are not explicitly mapped. | Keep visible in downstream contracts and final output |
| UNC-002 | Spend-only campaign/adset metadata is UNKNOWN. | Do not reason about campaign/adset identity for spend-only rows |
| UNC-003 | Impressions, clicks and CTR are unavailable. | Do not create funnel-entry interpretations beyond leads and spend |
| UNC-004 | Creative asset metadata is unavailable. | Keep creative reasoning at ad reference/name level only |
| UNC-005 | `campaign_signal` is spend-side only. | Do not state that lead rows directly carry commercial signal |

---

## Evidence Links

| Knowledge Category | Evidence Source |
|---|---|
| Insights | EVD-001, EVD-002, EVD-003, EVD-004 |
| Hypotheses | EVD-001, EVD-003, EVD-004 |
| Conclusions | EVD-001, EVD-002, EVD-004, source metric links |
| Priorities | EVD blocks and Evidence Contract limitations |
| Risks | Evidence Contract limitations and uncertainty notes |
| Uncertainties | Evidence Contract uncertainty notes |

---

## Excluded Recommendations

The following are explicitly outside this Knowledge Contract:

- budget allocation actions;
- campaign or adset optimization actions;
- creative production actions;
- lead handling or sales-process actions;
- execution priorities;
- implementation plans;
- presentation-ready executive narrative.

---

## Critical Fields

| Field | Status | Notes |
|---|---|---|
| contract_id | Present | `VCA-AUC-001-KNW-001` |
| context_contract_id | Present | `VCA-AUC-001-CTX-DEF-2026-06` |
| evidence_contract_id | Present | `VCA-AUC-001-EVD-001` |
| reasoning_scope | Present | AUC-001 June 2026 evidence from `ad_quality_spend_model` |
| insights | Present | INS-001 through INS-003 |
| hypotheses | Present | HYP-001 through HYP-002 |
| conclusions | Present | CON-001 through CON-002 |
| priorities | Present | PRI-001 through PRI-004 |
| risks | Present | RSK-001 through RSK-005 |
| uncertainties | Present | UNC-001 through UNC-005 |
| evidence_links | Present | Mapped above |
| excluded_recommendations | Present | Listed above |
| transition_status | Present | T-026 ready to start |

---

## Validation Rules Applied

| Rule | Result | Evidence |
|---|---|---|
| Evidence dependency | Pass | Contract consumes `VCA-AUC-001-EVD-001` |
| Knowledge Set dependency | Pass | Contract formalizes `VCA-AUC-001-KNW-SET-001` |
| Evidence-backed reasoning | Pass | Every contracted knowledge item links to evidence or limitations |
| No new evidence | Pass | Contract does not add observations beyond T-024 |
| Correlation caution | Pass | Hypotheses are non-causal and condition-bound |
| No recommendations | Pass | No suggested action, execution plan or allocation is included |
| Uncertainty declaration | Pass | UNC-001 through UNC-005 are explicit |
| Priority traceability | Pass | Priorities are reasoning priorities with evidence basis |

---

## Transition Status

| Target | Status | Reason |
|---|---|---|
| T-025 Knowledge Contract | Completed | Knowledge Set is formalized with traceability, priorities, risks and uncertainties |
| T-026 Knowledge Set | Completed | Knowledge Set has been confirmed against this contract |
| Recommendation layer | Ready to start | Requires use of the confirmed Knowledge Set and this contract |
| Presentation layer | Not authorized | Requires downstream recommendation and presentation contracts |

---

## Traceability

- [T-025 in docs/tasks.md](../tasks.md)
- [AUC-001 Knowledge Set](auc-001-knowledge-set.md)
- [AUC-001 Evidence Contract](auc-001-evidence-contract.md)
- [AUC-001 Evidence Set](auc-001-evidence-set.md)
- [AUC-001 Analytical Contract](auc-001-analytical-contract.md)
- [VCA-KNW-001 Base Knowledge Contract](../contracts/knowledge.contract.md)
- [SPEC-001 Analytical Lifecycle](../../specs/spec-001-analytical-lifecycle.md)
- [SPEC-002 Component Boundaries](../../specs/spec-002-component-boundaries.md)
- [SPEC-004 Transversal Contracts](../../specs/spec-004-transversal-contracts.md)
- [AUC-001 Meta Lead Quality Analysis](../../analytical_use_cases/meta_lead_quality_analysis.md)
- [Meta Lead Quality Analysis Skill](../../.github/skills/meta-lead-quality-analysis/SKILL.md)

---

## Completion Statement

T-025 is complete.

The Knowledge Contract formalizes the AUC-001 Knowledge Set, preserving evidence links, non-causal hypotheses, reasoning priorities, risks, uncertainties and excluded recommendations.

T-026 has confirmed the Knowledge Set against this contract. T-027 may now begin recommendation-layer work from the confirmed Knowledge Set.