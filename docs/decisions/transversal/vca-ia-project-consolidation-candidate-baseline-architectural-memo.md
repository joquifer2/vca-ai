# VCA IA Project Consolidation Candidate Baseline - Architectural Memo

Estado: Draft documental candidato.

Tipo de artefacto: Nota de decision transversal.

Estructura: Inferida. No existe template especifico para memo arquitectonico transversal en `docs/templates/`.

Fecha: 2026-07-28

Responsable documental: Documentation Agent

Revision requerida: Reviewer Agent y QA Gate Agent.

Decision de cierre: Candidato pendiente. Este memo no declara `PASS`, no establece baseline definitivo y no sustituye validacion humana.

---

## 1. Proposito

Este memo consolida documentalmente una linea base estable candidata para navegar y gobernar el repositorio `VCA IA` tras la estabilizacion operativa de AUC-001 registrada en los artefactos vigentes.

La consolidacion se limita a documentar estructura, rutas, responsabilidades documentales y criterios de mantenimiento del repositorio. No introduce arquitectura funcional nueva, no modifica runtime, no altera contratos operativos y no reinterpreta decisiones aprobadas.

---

## 2. Alcance

Incluye:

- registrar una linea base documental candidata para organizacion transversal del repositorio;
- crear artefactos iniciales de gobernanza documental en `docs/repository-governance/`;
- persistir un task plan documental de la iteracion `Project Consolidation`;
- aclarar que la navegacion y la clasificacion documental no cambian la precedencia oficial;
- mantener AUC-001 como caso estable ya registrado, sin ejecutar ni modificar su operativa.

Excluye:

- modificar AUC-001 operativo;
- modificar contratos AUC-001;
- modificar runtime, BigQuery, MCP o herramientas de ejecucion;
- modificar outputs reales, outputs historicos o `outputs/auc-001/current/`;
- usar outputs historicos como fuente analitica;
- promover decisiones a Foundation;
- declarar cierre `PASS` sin Reviewer/QA.

---

## 3. Contexto documental

La referencia metodologica general del repositorio sigue siendo `.github/instructions/sdd.instructions.md`.

`docs/context_refs.md` actua como indice oficial de contexto y trazabilidad. Esta iteracion lo actualiza de forma limitada para registrar `Project Consolidation` como `DRAFT / PERSISTED FOR REVIEW`, sin declarar baseline definitivo y sin reabrir AUC-001.

El Project Brief define VCA IA como proyecto derivado SDD para un sistema analitico trazable de VCA. Esta consolidacion opera dentro de esa naturaleza de proyecto derivado y no convierte el repositorio en Foundation ni propone Foundation como destino de ninguna capacidad.

---

## 4. Decision documental candidata

Se propone tratar la estructura documental actual de `VCA IA` como baseline estable candidato para mantenimiento y navegacion, bajo estas condiciones:

1. El baseline es documental, no funcional.
2. El baseline es candidato hasta revision por Reviewer Agent y QA Gate Agent.
3. Las rutas operativas de AUC-001 permanecen fuera del alcance de esta iteracion.
4. La gobernanza de repositorio creada en `docs/repository-governance/` es inicial y no canonica hasta validacion.
5. Las reglas locales de clasificacion no pueden redefinir la precedencia documental general.

---

## 5. Modelo de repositorio candidato

| Area | Funcion documental candidata | Estado |
|---|---|---|
| `project_brief.md` | Proposito, alcance y limites del proyecto | Vigente segun contexto actual |
| `docs/context_refs.md` | Indice oficial de contexto y trazabilidad | Vigente; actualizado con referencia draft de Project Consolidation, sin baseline definitivo |
| `specs/` | Specifications versionadas y aplicables | Vigente segun cada spec |
| `analytical_use_cases/` | Definicion y navegacion de casos analiticos | Vigente; AUC-001 fuera de cambios operativos |
| `.github/skills/` | Skills documentales u operativas autorizadas | Fuera de cambios en esta iteracion |
| `docs/contracts/` | Contratos documentales y metodologicos | Fuera de cambios en esta iteracion |
| `docs/decisions/` | Decisiones y memos estabilizados o candidatos | Ampliado con este memo candidato |
| `docs/evaluations/` | Evaluaciones, experimentos, validaciones y registros historicos locales | Ajuste local de clasificacion solamente |
| `docs/repository-governance/` | Gobernanza documental inicial del repositorio | Nuevo, draft inicial |
| `tasks/` | Planes de trabajo trazables por iteracion | Ampliado con task plan documental |
| `outputs/` | Productos analiticos persistidos | No modificado |

---

## 6. Relacion con AUC-001

AUC-001 se mantiene como caso de uso estable segun los gates y registros vigentes. Esta iteracion no reabre AUC-001, no modifica su ruta canonica, no cambia sus contratos y no usa sus outputs como evidencia analitica.

Las referencias a AUC-001 en esta consolidacion solo cumplen una funcion de limite documental: identificar areas protegidas y evitar que la consolidacion transversal altere decisiones operativas ya cerradas.

---

## 7. WS-3

`WS-3` queda registrado unicamente como propuesta documental futura no ejecutable y no canonica.

No se crea workflow, runtime, automatizacion ni decision operacional asociada a `WS-3` en esta iteracion. Cualquier evolucion posterior de `WS-3` requerira artefacto propio, trazabilidad explicita, Reviewer y QA.

---

## 8. Riesgos y controles

| Riesgo | Control aplicado |
|---|---|
| Convertir una consolidacion documental en cambio funcional | Alcance explicitamente documental y exclusion de runtime, contratos y outputs |
| Redefinir precedencia general desde documentos secundarios | Referencia exclusiva a `.github/instructions/sdd.instructions.md` |
| Declarar baseline definitivo sin validacion | Estado `Draft documental candidato` |
| Usar AUC-001 como fuente analitica | AUC-001 solo se referencia como limite documental |
| Duplicar contenido canonico | Los documentos nuevos describen navegacion y mantenimiento, no reemplazan artefactos existentes |

---

## 9. Artefactos base de la iteracion

| Artefacto | Ruta | Estado |
|---|---|---|
| Memo arquitectonico | `docs/decisions/transversal/vca-ia-project-consolidation-candidate-baseline-architectural-memo.md` | Draft candidato |
| Task plan | `tasks/vca-ia-project-consolidation-task-plan.md` | Draft documental |
| Repository inventory inicial | `docs/repository-governance/repository-inventory.md` | Inicial |
| Documentation taxonomy | `docs/repository-governance/documentation-taxonomy.md` | Draft inicial |
| Navigation model | `docs/repository-governance/navigation-model.md` | Draft inicial |
| Repository governance guide | `docs/repository-governance/repository-governance-guide.md` | Draft inicial |

---

## 10. Siguiente paso recomendado

Enviar este paquete documental a Reviewer Agent para revisar coherencia, duplicacion, estado honesto y cumplimiento de restricciones. Despues, QA Gate Agent debe determinar si la iteracion puede cerrarse, condicionarse o bloquearse.