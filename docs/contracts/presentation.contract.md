# Presentation Contract

## Metadata

| Field | Value |
|---|---|
| Contract ID | VCA-PRS-001 |
| Contract Name | Presentation Contract |
| Contract Category | Presentation Contract |
| Status | Documented |
| Version | 1.1.0 |
| Last Updated | 2026-07-13 |
| Owner | Equipo VCA |
| Source Index | [docs/contracts.md](../contracts.md) |

---

## Purpose

Delimitar el contenido aprobado que puede consumir la Presentation Layer para construir la proyeccion de presentacion seleccionada o el Traceable Output autorizado.

Este contract define que conocimiento, recomendaciones, limitaciones, fuentes, trazabilidad y restricciones de proyeccion estan autorizados para presentacion.

Este contract no selecciona la proyeccion por conveniencia narrativa; la proyeccion debe provenir del Context Contract o Execution Context canonicalizado.

Este contract no crea evidencia nueva.

Este contract no introduce interpretaciones nuevas.

Este contract no reordena prioridades ni cambia recomendaciones.

---

## Producer

Framework, tras validar el contenido generado por Reasoning Layer y Recommendation Contract, y una vez que la proyeccion de presentacion sea determinable desde el contexto.

## Consumer

- Presentation Layer.
- Analytical Projection, cuando sea la proyeccion seleccionada.
- Executive Report, cuando sea la proyeccion seleccionada.
- Template Builder.
- Future Traceable Output.

## Inputs

| Input | Description | Source |
|---|---|---|
| Context Definition | Objetivo, alcance, audiencia y restricciones del artefacto | VCA-CTX-001 |
| Presentation Projection Readiness | Estado de determinabilidad de la proyeccion y, cuando aplique, proyeccion seleccionada | VCA-CTX-001; Execution Context |
| Knowledge Set | Insights, conclusiones, incertidumbres y riesgos aprobados | VCA-KNW-001 |
| Recommendation Set | Acciones sugeridas, justificacion, prioridad y trazabilidad | VCA-REC-001 |
| Evidence References | Referencias necesarias para sostener el contenido presentado | VCA-EVD-001 |
| Limitations | UNKNOWN, pendientes, riesgos e incertidumbres que deben quedar visibles | VCA-KNW-001; VCA-REC-001 |
| Output Request | Tipo de salida o proyeccion solicitada, sin alterar el contenido analitico | Solicitud de analisis; AUC aplicable; VCA-CTX-001 |

## Outputs

| Output | Description |
|---|---|
| Presentation Mode | Modo autorizado de salida: Analytical, Executive o not_applicable segun el contexto |
| Selected Presentation Projection | Proyeccion materializable por Presentation Layer segun el contexto canonicalizado |
| Presentation Content Scope | Contenido aprobado para ser presentado |
| Required Sections | Secciones que debe incluir el artefacto final |
| Source References | Fuentes y contracts que deben permanecer trazables |
| Approved Recommendations | Recomendaciones autorizadas para presentacion sin reordenar ni reescribir prioridades |
| Required Limitations | Limitaciones, UNKNOWN y pendientes que deben mostrarse |
| Excluded Content | Evidencia, interpretaciones o recomendaciones no aprobadas para presentacion |
| Presentation Constraints | Restricciones de formato, audiencia y proyeccion que no pueden alterar el contenido |
| Boundary Status | Indicacion de que no se introdujo nueva evidencia, interpretacion ni priorizacion |
| Transition Readiness | Indicacion de si el contract permite construir la proyeccion seleccionada o debe bloquearse |

## Critical Fields

