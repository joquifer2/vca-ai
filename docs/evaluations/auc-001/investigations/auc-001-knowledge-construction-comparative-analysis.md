# AUC-001 Knowledge Construction Comparative Analysis

## Metadata

| Field | Value |
|---|---|
| Evaluation ID | VCA-AUC-001-EVAL-KCA-001 |
| Evaluation Name | AUC-001 Knowledge Construction Comparative Analysis |
| Evaluation Type | Methodological Investigation; Comparative Analysis |
| Analytical Use Case | AUC-001 - Meta Lead Quality Analysis |
| Status | Documented |
| Version | 1.0.0 |
| Last Updated | 2026-07-16 |
| Owner | Equipo VCA |
| Scope | Comparative reconstruction of Evidence Set to Knowledge Set transformation in AUC-001 |

## 1. Propósito

Investigar comparativamente cómo se construye actualmente el Knowledge Set de AUC-001 a partir de un Evidence Set y qué operaciones analíticas estaban presentes en el proceso histórico de mayor calidad.

El objetivo no es proponer una nueva Specification, ni redefinir la arquitectura, ni corregir el workflow operativo. El objetivo es identificar qué se ganó, qué se perdió y qué permanece ambiguo cuando el proceso pasó de un prompt monolítico a un lifecycle separado por capas.

## 2. Alcance

Esta investigación cubre el caso de uso AUC-001 - Meta Lead Quality Analysis y compara dos momentos:

- el proceso histórico de alta calidad representado por el informe experimental clasificado en `docs/corpus/auc-001/informe_calidad_leads_scoring_20260701.md`;
- el workflow actual descrito por la skill, el runbook, el checklist, las referencias oficiales y las evaluaciones documentales recientes de razonamiento, recomendación, presentación y regresión.

No se ejecutaron consultas nuevas sobre BigQuery. No se modificó ningún artefacto operativo ni arquitectónico. La investigación es documental y comparativa.

## 3. Corpus analizado

### Corpus histórico principal

- `docs/corpus/auc-001/informe_calidad_leads_scoring_20260701.md`

  Artefacto histórico experimental incorporado al workspace para reconstruir el informe monolítico de mayor calidad. Se incluye porque concentra el programa analítico antiguo, la lectura de variables, las comparaciones por creatividad y campaña, y las implicaciones de negocio que luego se diluyeron.

### Corpus histórico complementario

- `docs/corpus/auc-001/informe_calidad_leads_20260510.md`

  Precursor temprano del patrón de análisis de calidad y scoring. Se usa como apoyo para identificar la evolución del lenguaje analítico y del foco en señales de intención.

### Prompt histórico monolítico

- `.github/prompts/lead_quality_analytical_report.md`

  Archivo versionado en el repositorio. El historial actual del repo muestra como primer commit conocido `59441c9bea876471bf4630a3115b225d1bcd3f8e` (`2026-07-13T16:50:52+02:00`), por lo que esta copia sirve como referencia archivada del prompt histórico monolítico.

  La contradicción se resuelve así: la ejecución histórica original pudo usar un prompt adjunto a la tarea y no versionado en ese momento; la copia que hoy vive en el repositorio sí está versionada y permite reproducibilidad documental, pero no prueba por sí sola la versión exacta usada en aquella ejecución original.

  Esta copia actual permite ver qué instrucciones activaban la profundidad analítica: variables, campañas, creatividades, señales combinadas, riesgos y recomendación ejecutiva.

  El texto completo del prompt histórico se conserva también como anexo de este documento para facilitar la comparación metodológica.

### Skill, runbook y checklist actuales

- `.github/skills/meta-lead-quality-analysis/SKILL.md`
- `.github/skills/meta-lead-quality-analysis/RUNBOOK.md`
- `.github/skills/meta-lead-quality-analysis/CHECKLIST.md`
- `.github/skills/meta-lead-quality-analysis/references.md`

  Representan el workflow actual separado por capas. Se incluyen porque son el control principal del lifecycle vigente y porque permiten detectar qué parte del programa analítico fue explicitada y qué parte quedó implícita.

### Presentation Policies

- `.github/presentation_policies/analytical-review.md`
- `.github/presentation_policies/executive-decision-support.md`

  Se incluyen para verificar si la reducción de profundidad pudo venir de la capa de presentación o si el problema está antes, en Knowledge Set.

### Artefactos de evaluación y regresión

