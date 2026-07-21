# SPEC-014 - AUC-001 Analytical Product Contract

## Estado

Cerrada - P01 Documentary Closure PASS.

## Fecha

2026-07-21

## Ámbito

AUC-001-P01.

## Título

Contrato de Producto Analítico específico de AUC-001.

## Decisión base

Esta Specification materializa el memo arquitectónico:

`docs/decisions/auc-001/auc-001-p01-analytical-product-contract-architectural-analysis.md`

La Specification no reproduce el prompt histórico, no usa outputs históricos como valores esperados y no incorpora conocimiento analítico nuevo derivado de informes anteriores.

Los artefactos históricos solo pueden usarse como referencia de forma, cobertura funcional o necesidades de producto previamente observadas, nunca como evidencia vigente ni como verdad de negocio.

---

## 1. Propósito

Definir el Contrato de Producto Analítico específico de AUC-001 para determinar qué debe contener, separar y declarar un producto analítico válido sobre calidad de leads de Meta Ads.

El contrato gobierna la suficiencia del producto final:

* qué preguntas debe responder;
* qué preguntas puede declarar como parciales, desconocidas o no aplicables;
* qué vistas analíticas son requeridas;
* qué profundidad mínima debe alcanzar cada pregunta;
* cómo se separan evidencia, conocimiento, recomendaciones y presentación;
* cómo se distingue el núcleo común del producto de sus proyecciones analítica y ejecutiva;
* cómo se evita confundir presencia formal de secciones o tablas con completitud analítica real.

---

## 2. Boundary de AUC-001-P01

AUC-001-P01 corresponde exclusivamente a la definición y aprobación del Contrato de Producto Analítico específico de AUC-001.

Incluye:

* definición normativa del contrato;
* taxonomía de preguntas analíticas;
* matriz de cobertura integrada en el propio contrato;
* criterios de completitud, profundidad y calidad analítica;
* reglas para `UNKNOWN`, evidencia insuficiente, cobertura parcial y `not_available`;
* separación entre requisitos de contenido, criterios de calidad y restricciones interpretativas;
* clasificación definitiva de residuos P0/P01 como requisitos de producto, experimentos medibles, acciones verificables o hipótesis no accionables.

No incluye:

* implementación runtime;
* cambios de código;
* consultas BigQuery;
* generación de nuevos Evidence Sets;
* generación de Knowledge Sets;
* generación de Recommendation Sets;
* generación de reports;
* definición de tareas;
* definición de gates;
* validación experimental del contrato.

La implementación y validación experimental pertenecen a fases posteriores.

---

## 3. Estado canónico reconstruido

El estado documental vigente de AUC-001 es:

* P0 está cerrado con PASS y observaciones residuales.
* PCI-001 cerró el modelo canónico de coste-calidad mediante SPEC-012.
* PCI-002 cerró la salida estructurada de reconciliación mediante SPEC-013.
* La salida runtime actual es consumible para sus objetivos de reconciliación.
* La siguiente necesidad no es una corrección de runtime sino la definición del contrato de producto analítico.
* Los residuos no bloqueantes de P0 se enrutan a P01 o backlog, no invalidan P0.

Los residuos documentales relevantes para P01 son:

* `ad_id_norm` existe como identificador técnico, pero el producto necesita tratar `ad_name` como etiqueta interpretativa cuando esté disponible.
* `ticket_status` no está incorporado como dimensión analítica vigente y requiere clasificación contractual antes de exigirse.
* la evolución semanal existe de forma limitada y debe definirse si es requisito obligatorio, condicional o parcial;
* las recomendaciones deben distinguirse de conclusiones y clasificarse como experimentos medibles, acciones verificables o hipótesis no accionables cuando pretendan orientar acción.

---

## 4. Relación con contratos existentes

El Contrato de Producto Analítico de AUC-001 no sustituye los contratos transversales. Los coordina para este caso de uso.

| Contrato | Rol transversal | Relación con este contrato |
| --- | --- | --- |
| Analytical Contract | Define preguntas, límites, capacidades y métricas analíticas de AUC-001. | Es la fuente primaria de preguntas y restricciones analíticas. Este contrato define la suficiencia del producto construido sobre esas preguntas. |
| Evidence Contract | Regula Evidence Sets observables, trazables y sin interpretación. | Exige que cada respuesta analítica declare evidencia fuente, cobertura, limitaciones y estados `UNKNOWN`. |
| Knowledge Contract | Convierte evidencia en insights, hipótesis, conclusiones, riesgos e incertidumbres. | Exige que la interpretación y la implicación de negocio estén separadas de la evidencia cruda. |
| Recommendation Contract | Regula acciones sugeridas, justificadas, priorizadas y evaluables. | Exige que las recomendaciones accionables de AUC-001 se formulen como experimentos medibles cuando proceda. |
| Presentation Contract | Regula proyecciones de presentación sin crear nuevo conocimiento. | Representa el núcleo común aprobado sin modificar evidencia, interpretación ni recomendaciones. |

