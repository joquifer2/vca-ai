# Specification

## Metadata

### Spec ID

SPEC-003

### Title

Extensibility Model

### Status

Draft

### Owner

Foundation maintainers

### Last Updated

2026-07-10

---

## 1. Purpose

Definir como puede ampliarse AIF mediante Skills, Routines, Templates y Contracts sin modificar el nucleo metodologico comun ni introducir acoplamiento con dominios o tecnologias concretas.

---

## 2. Background

El Project Brief establece que la Foundation debe ser extensible y que el conocimiento de dominio pertenece a las Skills. Esta specification concreta que puede extenderse, que debe permanecer estable y que condiciones debe cumplir una extension compatible.

La documentación y evaluación de una extensión concreta no pertenece a esta spec general. Ese rol se formaliza en SPEC-007 mediante el Extension Compatibility Dossier.

---

## 3. Objective

Esta capacidad debe conseguir que nuevos dominios, casos de uso y necesidades de salida puedan incorporarse sobre la Foundation reutilizando el mismo proceso comun.

El resultado debe ser un modelo de extension controlada que permita evolucionar el sistema sin reescribir el nucleo metodologico.

---

## 4. Scope

### Included

- definicion del rol de Skills, Routines, Templates y Contracts en la extensibilidad;
- reglas de compatibilidad entre extensiones y nucleo comun;
- restricciones para evitar que una extension altere metodologia fundacional;
- criterios minimos para considerar una extension reusable.

### Excluded

- implementacion concreta de una Skill de dominio;
- documentacion o evaluacion detallada de una extension concreta mediante un dossier instanciado;
- catalogo exhaustivo de extensiones futuras;
- packaging tecnico o mecanismo de despliegue de extensiones;
- logica de negocio especifica.

---

## 5. Actors

| Actor | Description |
| --- | --- |
| Foundation Core | Metodo comun que debe permanecer estable y reusable |
| Skill Author | Define conocimiento especifico de dominio compatible con la Foundation |
| Routine Author | Define procedimientos reutilizables aplicables en multiples Skills |
| Template Author | Define estructuras de artefactos finales sin alterar el analisis |
| Contract Author | Define estructuras estandarizadas para desacoplar componentes |
| Reviewer | Valida que la extension respete principios y limites fundacionales |

---

## 6. Inputs

| Input | Description |
| --- | --- |
| Core Methodology | Principios, ciclo de vida y limites fundacionales de AIF |
| Domain Knowledge | Reglas, metricas y definiciones propias de una Skill |
| Reusable Procedure Need | Necesidad de encapsular un proceso repetible como Routine |
| Output Structure Need | Necesidad de representar conocimiento en un formato determinado |
| Boundary Requirements | Reglas de desacoplamiento y handoff entre componentes |

---

## 7. Outputs

| Output | Description |
| --- | --- |
| Extension Categories | Definicion de tipos de extension admitidos |
| Compatibility Rules | Reglas que una extension debe respetar para ser valida |
| Stability Rules | Elementos del nucleo que no pueden modificarse desde una extension |
| Reuse Criteria | Criterios minimos para considerar una extension reusable |

---

## 7.1 Extension Declaration Requirements

Toda extension candidata debe declararse mediante un artefacto reutilizable que incluya, como minimo, los siguientes campos:

| Field | Required Content |
| --- | --- |
| Extension Name | Nombre unico y estable de la extension |
| Extension Category | Skill, Routine, Template o Contract |
| Purpose | Problema que resuelve y valor que aporta |
| System Surface | Parte del sistema que amplifica o especializa |
| Inputs | Artefactos, contratos o contexto requeridos |
| Outputs | Artefactos, conocimiento o estructuras que produce |
| Applicable Phase | Fase o fases del ciclo comun en las que aplica |
| Domain Dependence | Dependencias de dominio que introduce, si existen |
| Boundary Impact | Limites que debe respetar y capas que no puede invadir |
| Reuse Rationale | Motivo por el que la extension es reusable y no puntual |
| Unknowns | Huecos, supuestos o incertidumbres declaradas |

---

## 7.2 Extension Review Rules

Una extension solo puede considerarse compatible cuando supera las siguientes comprobaciones:

| Review Check | Expected Result |
| --- | --- |
| Core Preservation | No elimina fases ni altera la secuencia metodologica comun |
| Boundary Preservation | No reasigna responsabilidades entre componentes fundacionales |
| Input/Output Clarity | Declara inputs y outputs de forma explicita y revisable |
| Domain Containment | Mantiene el conocimiento de dominio encapsulado dentro de la extension |
| Technology Neutrality | No impone una tecnologia obligatoria al core fundacional |
| Reuse Test | Su valor no depende de un unico caso puntual no generalizable |
| Traceability | Permite rastrear su efecto sobre evidencia, conocimiento o presentacion |
| Unknown Handling | Declara estados UNKNOWN o supuestos cuando falta contexto verificable |

---

## 7.3 Stability Rules For The Core

- el ciclo de vida comun definido por la Foundation no puede ser acortado ni reordenado por una extension;
- los limites entre adquisicion, analisis, razonamiento y presentacion no pueden ser alterados;
- una extension no puede mover conocimiento de dominio al nucleo metodologico comun;
- ningun Template puede introducir logica analitica nueva;
- ninguna Routine reusable puede asumir dependencias obligatorias sobre una unica tecnologia del core.

