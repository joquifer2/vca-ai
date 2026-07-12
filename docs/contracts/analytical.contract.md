# Analytical Contract

## Metadata

| Field | Value |
|---|---|
| Contract ID | VCA-ANL-001 |
| Contract Name | Analytical Contract |
| Contract Category | Analytical Contract |
| Status | Documented |
| Version | 1.0.0 |
| Last Updated | 2026-07-12 |
| Owner | Equipo VCA |
| Source Index | [docs/contracts.md](../contracts.md) |

---

## Purpose

Formalizar el Analytical Model producido durante la fase de Preparacion.

Este contract describe el modelo preparado, las transformaciones relevantes, validaciones minimas, criterios de suficiencia y limitaciones que condicionan el analisis posterior.

Este contract no produce hallazgos observables.

Este contract no interpreta resultados.

Este contract no formula conclusiones ni recomendaciones.

---

## Producer

Analytical Layer / fase Preparacion.

## Consumer

- Analytical Layer / fase Analisis.
- Future Evidence Contract.
- Framework, para validar readiness metodologica antes de Analisis.

## Inputs

| Input | Description | Source |
|---|---|---|
| Context Definition | Objetivo, alcance, restricciones y periodo | VCA-CTX-001 |
| Data Source Declaration | Fuente, disponibilidad y alcance expuesto | VCA-DATA-001 |
| Discovery Model | Entidades, dimensiones, metricas, relaciones, granularidad y limitaciones | VCA-DISC-001 |
| Preparation Requirements | Necesidades de consolidacion, normalizacion o derivacion permitidas por el objetivo | AUC aplicable; Skill aprobada |
| Discovery Limitations | Restricciones que deben preservarse durante la preparacion | VCA-DISC-001 |

## Outputs

| Output | Description |
|---|---|
| Analytical Model | Modelo preparado, coherente e interpretable para producir evidencia |
| Included Entities | Entidades incluidas en el modelo preparado |
| Included Dimensions | Dimensiones disponibles para analisis |
| Included Metrics | Metricas disponibles para analisis |
| Transformations | Transformaciones relevantes aplicadas o declaradas como no aplicadas |
| Validation Summary | Validaciones minimas de integridad, coherencia y suficiencia |
| Preparation Limitations | Limitaciones que deben propagarse a Analisis |
| Transition Readiness | Indicacion de si el contract permite avanzar a Analisis o debe bloquearse |

## Critical Fields

| Field | Required | Description |
|---|---|---|
| contract_id | Yes | Identificador estable del contract |
| context_contract_id | Yes | Context Contract que delimita el modelo preparado |
| data_contract_id | Yes | Data Contract usado como fuente |
| discovery_contract_id | Yes | Discovery Contract usado como entrada |
| analytical_scope | Yes | Porcion preparada para analisis |
| included_entities | Yes | Entidades incluidas o UNKNOWN |
| included_dimensions | Yes | Dimensiones incluidas o UNKNOWN |
| included_metrics | Yes | Metricas incluidas o UNKNOWN |
| transformations | Yes | Transformaciones relevantes, no aplicadas o UNKNOWN |
| validation_summary | Yes | Validaciones minimas ejecutadas o pendientes |
| limitations | Yes | Limitaciones que afectan Analisis |
| traceability_links | Yes | Artefactos o fuentes que justifican el contract |
| transition_status | Yes | Estado de avance hacia Analisis |

## Validation Rules

| Rule | Description |
|---|---|
| Discovery dependency | No puede emitirse un Analytical Contract usable sin Discovery Contract previo |
| Preparation only | El contract solo puede describir preparacion, estructura y validaciones del modelo |
| No evidence | El contract no puede convertir datos preparados en hallazgos observables |
| No reasoning | El contract no puede producir insights, hipotesis, conclusiones ni recomendaciones |
| Transformation traceability | Toda transformacion relevante debe quedar declarada y trazada a la necesidad analitica |
| Validation visibility | Integridad, coherencia y suficiencia minima deben declararse antes de Analisis |
| Limitation propagation | Toda limitacion de Discovery o Preparacion debe propagarse hacia Analisis |
| Unknown explicitness | Campos, transformaciones o validaciones no verificadas deben marcarse UNKNOWN o PENDING |

