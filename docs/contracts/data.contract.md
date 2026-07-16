# Data Contract

## Metadata

| Campo | Valor |
|---|---|
| Contract ID | VCA-DATA-001 |
| Contract Name | Data Provider Principal Contract |
| Contract Category | Data Contract |
| Status | Documented |
| Version | 1.0.0 |
| Last Updated | 2026-07-12 |
| Owner | Equipo VCA |
| Source Index | [docs/contracts.md](/docs/contracts.md) |

---

## Purpose

Formalizar la informacion minima que un Data Provider debe exponer antes de Discovery y preparacion analitica, incluyendo origen, periodo, estructura logica, metricas disponibles, limitaciones y trazabilidad.

Este contract no interpreta datos.

Este contract no calcula hallazgos.

Este contract no produce evidencia derivada, conocimiento, recomendaciones ni presentacion.

---

## Producer

Data Provider principal.

Para AUC-001, el Data Provider principal previsto es BigQuery MCP Server.

## Consumer

- Framework / fase Discovery.
- Analytical Layer.
- Future Data Contract instanciado del caso AUC-001.

## Inputs

| Input | Descripcion | Fuente |
|---|---|---|
| Context Contract | Objetivo, alcance, periodo, restricciones y fuentes oficiales requeridas | VCA-CTX-001 |
| Data Provider Identification | Identificacion del proveedor que expone la informacion | docs/context_refs.md; AUC aplicable |
| Requested Data Scope | Porcion de datos solicitada segun objetivo, periodo y alcance operativo | Context Contract; AUC aplicable |
| Access Constraints | Limitaciones de acceso, disponibilidad o permisos conocidos | Data Provider; docs/context_refs.md |
| Source Metadata | Descripcion disponible de datasets, tablas, vistas, modelos o recursos equivalentes | Data Provider |

## Outputs

| Output | Descripcion |
|---|---|
| Data Source Declaration | Fuente principal, origen y mecanismo de consulta o acceso declarado |
| Logical Structure | Descripcion no tecnica cerrada de entidades, dimensiones, metricas y granularidad disponibles |
| Data Scope | Periodo, filtros, segmentos o porcion de datos expuesta |
| Data Availability | Estado de disponibilidad de los datos solicitados |
| Data Limitations | Huecos, restricciones, sesgos, latencia, permisos o limitaciones conocidas |
| Traceability Links | Referencias hacia fuente, contexto, AUC, skill o evidencia documental aplicable |
| Transition Readiness | Indicacion de si el contract permite avanzar a Discovery o debe bloquearse |

## Critical Fields

| Campo | Obligatorio | Descripcion |
|---|---|---|
| contract_id | Yes | Identificador estable del contract |
| data_provider | Yes | Productor de la informacion |
| consumer | Yes | Componente o fase que consume el contract |
| source_reference | Yes | Fuente, dataset, tabla, vista, modelo o recurso equivalente |
| requested_scope | Yes | Alcance solicitado desde el Context Contract |
| exposed_scope | Yes | Alcance realmente expuesto por el proveedor |
| time_period | Yes | Periodo cubierto o UNKNOWN si no esta disponible |
| entities | Yes | Entidades logicas disponibles o UNKNOWN |
| dimensions | Yes | Dimensiones disponibles o UNKNOWN |
| metrics | Yes | Metricas disponibles o UNKNOWN |
| granularity | Yes | Nivel de detalle disponible o UNKNOWN |
| limitations | Yes | Limitaciones, huecos o restricciones observadas |
| traceability_links | Yes | Artefactos o fuentes que justifican el contract |
| transition_status | Yes | Estado de avance hacia Discovery |

## Validation Rules

