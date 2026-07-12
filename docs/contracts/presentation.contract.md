# Presentation Contract

## Metadata

| Field | Value |
|---|---|
| Contract ID | VCA-PRS-001 |
| Contract Name | Presentation Contract |
| Contract Category | Presentation Contract |
| Status | Documented |
| Version | 1.0.0 |
| Last Updated | 2026-07-12 |
| Owner | Equipo VCA |
| Source Index | [docs/contracts.md](../contracts.md) |

---

## Purpose

Delimitar el contenido aprobado que puede consumir la Presentation Layer para construir un Output Artifact.

Este contract define que conocimiento, recomendaciones, limitaciones, fuentes y trazabilidad estan autorizados para presentacion.

Este contract no crea evidencia nueva.

Este contract no introduce interpretaciones nuevas.

Este contract no reordena prioridades ni cambia recomendaciones.

---

## Producer

Framework, tras validar el contenido generado por Reasoning Layer y Recommendation Contract.

## Consumer

- Presentation Layer.
- Template Builder.
- Future Output Artifact.

## Inputs

| Input | Description | Source |
|---|---|---|
| Context Definition | Objetivo, alcance, audiencia y restricciones del artefacto | VCA-CTX-001 |
| Knowledge Set | Insights, conclusiones, incertidumbres y riesgos aprobados | VCA-KNW-001 |
| Recommendation Set | Acciones sugeridas, justificacion, prioridad y trazabilidad | VCA-REC-001 |
| Evidence References | Referencias necesarias para sostener el contenido presentado | VCA-EVD-001 |
| Limitations | UNKNOWN, pendientes, riesgos e incertidumbres que deben quedar visibles | VCA-KNW-001; VCA-REC-001 |
| Output Request | Tipo de artefacto final solicitado, sin alterar el contenido analitico | Solicitud de analisis; AUC aplicable |

## Outputs

| Output | Description |
|---|---|
| Presentation Content Scope | Contenido aprobado para ser presentado |
| Required Sections | Secciones que debe incluir el artefacto final |
| Source References | Fuentes y contracts que deben permanecer trazables |
| Approved Recommendations | Recomendaciones autorizadas para presentacion sin reordenar ni reescribir prioridades |
| Required Limitations | Limitaciones, UNKNOWN y pendientes que deben mostrarse |
| Excluded Content | Evidencia, interpretaciones o recomendaciones no aprobadas para presentacion |
| Presentation Constraints | Restricciones de formato que no pueden alterar el contenido |
| Transition Readiness | Indicacion de si el contract permite construir el Output Artifact o debe bloquearse |

## Critical Fields

| Field | Required | Description |
|---|---|---|
| contract_id | Yes | Identificador estable del contract |
| context_contract_id | Yes | Context Contract que delimita la presentacion |
| knowledge_contract_id | Yes | Knowledge Contract autorizado |
| recommendation_contract_id | Yes | Recommendation Contract autorizado |
| presentation_scope | Yes | Alcance del contenido aprobado |
| required_sections | Yes | Secciones minimas del artefacto final |
| source_references | Yes | Referencias que deben conservar trazabilidad |
| approved_recommendations | Yes | Recomendaciones autorizadas o declaracion de no disponibilidad |
| required_limitations | Yes | Limitaciones y UNKNOWN que deben quedar visibles |
| excluded_content | Yes | Contenido excluido por no estar aprobado |
| presentation_constraints | Yes | Restricciones de formato o audiencia |
| transition_status | Yes | Estado de avance hacia Output Artifact |

## Validation Rules

| Rule | Description |
|---|---|
| Recommendation dependency | No puede emitirse un Presentation Contract usable sin Recommendation Contract previo |
| Knowledge dependency | El contenido presentado debe estar respaldado por Knowledge Contract cuando incluya interpretaciones |
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
| Prioridad ambigua | Usar prioridad aprobada en Recommendation Contract o bloquear si no existe |
| Incertidumbre no visible | Bloquear salida hasta reflejarla en Required Limitations |

## Idempotency Rules

Este contract es documental y no construye el Output Artifact por si mismo.

Una instancia concreta del Presentation Contract debe autorizar el mismo contenido cuando consume el mismo Context Contract, Knowledge Contract, Recommendation Contract y Output Request declarado.

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
| AUC-001 | Analytical use case |
| meta-lead-quality-analysis | Skill |

## Evidence

- SPEC-001 define Constructor de Informes como fase final que presenta conocimiento y recomendaciones ya validados sin introducir nueva evidencia, interpretacion ni recomendaciones.
- SPEC-002 establece que Presentation Layer construye artefactos finales a partir de conocimiento ya generado y no puede crear nueva evidencia ni reinterpretar conclusiones.
- SPEC-004 reconoce el Presentation Contract como categoria fundacional para delimitar contenido aprobado para presentacion.
- AUC-001 requiere un informe ejecutivo con contexto, fuentes de evidencia, preparacion, analisis, razonamiento, recomendaciones, limitaciones y pendientes.
- La skill asociada exige que el informe incluya limitaciones y pendientes sin introducir supuestos no verificados.

## Risks

| Risk | Severity | Impact | Evidence |
|---|---|---|---|
| Presentacion crea contenido nuevo | Important | Rompe trazabilidad entre evidencia, conocimiento y salida | SPEC-001; SPEC-002 |
| Prioridades alteradas por formato | Important | Cambia el significado de recomendaciones aprobadas | SPEC-002; SPEC-004 |
| Limitaciones omitidas | Important | Puede presentar conclusiones como mas firmes de lo permitido | AUC-001; skill |
| Trazabilidad insuficiente en salida | Important | Debilita revision ejecutiva y auditoria posterior | SPEC-004; AUC-001 |

## Definition of Done

Este contract cumple T-013 cuando:

1. Delimita el contenido aprobado para Presentation Layer.
2. Declara dependencia explicita de Knowledge y Recommendation Contracts.
3. Exige conservar fuentes, limitaciones, UNKNOWN y trazabilidad.
4. Prohibe crear evidencia, reinterpretar conclusiones o alterar prioridades.
5. Define readiness para construir el Output Artifact sin sustituir el analisis.