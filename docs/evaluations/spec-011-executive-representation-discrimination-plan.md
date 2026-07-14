# SPEC-011 Executive Representation Discrimination Plan

## Metadata

| Field | Value |
|---|---|
| Document Type | Experimental Discrimination Plan |
| Status | Draft |
| Version | 1.0.0 |
| Last Updated | 2026-07-14 |
| Owner | Equipo VCA |
| Related Specification | SPEC-011 - Communication Context Representation Transformation |
| Related Decision | VCA-AUC-001-ARCH-003 - Communication Context Representation Transformation |
| Related Contract | AUC-001 Presentation Contract |
| Related Use Case | AUC-001 - Meta Lead Quality Analysis |
| Experimental Focus | Executive representation discrimination under the current architecture |

---

## Purpose

Diseñar un experimento de discriminacion que permita determinar si las transformaciones necesarias para producir una comunicacion ejecutiva adecuada pueden explicarse completamente mediante la arquitectura vigente.

Este plan no valida una nueva capacidad.

Este plan no refuta SPEC-011 por defecto.

Este plan no modifica la arquitectura aprobada.

Este plan solo produce la evidencia necesaria para decidir si la arquitectura vigente explica completamente el comportamiento observado o si queda un residuo de responsabilidad arquitectonica que requiera analisis posterior.

---

## Evidence of Partida

| Artifact | Relevance |
|---|---|
| [SPEC-011 Communication Context Representation Transformation](../../specs/spec-011-communication-context-representation-transformation.md) | Defines the current transformation responsibility and its invariants. |
| [VCA-AUC-001-ARCH-003 Communication Context Representation Transformation](../evaluations/auc-001-communication-context-representation-transformation-architectural-decision.md) | Establishes the reusable architectural responsibility around Communication Context-driven representation. |
| [AUC-001 Presentation Contract](../handoffs/auc-001-presentation-contract.md) | Delimits the approved content and representation invariants for the selected output. |
| [AUC-001 Meta Lead Quality Analysis](../../analytical_use_cases/meta_lead_quality_analysis.md) | Provides the stabilized canonical content that must remain unchanged. |
| [Meta Lead Quality Analysis Skill](../../.github/skills/meta-lead-quality-analysis/SKILL.md) | Ensures the analytical workflow is already aligned with the case of use. |
| Current Executive Report baseline | Observed executive output that still reads as strongly analytical. |

Baseline output reference:

- [Current executive report without history](../../outputs/evaluations/auc-001-executive-lead-quality-report-to-2026-06-30-no-history-2026-07-14.md)

Observed issues in the baseline output:

- excess numerical precision;
- too many tables;
- early exposure of technical details;
- organization too close to the analytical pipeline;
- weak orientation toward decision making.

---

## Experimental Objective

Determinar si las transformaciones que resulten necesarias durante el tratamiento para convertir el contenido canónico aprobado en una comunicacion ejecutiva adecuada pueden explicarse integramente mediante la arquitectura vigente.

The question under test is not whether the current implementation is elegant.

The question under test is whether the required transformations are fully explainable as representation transformations compatible with the current architecture.

---

## Working Hypotheses

| Hypothesis ID | Hypothesis |
|---|---|
| H-1 | All transformations required to obtain an adequate executive communication can be explained by SPEC-011, ARCH-003, the Presentation Contract, and the current Communication Context. |
| H-2 | One or more required transformations cannot be explained by the current architecture and therefore reveal a residual architectural responsibility. |

The experiment does not assume either hypothesis in advance.

---

## Controlled Variables

The following variables remain fixed in both the control and treatment outputs:

- the same Execution Context canonicalizado;
- the same Selected Presentation Projection;
- the same Communication Context;
- the same Evidence Set;
- the same Knowledge Set;
- the same Recommendation Set;
- the same Presentation Contract;
- the same approved canonical content.

The only experimental variable is representation.

---

## Experimental Variable

| Variable | Description |
|---|---|
| Representation | The way the same approved canonical content is organized, condensed, worded, ordered, and made decision-oriented during the treatment for executive consumption. |

The experiment must not change the underlying content, priorities, limitations, or semantic meaning.

---

## Experimental Outputs

### Control

Representation obtained by the current implementation of SPEC-011, using the same fixed inputs and the same approved canonical content.

### Treatment

Representation built by attempting to improve executive communication of the same canonical content, while explicitly classifying each transformation applied.

