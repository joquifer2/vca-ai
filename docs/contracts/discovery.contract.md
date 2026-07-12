# Discovery Contract

## Metadata

| Field | Value |
|---|---|
| Contract ID | VCA-DISC-001 |
| Contract Name | Discovery Contract |
| Contract Category | Discovery Contract |
| Status | Documented |
| Version | 1.0.0 |
| Last Updated | 2026-07-12 |
| Owner | Equipo VCA |
| Source Index | [docs/contracts.md](../contracts.md) |

---

## Purpose

Formalizar el Discovery Model antes de la preparacion analitica.

Este contract describe datasets, entidades, dimensiones, metricas, relaciones, granularidad y limitaciones observadas a partir del Context Contract y del Data Contract.

Este contract no prepara datos.

Este contract no produce evidencia analitica.

Este contract no interpreta resultados ni formula recomendaciones.

---

## Producer

Framework / fase Discovery.

## Consumer

- Analytical Layer.
- Future Analytical Contract.
- Skill aplicable, solo para validar compatibilidad de reglas de dominio con el espacio de datos descubierto.

## Inputs

| Input | Description | Source |
|---|---|---|
| Context Definition | Objetivo, alcance, restricciones, periodo y fuentes oficiales | VCA-CTX-001 |
| Data Source Declaration | Fuente principal, alcance expuesto y disponibilidad | VCA-DATA-001 |
| Logical Structure | Entidades, dimensiones, metricas y granularidad expuestas por el Data Provider | VCA-DATA-001 |
| Data Limitations | Huecos, permisos, latencia, granularidad o restricciones conocidas | VCA-DATA-001 |
| Skill Rules | Reglas de dominio que ayudan a reconocer elementos relevantes sin alterar el core | Skill aprobada, cuando aplique |

## Outputs

| Output | Description |
|---|---|
| Discovery Model | Descripcion logica del espacio de datos relevante para el objetivo |
| Relevant Entities | Entidades que pueden ser usadas por la fase de Preparacion |
| Relevant Dimensions | Dimensiones disponibles y aplicables al alcance |
| Relevant Metrics | Metricas disponibles y aplicables al alcance |
| Relationships | Relaciones observadas o declaradas entre entidades, dimensiones y metricas |
| Granularity Statement | Nivel de detalle disponible y sus efectos sobre el analisis |
| Discovery Limitations | Limitaciones que condicionan la preparacion y la interpretacion posterior |
| Transition Readiness | Indicacion de si el contract permite avanzar a Preparacion o debe bloquearse |

## Critical Fields

| Field | Required | Description |
|---|---|---|
| contract_id | Yes | Identificador estable del contract |
| context_contract_id | Yes | Context Contract que delimita el discovery |
| data_contract_id | Yes | Data Contract usado como fuente del discovery |
| discovery_scope | Yes | Porcion del espacio de datos evaluada |
| entities | Yes | Entidades relevantes o UNKNOWN |
| dimensions | Yes | Dimensiones relevantes o UNKNOWN |
| metrics | Yes | Metricas relevantes o UNKNOWN |
| relationships | Yes | Relaciones declaradas, observadas o UNKNOWN |
| granularity | Yes | Nivel de detalle disponible o UNKNOWN |
| limitations | Yes | Limitaciones que afectan Preparacion o Analisis |
| excluded_elements | Yes | Elementos no considerados y motivo |
| traceability_links | Yes | Artefactos o fuentes que justifican el contract |
| transition_status | Yes | Estado de avance hacia Preparacion |

## Validation Rules

| Rule | Description |
|---|---|
| Context dependency | No puede emitirse un Discovery Contract usable sin Context Contract previo |
| Data dependency | No puede emitirse un Discovery Contract usable sin Data Contract previo |
| No preparation | Discovery no puede normalizar, transformar, consolidar ni derivar modelos analiticos |
| No evidence | Discovery no puede convertir metricas disponibles en hallazgos o evidencia analitica |
| No interpretation | Discovery no puede producir insights, hipotesis, conclusiones ni recomendaciones |
| Limitation propagation | Toda limitacion observada debe propagarse hacia Preparacion |
| Unknown explicitness | Entidades, dimensiones, metricas o relaciones no verificadas deben marcarse UNKNOWN |
| Scope alignment | El Discovery Model debe mantenerse dentro del alcance definido por Context y Data Contracts |

