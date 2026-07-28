# VCA IA Project Consolidation - Task Plan

Estado: Draft documental.

Tipo de artefacto: Task plan transversal.

Estructura: Inferida. No existe template especifico para task plan transversal en `docs/templates/`.

Fecha: 2026-07-28

Responsable documental: Documentation Agent

Revision requerida: Reviewer Agent y QA Gate Agent.

Decision de cierre: QA validated / human validation pending. Este plan no declara baseline definitivo.

---

## 1. Objetivo

Ejecutar documentalmente la iteracion `Project Consolidation` para dejar persistidos los artefactos base de consolidacion transversal del repositorio VCA IA, sin introducir cambios funcionales ni operativos.

---

## 2. Alcance autorizado

Incluye:

- crear un memo arquitectonico transversal candidato;
- crear un task plan documental de la iteracion;
- crear documentos iniciales de gobernanza en `docs/repository-governance/`;
- ajustar la clasificacion local de `docs/evaluations/README.md` sin redefinir precedencia general;
- registrar restricciones de alcance y estado pendiente de validacion.

Excluye:

- mover archivos existentes;
- modificar AUC-001 operativo;
- modificar contratos AUC-001;
- modificar runtime, BigQuery, MCP o outputs reales;
- modificar `outputs/auc-001/current/`;
- usar outputs historicos como fuente analitica;
- proponer Foundation como decision;
- declarar cierre `PASS` sin Reviewer/QA.

---

## 3. Entradas documentales

| Entrada | Uso |
|---|---|
| `.github/instructions/sdd.instructions.md` | Precedencia, estado SDD y restricciones metodologicas |
| `.github/copilot-instructions.md` | Reglas de trabajo documental y separacion Foundation/proyecto |
| `AGENTS.md` | Routing y limites de agentes metodologicos |
| `.github/agents/documentation.agent.md` | Definicion canonica del Documentation Agent |
| `docs/context_refs.md` | Contexto oficial del proyecto |
| `project_brief.md` | Proposito, alcance y naturaleza de VCA IA |
| `README.md` | Navegacion y estado resumido del repositorio |

---

## 4. Plan de tareas

| ID | Tarea | Resultado esperado | Estado |
|---|---|---|---|
| PC-001 | Revisar instrucciones obligatorias y contexto base | Restricciones y fuentes aplicables identificadas | Hecho |
| PC-002 | Persistir memo arquitectonico transversal candidato | Memo creado en `docs/decisions/transversal/` | Hecho |
| PC-003 | Persistir task plan documental | Task plan creado en `tasks/` | Hecho |
| PC-004 | Crear inventario inicial del repositorio | Inventario inicial en `docs/repository-governance/` | Hecho |
| PC-005 | Crear taxonomia documental inicial | Taxonomia draft en `docs/repository-governance/` | Hecho |
| PC-006 | Crear modelo de navegacion inicial | Modelo draft en `docs/repository-governance/` | Hecho |
| PC-007 | Crear guia inicial de gobernanza del repositorio | Guia draft en `docs/repository-governance/` | Hecho |
| PC-008 | Ajustar `docs/evaluations/README.md` | Regla local de clasificacion acotada a `docs/evaluations/` | Hecho |
| PC-009 | Revisar rutas modificadas | Lista final de cambios disponible para Reviewer/QA en `docs/handoffs/vca-ia-project-consolidation-documentation-handoff.md` | Hecho |
| PC-010 | Revision por Reviewer Agent | Hallazgos, condiciones o aprobacion documental | Pendiente |
| PC-011 | Validacion por QA Gate Agent | Decision de cierre formal | Hecho |

---

## 5. Criterios de aceptacion documental

- Los artefactos nuevos existen en las rutas solicitadas o coherentes.
- Cada artefacto nuevo declara si su estado es inicial, draft o candidato.
- No se altera ninguna ruta operativa restringida.
- No se declara baseline definitivo.
- `docs/evaluations/README.md` contiene solo una regla local de clasificacion para su propio arbol.
- La precedencia general se referencia exclusivamente mediante `.github/instructions/sdd.instructions.md`.
- `WS-3` queda tratado como propuesta documental futura no ejecutable y no canonica.
- La iteracion queda validada por QA con condicion de validacion humana pendiente, sin baseline definitivo.

---

## 6. Riesgos pendientes

| Riesgo | Estado |
|---|---|
| Incorporacion en `docs/context_refs.md` | Realizada como referencia draft de Project Consolidation, sin declarar baseline definitivo |
| Gobernanza inicial incompleta | Esperado; los documentos estan marcados como iniciales |
| Cierre sin Reviewer/QA | Bloqueado por estado explicito de candidato pendiente |

---

## 7. Handoff

Este task plan queda preparado para revision documental. El siguiente paso recomendado es que Reviewer Agent revise coherencia, duplicacion, restricciones y trazabilidad antes de cualquier QA Gate de cierre.