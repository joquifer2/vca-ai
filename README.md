# VCA IA

## Sistema Analítico basado en Inteligencia Artificial

**Versión documental:** v1.0.0
**Estado:** Development Authorized

---

# ¿Qué es VCA IA?

VCA IA es el sistema analítico para VCA.

Su objetivo es ayudar a transformar datos, contexto de negocio y conocimiento experto en análisis trazables, conclusiones fundamentadas y recomendaciones útiles para la toma de decisiones.

No pretende sustituir el criterio humano ni generar informes automáticamente. Su propósito es construir un proceso analítico consistente, repetible y auditable que permita comprender cómo se ha llegado a cada conclusión.

Este repositorio contiene la definición del sistema, sus reglas metodológicas, los casos de uso analíticos, las decisiones adoptadas y la documentación necesaria para hacerlo evolucionar de forma controlada.

---

# ¿Qué problema resuelve?

En cualquier organización, la información necesaria para analizar un problema suele encontrarse repartida entre múltiples fuentes:

* bases de datos;
* documentación interna;
* conocimiento de negocio;
* experiencia de los equipos;
* informes anteriores.

Cuando ese conocimiento no está organizado es frecuente que:

* distintos análisis lleguen a conclusiones diferentes;
* se mezclen hechos con interpretaciones;
* no quede claro por qué se recomienda una determinada acción;
* el contexto se pierda con el tiempo;
* o cada nuevo análisis tenga que comenzar prácticamente desde cero.

VCA IA nace para evitar esa situación mediante un sistema común que conecte contexto, evidencia, conocimiento y recomendaciones dentro de un mismo proceso analítico.

---

# ¿Cómo funciona?

VCA IA organiza el trabajo en cinco capas claramente diferenciadas.

| Capa                | Finalidad                                                                      |
| ------------------- | ------------------------------------------------------------------------------ |
| **Contexto**        | Define qué se quiere analizar, con qué objetivo y bajo qué alcance.            |
| **Evidencia**       | Recoge únicamente los datos y hechos disponibles en las fuentes autorizadas.   |
| **Conocimiento**    | Convierte la evidencia en hallazgos e interpretaciones útiles para el negocio. |
| **Recomendaciones** | Propone acciones justificadas por la evidencia obtenida.                       |
| **Presentación**    | Adapta el resultado al destinatario sin alterar el significado del análisis.   |

Esta separación permite mantener la trazabilidad del razonamiento y facilita revisar cualquier análisis incluso mucho tiempo después de haber sido realizado.

---

# Principios del sistema

Todo análisis realizado mediante VCA IA debe respetar una serie de principios básicos:

* separar siempre hechos e interpretaciones;
* mantener la trazabilidad entre evidencia y conclusiones;
* reconocer explícitamente las incertidumbres y limitaciones;
* justificar las recomendaciones mediante conocimiento construido;
* reutilizar capacidades ya validadas;
* conservar la posibilidad de revisión humana en todo momento.

Estos principios son independientes del dominio de negocio y permiten que el sistema pueda crecer incorporando nuevos casos de uso.

---

# Estado actual

El proyecto ha completado su fase de definición y dispone de autorización para continuar el desarrollo.

Actualmente cuenta con:

* una arquitectura metodológica estable;
* un primer caso de uso analítico completamente operativo;
* capacidades documentadas para construir conocimiento analítico;
* mecanismos formales de validación mediante gates;
* y un primer ciclo experimental finalizado.

## Primer caso de uso

**AUC-001 — Meta Lead Quality Analysis**

Este caso de uso analiza la calidad de los leads captados mediante Meta Ads y ha servido para validar experimentalmente varias capacidades reutilizables del sistema, entre ellas:

* resolución automática del alcance de ejecución;
* separación entre análisis y presentación;
* adaptación del conocimiento al destinatario;
* construcción de narrativas analíticas trazables.

Su cierre experimental ha sido aprobado con decisión:

**READY FOR CLOSURE**

