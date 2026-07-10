# SDD instructions - jqf-sdd-foundation

## 1. Objetivo de estas instrucciones

Asegurar que el trabajo se mantiene en la metodologia SDD y respeta el plan aprobado del proyecto.

Estas instrucciones aplican a todo trabajo en repositorios basados en jqf-sdd-foundation hasta que se autorice expresamente el paso a Development.

## 2. Estado actual

Estado vigente:

- SDD -> Specification / Structure.

No estamos en Development.

## 3. Reglas SDD por fase

### 3.1 Specification

Permitido:

- definir alcance;
- definir limites;
- definir taxonomias;
- definir inputs y outputs dentro de la spec;
- definir restricciones y reglas de gobierno dentro de la spec;
- definir riesgos;
- definir criterios de salida de fase.

No permitido:

- implementar runtime;
- crear codigo de agentes;
- elegir framework;
- crear tools reales;
- crear workflows ejecutables.

### 3.2 Structure

Permitido:

- crear estructura de carpetas minima;
- crear archivos base de instrucciones, prompts y specs;
- normalizar naming y precedencia documental;
- preparar esqueletos no ejecutables.

No permitido:

- convertir estructura en implementacion tecnica;
- introducir automatizacion operativa;
- construir arquitectura distribuida.

### 3.3 Development

Solo permitido cuando exista aprobacion explicita y checklist de salida completado.

Hasta ese momento, cualquier implementacion queda fuera de alcance.

## 4. Comportamiento esperado durante Specification

- priorizar claridad de spec sobre soluciones tecnicas;
- mantener separación respecto a la Source of Truth funcional del proyecto;
- no duplicar logica funcional;
- no crear decisiones tecnologicas definitivas;
- marcar pendientes y riesgos cuando falte validacion.

Reglas de simplificacion documental:

- antes de crear un nuevo tipo de artefacto, comprobar si puede resolverse como seccion de una spec existente;
- no crear contracts separados salvo que sean transversales a varias capacidades o a todo el repositorio.

## 5. Restricciones actuales obligatorias

No hacer todavia:

- seleccion de framework;
- runtime;
- multiagente complejo;
- tools reales;
- workflows automaticos;
- codigo ejecutable de agentes.

## 6. Regla de control de alcance

Si una propuesta entra en implementacion, debe detenerse y volver a:

- spec;
- limites;
- evidencia documental;
- criterio de fase.

## 7. Criterio de cumplimiento

Estas instrucciones se consideran cumplidas cuando:

- el trabajo producido es documental;
- respeta el plan aprobado;
- mantiene estado Specification / Structure;
- no introduce implementacion prematura.

## 8. Backlog Governance

`docs/tasks.md` es un artefacto auxiliar de gobernanza.

No sustituye:

- specs;
- contracts transversales;
- skills;
- prompts;
- gates;
- evals.

Toda tarea registrada debe estar vinculada a:

- una fase SDD;
- un artefacto;
- una decision relevante;
- una futura linea de trabajo.

Las tareas deben representar trabajo significativo.

No deben representar actividad diaria.

Antes de crear nuevas tareas, comprobar si ya existe una tarea equivalente.

Antes de marcar una tarea como completada, verificar que el criterio de cierre se ha cumplido.

Si una tarea pierde relevancia o deja de aplicar, debe marcarse como descartada en lugar de eliminarse silenciosamente.

## Context Governance

`docs/context_refs.md` actúa como el mapa oficial de referencias de contexto del proyecto.

- Antes de crear o modificar cualquiera de los siguientes artefactos, revisar `docs/context_refs.md`:
	- Project Brief
	- Specifications
	- Architecture
	- Tasks
	- Código
	- Documentación técnica

- Si `docs/context_refs.md` existe:
	- utilizarlo como fuente oficial de referencias;
	- consultar las "fuentes obligatorias" indicadas en él;
	- respetar las versiones y estados documentados;
	- no inferir ni sustituir contexto cuando exista una fuente oficial publicada.

- Si `docs/context_refs.md` NO existe:
	- crearlo a partir de `docs/templates/context_refs.template.md`;
	- marcar las referencias faltantes como `PENDING` hasta su verificación.

- `context_refs.md` no debe duplicar contenido completo de CCDs, decisiones, actas de reuniones o documentación externa. Su función es actuar como índice, trazabilidad y mecanismo de carga de contexto, no como repositorio de copias completas.

- Regla explícita: Antes de generar cualquier Project Brief, Specification, Architecture o Tasks, comprobar la existencia de `docs/context_refs.md` y actuar conforme a su contenido.

## Precedencia documental oficial

Cuando exista conflicto entre artefactos del repositorio, aplicar este orden de precedencia:

1. `.github/instructions/sdd.instructions.md`
2. `.github/copilot-instructions.md`
3. `docs/context_refs.md`
4. `project_brief.md`
5. `specs/` versionadas y aplicables
6. `README.md`
7. `docs/glosario_terminos.md`
8. templates y artefactos auxiliares

