# Recommendation Contract

## Metadata

| Field | Value |
|---|---|
| Contract ID | VCA-REC-001 |
| Contract Name | Recommendation Contract |
| Contract Category | Recommendation Contract |
| Status | Documented |
| Version | 1.0.0 |
| Last Updated | 2026-07-12 |
| Owner | Equipo VCA |
| Source Index | [docs/contracts.md](../contracts.md) |

---

## Purpose

Formalizar el Recommendation Set producido durante la fase de Recomendaciones.

Este contract convierte conocimiento trazable en acciones sugeridas, justificadas, priorizadas y evaluables.

Cada recomendacion debe conservar relacion explicita con insights, conclusiones, riesgos, incertidumbres o evidencia del Knowledge Contract.

Este contract no crea evidencia nueva.

Este contract no reescribe conclusiones.

Este contract no construye el artefacto final de presentacion.

---

## Producer

Reasoning Layer / fase Recomendaciones.

## Consumer

- Framework, para validar readiness antes de presentacion.
- Presentation Layer, mediante futuro Presentation Contract.
- Future Presentation Contract.

## Inputs

| Input | Description | Source |
|---|---|---|
| Context Definition | Objetivo, alcance, restricciones y decision soportada | VCA-CTX-001 |
| Knowledge Set | Insights, hipotesis, conclusiones, prioridades, riesgos e incertidumbres | VCA-KNW-001 |
| Knowledge Traceability | Vinculo entre conocimiento y evidencia | VCA-KNW-001 |
| Uncertainties | UNKNOWN, limitaciones o incertidumbres materiales | VCA-KNW-001 |
| Skill Rules | Criterios de dominio para formular acciones dentro del alcance aprobado | Skill aprobada, cuando aplique |

## Outputs

| Output | Description |
|---|---|
| Recommendation Set | Conjunto de acciones sugeridas, priorizadas y trazables |
| Suggested Actions | Acciones concretas sugeridas dentro del alcance aprobado |
| Justification | Razon por la que cada accion deriva del conocimiento disponible |
| Priority | Orden relativo de ejecucion, importancia o urgencia |
| Expected Impact | Impacto esperado expresado de forma cualitativa o segun criterio disponible |
| Effort Estimate | Esfuerzo relativo o UNKNOWN cuando no pueda verificarse |
| Dependencies | Dependencias, prerequisitos o validaciones necesarias |
| Risks | Riesgos de ejecucion, interpretacion o evidencia asociados a la accion |
| Confidence | Nivel de confianza o condicion de incertidumbre declarada |
| Traceability | Vinculo con Knowledge Contract, Evidence Contract o limitaciones relevantes |
| Transition Readiness | Indicacion de si el contract permite avanzar a Presentacion o debe bloquearse |

## Critical Fields

| Field | Required | Description |
|---|---|---|
| contract_id | Yes | Identificador estable del contract |
| context_contract_id | Yes | Context Contract que delimita las recomendaciones |
| knowledge_contract_id | Yes | Knowledge Contract usado como base |
| recommendation_scope | Yes | Porcion de conocimiento convertida en acciones sugeridas |
| suggested_actions | Yes | Acciones sugeridas o declaracion de no disponibilidad |
| justification | Yes | Justificacion trazada a conocimiento y evidencia |
| priority | Yes | Prioridad o criterio de no aplicacion |
| expected_impact | Yes | Impacto esperado o UNKNOWN |
| effort | Yes | Esfuerzo estimado o UNKNOWN |
| dependencies | Yes | Dependencias y prerequisitos |
| risks | Yes | Riesgos asociados |
| confidence | Yes | Confianza, incertidumbre o limitacion declarada |
| traceability_links | Yes | Artefactos o fuentes que justifican el contract |
| transition_status | Yes | Estado de avance hacia Presentacion |

## Validation Rules

| Rule | Description |
|---|---|
| Knowledge dependency | No puede emitirse un Recommendation Contract usable sin Knowledge Contract previo |
| Action traceability | Toda accion sugerida debe enlazarse a insight, conclusion, riesgo u oportunidad identificable |
| Justification required | Toda recomendacion debe explicar por que se sugiere |
| Priority required | Toda recomendacion debe declarar prioridad o motivo de no priorizacion |
| Uncertainty propagation | Incertidumbres materiales del Knowledge Contract deben mantenerse visibles |
| No new evidence | El contract no puede crear evidencia nueva ni alterar hallazgos o conclusiones |
| No presentation rewrite | El contract no puede transformar recomendaciones en artefacto final ni cambiar formato de salida |
| Scope alignment | Las recomendaciones deben permanecer dentro del alcance definido por Context y Knowledge Contracts |

