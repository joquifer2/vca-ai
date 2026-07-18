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
- [.github/skills/meta-lead-quality-analysis/SKILL.md](/.github/skills/meta-lead-quality-analysis/SKILL.md)
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
| AUC-001 | Analytical use case |
| meta-lead-quality-analysis | Skill |

## Evidence

- SPEC-001 define Analisis como la fase que produce evidencia observable a partir del modelo analitico preparado.
- SPEC-002 establece que la Analytical Layer produce evidencia observable sin introducir conclusiones de negocio ni recomendaciones.
- SPEC-004 reconoce el Evidence Contract como categoria fundacional para formalizar hallazgos observables separados de interpretacion.
- AUC-001 requiere separar hechos observables, evidencia derivada, interpretaciones y recomendaciones.
- La skill asociada exige no inventar datos, segmentos, campanas, periodos ni conclusiones no sustentadas.

## Risks

| Risk | Severity | Impact | Evidence |
|---|---|---|---|
| Evidencia mezclada con interpretacion | Important | Rompe la separacion entre Analisis y Razonamiento | SPEC-001; SPEC-002 |
| Hallazgos sin trazabilidad | Important | Debilita auditabilidad y confiabilidad | SPEC-004; AUC-001 |
| Limitaciones ocultas | Important | Puede inducir razonamiento posterior no sustentado | SPEC-001; skill |
| Evidencia insuficiente tratada como concluyente | Important | Produce conclusiones no verificables | AUC-001; skill |

## Definition of Done

Este contract cumple T-010 cuando:

1. Formaliza hallazgos observables y evidencia derivada.
2. Declara dependencia explicita del Analytical Contract.
3. Mantiene evidencia separada de interpretacion, conocimiento y recomendaciones.
4. Declara trazabilidad entre evidencia y modelo analitico.
5. Propaga UNKNOWN, limitaciones e incertidumbre antes de Razonamiento.

## AUC-001 Post-Closure Cost-Quality Evidence Rules

Estas reglas aplican solo a la evolucion post-cierre `AUC-001-PCI-001` definida por SPEC-012. No reabren el ciclo experimental original ni modifican outputs historicos.

### Runtime Boundary

| Fase | Responsabilidad |
|---|---|
| Evidence Acquisition | Adquirir agregados lead-side y spend-side mediante BigQuery MCP, sin unir fuentes ni interpretar. |
| Analytical Preparation | Normalizar, limpiar, validar y agregar cada fuente de forma independiente. |
| Evidence Set Construction | Ejecutar full outer join determinista, asignar coverage states, reconciliar totales, calcular invariantes y construir el Evidence Set coste-calidad. |

### Canonical Model vs Executed Evidence Set

| Elemento | Regla |
|---|---|
| Canonical model | Reglas estables de fuentes, normalizacion, universos, metricas, invariantes y blockers. |
| Executed Evidence Set | Instancia para un periodo, execution_id, datos, resultados, limitaciones y trazabilidad especificos. |
| Historical outputs | Permanecen inmutables y no pueden sobrescribirse ni usarse como expected values. |
| Post-closure outputs | Para `AUC-001-PCI-001` deben declarar la iteracion y persistirse bajo `outputs/auc-001/pci-001/2026-06-30/`; futuras iteraciones usaran `outputs/auc-001/pci-00N/<execution-date>/`. |

### Coverage States

| Estado | Regla |
|---|---|
| `matched` | Lead-side valido y spend `COMMERCIAL` valido para el mismo `ad_id_norm`. |
| `lead_only` | Lead-side valido sin spend `COMMERCIAL` emparejado; no soporta CPL/CPQL. |
| `spend_only` | Spend `COMMERCIAL` valido sin lead-side emparejado; no implica cero leads reales ni ineficiencia automatica. |
| `UNKNOWN` | Clasificacion no fiable por ID invalido, colision, duplicidad, periodo incompatible, señal invalida, fuente no validada o estructura incompleta. |

### Economic Universes And Metrics

El Evidence Set post-cierre debe distinguir `total_spend_all_signals`, `commercial_spend`, `matched_commercial_spend`, `spend_only_commercial_spend`, `total_leads`, `matched_leads`, `lead_only_leads`, `total_ab_leads`, `matched_ab_leads`, `lead_only_ab_leads`, Tier A total/matched y Tier B total/matched.

Metricas permitidas: `cpl_commercial_matched`, `qualified_rate_ab_global`, `qualified_rate_ab_matched`, `cost_per_ab_commercial_matched`, `cost_per_tier_a_commercial_matched`, `spend_share_by_signal`, `spend_share_matched`, `lead_share_matched`, `ab_share_matched`, `commercial_spend_per_matched_lead_observed`.

Metricas prohibidas: `CPL` sin universo, `CPQL` sin universo/señal/coverage, CPL/CPQL sobre `lead_only`, CPL/CPQL sobre `spend_only`, coste-calidad mezclando señales, rankings por `ad_name`, ratios con denominador cero convertido a cero y metricas que usen historicos como expected values.

### Invariants And Precision

```text
commercial_spend = matched_spend + spend_only_spend
lead_total = matched_leads + lead_only_leads
ab_total = matched_ab_leads + lead_only_ab_leads
tier_a_total = matched_tier_a + lead_only_tier_a
tier_b_total = matched_tier_b + lead_only_tier_b
prepared_ad_count = matched_ad_count + lead_only_ad_count + spend_only_ad_count
```

Moneda EUR, tipo recomendado `NUMERIC`, sin redondeo intermedio, presentacion monetaria a 2 decimales, tolerancia monetaria 0.01 EUR por fila y agregado, denominador cero como `NULL`, desconocidos como `NULL` o `UNKNOWN` explicito.

### Publication Controls

| Condicion | Clasificacion |
|---|---|
| Invariantes incumplidas, colisiones de `ad_id_norm`, periodos incompatibles, señal invalida, mezcla de señales, ausencia de trazabilidad MCP o fuente canonica no validada | Blocking error |
| `spend_only` interpretado como cero leads reales sin sustentar recomendacion | Warning |
| Muestra insuficiente para ranking o recomendacion | Presentation limitation |

Todo blocking error debe detener la publicacion del Evidence Set completo, bloque afectado o metrica concreta segun el alcance definido en SPEC-012.