The treatment must not assume that any transformation automatically belongs to SPEC-011.

---

## Classification Framework

For each transformation required by the treatment, classify it using the following categories:

| Transformation | Compatible with SPEC-011 | Dudosa | Fuera de la arquitectura vigente | Motivo | Justification |
|---|---|---|---|---|---|
| Numeric precision reduction |  |  |  |  |  |
| Table consolidation / reduction |  |  |  |  |  |
| Decision-first ordering |  |  |  |  |  |
| Technical detail deferral |  |  |  |  |  |
| Abstraction increase |  |  |  |  |  |
| Vocabulary simplification |  |  |  |  |  |
| Traceability prominence tuning |  |  |  |  |  |
| Coverage-state disclosure placement |  |  |  |  |  |
| Executive summary framing |  |  |  |  |  |

Motivo values are constrained to the following set:

- Representation;
- Communication Context;
- Presentation Contract;
- Unknown;
- Possible new responsibility.

Classification rules:

- Compatible with SPEC-011: the transformation changes representation only, preserves semantic equivalence, preserves traceability, and does not alter the approved content.
- Dudosa: the transformation may be representational, but the current evidence does not clearly show whether it belongs inside the current architectural responsibility or whether it is merely an executive convenience.
- Fuera de la arquitectura vigente: the transformation changes content, priorities, conclusions, coverage, or introduces a new representational responsibility not justified by SPEC-011, ARCH-003, the Presentation Contract, or the Communication Context.
- Motivo: the primary locus used to explain why the transformation is compatible, doubtful, or outside the current architecture.

---

## Controls for Equivalence Semantics

Both outputs must satisfy the following controls:

| Control | Requirement |
|---|---|
| Same canonical content | The control and treatment must use exactly the same approved canonical content. |
| No new evidence | Neither output may introduce new evidence blocks or new data extraction. |
| No new reasoning | Neither output may generate new reasoning, hypotheses, or conclusions. |
| No changed conclusions | The conclusions must remain the same across both outputs. |
| No priority changes | Recommendation priorities must remain unchanged. |
| No coverage changes | Coverage states must remain unchanged. |
| Decision equivalence | Both outputs must support the same business decisions with the same confidence and without hiding decision-critical information. |
| Semantic equivalence | Both outputs must preserve the approved meaning of the source content. |
| Reconstructability | Both outputs must remain reconstructible from the same source artifacts. |

If any control fails, the experiment is invalid for the purpose of discriminating representation responsibilities.

---

## Experimental Protocol

1. Capture the control output from the current SPEC-011 implementation using the fixed inputs and the approved canonical content.
2. Construct the treatment output using the same fixed inputs and the same approved canonical content.
3. For every transformation required by the treatment, record what changed and why the change was necessary.
4. Classify each transformation using the classification framework above.
5. Verify that the control and treatment preserve semantic equivalence and reconstructability.
6. Compare the control and treatment to identify which transformations are actually required for executive adequacy.
7. Determine whether those transformations are fully explainable by the current architecture or whether any residual remains outside it.

The protocol intentionally avoids assuming in advance that the current implementation is sufficient or insufficient.

---

## Candidate Transformation Families

The experiment should actively probe the following families of transformation because they are the observed pain points in the current executive output:

| Transformation Family | Experimental Purpose | Typical Discrimination Question |
|---|---|---|
| Numerical compression | Reduce unnecessary precision while preserving traceability and meaning. | Is rounding a representation choice or does it indicate a separate responsibility? |
| Tabular compression | Reduce the number of tables without losing decision-relevant content. | Is table consolidation still a representation transformation? |
| Decision-first narrative | Reorganize the output so executive implications appear before supporting detail. | Is executive ordering covered by the current architecture? |
| Technical deferral | Move technical detail later in the output or collapse it into summaries. | Is delaying technical detail only a communication-context effect? |
| Abstraction tuning | Raise or lower detail level while preserving semantic equivalence. | Does abstraction tuning remain within SPEC-011? |
| Vocabulary simplification | Replace analytical phrasing with executive phrasing without changing meaning. | Is vocabulary adaptation part of representation or a separate narrative responsibility? |
| Traceability tuning | Adjust how visibly traceability is exposed without removing it. | Is traceability prominence part of the contract or the context? |
| Coverage-state handling | Decide how matched/lead_only/spend_only should be surfaced in an executive artifact. | Is coverage presentation a contractual invariant or a contextual choice? |