| Field | Required | Description |
|---|---|---|
| contract_id | Yes | Identificador estable del contract |
| context_contract_id | Yes | Context Contract que delimita la presentacion |
| knowledge_contract_id | Yes | Knowledge Contract autorizado |
| recommendation_contract_id | Yes | Recommendation Contract autorizado |
| presentation_mode | Conditional | Modo de salida autorizado cuando la ejecucion requiere proyeccion de presentacion |
| selected_presentation_projection | Conditional | Proyeccion seleccionada desde el Context Contract o Execution Context canonicalizado |
| presentation_scope | Yes | Alcance del contenido aprobado |
| required_sections | Yes | Secciones minimas del artefacto final |
| source_references | Yes | Referencias que deben conservar trazabilidad |
| approved_recommendations | Yes | Recomendaciones autorizadas o declaracion de no disponibilidad |
| required_limitations | Yes | Limitaciones y UNKNOWN que deben quedar visibles |
| excluded_content | Yes | Contenido excluido por no estar aprobado |
| presentation_constraints | Yes | Restricciones de formato, audiencia o proyeccion |
| boundary_status | Yes | Confirmacion de que no se crea evidencia, interpretacion ni priorizacion nueva |
| transition_status | Yes | Estado de avance hacia la proyeccion seleccionada o Traceable Output |

## Validation Rules

| Rule | Description |
|---|---|
| Recommendation dependency | No puede emitirse un Presentation Contract usable sin Recommendation Contract previo |
| Knowledge dependency | El contenido presentado debe estar respaldado por Knowledge Contract cuando incluya interpretaciones |
| Projection selection dependency | Cuando la ejecucion requiera presentacion, la proyeccion debe venir determinada por el Context Contract o Execution Context canonicalizado |
| Single selected projection | Presentation Layer debe materializar unicamente la proyeccion seleccionada para la ejecucion concreta |
| Sibling projection preservation | Analytical Projection y Executive Report son representaciones hermanas del mismo contenido canonico aprobado, no pasos secuenciales |
| No projection derivation | Ninguna proyeccion puede derivarse de otra proyeccion; ambas deben consumir el contenido aprobado desde los contracts fuente |
| Projection ambiguity blocks | Si la proyeccion requerida no es determinable, debe bloquearse la salida o solicitar aclaracion antes de presentarla |
| No new evidence | Presentation no puede crear evidencia nueva |
| No reinterpretation | Presentation no puede reinterpretar conclusiones, riesgos o incertidumbres |
| No priority rewrite | Presentation no puede alterar la prioridad de recomendaciones aprobadas |
| Limitation visibility | Limitaciones, UNKNOWN y pendientes materiales deben permanecer visibles |
| Traceability preservation | El artefacto final debe conservar referencias suficientes hacia contracts fuente |
| Format containment | Cambios de formato no pueden alterar significado, alcance ni prioridad |

## Traceability

- [project_brief.md](../../project_brief.md)
- [docs/context_refs.md](../context_refs.md)
- [docs/contracts.md](../contracts.md)
- [docs/contracts/context.contract.md](context.contract.md)
- [docs/contracts/evidence.contract.md](evidence.contract.md)
- [docs/contracts/knowledge.contract.md](knowledge.contract.md)
- [docs/contracts/recommendation.contract.md](recommendation.contract.md)
- [specs/spec-001-analytical-lifecycle.md](../../specs/spec-001-analytical-lifecycle.md)
- [specs/spec-002-component-boundaries.md](../../specs/spec-002-component-boundaries.md)
- [specs/spec-004-transversal-contracts.md](../../specs/spec-004-transversal-contracts.md)
- [specs/spec-010-presentation-projection-selection.md](../../specs/spec-010-presentation-projection-selection.md)
- [docs/evaluations/auc-001-presentation-projection-architectural-decision.md](../evaluations/auc-001-presentation-projection-architectural-decision.md)
- [docs/evaluations/auc-001-documentary-alignment-decision.md](../evaluations/auc-001-documentary-alignment-decision.md)
- [analytical_use_cases/meta_lead_quality_analysis.md](../../analytical_use_cases/meta_lead_quality_analysis.md)
- [.github/skills/meta-lead-quality-analysis/SKILL.md](../../.github/skills/meta-lead-quality-analysis/SKILL.md)
- [gates/spec-008-development-entry-phase-gate.md](../../gates/spec-008-development-entry-phase-gate.md)

## Unknown Handling

