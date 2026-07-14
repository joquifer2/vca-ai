# AUC-001 Regression Containment Review

## Metadata

| Campo | Valor |
|---|---|
| Review ID | VCA-AUC-001-RCR-001 |
| Review Name | AUC-001 Regression Containment Review |
| Review Type | Regression Containment / Documentary Validation |
| Analytical Use Case | AUC-001 - Meta Lead Quality Analysis |
| Status | Documented |
| Version | 1.0.0 |
| Last Updated | 2026-07-14 |
| Owner | Equipo VCA |
| Scope | Contener la regresion observada en el ultimo informe de AUC-001 y determinar su impacto sobre la validez documental del caso |

---

## Objetivo declarado

Determinar si el ultimo informe de AUC-001 debe invalidarse, qué invariantes metodologicas fueron violadas, cuál es el ultimo baseline conocido y qué diferencias separan ese baseline del estado actual.

Esta revisión no corrige la implementación.

Esta revisión no modifica ningún artefacto existente.

Esta revisión no redefine la arquitectura.

Esta revisión no genera un nuevo informe analítico.

---

## Evidencia consolidada revisada

| Artefacto | Rol en la contención | Estado observado |
|---|---|---|
| [AUC-001 Data Contract](../handoffs/auc-001-data-contract.md) | Delimita el proveedor, el alcance y las limitaciones documentadas | Documentado; MCP pendiente en el contrato |
| [AUC-001 BigQuery MCP Integration Validation](auc-001-bigquery-mcp-integration-validation.md) | Valida acceso directo MCP para un scope técnico concreto | PASS WITH OBSERVATIONS |
| [AUC-001 Presentation Output Documentary Evaluation](auc-001-presentation-output-evaluation.md) | Valida la salida ejecutiva aprobada | Pass |
| [AUC-001 End-To-End Traceability Test Report](auc-001-end-to-end-traceability-test-report.md) | Verifica trazabilidad end-to-end | PASS |
| [AUC-001 Development Entry Readiness Evidence](auc-001-development-entry-readiness-evidence.md) | Consolida el cierre documental de AUC-001 | PASS WITH OBSERVATIONS |
| [AUC-001 Executive Output Artifact](../handoffs/auc-001-executive-report.md) | Baseline ejecutivo aprobado | Documented |
| [Current report under regression](../../outputs/evaluations/meta-ads-lead-quality-report-to-2026-06-30-from-zero.md) | Última ejecución observada | Revisado |

---

## 1. ¿Debe invalidarse el último informe como evidencia oficial?

Sí.

El informe [meta-ads-lead-quality-report-to-2026-06-30-from-zero.md](../../outputs/evaluations/meta-ads-lead-quality-report-to-2026-06-30-from-zero.md) debe considerarse inválido como evidencia oficial de AUC-001.

### Causa observable

- utilizó BigQuery CLI directo en lugar del proveedor autorizado como canal principal de evidencia;
- consultó `datamart-vca-494114.raw_meta.facebook_ad_insights`, tabla que no forma parte de las fuentes autorizadas por el Data Contract aprobado para AUC-001;
- declaró que no consultó documentación del repositorio, por lo que no materializó el loading contextual esperado;
- no deja evidencia observable de materialización previa de Evidence Set, Knowledge Set y Recommendation Set;
- cambió métricas, cobertura, conclusiones y recomendaciones respecto del modelo aprobado.

El informe no es una variante válida del baseline aprobado; es una ejecución regresiva con cambio de proveedor y cambio de marco de evidencia.

---

## 2. Invariantes metodológicas y operativas violadas

| Invariante | Resultado | Nota |
|---|---|---|
| Data Provider compliance | Fail | Se usó CLI directo y se leyó `raw_meta.facebook_ad_insights`, fuera del proveedor autorizado para el flujo aprobado |
| Data Contract compliance | Fail | La fuente `raw_meta.facebook_ad_insights` no está autorizada por el Data Contract de AUC-001 y altera el alcance documentado |
| Context loading | Fail | El informe declara que no consultó documentación del repositorio |
| Evidence Set materialization | Not demonstrated | No hay evidencia observable de materialización previa del Evidence Set aprobado |
| Knowledge Set materialization | Not demonstrated | No hay evidencia observable de materialización previa del Knowledge Set aprobado |
| Recommendation Set materialization | Not demonstrated | No hay evidencia observable de materialización previa del Recommendation Set aprobado |
| Presentation compliance | Fail | La salida se apoya en un modelo distinto y no preserva el encadenamiento presentation-layer aprobado |
| Validez del informe final | Fail | El resultado modifica métricas, cobertura, conclusiones y recomendaciones fuera del baseline aprobado |

