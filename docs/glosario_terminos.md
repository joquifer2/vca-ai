# Glosario de términos — SDD, Harness Engineering y Analytical Intelligence Foundation

## 1. Objetivo

Este glosario define los conceptos fundamentales utilizados en repositorios basados en **Specification Driven Development (SDD)** y, en particular, en **Analytical Intelligence Foundation (AIF)**.

Su objetivo es proporcionar un vocabulario común para:

- reducir ambigüedades;
- mejorar la trazabilidad;
- mantener coherencia entre artefactos;
- facilitar la evolución controlada de sistemas basados en agentes;
- separar claramente contexto, datos, evidencia, conocimiento, recomendaciones y presentación.

Este documento no define lógica de negocio, SOPs ni reglas funcionales específicas de un cliente o proyecto derivado.

---

## 2. Conceptos fundamentales

### Analytical Intelligence Foundation (AIF)

Foundation metodológica reutilizable para estructurar procesos analíticos realizados por agentes de IA.

AIF define un ciclo común para transformar contexto y datos en evidencia, conocimiento, recomendaciones y artefactos de salida, manteniendo separación de responsabilidades, trazabilidad y neutralidad tecnológica.

### Foundation

Repositorio reutilizable que proporciona metodología, gobernanza, agentes metodológicos, templates, contracts y artefactos base para futuros proyectos.

Una Foundation no representa por sí misma una implementación productiva ni un proyecto de cliente.

### Proyecto derivado

Proyecto creado a partir de una Foundation.

Instancia y adapta los artefactos fundacionales a un caso de uso concreto, un dominio, un cliente o una implementación determinada.

### Core fundacional

Conjunto de principios, fases, límites, reglas y artefactos comunes que deben permanecer estables para preservar la reutilización de la Foundation.

Una extensión puede ampliar o especializar el core, pero no alterar sus responsabilidades fundamentales ni eliminar fases obligatorias.

### Source of Truth

Sistema, repositorio o documento considerado la referencia canónica para una determinada información.

Toda información derivada debe alinearse con su Source of Truth correspondiente.

### Context Governance

Sistema de reglas que determina cómo se identifican, referencian, cargan y utilizan las fuentes oficiales de contexto dentro de un proyecto.

Su objetivo es evitar dependencia de memoria informal, reducir inconsistencias y garantizar trazabilidad.

### Context References

Documento que actúa como índice oficial de las fuentes de contexto de un proyecto.

No almacena el conocimiento completo: referencia las fuentes que deben consultarse antes de generar o modificar artefactos relevantes.

Ubicación habitual:

```text
docs/context_refs.md
```

### Client Context Document (CCD)

Documento maestro que concentra el conocimiento relevante de un cliente.

Puede incluir negocio, objetivos, restricciones, ecosistema tecnológico, definiciones oficiales, KPIs, decisiones relevantes y aprendizajes reales.

### Human-in-the-loop

Principio según el cual las decisiones relevantes requieren validación humana.

Los agentes asisten el trabajo humano, pero no sustituyen la responsabilidad final de decisión.

### UNKNOWN

Estado explícito utilizado cuando una información, supuesto, comportamiento o dependencia no puede verificarse con la evidencia disponible.

Un UNKNOWN no debe completarse mediante inferencia informal.

### Trazabilidad

Capacidad de reconstruir el origen, transformación, relación y justificación de una decisión, hallazgo, contract o artefacto.

### Auditabilidad

Capacidad de revisar de forma independiente qué fuentes, criterios, reglas y decisiones dieron lugar a un resultado.

### Readiness

Nivel de preparación suficiente para avanzar de fase o hito sin introducir ambigüedades significativas.

La readiness se evalúa mediante criterios explícitos, evidencia y gates.

### Definition of Done

Conjunto de condiciones que deben cumplirse para considerar un artefacto, capacidad, evaluación o fase como completada.

### Criterio de aceptación

Condición verificable que permite determinar si una specification o capacidad cumple el comportamiento definido.

### Precedencia documental

Regla que determina qué artefacto prevalece cuando existe una contradicción entre documentos.

La jerarquía oficial no debe duplicarse en distintos documentos. Debe consultarse en:

```text
.github/instructions/sdd.instructions.md
```

### Coherencia documental transversal

Consistencia global entre artefactos relacionados del repositorio.

Incluye dependencias, referencias cruzadas, terminología, preguntas abiertas, consideraciones futuras, índices y documentos de contexto.

