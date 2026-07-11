# Context References

# Referencias de Contexto del Proyecto

> Este documento define las fuentes de contexto oficiales que deben consultarse antes de generar o modificar cualquier Project Brief, Spec, documento de Arquitectura, Tasks, codigo o documentacion tecnica de este proyecto.
>
> No duplica el contenido completo de otras fuentes. Actua como indice de referencias y trazabilidad del contexto utilizado por esta Foundation.
>
> Estado de transicion del proyecto derivado: PENDING adaptacion.

---

# 1. Identidad del Proyecto

```yaml
proyecto:
  nombre: Analytical Intelligence Foundation
  id_proyecto: AIF-FOUNDATION
  tipo_proyecto: Foundation reutilizable basada en SDD
  estado: Stable
  version: v1.0.0
  fecha_creacion: 2026-07-10
  responsable: Foundation maintainers

cliente:
  id_cliente: N/A
  nombre_cliente: N/A
  estado_relacion: No aplica
```

---

# 2. Contexto de Cliente Requerido

## CCD - Client Context Document

```yaml
ccd:
  requerido: false

  fuente_humana:
    sistema: N/A
    ubicacion: N/A

  fuente_runtime_ia:
    sistema: N/A
    uri: N/A

  version: N/A
  estado: No aplica
  ultima_revision: N/A
  fecha_consulta: 2026-07-10
```

## Notas sobre el uso del CCD

- Esta Foundation no esta asociada a un cliente concreto.
- No debe inferirse conocimiento de negocio especifico desde fuentes externas no publicadas en el repositorio.
- Cualquier proyecto derivado debera inicializar su propio CCD o marcarlo como PENDING segun corresponda.

---

# 3. Decisiones Relacionadas

> La fuente oficial de decisiones para esta Foundation son sus artefactos documentales versionados en el repositorio.

| Fecha | Decision | Impacto en este proyecto | Fuente |
| --- | --- | --- | --- |
| 2026-07-10 | Mantener la Foundation como repositorio metodologico, sin implementacion productiva | Limita el alcance a metodologia, gobernanza, templates y artefactos reutilizables | .github/copilot-instructions.md |
| 2026-07-10 | Mantener independencia respecto a dominio, runtime y proveedor tecnologico | Condiciona alcance, arquitectura conceptual y criterios de exito | README.md |
| 2026-07-10 | Mantener materializado el roadmap fundacional inicial en las specs 001-007, los gates documentales y el dossier de compatibilidad ya publicados, sin ampliar alcance funcional | Consolida la secuencia de evolucion documental ya resuelta y evita reabrir decisiones de alcance ya cerradas | README.md; specs/spec-001-analytical-lifecycle.md; specs/spec-002-component-boundaries.md; specs/spec-003-extensibility-model.md; specs/spec-004-transversal-contracts.md; specs/spec-005-readiness-gates.md; specs/spec-006-documentary-evaluations.md; specs/spec-007-extension-compatibility-reusability.md |
| 2026-07-11 | Publicar la Foundation como version estable v1.0.0 | Marca el primer corte estable documental del repositorio sin modificar su estado SDD en Specification / Structure | README.md; project_brief.md |
| 2026-07-11 | Validar el caso de uso AUC-001 y la skill meta-lead-quality-analysis como primer caso analitico trazable de VCA IA | Deja constancia documental de la evidencia base para iniciar la linea de trabajo analitica del proyecto | analytical_use_cases/meta_lead_quality_analysis.md; .github/skills/meta-lead-quality-analysis/SKILL.md |

## Decisiones pendientes de validar

No hay decisiones pendientes de validar sobre el roadmap inicial de evolucion fundacional con la informacion actualmente publicada en el repositorio.

---

# 4. Proyectos Relacionados

| Proyecto | Relacion con este proyecto | Estado | Fuente |
| --- | --- | --- | --- |
| jqf-sdd-foundation | Base metodologica y de gobernanza sobre la que se define esta Foundation | Activo | README.md |

---

# 5. Reuniones Relacionadas

| Fecha | Reunion | Informacion relevante | Fuente |
| --- | --- | --- | --- |
| PENDING | PENDING | No hay actas versionadas en el repositorio para esta inicializacion | PENDING |

---

# 6. Conocimiento Reutilizable Relacionado

| Recurso | Tipo | Motivo de uso | Fuente |
| --- | --- | --- | --- |
| Project Brief Template | Template | Estructura oficial del project brief | docs/templates/project_brief.template.md |
| Context References Template | Template | Estructura oficial de referencias de contexto | docs/templates/context_refs.template.md |
| Extension Compatibility Dossier Template | Template | Estructura oficial para documentar compatibilidad y reutilización de extensiones | docs/templates/extension_compatibility_dossier.template.md |
| Analytical Use Case AUC-001 | Caso de uso | Caso de uso analítico fuente para validar VCA IA y definir la primera capability analítica | analytical_use_cases/meta_lead_quality_analysis.md |
| Meta Lead Quality Analysis Skill | Skill | Skill reutilizable asociada al caso de uso AUC-001 | .github/skills/meta-lead-quality-analysis/SKILL.md |
| Tasks Backlog | Governance | Backlog auxiliar de trabajo trazable para la Foundation | docs/tasks.md |
| Glosario SDD | Documentacion | Definiciones oficiales de artefactos y terminos | docs/glosario_terminos.md |
| SDD Harness Instructions | Instrucciones | Reglas de fase, alcance y contexto | .github/instructions/sdd.instructions.md |

