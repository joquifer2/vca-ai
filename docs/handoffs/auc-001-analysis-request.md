# AUC-001 Analysis Request

## Metadata

| Field | Value |
|---|---|
| Artifact ID | VCA-AUC-001-ANL-REQ-001 |
| Artifact Type | Analysis Request |
| Analytical Use Case | AUC-001 - Meta Lead Quality Analysis |
| Related Contract | VCA-CTX-001 |
| Status | Documented with blocking UNKNOWNs |
| Version | 1.0.0 |
| Last Updated | 2026-07-12 |
| Owner | Equipo VCA |
| Scope | Analysis request instance |
| Backing Task | T-016 |

---

## Purpose

Representar la solicitud analitica concreta que inicia la cadena documental de AUC-001 antes de normalizarla como Execution Context.

Este artefacto captura la intencion de analisis, el resultado esperado y las restricciones declaradas para que el Execution Context pueda estructurar la ejecucion concreta de forma trazable.

Este artefacto es prerequisito documental de T-016 y no sustituye la validacion del Context Definition.

Este artefacto no resuelve el contexto oficial.

Este artefacto no produce evidencia.

Este artefacto no interpreta datos.

---

## Architectural Position

| Layer | Role |
|---|---|
| User Request | Expresion humana inicial de la necesidad analitica |
| Analysis Request | Normalizacion de la solicitud analitica |
| Execution Context | Normalizacion de la solicitud de ejecucion concreta |
| Context Resolution | Resolucion documental del contexto oficial para la ejecucion |
| Context Definition | Definicion validada del alcance operativo para Discovery |

---

## Responsibility

El Analysis Request tiene la responsabilidad de fijar la necesidad analitica concreta, el tipo de salida esperado y las restricciones declaradas antes de la instanciacion operativa de la ejecucion.

Su funcion es cerrar la brecha entre la peticion humana y el Execution Context sin mezclar todavia contexto oficial ni validacion metodologica.

---

## Producer

- Persona solicitante.
- Framework documental de intake, cuando exista.

## Consumers

- Execution Context.
- Reviewer, cuando requiera validar la claridad de la solicitud antes de avanzar.
- Flujo de Context Resolution, indirectamente, a traves del Execution Context.

---

## Inputs

| Input | Description | Source |
|---|---|---|
| User Request | Intencion expresada por la persona solicitante | Conversacion o solicitud de ejecucion |
| Analysis Objective | Proposito del analisis y decision a soportar | User Request; AUC-001 |
| Output Request | Tipo de salida final esperada | User Request; AUC-001 |
| Audience | Destinatarios del resultado | User Request; AUC-001 |
| Constraints | Restricciones declaradas o conocidas | User Request; project_brief.md; AUC-001 |
| Known Context References | Fuentes oficiales que ya se conocen como relevantes | docs/context_refs.md; project_brief.md |

---

## Outputs

| Output | Description |
|---|---|
| Analysis Request Record | Registro trazable de la solicitud analitica concreta |
| Request Identifier | Identificador unico de la solicitud |
| Requested Objective | Objetivo y decision a soportar |
| Requested Output | Forma de salida o informe solicitado |
| Request Constraints | Restricciones declaradas y supuestos visibles |
| Traceability Links | Enlaces hacia User Request, AUC-001 y fuentes oficiales |
| Readiness for Execution Context | Indicacion de si la solicitud puede pasar a Execution Context |
| Blocking Unknowns | Huecos que impiden normalizar la solicitud |

---

## Critical Fields

| Field | Required | Description |
|---|---|---|
| request_id | Yes | Identificador estable de la solicitud analitica |
| analysis_objective | Yes | Objetivo concreto de la solicitud |
| output_request | Yes | Tipo de salida esperada |
| audience | Yes | Audiencia o destinatarios del resultado |
| constraints | Yes | Restricciones metodologicas o de contexto |
| assumptions | Yes | Supuestos declarados y verificables |
| traceability_links | Yes | Enlaces a User Request, AUC y artefactos relacionados |
| validation_status | Yes | Estado de validacion de la solicitud analitica |

---

## Validation Rules

| Rule | Description |
|---|---|
| Request before execution context | No puede iniciarse el Execution Context sin una instancia de Analysis Request |
| No implicit request | El objetivo, la salida y la audiencia no pueden inferirse si no estan explicitados |
| Unknown explicitness | Cualquier hueco debe declararse como UNKNOWN o bloqueante |
| Scope preservation | El artefacto no puede ampliar ni reescribir el AUC, la Skill o el Project Brief |
| Context containment | El artefacto no puede producir evidencia, interpretacion ni recomendaciones |
| Traceability preservation | Toda instancia debe enlazarse a la solicitud original y a las fuentes oficiales |

---

## Lifecycle

1. Se crea a partir del User Request o de una solicitud documental equivalente.
2. Se contrasta con el AUC-001 y con las fuentes oficiales conocidas.
3. Se valida documentalmente antes de Execution Context.
4. Se conserva como evidencia de trazabilidad de la solicitud concreta.
5. Si cambia un dato material, se genera una nueva instancia.

---

## Unknown Handling

| Unknown | Handling |
|---|---|
| Objetivo no definido | Bloquea la validacion del Analysis Request |
| Salida esperada no definida | Bloquea la normalizacion de la solicitud |
| Audiencia no definida | Marcar UNKNOWN si afecta al encargo |
| Restricciones no definidas | Bloquea o deja la solicitud incompleta |
| Fuentes oficiales insuficientes | Marcar PENDING y evaluar bloqueo |

---

## Traceability

- [AUC-001 Execution Context](auc-001-execution-context.md)
- [VCA-CTX-001 Context Contract](../contracts/context.contract.md)
- [AUC-001 Meta Lead Quality Analysis](../../analytical_use_cases/meta_lead_quality_analysis.md)
- [Meta Lead Quality Analysis Skill](../../.github/skills/meta-lead-quality-analysis/SKILL.md)
- [Project Brief](../../project_brief.md)
- [Context References](../context_refs.md)
- [docs/tasks.md](../tasks.md)
- [README](../../README.md)
- [SPEC-001 Analytical Lifecycle](../../specs/spec-001-analytical-lifecycle.md)
- [SPEC-002 Component Boundaries](../../specs/spec-002-component-boundaries.md)
- [docs/glosario_terminos.md](../glosario_terminos.md)

---

## Relationship to Existing Artifacts

| Artifact | Relationship |
|---|---|
| User Request | Fuente humana inicial |
| AUC-001 | Capacidad reusable y permanente |
| Skill | Procedimiento reusable |
| Project Brief | Limites y proposito del proyecto |
| Analysis Request | Solicitud analitica concreta |
| T-016 | Validacion documental que consume esta solicitud como prerequisito |
| Execution Context | Artefacto derivado que normaliza la solicitud de ejecucion concreta |
| Context Resolution | Artefacto derivado que resuelve el contexto oficial de la ejecucion |
| Context Definition | Instancia derivada y validada para Discovery |

---

## Decision Summary

Este artefacto separa la solicitud analitica concreta de la ejecucion operativa.

Sin este artefacto, la cadena documental salta directamente de la peticion humana al Execution Context, lo que deja un hueco que algunos implementadores interpretan como bloqueo.

Con este artefacto, el flujo queda separable en cinco niveles:

- solicitud humana;
- solicitud analitica concreta;
- instancia operativa de ejecucion;
- resolucion documental del contexto;
- contexto formal validado.

Eso permite mantener intactos el AUC, la Skill y el Context Contract como artefactos reutilizables, mientras se incorpora una capa documental de solicitud que precede al Execution Context.