### Impacto transversal entre artefactos

Conjunto de cambios que una modificación documental puede provocar sobre otros artefactos del repositorio.

También puede denominarse **Cross-Artifact Impact**.

---

## 3. Artefactos SDD

### Project Brief

Documento inicial que describe el propósito, problema, alcance, exclusiones, contexto, restricciones, riesgos y criterios de éxito de un proyecto o Foundation.

### Specification (Spec)

Artefacto principal para definir una capacidad, agente, componente o marco metodológico.

Una specification establece qué debe conseguirse, qué incluye, qué excluye, qué reglas se aplican, qué riesgos existen y cómo se valida.

### Retrospective Specification

Specification que reconstruye el comportamiento actual de un sistema existente.

Describe el estado **As-Is**, no introduce funcionalidades futuras y marca como UNKNOWN aquello que no puede verificarse.

### Contract

Artefacto que formaliza expectativas de intercambio entre productores y consumidores.

En AIF, un contract no implica necesariamente un schema técnico ejecutable. Puede ser un acuerdo documental sobre propósito, inputs, outputs, campos críticos, reglas de validación y trazabilidad.

### Contract transversal

Contract reutilizable que conecta múltiples fases, componentes o extensiones de la Foundation sin depender de una tecnología o dominio concreto.

### Instructions

Reglas de comportamiento aplicables a asistentes, agentes o herramientas de IA.

No sustituyen specifications, contracts ni lógica funcional del proyecto.

### Prompt

Instrucción o patrón de interacción utilizado para obtener un comportamiento determinado de un modelo.

No sustituye una specification.

### Skill

Extensión reutilizable que aporta conocimiento, criterios o comportamiento especializado para una tarea o dominio.

En AIF, una Skill puede enriquecer análisis o razonamiento, pero no alterar el lifecycle común ni reasignar responsabilidades fundacionales.

### Skill metodológica

Skill utilizada para gobernar o apoyar el proceso SDD.

### Skill operativa

Skill utilizada para ejecutar trabajo funcional o de negocio.

### Routine

Extensión reutilizable que encapsula un procedimiento común aplicable en varias Skills o proyectos.

Una Routine debe definirse por un proceso generalizable, no por una necesidad puntual de un único caso.

### Template

Estructura reutilizable utilizada para crear artefactos consistentes.

Un Template define forma y organización, pero no debe introducir evidencia, razonamiento o decisiones nuevas.

### Workflow

Secuencia documentada de pasos para alcanzar un resultado.

Durante Specification y Structure, los workflows deben permanecer documentales y no ejecutables.

### Eval

Término genérico para un artefacto de evaluación.

En AIF se concreta mediante el marco de **Documentary Evaluations**.

### Gate

Punto formal de control utilizado para decidir si una capacidad, fase o conjunto de artefactos puede avanzar.

### Handoff

Transferencia controlada de un artefacto entre fases o componentes.

Todo handoff debe declarar qué se entrega, quién lo produce, quién lo consume y qué precondiciones deben cumplirse.

### Analysis Request

Artefacto que normaliza la solicitud analitica concreta antes de su instanciacion como Execution Context.

Captura objetivo, salida esperada, audiencia, restricciones y trazabilidad hacia la intencion humana.

No resuelve el contexto oficial ni produce evidencia.

### Execution Context

Artefacto de ejecución que normaliza la solicitud operativa de una corrida concreta antes de la resolución del contexto oficial.

Captura objetivo, periodo, alcance pedido, filtros, audiencia, definición operativa solicitada y trazabilidad hacia la intención humana.

No produce evidencia ni reemplaza el Context Resolution ni el Context Contract.

### Artefacto canónico

Documento reconocido como referencia principal para una definición o decisión concreta.

### Related Artifacts

Sección de una specification que identifica otros artefactos relacionados y explica su relación.

### Dependencies

Sección que declara los documentos, decisiones, componentes o capacidades de los que depende un artefacto.

### Open Questions

Preguntas todavía no resueltas que deben permanecer explícitas hasta disponer de decisión o evidencia suficiente.

### Future Considerations

Posibles evoluciones futuras que no forman parte del alcance actual ni deben interpretarse como trabajo ya aprobado.

---

## 4. Agentes

### Agent

Entidad responsable de una función estable dentro del sistema.

