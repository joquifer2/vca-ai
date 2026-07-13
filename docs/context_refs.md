# Context References

# Referencias de Contexto del Proyecto

> Este documento define las fuentes de contexto oficiales que deben consultarse antes de generar o modificar cualquier Project Brief, Spec, documento de arquitectura, Tasks, codigo o documentacion tecnica de vca-ai.
>
> No duplica el contenido completo de otras fuentes. Actua como indice de referencias y trazabilidad del contexto oficial del proyecto.
>
> Estado de transicion del proyecto derivado: Development Authorized.

---

# 1. Identidad del Proyecto

```yaml
proyecto:
  nombre: VCA IA
  id_proyecto: VCA-IA
  tipo_proyecto: Proyecto derivado SDD para un sistema analitico trazable de VCA
  estado: Development Authorized
  version: v1.0.0
  fecha_creacion: 2026-07-10
  responsable: VCA IA maintainers

cliente:
  id_cliente: VCA
  nombre_cliente: VCA
  estado_relacion: Contexto operativo del proyecto
```

---

# 2. Contexto de Cliente Requerido

## Contexto oficial del proyecto

```yaml
contexto_proyecto:
  conocimiento_persistente:
    sistema: filesystem
    ubicacion: knowledge/client/
    version: activa
    estado: vigente
    ultima_revision: 2026-07-11
    fecha_consulta: 2026-07-11

  ccd_independiente:
    requerido: false
    estado: no_publicado
    observacion: El contexto oficial del proyecto se concentra actualmente en la Knowledge Base y en los artefactos canonicos del repositorio.
```

## Notas sobre el uso del contexto oficial

- La Knowledge Base del proyecto es la referencia primaria para el contexto persistente y reutilizable.
- No debe inferirse conocimiento de negocio, arquitectura o restricciones desde fuentes externas no publicadas en el repositorio.
- Si en el futuro se formaliza un CCD independiente, debera registrarse aqui como referencia oficial adicional.

---

# 3. Decisiones Relacionadas

> La fuente oficial de decisiones del proyecto son los artefactos versionados en el repositorio.

| Fecha | Decisión | Impacto en este proyecto | Fuente |
| --- | --- | --- | --- |
| 2026-07-11 | Adoptar AIF Foundation como dependencia metodologica reutilizable | Permite reutilizar la base SDD sin convertir la Foundation en el objeto del proyecto | README.md; project_brief.md |
| 2026-07-11 | Validar el caso de uso AUC-001 y la skill meta-lead-quality-analysis como primer ciclo analitico trazable | Define la primera capacidad analitica aprobada del proyecto y su via de ejecucion | analytical_use_cases/meta_lead_quality_analysis.md; .github/skills/meta-lead-quality-analysis/SKILL.md |
| 2026-07-11 | Definir criterios de validacion para AUC-001 | Establece criterios observables y reutilizables para validar el caso | analytical_use_cases/meta_lead_quality_analysis.md; docs/tasks.md |
| 2026-07-11 | Cerrar el primer ciclo de tareas de AUC-001 | Registra la delimitacion, evidencia, flujo y validacion del primer caso analitico | analytical_use_cases/meta_lead_quality_analysis.md; docs/tasks.md; docs/context_refs.md |
| 2026-07-11 | Autorizar la entrada a Development mediante SPEC-008 con PASS WITH OBSERVATIONS | Situa el proyecto en Development manteniendo visibles las observaciones activas del Phase Gate | gates/spec-008-development-entry-phase-gate.md; sdd_readiness_assessment.md |
| 2026-07-13 | Formalizar el Analytical Use Case Completion / Acceptance Gate mediante SPEC-009 | Introduce un gate reutilizable para el cierre y aceptacion documental de un caso analitico, distinto del Phase Gate de Development | specs/spec-009-analytical-use-case-completion-acceptance-gate.md; docs/evaluations/auc-001-closure-reconciliation-review.md |
| 2026-07-13 | Validar la integracion MCP de BigQuery para AUC-001 mediante T-039 | Separa la validacion MCP de la adquisicion CLI de T-018 y deja trazabilidad tecnica del acceso directo al provider | docs/evaluations/auc-001-bigquery-mcp-integration-validation.md; docs/tasks.md |

## Decisiones pendientes de validar

No hay decisiones pendientes de validar que bloqueen la evolucion actual del proyecto con la informacion publicada en el repositorio.

---

# 4. Proyectos Relacionados

