# Knowledge Contract

## Metadata

| Field | Value |
|---|---|
| Contract ID | VCA-KNW-001 |
| Contract Name | Knowledge Contract |
| Contract Category | Knowledge Contract |
| Status | Documented |
| Version | 1.0.0 |
| Last Updated | 2026-07-12 |
| Owner | Equipo VCA |
| Source Index | [docs/contracts.md](/docs/contracts.md) |

---

## Purpose

Formalizar el Knowledge Set producido durante la fase de Razonamiento.

Este contract transforma evidencia observable en conocimiento explicito: insights, hipotesis, conclusiones, prioridades, oportunidades, riesgos e incertidumbres declaradas.

Este contract debe mantener trazabilidad entre cada interpretacion y la evidencia que la respalda.

Este contract no formula acciones sugeridas.

Este contract no define esfuerzo, dependencias operativas ni plan de ejecucion.

---

## Producer

Reasoning Layer / fase Razonamiento.

## Consumer

- Reasoning Layer / fase Recomendaciones.
- Future Recommendation Contract.
- Framework, para validar readiness metodologica antes de Recomendaciones.

## Inputs

| Input | Description | Source |
|---|---|---|
| Context Definition | Objetivo, alcance, restricciones y decision soportada | VCA-CTX-001 |
| Evidence Set | Hallazgos observables, evidencia derivada y limitaciones | VCA-EVD-001 |
| Evidence Traceability | Vinculo entre evidencia y modelo analitico | VCA-EVD-001 |
| Evidence Limitations | Huecos, sensibilidad, insuficiencia o incertidumbre de lectura | VCA-EVD-001 |
| Skill Rules | Criterios de dominio que permiten interpretar evidencia dentro del alcance aprobado | Skill aprobada, cuando aplique |

## Outputs

| Output | Description |
|---|---|
| Knowledge Set | Conjunto de conocimiento estructurado y trazable |
| Insights | Interpretaciones respaldadas por evidencia identificable |
| Hypotheses | Hipotesis plausibles con evidencia, incertidumbre y condiciones de validacion |
| Conclusions | Conclusiones soportadas por evidencia y alcance declarado |
| Priorities | Orden relativo de relevancia, impacto o urgencia metodologicamente justificado |
| Opportunities | Areas potenciales de mejora identificadas desde evidencia y contexto |
| Risks | Riesgos interpretativos, de negocio o de evidencia que condicionan la lectura |
| Uncertainties | Incertidumbres, UNKNOWN o limitaciones que deben permanecer visibles |
| Transition Readiness | Indicacion de si el contract permite avanzar a Recomendaciones o debe bloquearse |

## Critical Fields

| Field | Required | Description |
|---|---|---|
| contract_id | Yes | Identificador estable del contract |
| context_contract_id | Yes | Context Contract que delimita el razonamiento |
| evidence_contract_id | Yes | Evidence Contract usado como base |
| reasoning_scope | Yes | Porcion de evidencia interpretada |
| insights | Yes | Insights trazados a evidencia o declaracion de no disponibilidad |
| hypotheses | Yes | Hipotesis, condiciones y soporte de evidencia |
| conclusions | Yes | Conclusiones respaldadas o UNKNOWN |
| priorities | Yes | Priorizacion justificada o no aplicable |
| risks | Yes | Riesgos relevantes de interpretacion o contexto |
| uncertainties | Yes | Incertidumbres y UNKNOWN declarados |
| evidence_links | Yes | Trazabilidad entre conocimiento y evidencia |
| excluded_recommendations | Yes | Acciones no incluidas por quedar fuera de esta fase |
| transition_status | Yes | Estado de avance hacia Recomendaciones |

## Validation Rules

| Rule | Description |
|---|---|
| Evidence dependency | No puede emitirse un Knowledge Contract usable sin Evidence Contract previo |
| Evidence-backed reasoning | Todo insight, hipotesis o conclusion debe enlazarse a evidencia identificable |
| Uncertainty declaration | La incertidumbre debe declararse cuando la evidencia no sea concluyente |
| No new evidence | Razonamiento no puede crear evidencia nueva ni modificar hallazgos observables |
| No recommendations | El contract no puede formular acciones sugeridas ni planes de ejecucion |
| Correlation caution | Correlaciones y patrones deben distinguirse de causalidad o explicacion confirmada |
| Priority traceability | Toda prioridad debe indicar criterio, evidencia o limitacion que la justifica |
| Unknown explicitness | Interpretaciones no verificables deben marcarse UNKNOWN, no completarse por inferencia |

