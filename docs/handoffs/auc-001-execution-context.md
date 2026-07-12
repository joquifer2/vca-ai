# AUC-001 Execution Context

## Metadata

| Field | Value |
|---|---|
| Artifact ID | VCA-AUC-001-EXEC-CTX-001 |
| Artifact Type | Execution Context |
| Analytical Use Case | AUC-001 - Meta Lead Quality Analysis |
| Related Contract | VCA-CTX-001 |
| Status | Documented with blocking UNKNOWNs |
| Version | 1.0.0 |
| Last Updated | 2026-07-12 |
| Owner | Equipo VCA |
| Scope | Execution instance |
| Backing Task | T-015 / T-016 |

---

## Purpose

Representar la solicitud operativa normalizada de una ejecucion concreta del analisis de AUC-001 a partir de una Analysis Request antes de iniciar la resolucion del contexto oficial.

Este artefacto registra la intencion de ejecucion, su alcance pedido y sus restricciones declaradas para que la Context Resolution pueda trabajar sobre una instancia concreta y trazable.

Este artefacto actua como entrada operativa para T-015 y como habilitador documental de T-016.

Este artefacto no produce evidencia.

Este artefacto no interpreta datos.

Este artefacto no reemplaza el AUC, la Skill, el Project Brief, el Context Resolution ni el Context Contract.

---

## Architectural Position

| Layer | Role |
|---|---|
| User Request | Origen humano de la necesidad analitica |
| Analysis Request | Solicitud analitica concreta que precede a la normalizacion operativa |
| Execution Context | Normalizacion de la solicitud de ejecucion |
| Context Resolution | Resolucion documental del contexto oficial para la ejecucion |
| Context Definition | Definicion validada del alcance operativo para Discovery |
| Context Contract | Contrato reusable que formaliza el contexto ya delimitado |
| Downstream Contracts | Consumer del contexto validado de la ejecucion |

---

## Responsibility

El Execution Context tiene la responsabilidad de capturar, estructurar y congelar los parametros concretos solicitados para una corrida analitica de AUC-001.

Su funcion es cerrar la brecha entre la intencion del usuario y la resolucion documental del contexto que consumen los agentes y contracts posteriores.

---

## Producer

- Framework u orquestador documental de la ejecucion.
- Reviewer, cuando se requiera validacion documental previa antes de avanzar.

## Consumers

- Implementation Agent.
- Context Resolution.
- Flujo que construye el Context Definition.
- Framework de validacion del Context Definition.
- Data acquisition flow, indirectamente, a traves del contexto validado.

---

## Inputs

| Input | Description | Source |
|---|---|---|
| User Request | Intencion expresada por la persona solicitante | Conversacion o solicitud de ejecucion |
| Analysis Objective | Proposito concreto de la corrida | User Request; AUC-001 |
| Analysis Period | Ventana temporal exacta de la ejecucion | User Request; aprobacion documental |
| Campaign Scope | Campanas incluidas y excluidas | User Request; validacion documental |
| Ad Set Scope | Conjuntos incluidos y excluidos | User Request; validacion documental |
| Creative Scope | Creatividades incluidas y excluidas | User Request; validacion documental |
| Filters | Filtros operativos aplicables | User Request; validacion documental |
| Operational Lead Quality Definition | Definicion operativa de Lead de Calidad para esta corrida | User Request; contextos oficiales; Knowledge Base |
| Audience | Destinatarios del resultado | User Request; AUC-001 |
| Official Context References | Fuentes oficiales que deben consultarse en la resolucion | docs/context_refs.md; project_brief.md; knowledge/client/ |
| Constraints | Restricciones metodologicas o de alcance aplicables | project_brief.md; AUC-001; Skill |
| Assumptions | Supuestos explicitados y verificables | Solicitud de ejecucion; contexto oficial |

---

## Outputs

| Output | Description |
|---|---|
| Execution Context Record | Registro trazable de la corrida concreta |
| Execution Identifier | Identificador unico de la ejecucion |
| Operational Scope | Periodo, campañas, conjuntos, creatividades, filtros y audiencia |
| Contextual Constraints | Restricciones y supuestos explicitados |
| Traceability Links | Enlaces hacia User Request, AUC-001 y fuentes oficiales |
| Readiness for Context Resolution | Indicacion de si la solicitud puede pasar a Context Resolution |
| Blocking Unknowns | Huecos que impiden completar la solicitud operativa |

---

## Critical Fields