- `docs/evaluations/auc-001/validations/auc-001-reasoning-recommendations-evaluation.md`
- `docs/evaluations/auc-001/validations/auc-001-presentation-output-evaluation.md`
- `docs/evaluations/auc-001/validations/auc-001-end-to-end-traceability-test-report.md`
- `docs/evaluations/auc-001/diagnostics/auc-001-regression-root-cause-analysis.md`
- `docs/evaluations/auc-001/diagnostics/auc-001-regression-containment-review.md`

  Se usan como evidencia documental del estado actual: separación correcta de capas, trazabilidad preservada y regresión explicada como pérdida de scaffolding analítico, no como fallo de presentación.

### Knowledge Set actual

- `docs/handoffs/auc-001-knowledge-set.md`

  Se leyó de forma directa y se comparó contra el informe histórico y contra el corpus documental del workflow actual. La comparación no depende solo de evaluaciones previas; parte de la evidencia base es la lectura del artefacto actual.

  Lo que no se reconstruyó fue el origen fuente línea por línea del Knowledge Set en su ejecución productiva, porque ese proceso no está disponible como traza completa dentro del repositorio.

### Caso de uso vigente

- `analytical_use_cases/meta_lead_quality_analysis.md`

  Se usa para comprobar cuánto del programa analítico quedó realmente definido a nivel de caso de uso y cuánto dependía del prompt histórico.

## 4. Método de comparación

La comparación se realizó en cuatro pasos:

1. Reconstruir el proceso histórico de calidad alta como cadena de preguntas, evidencias, operaciones, findings, knowledge e implicaciones.
2. Identificar en el workflow actual qué partes están explícitas, cuáles están implícitas y cuáles dependen de iniciativa del modelo.
3. Clasificar las operaciones analíticas observadas y separarlas entre generales, específicas de marketing, específicas de AUC-001 y dependientes del dataset.
4. Evaluar hipótesis alternativas sobre la regresión de profundidad analítica.

La taxonomía operativa usada inicialmente fue la solicitada por el encargo: exploración, análisis descriptivo, comparativo, relacional, robustez, interpretación y síntesis. Se ajustó solo donde la evidencia lo exigió.

## 5. Estado real del workflow actual

El workflow actual está correctamente separado en capas:

Execution Context -> Evidence -> Knowledge -> Recommendations -> Presentation

Eso es una mejora metodológica real. La evidencia, el conocimiento y las recomendaciones quedan estabilizados antes de la presentación, y la presentación no debe reconstruirlos.

Sin embargo, el workflow actual describe bien la secuencia, pero describe poco el contenido analítico interno de la transformación de Evidence Set a Knowledge Set. El runbook pide que Knowledge responda preguntas como:

- qué patrones aparecen;
- qué está cambiando;
- qué explica mejor el rendimiento;
- qué anomalías existen;
- qué riesgos aparecen;
- qué incertidumbres permanecen.

Eso es correcto, pero todavía es demasiado abstracto para reproducir la densidad analítica del informe histórico. Faltan instrucciones explícitas sobre:

- concentración de señales;
- benchmarking interno;
- relaciones entre variables;
- combinaciones de señales;
- ranking multicriterio;
- trade-offs entre volumen y calidad;
- robustez por cobertura y tamaño muestral;
- implicaciones de negocio a partir de patrones observados.

Conclusión provisional: el lifecycle está bien, pero el programa de preguntas analíticas está demasiado desprescrito.

## 6. Preguntas analíticas identificadas

Las preguntas que guiaban el proceso histórico de mayor calidad pueden reconstruirse así:

| ID | Pregunta analítica | Tipo |
|---|---|---|
| Q-01 | ¿Cuánto volumen total y cuánta calidad comercial genera el canal? | Volumen / calidad |
| Q-02 | ¿Qué parte del tráfico aporta leads cualificados y high quality? | Calidad / concentración |
| Q-03 | ¿Qué variables explican mejor la calidad? | Variables explicativas |
| Q-04 | ¿Qué señales combinadas elevan la probabilidad de calidad? | Relaciones / combinaciones |
| Q-05 | ¿Qué campañas, conjuntos y creatividades son más eficientes? | Comparación / eficiencia |
| Q-06 | ¿Dónde se concentra el valor? | Concentración |
| Q-07 | ¿Cómo evoluciona la calidad en el tiempo? | Evolución temporal |
| Q-08 | ¿Qué patrones son robustos y cuáles son exploratorios? | Robustez |
| Q-09 | ¿Qué limitaciones impiden sobreinterpretar el análisis? | Riesgo / incertidumbre |
| Q-10 | ¿Qué implicaciones tiene esto para negocio y optimización de Meta? | Síntesis / negocio |