---

## 7.4 Reuse Criteria

Para considerarse reusable, una extension debe cumplir como minimo lo siguiente:

- aplica a mas de un caso de uso plausible dentro de la metodologia;
- se describe por su procedimiento, estructura o regla general y no por un incidente aislado;
- puede revisarse sin depender de conocimiento tacito no documentado;
- explicita que parte del sistema amplifica y que parte permanece inalterada.

---

## 8. Functional Requirements

### FR-001

La Foundation debe permitir Skills que aporten conocimiento de dominio, equivalencias, metricas y recomendaciones especificas sin cambiar la metodologia comun.

### FR-002

La Foundation debe permitir Routines reutilizables que implementen procedimientos comunes de discovery, preparacion, analisis, razonamiento o presentacion.

### FR-003

La Foundation debe permitir Templates dedicados a estructurar artefactos finales sin introducir logica analitica ni conocimiento nuevo.

### FR-004

La Foundation debe permitir Contracts que definan expectativas de intercambio entre componentes y reduzcan acoplamiento.

### FR-005

Una extension compatible no debe eliminar fases del ciclo comun ni reasignar responsabilidades fundacionales entre componentes.

### FR-006

Una Skill debe poder especializar interpretacion y recomendaciones de dominio, pero no incorporar dependencias obligatorias sobre una unica fuente de datos o tecnologia del core.

### FR-007

Toda extension debe declarar de forma explicita que parte del sistema amplifica, que inputs necesita y que outputs produce.

---

## 9. Business Rules

### BR-001

El conocimiento de dominio pertenece a las Skills, no al nucleo fundacional.

### BR-002

La metodologia comun prevalece sobre cualquier extension.

### BR-003

Una Routine reusable debe definirse por procedimiento comun, no por necesidad puntual de un unico dominio.

### BR-004

Si una extension necesita inventar evidencia o inferir contexto no documentado, debe marcarlo como UNKNOWN o quedar fuera de cumplimiento.

---

## 10. Constraints

- la extensibilidad debe seguir siendo documental en esta fase del repositorio;
- no se deben introducir mecanismos operativos de instalacion o ejecucion;
- el nucleo debe permanecer independiente de cliente, dominio y proveedor tecnologico;
- las extensiones deben poder revisarse mediante criterios reutilizables, no decisiones ad hoc.

---

## 11. Assumptions

- diferentes dominios compartiran suficientes patrones como para reutilizar la misma metodologia comun;
- habra valor en reutilizar Routines y Templates entre multiples Skills;
- los Contracts pueden actuar como mecanismo principal de desacoplamiento sin requerir tecnologia concreta.

---

## 12. Risks

| Risk | Impact | Notes |
| --- | --- | --- |
| Permitir extensiones que muten el core | Alto | Rompe estabilidad y reutilizacion |
| Crear Routines demasiado especificas | Medio | Reduce reuso y aumenta duplicacion |
| Confundir templates con logica de analisis | Alto | Mezcla presentacion con razonamiento |

---

## 13. Acceptance Criteria

### AC-001

La spec define al menos cuatro categorias de extension y su rol diferenciado.

### AC-002

La spec deja explicito que las Skills amplian conocimiento y no la metodologia comun.

### AC-003

La spec fija condiciones claras para que una extension no rompa el ciclo ni los limites fundacionales.

---

## 14. Dependencies

- project_brief.md;
- docs/context_refs.md;
- spec-001-analytical-lifecycle.md;
- spec-002-component-boundaries.md;
- spec-004-transversal-contracts.md.

---

## 15. Open Questions

- que metadata adicional convendria especializar por categoria mas alla del dossier general definido en SPEC-007;
- si convendra instanciar un gate especifico de compatibilidad para extensiones concretas cuando el volumen crezca;
- que contracts fundacionales convendria instanciar primero para maximizar reuso entre extensiones.

---

## 16. Future Considerations

- crear templates dedicados para Skills, Routines y Contracts;
- aplicar SPEC-007 para documentar y evaluar extensiones concretas sin duplicar reglas generales de extensibilidad;
- instanciar gates y evaluaciones apoyandose en SPEC-005 y SPEC-006 cuando una extension concreta lo requiera.

---

## 17. Related Artifacts

| Artifact | Relationship |
| --- | --- |
| project_brief.md | Define el proposito y alcance fundacional |
| docs/context_refs.md | Fuente oficial de contexto utilizada para esta spec |
| spec-001-analytical-lifecycle.md | Define el proceso comun que las extensiones deben respetar |
| spec-002-component-boundaries.md | Define los limites que ninguna extension debe romper |
| spec-004-transversal-contracts.md | Define contracts reutilizables que las extensiones pueden requerir o producir |
| spec-007-extension-compatibility-reusability.md | Define como documentar y evaluar una extension concreta sin redefinir el modelo general |

---

## Definition of Done

La specification esta completa cuando:

- el objetivo esta definido;
- el alcance esta definido;
- los limites estan definidos;
- los inputs estan definidos;
- los outputs estan definidos;
- los requisitos funcionales estan definidos;
- las reglas principales estan documentadas;
- los riesgos relevantes estan identificados;
- existen criterios de aceptacion verificables.