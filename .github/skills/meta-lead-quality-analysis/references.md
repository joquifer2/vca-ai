# References — Meta Lead Quality Analysis

## Propósito

Este documento declara las referencias oficiales que deben consultarse antes de ejecutar el caso de uso AUC-001.

Su objetivo es centralizar las dependencias documentales del caso de uso y evitar que la skill replique continuamente rutas o referencias.

No sustituye la Skill.

No sustituye el Runbook.

No sustituye los contratos.

No define comportamiento operativo.

---

# Referencias obligatorias

## Caso de uso

- `analytical_use_cases/meta_lead_quality_analysis.md`

Define:

- objetivo;
- alcance;
- criterios de éxito;
- límites funcionales.

---

## Contexto oficial

- `docs/context_refs.md`

Punto de entrada oficial para localizar el resto del contexto del proyecto.

Debe consultarse antes de adquirir evidencia.

---

## Contratos

### Data Contract

Determina:

- Data Providers autorizados;
- tablas autorizadas;
- campos autorizados;
- restricciones de adquisición.

---

### Presentation Contract

Determina:

- restricciones de representación;
- invariantes de presentación;
- límites de Presentation Layer.

### BigQuery MCP discover_metadata Contract Reference

- `docs/contracts/bigquery-mcp-discover-metadata.contract.md`

Registra el schema real observado del servidor MCP para `discover_metadata`, sus selectores canonicos, ejemplos validos e invalidos, codigos de error y estados de salida de la Fase 05.

Esta referencia no redefine el contrato del servidor. Debe refrescarse desde `tools/list` cuando el BigQuery MCP Server cambie su schema.

---

## Contexto de negocio

Obligatorio para restricciones contextuales locales de AUC-001:

- `knowledge/client/ccd.md`
- `analytical_use_cases/auc-001/faro-strategic-context-profile.json`

Cuando esten disponibles y apliquen:

- FARO
- CLARO
- KPIs oficiales
- `project_brief.md`

Estas referencias contienen las definiciones funcionales y de negocio que prevalecen sobre cualquier inferencia realizada desde el modelo de datos. El contenido normativo del CCD no debe duplicarse. Las restricciones ejecutables necesarias para AUC-001 se materializan en el perfil local y se transportan mediante `strategic_context_constraints` con referencias trazables a `knowledge/client/ccd.md`.

---

## Specifications

La ejecución deberá respetar todas las Specifications aprobadas aplicables.

En particular:

- Execution Scope Canonicalization
- Presentation Projection Selection (SPEC-010)
- Communication Context Representation Transformation (SPEC-011)
- AUC-001 Analytical Product Contract (SPEC-014)
- AUC-001 Canonical Projection Consolidation (SPEC-015)
- AUC-001 Operational Acceptance Package Contract (SPEC-016)

La skill no necesita reinterpretarlas.

Debe asumirlas como capacidades disponibles del framework.

---

## Perfiles de Knowledge Generation

Durante la Fase 09 del Runbook deben consultarse:

- `.github/skills/meta-lead-quality-analysis/ANALYTICAL_PROFILE.md`
- `.github/skills/meta-lead-quality-analysis/knowledge-construction-profile.md`

Estos perfiles guian el programa interno de investigacion analitica y la consolidacion del Knowledge Set.

No sustituyen el Evidence Set.

No introducen evidencia nueva.

No autorizan recomendaciones dentro de Knowledge Generation.

---

## Presentation Policies

Cuando corresponda a la solicitud:

### Analytical

- `.github/presentation_policies/analytical-review.md`

---

### Executive

- `.github/presentation_policies/executive-decision-support.md`

Las Presentation Policies únicamente modifican la representación del contenido canónico.

No modifican:

- evidencia;
- conocimiento;
- recomendaciones;
- prioridades;
- coverage states.

---

## Artefactos canónicos esperados

Antes de Presentation Layer deberán existir:

- Context Definition
- Evidence Set
- Knowledge Set
- Recommendation Set
- Coverage Matrix y Common Product Core conforme a SPEC-014
- Canonical Projection Source conforme a SPEC-015

Cuando una ejecucion persista paquete fisico, tambien deberan existir los artefactos operativos definidos por SPEC-016: preflight MCP, Evidence Acquisition Record completo, manifests, fingerprints, trazabilidad fisica, resultados de validacion, higiene de namespace y handoff verificable.

Estos artefactos serán construidos siguiendo `RUNBOOK.md`.

Las Presentation Policies consumirán estos artefactos.

No deberán reconstruirlos.

---

## Data Provider autorizado

El Data Provider autorizado para este caso de uso es el definido por el Data Contract vigente.

El runtime resolverá el mecanismo de acceso utilizando las capacidades disponibles en el entorno.

Todas las consultas deberán limitarse a las fuentes publicadas por el Data Contract.

La disponibilidad técnica de una fuente no implica autorización metodológica.

Para `discover_metadata`, AUC-001 debe utilizar exclusivamente el contrato canonico documentado en `docs/contracts/bigquery-mcp-discover-metadata.contract.md`. No se permiten selectores con prefijo de proyecto, valores legacy plurales de `scope_request`, nombres logicos inferidos ni pruebas sucesivas de formatos.

Para llamadas `query_read_only` del BigQuery MCP Server, `execution_context` es un contrato cerrado y no un contenedor de trazabilidad. Debe construirse solo con:

```yaml
execution_context:
  project_id: <authorized_project_id>
  dataset_id: <authorized_dataset_id>
  max_bytes_billed: <workspace_cost_limit_bytes>
```

En el workspace `vca`, `project_id` debe ser `datamart-vca-494114` y `max_bytes_billed` debe ser `1073741824`.

El `dataset_id` debe ser `intermediate` para consultas sobre `datamart-vca-494114.intermediate.*` y `marts` para consultas sobre `datamart-vca-494114.marts.*`.

No incluir dentro de `execution_context`: `workspace_id`, `table_id`, `purpose`, `request_id`, `resource_selector`, `location`, `auth_mode` ni ningun otro campo descriptivo o no soportado. `request_id` debe permanecer en el nivel superior de la llamada; la SQL debe permanecer en `sql_query`; la trazabilidad adicional debe documentarse en artefactos de ejecucion o auditoria.

---


## Artefactos historicos y gaps fuera del flujo principal

Los outputs historicos y experimentales pueden consultarse para auditoria, comparacion metodologica o trazabilidad cuando la solicitud lo autorice, pero no son Evidence nueva ni expected values de una ejecucion actual.

Permanecen fuera del flujo operativo principal hasta nueva evidencia o decision separada: revenue/CRM, causalidad creativa, metadata creativa adicional, temporalidad limitada por proveedor y gap MCP multi-tabla.
---

## Prioridad de referencias

En caso de conflicto prevalecerá el siguiente orden:

1. Specifications aprobadas.
2. Contratos.
3. Caso de uso.
4. Contexto oficial.
5. Runbook.
6. Presentation Policies.
7. Skill.

---

## Definition of Done

Las referencias se consideran correctamente resueltas cuando:

- todas las dependencias obligatorias han sido localizadas;
- los contratos aplicables han sido identificados;
- el Data Provider autorizado ha sido confirmado;
- la Presentation Policy adecuada ha sido localizada cuando corresponda.