---

# 7. Fuentes Tecnicas Relacionadas

## Repositorios

```yaml
repositorios:
  - nombre: aif-foundation
    url: https://github.com/joquifer2/analytical-intelligence-foundation.git
    rama: main
    descripcion: Repositorio Foundation reutilizable para metodologia y gobernanza de inteligencia analitica
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
apis: []
```

---

# 8. Fuentes Runtime para Agentes IA

> Esta Foundation no define fuentes runtime operativas. Solo documenta referencias metodologicas y de gobernanza.

```yaml
runtime_sources:

  documentos_publicados:
    - nombre: README
      tipo: Documentacion fundacional
      uri: README.md
      version: versionada en repositorio
      estado: activo
    - nombre: Project Brief
      tipo: Definicion fundacional
      uri: project_brief.md
      version: versionada en repositorio
      estado: activo
    - nombre: SDD Instructions
      tipo: Instrucciones de gobernanza
      uri: .github/instructions/sdd.instructions.md
      version: versionada en repositorio
      estado: activo
    - nombre: SPEC-001 Analytical Lifecycle
      tipo: Specification fundacional
      uri: specs/spec-001-analytical-lifecycle.md
      version: versionada en repositorio
      estado: activo
    - nombre: SPEC-002 Component Boundaries
      tipo: Specification fundacional
      uri: specs/spec-002-component-boundaries.md
      version: versionada en repositorio
      estado: activo
    - nombre: SPEC-003 Extensibility Model
      tipo: Specification fundacional
      uri: specs/spec-003-extensibility-model.md
      version: versionada en repositorio
      estado: activo
    - nombre: SPEC-004 Transversal Contracts
      tipo: Specification fundacional
      uri: specs/spec-004-transversal-contracts.md
      version: versionada en repositorio
      estado: activo
    - nombre: SPEC-005 Readiness Gates
      tipo: Specification fundacional
      uri: specs/spec-005-readiness-gates.md
      version: versionada en repositorio
      estado: activo
    - nombre: SPEC-006 Documentary Evaluations
      tipo: Specification fundacional
      uri: specs/spec-006-documentary-evaluations.md
      version: versionada en repositorio
      estado: activo
    - nombre: SPEC-007 Extension Compatibility and Reusability
      tipo: Specification fundacional
      uri: specs/spec-007-extension-compatibility-reusability.md
      version: versionada en repositorio
      estado: activo
    - nombre: Analytical Use Case AUC-001 Meta Lead Quality Analysis
      tipo: Caso de uso analitico
      uri: analytical_use_cases/meta_lead_quality_analysis.md
      version: versionada en repositorio
      estado: activo
    - nombre: Meta Lead Quality Analysis Skill
      tipo: Skill
      uri: .github/skills/meta-lead-quality-analysis/SKILL.md
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
3. Revisar `README.md` para mantener coherencia con el proposito y limites de la Foundation.
4. Consultar `docs/glosario_terminos.md` antes de introducir nuevos artefactos o redefinir terminos.
5. Usar templates oficiales antes de crear variantes de documentos.
6. No introducir implementacion productiva, runtime ni tecnologia ejecutable dentro de la Foundation.
7. Marcar cualquier ausencia de contexto relevante como `PENDING`.
8. No depender de memoria informal si existe una fuente publicada en el repositorio.
9. Si existe conflicto entre fuentes, aplicar la precedencia documental oficial definida en `.github/instructions/sdd.instructions.md`.

---

# 10. Jerarquia de Contexto en Caso de Conflicto

La precedencia documental oficial del repositorio se define exclusivamente en `.github/instructions/sdd.instructions.md`.

Este documento debe remitir a esa jerarquia y no mantener una version paralela.

---

# 11. Contexto Pendiente

No hay fuentes de contexto pendientes que bloqueen o introduzcan ambiguedad material sobre el roadmap inicial de evolucion fundacional con la informacion actualmente publicada en el repositorio.

---

# 12. Trazabilidad

```yaml
trazabilidad:
  creado_por: GitHub Copilot
  fecha_creacion: 2026-07-10
  ultima_actualizacion: 2026-07-10
  actualizado_por: GitHub Copilot
  ultima_actualizacion: 2026-07-11
  actualizado_por: GitHub Copilot
  contexto_validado_por: PENDING
  fecha_validacion: PENDING
  version_contexto: inicial-roadmap-extension-compatibility-resuelto
```

---

# 13. Instruccion para Agentes IA

Antes de generar o modificar `project_brief.md`, specs, arquitectura, tasks, codigo o documentacion tecnica:

1. Leer este archivo.
2. Identificar las fuentes obligatorias.
3. Revisar decisiones relacionadas.
4. Revisar conocimiento reutilizable.
5. Revisar fuentes tecnicas relacionadas cuando aplique.
6. Marcar cualquier ausencia de contexto como `PENDING`.
7. No inventar contexto de cliente, negocio, arquitectura, restricciones o decisiones si no esta documentado.
8. Registrar en este archivo cualquier nueva fuente relevante descubierta durante el proyecto.