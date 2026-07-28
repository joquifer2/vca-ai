# Documentation Taxonomy

Estado: Draft inicial.

Tipo de artefacto: Taxonomia documental.

Estructura: Inferida. No existe template especifico para taxonomia documental en `docs/templates/`.

Fecha: 2026-07-28

Revision requerida: Reviewer Agent y QA Gate Agent.

---

## 1. Proposito

Esta taxonomia inicial clasifica los tipos documentales usados en `VCA IA` para facilitar ubicacion, mantenimiento y revision.

No redefine precedencia documental. La precedencia general permanece definida exclusivamente en `.github/instructions/sdd.instructions.md`.

---

## 2. Categorias documentales

| Categoria | Ruta habitual | Funcion |
|---|---|---|
| Identidad del proyecto | `project_brief.md`, `README.md` | Explicar proposito, alcance, estado y navegacion inicial |
| Contexto oficial | `docs/context_refs.md` | Indexar fuentes de contexto y trazabilidad |
| Specifications | `specs/` | Definir capacidades, limites y criterios versionados |
| Analytical Use Cases | `analytical_use_cases/` | Documentar casos de uso analiticos y su estado |
| Skills | `.github/skills/` | Definir procedimientos de ejecucion autorizados |
| Contratos | `docs/contracts/` | Establecer invariantes documentales u operativas |
| Decisiones | `docs/decisions/` | Registrar decisiones, analisis arquitectonicos y memos |
| Evaluaciones | `docs/evaluations/` | Registrar investigations, experiments, validations, diagnostics e historical locales |
| Gates | `gates/` | Emitir decisiones de avance, bloqueo, condicion o cierre |
| Handoffs | `docs/handoffs/` | Transferir contexto entre agentes o fases |
| Planes de tareas | `tasks/` | Convertir decisiones y specs en trabajo trazable |
| Backlog documental | `docs/tasks.md` | Registrar trabajo documental auxiliar significativo |
| Gobernanza de repositorio | `docs/repository-governance/` | Mantener inventario, taxonomia, navegacion y reglas de mantenimiento |
| Templates | `docs/templates/` | Proveer estructuras base para artefactos futuros |
| Outputs | `outputs/` | Persistir productos analiticos generados y validados |

---

## 3. Estados documentales

| Estado | Significado |
|---|---|
| Inicial | Artefacto creado para orientar, aun incompleto o sin validacion completa |
| Draft | Artefacto redactado para revision, sin aprobacion final |
| Candidato | Artefacto propuesto como base o cierre, pendiente de Reviewer/QA |
| Vigente | Artefacto aplicable segun contexto y precedencia actual |
| Historico | Artefacto conservado por trazabilidad sin vigencia operativa |
| Protegido | Area que no debe modificarse sin autorizacion especifica |

---

## 4. Regla de clasificacion

Un documento debe vivir en la ruta que corresponda a su funcion primaria.

Si un documento mezcla varias funciones, debe preferirse separar explicacion, decision, evaluacion y procedimiento, salvo que un artefacto canonico existente ya requiera mantenerlas juntas.

---

## 5. Limites

Esta taxonomia no crea tipos documentales obligatorios nuevos, no convierte propuestas en decisiones aprobadas y no permite mover archivos existentes por iniciativa de esta iteracion.