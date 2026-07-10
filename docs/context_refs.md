# Context References

# Referencias de Contexto del Proyecto

> Este documento define las fuentes de contexto oficiales que deben consultarse antes de generar o modificar cualquier Project Brief, Spec, documento de Arquitectura, Tasks, codigo o documentacion tecnica de este proyecto.
>
> No duplica el contenido completo de otras fuentes. Actua como indice de referencias y trazabilidad del contexto utilizado por esta Foundation.

---

# 1. Identidad del Proyecto

```yaml
proyecto:
  nombre: Analytical Intelligence Foundation
  id_proyecto: AIF-FOUNDATION
  tipo_proyecto: Foundation reutilizable basada en SDD
  estado: Proposed
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

## Decisiones pendientes de validar

| Tema | Motivo de la duda | Responsable | Estado |
| --- | --- | --- | --- |
| Roadmap de adopcion inicial | El orden de priorizacion de capacidades fundacionales no esta aprobado formalmente | Foundation maintainers | PENDING |

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
| Glosario SDD | Documentacion | Definiciones oficiales de artefactos y terminos | docs/glosario_terminos.md |
| SDD Harness Instructions | Instrucciones | Reglas de fase, alcance y contexto | .github/instructions/sdd.instructions.md |

---

# 7. Fuentes Tecnicas Relacionadas

## Repositorios

```yaml
repositorios:
  - nombre: aif-foundation
    url: PENDING
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
    - nombre: SDD Instructions
      tipo: Instrucciones de gobernanza
      uri: .github/instructions/sdd.instructions.md
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
9. Si existe conflicto entre fuentes, aplicar la jerarquia definida en este documento.

---

# 10. Jerarquia de Contexto en Caso de Conflicto

Cuando exista conflicto entre fuentes, aplicar este orden:

1. `.github/instructions/sdd.instructions.md`
2. `.github/copilot-instructions.md`
3. `README.md`
4. `docs/glosario_terminos.md`
5. `project_brief.md`
6. Templates y artefactos auxiliares

---

# 11. Contexto Pendiente

| Fuente pendiente | Motivo | Impacto | Responsable | Estado |
| --- | --- | --- | --- | --- |
| URL canonica del repositorio | No aparece en el contexto disponible | Baja | Foundation maintainers | PENDING |
| Acta o decision formal de roadmap | No existe referencia versionada en el repositorio | Media | Foundation maintainers | PENDING |

---

# 12. Trazabilidad

```yaml
trazabilidad:
  creado_por: GitHub Copilot
  fecha_creacion: 2026-07-10
  ultima_actualizacion: 2026-07-10
  actualizado_por: GitHub Copilot
  contexto_validado_por: PENDING
  fecha_validacion: PENDING
  version_contexto: inicial
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