## Traceability

- [project_brief.md](../../project_brief.md)
- [docs/context_refs.md](../context_refs.md)
- [docs/contracts.md](../contracts.md)
- [docs/contracts/context.contract.md](context.contract.md)
- [docs/contracts/evidence.contract.md](evidence.contract.md)
- [docs/contracts/knowledge.contract.md](knowledge.contract.md)
- [specs/spec-001-analytical-lifecycle.md](../../specs/spec-001-analytical-lifecycle.md)
- [specs/spec-002-component-boundaries.md](../../specs/spec-002-component-boundaries.md)
- [specs/spec-004-transversal-contracts.md](../../specs/spec-004-transversal-contracts.md)
- [analytical_use_cases/meta_lead_quality_analysis.md](../../analytical_use_cases/meta_lead_quality_analysis.md)
- [.github/skills/meta-lead-quality-analysis/SKILL.md](../../.github/skills/meta-lead-quality-analysis/SKILL.md)
- [gates/spec-008-development-entry-phase-gate.md](../../gates/spec-008-development-entry-phase-gate.md)

## Unknown Handling

| Unknown | Handling |
|---|---|
| Accion sin conocimiento trazable | Excluir o marcar UNKNOWN; no puede pasar a Presentation |
| Impacto esperado no verificable | Marcar UNKNOWN y declarar condicion de validacion posterior |
| Esfuerzo no verificable | Marcar UNKNOWN sin inventar estimacion |
| Dependencia no identificada | Marcar PENDING y propagar a Presentation Contract |
| Riesgo material no resuelto | Mantener visible y condicionar prioridad o confianza |
| Incertidumbre de evidencia | Propagar desde Knowledge Contract y evitar recomendacion concluyente |

## Idempotency Rules

Este contract es documental y no ejecuta acciones.

Una instancia concreta del Recommendation Contract debe describir de forma estable el mismo Recommendation Set cuando consume el mismo Context Contract, Knowledge Contract, Skill Rules y criterios de priorizacion declarados.

## Dependencies

| Dependency | Type |
|---|---|
| VCA-CTX-001 | Context Contract |
| VCA-KNW-001 | Knowledge Contract |
| Project Brief | Source of Truth |
| Context References | Source of Truth |
| SPEC-001 | Lifecycle |
| SPEC-002 | Boundary |
| SPEC-004 | Contract framework |
| AUC-001 | Analytical use case |
| meta-lead-quality-analysis | Skill |

## Evidence

- SPEC-001 define Recomendaciones como la fase que convierte conocimiento priorizado en acciones sugeridas, justificadas y evaluables.
- SPEC-002 establece que Reasoning Layer produce conocimiento accionable y que Presentation Layer no debe crear nueva evidencia ni reinterpretar conclusiones.
- SPEC-004 reconoce el Recommendation Contract como categoria fundacional para formalizar acciones sugeridas y su justificacion.
- AUC-001 requiere recomendaciones accionables y priorizadas.
- La skill asociada exige recomendaciones concretas, justificadas y alineadas con el contexto de negocio de VCA.

## Risks

| Risk | Severity | Impact | Evidence |
|---|---|---|---|
| Recomendacion sin trazabilidad | Important | Debilita confiabilidad y revision posterior | SPEC-001; SPEC-004 |
| Accion sugerida fuera de alcance | Important | Introduce decision funcional no aprobada | Project Brief; AUC-001 |
| Impacto o esfuerzo inventado | Important | Puede inducir decisiones no sustentadas | Skill; SPEC-001 |
| Recomendacion concluyente con incertidumbre material | Important | Oculta limites de evidencia y razonamiento | VCA-KNW-001; AUC-001 |

## Definition of Done

Este contract cumple T-012 cuando:

1. Formaliza acciones sugeridas, justificacion, prioridad, impacto, esfuerzo, dependencias, riesgos y confianza.
2. Declara dependencia explicita del Knowledge Contract.
3. Mantiene trazabilidad entre recomendaciones, conocimiento y evidencia.
4. Propaga incertidumbres y UNKNOWN sin inventar impacto, esfuerzo o dependencias.
5. No crea evidencia nueva ni construye el artefacto final de presentacion.