El Product Contract no es una fase posterior a Presentation. Es un contrato envolvente de aceptación del producto canónico de AUC-001.

Evalúa la suficiencia del producto después de que existan artefactos canónicos estabilizados y antes de autorizar cualquier representación como producto conforme.

La relación de aceptación es:

1. Evidence Contract para hechos observables.
2. Analytical Contract para preguntas y límites de lectura.
3. Knowledge Contract para interpretación.
4. Recommendation Contract para acción evaluable.
5. Product Contract de AUC-001 para aceptación envolvente de suficiencia, cobertura, profundidad y calidad del producto canónico.
6. Presentation Contract para representación del contenido aprobado sin reconstruirlo.

---

## 5. Definición del contrato

El Contrato de Producto Analítico específico de AUC-001 es un contrato local del caso de uso.

Debe responder a esta pregunta:

> Dado un periodo y una ejecución autorizada de AUC-001, ¿qué condiciones debe cumplir el producto analítico para considerarse suficientemente completo, profundo, útil y honesto sobre la calidad de leads de Meta Ads?

El contrato no define nuevas fuentes, métricas canónicas ni reglas de reconciliación. Esas responsabilidades permanecen en SPEC-012, SPEC-013 y el Analytical Contract vigente.

---

## 6. Principios normativos

### 6.1 Completitud por pregunta y criticidad

La completitud se evalúa por pregunta analítica y por criticidad. No existe un único booleano global de completitud que pueda ocultar carencias importantes.

Un producto puede ser completo para preguntas obligatorias, parcial para preguntas condicionales, conforme con ausencias justificadas o no apto si falla una pregunta obligatoria crítica sin justificación suficiente.

### 6.2 `not_available` no implica incumplimiento automático

El estado `not_available` no implica automáticamente incumplimiento.

Puede ser conforme si:

* la ausencia está explícitamente justificada;
* la fuente, dimensión o métrica no estaba disponible en la ejecución autorizada;
* la ausencia no impide responder una pregunta obligatoria crítica;
* el producto declara el impacto de la ausencia sobre interpretación, recomendación y decisión.

Si `not_available` afecta a una pregunta obligatoria crítica y no existe una vía analítica equivalente autorizada, debe registrarse como brecha contractual.

### 6.3 Separación de capas

El contrato debe mantener separadas tres categorías:

* requisitos de contenido: qué debe aparecer o declararse;
* criterios de calidad: con qué profundidad, trazabilidad, comparabilidad y utilidad debe tratarse;
* restricciones interpretativas: qué inferencias están prohibidas, limitadas o condicionadas.

Una pregunta puede tener requisitos de contenido completos y aun así fallar por baja calidad interpretativa.

### 6.4 Vistas analíticas requeridas, no tablas literales

Las tablas obligatorias deben expresarse como vistas analíticas requeridas.

Se admiten formatos equivalentes si preservan granularidad, métricas canónicas, comparabilidad, finalidad analítica, trazabilidad y visibilidad de cobertura.

Una tabla Markdown, una sección narrativa, una matriz estructurada o una salida JSON pueden ser equivalentes solo si conservan esas propiedades.

### 6.5 Profundidad mínima verificable

Cada pregunta analítica obligatoria debe alcanzar un umbral mínimo verificable de profundidad.

Para considerarse cubierta, debe incluir al menos:

* evidencia observada o derivada autorizada;
* comparación relevante;
* interpretación separada de la evidencia;
* implicación de negocio;
* limitación, incertidumbre o condición de cobertura;
* conclusión, hipótesis o declaración `UNKNOWN` cuando proceda;
* trazabilidad al Evidence Set o salida estructurada aplicable.

### 6.6 Presencia formal no equivale a cobertura

Una fila de la matriz de cobertura no puede considerarse completa solo por la presencia de una tabla, gráfico, sección o párrafo.

La cobertura requiere cumplir simultáneamente contenido, profundidad, calidad y restricciones interpretativas.

---

## 7. Estados de cobertura

Cada pregunta o vista analítica debe declarar un estado de cobertura.

| Estado | Definición | Uso permitido |
| --- | --- | --- |
| `complete` | La pregunta cumple contenido, profundidad, calidad, trazabilidad y límites. | Preguntas obligatorias o condicionales plenamente respondidas. |
| `partial` | Existe evidencia o interpretación útil, pero falta granularidad, comparación, cobertura o profundidad. | Conforme solo si se declara impacto y no se presenta como respuesta total. |
| `not_available` | La fuente, dimensión o métrica no está disponible en la ejecución autorizada. | Conforme si está justificado y no bloquea una pregunta obligatoria crítica. |
| `not_applicable` | La pregunta no corresponde al periodo, fuente, boundary o decisión analítica. | Debe justificarse explícitamente. |
| `UNKNOWN` | La evidencia disponible no permite concluir. | Debe conservarse como resultado analítico válido, no rellenarse por inferencia. |
| `blocked` | No puede evaluarse una pregunta obligatoria crítica por ausencia no justificable o ruptura contractual. | Impide declarar el producto completo para su finalidad principal. |