Un agente posee objetivo, responsabilidades, límites y criterios de actuación.

### Agente metodológico

Agente utilizado para gobernar el ciclo SDD.

No representa una capacidad funcional de negocio.

### Specification Agent

Agente metodológico responsable de transformar ideas, necesidades o problemas en specifications claras, acotadas y verificables.

### Architect Agent

Agente metodológico responsable de definir o revisar arquitectura, límites, componentes, relaciones y decisiones técnicas dentro de la fase autorizada.

### Tasks Planner Agent

Agente metodológico responsable de transformar artefactos aprobados en tareas trazables y secuenciadas.

En proyectos derivados, puede preparar la descomposicion operativa cuando la fase correspondiente lo permita, sin introducir ejecucion dentro de la Foundation.

### Reviewer Agent

Agente metodológico responsable de revisar artefactos, detectar contradicciones, ambigüedades, riesgos y falta de trazabilidad.

No debe corregir silenciosamente aquello que revisa ni sustituir la decisión humana final.

### Documentation Agent

Agente metodológico responsable de crear, ordenar y mantener documentación clara, navegable y alineada con los artefactos existentes.

También mantiene la coherencia documental transversal sin redefinir decisiones funcionales o técnicas.

### QA Gate Agent

Agente metodológico responsable de evaluar gates y recomendar si una capacidad puede avanzar, requiere cambios o queda bloqueada.

### Implementation Agent

Agente metodológico responsable de implementar cambios técnicos únicamente cuando la fase Development está autorizada.

### GitHub Workflow Agent

Agente metodologico retirado del catalogo activo de `vca-ai`. GitHub se conserva como herramienta de soporte y trazabilidad bajo autorizacion humana cuando proceda, no como fase metodologica independiente.

### Agente operativo

Agente diseñado para ejecutar trabajo funcional o de negocio.

---

## 5. Harness Engineering

### Harness

Sistema que gobierna, controla y valida el comportamiento de agentes y capacidades mediante reglas, estados, transiciones, controles y responsabilidades.

### SDD Harness

Sistema de gobierno documental utilizado para diseñar, revisar, validar y evolucionar capacidades mediante Specification Driven Development.

Gobierna agentes, specifications, skills, prompts, workflows, evaluaciones y gates.

No gobierna runtime ni infraestructura productiva.

### Governance Harness

Conjunto de reglas y mecanismos transversales que garantizan coherencia, trazabilidad, control de cambios y cumplimiento de políticas.

### Design Harness

Harness orientado al diseño y definición de capacidades antes de la implementación.

### Operational Harness

Harness responsable de la operación real de agentes, integraciones, herramientas, políticas y controles en ejecución.

### Runtime Harness

Capa que gobierna la ejecución técnica de agentes, herramientas y orquestadores.

Queda fuera del alcance documental de AIF en su fase actual.

---

## 6. Fases SDD

### Proposed

Estado inicial de una idea o capacidad pendiente de definición.

### Specification

Fase destinada a definir alcance, límites, objetivos, restricciones, riesgos y criterios de aceptación.

No permite implementación técnica.

### Structure

Fase destinada a organizar carpetas, artefactos, templates, naming, precedencia y estructuras no ejecutables.

### Development

Fase de implementación técnica.

Solo puede iniciarse tras aprobación explícita y cumplimiento de los gates correspondientes.

### Validation

Fase destinada a comprobar que la implementación cumple los requisitos definidos.

### Active

Estado de una capacidad aprobada y en uso.

### Deprecated

Estado de una capacidad retirada o en proceso de sustitución.

### As-Is

Descripción verificable del estado actual de un sistema, proceso o arquitectura.

### To-Be

Descripción del estado futuro deseado y aprobado.

---

## 7. Analytical Lifecycle de AIF

### Analytical Lifecycle

Ciclo metodológico común de AIF para transformar contexto y datos en conocimiento accionable.

Está compuesto por:

1. Contexto
2. Discovery
3. Preparación
4. Análisis
5. Razonamiento
6. Recomendaciones
7. Constructor de Informes

### Contexto

Fase que delimita el objetivo del análisis, la decisión a soportar, las restricciones y las fuentes oficiales de contexto.

### Discovery

Fase que identifica datasets, entidades, dimensiones, métricas, relaciones y limitaciones relevantes antes de preparar los datos.

### Preparación

Fase que transforma los datos identificados en un modelo analítico coherente, interpretable y apto para producir evidencia.

