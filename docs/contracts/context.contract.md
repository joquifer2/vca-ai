# Context Contract

## Metadata

| Campo | Valor |
|---|---|
| Contract ID | VCA-CTX-001 |
| Contract Name | Context Contract |
| Contract Category | Context Contract |
| Status | Documented |
| Version | 1.1.0 |
| Last Updated | 2026-07-13 |
| Owner | Equipo VCA |
| Source Index | [docs/contracts.md](/docs/contracts.md) |

---

## Purpose

Formalizar el objetivo, alcance, restricciones, decision soportada, fuentes oficiales y estados UNKNOWN de un analisis antes de iniciar Discovery, adquisicion de datos, preparacion, analisis, razonamiento o seleccion de proyeccion de presentacion.

Cuando la ejecucion requiera una salida de presentacion, este contract tambien debe hacer visible la canonicalizacion del alcance de ejecucion y la determinabilidad de la proyeccion de presentacion.

Este contract no define schemas tecnicos ejecutables.

Este contract no implementa integraciones productivas.

Este contract no introduce requisitos funcionales nuevos fuera de las capacidades documentales aprobadas por SPEC-010 y las decisiones arquitectonicas relacionadas.

---

## Producer

Framework.

## Consumer

- Framework / fase Discovery.
- Data Provider, cuando necesite delimitar la porcion de datos aplicable.
- Analytical Layer, cuando necesite conocer alcance y restricciones antes de preparar datos.
- Presentation Layer, solo para consumir la proyeccion seleccionada o verificar que la seleccion es determinable desde el contexto.
- Skill aplicable, cuando aporte reglas de dominio dentro del alcance aprobado.

## Inputs

| Input | Descripcion | Fuente |
|---|---|---|
| Analysis Objective | Proposito del analisis y decision a soportar | Solicitud de analisis; AUC aplicable |
| Context References | Fuentes oficiales de contexto que deben consultarse | docs/context_refs.md |
| Project Constraints | Limites del proyecto y restricciones metodologicas | project_brief.md; specs/ |
| Skill Rules | Reglas de dominio aplicables al caso | Skill aprobada, cuando aplique |
| Operational Scope | Periodo, alcance de campañas o segmentos y audiencia del informe | Solicitud de analisis; AUC aplicable |
| Output Request | Solicitud de salida, audiencia prevista y necesidad de proyeccion cuando aplique | Solicitud de analisis; AUC aplicable |

## Outputs

| Output | Descripcion |
|---|---|
| Context Definition | Objetivo, decision soportada, alcance, restricciones y supuestos declarados |
| Official Context Sources | Fuentes oficiales consultadas o requeridas |
| Applicability Statement | Declaracion de aplicabilidad del caso, skill o extension |
| Unknowns | Huecos, limitaciones o datos no disponibles marcados como UNKNOWN |
| Execution Scope Canonicalization Result | Alcance de ejecucion resuelto, distinguiendo parametros de ejecucion y parametros metodologicos heredados |
| Presentation Projection Readiness | Indicacion de si la proyeccion de presentacion es determinable, no requerida o debe bloquearse por ambiguedad |
| Transition Readiness | Indicacion de si el contract permite avanzar a Discovery o debe bloquearse |

## Critical Fields

| Campo | Obligatorio | Descripcion |
|---|---|---|
| contract_id | Yes | Identificador estable del contract |
| analysis_objective | Yes | Objetivo del analisis |
| supported_decision | Yes | Decision o lectura ejecutiva que el analisis debe soportar |
| analysis_scope | Yes | Alcance operativo: caso, periodo, fuentes o limites aplicables |
| official_context_sources | Yes | Fuentes oficiales consultadas o requeridas |
| constraints | Yes | Restricciones metodologicas, funcionales o de contexto |
| assumptions | Yes | Supuestos declarados y verificables |
| unknowns | Yes | Huecos o informacion no verificable |
| execution_scope_canonicalization | Conditional | Resultado de canonicalizacion cuando la solicitud pueda heredar, cambiar o fijar parametros de ejecucion |
| execution_parameters | Conditional | Parametros especificos de la instancia de ejecucion, como periodo, alcance operativo, filtros, audiencia o solicitud de salida |
| methodological_parameters | Conditional | Parametros heredados del AUC, Skill o specs salvo modificacion explicita compatible |
| output_request | Conditional | Solicitud de salida declarada o marcada como UNKNOWN cuando afecte a la proyeccion de presentacion |
| presentation_projection_status | Conditional | Estado de determinabilidad de la proyeccion: not_required, determined, ambiguous o blocked |
| traceability_links | Yes | Artefactos que justifican el contract |
| transition_status | Yes | Estado de avance hacia Discovery |

## Validation Rules

| Regla | Descripcion |
|---|---|
| Context before data | No puede avanzarse a Discovery o Data Provider sin objetivo, alcance y fuentes oficiales declaradas |
| No informal context | No puede completarse contexto mediante memoria informal si no existe fuente publicada |
| Unknown explicitness | La informacion ausente debe declararse como UNKNOWN o PENDING, no inferirse |
| Scope preservation | El contract no puede ampliar el alcance aprobado por Project Brief, AUC, Skill o Specs |
| Execution scope canonicalization | Cuando existan parametros variables de ejecucion, el contract debe canonicalizarlos antes de congelar el Execution Context |
| Execution parameter precedence | Los parametros de ejecucion de la solicitud actual prevalecen sobre valores heredados de ejecuciones anteriores una vez canonicalizados |
| Methodological parameter inheritance | Los parametros metodologicos se heredan del AUC, Skill o specs salvo modificacion explicita, compatible y trazable |
| Projection determinability | Si la salida requiere presentacion y la proyeccion no puede determinarse desde audiencia, proposito, decision soportada u Output Request, el flujo debe bloquearse o pedir aclaracion |
| Source traceability | Cada fuente de contexto usada debe estar enlazada a un artefacto oficial o marcada como no disponible |
| Boundary compliance | El contract no puede producir evidencia, interpretacion, conclusiones ni recomendaciones |
| Skill containment | Las reglas de dominio de una Skill solo pueden aplicarse dentro del alcance declarado |

