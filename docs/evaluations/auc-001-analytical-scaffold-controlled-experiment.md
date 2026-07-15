# AUC-001 Analytical Scaffold Controlled Experiment

## 1. Objetivo

Diseñar y verificar la ejecutabilidad de un experimento controlado para comparar tres mecanismos de transformación del mismo Evidence Set en Knowledge, Recommendations y Presentation dentro de AUC-001.

La hipótesis experimental es que la pérdida de profundidad analítica observada tras la evolución del lifecycle podría deberse a la ausencia de un scaffold explícito de operaciones analíticas entre Evidence y Knowledge.

Este documento no ejecuta comparaciones especulativas. Verifica si el experimento puede ejecutarse con el estado actual del repositorio y define el protocolo mínimo necesario para ejecutarlo posteriormente de forma reproducible.

## 2. Estado actual del repositorio respecto al experimento

El repositorio contiene una ejecución canónica completa de AUC-001 para junio de 2026:

| Elemento | Estado observable | Evidencia |
|---|---|---|
| Analytical Use Case | Existe y delimita AUC-001. | `analytical_use_cases/meta_lead_quality_analysis.md` |
| Skill actual | Existe y obliga a usar workflow, runbook, references y checklist. | `.github/skills/meta-lead-quality-analysis/SKILL.md` |
| Runbook | Existe y define Execution Context, Evidence, Knowledge, Recommendations y Presentation. | `.github/skills/meta-lead-quality-analysis/RUNBOOK.md` |
| Checklist | Existe y valida cierre de estados antes de Presentation. | `.github/skills/meta-lead-quality-analysis/CHECKLIST.md` |
| References | Existe y declara artefactos obligatorios. | `.github/skills/meta-lead-quality-analysis/references.md` |
| Execution Context | Existe, validado y congelado para junio de 2026. | `docs/handoffs/auc-001-execution-context.md` |
| Evidence Set | Existe y está documentado como `VCA-AUC-001-EVD-SET-001`. | `docs/handoffs/auc-001-evidence-set.md` |
| Knowledge Set | Existe y está confirmado contra Knowledge Contract. | `docs/handoffs/auc-001-knowledge-set.md` |
| Recommendation Set | Existe y está confirmado contra Recommendation Contract. | `docs/handoffs/auc-001-recommendation-set.md` |
| Presentation | Existe como Executive Output Artifact. | `docs/handoffs/auc-001-executive-report.md` |
| Prompt histórico | Existe como adjunto y está orientado a CSVs/integración automática. | `C:\Users\jordi\.codex\attachments\c136334f-3dbf-4bd7-9dba-ca1c6908506e\pasted-text.txt` |
| Historial Git | Muestra refactors de skill y outputs experimentales previos. | `git log`, `git show 4d6b8e3`, `git show 59441c9`, `git show 8789eed` |

Observación crítica:

El repositorio contiene artefactos suficientes para observar una baseline ya materializada, pero no contiene todavía un harness experimental que ejecute A, B y C con el mismo Evidence Set, registre prompts exactos, congele criterios de evaluación y produzca outputs comparables.

## 3. Diseño experimental

### Condición A — Baseline

Usar exclusivamente el workflow actual:

- AUC actual.
- Skill actual.
- Runbook actual.
- Contracts actuales.
- Evidence Set actual.
- Knowledge Generation sin instrucciones adicionales.
- Recommendation Generation desde Knowledge.
- Presentation desde Recommendation Set y Presentation Contract.

### Condición B — Workflow + Analytical Scaffold

Mantener el mismo workflow y el mismo Evidence Set, pero añadir antes de Knowledge Generation un repertorio explícito de operaciones analíticas generales:

- Comparative Analysis.
- Segmentation.
- Distribution Analysis.
- Trend Analysis.
- Concentration Analysis.
- Ranking.
- Thresholding.
- Coverage Analysis.
- Robustness Evaluation.
- Variable Explanatory Assessment.
- Cost Efficiency Analysis.
- Business Interpretation.

El scaffold no debe introducir:

- evidencia nueva;
- operaciones específicas de marketing;
- recomendaciones anticipadas;
- cambios en lifecycle;
- cambios en Presentation Policy.

### Condición C — Prompt histórico

Usar el prompt histórico monolítico como mecanismo de transformación, con el mismo Evidence Set congelado y sin nuevas consultas.