### Análisis

Fase que produce hallazgos observables a partir del modelo analítico sin convertirlos todavía en conclusiones o recomendaciones.

### Razonamiento

Fase que transforma evidencia en conocimiento explícito: insights, hipótesis, oportunidades, riesgos, prioridades e incertidumbres.

### Recomendaciones

Fase que convierte el conocimiento priorizado en acciones sugeridas, justificadas y evaluables.

### Constructor de Informes

Fase final que representa conocimiento y recomendaciones ya validados en el formato de salida requerido.

No puede introducir nueva evidencia, interpretación o recomendación.

### Context Definition

Salida estructurada de la fase Contexto.

Declara objetivo, alcance, restricciones, decisión soportada y fuentes oficiales de contexto.

### Discovery Model

Descripción lógica de datasets, entidades, relaciones, métricas y limitaciones relevantes para el análisis.

### Analytical Model

Datos preparados y organizados bajo un modelo coherente, interpretable y apto para producir evidencia.

### Evidence Set

Conjunto de hallazgos observables obtenidos durante el análisis.

Debe permanecer separado de interpretaciones y recomendaciones.

### Knowledge Set

Conjunto de insights, hipótesis, prioridades, conclusiones e incertidumbres respaldadas por evidencia.

### Recommendation Set

Conjunto de acciones sugeridas con su justificación, impacto esperado, esfuerzo, dependencias, riesgos y trazabilidad.

### Output Artifact

Representación final del conocimiento y las recomendaciones en el formato solicitado.

---

## 8. Componentes y límites de AIF

### Framework

Coordinador metodológico del lifecycle analítico.

Valida secuencia, completitud y precondiciones de handoff, pero no sustituye a las capas ni actúa como runtime productivo.

### Data Provider

Componente responsable de adquirir información desde una fuente externa y exponerla mediante contracts.

No interpreta datos ni formula conclusiones.

### Analytical Layer

Capa responsable de preparar datos y producir evidencia observable.

No introduce conclusiones de negocio ni recomendaciones.

### Reasoning Layer

Capa responsable de convertir evidencia en conocimiento accionable.

No debe reconsultar la fuente original para compensar evidencia mal definida.

### Presentation Layer

Capa responsable de construir artefactos finales a partir de conocimiento y recomendaciones ya generados.

No crea evidencia ni reinterpreta conclusiones.

### Template Builder

Componente que transforma conocimiento aprobado en un artefacto de salida utilizando una estructura determinada.

### Component Boundary

Límite explícito que separa las responsabilidades de dos o más componentes.

### Boundary Constraint

Restricción que impide que un componente asuma responsabilidades pertenecientes a otra capa.

### Boundary Compliance

Cumplimiento verificable de los límites y responsabilidades definidos entre componentes.

### Responsibility Map

Mapa que documenta la responsabilidad principal de cada componente y aquello que no debe hacer.

### Handoff Rules

Reglas que establecen qué artefactos pueden intercambiarse entre componentes y qué precondiciones deben cumplirse.

### Receiver Preconditions

Condiciones que debe cumplir un artefacto antes de ser aceptado por el componente receptor.

### Sender Exit Condition

Condición que debe cumplir el componente emisor antes de considerar completado un handoff.

### Coordination Principles

Principios que regulan cómo el Framework coordina fases y componentes sin sustituir sus responsabilidades.

---

## 9. Contracts transversales de AIF

### Context Contract

Contract que formaliza objetivo, restricciones, decisión soportada y fuentes de contexto aplicables.

### Data Contract

Contract que describe la información entregada por un Data Provider antes del trabajo analítico.

### Data Provider Contract

Especialización o uso del Data Contract para definir cómo un proveedor expone datos al sistema analítico.

### Discovery Contract

Contract que formaliza el Discovery Model y sus limitaciones.

### Analytical Contract

Contract que formaliza el Analytical Model resultante de la preparación.

### Evidence Contract

Contract que formaliza hallazgos observables separados de interpretación.

### Knowledge Contract

Contract que formaliza insights, hipótesis, prioridades, conclusiones e incertidumbres.

### Recommendation Contract

Contract que formaliza acciones sugeridas y su justificación.

### Presentation Contract

Contract que delimita el contenido aprobado que puede consumir la Presentation Layer.

### Extension Contract

Contract que declara inputs, outputs y restricciones introducidas por una extensión sin alterar el core.