La diferencia clave con el workflow actual es que hoy esas preguntas no están enumeradas como programa analítico; quedan absorbidas dentro de una formulación genérica de Knowledge.

## 7. Operaciones analíticas identificadas

### Exploración

- inspección de cobertura de datos y fuentes;
- validación de volumen disponible;
- identificación de variables presentes y ausentes;
- detección de limitaciones de medición.

### Análisis descriptivo

- totales de leads, inversión y costes medios;
- distribución por tiers de calidad;
- distribución por origen, campaña, creativo y periodo;
- evolución temporal por semana o mes.

### Análisis comparativo

- comparación de CPL, CPQL y CPHQL;
- comparación entre campañas;
- comparación entre creatividades;
- ranking de piezas por eficiencia;
- comparación entre grupos de señal.

### Análisis relacional

- relación entre billetes, fecha prevista y calidad;
- relación entre tipo de experiencia y calidad;
- relación entre número de personas y calidad;
- acumulación de señales de intención;
- lectura conjunta de volumen y calidad.

### Evaluación de robustez

- lectura de tamaño muestral;
- prudencia ante señales de bajo volumen;
- control de sesgo por cobertura;
- limitaciones por falta de ventas, llamadas o ingresos;
- distinción entre señal prometedora y eficacia demostrada.

### Interpretación

- explicación de por qué una variable parece más explicativa que otra;
- lectura de proximidad a la decisión comercial;
- distinción entre volumen barato y valor comercial;
- inferencia de implicaciones operativas.

### Síntesis

- consolidación de hallazgos en una lectura global;
- priorización de aprendizajes;
- construcción de implicaciones de negocio;
- derivación de recomendaciones.

## 8. Reconstrucción Evidence -> Finding -> Knowledge

| ID | Pregunta | Evidencia | Operación | Finding intermedio | Knowledge generado | Confianza | Implicación |
|---|---|---|---|---|---|---|---|
| R-01 | ¿Cuánto volumen y calidad genera el canal? | 1.339 leads, 396 qualified, 65 high quality, 29,6% y 4,9% | Descriptivo + síntesis | Hay volumen suficiente, pero la calidad es minoritaria | El canal compra volumen barato, no calidad homogénea | Alta | No optimizar solo por CPL |
| R-02 | ¿Dónde se concentra el valor? | [Informe histórico](/docs/corpus/auc-001/informe_calidad_leads_scoring_20260701.md) y EVD-003 | Concentración + comparativo | Las piezas ViajeSinEstres_AlivioEmocional y ViajaComoInvitado_Identidad concentran la mayor parte del volumen y de los cualificados observados | El valor aparece concentrado en pocas piezas de mayor volumen | Alta | Proteger activos de aprendizaje |
| R-03 | ¿Qué variable se asocia con mayor diferencia de calidad? | [Informe histórico](/docs/corpus/auc-001/informe_calidad_leads_scoring_20260701.md) y tabla de billetes de avión | Relacional + comparativo | Tener billetes o estar en proceso de compra se asocia con una diferencia marcada de calidad frente a estar solo mirando | La disponibilidad de billetes es la señal observada con mayor diferencia de calidad entre categorías | Alta | Priorizar esta señal como referencia para CAPI y scoring |
| R-04 | ¿Qué papel juega la fecha? | Tabla de fecha prevista de viaje | Relacional + comparativo | Cuanto más cercana la fecha, más calidad | La proximidad temporal es una señal fuerte de decisión | Alta | Priorizar leads con horizonte cercano |
| R-05 | ¿Qué experiencia genera más valor? | Tabla por tipo de experiencia | Comparativo + descriptivo | La experiencia personalizada destaca | La personalización aumenta la probabilidad de calidad | Media-alta | Reforzar mensajes de valor añadido |
| R-06 | ¿Influye el tamaño del grupo? | Tabla por número de personas | Descriptivo + comparativo | Los grupos más grandes tienen algo más de calidad, pero poco volumen | El tamaño del grupo es una señal secundaria | Media | Usarla como segmentación auxiliar |
| R-07 | ¿Cómo se combinan las señales? | Cruce de billetes, fecha y experiencia | Relacional + síntesis | Las señales se acumulan y refuerzan mutuamente | La combinación de señales presenta una asociación más fuerte con la calidad que las variables aisladas | Alta | Las decisiones basadas en una sola variable podrían perder información relevante |
| R-08 | ¿Qué campaña funciona mejor? | Comparación CAPTACIÓN vs RTG | Comparativo + trade-off | Una campaña es mejor para volumen eficiente y otra para calidad relativa | Las campañas tienen roles distintos en la cartera | Alta | Separar lógica de presupuesto y objetivo |
| R-09 | ¿Qué creatividades rinden mejor? | Ranking por creatividades y costes | Comparativo + ranking | Algunas piezas son mejores en volumen, otras en calidad | La creatividad debe evaluarse por eficiencia de calidad, no solo por CPL | Media-alta | Hacer lectura por CPQL y CPHQL |
| R-10 | ¿Qué tan robustas son las conclusiones? | Limitaciones y ausencia de ventas/ingresos | Robustez + interpretación | Hay señales útiles, pero no prueba de rentabilidad final | El análisis es direccional, no definitivo | Alta | No sobreinterpretar correlación como causalidad |

