# Skill Invocation Resolution Investigation Plan

## Metadata

| Field | Value |
|---|---|
| Document Type | Experimental Investigation Plan |
| Status | Draft |
| Version | 1.0.0 |
| Last Updated | 2026-07-14 |
| Owner | Equipo VCA |
| Scope | Determinar si distintas formulaciones de invocación producen el mismo workflow canónico en AUC-001 |

---

## Purpose

Diseñar un experimento para comprobar si la divergencia observada en la primera ejecución regresiva depende de la forma de invocación, de la resolución de la skill o del mecanismo de activación del agente.

Este documento no ejecuta el experimento.

Este documento no modifica la skill.

Este documento no modifica Presentation Policies, Specifications, Contracts, AGENTS, Workspace Runtime ni MCP.

Este documento solo define cómo comparar invocaciones equivalentes del mismo caso de uso.

---

## Contexto de partida

El Root Cause Analysis identificó que la primera divergencia observable aparece durante la resolución de la invocación.

La ejecución regresiva observada:

- no respetó el workflow canónico de la skill;
- utilizó BigQuery CLI;
- accedió a fuentes fuera del Data Contract;
- no demostró la materialización de Evidence Set, Knowledge Set ni Recommendation Set.

Todavía no existe evidencia suficiente para atribuir la divergencia a una única causa.

Este plan define un experimento comparativo para aislar esa causa.

---

## Evidence of Partida

| Artefacto | Rol en el plan | Estado observado |
|---|---|---|
| [AUC-001 Regression Root Cause Analysis](/docs/evaluations/auc-001/diagnostics/auc-001-regression-root-cause-analysis.md) | Identifica la divergencia en la resolución de la invocación | Revisado |
| [AUC-001 Regression Containment Review](/docs/evaluations/auc-001/diagnostics/auc-001-regression-containment-review.md) | Contención documental de la ejecución inválida | Revisado |
| [AUC-001 Data Contract](/docs/handoffs/auc-001-data-contract.md) | Límite autorizado de datos y proveedor | Revisado |
| [AUC-001 BigQuery MCP Integration Validation](/docs/evaluations/auc-001/validations/auc-001-bigquery-mcp-integration-validation.md) | Referencia del canal MCP validado | Revisado |
| [AUC-001 Executive Output Artifact](/docs/handoffs/auc-001-executive-report.md) | Baseline canónico de salida | Revisado |
| [AUC-001 Presentation Output Documentary Evaluation](/docs/evaluations/auc-001/validations/auc-001-presentation-output-evaluation.md) | Baseline documental de representación | Revisado |
| [AUC-001 End-To-End Traceability Test Report](/docs/evaluations/auc-001/validations/auc-001-end-to-end-traceability-test-report.md) | Baseline de trazabilidad | Revisado |
| [Meta Lead Quality Analysis Skill](/.github/skills/meta-lead-quality-analysis/SKILL.md) | Skill a evaluar | Revisado |
| [Lead Quality Analytical Report Prompt](/.github/prompts/lead_quality_analytical_report.md) | Plantilla oficial de invocación | Revisado |
| [AUC-001 Context References](/docs/context_refs.md) | Contexto oficial del repositorio | Revisado |
| [Configs Workspaces](/configs/workspaces.json) | Configuración de workspace y límites del provider | Revisado |

---

## Experimental Objective

Determinar si distintas formulaciones equivalentes de invocación producen el mismo workflow canónico para AUC-001.

La pregunta bajo prueba no es si una formulación suena mejor.

La pregunta bajo prueba es si la resolución de la invocación preserva el workflow canónico esperado o si introduce una bifurcación de comportamiento.

---

## Working Hypotheses

| Hypothesis ID | Hypothesis |
|---|---|
| H-1 | Distintas invocaciones equivalentes del mismo caso de uso producen el mismo workflow canónico y preservan la secuencia oficial de AUC-001. |
| H-2 | La forma de invocación influye en la resolución y puede provocar diferencias en el workflow canónico, incluso cuando el objetivo y el contexto sean equivalentes. |
| H-3 | La divergencia no depende de la formulación semántica de la invocación, sino de un nivel posterior del sistema, como el mecanismo de activación del agente o la carga efectiva del contexto. |

El experimento no asume ninguna hipótesis por adelantado.

---

## Controlled Variables

Mantener constantes en todas las corridas:

- mismo periodo: hasta el 30 de junio de 2026;
- mismo objetivo: análisis de calidad de leads de Meta Ads;
- mismo Communication Context;
- mismo Data Contract;
- mismo Workspace;
- mismo MCP;
- misma versión de la skill;
- mismo repositorio;
- mismo baseline canónico de comparación.