---

## 3. Último baseline conocido compatible con el flujo aprobado

No se observa en el repositorio una única ejecución end-to-end que demuestre simultáneamente todas estas condiciones para el informe final:

- uso exclusivo de BigQuery MCP Server;
- respeto estricto del Data Contract de AUC-001;
- ausencia de CLI;
- coherencia con los artefactos canónicos aprobados.

La evidencia sí permite reconstruir dos baselines conocidos y separados:

### 3.1 Baseline de acceso de datos validado

La última validación documental y técnica explícita de acceso directo MCP es [AUC-001 BigQuery MCP Integration Validation](auc-001-bigquery-mcp-integration-validation.md), con alcance técnico validado sobre `datamart-vca-494114.intermediate.int_faro_lead_scoring`.

Este baseline demuestra:

- acceso MCP alcanzable;
- autenticación VCA válida;
- metadata descubierta correctamente;
- consulta read-only exitosa;
- separación explícita frente a la adquisición CLI histórica.

### 3.2 Baseline de salida canónica aprobada

La última versión conocida coherente con los artefactos canónicos aprobados es el [AUC-001 Executive Output Artifact](../handoffs/auc-001-executive-report.md), validado documentalmente por T-036, T-037 y T-038.

Este baseline demuestra:

- preservación de Evidence, Knowledge y Recommendation Sets;
- trazabilidad end-to-end;
- separación de capas;
- recomendaciones documentales no operativas;
- coherencia con la cadena de contratos y evaluaciones aprobadas.

### 3.3 Conclusión sobre el último baseline exacto pedido

La evidencia disponible no demuestra una única ejecución que una simultáneamente ambos planos en el sentido estricto solicitado por la regresión:

- la validación MCP existe, pero para un scope técnico concreto;
- la salida canónica aprobada existe, pero su coherencia documental está separada de la validación MCP total del informe regresivo.

Por tanto, el último baseline conocido debe interpretarse como una combinación de:

- T-039 para la validación MCP del proveedor;
- T-031 / T-036 / T-037 / T-038 para la coherencia de la salida canónica aprobada.

---

## 4. Diferencias entre baseline y estado actual

| Área | Baseline conocido | Estado actual regresivo |
|---|---|---|
| Fuente de datos | MCP validado para el scope técnico de T-039 y contrato AUC-001 con exposición documentada | BigQuery CLI directo sobre `raw_meta.facebook_ad_insights` y otras tablas |
| Documento consultado | Contexto, contratos y artefactos aprobados del flujo AUC-001 | Declara que no consultó documentación del repositorio |
| Materialización de capas | Evidence, Knowledge, Recommendation y Presentation Sets trazables | No demostrada |
| Cobertura y resultados | `matched`, `lead_only`, `spend_only` preservados en el modelo aprobado | Cambia totales, cobertura y lectura de eficiencia |
| Conclusiones | Coherentes con el modelo aprobado | Modificadas por la nueva fuente y el nuevo modelo |
| Recomendaciones | Trazables y contractualmente delimitadas | Reescritas a partir de un marco distinto |

---

## 5. Recomendación de contención

La contención metodológica recomendada es la siguiente:

1. Invalidar el informe [meta-ads-lead-quality-report-to-2026-06-30-from-zero.md](../../outputs/evaluations/meta-ads-lead-quality-report-to-2026-06-30-from-zero.md) como evidencia oficial de AUC-001.
2. Tratar toda nueva validación de AUC-001 como no válida hasta restaurar el acceso exclusivo mediante el Data Provider autorizado.
3. No aceptar como válida ninguna salida que no declare explícitamente su dependencia del Data Contract y de los artefactos canónicos aprobados.
4. Mantener separada la validación MCP de T-039 respecto de cualquier adquisición histórica por CLI.

La contención debe dejar explícito que ninguna nueva validación de AUC-001 puede considerarse válida hasta restaurar el acceso exclusivo mediante el Data Provider autorizado.
