# AUC-001 Regression Root Cause Analysis

## Metadata

| Campo | Valor |
|---|---|
| Analysis ID | VCA-AUC-001-RCA-001 |
| Analysis Name | AUC-001 Regression Root Cause Analysis |
| Analysis Type | Root Cause Analysis / Regression Investigation |
| Analytical Use Case | AUC-001 - Meta Lead Quality Analysis |
| Status | Documented |
| Version | 1.0.0 |
| Last Updated | 2026-07-14 |
| Owner | Equipo VCA |
| Scope | Identificar la causa mínima que explica la regresion observada entre el ultimo comportamiento válido y la primera ejecución regresiva |

---

## Propósito

Reconstruir cronológicamente qué cambió entre el último comportamiento válido y la primera ejecución regresiva, y evaluar qué hipótesis explican la regresión con mayor probabilidad.

Este análisis no corrige la regresión.

Este análisis no modifica Specifications, Decisions, Presentation Policies, Skills, Contracts ni AIF Foundation.

Este análisis no propone implementación.

---

## Evidencia revisada

| Artefacto | Rol en el análisis | Estado observado |
|---|---|---|
| [AUC-001 Regression Containment Review](/docs/evaluations/auc-001/diagnostics/auc-001-regression-containment-review.md) | Contención documental de la regresión | Revisado |
| [AUC-001 Data Contract](/docs/handoffs/auc-001-data-contract.md) | Límite autorizado de datos y proveedor | Revisado |
| [AUC-001 BigQuery MCP Integration Validation](/docs/evaluations/auc-001/validations/auc-001-bigquery-mcp-integration-validation.md) | Validación MCP directa disponible | Revisado |
| [AUC-001 Presentation Output Documentary Evaluation](/docs/evaluations/auc-001/validations/auc-001-presentation-output-evaluation.md) | Baseline de presentación aprobado | Revisado |
| [AUC-001 End-To-End Traceability Test Report](/docs/evaluations/auc-001/validations/auc-001-end-to-end-traceability-test-report.md) | Baseline de trazabilidad end-to-end | Revisado |
| [AUC-001 Development Entry Readiness Evidence](/docs/evaluations/auc-001/validations/auc-001-development-entry-readiness-evidence.md) | Cierre documental consolidado | Revisado |
| [AUC-001 Executive Output Artifact](/docs/handoffs/auc-001-executive-report.md) | Último baseline ejecutivo canónico | Revisado |
| [meta-ads-lead-quality-report-to-2026-06-30-from-zero.md](/outputs/auc-001/2026-06-30/analytical-report.md) | Primera ejecución regresiva identificada | Revisado |
| [AUC-001 Evidence Acquisition](/docs/handoffs/auc-001-evidence-acquisition.md) | Baseline de adquisición histórico CLI | Revisado |
| [AUC-001 Context References](/docs/context_refs.md) | Estado del proveedor y runtime oficial | Revisado |
| `.github/skills/meta-lead-quality-analysis/SKILL.md` | Skill operativa del caso | Revisado |
| `AGENTS.md` | Gobernanza metodológica del repositorio | Revisado |
| `configs/workspaces.json` | Configuración del workspace BigQuery | Revisado |
| `.github/prompts/lead_quality_analytical_report.md` | Plantilla de ejecución del informe | Revisado |
| `.github/presentation_policies/analytical-review.md` | Presentation Policy analítica reciente | Revisado |
| `.github/presentation_policies/executive-decision-support.md` | Presentation Policy ejecutiva reciente | Revisado |

---

## 1. Cronología de cambios relevantes

### 1.1 Baseline canónico previo a la regresión

El baseline operativo más sólido antes de la regresión se apoya en la cadena documental aprobada de AUC-001:

- T-036 valida el Presentation Contract y el Executive Output Artifact.
- T-037 consolida la evidencia de readiness.
- T-038 valida la trazabilidad end-to-end.
- T-039 valida la integración directa del BigQuery MCP Server para `datamart-vca-494114.intermediate.int_faro_lead_scoring`.

El artefacto ejecutivo canónico vigente es [AUC-001 Executive Output Artifact](/docs/handoffs/auc-001-executive-report.md).

### 1.2 Cambios recientes en el entorno metodológico

En el estado actual del workspace se observan cambios recientes en:

- `.github/skills/meta-lead-quality-analysis/SKILL.md`;
- `.github/presentation_policies/analytical-review.md`;
- `.github/presentation_policies/executive-decision-support.md`.

La skill fue reforzada para exigir separación explícita entre Context Definition, Evidence Set, Knowledge Set, Recommendation Set y Presentation Layer, y para permitir el uso de Presentation Policies compatibles con el Communication Context.

Las Presentation Policies nuevas especializan la representación del contenido canónico para dos modos distintos:

- revisión analítica detallada;
- soporte ejecutivo a la decisión.