| Unknown | Handling |
|---|---|
| Recomendacion no aprobada | Excluir de presentacion o marcar como no disponible |
| Limitacion material ausente | Bloquear construccion del Output Artifact hasta incorporarla |
| Fuente de evidencia no trazable | Bloquear o marcar insuficiencia explicita |
| Audiencia o formato no definido | Marcar PENDING; no alterar contenido para compensarlo |
| Proyeccion de presentacion no definida | Bloquear o solicitar aclaracion antes de construir la salida |
| Conflicto entre Output Request y contexto canonicalizado | Bloquear hasta resolver la inconsistencia en Context Contract o Execution Context |
| Prioridad ambigua | Usar prioridad aprobada en Recommendation Contract o bloquear si no existe |
| Incertidumbre no visible | Bloquear salida hasta reflejarla en Required Limitations |

## Idempotency Rules

Este contract es documental y no construye el Output Artifact por si mismo.

Una instancia concreta del Presentation Contract debe autorizar el mismo contenido cuando consume el mismo Context Contract, Knowledge Contract, Recommendation Contract y Output Request declarado.

Cuando consuma la misma proyeccion seleccionada y el mismo contenido canonico aprobado, debe producir el mismo alcance autorizado aunque cambie el formato de presentacion.

## Dependencies

| Dependency | Type |
|---|---|
| VCA-CTX-001 | Context Contract |
| VCA-KNW-001 | Knowledge Contract |
| VCA-REC-001 | Recommendation Contract |
| Project Brief | Source of Truth |
| Context References | Source of Truth |
| SPEC-001 | Lifecycle |
| SPEC-002 | Boundary |
| SPEC-004 | Contract framework |
| SPEC-010 | Presentation projection selection |
| VCA-AUC-001-ARCH-002 | Presentation projection architecture |
| AUC-001 | Analytical use case |
| meta-lead-quality-analysis | Skill |

## Evidence

- SPEC-001 define Constructor de Informes como fase final que presenta conocimiento y recomendaciones ya validados sin introducir nueva evidencia, interpretacion ni recomendaciones.
- SPEC-002 establece que Presentation Layer construye artefactos finales a partir de conocimiento ya generado y no puede crear nueva evidencia ni reinterpretar conclusiones.
- SPEC-004 reconoce el Presentation Contract como categoria fundacional para delimitar contenido aprobado para presentacion.
- SPEC-010 exige distinguir entre proyeccion analitica y proyeccion ejecutiva, seleccionadas desde el Execution Context canonicalizado.
- VCA-AUC-001-ARCH-002 define que la proyeccion analitica y el Executive Report son representaciones paralelas del mismo contenido validado y no se derivan entre si.
- AUC-001 requiere un informe ejecutivo con contexto, fuentes de evidencia, preparacion, analisis, razonamiento, recomendaciones, limitaciones y pendientes.
- La skill asociada exige que el informe incluya limitaciones y pendientes sin introducir supuestos no verificados.

## Risks

| Risk | Severity | Impact | Evidence |
|---|---|---|---|
| Presentacion crea contenido nuevo | Important | Rompe trazabilidad entre evidencia, conocimiento y salida | SPEC-001; SPEC-002 |
| Prioridades alteradas por formato | Important | Cambia el significado de recomendaciones aprobadas | SPEC-002; SPEC-004 |
| Limitaciones omitidas | Important | Puede presentar conclusiones como mas firmes de lo permitido | AUC-001; skill |
| Trazabilidad insuficiente en salida | Important | Debilita revision ejecutiva y auditoria posterior | SPEC-004; AUC-001 |
| Presentation Layer selecciona proyeccion ad hoc | Important | Rompe dependencia con Execution Context canonicalizado | SPEC-010 |
| Executive Report deriva de una proyeccion analitica | Important | Introduce acoplamiento secuencial y riesgo de divergencia semantica | VCA-AUC-001-ARCH-002 |

## Definition of Done

Este contract cumple T-013 y queda alineado con T-044 cuando:

1. Delimita el contenido aprobado para Presentation Layer.
2. Declara dependencia explicita de Knowledge y Recommendation Contracts.
3. Exige conservar fuentes, limitaciones, UNKNOWN y trazabilidad.
4. Prohibe crear evidencia, reinterpretar conclusiones o alterar prioridades.
5. Define readiness para construir la proyeccion seleccionada o Traceable Output sin sustituir el analisis.
6. Exige que la proyeccion de presentacion sea determinada por el contexto canonicalizado cuando aplique.
7. Preserva que Analytical Projection y Executive Report sean representaciones hermanas del mismo contenido aprobado.