| Regla | Descripcion |
|---|---|
| Context dependency | No puede emitirse un Data Contract usable sin Context Contract previo |
| Provider boundary | El Data Provider no puede emitir insights, hipotesis, conclusiones ni recomendaciones |
| Scope alignment | El alcance expuesto debe corresponderse con el alcance solicitado o declarar divergencias |
| Source declaration | La fuente debe estar identificada de forma suficiente o marcarse como UNKNOWN/PENDING |
| Limitation visibility | Toda limitacion conocida debe documentarse antes de Discovery |
| No inferred schema | La estructura logica no debe inventar campos, metricas o entidades no publicados por la fuente |
| Transition blocking | Si faltan fuente, periodo o metricas minimas, el avance a Discovery debe bloquearse o marcarse incompleto |

## Traceability

- [project_brief.md](/project_brief.md)
- [docs/context_refs.md](/docs/context_refs.md)
- [specs/spec-001-analytical-lifecycle.md](/specs/spec-001-analytical-lifecycle.md)
- [specs/spec-002-component-boundaries.md](/specs/spec-002-component-boundaries.md)
- [specs/spec-004-transversal-contracts.md](/specs/spec-004-transversal-contracts.md)
- [analytical_use_cases/meta_lead_quality_analysis.md](/analytical_use_cases/meta_lead_quality_analysis.md)
- [.github/skills/meta-lead-quality-analysis/SKILL.md](/.github/skills/meta-lead-quality-analysis/SKILL.md)
- [gates/spec-008-development-entry-phase-gate.md](/gates/spec-008-development-entry-phase-gate.md)

## Unknown Handling

| Unknown | Tratamiento |
|---|---|
| Data Provider principal no disponible | Bloquear avance hacia Discovery operativo y registrar limitacion |
| Fuente, dataset o recurso no identificado | Marcar UNKNOWN/PENDING y no completar estructura por inferencia |
| Periodo no disponible | Bloquear si el analisis requiere comparacion temporal o trazabilidad por periodo |
| Metricas minimas no disponibles | Bloquear o declarar insuficiencia segun AUC aplicable |
| Granularidad no declarada | Marcar UNKNOWN y propagar a Discovery como limitacion |
| Restricciones de acceso no verificadas | Marcar PENDING y evitar asumir disponibilidad |

## Idempotency Rules

Este contract es documental y no ejecuta consultas. Una instancia concreta del Data Contract debe poder repetirse con el mismo Context Contract y la misma fuente sin cambiar el significado del alcance solicitado.

## Dependencies

| Dependencia | Tipo |
|---|---|
| VCA-CTX-001 | Context Contract |
| Project Brief | Source of Truth |
| Context References | Source of Truth |
| SPEC-001 | Lifecycle |
| SPEC-002 | Boundary |
| SPEC-004 | Contract framework |
| AUC-001 | Analytical use case |
| meta-lead-quality-analysis | Skill |
| BigQuery MCP Server | Data Provider principal previsto |

## Evidence

- SPEC-001 exige identificar datasets, entidades, dimensiones, metricas, relaciones y limitaciones antes de la preparacion.
- SPEC-002 establece que el Data Provider adquiere y expone informacion sin interpretar datos ni formular recomendaciones.
- SPEC-004 reconoce el Data Contract como categoria fundacional y exige metadata minima.
- AUC-001 identifica BigQuery MCP Server como Data Provider principal para volumen, calidad, eficiencia, campanas, creatividades y segmentacion.
- La skill asociada prioriza BigQuery MCP Server como fuente principal de evidencia cuando existan datos disponibles.

## Risks

| Riesgo | Severidad | Impacto | Evidencia |
|---|---|---|---|
| Data Provider emite interpretacion | Important | Rompe separacion entre adquisicion y razonamiento | SPEC-002 |
| Fuente principal no disponible | Important | Impide reunir evidencia minima verificable | AUC-001; skill |
| Estructura logica incompleta | Important | Debilita Discovery y preparacion analitica | SPEC-001 |
| Asumir campos no publicados | Important | Introduce evidencia no verificable | SPEC-004; skill |