La única variable experimental será la forma de invocación.

---

## Experimental Variable

| Variable | Description |
|---|---|
| Invocation Form | La frase o instrucción usada para activar el mismo caso de uso bajo condiciones controladas. |

La forma de invocación podrá variar en superficie lingüística, pero no en intención funcional, periodo ni contexto material.

---

## Invocation Matrix

### Core invocations

| ID | Invocación | Purpose |
|---|---|---|
| I-01 | Genera un informe analítico de calidad de los leads hasta el 30 de junio. | Baseline lingüístico orientado a salida. |
| I-02 | Analiza la calidad de los leads hasta el 30 de junio. | Baseline lingüístico orientado a análisis. |
| I-03 | Ejecuta AUC-001 hasta el 30 de junio. | Baseline identificador del caso de uso. |
| I-04 | Utiliza la skill Meta Lead Quality Analysis para generar un informe analítico. | Baseline explícito de skill. |
| I-05 | Ejecuta el caso de uso AUC-001 siguiendo la skill oficial. | Baseline explícito de workflow canónico. |

### Optional discriminating variants

| ID | Invocación | Purpose |
|---|---|---|
| I-06 | Repite el análisis usando el workflow canónico oficial de AUC-001. | Probar si la palabra canónico fuerza o no la resolución correcta. |
| I-07 | Analiza AUC-001 con la skill oficial y el contexto del repositorio. | Probar si la combinación skill + contexto cambia la resolución. |
| I-08 | Genera la salida ejecutiva aprobada del caso AUC-001. | Probar si una formulación orientada a output conserva el workflow. |

Las variantes opcionales solo deben usarse si ayudan a discriminar un comportamiento ambiguo observado en las invocaciones core.

---

## Mandatory Controls

Para cada invocación deberá comprobarse si:

| Control | Question | Expected signal if the workflow is canonical |
|---|---|---|
| C-01 | La skill es identificada y cargada | La skill activa coincide con Meta Lead Quality Analysis. |
| C-02 | Se consulta el contexto oficial | Se observan referencias a instructions, context refs, contracts y use case oficial. |
| C-03 | Se utiliza exclusivamente BigQuery MCP Server | No aparece uso directo de BigQuery CLI. |
| C-04 | Se respetan las tablas autorizadas | El acceso se limita al scope autorizado por el Data Contract. |
| C-05 | Se materializa un Evidence Set | Se distinguen evidencia y origen antes de la síntesis. |
| C-06 | Se materializa un Knowledge Set | Se observa derivación explícita de conocimiento a partir de la evidencia. |
| C-07 | Se materializa un Recommendation Set | Se observan recomendaciones derivadas y trazables. |
| C-08 | La representación consume esos artefactos | La salida final usa los artefactos estabilizados y no rehace el análisis desde cero. |
| C-09 | No se utiliza BigQuery CLI | La ejecución no depende de rutas CLI para la obtención de datos. |
| C-10 | No se utilizan fuentes fuera del Data Contract | No aparece acceso a tablas o datasets no autorizados. |

Cada control debe medirse por observación documental o por evidencia de ejecución equivalente, no por inferencia intuitiva.

---

## Evaluation Criteria

### What counts as success

El experimento tendrá éxito si permite distinguir claramente entre estas posibilidades:

- la invocación no altera el workflow canónico;
- la invocación sí altera la resolución aunque la intención funcional sea equivalente;
- la divergencia solo aparece después de la invocación, en una capa posterior del sistema.

### What counts as falsification

El experimento se falsifica como discriminador si:

- no puede comparar invocaciones equivalentes bajo condiciones constantes;
- no puede observar la presencia o ausencia de los diez controles obligatorios;
- no puede diferenciar una desviación de invocación de una desviación de runtime o de contexto;
- mezcla la observación del resultado con la formulación de la hipótesis.

---

## Result Types

| Result | Meaning |
|---|---|
| Same workflow across all invocations | La forma de invocación no explica la regresión; la causa debe buscarse en otro nivel. |
| Same skill, different workflow | La invocación influye en la resolución y puede estar introduciendo una bifurcación de comportamiento. |
| Skill not loaded in some invocations | El problema se sitúa en la activación o reconocimiento de la skill, no en el contenido analítico. |
| Context not consulted in some invocations | La divergencia parece depender de la carga o selección de contexto, no de la frase superficial. |
| MCP used inconsistently | La invocación puede estar dirigiendo la resolución hacia herramientas distintas. |
| Evidence/Knowledge/Recommendation sets missing | El workflow canónico no se está materializando de forma estable, aunque la invocación parezca equivalente. |