| Proyecto | Relacion con este proyecto | Estado | Fuente |
| --- | --- | --- | --- |
| AIF Foundation | Dependencia metodologica reutilizable | Activo | .github/instructions/sdd.instructions.md; .github/copilot-instructions.md |
| Ecosistema analitico existente de VCA | Fuente operativa de contexto y evidencia para los casos analiticos del proyecto | Activo | project_brief.md; knowledge/client/ |

---

# 5. Reuniones Relacionadas

No hay reuniones versionadas relevantes para la contextualizacion actual del proyecto en el repositorio.

---

# 6. Conocimiento Reutilizable Relacionado

| Recurso | Tipo | Motivo de uso | Fuente |
| --- | --- | --- | --- |
| Knowledge Base del proyecto | Base de conocimiento | Contexto persistente y reutilizable del proyecto | knowledge/client/ |
| Analytical Use Case AUC-001 | Caso de uso analitico | Primer caso aprobado que valida la linea de trabajo del proyecto | analytical_use_cases/meta_lead_quality_analysis.md |
| Meta Lead Quality Analysis Skill | Skill | Skill asociada al primer caso analitico aprobado | .github/skills/meta-lead-quality-analysis/SKILL.md |
| Project Brief | Definicion oficial del proyecto | Proposito, alcance, limites y criterios de exito | project_brief.md |
| README | Vision general navegable del proyecto | Estructura de entrada y orientacion general | README.md |
| Specifications del proyecto | Specifications | Lifecycle, boundaries, extensibilidad, contracts, gates y evaluaciones del proyecto | specs/ |
| Tasks Backlog | Governance | Seguimiento trazable del trabajo aprobado | docs/tasks.md |
| SDD Readiness Assessment | Evaluation | Evidencia de readiness para la entrada a Development | sdd_readiness_assessment.md |
| Phase Gate Record | Governance | Registro de la autorizacion de entrada a Development | gates/spec-008-development-entry-phase-gate.md |
| AUC-001 Closure Reconciliation Review | Evaluation | Reconciliacion de cierre documental del caso AUC-001 | docs/evaluations/auc-001-closure-reconciliation-review.md |
| AUC-001 BigQuery MCP Integration Validation | Evaluation | Validacion documental y tecnica del acceso MCP separada de T-018 | docs/evaluations/auc-001-bigquery-mcp-integration-validation.md |
| SPEC-009 Analytical Use Case Completion / Acceptance Gate | Specification | Gate reusable para cierre y aceptacion de Analytical Use Cases | specs/spec-009-analytical-use-case-completion-acceptance-gate.md |
| SDD Instructions | Instrucciones | Reglas de fase, contexto y precedencia documental | .github/instructions/sdd.instructions.md |
| Glosario de terminos | Documentacion | Definiciones oficiales de artefactos y terminos | docs/glosario_terminos.md |

---

# 7. Fuentes Tecnicas Relacionadas

## Repositorios

```yaml
repositorios:
  - nombre: vca-ai
    url: https://github.com/joquifer2/vca-ai.git
    rama: main
    descripcion: Repositorio principal del proyecto derivado VCA IA
```

## Google Cloud

```yaml
google_cloud:
  proyectos: []
  buckets_gcs: []
  bigquery:
    datasets: []
    tablas: []
```

## Dashboards

```yaml
dashboards: []
```

## APIs / Plataformas Externas

```yaml
apis:
  - nombre: BigQuery MCP Server
    documentacion: PENDING
    uso_en_proyecto: Fuente principal de evidencia para el caso AUC-001 y futuros analisis trazables
```

---

# 8. Fuentes Runtime para Agentes IA

> Esta seccion indica que fuentes deben consultar los agentes durante el desarrollo y la evolucion del proyecto.