Los estados de cobertura y los estados de conclusión analítica deben distinguirse.

`not_available` describe ausencia de una fuente, dimensión, métrica o granularidad autorizada. No significa que exista evidencia inconclusa; significa que el dato requerido no está disponible dentro del boundary autorizado.

`UNKNOWN` describe una conclusión no resoluble con la evidencia disponible. Puede existir evidencia suficiente para observar el fenómeno y, aun así, ser insuficiente para concluir una causa, prioridad, ganador, cambio material o recomendación.

Por tanto:

* si falta la dimensión o fuente autorizada, usar `not_available`;
* si la dimensión existe pero no permite concluir, usar `UNKNOWN`;
* si existe una respuesta útil pero incompleta, usar `partial`;
* si una pregunta obligatoria crítica no puede responderse sin inferencia prohibida, usar `blocked`.

---

## 8. Taxonomía de preguntas analíticas

### 8.1 Preguntas obligatorias

| ID | Pregunta obligatoria | Criticidad | Resultado esperado |
| --- | --- | --- | --- |
| AQ-001 | ¿Qué volumen de leads se generó y cómo evolucionó la captación en el periodo? | Alta | Lectura de volumen, ritmo de captación y cobertura temporal básica, sin absorber la evolución de calidad propia de AQ-009. |
| AQ-002 | ¿Cuál fue la distribución de calidad por tiers FARO y qué peso tuvieron Tier A y A/B? | Alta | Distribución de calidad con denominadores explícitos. |
| AQ-003 | ¿Qué eficiencia coste-calidad se observa usando métricas canónicas reconciliadas? | Alta | Lectura económica con cobertura matched, lead-only, spend-only y `UNKNOWN`. |
| AQ-004 | ¿Qué campañas y conjuntos combinan mejor volumen, calidad y coste? | Alta | Ranking o comparación equivalente con límites de cobertura. |
| AQ-005 | ¿Qué anuncios o creatividades concentran valor, desperdicio o dependencia? | Media-alta | Vista por `ad_id_norm` y etiqueta `ad_name` cuando esté disponible. |
| AQ-006 | ¿Qué señales FARO, formulario o cualificación ayudan a explicar la calidad observada? | Alta | Lectura explicativa no causal con evidencia y límites. |
| AQ-007 | ¿Qué trade-offs aparecen entre volumen, calidad y coste? | Alta | Interpretación de tensiones de negocio y no solo métricas aisladas. |
| AQ-008 | ¿Qué concentraciones, dependencias o riesgos estructurales aparecen? | Media-alta | Identificación de dependencia por campaña, conjunto, anuncio, segmento o periodo. |
| AQ-009 | ¿Cómo evolucionan la calidad y, cuando aplique, la eficiencia coste-calidad en el tiempo? | Alta | Vista temporal comparable de calidad y cambios interpretables, mensual como mínimo y semanal cuando sea comparable. |
| AQ-010 | ¿Qué oportunidades de optimización se derivan del conocimiento disponible? | Alta | Recomendaciones o hipótesis clasificadas como experimento medible, acción verificable o hipótesis no accionable cuando propongan acción o preparen una decisión. |
| AQ-011 | ¿Qué límites de evidencia condicionan la lectura del producto? | Alta | Declaración explícita de cobertura parcial, ausencia de datos y `UNKNOWN`. |

### 8.2 Preguntas condicionales

| ID | Pregunta condicional | Condición de aplicabilidad | Resultado esperado si aplica |
| --- | --- | --- | --- |
| CQ-001 | ¿Existen diferencias relevantes por plataforma, placement, device u otra superficie Meta? | La dimensión está disponible y es comparable. | Comparación segmentada con limitaciones. |
| CQ-002 | ¿Qué aporta `ticket_status` u otra dimensión CRM/post-lead a la lectura de calidad? | La fuente está autorizada, trazable y con cobertura suficiente. | Lectura post-lead separada del scoring FARO. |
| CQ-003 | ¿Existe evidencia suficiente para interpretar madurez CAPI o eventos Meta posteriores? | Hay evidencia vigente y autorizada sobre CAPI/eventos. | Lectura descriptiva sin inferir causalidad no validada. |
| CQ-004 | ¿Puede aislarse una lectura robusta de Tier A o alta calidad? | El denominador y volumen permiten comparabilidad. | Lectura de eficiencia y concentración de alta calidad. |
| CQ-005 | ¿Hay metadata creativa adicional más allá de `ad_name`? | La metadata está disponible y no requiere inferencias visuales externas. | Lectura creativa descriptiva y no causal. |
| CQ-006 | ¿Puede conectarse calidad con conversión comercial, revenue o ventas? | La fuente CRM/comercial está autorizada y reconciliada. | Lectura de negocio separada del producto base. |
| CQ-007 | ¿Es comparable la evolución semanal completa? | Existen semanas completas o reglas explícitas para semanas parciales. | Análisis semanal con advertencia sobre parcialidad. |