### Producer

Componente, capa o artefacto que emite un contract.

### Consumer

Componente, capa o artefacto que recibe y utiliza un contract.

### Critical Fields

Campos o bloques mínimos cuya ausencia invalida un contract.

### Validation Rules

Reglas utilizadas para comprobar la completitud, consistencia y utilizabilidad de un contract.

### Traceability Links

Referencias que conectan un contract, gate o evaluación con sus fuentes, evidencias y artefactos relacionados.

### Unknown Handling

Reglas que indican cómo deben documentarse ausencias, limitaciones o estados UNKNOWN.

### Ruptura controlada

Cambio incompatible que se declara, documenta y gestiona de forma explícita en lugar de introducirse silenciosamente.

---

## 10. Readiness Gates

### Readiness Gate

Categoría general de gate utilizada para validar que una fase, artefacto o hito está suficientemente preparado para avanzar.

### Phase Gate

Gate que valida el avance entre fases SDD.

### Artifact Gate

Gate que valida la suficiencia de un artefacto o conjunto de artefactos.

### Boundary Gate

Gate que valida que se preservan límites y responsabilidades entre componentes.

### Contract Gate

Gate que valida que los contracts requeridos existen, son completos y pueden utilizarse.

### Evaluation Gate

Especialización de Readiness Gate orientada a comprobar si existe evidencia suficiente para emitir una decisión.

### Gate Scope

Alcance del gate: fase, artefacto, contract, boundary, evaluación u otro hito definido.

### Required Artifacts

Artefactos obligatorios que deben existir para poder evaluar un gate.

### Required Evidence

Evidencia mínima que debe observarse para emitir una decisión.

### Pass Criteria

Condiciones mínimas que permiten considerar superado un gate.

### Block Criteria

Condiciones que obligan a fallar o bloquear un gate.

### Decision Model

Conjunto normalizado de decisiones que puede emitir un gate.

### Pass

Decisión que indica que el gate se ha superado sin condiciones relevantes.

### Pass with minor conditions

Decisión que permite avanzar con condiciones menores claramente documentadas.

### Fail — changes required

Decisión que impide superar el gate hasta corregir defectos relevantes.

### Blocked

Decisión que indica que el gate no puede evaluarse o superarse por ausencia de evidencia, artefactos o decisiones críticas.

### Riesgo residual

Riesgo que permanece incluso después de superar un gate.

---

## 11. Evaluaciones documentales

### Documentary Evaluation

Artefacto estructurado utilizado para evaluar suficiencia, coherencia, trazabilidad y riesgos de specs, contracts, gates, boundaries o contexto.

No sustituye la aprobación humana final.

### Artifact Evaluation

Evaluación centrada en la suficiencia y coherencia de uno o varios artefactos.

### Gate Evaluation

Evaluación que determina si un gate dispone de base documental suficiente para emitir una decisión.

### Contract Evaluation

Evaluación que comprueba si un contract es utilizable, trazable y compatible con el marco fundacional.

### Boundary Evaluation

Evaluación que comprueba si se preservan límites, handoffs y responsabilidades.

### Context Evaluation

Evaluación que determina si el contexto disponible es suficiente y coherente para continuar.

### Readiness Evaluation

Categoría general de evaluación que determina si el estado documental permite avanzar.

### Assessment Model

Modelo que separa observaciones, hallazgos, gaps, riesgos y recomendaciones dentro de una evaluación documental.

### Observation

Hecho documental directamente observable.

### Finding

Interpretación controlada derivada de una o más observaciones.

### Gap

Información faltante, insuficiente o no verificable.

### Risk

Consecuencia potencial derivada de un gap, contradicción o limitación.

### Recommendation

Acción sugerida para corregir una deficiencia, reducir un riesgo o permitir el avance.

### Decision Support

Evidencia documental que apoya, condiciona o bloquea una decisión de gate.

### Evaluation Scope

Artefacto, gate, contract, boundary o contexto concreto que se evalúa.

### Source Artifacts

Artefactos utilizados como evidencia o fuente durante una evaluación.

---

## 12. Extensibilidad

### Extensión

Elemento que amplía o especializa la Foundation sin modificar el core metodológico.

Las categorías reconocidas son Skill, Routine, Template y Contract.

### Extensibility Model

Marco general que define cómo pueden incorporarse extensiones compatibles y reutilizables.

### Extension Author