### Evolucion post-cierre de AUC-001

El ciclo experimental original de AUC-001 permanece cerrado y su producto validado no se modifica retrospectivamente.

La mejora definida por `SPEC-012 - AUC-001 Canonical Cost-Quality Model` se clasifica como una evolucion post-cierre. Su validacion se ejecuto como `AUC-001 Post-Closure Iteration 1` (`AUC-001-PCI-001`), con [Entry Gate](/gates/auc-001-pci-001-entry-gate.md), [Exit Gate](/gates/auc-001-pci-001-exit-gate.md) y outputs propios bajo `outputs/auc-001/pci-001/2026-06-30/`, sin sobrescribir `outputs/auc-001/2026-06-30/` ni promover la capacidad a AIF Foundation.

Estado de la evolucion SPEC-012: `AUC-001-PCI-001` ejecutado; Exit Gate `PASS WITH CONDITIONS`; modelo canonico coste-calidad estabilizado dentro de AUC-001.

La mejora definida por `SPEC-013 - AUC-001 Structured Reconciliation Output` endurece la exposicion estructurada del runtime para futuras ejecuciones AUC-001. Su implementacion tecnica, validacion QA y Exit Gate estan completados con decision `PASS WITH CONDITIONS`. No modifica outputs historicos, no regenera informes y no inicia contrato de producto analitico.

El cierre operativo P0 fue reevaluado el 2026-07-19 con evidencia adicional de la ultima ejecucion real AUC-001 hasta 2026-06-30. La decision QA inicial fue `P0 BLOCKED` por falta de persistencia fisica SPEC-013. Tras AUC-001-PCI-002, la decision final es `P0 PASS WITH RESIDUAL OBSERVATIONS - READY FOR P01`. En ese momento, P01 no quedo iniciado por ese cierre.

Specification Agent formalizo la correccion minima como `CORRECTIVE TASKS UNDER SPEC-013`. No se abrio una nueva specification: esa correccion fue planificada y ejecutada como `AUC-001-PCI-002` para persistir un `execution/runtime-output.json` fisico conforme a SPEC-013 en un nuevo namespace autorizado.

QA Gate Agent ha evaluado el Entry Gate de AUC-001-PCI-002 con `PASS WITH CONDITIONS`, ha validado la implementacion local con pruebas 14/14 PASS y ha autorizado la ejecucion real via BigQuery MCP. Implementation Agent ha materializado el paquete real en `outputs/auc-001/pci-002/2026-06-30/`. QA Gate Agent ha validado fisicamente `execution/runtime-output.json` desde disco, ha emitido el Exit Gate de PCI-002 con `PASS` y ha reemitido el P0 Operational Closure Gate como `P0 PASS WITH RESIDUAL OBSERVATIONS - READY FOR P01`.

P01 fue formalizado el 2026-07-21 como `AUC-001-P01 - Analytical Product Contract Definition`. Architect Agent emitio el memo arquitectonico y Specification Agent creo `SPEC-014 - AUC-001 Analytical Product Contract`. Reviewer Agent reviso adversarialmente la Specification, Specification Agent corrigio las condiciones y Reviewer Agent emitio `PASS`. QA Gate Agent emitio el cierre documental de P01 con decision `PASS`.

P02 fue planificado a partir de SPEC-014 y del cierre documental de P01. Tras implementacion local, autorizacion de ejecucion real via BigQuery MCP, materializacion del paquete `outputs/auc-001/p02/2026-07-17/` y revalidacion fisica QA con `PASS WITH DECLARED LIMITATIONS`, QA Gate Agent emitio el Closure Gate de P02. Estado canonico vigente: `AUC-001-P02 CLOSURE PASS WITH DECLARED LIMITATIONS - ANALYTICAL PRODUCT CONTRACT REAL EXECUTION CLOSED`.

### Namespace de outputs post-cierre

El namespace oficial para la primera iteracion post-cierre es `outputs/auc-001/pci-001/2026-06-30/`.