## Traceability

- [project_brief.md](/project_brief.md)
- [docs/context_refs.md](/docs/context_refs.md)
- [docs/contracts.md](/docs/contracts.md)
- [docs/contracts/context.contract.md](context.contract.md)
- [docs/contracts/analytical.contract.md](analytical.contract.md)
- [docs/contracts/evidence.contract.md](evidence.contract.md)
- [specs/spec-001-analytical-lifecycle.md](/specs/spec-001-analytical-lifecycle.md)
- [specs/spec-002-component-boundaries.md](/specs/spec-002-component-boundaries.md)
- [specs/spec-004-transversal-contracts.md](/specs/spec-004-transversal-contracts.md)
- [analytical_use_cases/meta_lead_quality_analysis.md](/analytical_use_cases/meta_lead_quality_analysis.md)
- [gates/spec-008-development-entry-phase-gate.md](/gates/spec-008-development-entry-phase-gate.md)

## Unknown Handling

| Unknown | Handling |
|---|---|
| Insight sin evidencia suficiente | Marcar UNKNOWN o excluir del Knowledge Set |
| Hipotesis no validable con evidencia disponible | Declarar como hipotesis pendiente y no convertirla en conclusion |
| Conclusion no soportada | Bloquear avance a Recomendaciones para esa conclusion |
| Prioridad sin criterio trazable | Marcar PENDING y no usar como base de recomendacion |
| Causalidad no demostrada | Declarar correlacion, asociacion o lectura tentativa segun corresponda |
| Incertidumbre material | Propagar a Recommendation Contract y salida final |

## Idempotency Rules

Este contract es documental y no ejecuta razonamiento por si mismo.

Una instancia concreta del Knowledge Contract debe describir de forma estable el mismo Knowledge Set cuando consume el mismo Context Contract, Evidence Contract, Skill Rules y criterios de razonamiento declarados.

## Dependencies

| Dependency | Type |
|---|---|
| VCA-CTX-001 | Context Contract |
| VCA-EVD-001 | Evidence Contract |
| Project Brief | Source of Truth |
| Context References | Source of Truth |
| SPEC-001 | Lifecycle |
| SPEC-002 | Boundary |
| SPEC-004 | Contract framework |

## Evidence

- SPEC-001 define Razonamiento como la fase que transforma evidencia en insights, hipotesis, oportunidades, riesgos, prioridades e incertidumbres.
- SPEC-002 establece que la Reasoning Layer consume evidencia y produce conocimiento accionable sin reconsultar la fuente original para compensar evidencia mal definida.
- SPEC-004 reconoce el Knowledge Contract como categoria fundacional para formalizar insights, hipotesis, prioridades e incertidumbres.
- La skill asociada exige evitar saltos logicos y distinguir correlacion de interpretacion.

## Risks

| Risk | Severity | Impact | Evidence |
|---|---|---|---|
| Insight sin evidencia trazable | Important | Debilita confiabilidad y auditabilidad | SPEC-001; SPEC-004 |
| Razonamiento crea evidencia nueva | Important | Rompe separacion entre Analisis y Razonamiento | SPEC-001; SPEC-002 |
| Recomendaciones prematuras | Important | Mezcla Razonamiento con Recomendaciones | SPEC-001; SPEC-004 |

## Definition of Done

Este contract cumple T-011 cuando:

1. Formaliza insights, hipotesis, conclusiones, prioridades, riesgos e incertidumbres.
2. Declara dependencia explicita del Evidence Contract.
3. Mantiene trazabilidad entre conocimiento y evidencia.
4. Distingue correlacion, hipotesis, conclusion e incertidumbre.
5. No formula recomendaciones ni acciones sugeridas.

## Contextual Constraint Declaration

Cuando Knowledge interprete evidencia condicionada por contexto de negocio, dominio o estrategia, debe consumir las restricciones contextuales aplicables desde un perfil o artefacto local declarado.

Cada claim afectado debe conservar trazabilidad a:

- la evidencia usada;
- el perfil de restricciones aplicable;
- la fuente canonica de la restriccion;
- el identificador estable de la regla o restriccion aplicada.

Knowledge no puede crear restricciones nuevas ni completar restricciones ausentes por inferencia. Si una interpretacion entra en conflicto con el perfil aplicable, debe bloquearse, degradarse a hipotesis con incertidumbre explicita o declararse UNKNOWN segun el alcance.