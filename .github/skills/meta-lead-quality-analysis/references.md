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

---

## Contexto de negocio

Cuando estén disponibles:

- CCD
- FARO
- CLARO
- KPIs oficiales
- `project_brief.md`

Estas referencias contienen las definiciones funcionales y de negocio que prevalecen sobre cualquier inferencia realizada desde el modelo de datos.

---

## Specifications

La ejecución deberá respetar todas las Specifications aprobadas aplicables.

En particular:

- Execution Scope Canonicalization
- Presentation Projection Selection (SPEC-010)
- Communication Context Representation Transformation (SPEC-011)

La skill no necesita reinterpretarlas.

Debe asumirlas como capacidades disponibles del framework.

---

## Presentation Policies

Cuando corresponda a la solicitud:

### Analytical

- `presentation-policies/analytical-review.md`

---

### Executive

- `presentation-policies/executive-decision-support.md`

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

Estos artefactos serán construidos siguiendo `RUNBOOK.md`.

Las Presentation Policies consumirán estos artefactos.

No deberán reconstruirlos.

---

## Data Provider autorizado

El Data Provider autorizado para este caso de uso es el definido por el Data Contract vigente.

El runtime resolverá el mecanismo de acceso utilizando las capacidades disponibles en el entorno.

Todas las consultas deberán limitarse a las fuentes publicadas por el Data Contract.

La disponibilidad técnica de una fuente no implica autorización metodológica.

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