### 1.3 Primera ejecución regresiva identificada

La primera ejecución regresiva observada es [meta-ads-lead-quality-report-to-2026-06-30-from-zero.md](/outputs/auc-001/2026-06-30/analytical-report.md).

Esa ejecución declara:

- fuente usada: BigQuery directo;
- documentos consultados: ninguno;
- criterio de calidad inferido desde `lead_tier`;
- uso de `raw_meta.facebook_ad_insights`;
- ausencia observable de materialización previa de Evidence Set, Knowledge Set y Recommendation Set.

---

## 2. Último baseline conocido

No existe en la evidencia un único artefacto que demuestre simultáneamente las cuatro condiciones pedidas para la regresión:

- uso exclusivo de BigQuery MCP Server;
- respeto estricto del Data Contract;
- ausencia de CLI;
- coherencia con los artefactos canónicos aprobados.

La mejor reconstrucción del último baseline conocido es la combinación de:

- [AUC-001 BigQuery MCP Integration Validation](/docs/evaluations/auc-001/validations/auc-001-bigquery-mcp-integration-validation.md) para el acceso MCP validado;
- [AUC-001 Executive Output Artifact](/docs/handoffs/auc-001-executive-report.md) para la salida canónica aprobada;
- [AUC-001 End-To-End Traceability Test Report](/docs/evaluations/auc-001/validations/auc-001-end-to-end-traceability-test-report.md) para la continuidad documental;
- [AUC-001 Development Entry Readiness Evidence](/docs/evaluations/auc-001/validations/auc-001-development-entry-readiness-evidence.md) para el estado consolidado de cierre.

### Baseline operativo más cercano al comportamiento válido

El baseline válido más cercano al workflow aprobado es el Executive Output Artifact de AUC-001, respaldado por T-036/T-037/T-038.

Sus rasgos relevantes son:

- consume Evidence, Knowledge y Recommendation Sets ya estabilizados;
- preserva `matched`, `lead_only` y `spend_only`;
- no genera evidencia nueva;
- no introduce nuevas recomendaciones;
- no altera prioridades;
- mantiene la trazabilidad hacia los artefactos fuente.

---

## 3. Primera ejecución regresiva identificada

La primera ejecución regresiva identificada es el informe [meta-ads-lead-quality-report-to-2026-06-30-from-zero.md](/outputs/auc-001/2026-06-30/analytical-report.md).

### Señales observables de regresión

- utiliza BigQuery CLI directamente;
- consulta `datamart-vca-494114.raw_meta.facebook_ad_insights`;
- no declara consulta de documentos del repositorio;
- reconfigura las métricas respecto del baseline aprobado;
- cambia cobertura, conclusiones y recomendaciones;
- no demuestra la materialización previa de Evidence, Knowledge o Recommendation Sets;
- presenta una estructura de informe independiente del workflow aprobado.

### Comparación mínima con el baseline

| Área | Baseline válido | Primera ejecución regresiva |
|---|---|---|
| Fuente de datos | MCP validado para el scope técnico de T-039 y artefactos canónicos aprobados | BigQuery CLI directo |
| Lectura documental | Cargada desde contexto, contracts y evaluaciones | Declara no haber consultado documentos del repositorio |
| Capas estabilizadas | Evidence, Knowledge, Recommendation y Presentation Sets visibles | No demostradas |
| Cobertura | `matched`, `lead_only`, `spend_only` preservados | Cambia totales, cobertura y lectura de eficiencia |
| Validez del informe | Documentalmente coherente | Inválido como evidencia oficial |

---

## 4. Hipótesis evaluadas

### H1. La regresión fue causada por cambios en la Skill

| Elemento | Evaluación |
|---|---|
| Evidencia a favor | La skill fue modificada y ahora explicita la separación entre capas, la estabilización previa de Evidence/Knowledge/Recommendation y el posible uso de Presentation Policies. |
| Evidencia en contra | La skill modificada sigue exigiendo consultar CCD, FARO, CLARO, `docs/context_refs.md` y utilizar BigQuery MCP Server cuando esté disponible. No hay nada en la skill que justifique usar CLI directo ni omitir el contexto oficial. |
| Confianza | Baja |
| Cobertura de la regresión | Parcial como máximo |

Conclusión: los cambios de la skill no explican por sí solos la regresión observada.

### H2. La regresión fue causada por cambios en la forma de invocar la Skill

| Elemento | Evaluación |
|---|---|
| Evidencia a favor | La plantilla oficial de ejecución [lead_quality_analytical_report.md](/.github/prompts/lead_quality_analytical_report.md) exige revisar instrucciones, specifications, contracts, AUC-001, skill y fuentes de contexto antes de comenzar; también exige usar BigQuery MCP Server cuando el scope lo permita y distinguir evidencia MCP de evidencia CLI. La ejecución regresiva declara exactamente lo contrario: no consultó documentos y usó BigQuery directo. |
| Evidencia en contra | No existe prueba directa de la llamada exacta usada para generar el informe regresivo; la inferencia se basa en el artefacto resultante y en la plantilla oficial disponible. |
| Confianza | Alta |
| Cobertura de la regresión | Alta; explica directamente la omisión de contexto y el salto a CLI |