### 8.3 Preguntas no aplicables

| ID | Pregunta no aplicable | Motivo |
| --- | --- | --- |
| NAQ-001 | ¿Cuál es el efecto causal de una creatividad, campaña o anuncio? | Requiere diseño experimental o causalidad validada. |
| NAQ-002 | ¿Qué cambios operativos debe ejecutar automáticamente Meta Ads? | Pertenece a implementación o decisión humana posterior. |
| NAQ-003 | ¿Cómo debe modificarse el pipeline de datos o runtime? | Pertenece a fases de implementación, no a P01. |
| NAQ-004 | ¿Qué valores exactos debe reproducir el producto a partir de informes históricos? | Los históricos no son expected values. |
| NAQ-005 | ¿Cómo debe generalizarse este contrato a toda la Foundation? | Este contrato es local de AUC-001. |

---

## 9. Matriz de cobertura integrada del contrato

La matriz es parte normativa del contrato. Cada ejecución futura que declare conformidad con este contrato debe evaluar sus filas por pregunta, criticidad y estado de cobertura.

| ID | Criticidad | Vista analítica requerida | Evidencia mínima | Interpretación mínima | Recomendación requerida | Estado válido |
| --- | --- | --- | --- | --- | --- | --- |
| AQ-001 | Obligatoria alta | Vista de volumen y captación | Leads totales, periodo, granularidad temporal básica, cobertura. | Ritmo de captación, cambios de volumen y cautelas por periodo parcial, sin interpretar calidad temporal. | No obligatoria salvo cambio accionable. | `complete`, `partial`, `UNKNOWN`, `blocked` |
| AQ-002 | Obligatoria alta | Vista de calidad FARO | Distribución por tiers, A/B, Tier A, denominadores. | Lectura de calidad relativa y peso de segmentos valiosos. | No obligatoria salvo oportunidad clara. | `complete`, `partial`, `blocked` |
| AQ-003 | Obligatoria alta | Vista coste-calidad reconciliada | Spend, leads matched, cobertura, métricas canónicas SPEC-012. | Eficiencia económica con universo explícito. | Si hay optimización económica, debe ser medible. | `complete`, `partial`, `blocked` |
| AQ-004 | Obligatoria alta | Vista campaña/adset | Volumen, calidad, coste cuando esté reconciliado. | Comparación volumen-calidad-coste y sesgos de cobertura. | Requerida si se priorizan campañas/adsets. | `complete`, `partial`, `blocked` |
| AQ-005 | Obligatoria media-alta | Vista anuncio/creatividad | `ad_id_norm` o identificador técnico equivalente, métricas por anuncio y `ad_name` si existe. | Valor, desperdicio o dependencia sin causalidad no validada. | Requerida si se propone test creativo. | `complete`, `partial`, `UNKNOWN`, `not_available`, `blocked` |
| AQ-006 | Obligatoria alta | Vista señales explicativas | Señales FARO/formulario/cualificación disponibles. | Asociaciones observadas, no causalidad. | No obligatoria salvo hipótesis testable. | `complete`, `partial`, `UNKNOWN`, `not_available`, `blocked` |
| AQ-007 | Obligatoria alta | Vista trade-off | Comparaciones cruzadas volumen-calidad-coste. | Tensión de negocio y coste de oportunidad. | Requerida si se propone redistribución. | `complete`, `partial`, `blocked` |
| AQ-008 | Obligatoria media-alta | Vista concentración/dependencia | Distribución por entidad, segmento o periodo. | Riesgo por dependencia o concentración. | Requerida si se propone mitigación. | `complete`, `partial`, `UNKNOWN`, `not_available`, `blocked` |
| AQ-009 | Obligatoria alta | Vista temporal de calidad | Serie mensual de calidad y serie semanal si comparable; coste-calidad temporal cuando aplique. | Evolución de calidad, cambios interpretables, estabilidad y límites de semanas parciales. | Requerida si se propone calendario de acción. | `complete`, `partial`, `UNKNOWN`, `blocked` |
| AQ-010 | Obligatoria alta | Vista de oportunidades | Knowledge Set aprobado y trazable. | Prioridad, impacto esperado, incertidumbre. | Si hay acción, debe clasificarse como experimento medible o acción verificable. | `complete`, `partial`, `UNKNOWN`, `not_available`, `blocked` |
| AQ-011 | Obligatoria alta | Vista de límites | Cobertura, reconciliación, missingness, `UNKNOWN` y `not_available`. | Impacto de límites sobre lectura y decisión. | No aplicable. | `complete`, `partial`, `UNKNOWN`, `blocked` |
| CQ-001 | Condicional | Vista plataforma/superficie | Dimensión comparable. | Diferencias segmentadas y cautelas. | Solo si hay acción segmentada. | `complete`, `partial`, `not_available`, `not_applicable` |
| CQ-002 | Condicional | Vista post-lead/CRM | `ticket_status` u otra dimensión autorizada. | Separación entre calidad FARO y estado comercial. | Solo si hay acción sobre proceso comercial. | `complete`, `partial`, `not_available`, `not_applicable` |
| CQ-003 | Condicional | Vista CAPI/eventos | Evidencia vigente de eventos. | Madurez o limitación descriptiva. | Solo si hay experimento de tracking. | `complete`, `partial`, `not_available`, `not_applicable` |
| CQ-004 | Condicional | Vista alta calidad | Tier A o segmento equivalente con volumen suficiente. | Lectura robusta o declaración de insuficiencia. | Solo si hay acción sobre alta calidad. | `complete`, `partial`, `UNKNOWN`, `not_applicable` |
| CQ-005 | Condicional | Vista metadata creativa | Metadata disponible y trazable. | Patrones descriptivos sin inferencia visual no autorizada. | Solo si hay test creativo. | `complete`, `partial`, `not_available`, `not_applicable` |
| CQ-006 | Condicional | Vista conversión/revenue | Fuente comercial reconciliada. | Relación negocio-calidad con límites. | Solo si hay acción comercial. | `complete`, `partial`, `not_available`, `not_applicable` |
| CQ-007 | Condicional | Vista semanal completa | Semanas completas o reglas de comparabilidad. | Cambios semanales y advertencia de parcialidad. | Solo si hay decisión temporal. | `complete`, `partial`, `not_available`, `not_applicable` |