Responsable de declarar el propósito, superficie, inputs, outputs, límites y dependencias de una extensión.

### System Surface

Parte del sistema que una extensión amplía o especializa.

También puede denominarse **Core Surface** en el contexto de un dossier.

### Boundary Impact

Impacto que una extensión puede producir sobre límites, capas o responsabilidades fundacionales.

### Domain Dependence

Dependencias de dominio introducidas por una extensión.

### Reuse Rationale

Justificación de por qué una extensión puede reutilizarse más allá de un caso puntual.

### Core Preservation

Regla que exige que una extensión no elimine fases ni modifique el núcleo metodológico.

### Boundary Preservation

Regla que exige que una extensión no reasigne responsabilidades entre componentes.

### Domain Containment

Regla que exige que el conocimiento específico de dominio permanezca encapsulado en la extensión correspondiente.

### Technology Neutrality

Propiedad según la cual una extensión, contract o artefacto no impone una tecnología, proveedor o runtime obligatorio al core.

### Compatible Extension

Extensión que respeta lifecycle, boundaries, contracts, trazabilidad y neutralidad tecnológica.

### Reusable Extension

Extensión compatible cuyo valor puede aplicarse de forma plausible en más de un caso de uso.

### Case-Specific Extension

Extensión limitada a un único contexto o necesidad puntual y que no debe presentarse como reutilizable.

### Extension Compatibility Dossier

Artefacto fundacional utilizado para documentar y evaluar la compatibilidad y reutilización de una extensión concreta.

### Extension Profile

Sección del dossier que identifica la extensión, su categoría, propósito y superficie del sistema.

### Compatibility Profile

Sección del dossier que declara límites, contracts y dependencias permitidas o prohibidas.

### Reusability Profile

Sección del dossier que declara casos de uso plausibles y condiciones de reutilización.

### Review Summary

Sección del dossier que recoge observaciones, hallazgos, gaps, riesgos, recomendaciones y decisión documental.

### Compatibility Statement

Declaración explícita de compatibilidad de una extensión con el core fundacional.

### Reuse Statement

Declaración explícita de reutilización más allá de un único caso.

### Allowed Dependencies

Dependencias que una extensión puede utilizar sin comprometer su compatibilidad.

### Forbidden Dependencies

Dependencias que una extensión no puede asumir porque romperían límites, neutralidad o reutilización.

---

## 13. Plantillas reutilizables

### Project Brief Template

Plantilla utilizada para iniciar nuevos proyectos o Foundations.

### Specification Template

Plantilla utilizada para crear specifications consistentes.

### Contracts Template

Plantilla utilizada para documentar contracts con una estructura común.

### Extension Compatibility Dossier Template

Plantilla utilizada para documentar compatibilidad y reutilización de una extensión concreta.

### Template instanciado

Artefacto real creado a partir de una plantilla para un proyecto, evaluación o extensión concreta.

La existencia de un template no implica que deba crearse automáticamente una instancia.

---

## 14. Regla anti-sobreingeniería documental

Antes de crear un nuevo tipo de artefacto:

1. comprobar si puede resolverse dentro de una specification existente;
2. evitar duplicación documental;
3. evitar crear contracts innecesarios;
4. priorizar simplicidad, trazabilidad y mantenibilidad;
5. comprobar el impacto sobre artefactos relacionados.

---

## 15. Checklist rápido de uso

- Para definir una capacidad: crear o actualizar una Specification.
- Para definir el contexto: actualizar Project Brief y Context References.
- Para formalizar un intercambio: utilizar un Contract.
- Para encapsular conocimiento de dominio: utilizar una Skill.
- Para encapsular un procedimiento reusable: utilizar una Routine.
- Para estructurar un artefacto: utilizar un Template.
- Para validar avance: utilizar un Gate.
- Para evaluar evidencia documental: utilizar una Documentary Evaluation.
- Para documentar una extensión concreta: utilizar un Extension Compatibility Dossier.
- Para resolver conflictos documentales: consultar la precedencia oficial en `sdd.instructions.md`.

---

## 16. Cierre

Este glosario prioriza:

- claridad;
- simplicidad;
- separación de responsabilidades;
- trazabilidad;
- gobernanza;
- coherencia transversal;
- evolución controlada;
- reutilización.

Su propósito es servir como referencia común para AIF y para cualquier repositorio construido o derivado de `jqf-sdd-foundation`.

