# Evidence Contract

## Metadata

| Field | Value |
|---|---|
| Contract ID | VCA-EVD-001 |
| Contract Name | Evidence Contract |
| Contract Category | Evidence Contract |
| Status | Documented |
| Version | 1.0.0 |
| Last Updated | 2026-07-12 |
| Owner | Equipo VCA |
| Source Index | [docs/contracts.md](/docs/contracts.md) |

---

## Purpose

Formalizar el Evidence Set producido durante la fase de Analisis.

Este contract estructura hallazgos observables y evidencia derivada a partir del Analytical Model, manteniendolos separados de interpretaciones, insights, hipotesis, conclusiones y recomendaciones.

Este contract no razona sobre causas.

Este contract no prioriza oportunidades.

Este contract no formula acciones sugeridas.

---

## Producer

Analytical Layer / fase Analisis.

## Consumer

- Reasoning Layer.
- Future Knowledge Contract.
- Framework, para validar suficiencia de evidencia antes de Razonamiento.

## Inputs

| Input | Description | Source |
|---|---|---|
| Context Definition | Objetivo, alcance, restricciones y periodo | VCA-CTX-001 |
| Analytical Model | Modelo preparado, transformaciones y validaciones minimas | VCA-ANL-001 |
| Included Metrics | Metricas disponibles para producir evidencia observable | VCA-ANL-001 |
| Preparation Limitations | Limitaciones heredadas de Preparacion | VCA-ANL-001 |
| Skill Rules | Reglas de dominio que ayudan a clasificar evidencia sin convertirla en razonamiento | Skill aprobada, cuando aplique |

## Outputs

| Output | Description |
|---|---|
| Evidence Set | Conjunto de hallazgos observables y evidencia derivada |
| Observable Findings | Hechos observables producidos desde el Analytical Model |
| Derived Evidence | Calculos, comparaciones, distribuciones o patrones derivados del modelo preparado |
| Evidence Scope | Periodo, segmentos, metricas y limites cubiertos por la evidencia |
| Evidence Traceability | Relacion entre cada evidencia y el Analytical Model o fuente que la respalda |
| Evidence Limitations | Limitaciones, huecos, sensibilidad o incertidumbre de lectura |
| Transition Readiness | Indicacion de si el contract permite avanzar a Razonamiento o debe bloquearse |

## Critical Fields

| Field | Required | Description |
|---|---|---|
| contract_id | Yes | Identificador estable del contract |
| context_contract_id | Yes | Context Contract que delimita la evidencia |
| analytical_contract_id | Yes | Analytical Contract usado como base |
| evidence_scope | Yes | Porcion evaluada del modelo analitico |
| observable_findings | Yes | Hallazgos observables o UNKNOWN |
| derived_evidence | Yes | Evidencia derivada o declaracion de no aplicacion |
| source_metric_links | Yes | Vinculo entre evidencia y metrica, entidad o dimension fuente |
| limitations | Yes | Limitaciones que afectan la evidencia |
| uncertainty_notes | Yes | Notas de sensibilidad, insuficiencia o UNKNOWN |
| excluded_interpretations | Yes | Interpretaciones no incluidas por quedar fuera de esta fase |
| traceability_links | Yes | Artefactos o fuentes que justifican el contract |
| transition_status | Yes | Estado de avance hacia Razonamiento |

## Validation Rules

| Rule | Description |
|---|---|
| Analytical dependency | No puede emitirse un Evidence Contract usable sin Analytical Contract previo |
| Observable only | Los hallazgos deben permanecer observables o derivados del modelo analitico |
| No reasoning | El contract no puede producir insights, hipotesis, causas, conclusiones ni recomendaciones |
| Evidence traceability | Cada hallazgo debe poder rastrearse al Analytical Model o marcarse insuficiente |
| Limitation propagation | Toda limitacion del Analytical Contract debe reflejarse en la evidencia afectada |
| Uncertainty visibility | La evidencia insuficiente o sensible debe declararse antes de Razonamiento |
| Unknown explicitness | Hallazgos no verificables deben marcarse UNKNOWN, no completarse por inferencia |
| Scope alignment | La evidencia debe mantenerse dentro del alcance definido por Context y Analytical Contracts |

## Traceability