Ninguna fila puede marcarse `complete` por contener solamente una tabla o una sección nominal.

---

## 10. Vistas analíticas requeridas

Las siguientes vistas son requisitos de producto. No prescriben formato visual único.

| Vista | Granularidad mínima | Métricas o campos mínimos | Finalidad |
| --- | --- | --- | --- |
| Volumen y evolución | Periodo total y tiempo | Leads, periodo, cobertura temporal. | Entender escala y dinámica. |
| Calidad FARO | Tier y periodo | Tier A, Tier B, A/B, total, tasas con denominador. | Entender valor relativo de leads. |
| Coste-calidad reconciliada | Signal/campaña/adset cuando aplique | Spend, matched leads, matched A/B, matched Tier A, métricas canónicas. | Evaluar eficiencia económica sin universos ambiguos. |
| Campaña/adset | Campaña y conjunto | Volumen, calidad, coste, cobertura. | Comparar unidades de inversión. |
| Anuncio/creatividad | `ad_id_norm` y `ad_name` si disponible | Volumen, calidad, coste, cobertura. | Detectar concentración, valor o desperdicio por anuncio. |
| Temporal | Mes y semana comparable | Volumen, calidad, coste si aplica. | Detectar tendencia, cambio o estacionalidad operativa. |
| Señales explicativas | Señal FARO/formulario/segmento | Distribuciones, tasas, volumen y cobertura. | Explicar calidad observada sin causalidad no validada. |
| Concentración/dependencia | Entidad relevante | Peso relativo, contribución a calidad/coste, dependencia. | Identificar riesgo estructural. |
| Límites y cobertura | Fuente, join, estado de reconciliación | matched, lead-only, spend-only, `UNKNOWN`, missingness. | Evitar sobreinterpretación. |
| Oportunidades y acciones | Recomendación o hipótesis | categoría, hipótesis o justificación, acción, métrica o resultado verificable, guardrail cuando aplique, ventana o criterio de cierre. | Separar experimentos medibles, acciones verificables e hipótesis no accionables. |

---

## 11. Requisitos de contenido

Un producto conforme debe contener:

* identificación del periodo, alcance y fuentes autorizadas;
* declaración de coverage status por pregunta analítica;
* respuestas a las preguntas obligatorias o declaración justificada de bloqueo;
* vistas analíticas requeridas o formatos equivalentes;
* métricas canónicas de coste-calidad cuando se trate eficiencia económica;
* separación explícita entre evidencia, interpretación, conocimiento y recomendaciones;
* limitaciones y `UNKNOWN` visibles cerca de la decisión que condicionan;
* recomendaciones accionables clasificadas como experimentos medibles o acciones verificables cuando proceda;
* trazabilidad suficiente a Evidence Set, runtime output o artefacto autorizado.

---

## 12. Criterios verificables de completitud

Una pregunta obligatoria está completa solo si cumple todos estos criterios:

* la pregunta está identificada de forma explícita;
* existe evidencia autorizada asociada;
* se declara el universo y denominador utilizado;
* se incluye comparación relevante cuando la pregunta lo requiere;
* se interpreta el resultado sin mezclarlo con evidencia cruda;
* se explica la implicación de negocio;
* se declara limitación, incertidumbre o ausencia relevante;
* se ofrece conclusión, hipótesis o `UNKNOWN` justificado;
* la matriz integrada refleja el mismo estado que el contenido narrativo;
* no se violan métricas prohibidas, causalidad no validada ni universos ambiguos.