Conclusión: es la hipótesis más fuerte. El cambio mínimo necesario para explicar la regresión es una invocación que bypassó o no cargó el workflow canónico de la skill y de su prompt oficial.

### H3. La regresión fue causada por cambios en AGENTS.md

| Elemento | Evaluación |
|---|---|
| Evidencia a favor | AGENTS.md define el flujo metodológico general y la separación de roles. |
| Evidencia en contra | AGENTS.md no muestra cambios recientes relevantes en el workspace, y su contenido actual no justifica usar CLI directo ni omitir context loading. |
| Confianza | Muy baja |
| Cobertura de la regresión | No explica la causa observable |

Conclusión: no hay evidencia de que AGENTS.md sea la causa mínima de la regresión.

### H4. La regresión fue causada por Workspace Runtime o Tool Resolution

| Elemento | Evaluación |
|---|---|---|
| Evidencia a favor | `configs/workspaces.json` restringe el workspace BigQuery con deny-by-default y tablas permitidas; el runtime formal existe y es estricto. |
| Evidencia en contra | La configuración disponible no cambió para explicar el uso de CLI directo ni el acceso a `raw_meta.facebook_ad_insights`; además, T-039 demuestra que el MCP sí estaba operativo para el scope validado. |
| Confianza | Baja |
| Cobertura de la regresión | Parcial como máximo |

Conclusión: el runtime no parece ser la causa mínima; más bien muestra que el canal autorizado existía y no fue usado.

### H5. La regresión fue causada por la interacción entre varios cambios recientes

| Elemento | Evaluación |
|---|---|---|
| Evidencia a favor | La skill fue reforzada, se introdujeron Presentation Policies, y el prompt oficial del informe pide reconstruir contexto, usar MCP y separar evidencia MCP/CLI. Un cambio de invocación fuera del flujo canónico podría haber interactuado con esa nueva configuración para producir una salida ad hoc. |
| Evidencia en contra | Los cambios recientes no explican por sí solos la decisión de ignorar contexto y usar CLI directo; el componente decisivo sigue siendo la invocación. |
| Confianza | Media |
| Cobertura de la regresión | Parcial; no es necesario para explicar el fallo mínimo |

Conclusión: la interacción entre varios cambios recientes es compatible con el escenario, pero no es la explicación mínima.

---

## 5. Causa mínima más probable

La causa mínima más probable es H2: una invocación que no cargó o no respetó el workflow canónico de la skill y del prompt oficial de AUC-001.

### Por qué esta causa es mínima

Porque explica directamente los síntomas observables:

- se omitió la consulta de documentos del repositorio;
- se usó BigQuery CLI en lugar del MCP autorizado;
- se accedió a una tabla fuera del Data Contract aprobado;
- no se demostraron las capas estabilizadas previas;
- se produjo una representación distinta del workflow aprobado.

### Por qué las otras hipótesis no son suficientes por sí solas

- H1 no explica el salto a CLI ni la omisión de contexto, porque la skill sigue exigiendo lo contrario.
- H3 no está respaldada por cambios observables en AGENTS.md.
- H4 no se sostiene porque el runtime y el MCP validado existen, y la regresión no parece venir de una imposibilidad técnica sino de una ruta no usada.
- H5 es compatible, pero más amplia de lo necesario.

---

## 6. Cuestiones abiertas

| Cuestión | Estado |
|---|---|
| La invocación exacta usada para generar el informe regresivo | No observada directamente |
| Si el prompt oficial fue omitido, mal cargado o ignorado | No demostrado de forma directa |
| Si las Presentation Policies nuevas influyeron en la decisión de empezar desde cero | Compatible, pero no probado como causa principal |
| Si hubo una herramienta o selector que favoreció CLI sobre MCP | No demostrado |
| Si la ejecución regresiva fue manual o mediada por un agente diferente | No demostrado |

---

## 7. Recomendación sobre qué investigar o corregir primero

La primera prioridad debe ser investigar y corregir la forma de invocación del flujo AUC-001.

### Razón

Es el punto con mayor capacidad explicativa y menor número de supuestos:

- el prompt oficial exige contexto, MCP y separación de evidencia;
- la skill exige exactamente esa secuencia;
- el runtime y el MCP estaban disponibles;
- la regresión ocurrió porque esa secuencia no se siguió.

### Implicación práctica

Antes de revisar la skill, AGENTS o el runtime, conviene verificar cómo se está lanzando el caso de uso y qué plantilla, modo o contexto está recibiendo el agente en el momento de generar el informe.