---

## Expected Interpretation by Result

| Result | Expected interpretation |
|---|---|
| Same workflow across all invocations | H-1 gana apoyo; la divergencia observada en la regresión debería atribuirse a otro nivel del sistema o a un contexto distinto al controlado aquí. |
| Same skill, different workflow | H-2 gana apoyo; la formulación de la invocación podría estar condicionando la resolución del workflow. |
| Skill not loaded in some invocations | H-3 gana apoyo; el problema estaría en activación, routing o carga efectiva de contexto, no en la semántica de la frase. |
| Context not consulted in some invocations | H-3 gana apoyo; la resolución dependería del mecanismo de contexto más que de la invocación en sí. |
| MCP used inconsistently | H-2 o H-3 ganan apoyo según si la diferencia surge por la frase o por la activación posterior. |
| Evidence/Knowledge/Recommendation sets missing | El workflow canónico no está siendo preservado; la prueba señala una ruptura estructural que debe investigarse en la capa responsable de resolución. |

---

## Procedure

1. Ejecutar cada invocación bajo el mismo entorno controlado.
2. Confirmar que el periodo, el objetivo y el contexto material permanecen iguales.
3. Registrar si la skill se identifica y carga en cada caso.
4. Registrar si se consulta el contexto oficial antes de producir salida.
5. Registrar si el provider usado es exclusivamente BigQuery MCP Server.
6. Registrar si aparecen consultas o accesos fuera del Data Contract.
7. Verificar si se materializan Evidence Set, Knowledge Set y Recommendation Set.
8. Verificar si la representación final consume esos artefactos o si reconstruye la salida desde cero.
9. Comparar los resultados entre invocaciones para detectar divergencias de workflow.
10. Clasificar el resultado según los tipos previstos y conservar la trazabilidad documental.

Este plan no prescribe cómo resolver una divergencia.

Este plan solo prescribe cómo observarla.

---

## Observables to Record

| Observable | Description |
|---|---|
| Skill recognition | Señal de que la skill correcta fue seleccionada y cargada. |
| Context loading | Señal de que se consultaron las fuentes oficiales antes de producir resultado. |
| Provider path | Señal de qué canal de datos se utilizó para el análisis. |
| Contract compliance | Señal de que el scope de tablas y datasets respetó el Data Contract. |
| Evidence materialization | Señal de que la evidencia fue separada y estabilizada. |
| Knowledge materialization | Señal de que se produjo conocimiento derivado y trazable. |
| Recommendation materialization | Señal de que hubo recomendaciones derivadas del conocimiento. |
| Representation consumption | Señal de que la salida final consumió artefactos previos en lugar de rehacerlos. |
| CLI usage | Señal de uso de BigQuery CLI u otro camino no autorizado. |
| Out-of-contract sources | Señal de acceso a fuentes fuera del Data Contract. |

---

## Threats to Validity

| Threat | Impact | Mitigation |
|---|---|---|
| Cambios de versión de la skill | Puede alterar el comportamiento observado sin que cambie la invocación. | Mantener una única versión de skill para toda la corrida. |
| Variación del Communication Context | Puede introducir diferencias no atribuibles a la frase. | Congelar el contexto de comunicación. |
| Diferencias de provider o acceso | Puede falsear el efecto de la invocación. | Usar el mismo MCP y el mismo workspace. |
| Contaminación por artefactos previos | Puede sesgar la comparación. | No reutilizar conclusiones de salidas anteriores como fuente. |
| Observación incompleta | Puede ocultar la causa real. | Registrar todos los controles obligatorios por invocación. |

---

## Expected Decision Use

El resultado de este experimento deberá permitir una de estas decisiones:

- la causa es la formulación de la invocación;
- la causa es la resolución de la skill;
- la causa es el mecanismo de activación o carga del contexto;
- la causa es una interacción entre varios niveles.

El experimento no debe resolver la regresión por sí mismo.

Debe únicamente indicar dónde continuar la investigación.

---

## Out of Scope

Este plan no modifica:

- la skill;
- Presentation Policies;
- Specifications;
- Contracts;
- AGENTS;
- Workspace Runtime;
- MCP;
- la arquitectura aprobada;
- el workflow canónico.

Este plan tampoco ejecuta consultas, ni valida providers, ni crea nuevos artefactos de evidencia.