Una pregunta condicional está completa solo si, además de lo anterior, se justifica por qué aplica.

Una pregunta no aplicable debe indicar por qué queda fuera de boundary.

---

## 13. Criterios verificables de profundidad

La profundidad mínima se evalúa por pregunta, no por extensión textual.

Debe poder verificarse que la respuesta contiene:

* evidencia: qué se observó;
* comparación: contra qué entidad, periodo, segmento, baseline o alternativa se interpreta;
* interpretación: qué significa analíticamente;
* implicación de negocio: por qué importa para decisiones sobre Meta Lead Ads;
* limitación o incertidumbre: qué no puede concluirse o con qué cobertura;
* conclusión o hipótesis: qué queda establecido o qué debe validarse después.

Para preguntas obligatorias, la ausencia de cualquiera de estos elementos degrada el estado a `partial` o `blocked`, según criticidad.

---

## 14. Criterios verificables de calidad analítica

Un producto conforme debe:

* usar métricas canónicas de SPEC-012 cuando trate coste-calidad;
* preservar estados de cobertura de SPEC-013 cuando use salida reconciliada;
* evitar CPL, CPQL o CPHQL genéricos sin universo, denominador y cobertura;
* no usar `ad_name` como clave técnica ni fallback de join;
* no inferir causalidad creativa, causalidad de plataforma ni eficacia comercial sin evidencia validada;
* separar descriptive findings, knowledge, recommendations y presentation;
* declarar cuando una lectura es asociativa, exploratoria o experimental;
* mantener consistencia entre matriz de cobertura, narrativa y recomendaciones;
* no ocultar `UNKNOWN` por razones de fluidez ejecutiva;
* no transformar recomendaciones en órdenes operativas no validadas.

---

## 15. Regla mínima de robustez y suficiencia de muestra

P01 no fija umbrales numéricos universales para todo periodo, segmento o entidad. Sí fija una regla contractual mínima que debe aplicarse antes de declarar una lectura como concluyente.

Toda vista, ranking, comparación, recomendación o hipótesis debe declarar:

* denominador utilizado;
* volumen observado;
* cobertura aplicable;
* granularidad temporal o segmentación;
* comparador utilizado;
* si la muestra es suficiente, baja o no evaluable para la conclusión propuesta.

Cuando el volumen, denominador o cobertura no permitan sostener una conclusión, el producto debe degradar la fila afectada a `partial` o declarar la conclusión como `UNKNOWN`.

Cuando falte la fuente, dimensión o métrica necesaria para evaluar la robustez, debe usarse `not_available`.

Queda prohibido declarar rankings concluyentes, ganadores, perdedores, desperdicio, concentración material, cambios temporales o recomendaciones de optimización sobre muestras insuficientes sin marcar explícitamente `low_sample`, `partial` o `UNKNOWN`.

Los umbrales numéricos específicos podrán calibrarse en fases posteriores, pero la regla de denominador, cobertura, comparador y degradación por baja muestra queda resuelta por esta Specification.

---

## 16. Restricciones interpretativas

El contrato prohíbe:

* convertir informes históricos en expected values;
* asumir que una dimensión ausente no existe en negocio;
* imputar `ticket_status` desde calidad FARO;
* imputar calidad comercial desde interacciones de Meta sin contrato específico;
* comparar entidades con cobertura incompatible sin advertencia;
* interpretar semanas parciales como semanas completas;
* declarar ganadores creativos por `ad_name` sin controlar volumen, cobertura y contexto;
* presentar recomendaciones como decisiones ya aprobadas;
* mezclar núcleo común y proyección ejecutiva hasta cambiar el significado analítico.

---

## 17. Tratamiento de `UNKNOWN`, evidencia insuficiente y cobertura parcial

`UNKNOWN` es un resultado analítico válido. Debe usarse cuando la evidencia autorizada no permite concluir, incluso si existe una expectativa de negocio o una comparación histórica.

La evidencia insuficiente debe documentarse con pregunta afectada, fuente o dimensión ausente, impacto sobre interpretación, impacto sobre recomendación, estado de cobertura y condición necesaria para resolverla después.

La cobertura parcial debe distinguir parcialidad por periodo, join, reconciliación, dimensión no disponible, volumen bajo, ausencia de comparador o granularidad insuficiente.

---

## 18. Núcleo común, proyección analítica y proyección ejecutiva

### 18.1 Núcleo común del producto

El núcleo común contiene lo que debe ser semánticamente idéntico en cualquier proyección:

* periodo y scope;
* fuentes autorizadas;
* Evidence references;
* métricas canónicas;
* preguntas cubiertas;
* coverage status;
* Knowledge claims;
* recomendaciones aprobadas, si existen;
* limitaciones, incertidumbres y `UNKNOWN`.