El uso de esta condición requiere adaptar la entrada del prompt histórico, porque el prompt original espera uno o varios CSVs y contiene instrucciones de inspección, integración automática, scoring y costes que no coinciden directamente con un Evidence Set canónico ya cerrado.

## 4. Variables controladas

Variables que deben permanecer idénticas:

| Variable | Valor congelado |
|---|---|
| Analytical Use Case | AUC-001 — Meta Lead Quality Analysis |
| Execution ID | `VCA-AUC-001-EXEC-2026-06` |
| Periodo | 2026-06-01 to 2026-06-30 |
| Evidence Set | `VCA-AUC-001-EVD-SET-001` |
| Evidence blocks | EVD-001, EVD-002, EVD-003, EVD-004 |
| Source model | `ad_quality_spend_model` |
| Source tables | `marts.fct_lead_enriched`; `intermediate.int_faro_lead_scoring`; `marts.fct_spend` |
| Model grain | normalized `ad_id` (`ad_id_norm`) |
| Lead quality rule | `lead_tier IN ('A', 'B')` |
| Spend filter | `campaign_signal = 'COMMERCIAL'` |
| Coverage states | `matched`; `lead_only`; `spend_only` |
| Presentation Policy | `executive-decision-support`, if executive output is selected |

Variables que no deben cambiar:

- No ejecutar nuevas consultas BigQuery.
- No cambiar datos.
- No cambiar AUC.
- No cambiar skill, runbook, prompts, contracts ni handoffs.
- No cambiar Presentation Policy.
- No añadir evidencia externa.

Variable independiente:

```text
Mecanismo de transformación Evidence → Knowledge.
```

## 5. Verificación de ejecutabilidad

### Criterios de ejecutabilidad

Una condición se considera ejecutable solo si puede producir Knowledge Set, Recommendations y Presentation:

- usando exactamente el Evidence Set congelado;
- sin nuevas consultas;
- con instrucciones completas y reproducibles;
- sin modificar artefactos existentes;
- con un input package idéntico salvo por el mecanismo Evidence → Knowledge;
- con outputs persistibles para evaluación posterior;
- con criterios de comparación definidos antes de generar resultados.

### Resultado de verificación

| Condición | Clasificación | Justificación |
|---|---|---|
| A — Baseline | Ejecutable ya materializada | Existen Knowledge Set, Recommendation Set y Executive Output Artifact actuales derivados del Evidence Set de junio 2026. |
| B — Workflow + Analytical Scaffold | Parcialmente ejecutable | El repo contiene Evidence Set y contracts, pero no contiene un scaffold congelado, un prompt operativo exacto, un harness de ejecución ni una plantilla de output para distinguir findings intermedios de Knowledge. |
| C — Prompt histórico | Parcialmente ejecutable | El prompt histórico existe, pero espera CSVs y tareas de inspección/integración/scoring que violarían el control del Evidence Set si se aplican literalmente. Requiere un protocolo de adaptación de entrada no existente. |

Conclusión de ejecutabilidad:

El experimento completo no es ejecutable todavía de forma objetiva y reproducible. Solo existe una baseline materializada. No hay resultados válidos para comparar A, B y C bajo controles equivalentes.

## 6. Estado de las condiciones A, B y C

### Condición A — Baseline

Estado: Ejecutable ya materializada.

Artefactos disponibles:

- `docs/handoffs/auc-001-knowledge-set.md`
- `docs/handoffs/auc-001-recommendation-set.md`
- `docs/handoffs/auc-001-executive-report.md`

Evidencia de alineación:

- El Knowledge Set consume EVD-001 through EVD-004.
- El Recommendation Set consume el Knowledge Set confirmado.
- El Executive Output consume Evidence, Knowledge y Recommendation Sets ya aprobados.

### Condición B — Workflow + Analytical Scaffold

Estado: Parcialmente ejecutable.

Elementos disponibles:

- Evidence Set congelado.
- Knowledge Contract.
- Recommendation Contract.
- Presentation Contract.
- Lista candidata de operaciones generales en el encargo.

Elementos faltantes:

- Scaffold exacto, congelado y versionado.
- Instrucción reproducible que indique cómo aplicar cada operación sin crear evidencia nueva.
- Formato de finding intermedio.
- Criterios para descartar operaciones no aplicables.
- Criterios para transformar findings en Knowledge sin adelantar Recommendations.
- Output path separado para B.
- Método de evaluación antes de ejecutar.