| Field | Required | Description |
|---|---|---|
| execution_id | Yes | Identificador estable de la corrida concreta |
| analysis_objective | Yes | Objetivo concreto de la ejecucion |
| analysis_period | Yes | Periodo exacto del analisis |
| campaign_scope | Yes | Campanas incluidas y excluidas |
| ad_set_scope | Yes | Conjuntos de anuncios incluidos y excluidos |
| creative_scope | Yes | Creatividades incluidas y excluidas |
| filters | Yes | Filtros operativos aplicables |
| lead_quality_definition | Yes | Definicion operativa de Lead de Calidad para la ejecucion |
| audience | Yes | Audiencia o destinatarios del resultado |
| official_context_sources | Yes | Fuentes oficiales consultadas o requeridas |
| constraints | Yes | Restricciones metodologicas o de contexto |
| assumptions | Yes | Supuestos declarados y verificables |
| traceability_links | Yes | Enlaces a User Request, AUC y artefactos relacionados |
| validation_status | Yes | Estado de validacion de la solicitud operativa |

---

## Validation Rules

| Rule | Description |
|---|---|
| Request before resolution | No puede iniciarse la Context Resolution sin una instancia de Execution Context |
| No implicit scope | El periodo, el alcance y los filtros no pueden inferirse si no estan explicitados |
| Unknown explicitness | Cualquier hueco debe declararse como UNKNOWN o bloqueante |
| Scope preservation | El artefacto no puede ampliar ni reescribir el AUC, la Skill o el Project Brief |
| Context containment | El artefacto no puede producir evidencia, interpretacion ni recomendaciones |
| Traceability preservation | Toda instancia debe enlazarse a la solicitud original y a las fuentes oficiales |
| Freeze on validation | Una vez validado, el contenido de la corrida debe quedar congelado para esa ejecucion |

---

## Lifecycle

1. Se crea a partir del User Request o de una solicitud documental equivalente.
2. Se contrasta con las fuentes oficiales y con el AUC-001.
3. Se valida documentalmente antes de Context Resolution, Discovery o adquisicion de datos.
4. Se congela para la ejecucion concreta.
5. Se conserva como evidencia de trazabilidad de la corrida.
6. Si cambia un dato material, se genera una nueva instancia.

---

## Unknown Handling

| Unknown | Handling |
|---|---|
| Periodo no definido | Bloquea la validacion del Execution Context |
| Alcance de campañas, conjuntos o creatividades no definido | Bloquea la validacion del Execution Context |
| Filtros no definidos | Bloquea o deja el contexto incompleto |
| Definicion operativa de Lead de Calidad no definida | Bloquea la Context Resolution y la validacion del Context Definition |
| Audiencia no definida | Marcar UNKNOWN si afecta a la salida o al encargo |
| Fuentes oficiales insuficientes | Marcar PENDING y evaluar bloqueo |

---

## Traceability

- [AUC-001 Context Resolution](auc-001-context-resolution.md)
- [AUC-001 Analysis Request](auc-001-analysis-request.md)
- [VCA-CTX-001 Context Contract](../contracts/context.contract.md)
- [AUC-001 Meta Lead Quality Analysis](../../analytical_use_cases/meta_lead_quality_analysis.md)
- [Meta Lead Quality Analysis Skill](../../.github/skills/meta-lead-quality-analysis/SKILL.md)
- [Project Brief](../../project_brief.md)
- [Context References](../context_refs.md)
- [README](../../README.md)
- [SPEC-001 Analytical Lifecycle](../../specs/spec-001-analytical-lifecycle.md)
- [SPEC-002 Component Boundaries](../../specs/spec-002-component-boundaries.md)
- [docs/glosario_terminos.md](../glosario_terminos.md)

---

## Relationship to Existing Artifacts

| Artifact | Relationship |
|---|---|
| User Request | Fuente humana inicial |
| Analysis Request | Solicitud analitica concreta previa a la ejecucion |
| AUC-001 | Capacidad reusable y permanente |
| Skill | Procedimiento reusable |
| Project Brief | Limites y proposito del proyecto |
| Context Contract | Contrato reusable que formaliza el contexto ya delimitado |
| Context Resolution | Artefacto derivado que resuelve el contexto oficial de la ejecucion |
| Context Definition | Instancia derivada y validada para Discovery |
| Downstream Contracts | Consumen el contexto validado de la corrida |

---

## Decision Summary

Este artefacto es necesario para representar la solicitud operativa concreta de una ejecucion.

Se apoya en una Analysis Request previa que fija la necesidad analitica concreta antes de la normalizacion de la ejecucion.

Sin este artefacto, la Context Resolution depende de informacion dispersa en la solicitud humana, el AUC, la Skill y las fuentes oficiales, lo que reproduce el bloqueo metodologico detectado en T-016.

Con este artefacto, el flujo queda separable en cuatro niveles:

- solicitud humana;
- instancia operativa de ejecucion;
- resolucion documental del contexto;
- contexto formal validado.

Eso permite mantener intactos el AUC, la Skill y el Context Contract como artefactos reutilizables, mientras se incorpora una capa documental de instancia para cada corrida concreta y una capa de resolucion para materializar el contexto oficial.