## Traceability

- [project_brief.md](../../project_brief.md)
- [docs/context_refs.md](../context_refs.md)
- [docs/contracts.md](../contracts.md)
- [docs/contracts/context.contract.md](context.contract.md)
- [docs/contracts/data.contract.md](data.contract.md)
- [specs/spec-001-analytical-lifecycle.md](../../specs/spec-001-analytical-lifecycle.md)
- [specs/spec-002-component-boundaries.md](../../specs/spec-002-component-boundaries.md)
- [specs/spec-004-transversal-contracts.md](../../specs/spec-004-transversal-contracts.md)
- [analytical_use_cases/meta_lead_quality_analysis.md](../../analytical_use_cases/meta_lead_quality_analysis.md)
- [.github/skills/meta-lead-quality-analysis/SKILL.md](../../.github/skills/meta-lead-quality-analysis/SKILL.md)
- [gates/spec-008-development-entry-phase-gate.md](../../gates/spec-008-development-entry-phase-gate.md)

## Unknown Handling

| Unknown | Handling |
|---|---|
| Entidades no identificadas | Bloquear Preparacion si impide construir un modelo analitico coherente |
| Dimensiones no identificadas | Marcar UNKNOWN y limitar segmentacion o comparacion posterior |
| Metricas no identificadas | Bloquear si afectan la evidencia minima requerida por el AUC |
| Relaciones no verificadas | Marcar UNKNOWN y evitar joins, agrupaciones o lecturas dependientes |
| Granularidad insuficiente | Propagar como limitacion hacia Preparacion y Analisis |
| Limitaciones no evaluadas | Marcar PENDING y no considerar listo el handoff |

## Idempotency Rules

Este contract es documental y no ejecuta transformaciones.

Una instancia concreta del Discovery Contract debe producir el mismo Discovery Model cuando consume el mismo Context Contract, el mismo Data Contract y la misma metadata de fuente.

## Dependencies

| Dependency | Type |
|---|---|
| VCA-CTX-001 | Context Contract |
| VCA-DATA-001 | Data Contract |
| Project Brief | Source of Truth |
| Context References | Source of Truth |
| SPEC-001 | Lifecycle |
| SPEC-002 | Boundary |
| SPEC-004 | Contract framework |
| AUC-001 | Analytical use case |
| meta-lead-quality-analysis | Skill |

## Evidence

- SPEC-001 define Discovery como la fase que identifica datasets, entidades, dimensiones, metricas, relaciones y limitaciones antes de Preparacion.
- SPEC-002 exige que los handoffs entre Data Provider y Analytical Layer ocurran mediante artefactos identificables.
- SPEC-004 reconoce el Discovery Contract como categoria fundacional para formalizar el Discovery Model y sus limitaciones.
- AUC-001 requiere identificar Data Providers, evidencia principal, volumen, calidad, eficiencia, campanas, creatividades y segmentacion antes del analisis.
- La skill asociada exige no inventar datos, segmentos, campanas, periodos ni conclusiones no sustentadas.

## Risks

| Risk | Severity | Impact | Evidence |
|---|---|---|---|
| Discovery incompleto | Important | Puede conducir a una Preparacion ambigua o no trazable | SPEC-001 |
| Discovery convertido en preparacion | Important | Mezcla fases y debilita boundary compliance | SPEC-001; SPEC-002 |
| Relaciones asumidas sin fuente | Important | Puede producir modelos analiticos no verificables | SPEC-004; skill |
| Limitaciones no propagadas | Important | Puede ocultar incertidumbre en Analisis y Razonamiento | SPEC-001; AUC-001 |

## Definition of Done

Este contract cumple T-008 cuando:

1. Formaliza entidades, dimensiones, metricas, relaciones, granularidad y limitaciones.
2. Declara dependencia explicita de Context Contract y Data Contract.
3. Preserva la separacion entre Discovery, Preparacion, Analisis y Razonamiento.
4. Declara reglas de validacion y bloqueo antes de Preparacion.
5. Propaga UNKNOWN y limitaciones sin inferir datos no publicados.