## Traceability

- [project_brief.md](../../project_brief.md)
- [docs/context_refs.md](../context_refs.md)
- [docs/contracts.md](../contracts.md)
- [docs/contracts/context.contract.md](context.contract.md)
- [docs/contracts/data.contract.md](data.contract.md)
- [docs/contracts/discovery.contract.md](discovery.contract.md)
- [specs/spec-001-analytical-lifecycle.md](../../specs/spec-001-analytical-lifecycle.md)
- [specs/spec-002-component-boundaries.md](../../specs/spec-002-component-boundaries.md)
- [specs/spec-004-transversal-contracts.md](../../specs/spec-004-transversal-contracts.md)
- [analytical_use_cases/meta_lead_quality_analysis.md](../../analytical_use_cases/meta_lead_quality_analysis.md)
- [.github/skills/meta-lead-quality-analysis/SKILL.md](../../.github/skills/meta-lead-quality-analysis/SKILL.md)
- [gates/spec-008-development-entry-phase-gate.md](../../gates/spec-008-development-entry-phase-gate.md)

## Unknown Handling

| Unknown | Handling |
|---|---|
| Modelo analitico no derivable desde Discovery | Bloquear Analisis hasta resolver Discovery o Data Contract |
| Transformaciones no documentadas | Marcar PENDING y bloquear si afectan interpretacion posterior |
| Validaciones minimas no realizadas | Bloquear avance a Analisis o declarar insuficiencia explicita |
| Metricas incluidas no verificadas | Marcar UNKNOWN y excluir de Evidence Set hasta validacion |
| Dimensiones insuficientes | Propagar limitacion a Analisis y a segmentaciones posteriores |
| Inconsistencias entre Discovery y Preparacion | Bloquear hasta corregir o documentar la divergencia |

## Idempotency Rules

Este contract es documental y no ejecuta transformaciones.

Una instancia concreta del Analytical Contract debe describir de forma estable el mismo Analytical Model cuando consume el mismo Context Contract, Data Contract, Discovery Contract y reglas de preparacion declaradas.

## Dependencies

| Dependency | Type |
|---|---|
| VCA-CTX-001 | Context Contract |
| VCA-DATA-001 | Data Contract |
| VCA-DISC-001 | Discovery Contract |
| Project Brief | Source of Truth |
| Context References | Source of Truth |
| SPEC-001 | Lifecycle |
| SPEC-002 | Boundary |
| SPEC-004 | Contract framework |
| AUC-001 | Analytical use case |
| meta-lead-quality-analysis | Skill |

## Evidence

- SPEC-001 define Preparacion como la fase que transforma datos identificados en un modelo analitico coherente y apto para producir evidencia.
- SPEC-002 establece que la Analytical Layer prepara datos y produce evidencia observable, pero no introduce conclusiones de negocio ni recomendaciones.
- SPEC-004 reconoce el Analytical Contract como categoria fundacional para formalizar el Analytical Model resultante de la preparacion.
- AUC-001 requiere preparar evidencia de volumen, conversiones, coste, campanas, creatividades, calidad y segmentacion antes del razonamiento.
- La skill asociada exige separar preparacion de datos, analisis, razonamiento y recomendaciones.

## Risks

| Risk | Severity | Impact | Evidence |
|---|---|---|---|
| Preparacion no trazada | Important | Debilita la auditabilidad del Evidence Set | SPEC-001; SPEC-004 |
| Analytical Contract convertido en evidencia | Important | Mezcla Preparacion con Analisis | SPEC-001; SPEC-002 |
| Transformaciones no declaradas | Important | Puede alterar interpretacion posterior sin trazabilidad | SPEC-001 |
| Validaciones insuficientes | Important | Puede producir evidencia sobre un modelo no confiable | SPEC-001; AUC-001 |

## Definition of Done

Este contract cumple T-009 cuando:

1. Formaliza el Analytical Model preparado.
2. Declara transformaciones relevantes, validaciones minimas y limitaciones.
3. Declara dependencia explicita de Context, Data y Discovery Contracts.
4. Preserva la separacion entre Preparacion, Analisis y Razonamiento.
5. Propaga UNKNOWN y limitaciones sin producir evidencia ni interpretacion.