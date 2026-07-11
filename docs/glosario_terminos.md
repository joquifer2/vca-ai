# Glosario de términos - SDD, Harness Engineering y Artefactos

## 1. Objetivo

Este glosario define los conceptos fundamentales utilizados en repositorios basados en SDD (Specification Driven Development).

Su objetivo es proporcionar un vocabulario común para reducir ambigüedades, mejorar la trazabilidad y facilitar la evolución controlada de sistemas basados en agentes.

No define lógica de negocio, SOPs ni reglas funcionales específicas de ningún proyecto.

---

## 2. Conceptos fundamentales

### Source of Truth

Sistema, repositorio o documento considerado la referencia canónica para una determinada información.

Toda información derivada debe alinearse con su Source of Truth correspondiente.

Ejemplos:

* reglas de negocio;
* procesos operativos;
* taxonomías;
* definiciones funcionales.

---

### Context Governance

Sistema de reglas que determina cómo se identifican, referencian, cargan y utilizan las fuentes oficiales de contexto dentro de un proyecto.

Su objetivo es evitar dependencia de memoria informal, reducir inconsistencias y garantizar trazabilidad de las fuentes de contexto utilizadas.

### Context References

Documento que actúa como índice oficial de las fuentes de contexto de un proyecto. No almacena el conocimiento completo; referencia las fuentes que deben consultarse antes de generar o modificar artefactos relevantes.

Ubicación recomendada:

docs/context_refs.md

### Client Context Document (CCD)

Documento maestro que concentra el conocimiento relevante de un cliente. Puede incluir negocio, objetivos, restricciones, ecosistema tecnológico, definiciones oficiales, KPIs, decisiones relevantes y lecciones aprendidas.

Cuando exista, el CCD debe considerarse la fuente principal de contexto del cliente.

---

### Human-in-the-loop

Principio según el cual las decisiones relevantes requieren validación humana.

Los agentes asisten el trabajo humano, pero no sustituyen la responsabilidad final de decisión.

---

### Readiness

Nivel de preparación suficiente para avanzar de fase sin introducir ambigüedades significativas.

La readiness se evalúa mediante criterios explícitos y gates.

---

### Definition of Done

Conjunto de condiciones que deben cumplirse para considerar un artefacto, capacidad o fase como completada.

---

## 3. Artefactos SDD

### Project Brief

Documento inicial que describe:

* propósito del proyecto;
* problema a resolver;
* alcance;
* límites;
* riesgos;
* contexto;
* criterios de éxito.

Es el punto de partida de cualquier proceso SDD.

---

### Specification (Spec)

Artefacto principal para definir una capacidad, agente o componente.

Una specification responde a:

* qué es;
* qué debe hacer;
* qué límites tiene;
* qué inputs acepta;
* qué outputs genera;
* qué reglas debe respetar.

Una specification puede incluir:

* propósito;
* alcance;
* responsabilidades;
* restricciones;
* riesgos;
* criterios de aceptación;
* Definition of Done.

---

### Contract

Documento que define reglas transversales compartidas por múltiples capacidades o por el repositorio completo.

Un contract solo debe existir cuando la regla afecta a múltiples artefactos.

Ejemplos:

* política de memoria;
* política de herramientas;
* reglas Human-in-the-loop;
* precedencia documental;
* resolución de conflictos.

---

### Instructions

Reglas de comportamiento para asistentes, agentes o herramientas de IA.

Definen cómo debe comportarse el sistema dentro de un contexto determinado.

Las instructions:

* no sustituyen specifications;
* no sustituyen contracts;
* no contienen lógica funcional de negocio.

---

### Prompt

Instrucción o patrón de interacción utilizado para obtener un comportamiento específico de un modelo.

Un prompt no define capacidades completas ni sustituye una specification.

---

### Skill

Procedimiento reutilizable diseñado para ejecutar una tarea concreta.

Una skill encapsula conocimiento operativo repetible.

Ejemplos:

* git-sync;
* revisión documental;
* preparación de commits;
* validación de naming.

---

### Skill metodológica

Skill utilizada para gobernar o apoyar el proceso SDD.

Ejemplos:

* git-sync;
* revisión de artefactos;
* preparación de documentación.

---

### Skill operativa

Skill utilizada por agentes funcionales para ejecutar trabajo de negocio.

Ejemplos:

* generación de informes;
* clasificación de incidencias;
* análisis de datos.

---

### Workflow

Secuencia documentada de pasos para alcanzar un resultado determinado.

Un workflow puede ser conceptual o ejecutable.

Durante Specification y Structure se permiten únicamente workflows documentales.

---

### Eval

Artefacto utilizado para validar calidad, comportamiento o cumplimiento de requisitos.

Las evaluaciones permiten medir si una capacidad cumple lo esperado.

---

### Gate

Punto formal de validación utilizado para decidir si una capacidad puede avanzar a la siguiente fase.

Un gate puede:

* aprobar;
* aprobar con condiciones;
* solicitar cambios;
* bloquear.

---

## 4. Agentes

### Agent

Entidad responsable de una función estable dentro del sistema.

Un agente posee:

* objetivo;
* responsabilidades;
* límites;
* criterios de actuación.

---

### Agente metodológico

Agente utilizado para gobernar el ciclo SDD.

No representa capacidades de negocio.

Ejemplos:

* Specification Agent;
* Architect Agent;
* Tasks Planner Agent;
* Reviewer Agent;
* Documentation Agent;
* QA Gate Agent;
* Implementation Agent;
* GitHub Workflow Agent.

---

### Agente operativo

Agente diseñado para ejecutar trabajo funcional o de negocio.

Ejemplos:

* agente de reporting;
* agente de forecasting;
* agente de análisis comercial;
* agente de atención al cliente.

---

## 5. Harness Engineering

### Harness

Sistema que gobierna, controla y valida el comportamiento de agentes y capacidades.

Un harness define:

* reglas;
* estados;
* transiciones;
* controles;
* validaciones;
* responsabilidades.

---

### SDD Harness

Sistema de gobierno documental utilizado para diseñar, revisar, validar y evolucionar capacidades mediante Specification Driven Development.

Gobierna:

* agentes;
* specifications;
* skills;
* prompts;
* workflows;
* evaluaciones;
* gates.

No gobierna runtime ni infraestructura.

---

### Governance Harness

Conjunto de reglas y mecanismos que garantizan coherencia, trazabilidad y control de cambios.

Su foco principal es la gobernanza.

---

### Design Harness

Harness orientado al diseño y definición de capacidades antes de la implementación.

El SDD Harness es un ejemplo de Design Harness.

---

### Operational Harness

Harness utilizado para controlar agentes operativos en ejecución.

Puede incluir:

* herramientas;
* observabilidad;
* validaciones automáticas;
* monitorización;
* gestión de errores.

---

### Runtime Harness

Capa que gobierna la ejecución real de agentes y herramientas.

Puede incluir:

* runtimes de agentes;
* orquestadores;
* sistemas de evaluación automática;
* observabilidad.

---

## 6. Fases SDD

### Proposed

Idea inicial pendiente de definición.

---

### Specification

Fase destinada a definir:

* alcance;
* límites;
* objetivos;
* riesgos;
* criterios de aceptación.

No se permite implementación técnica.

---

### Structure

Fase destinada a organizar:

* carpetas;
* artefactos;
* precedencia documental;
* estructuras no ejecutables.

No se permite implementación técnica.

---

### Development

Fase de implementación técnica.

Solo puede iniciarse tras aprobación explícita.

---

### Validation

Fase destinada a comprobar que la implementación cumple los requisitos definidos.

---

### Active

Estado de una capacidad aprobada y en uso.

---

### Deprecated

Estado de una capacidad retirada o en proceso de sustitución.

---

## 7. Plantillas reutilizables

### Project Brief Template

Plantilla utilizada para iniciar nuevos proyectos.

Archivo recomendado:

```text
docs/templates/project_brief.template.md
```

---

### Specification Template

Plantilla utilizada para crear specifications consistentes.

Archivo recomendado:

```text
specs/templates/spec.template.md
```

Las plantillas proporcionan estructura.

El razonamiento y definición del contenido corresponde a los agentes metodológicos.

---

## 8. Regla anti-sobreingeniería documental

Antes de crear un nuevo tipo de artefacto:

1. comprobar si puede resolverse dentro de una specification existente;
2. evitar duplicación documental;
3. evitar crear contracts innecesarios;
4. priorizar simplicidad y trazabilidad.

---

## 9. Precedencia documental

La única referencia autorizada para resolver conflictos entre artefactos es la sección **Precedencia documental oficial** de `.github/instructions/sdd.instructions.md`.

Este glosario no redefine ni replica esa jerarquía.

Si un término entra en conflicto con otro artefacto, debe aplicarse exclusivamente la precedencia oficial y corregirse la inconsistencia en la fuente afectada.

---

## 10. Checklist rápido de uso

* Si necesitas definir una capacidad → crea o actualiza una Specification.
* Si necesitas definir el contexto de un proyecto → actualiza el Project Brief.
* Si necesitas gobernar una fase SDD → utiliza el agente metodológico correspondiente.
* Si necesitas una regla transversal → evalúa crear un Contract.
* Si necesitas un procedimiento reutilizable → crea una Skill.
* Si necesitas comportamiento contextual → utiliza Instructions.
* Si necesitas validación de avance → utiliza un Gate.
* Si necesitas comprobar calidad → utiliza una Eval.

---

## 11. Cierre

Este glosario prioriza:

* claridad;
* simplicidad;
* trazabilidad;
* gobernanza;
* evolución controlada.

Su propósito es servir como referencia común para cualquier repositorio construido sobre `jqf-sdd-foundation`.