## 9. Comparación entre proceso histórico y actual

### Lo que el proceso histórico hacía mejor

- convertía el análisis en un programa de preguntas explícitas;
- obligaba a cruzar variables y no solo a leer métricas;
- promovía lectura de concentración, comparativa y relaciones;
- elevaba implicaciones de negocio a partir de patrones concretos;
- distinguía con claridad volumen, calidad, eficiencia y robustez;
- hacía visible el trade-off entre CPL bajo y valor comercial real.

### Lo que el workflow actual hace mejor

- separa correctamente context, evidence, knowledge, recommendations y presentation;
- preserva trazabilidad y limita reconstrucción en Presentation Layer;
- evita mezclar evidencia y recomendación;
- protege las coverage states y las limitaciones;
- reduce el riesgo de que la presentación vuelva a razonar desde los datos.

### Lo que el workflow actual hace peor

- no define una batería de preguntas analíticas equivalentes a la del proceso histórico;
- no enumera operaciones mínimas para construir conocimiento profundo;
- deja demasiado espacio a la iniciativa del modelo para descubrir relaciones y combinaciones;
- favorece una Knowledge Set más correcto metodológicamente, pero menos rico analíticamente.

## 10. Knowledge generado y perdido

### Knowledge preservado o mejor protegido hoy

- la separación de estados lógicos;
- la trazabilidad end-to-end;
- la visibilidad de coverage states;
- la preservación de limitaciones y UNKNOWNs;
- la no reconstrucción del conocimiento en Presentation.

### Knowledge que se generaba mejor antes

- jerarquía de señales de intención;
- papel diferencial de campañas y creatividades;
- lectura de trade-offs entre volumen, calidad y eficiencia;
- concentración del valor en pocos activos;
- análisis explícito de relaciones entre variables;
- síntesis de implicaciones de negocio.

### Knowledge que hoy aparece debilitado

- qué variable explica mejor el rendimiento;
- qué combinaciones de señales son más útiles;
- qué patrones son más robustos y cuáles exploratorios;
- qué segmentos o creatividades concentran el valor;
- qué conclusiones son sólidas frente a cuáles dependen de cobertura parcial.

### Frontera entre Knowledge e implicación

- Knowledge debe formular asociaciones, diferencias observadas y patrones descriptivos.
- La implicación debe traducir esos hallazgos en consecuencias de negocio, todavía sin prescribir una acción concreta.
- Recommendation debe convertir la implicación en una decisión o línea de acción explícita.

## 11. Operaciones genéricas y específicas