### 18.2 Proyección analítica

La proyección analítica puede incluir mayor detalle técnico y diagnóstico:

* vistas completas;
* comparaciones extensas;
* estados de reconciliación;
* notas metodológicas;
* lectura de señales;
* interpretación por pregunta;
* matriz de cobertura completa.

No puede crear evidencia nueva ni modificar conclusiones del núcleo común.

### 18.3 Proyección ejecutiva

La proyección ejecutiva puede resumir para decisión:

* mensajes principales;
* implicaciones de negocio;
* oportunidades priorizadas;
* riesgos y límites;
* recomendaciones experimentales.

No puede ocultar limitaciones materiales, degradar `UNKNOWN` a certeza ni convertir hipótesis en conclusión.

---

## 19. Comparación funcional de producto

| Dimensión | Producto histórico | Producto actual | Producto objetivo P01 |
| --- | --- | --- | --- |
| Naturaleza | Producto monolítico rico, mezclaba análisis, narrativa, recomendaciones y posibles acciones. | Producto metodológicamente más controlado, con runtime consumible y reconciliación estructurada. | Producto con contrato explícito de suficiencia, profundidad y separación de capas. |
| Fuente de verdad | No debe usarse como expected values. | SPEC-012, SPEC-013, Analytical Contract y outputs vigentes autorizados. | Contrato P01 como criterio de producto sobre evidencia vigente. |
| Cobertura | Amplia en apariencia, con riesgo de mezcla de boundaries. | Sólida en coste-calidad y reconciliación, parcial en dimensiones de producto. | Cobertura evaluada por pregunta y criticidad. |
| Recomendaciones | Orientadas a acción, no siempre formuladas como experimentos medibles. | Existentes de forma más limitada o residual según ejecución. | Acciones formuladas como hipótesis experimentales con métrica y criterio de éxito. |
| Presentación | Una narrativa unificada. | Separación creciente entre evidencia, conocimiento y presentación. | Núcleo común con proyecciones analítica y ejecutiva equivalentes semánticamente. |
| `UNKNOWN` | Podía quedar diluido por narrativa. | Más visible por contratos de evidencia y reconciliación. | Obligatorio, verificable y cercano a la pregunta afectada. |

---

## 20. Clasificación definitiva de residuos P0/P01

### 20.1 `ad_name`

`ad_name` queda clasificado como requisito de producto condicional y etiqueta interpretativa.

Debe incluirse en la vista anuncio/creatividad cuando esté disponible en evidencia autorizada. Mejora legibilidad, auditabilidad y utilidad ejecutiva, pero no sustituye a `ad_id_norm` como identificador técnico, no puede usarse como clave de join y no puede funcionar como fallback.

Su ausencia puede ser `not_available` si está justificada y la pregunta puede responderse por identificador técnico. Su ausencia degrada la calidad ejecutiva si impide interpretar anuncios de forma accionable, pero no bloquea AQ-005 por sí sola.

AQ-005 solo puede quedar `blocked` si falta toda granularidad autorizada de anuncio/creatividad, si no existe `ad_id_norm` ni identificador técnico equivalente, si las métricas mínimas por anuncio no pueden trazarse, o si la cobertura disponible obliga a inferir valor, desperdicio o dependencia sin soporte suficiente.

### 20.2 `ticket_status`

`ticket_status` queda clasificado como pregunta condicional post-lead/CRM.

No es requisito obligatorio del núcleo AUC-001 mientras no exista fuente autorizada, trazable y reconciliada. Si está disponible, debe separarse del scoring FARO y tratarse como dimensión de conversión o estado comercial posterior.

No puede imputarse desde tier, coste o comportamiento de anuncio. Su ausencia justificada no incumple automáticamente el contrato. Si en una fase posterior bloquea una pregunta obligatoria aprobada, debe registrarse como brecha contractual.

### 20.3 Evolución semanal

La evolución semanal queda clasificada como requisito temporal obligatorio condicionado por comparabilidad.

La pregunta temporal AQ-009 es obligatoria. El producto debe incluir una lectura temporal comparable. La vista mensual es el mínimo cuando la semanal no sea comparable. La vista semanal debe incluirse cuando existan semanas completas o reglas explícitas para semanas parciales.

Una semana parcial no puede compararse como semana completa. La ausencia de evolución semanal detallada puede ser `partial` o `not_available` si se justifica. Si la decisión depende de cambios semanales, la falta de comparabilidad debe declararse como limitación material.

### 20.4 Recomendaciones como experimentos medibles o acciones verificables

Las recomendaciones quedan clasificadas como requisito de calidad de producto cuando proponen acción.

Toda recomendación accionable debe clasificarse en una de estas categorías:

| Categoría | Uso | Requisitos mínimos |
| --- | --- | --- |
| `measurable_experiment` | Optimización, test creativo, redistribución, segmentación o hipótesis que requiere contraste. | Hipótesis, acción, población afectada, métrica primaria, guardrail, dirección esperada, criterio de éxito, ventana de validación, dependencia de evidencia, incertidumbre y condición de parada o revisión. |
| `verifiable_action` | Acción auditable sin diseño experimental, como revisar tracking, etiquetado, cobertura, nomenclatura o proceso documental. | Acción, responsable funcional futuro si aplica, evidencia que la justifica, resultado verificable, criterio de cierre, riesgo y dependencia. |
| `non_actionable_hypothesis` | Oportunidad o explicación plausible que aún no debe ejecutarse. | Hipótesis, soporte, incertidumbre, evidencia faltante y condición para promoverla a experimento o acción verificable. |

Una recomendación sin clasificación no puede presentarse como acción lista para ejecución.

Una recomendación de optimización no puede degradarse a `verifiable_action` para evitar definir métrica, guardrail, criterio de éxito o ventana de validación.

---

## 21. Criterios de aceptación de la Specification

Esta Specification está lista para Reviewer Agent si cumple:

* define el boundary de AUC-001-P01 como contrato y no implementación;
* integra la matriz de cobertura en el propio contrato;
* clasifica preguntas obligatorias, condicionales y no aplicables;
* separa contenido, calidad y restricciones interpretativas;
* define estados `complete`, `partial`, `not_available`, `not_applicable`, `UNKNOWN` y `blocked`;
* establece profundidad mínima verificable por pregunta;
* define regla mínima de robustez y suficiencia de muestra;
* distingue `UNKNOWN` como conclusión no resoluble de `not_available` como ausencia de fuente, dimensión o métrica;
* permite vistas equivalentes en lugar de tablas literales;
* impide declarar completitud por mera presencia formal;
* trata los residuos P0/P01 de forma definitiva;
* conserva precedencia de Analytical, Evidence, Knowledge, Recommendation y Presentation Contracts;
* no crea tareas, gates, código ni outputs de ejecución;
* no usa outputs históricos como fuente de nuevo conocimiento.

---

## 22. Criterios de aceptación del contrato en fases posteriores

Una implementación futura que reclame conformidad con este contrato deberá demostrar:

* evaluación de cobertura por pregunta y criticidad;
* matriz rellenada con estados y justificaciones;
* evidencia trazable por pregunta;
* vistas analíticas requeridas o equivalentes válidos;
* métricas canónicas donde aplique;
* tratamiento visible y distinguible de `UNKNOWN`, `not_available` y cobertura parcial;
* recomendaciones clasificadas como experimentos medibles, acciones verificables o hipótesis no accionables cuando haya acción propuesta;
* separación entre núcleo común y proyecciones;
* ausencia de inferencias prohibidas.

Estos criterios no son un gate creado por P01. Son condiciones contractuales para fases posteriores.

---

## 23. Cuestiones abiertas

Quedan abiertas para revisión humana o fases posteriores:

* si `ticket_status` debe incorporarse en un futuro como fuente autorizada del producto o permanecer fuera del núcleo;
* qué campos concretos de metadata creativa, además de `ad_name`, estarán disponibles y con qué cobertura;
* qué regla de comparabilidad semanal debe aprobarse para periodos con semanas parciales;
* qué formato operativo adoptará la matriz de cobertura en una implementación futura;
* qué umbrales cuantitativos específicos deben calibrarse en fases posteriores para aplicar la regla mínima de robustez por Tier A, anuncio o segmento;
* si el contrato local de AUC-001 debe convertirse más adelante en patrón reutilizable para otros Analytical Use Cases.

---

## 24. No objetivos

Esta Specification no pretende:

* validar una ejecución analítica;
* producir un informe;
* definir tareas de implementación;
* crear un QA Gate;
* modificar pipelines;
* consultar fuentes externas;
* ampliar el modelo canónico de coste-calidad;
* reemplazar contratos transversales;
* elevar este contrato a Foundation sin evaluación posterior.

---

## 25. Resultado esperado de P01

El resultado esperado de AUC-001-P01 es la aprobación documental del Contrato de Producto Analítico específico de AUC-001.

Después de su aprobación, fases posteriores podrán implementar soporte runtime o documental para la matriz, generar productos analíticos conformes, validar experimentalmente el contrato, abrir tareas específicas para gaps de datos o presentación y evaluar si el contrato local merece generalización.

Ninguna de esas acciones forma parte de P01.

---

## 26. Readiness para Reviewer Agent

La Specification está preparada para revisión metodológica por Reviewer Agent.

La revisión debería comprobar:

* consistencia con el memo arquitectónico;
* consistencia con Analytical, Evidence, Knowledge, Recommendation y Presentation Contracts;
* suficiencia de la matriz integrada;
* claridad de boundary P01;
* tratamiento correcto de residuos P0/P01;
* ausencia de expected values históricos;
* ausencia de implementación, tareas, gates u outputs.
