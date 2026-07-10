# Project Brief

## 1. Project Overview

### Project Name

Analytical Intelligence Foundation

### Working Title

AIF

### Status

Proposed

### Owner

Foundation maintainers

### Last Updated

2026-07-10

---

## 2. Purpose

Analytical Intelligence Foundation existe para convertir el razonamiento analitico experto en una metodologia reutilizable, modular y trazable, en lugar de depender de prompts aislados dificilmente mantenibles.

El proyecto busca resolver la fragmentacion habitual de los analisis asistidos por LLMs, donde cada caso obliga a rehacer instrucciones, mezclar conocimiento de negocio con logica analitica y tratar el informe final como objetivo principal en lugar de resultado.

Merece ser construido porque establece una base comun para transformar datos en conocimiento accionable con evidencia, explicabilidad y reutilizacion entre dominios sin atarse a una tecnologia concreta.

---

## 3. Business Context

El contexto de esta Foundation es metodologico, no operativo ni sectorial. Se orienta a proyectos que necesitan analizar datos con asistencia de IA preservando separacion entre adquisicion de datos, analisis, razonamiento y presentacion.

La Foundation no incorpora conocimiento de negocio, clientes, SOPs ni implementaciones productivas. Su funcion es proporcionar el marco comun sobre el que proyectos derivados puedan definir Skills, Specs, artefactos y gobierno sin romper la coherencia metodologica.

---

## 4. Problem Statement

Hoy muchos analisis asistidos por IA se construyen como prompts monoliticos, especificos de un unico problema y con escasa capacidad de evolucion.

Las limitaciones principales son:

- el conocimiento analitico queda encapsulado en instrucciones ad hoc;
- el razonamiento no se reutiliza entre dominios o proyectos;
- la logica de negocio y la logica analitica se mezclan;
- la evidencia y las conclusiones no siempre quedan claramente separadas;
- los artefactos de salida tienden a condicionar el proceso analitico.

Las consecuencias son baja mantenibilidad, duplicacion de trabajo, dificultad para auditar conclusiones y mayor riesgo de acoplar la solucion a una fuente de datos, herramienta o dominio concreto.

---

## 5. Desired Outcome

El resultado esperado es una Foundation documental y metodologica que defina un proceso analitico comun, extensible y reutilizable para futuros proyectos de inteligencia analitica asistida por IA.

Sabremos que el proyecto ha tenido exito cuando permita modelar el ciclo completo desde contexto hasta recomendaciones, separar claramente hechos, evidencia e interpretacion, y habilitar Skills de dominio sin modificar el nucleo metodologico.

---

## 6. Scope

### In Scope

- definicion de principios de diseno y principios arquitectonicos de la Foundation;
- definicion del ciclo de vida analitico comun;
- definicion de componentes reutilizables como Framework, Skills, Routines, Templates y Contracts;
- definicion de criterios de extensibilidad, trazabilidad y evidencia;
- documentacion y gobierno SDD necesarios para evolucion controlada.

### Out of Scope

- implementaciones productivas o runtime de agentes;
- conocimiento de negocio, cliente o dominio especifico;
- integraciones ejecutables con fuentes de datos, APIs o plataformas externas;
- herramientas concretas de BI, ETL, dashboarding o RAG;
- automatizacion de informes como objetivo principal del sistema.

---

## 7. Users and Stakeholders

### Primary Users

- equipos que disenan proyectos de inteligencia analitica asistida por IA;
- responsables metodologicos que necesitan una base reusable para proyectos derivados;
- autores de Skills y Specifications que extenderan la Foundation.

### Secondary Users

- revisores documentales y responsables de gates de readiness;
- equipos de implementacion en proyectos derivados;
- analistas que necesiten trazabilidad entre evidencia, insights y recomendaciones.

### Stakeholders

- Foundation maintainers;
- responsables de gobernanza SDD;
- futuros equipos de proyectos derivados que reutilizaran la Foundation.

---

## 8. Assumptions

- existe valor en separar metodologia analitica de conocimiento de dominio;
- los proyectos derivados necesitaran reutilizar una misma estructura de razonamiento con datos y contextos distintos;
- la independencia respecto a tecnologia y proveedor es un requisito estrategico de la Foundation;
- la evidencia debe poder trazarse hasta las conclusiones y recomendaciones;
- la primera validacion practica de la metodologia se realizara mas adelante mediante una Skill derivada, no dentro de esta Foundation.

---

## 9. Constraints

Las restricciones conocidas son:

- el repositorio esta en fase Specification / Structure, no en Development;
- la Foundation debe permanecer documental y no ejecutable;
- no se puede introducir conocimiento de cliente ni logica de negocio especifica;
- no se deben fijar dependencias obligatorias en una tecnologia, proveedor o runtime concretos;
- el alcance debe mantenerse generico y reutilizable para proyectos derivados.

---

## 10. Risks

| Risk | Impact | Notes |
| --- | --- | --- |
| Convertir la Foundation en un pseudo framework tecnico | Alto | Romperia la independencia metodologica y el alcance SDD actual |
| Mezclar conocimiento de dominio con metodologia comun | Alto | Reduciria reutilizacion y aumentaria acoplamiento |
| Definir conceptos demasiado abstractos sin capacidad de aplicacion posterior | Medio | Puede dificultar la adopcion en proyectos derivados |
| Priorizar formatos de salida sobre el proceso analitico | Medio | Debilita el principio de que el analisis precede al informe |
| Falta de trazabilidad entre evidencia y recomendaciones | Alto | Debilita explicabilidad y auditabilidad del sistema |

---

## 11. Source of Truth

| Source | Purpose |
| --- | --- |
| .github/instructions/sdd.instructions.md | Definir reglas de fase, alcance y gobierno SDD |
| .github/copilot-instructions.md | Definir restricciones especificas de Foundation y precedencia metodologica |
| README.md | Describir el proposito, limites y estructura de la Foundation |
| docs/glosario_terminos.md | Mantener consistencia terminologica de los artefactos |

### Context References

Documento de referencias de contexto utilizado:

docs/context_refs.md

Fuentes principales consultadas:

- README del repositorio.
- Instrucciones SDD de la Foundation.
- Copilot instructions del repositorio.
- Template oficial de Project Brief.
- Glosario SDD.

Notas relevantes sobre el contexto utilizado:

Se ha generado un brief fundacional, no un brief de cliente ni de implementacion. Donde faltan decisiones o referencias formales externas se ha marcado `PENDING`. Se ha evitado fijar tecnologia concreta para mantener la independencia declarada por la Foundation.


## 12. Success Criteria

- la Foundation define una metodologia comun reutilizable en distintos dominios analiticos;
- nuevas Skills pueden incorporarse sin modificar los principios nucleares ni el proceso comun;
- la separacion entre adquisicion, analisis, razonamiento y presentacion queda explicitamente definida;
- las recomendaciones futuras de proyectos derivados pueden trazarse hasta evidencia estructurada;
- el repositorio mantiene coherencia con SDD sin introducir implementacion prematura.

---

## 13. Open Questions

- que artefactos fundacionales adicionales deben priorizarse tras este brief para acelerar la adopcion en proyectos derivados;
- que criterio formal se utilizara para validar la primera Skill piloto de la metodologia.

---

## 14. Next Recommended Step

```text
Create additional specialized documentary evaluations when the scope requires it.
```

---

## Definition of Done

El Project Brief esta completo cuando:

- el problema esta definido;
- el objetivo esta definido;
- el alcance esta definido;
- los limites estan definidos;
- los riesgos principales son conocidos;
- existe contexto suficiente para iniciar Specification.