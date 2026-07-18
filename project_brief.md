# Project Brief

## 1. Project Overview

### Project Name

VCA IA

### Working Title

vca-ia

### Status

Development Authorized

### Owner

Equipo VCA

### Last Updated

2026-07-11

---

## 2. Purpose

VCA IA existe para convertirse en el sistema analítico corporativo de VCA, proporcionando un entorno estructurado para transformar datos, contexto y conocimiento del negocio en decisiones fundamentadas.

El proyecto busca resolver la fragmentación de los procesos analíticos cuando dependen de instrucciones ad hoc, decisiones implícitas y artefactos aislados que no conservan trazabilidad entre contexto, evidencia, razonamiento y resultado.

El proyecto merece ser construido porque proporciona una capacidad analítica consistente para VCA, con límites claros, criterios verificables y una base documental que facilita evolucionar el sistema sin rehacer el proceso cada vez.

VCA IA se concibe como una plataforma para desarrollar y ejecutar múltiples casos de uso analíticos reutilizando un mismo marco metodológico, en lugar de construir soluciones independientes para cada necesidad de análisis.

El primer caso de uso analítico aprobado es AUC-001, Meta Lead Quality Analysis, que valida el enfoque del sistema y actúa como referencia inicial para el resto de capacidades analíticas.

VCA IA no sustituye la plataforma de datos existente de VCA. La consume como fuente de información para ejecutar procesos analíticos asistidos por IA.

---

## 3. Business Context

VCA dispone de un ecosistema analítico consolidado que integra procesos comerciales, marketing, contexto de cliente, modelos de datos y plataformas analíticas sobre los que se apoyará VCA IA.

Entre los principales activos existentes se encuentran la documentación de contexto, la plataforma analítica, los modelos de datos, los procesos comerciales y los sistemas de soporte desarrollados por VCA.

El proyecto debe organizar y aprovechar ese entorno para convertirlo en un sistema analítico corporativo coherente, con trazabilidad entre contexto, evidencia, razonamiento y salida.

AUC-001 y la skill [meta-lead-quality-analysis](/.github/skills/meta-lead-quality-analysis/SKILL.md) ya forman parte del marco metodológico aprobado y sirven como primer ciclo validado del sistema analítico.

AIF Foundation actúa como dependencia metodológica del proyecto, no como objeto del sistema. Su papel es aportar la base SDD, la gobernanza documental y el marco común de análisis que VCA IA reutilizará sin modificar su naturaleza.

---

## 4. Problem Statement

Hoy el trabajo analítico de VCA puede quedar disperso entre fuentes de contexto, criterios de decisión, evidencia y salidas parciales, lo que dificulta mantener consistencia y trazabilidad.

Las limitaciones principales son:

- el contexto relevante puede quedar repartido entre documentos o conversaciones sin un punto de referencia único;
- el razonamiento analítico puede variar entre ejecuciones o responsables;
- la evidencia y la interpretación pueden mezclarse;
- los resultados no siempre quedan ligados de forma verificable a sus fuentes;
- la evolución del proceso puede depender de conocimiento tácito en lugar de artefactos reutilizables.

Las consecuencias son menor auditabilidad, mayor coste de repetición, riesgo de incoherencia entre análisis y recomendaciones, y dificultad para escalar el sistema a nuevos casos de uso sin perder control metodológico.

---

## 5. Desired Outcome

El resultado esperado es un sistema analítico para VCA capaz de sostener un ciclo de trabajo claro desde el contexto inicial hasta las conclusiones y recomendaciones, con trazabilidad documental suficiente para revisar decisiones y reutilizar criterios.

Sabremos que el proyecto ha tenido éxito cuando VCA disponga de un sistema que:

- permita estructurar análisis repetibles con entradas, procesos y salidas definidos;
- conserve la separación entre hechos, evidencia, interpretación y recomendación;
- haga visibles los criterios utilizados en cada análisis;
- pueda evolucionar sin perder coherencia documental;
- reutilice la metodología de AIF Foundation sin depender de ella como resultado funcional.

---

## 6. Scope

### In Scope

- construir el sistema analítico de VCA sobre la infraestructura existente;
- definir el sistema analítico corporativo de VCA y sus límites funcionales;
- definir entradas de contexto, evidencia, conocimiento de negocio y criterios de análisis;
- definir el flujo de trabajo analítico, sus salidas esperadas y su relación con la plataforma de datos existente;
- definir el papel de los Data Providers especializados dentro del sistema;
- definir usuarios, stakeholders y dependencias del sistema;
- incorporar el primer caso de uso analítico aprobado como referencia operacional inicial del sistema;
- reutilizar la primera skill analítica aprobada como capacidad ejecutable de análisis documental;
- usar AIF Foundation como base metodológica reutilizable;
- documentación inicial necesaria para iniciar Development de forma controlada.

### Out of Scope

- implementación productiva o runtime del sistema;
- infraestructura técnica concreta;
- integraciones ejecutables con herramientas o APIs específicas;
- conocimiento de negocio no publicado del entorno VCA;
- automatizaciones operativas que sustituyan la revisión humana;
- redefinir la metodología base heredada de AIF Foundation.

### Analytical Positioning

VCA IA no reemplaza la plataforma de datos existente de VCA. La consume y la organiza para ejecutar procesos analíticos asistidos por IA, integrando Data Providers, evidencia y conocimiento del negocio en un marco común.

---

## 7. Users and Stakeholders

### Primary Users

- analistas de VCA;
- responsables que consumen análisis y recomendaciones;
- personas que preparan contexto, evidencia o insumos para análisis.

### Secondary Users

- revisores documentales;
- responsables metodológicos;
- futuros equipos que mantendrán o extenderán el sistema.