| Operación | Clasificación | Motivo |
|---|---|---|
| Comparar tasas, costes y eficiencia | Potencialmente genérica | Aplica a muchos casos analíticos |
| Evaluar robustez por tamaño muestral | Potencialmente genérica | Es una operación metodológica transversal |
| Analizar concentración del valor | Potencialmente genérica | Útil en varios dominios de performance |
| Identificar relaciones entre señales | Potencialmente genérica | Es una operación analítica reusable |
| Ranking multicriterio | Potencialmente genérica | Es una operación reusable de ordenación y priorización |
| Ranking de campañas y creatividades por CPL, CPQL y CPHQL | Específica de AUC-001 / marketing | Las entidades y métricas pertenecen al caso de paid media |
| Lectura CPL, CPQL y CPHQL | Específica de marketing | Métricas propias de adquisición/performance |
| Uso de billetes, fecha prevista y tipo de experiencia | Dependiente del dataset | Son variables concretas del caso de viaje |
| Lectura de Meta Lead Ads, Tier A/B/C/D y QualifiedLead | Específica de AUC-001 | Depende del vocabulario y del scoring del caso |
| Separar lead_only, matched y spend_only | Específica de AUC-001 | Es una convención de cobertura del modelo del caso |
| Evaluar implicaciones de negocio | Potencialmente genérica | Es una operación reusable de síntesis; la especialización comercial depende del dominio |

Conclusión: existe un núcleo reusable de operaciones analíticas, pero su selección y parametrización deben seguir siendo específicas del caso de uso.

## 12. Fortalezas y defectos del prompt anterior

### Fortalezas

- explicitaba las preguntas que había que responder;
- obligaba a pensar en variables explicativas, no solo en métricas;
- empujaba a comparar campañas, creatividades y señales;
- favorecía la lectura de combinaciones y de acumulación de intención;
- conectaba hallazgos con implicaciones de negocio;
- producía una narrativa analítica más profunda.

### Defectos

- era redundante y muy prescriptivo;
- mezclaba análisis con decisiones de activación y estrategia de optimización;
- inducía inferencias de scoring y recomendaciones de alto nivel antes de estabilizar evidencia suficiente;
- podía empujar a sobreinterpretar correlaciones como señales operativas;
- estaba muy anclado a la semántica concreta de Meta Ads y del caso de viaje;
- difícilmente generalizable sin pérdida de intención analítica.

En particular, el prompt antiguo era potente, pero no necesariamente reusable sin adaptación.

## 13. Evaluación de hipótesis alternativas

### H1. Nueva capacidad metodológica

Hipótesis: existe una transformación reusable entre Evidence Set y Knowledge Set que todavía no está formalizada.

Evidencia a favor:

- el informe histórico muestra operaciones que no aparecen explícitamente en el workflow actual;
- varias de esas operaciones son metodológicamente generales;
- el salto de Evidence a Knowledge no debería depender solo de intuición del modelo.

Evidencia en contra:

- gran parte de la riqueza histórica viene del prompt monolítico y del caso concreto;
- no se observa todavía un patrón reusable suficientemente estabilizado para convertirlo en capacidad de Foundation.

Evaluación: plausible, pero no probada como nueva capacidad de Foundation.

### H2. Especialización insuficiente del Analytical Use Case

Hipótesis: el lifecycle general es suficiente, pero AUC-001 no define bien sus preguntas y operaciones analíticas.

Evidencia a favor:

- el caso de uso describe alcance y objetivos, pero no un programa de preguntas equivalente al del informe histórico;
- la skill actual pide respuestas abstractas y no una batería de operaciones;
- la pérdida de profundidad coincide con la pérdida de especificidad analítica.

Evidencia en contra:

- parte de esa especificidad podría vivir en la skill o en el prompt de invocación, no necesariamente en el AUC;
- el caso de uso sí establece evidencias mínimas y flujo general.

Evaluación: muy bien soportada.

### H3. Regresión producida por el refactor de la Skill

Hipótesis: la skill anterior contenía scaffolding analítico útil que se eliminó accidentalmente.

Evidencia a favor:

- la skill histórica sí contenía más instrucciones de contenido analítico;
- el workflow actual es más limpio pero menos prescriptivo;
- las evaluaciones recientes describen la pérdida de profundidad como una regresión de scaffolding.

Evidencia en contra:

- la skill actual mantiene mejor separación metodológica;
- no hay evidencia de que el refactor rompiera el lifecycle; lo que cambió fue el soporte analítico interno.

Evaluación: fuertemente plausible como factor contribuyente.

### H4. Efecto del prompt monolítico

Hipótesis: la calidad anterior era consecuencia de una prescripción exhaustiva difícil de generalizar.

Evidencia a favor:

- el prompt monolítico contenía un programa analítico muy detallado;
- guiaba explícitamente variables, comparaciones y recomendaciones;
- la riqueza del informe histórico parece depender en parte de esa exhaustividad.

Evidencia en contra:

- no toda esa riqueza es ruido; parte es un núcleo metodológico reusable;
- el hecho de que fuera exhaustivo no invalida su valor operativo.

Evaluación: también plausible; explica la diferencia de calidad, pero no basta por sí sola.

### H5. Problema combinado

Hipótesis: existe un núcleo reusable de operaciones analíticas, pero cada Analytical Use Case debe seleccionar y especializar cuáles ejecutar.

Evidencia a favor:

- algunas operaciones son genéricas y otras dependen del dataset;
- el histórico muestra el valor de especializar preguntas por caso;
- el workflow actual preserva lifecycle, pero no la selección operativa de preguntas.

Evidencia en contra:

- requiere separar con precisión qué parte pertenece a Foundation y cuál a AUC; eso todavía no está completamente demostrado.

Evaluación: la hipótesis mejor soportada.

## 14. Hallazgos metodológicos

1. El lifecycle correcto no garantiza profundidad analítica.
2. Knowledge Set necesita un programa de preguntas, no solo una definición de estado.
3. Las operaciones de comparación, relación, concentración y robustez son el motor de la calidad analítica.
4. Parte del valor histórico era reusable; parte era específico del caso y del prompt monolítico.
5. Presentation Policies mejoran la representación, pero no sustituyen el scaffolding de Knowledge.
6. El prompt histórico mezclaba contenido útil y sobreprescripción; no debe copiarse sin análisis.
7. La frontera entre Knowledge, implicación y Recommendation debe quedar explícita para evitar que el razonamiento se convierta prematuramente en acción.

## 15. Incertidumbres y evidencia pendiente

- No se revisaron logs exactos de invocación del workflow que produjo los outputs más recientes.
- No se reconstruyó aquí el Knowledge Set actual a nivel de artefacto fuente línea por línea; sí se leyó directamente el artefacto vigente y se comparó documentalmente, pero no existe una traza completa del proceso fuente que lo generó.
- No se ejecutó BigQuery de nuevo; eso es intencional y consistente con el encargo.
- No se aisló experimentalmente cuánto de la riqueza histórica dependía del prompt y cuánto de la skill previa.
- No se validó todavía un scaffold alternativo con el mismo Evidence Set para medir recuperación de profundidad.
- El prompt histórico sí está versionado hoy en `.github/prompts/lead_quality_analytical_report.md`, pero la ejecución histórica original no puede atribuirse de forma exacta a esa copia sin una evidencia temporal adicional.

## 16. Conclusión experimental

El refactor conservó el lifecycle y mejoró la disciplina metodológica, pero redujo la profundidad analítica porque desprescribió el programa de preguntas y operaciones que convertía Evidence en Knowledge.

La evidencia no apunta a una nueva capacidad de Foundation ya descubierta. Apunta más bien a un problema combinado:

- AUC-001 no especializa lo suficiente sus preguntas y operaciones;
- la skill actual ya no transporta el scaffolding analítico detallado que sí estaba presente en el entorno histórico;
- el prompt monolítico aportaba profundidad, pero también exceso de prescripción.

Por tanto, la hipótesis mejor soportada es H5, con H2 y H3 como causas más próximas y H4 como explicación parcial del comportamiento histórico.

## 17. Siguiente experimento recomendado

Ejecutar un experimento controlado de comparación sobre el mismo Evidence Set de AUC-001 usando dos variantes documentales:

1. workflow actual sin scaffolding adicional;
2. workflow actual con un programa explícito de preguntas y operaciones analíticas derivado del patrón histórico, sin introducir nuevas fuentes ni cambiar el lifecycle.

El experimento debería medir únicamente:

- profundidad y diversidad de operaciones analíticas;
- trazabilidad entre evidencia y conocimiento;
- separación formal entre Knowledge, implicación y Recommendation;
- capacidad de distinguir findings, knowledge y recomendaciones;
- cobertura de riesgos, robustez e implicaciones de negocio;
- presencia de sobreinterpretación o de ruido prescriptivo.

No debería usarse todavía para proponer una nueva Specification ni para elevar una nueva capacidad a Foundation.

## Anexo A. Prompt histórico monolítico

Fuente de referencia: [prompt_historico_monolitico.md](/docs/corpus/auc-001/prompt_historico_monolitico.md)

Este anexo conserva el prompt histórico completo que se utilizó como evidencia comparativa en la investigación.

Se incluye como material de trazabilidad metodológica, no como plantilla normativa del workflow actual.