### Condición C — Prompt histórico

Estado: Parcialmente ejecutable.

Elementos disponibles:

- Prompt histórico adjunto.
- Outputs históricos de referencia en `docs/evaluations/corpus`.
- Evidence Set actual.

Elementos faltantes:

- Adaptación controlada del Evidence Set a la entrada esperada por el prompt histórico.
- Regla explícita para desactivar inspección de CSVs y nuevas integraciones.
- Regla explícita para impedir que el prompt reconstruya scoring, costes o datos fuera de EVD-001..EVD-004.
- Separación posterior entre Knowledge, Recommendations y Presentation, porque el prompt histórico produce un informe monolítico.
- Output path separado para C.

## 7. Resultados

Solo existe resultado válido para la condición A.

### Resultado observable de A

El Knowledge Set actual contiene:

- INS-001: concentración de evidencia matched en una referencia de anuncio.
- INS-002: separación entre CAPTACION/ABO matched y RTG/CBO lead-only.
- INS-003: spend-only pequeño pero estructuralmente importante.
- HYP-001: concentración posible de señal en un subconjunto matched.
- HYP-002: RTG requiere tratamiento separado.
- CON-001: evidencia suficiente para razonar a nivel ad-level dentro del modelo corregido.
- CON-002: razonamiento campaign/adset parcialmente soportado y coverage-qualified.
- PRI-001..PRI-004.
- RSK-001..RSK-005.
- UNC-001..UNC-005.

El Recommendation Set actual contiene seis recomendaciones:

- REC-001: usar matched ad-level como base principal de eficiencia.
- REC-002: tratar RTG lead-only por separado.
- REC-003: validar mapping campaign/adset spend antes de recomendaciones por campaña.
- REC-004: mantener recomendaciones creativas a nivel ad reference.
- REC-005: preservar incertidumbre de duplicados/test.
- REC-006: excluir impressions/clicks/CTR salvo ampliación de scope.

No existen resultados válidos para B ni C bajo el diseño controlado. Por tanto, no se comparan resultados de profundidad, utilidad o calidad metodológica entre condiciones.

## 8. Comparativa

No procede una comparativa experimental completa porque no existen outputs ejecutados para B y C bajo las mismas variables controladas.

Comparativa limitada a ejecutabilidad:

| Dimensión | A | B | C |
|---|---|---|---|
| Knowledge Set disponible | Sí | No | No |
| Recommendations disponibles | Sí | No | No |
| Presentation disponible | Sí | No | No |
| Usa Evidence Set congelado | Sí | Diseñable, no ejecutado | Requiere adaptación |
| Reproducibilidad actual | Alta para A | Insuficiente | Insuficiente |
| Riesgo de contaminar variable independiente | Bajo | Medio | Alto |

No se evalúan:

- número comparado de findings;
- mejora real de profundidad;
- superioridad del prompt histórico;
- aproximación de B a C.

Hacerlo sería especulativo con el estado actual.

## 9. Evaluación de hipótesis

### H1. El workflow actual es suficiente

Evidencia a favor:

- A produjo un Knowledge Set, Recommendation Set y Presentation completos.
- La trazabilidad Evidence → Knowledge → Recommendations está documentada.
- Los coverage states, UNKNOWNs y limitations se preservan.

Evidencia en contra:

- A no prueba por sí sola profundidad analítica suficiente frente a alternativas.
- El Knowledge Set actual contiene pocos insights sustantivos y está muy centrado en límites de cobertura.

Incertidumbres:

- No existe comparación controlada con B y C.

Valoración:

No demostrada. A es ejecutable y metodológicamente trazable, pero no se puede afirmar suficiencia comparativa.

### H2. El scaffold analítico mejora significativamente la profundidad

Evidencia a favor:

- El repositorio y el encargo identifican operaciones generales plausibles.
- Outputs históricos y de Git muestran que operaciones como comparación, concentración, robustez y eficiencia pueden generar más lectura.

Evidencia en contra:

- No existe una ejecución B controlada.
- No existe scaffold congelado ni formato de findings intermedios.

Incertidumbres:

- No se sabe si la mejora vendría de operaciones generales o de conocimiento de dominio implícito al aplicarlas.

Valoración:

No demostrada. Hipótesis plausible, pendiente de ejecución.

### H3. El prompt histórico sigue siendo superior

Evidencia a favor:

- El prompt histórico contiene un repertorio amplio de preguntas, métricas, secciones e interpretación ejecutiva.
- Los informes históricos son más ricos en lectura de variables, relaciones, creatividad y decisiones.

Evidencia en contra:

- El prompt histórico no está diseñado para consumir un Evidence Set canónico cerrado.
- Mezcla Evidence, Knowledge, Recommendations y Presentation.
- Su superioridad no ha sido probada con el mismo Evidence Set de junio 2026.

Incertidumbres:

- Una adaptación controlada podría reducir parte de su ventaja.

Valoración:

No demostrada. Hay evidencia histórica de riqueza, no evidencia experimental controlada.

### H4. El scaffold recupera la mayor parte del valor del prompt histórico

Evidencia a favor:

- Parte del valor histórico parece proceder de operaciones generales, no solo de dominio.

Evidencia en contra:

- No hay output B ni output C comparables.
- No se ha separado valor procedente de operaciones generales, dominio y estructura monolítica.

Incertidumbres:

- La magnitud de recuperación no puede estimarse sin ejecución.

Valoración:

No demostrada.

## 10. Amenazas a la validez

Amenazas principales:

- Condición A ya existe y no fue generada en el mismo run experimental que B y C.
- B requeriría crear un scaffold; diseñarlo ahora podría incorporar sesgos de investigaciones previas.
- C requiere adaptar un prompt histórico orientado a CSVs; la adaptación podría alterar el mecanismo evaluado.
- El Evidence Set actual es más limitado que algunos outputs históricos: no incluye impressions, clicks, CTR ni creative asset metadata.
- La Presentation Policy impide crear nuevo conocimiento en Presentation, mientras que el prompt histórico mezcla conocimiento y presentación.
- La evaluación de “profundidad” requiere rúbrica previa; si se define después de ver outputs, contaminaría el resultado.
- El modelo puede variar entre ejecuciones si no se fija temperatura/modelo/procedimiento.

## 11. Limitaciones del experimento

Limitaciones actuales:

- No se ejecutaron nuevas consultas BigQuery.
- No se modificaron artefactos del repositorio.
- No se generaron outputs B ni C.
- No se simularon resultados.
- No se evaluó cuantitativamente profundidad analítica.
- El prompt histórico solo se verificó como artefacto disponible, no se ejecutó.
- Los outputs de Git `59441c9` se usaron solo como evidencia histórica de disponibilidad, no como resultados del experimento controlado.

## 12. Conclusiones

### 1. ¿La condición B mejora realmente respecto al baseline?

No.

Justificación: B no ha sido ejecutada bajo condiciones controladas. No existe output B válido para comparar.

### 2. ¿La mejora se aproxima al prompt histórico?

No.

Justificación: no existen resultados B ni C comparables.

### 3. ¿Qué parte de la mejora proviene de operaciones generales, dominio o prompt?

No determinable.

Justificación: el experimento necesario para separar esos factores todavía no es ejecutable.

### 4. ¿Existe evidencia suficiente para afirmar que hay un scaffold reutilizable?

Parcialmente.

Justificación: existe evidencia documental de operaciones generales candidatas y de que el baseline actual deja margen para más profundidad, pero no hay evidencia experimental controlada que demuestre reusabilidad ni mejora significativa.

### 5. ¿Cuál debería ser el siguiente paso?

D. Diseñar una capability experimental.

Justificación: no como arquitectura definitiva ni Specification, sino como capability experimental mínima para ejecutar el test. Especializar AUC-001, mejorar la Skill o mejorar el Runbook ahora introduciría cambios en el objeto de estudio antes de aislar la variable. La necesidad inmediata es un mecanismo experimental controlado, no una modificación permanente.

## 13. Protocolo mínimo para ejecutar el experimento en el futuro

### 13.1 Preparar un paquete de entrada congelado

Crear un input package experimental que incluya copias de solo lectura o referencias exactas a:

- Execution Context `VCA-AUC-001-EXEC-2026-06`.
- Evidence Set `VCA-AUC-001-EVD-SET-001`.
- Evidence Contract `VCA-AUC-001-EVD-001`.
- AUC-001.
- Skill actual.
- Runbook actual.
- Knowledge Contract.
- Recommendation Contract.
- Presentation Contract.
- Presentation Policy.