## Traceability

- [project_brief.md](/project_brief.md)
- [docs/context_refs.md](/docs/context_refs.md)
- [specs/spec-001-analytical-lifecycle.md](/specs/spec-001-analytical-lifecycle.md)
- [specs/spec-002-component-boundaries.md](/specs/spec-002-component-boundaries.md)
- [specs/spec-004-transversal-contracts.md](/specs/spec-004-transversal-contracts.md)
- [specs/spec-010-presentation-projection-selection.md](/specs/spec-010-presentation-projection-selection.md)
- [docs/decisions/auc-001/auc-001-execution-scope-canonicalization-architectural-decision.md](/docs/decisions/auc-001/auc-001-execution-scope-canonicalization-architectural-decision.md)
- [docs/decisions/auc-001/auc-001-presentation-projection-architectural-decision.md](/docs/decisions/auc-001/auc-001-presentation-projection-architectural-decision.md)
- [docs/decisions/auc-001/auc-001-documentary-alignment-decision.md](/docs/decisions/auc-001/auc-001-documentary-alignment-decision.md)
- [analytical_use_cases/meta_lead_quality_analysis.md](/analytical_use_cases/meta_lead_quality_analysis.md)
- [.github/skills/meta-lead-quality-analysis/SKILL.md](/.github/skills/meta-lead-quality-analysis/SKILL.md)
- [gates/spec-008-development-entry-phase-gate.md](/gates/spec-008-development-entry-phase-gate.md)

## Unknown Handling

| Unknown | Tratamiento |
|---|---|
| Periodo de analisis no definido | Bloquear avance hacia Discovery hasta declararlo |
| Criterio operativo de lead de calidad no definido | Bloquear AUC-001 hasta documentar el criterio o marcarlo como insuficiente |
| Fuente oficial de contexto no disponible | Marcar PENDING y evaluar si bloquea segun el caso |
| Data Provider no disponible | No corresponde resolverlo en este contract; debe propagarse al Data Contract |
| Alcance de campañas, conjuntos o creatividades no definido | Marcar UNKNOWN y bloquear si afecta a la interpretacion |
| Output Request ambiguo | Marcar UNKNOWN y bloquear si impide determinar la proyeccion de presentacion |
| Proyeccion de presentacion no determinable | Bloquear o solicitar aclaracion antes de construir la salida |

## Idempotency Rules

Este contract es documental y no ejecuta operaciones. Su reutilizacion debe mantener el mismo contract_id para la categoria general y registrar versiones o instancias del contexto cuando un analisis concreto lo requiera.

## Dependencies

| Dependencia | Tipo |
|---|---|
| Project Brief | Source of Truth |
| Context References | Source of Truth |
| SPEC-001 | Lifecycle |
| SPEC-002 | Boundary |
| SPEC-004 | Contract framework |
| SPEC-010 | Presentation projection selection |
| VCA-AUC-001-ARCH-001 | Execution Scope Canonicalization |
| VCA-AUC-001-ARCH-002 | Presentation projection architecture |
| AUC-001 | Analytical use case |
| meta-lead-quality-analysis | Skill |

## Evidence

- SPEC-001 exige que la fase Contexto delimite objetivo, restricciones y fuentes oficiales antes de Discovery.
- SPEC-002 exige que los handoffs se materialicen en artefactos identificables y revisables.
- SPEC-004 reconoce el Context Contract como categoria fundacional y exige metadata minima.
- SPEC-010 exige que la seleccion de proyeccion se derive del Execution Context canonicalizado.
- VCA-AUC-001-ARCH-001 define Execution Scope Canonicalization como responsabilidad reusable entre solicitud humana y Execution Context.
- VCA-AUC-001-ARCH-002 establece que Presentation Layer materializa la proyeccion solicitada por el contexto, no una decision ad hoc.
- AUC-001 y la skill asociada exigen confirmar objetivo, periodo, alcance operativo, criterio de lead de calidad y fuentes oficiales antes del analisis.

## Risks

| Riesgo | Severidad | Impacto | Evidencia |
|---|---|---|---|
| Avanzar a datos sin contexto suficiente | Important | Puede producir evidencia no alineada con el objetivo | SPEC-001; AUC-001 |
| Inferir contexto no publicado | Important | Rompe trazabilidad y puede introducir supuestos no verificados | docs/context_refs.md; skill |
| Mezclar contexto con evidencia o interpretacion | Important | Rompe boundary compliance entre fases | SPEC-002; SPEC-004 |
| Omitir canonicalizacion del alcance de ejecucion | Important | Puede heredar parametros de ejecuciones anteriores sin intencion documental | VCA-AUC-001-ARCH-001 |
| Permitir proyeccion de presentacion ambigua | Important | Puede trasladar una decision de contexto a Presentation Layer | SPEC-010; VCA-AUC-001-ARCH-002 |