---

## Classification Criteria

| Category | Criterion |
|---|---|
| Compatible with SPEC-011 | The transformation preserves semantic equivalence, keeps approved content unchanged, and can be justified as representation governed by Communication Context and ARCH-003. |
| Dudosa | The transformation appears representational, but the current evidence does not clearly show whether SPEC-011 already covers it or whether it is only an executive styling choice. |
| Fuera de la arquitectura vigente | The transformation requires changing content, meaning, priority, coverage, or a responsibility not justified by SPEC-011, ARCH-003, the Presentation Contract, or the Communication Context. |

The experiment must not classify by intuition.

The experiment must classify each transformation only after observing the treatment output and checking the control constraints.

---

## Acceptance Criteria

The experiment is successful if it produces enough evidence to answer the following question:

> Can an adequate executive communication be explained completely using only the responsibilities defined by the current architecture?

To be accepted, the experiment must:

- preserve the same canonical content in both outputs;
- preserve semantic equivalence;
- preserve traceability and coverage states;
- classify every required transformation;
- identify whether each transformation is compatible, doubtful, or outside the current architecture;
- record the motivo associated with each transformation;
- record any Observed Residual explicitly when a transformation cannot yet be justified but still preserves canonical content;
- make the decision boundaries explicit enough to support a later architectural analysis.

---

## Falsification Criteria

The experiment is falsified as a discrimination exercise if any of the following occurs:

- the treatment introduces new evidence or new reasoning;
- the treatment changes conclusions, priorities, or coverage states;
- the treatment reduces decision usefulness even if semantic equivalence is preserved;
- the treatment cannot be reconstructed from the same source artifacts;
- the required transformations cannot be classified with the available architectural references;
- the treatment still reads as analytically shaped even after all representation adjustments that can be justified by the current architecture.

---

## Possible Results

| Result | Meaning |
|---|---|
| Fully explainable by current architecture | All necessary transformations are classified as Compatible with SPEC-011 or are clearly justifiable through ARCH-003, the Presentation Contract, and the Communication Context. |
| Partially explainable | Some transformations are Compatible, some remain Dudosa, but none require a new capability; the residual may be methodological rather than architectural. |
| Observed Residual | One or more transformations cannot yet be justified by SPEC-011, ARCH-003, the Presentation Contract, or the Communication Context, but canonical content remains unchanged and the issue is recorded only as evidence for later analysis. |
| Residual architectural responsibility detected | One or more necessary transformations are consistently Fuera de la arquitectura vigente, indicating that the current responsibilities do not fully explain executive adequacy. |

---

## Conditions for Subsequent Architectural Analysis

A later architectural analysis is authorized only if the experiment produces evidence that:

- one or more necessary transformations are outside the current architecture; or
- multiple transformations remain persistently doubtful after applying the current responsibilities in good faith; or
- the treatment cannot achieve executive adequacy without introducing content-preserving behavior that is not explainable by SPEC-011, ARCH-003, the Presentation Contract, or the Communication Context.

If a transformation cannot be justified by the current architecture but does not modify the approved canonical content, it must be recorded as Observed Residual and not promoted immediately to a new architectural responsibility.

If all necessary transformations are explainable by the current architecture, no further architectural analysis is needed.

---

## Traceability

- [SPEC-011 Communication Context Representation Transformation](../../specs/spec-011-communication-context-representation-transformation.md)
- [VCA-AUC-001-ARCH-003 Communication Context Representation Transformation](auc-001-communication-context-representation-transformation-architectural-decision.md)
- [AUC-001 Presentation Contract](../handoffs/auc-001-presentation-contract.md)
- [AUC-001 Meta Lead Quality Analysis](../../analytical_use_cases/meta_lead_quality_analysis.md)
- [Meta Lead Quality Analysis Skill](../../.github/skills/meta-lead-quality-analysis/SKILL.md)
- [Current executive report without history](../../outputs/evaluations/auc-001-executive-lead-quality-report-to-2026-06-30-no-history-2026-07-14.md)

---

## Completion Statement

This plan defines a discrimination experiment to determine whether the transformations required for an adequate executive communication are fully explainable by the current architecture or whether a residual architectural responsibility remains.

It does not modify SPEC-011.

It does not introduce a new capability.

It does not pre-judge the experimental outcome.