El paquete debe declarar que EVD-001..EVD-004 son la única evidencia permitida.

### 13.2 Definir outputs separados

Usar rutas separadas, por ejemplo:

```text
outputs/evaluations/auc-001-controlled/A-knowledge.md
outputs/evaluations/auc-001-controlled/A-recommendations.md
outputs/evaluations/auc-001-controlled/A-presentation.md
outputs/evaluations/auc-001-controlled/B-knowledge.md
outputs/evaluations/auc-001-controlled/B-recommendations.md
outputs/evaluations/auc-001-controlled/B-presentation.md
outputs/evaluations/auc-001-controlled/C-knowledge.md
outputs/evaluations/auc-001-controlled/C-recommendations.md
outputs/evaluations/auc-001-controlled/C-presentation.md
```

Estas rutas no deben sustituir handoffs canónicos.

### 13.3 Congelar la condición A

Definir si A será:

- reutilización exacta de los handoffs actuales; o
- nueva generación baseline desde el mismo input package.

Para control experimental más fuerte, conviene regenerar A, B y C en el mismo procedimiento, pero sin modificar handoffs oficiales.

### 13.4 Congelar el scaffold de B

Crear un documento experimental no normativo con:

- lista exacta de operaciones;
- definición breve de cada operación;
- input permitido;
- output esperado por operación;
- regla para marcar operación no aplicable;
- regla para convertir findings intermedios en Knowledge;
- prohibición de recomendaciones anticipadas.

Formato mínimo de finding:

| Campo | Descripción |
|---|---|
| Finding ID | Identificador experimental |
| Operation | Operación aplicada |
| Evidence links | EVD IDs utilizados |
| Intermediate result | Patrón observado |
| Knowledge candidate | Interpretación trazable |
| Limitations | UNKNOWNs y boundaries |

### 13.5 Adaptar C sin romper el control

Crear una envoltura experimental del prompt histórico que:

- indique que no hay CSVs;
- entregue EVD-001..EVD-004 como única entrada;
- prohíba inspección de archivos, integración automática o nuevas consultas;
- prohíba inventar variables no presentes;
- exija separar el output monolítico en Knowledge, Recommendations y Presentation para evaluación.

Esta envoltura debe considerarse parte de C y quedar congelada antes de ejecución.

### 13.6 Definir rúbrica antes de ejecutar

Rúbrica mínima:

| Dimensión | Medida |
|---|---|
| Profundidad analítica | Número de findings distintos; diversidad de operaciones; relaciones entre variables; implicaciones de negocio. |
| Trazabilidad | Cada finding enlaza a EVD; ausencia de nuevos datos; saltos justificados. |
| Composición | Operaciones simples vs compuestas; patrones de composición. |
| Calidad metodológica | Incertidumbres, coverage states, separación Evidence/Knowledge/Recommendations, riesgo de sobreinterpretación. |
| Utilidad de negocio | Claridad, accionabilidad, soporte a decisión. |
| Coste metodológico | Complejidad, mantenibilidad, reusabilidad potencial. |

### 13.7 Ejecutar sin nuevas consultas

Regla de ejecución:

- No BigQuery.
- No web.
- No lectura de informes históricos como fuente de contenido.
- No uso de Knowledge/Recommendation de otra condición como input.
- Cada condición debe ejecutarse desde el mismo input package.

### 13.8 Comparar por evaluador separado

La evaluación debería realizarse después de generar outputs, idealmente con nombres de condición ocultos o con una matriz de evaluación prellenada, para reducir sesgo.

## 14. Recomendación para el siguiente experimento

El siguiente experimento debe ser un dry run controlado de B únicamente, antes de ejecutar A/B/C completos.

Objetivo del dry run:

- validar que el scaffold general puede producir findings intermedios desde EVD-001..EVD-004;
- comprobar que no añade evidencia;
- comprobar que no formula recomendaciones anticipadas;
- comprobar que respeta coverage states y UNKNOWNs;
- ajustar la rúbrica antes de comparar contra A y C.

Resultado esperado del dry run:

- un Knowledge Set experimental B;
- un registro de operaciones aplicadas/no aplicables;
- una lista de riesgos metodológicos observados.

Solo si este dry run es limpio debería ejecutarse el experimento completo A/B/C.