```yaml
runtime_sources:

  documentos_publicados:
    - nombre: README
      tipo: Documento oficial del proyecto
      uri: README.md
      version: versionada en repositorio
      estado: activo
    - nombre: Project Brief
      tipo: Definicion oficial del proyecto
      uri: project_brief.md
      version: versionada en repositorio
      estado: activo
    - nombre: Context References
      tipo: Indice oficial de contexto
      uri: docs/context_refs.md
      version: versionada en repositorio
      estado: activo
    - nombre: SDD Instructions
      tipo: Instrucciones de gobernanza
      uri: .github/instructions/sdd.instructions.md
      version: versionada en repositorio
      estado: activo
    - nombre: Analytical Use Case AUC-001 Meta Lead Quality Analysis
      tipo: Caso de uso analitico
      uri: analytical_use_cases/meta_lead_quality_analysis.md
      version: versionada en repositorio
      estado: activo
    - nombre: AUC-001 Execution Context
      tipo: Handoff documental
      uri: docs/handoffs/auc-001-execution-context.md
      version: versionada en repositorio
      estado: activo
    - nombre: AUC-001 Analysis Request
      tipo: Handoff documental
      uri: docs/handoffs/auc-001-analysis-request.md
      version: versionada en repositorio
      estado: activo
    - nombre: Meta Lead Quality Analysis Skill
      tipo: Skill
      uri: .github/skills/meta-lead-quality-analysis/SKILL.md
      version: versionada en repositorio
      estado: activo
    - nombre: Specifications del proyecto
      tipo: Specifications versionadas
      uri: specs/
      version: versionada en repositorio
      estado: activo
    - nombre: Tasks Backlog
      tipo: Governance
      uri: docs/tasks.md
      version: versionada en repositorio
      estado: activo
    - nombre: SDD Readiness Assessment
      tipo: Evaluation
      uri: sdd_readiness_assessment.md
      version: versionada en repositorio
      estado: activo
    - nombre: Phase Gate Record
      tipo: Governance
      uri: gates/spec-008-development-entry-phase-gate.md
      version: versionada en repositorio
      estado: activo
    - nombre: AUC-001 Closure Reconciliation Review
      tipo: Evaluation
      uri: docs/evaluations/auc-001-closure-reconciliation-review.md
      version: versionada en repositorio
      estado: activo
    - nombre: AUC-001 BigQuery MCP Integration Validation
      tipo: Evaluation
      uri: docs/evaluations/auc-001-bigquery-mcp-integration-validation.md
      version: versionada en repositorio
      estado: activo
    - nombre: SPEC-009 Analytical Use Case Completion / Acceptance Gate
      tipo: Specification
      uri: specs/spec-009-analytical-use-case-completion-acceptance-gate.md
      version: versionada en repositorio
      estado: activo

  indices_vectoriales: []

  bases_datos: []
```

---

# 9. Reglas de Carga de Contexto

Antes de crear o modificar cualquier artefacto del proyecto, se deben seguir estas reglas:

1. Consultar este archivo como indice oficial de contexto.
2. Revisar `.github/instructions/sdd.instructions.md` antes de proponer cambios de alcance, artefactos o evolucion de fase.
3. Revisar `README.md` y `project_brief.md` para mantener coherencia con el proposito, alcance y estado del proyecto.
4. Consultar `knowledge/client/` como fuente primaria de contexto persistente del proyecto.
5. Consultar `docs/glosario_terminos.md` antes de introducir nuevos terminos o redefinir artefactos.
6. Consultar las specifications, AUC-001, la skill asociada, tasks y gates cuando el cambio afecte a la linea analitica o a la gobernanza del proyecto.
7. No duplicar el contenido completo de la Knowledge Base ni de otras fuentes canonicas dentro de este documento.
8. No depender de memoria informal si existe una fuente publicada en el repositorio.
9. Marcar como `PENDING` solo aquello que realmente no exista o no este verificado.
10. Si existe conflicto entre fuentes, aplicar la precedencia documental oficial definida en `.github/instructions/sdd.instructions.md`.

---

# 10. Jerarquia de Contexto en Caso de Conflicto

La precedencia documental oficial del repositorio es la definida en `.github/instructions/sdd.instructions.md`.

Este documento la referencia y no la redefine.

---

# 11. Contexto Pendiente

No hay fuentes de contexto pendientes que bloqueen la evolucion actual del proyecto.

---

# 12. Trazabilidad

```yaml
trazabilidad:
  creado_por: GitHub Copilot
  fecha_creacion: 2026-07-10
  ultima_actualizacion: 2026-07-11
  actualizado_por: GitHub Copilot
  contexto_validado_por: Documentation Agent
  fecha_validacion: 2026-07-11
  version_contexto: vca-ia-contexto-oficial-development-authorized
```

---

# 13. Instruccion para Agentes IA

Antes de generar o modificar `project_brief.md`, specs, arquitectura, tasks, codigo o documentacion tecnica:

1. Leer este archivo.
2. Identificar las fuentes obligatorias.
3. Revisar decisiones relacionadas.
4. Revisar conocimiento reutilizable.
5. Revisar fuentes tecnicas relacionadas cuando aplique.
6. Revisar `knowledge/client/`, `README.md`, `project_brief.md`, `analytical_use_cases/`, la skill asociada, `docs/tasks.md` y los gates cuando el trabajo afecte al flujo analitico o a la transicion de fase.
7. Marcar cualquier ausencia de contexto como `PENDING` solo si la fuente realmente no existe o no esta publicada.
8. No inventar contexto de cliente, negocio, arquitectura, restricciones o decisiones si no esta documentado.
9. Registrar en este archivo cualquier nueva fuente relevante descubierta durante el proyecto.