La jerarquia `outputs/auc-001/` conserva la continuidad del caso de uso. `pci-001` identifica la iteracion metodologica y `2026-06-30` identifica la ejecucion. Futuras iteraciones usaran el patron `outputs/auc-001/pci-00N/<execution-date>/`.

Dentro del namespace se documenta esta estructura canonica: `execution/`, `evidence/`, `knowledge/`, `recommendations/`, `presentation/`, `analytical-report/` y `executive-report/`.

Los outputs historicos de `outputs/auc-001/2026-06-30/` son inmutables. No pueden usarse como expected values, ni como fuente de Knowledge o Recommendations, ni mezclarse con nuevas versiones de informes.

---

# Relación con AIF Foundation

VCA IA utiliza **AIF Foundation** como dependencia metodológica.

AIF Foundation proporciona el marco común de trabajo (SDD, gobernanza documental y capacidades analíticas reutilizables).

Sin embargo, el producto desarrollado en este repositorio es **VCA IA**.

La evolución metodológica sigue una regla sencilla:

> Ninguna capacidad pasa directamente a AIF Foundation.
>
> Primero debe descubrirse y validarse experimentalmente dentro de VCA IA.
> Solo después puede proponerse como capacidad reutilizable del framework.

---

# Organización del repositorio

| Área                    | Contenido                                                  |
| ----------------------- | ---------------------------------------------------------- |
| `project_brief.md`      | Propósito, alcance y objetivos del proyecto.               |
| `docs/context_refs.md`  | Índice oficial de contexto y trazabilidad documental.      |
| `specs/`                | Capacidades y reglas metodológicas del sistema.            |
| `analytical_use_cases/` | Casos de uso analíticos y estado de cada uno.              |
| `.github/skills/`       | Skills operativas para ejecutar los casos de uso.          |
| `docs/contracts/`       | Contratos metodológicos y documentales.                    |
| `docs/decisions/`       | Decisiones estabilizadas del proyecto.                     |
| `docs/evaluations/`     | Investigaciones, experimentos y validaciones.              |
| `docs/corpus/`          | Material histórico utilizado como referencia experimental. |
| `outputs/`              | Productos analíticos generados y validados.                |
| `gates/`                | Gates de avance, QA y cierre.                              |
| `docs/tasks.md`         | Backlog documental del proyecto.                           |

---

# ¿Dónde empezar?

## Si quieres comprender el proyecto

1. `project_brief.md`
2. `docs/context_refs.md`

## Si quieres comprender la metodología

1. `specs/`
2. `docs/contracts/`
3. `gates/`

## Si quieres comprender el primer caso de uso

1. `analytical_use_cases/auc-001/README.md`
2. `analytical_use_cases/meta_lead_quality_analysis.md`
3. `.github/skills/meta-lead-quality-analysis/SKILL.md`
4. `gates/auc-001-experimental-closure-gate.md`
5. `gates/auc-001-pci-001-entry-gate.md` y `gates/auc-001-pci-001-exit-gate.md`
6. `outputs/auc-001/2026-06-30/analytical-report.md`
7. `specs/spec-014-auc-001-analytical-product-contract.md`
8. `gates/auc-001-p01-documentary-closure-gate.md`
9. `tasks/auc-001-p02-analytical-product-contract-implementation-task-plan.md`
10. `gates/auc-001-p02-entry-gate.md`
11. `gates/auc-001-p02-closure-gate.md`

---

# Filosofía de evolución

VCA IA se desarrolla mediante **Specification Driven Development (SDD)**.

Las mejoras no se incorporan porque parezcan buenas ideas.

Cada nueva capacidad debe:

1. surgir de una necesidad real;
2. implementarse dentro de un caso de uso;
3. validarse experimentalmente;
4. documentarse;
5. y únicamente entonces proponerse como capacidad reutilizable.

Este enfoque permite que el sistema evolucione de forma controlada, manteniendo la coherencia entre metodología, implementación y conocimiento acumulado.