### Stakeholders

- Equipo VCA;
- responsables de gobernanza del proyecto;
- equipos propietarios de Data Providers y fuentes analíticas;
- mantenedores de AIF Foundation como dependencia metodológica;
- QA Gate Agent y Reviewer Agent como consumidores de la evidencia documental de gates, validaciones y revisiones;
- futuros usuarios del sistema analítico.

---

## 8. Assumptions

- VCA necesita un sistema analítico recurrente y no un flujo aislado de informes;
- la trazabilidad entre contexto, evidencia y recomendación es un requisito importante;
- VCA ya cuenta con una plataforma analítica que el proyecto debe aprovechar;
- los Data Providers especializados son una pieza central del sistema;
- la metodología de AIF Foundation es válida como base del proyecto y no debe redefinirse;
- el contexto de negocio relevante ya está suficientemente documentado para el primer caso de uso;
- AUC-001 y su skill asociada representan el primer ciclo analítico validado del proyecto;
- el sistema debe permanecer reutilizable y no depender de un dominio demasiado específico en esta fase.

---

## 9. Constraints

Las restricciones conocidas son:

- el proyecto se encuentra autorizado para Development mediante el Phase Gate de SPEC-008;
- el sistema debe evolucionar de forma controlada, manteniendo trazabilidad documental antes de cualquier runtime productivo;
- no se debe acoplar a un proveedor, runtime o tecnología concreta sin validación posterior;
- no se debe asumir contexto de negocio no publicado;
- el proyecto es greenfield y no requiere reconstrucción As-Is para continuar el desarrollo autorizado;
- AIF Foundation debe tratarse como dependencia metodológica, no como sustituto del proyecto VCA.

---

## 10. Risks

| Risk | Impact | Notes |
| --- | --- | --- |
| Definir el sistema demasiado abstraído | Alto | Puede dificultar su uso real en VCA y frenar la adopción |
| Mezclar metodología de base con necesidades específicas de VCA | Alto | Puede romper la separación entre dependencia metodológica y proyecto |
| Suponer contexto de negocio no validado | Alto | Puede introducir decisiones erróneas o irrelevantes |
| Acoplar el proyecto a tecnología prematura | Medio | Reduce flexibilidad para fases posteriores |
| No mantener trazabilidad entre evidencia y salida | Alto | Debilita la confiabilidad de las recomendaciones |
| Confundir la capa analítica del producto con la plataforma de datos subyacente | Alto | Puede generar decisiones de arquitectura incorrectas |

---

## 11. Source of Truth

Documentos o sistemas que contienen la lógica funcional principal.

| Source | Purpose |
| --- | --- |
| docs/context_refs.md | Índice oficial de contexto del proyecto y trazabilidad documental |
| .github/instructions/sdd.instructions.md | Reglas de fase, alcance y precedencia documental |
| README.md | Resumen del propósito, límites y estructura del proyecto |
| plataforma analítica existente de VCA | Fuente de datos, contexto y servicios analíticos que VCA IA consume |
| AIF Foundation | Dependencia metodológica reutilizable para el sistema analítico de VCA |
| analytical_use_cases/meta_lead_quality_analysis.md | Primer caso de uso analítico aprobado del proyecto |
| .github/skills/meta-lead-quality-analysis/SKILL.md | Primera skill analítica aprobada para ejecutar el caso AUC-001 |
| knowledge/ | Base de conocimiento del proyecto para contexto persistente y reutilizable |
| futuras specifications del proyecto VCA | Definición funcional detallada del sistema analítico |

### Context References

Documento de referencias de contexto utilizado:

docs/context_refs.md

Fuentes principales consultadas:

- README del repositorio.
- Instrucciones SDD del repositorio.
- Template oficial de Project Brief.
- Context References del proyecto.
- AUC-001 como primer caso de uso analítico aprobado.
- Skill meta-lead-quality-analysis como capacidad analítica inicial del sistema.
- conocimiento de contexto proporcionado por VCA sobre CCD, FARO, CLARO, BigQuery, dbt, Marketing, Comercial, SOP, hipótesis e informes.
- AIF Foundation como dependencia metodológica.

Notas relevantes sobre el contexto utilizado:

Este brief describe exclusivamente el sistema analítico que se va a construir para VCA. AIF Foundation se usa solo como base metodológica reutilizable. El contexto de negocio específico de VCA ya existe para el desarrollo autorizado del proyecto y se sigue consolidando en la Base de Conocimiento y en los artefactos de contexto.

## 12. Success Criteria

- VCA dispone de un sistema analítico claramente definido y trazable;
- las entradas, el proceso y las salidas del sistema están acotados;
- la evidencia y la interpretación permanecen separadas;
- el sistema puede evolucionar sin reabrir la definición metodológica base;
- el sistema puede incorporar nuevos análisis sin modificar la arquitectura analítica común;
- el primer caso de uso analítico aprobado y su skill asociada pueden ejecutarse de forma trazable;
- el brief aporta contexto suficiente para sostener Development sin ambigüedades críticas.

---

## 13. Open Questions

- No quedan preguntas abiertas relevantes para el alcance actualmente aprobado de VCA IA.
- Las preguntas que puedan surgir sobre nuevos casos de uso deberán documentarse cuando se abran nuevas specifications.

---

## 14. Next Recommended Step

```text
Continuar Development bajo el Phase Gate de SPEC-008 y mantener el SDD Readiness Assessment como evidencia histórica.
```

---

## Definition of Done

El Project Brief está completo cuando:

- el problema está definido;
- el objetivo está definido;
- el alcance está definido;
- los límites están definidos;
- los riesgos principales son conocidos;
- existe contexto suficiente para sostener Development autorizado.