- [project_brief.md](/project_brief.md)
- [docs/context_refs.md](/docs/context_refs.md)
- [docs/contracts.md](/docs/contracts.md)
- [docs/contracts/context.contract.md](context.contract.md)
- [docs/contracts/data.contract.md](data.contract.md)
- [docs/contracts/discovery.contract.md](discovery.contract.md)
- [docs/contracts/analytical.contract.md](analytical.contract.md)
- [specs/spec-001-analytical-lifecycle.md](/specs/spec-001-analytical-lifecycle.md)
- [specs/spec-002-component-boundaries.md](/specs/spec-002-component-boundaries.md)
- [specs/spec-004-transversal-contracts.md](/specs/spec-004-transversal-contracts.md)
- [analytical_use_cases/meta_lead_quality_analysis.md](/analytical_use_cases/meta_lead_quality_analysis.md)
- [gates/spec-008-development-entry-phase-gate.md](/gates/spec-008-development-entry-phase-gate.md)

## Unknown Handling

| Unknown | Handling |
|---|---|
| Hallazgo no verificable | Marcar UNKNOWN y excluir de Razonamiento como soporte factual |
| Evidencia sin trazabilidad al modelo | Bloquear avance a Razonamiento o marcar insuficiencia explicita |
| Metrica insuficiente | Declarar limitacion y evitar derivar interpretaciones desde ella |
| Comparacion no soportada por granularidad | Marcar UNKNOWN y propagar sensibilidad |
| Limitacion heredada no resuelta | Mantenerla visible en Evidence Limitations |
| Evidencia minima obligatoria ausente | Bloquear o declarar que el caso no esta listo para Razonamiento |

## Idempotency Rules

Este contract es documental y no ejecuta analisis por si mismo.

Una instancia concreta del Evidence Contract debe describir de forma estable el mismo Evidence Set cuando consume el mismo Context Contract, Analytical Contract y criterios de analisis declarados.

## Dependencies

| Dependency | Type |
|---|---|
| VCA-CTX-001 | Context Contract |
| VCA-ANL-001 | Analytical Contract |
| Project Brief | Source of Truth |
| Context References | Source of Truth |
| SPEC-001 | Lifecycle |
| SPEC-002 | Boundary |
| SPEC-004 | Contract framework |

## Evidence

- SPEC-001 define Analisis como la fase que produce evidencia observable a partir del modelo analitico preparado.
- SPEC-002 establece que la Analytical Layer produce evidencia observable sin introducir conclusiones de negocio ni recomendaciones.
- SPEC-004 reconoce el Evidence Contract como categoria fundacional para formalizar hallazgos observables separados de interpretacion.
- La skill asociada exige no inventar datos, segmentos, campanas, periodos ni conclusiones no sustentadas.

## Risks

| Risk | Severity | Impact | Evidence |
|---|---|---|---|
| Evidencia mezclada con interpretacion | Important | Rompe la separacion entre Analisis y Razonamiento | SPEC-001; SPEC-002 |
| Limitaciones ocultas | Important | Puede inducir razonamiento posterior no sustentado | SPEC-001; skill |

## Definition of Done

Este contract cumple T-010 cuando:

1. Formaliza hallazgos observables y evidencia derivada.
2. Declara dependencia explicita del Analytical Contract.
3. Mantiene evidencia separada de interpretacion, conocimiento y recomendaciones.
4. Declara trazabilidad entre evidencia y modelo analitico.
5. Propaga UNKNOWN, limitaciones e incertidumbre antes de Razonamiento.

## Contextual Constraint Declaration

Cuando una ejecucion requiera contexto de negocio, dominio o estrategia para interpretar evidencia en fases posteriores, Evidence debe declarar las restricciones contextuales aplicables como un bloque estructurado y trazable.

El bloque debe incluir, como minimo:

- identificador estable del perfil o artefacto local que materializa las restricciones;
- fuente canonica y referencias de origen;
- alcance de aplicacion;
- reglas transportadas en forma estructurada;
- estado de aplicabilidad por evidencia, metrica o dimension afectada;
- limitaciones, UNKNOWNs o conflictos detectados.

Evidence no interpreta esas restricciones. Solo las conserva como contexto, linaje y condicion de uso para Knowledge, Recommendations y Presentation.

Si una restriccion contextual requerida esta ausente, contradice la fuente canonica o no puede aplicarse al alcance declarado, Evidence debe registrar `UNKNOWN`, limitacion o bloqueo segun impacto.