Esta es la unica jerarquia oficial de precedencia documental del repositorio.

Los demas artefactos pueden referenciarla, pero no redefinirla ni mantener una version paralela.

## 9. SDD Harness

### 9.1 Rol del SDD Harness

El SDD Harness es el sistema de gobierno que define cómo se diseñan, documentan, revisan, validan y evolucionan las capacidades en repositorios basados en jqf-sdd-foundation.

Su función es garantizar que todo trabajo siga un proceso controlado, trazable y verificable antes de llegar a una fase de implementación.

El SDD Harness no define lógica funcional de negocio, no implementa agentes y no gobierna runtime, herramientas o infraestructura técnica.

Su responsabilidad es gobernar el proceso SDD.

Principios fundamentales:

- Human in the Loop.
- No implementación prematura.
- Trazabilidad documental.
- Evolución controlada.
- Source of Truth funcional del proyecto.
- Separación entre diseño e implementación.

---

### 9.2 Agentes metodológicos

El SDD Harness utiliza agentes metodológicos especializados para gobernar la evolución del repositorio.

Actualmente existen:

- Specification Agent
- Architect Agent
- Tasks Planner Agent
- Reviewer Agent
- Documentation Agent
- QA Gate Agent
- Implementation Agent
- GitHub Workflow Agent

Estos agentes no representan capacidades funcionales de negocio.

Su función es asistir el proceso SDD, asegurar coherencia documental, mantener trazabilidad y reducir el riesgo de implementación prematura.

La definición completa de cada agente se encuentra en:

```text
.github/agents/
```

---

### 9.3 Artefactos por fase

#### Specification

Artefactos permitidos:

- Project Brief
- Specifications
- Taxonomías
- Glosarios
- Instrucciones SDD
- Definición de alcance
- Definición de límites
- Riesgos
- Criterios de salida

Artefactos no requeridos todavía:

- Runtime
- Código
- Herramientas reales
- Workflows ejecutables

#### Structure

Artefactos permitidos:

- AGENTS.md
- Skills
- Prompts
- Gates
- Evals
- Workflows documentales
- Estructura de carpetas
- Reglas de precedencia
- Convenciones de naming

Los artefactos creados en esta fase deben permanecer documentales y no ejecutables.

#### Development

Solo puede iniciarse cuando exista aprobación explícita y se hayan cumplido los criterios de salida de las fases anteriores.

---

### 9.4 Gates

Los gates son puntos de control utilizados para determinar si una capacidad puede avanzar a la siguiente fase.

Su objetivo es impedir que el repositorio avance sin suficiente definición, evidencia o validación.

Un gate puede producir una de las siguientes decisiones:

- Pass
- Pass with conditions
- Fail
- Blocked

Un gate debe revisar, como mínimo:

- existencia de artefactos obligatorios;
- coherencia documental;
- trazabilidad;
- alineación con el estado SDD vigente;
- ausencia de implementación prematura.

Los gates nunca sustituyen la validación humana.

---

### 9.5 Precedencia documental

Cuando existan conflictos entre documentos, prevalece el artefacto de mayor nivel.

Orden de precedencia:

```text
Project Brief
↓
SDD Instructions
↓
Specifications
↓
Gates
↓
Skills
↓
Prompts
↓
Documentación auxiliar
```

Ningún artefacto puede contradecir a otro situado por encima en esta jerarquía.

Si se detecta una contradicción, debe resolverse actualizando el artefacto de mayor precedencia o eliminando la inconsistencia en los artefactos inferiores.

---

### 9.6 Definition of Done del SDD Harness

Una capacidad puede considerarse suficientemente madura dentro del SDD Harness cuando:

- existe una specification aprobada;
- el alcance está definido;
- los límites están definidos;
- existe trazabilidad documental;
- los riesgos relevantes están identificados;
- la capacidad puede ser revisada objetivamente;
- no existen contradicciones documentales conocidas;
- se mantiene alineación con la fase SDD vigente.

Hasta que estos criterios se cumplan, la capacidad no debe considerarse lista para Development.

---

### 9.7 Relación con Harness Engineering

El ecosistema "Harness" describe un conjunto de capacidades y responsabilidades relacionadas con la gobernanza, la ingeniería de procesos y la operación de políticas.

- SDD Harness: gobierna el diseño, la especificación, la revisión y la trazabilidad documental de capacidades definidas bajo SDD.
- Governance Harness: añade reglas, contracts y procesos transversales que aseguran coherencia entre proyectos y prácticas organizativas.
- Operational Harness: se ocupa de la ejecución y operación (runtimes, integraciones y fluxos operativos) y queda fuera del alcance de esta foundation.

Este repositorio gobierna diseño, documentación y validación; no contiene runtime, herramientas operativas ni implementaciones técnicas. Las decisiones y artefactos de operación deben residir en el Operational Harness o en proyectos derivados.
