# AUC-001 Evidence to Knowledge Independent Research

## 1. Propósito

Este documento reconstruye de forma independiente cómo se transforma evidencia en conocimiento, implicaciones y recomendaciones en AUC-001 — Meta Lead Quality Analysis.

El objetivo no es diseñar una solución ni modificar el lifecycle. El objetivo es observar, desde artefactos primarios y Git, qué operaciones analíticas aparecen entre Evidence y Knowledge, qué parte de la profundidad procede del prompt histórico, de la skill, del runbook, del AUC, de la evidencia disponible o del razonamiento emergente del modelo.

## 2. Regla de independencia aplicada

Se aplicó la regla de independencia de la investigación:

- No se usaron como fuente principal evaluaciones comparativas previas sobre esta regresión.
- No se leyó `docs/evaluations/auc-001-knowledge-construction-comparative-analysis.md`, detectado en el working tree como documento no trackeado y potencialmente contaminante por su título.
- No se usaron conclusiones de documentos de regresión como base analítica.
- La reconstrucción se realizó desde AUC-001, skill, runbook, checklist, contracts, handoffs actuales, outputs históricos, prompt histórico adjunto y versiones Git de artefactos primarios.

## 3. Corpus utilizado

Corpus primario revisado:

| Tipo | Artefacto |
|---|---|
| Analytical Use Case | `analytical_use_cases/meta_lead_quality_analysis.md` |
| Skill actual | `.github/skills/meta-lead-quality-analysis/SKILL.md` |
| Runbook actual | `.github/skills/meta-lead-quality-analysis/RUNBOOK.md` |
| Checklist actual | `.github/skills/meta-lead-quality-analysis/CHECKLIST.md` |
| Referencias de skill | `.github/skills/meta-lead-quality-analysis/references.md` |
| Prompt actual de evaluación | `.github/prompts/lead_quality_analytical_report.md` |
| Prompt histórico adjunto | `C:\Users\jordi\.codex\attachments\c136334f-3dbf-4bd7-9dba-ca1c6908506e\pasted-text.txt` |
| Encargo de investigación | `C:\Users\jordi\.codex\attachments\75e652c1-9378-4d01-bc2c-8b275be9212f\pasted-text.txt` |
| Output histórico | `docs/evaluations/corpus/informe_calidad_leads_20260510.md` |
| Output histórico experimental | `docs/evaluations/corpus/informe_calidad_leads_scoring_20260701.md` |
| Evidence actual | `docs/handoffs/auc-001-evidence-set.md` |
| Knowledge actual | `docs/handoffs/auc-001-knowledge-set.md` |
| Recommendations actual | `docs/handoffs/auc-001-recommendation-set.md` |
| Presentation actual | `docs/handoffs/auc-001-executive-report.md` |
| Presentation Contract | `docs/handoffs/auc-001-presentation-contract.md` |
| Presentation Policy | `.github/presentation_policies/executive-decision-support.md` |
| Lifecycle | `specs/spec-001-analytical-lifecycle.md` |
| Base contracts | `docs/contracts/evidence.contract.md`, `docs/contracts/knowledge.contract.md`, `docs/contracts/recommendation.contract.md` |
| Output actual desde Git | `git show 59441c9:outputs/evaluations/auc-001-report-quality-test-2026-06.md` |
| Output histórico desde Git | `git show 59441c9:outputs/meta-lead-quality-historical-to-2026-06-30-executive-report.md` |
| Historial skill | `git show 4d6b8e3:.github/skills/meta-lead-quality-analysis/SKILL.md`, `git show 6a141d5:.github/skills/meta-lead-quality-analysis/SKILL.md`, `git show 8789eed:.github/skills/meta-lead-quality-analysis/SKILL.md`, `git show b78c351:.github/skills/meta-lead-quality-analysis/SKILL.md` |

## 4. Corpus excluido para evitar contaminación

| Artefacto | Motivo |
|---|---|
| `docs/evaluations/auc-001-knowledge-construction-comparative-analysis.md` | Documento no trackeado con título directamente relacionado con comparación de construcción de conocimiento. Se registró, pero no se leyó. |
| `docs/evaluations/auc-001-regression-root-cause-analysis.md` | Por título, contiene análisis causal previo de regresión. No se usó como fuente principal. |
| `docs/evaluations/auc-001-regression-containment-review.md` | Por título, contiene revisión de contención de regresión. No se usó como fuente principal. |
| `docs/evaluations/auc-001-reasoning-recommendations-evaluation.md` | Evaluación posterior sobre reasoning/recommendations. No se usó como fuente principal. |
| `docs/evaluations/auc-001-presentation-output-evaluation.md` | Evaluación posterior de salida. No se usó como fuente principal. |

## 5. Método

El método aplicado fue:

1. Localizar artefactos primarios actuales y outputs históricos.
2. Leer el AUC, skill, runbook, checklist, contracts y handoffs actuales.
3. Leer el prompt histórico y los informes de ejemplo del corpus.
4. Consultar Git para reconstruir cambios relevantes de la skill y outputs no presentes en el árbol actual.
5. Reconstruir cadenas concretas de razonamiento con esta forma:

```text
Pregunta analítica
→ Evidencia utilizada
→ Operación aplicada
→ Resultado intermedio
→ Finding
→ Knowledge
→ Implicación
→ Recomendación
```

6. Separar cada operación en tres niveles: método analítico, aplicación de dominio y dependencia concreta del dataset.
7. Evaluar hipótesis alternativas sin convertir observaciones en arquitectura o Specification.

## 6. Reconstrucción del proceso histórico

### Cadena histórica A: no optimizar solo por volumen

| Paso | Reconstrucción |
|---|---|
| Pregunta analítica | ¿Estamos captando suficiente volumen y suficiente calidad? |
| Evidencia utilizada | Informe 2026-05-10: 342 leads, 111 A+B, 32,5% qualified, score medio 50,8; distribución A/B/C/D. |
| Operación aplicada | Distribution Analysis + Thresholding + Business Interpretation. |
| Resultado intermedio | El volumen es suficiente para leer patrones, pero solo un tercio tiene señal inicial de calidad. |
| Finding | Lead generado y lead cualificado no son equivalentes. |
| Knowledge | Optimizar Meta únicamente hacia formularios enviados puede reforzar captación barata o inmadura. |
| Implicación | La señal relevante debe distinguir calidad, no solo volumen. |
| Recomendación | Crear `Qualified Lead = score >= 60` y usar A+B como señal inicial de calidad. |

### Cadena histórica B: creatividad de volumen frente a creatividad de calidad

| Paso | Reconstrucción |
|---|---|
| Pregunta analítica | ¿Qué creatividades generan más volumen y cuáles generan mejor calidad? |
| Evidencia utilizada | Informe 2026-05-10: `ViajaComoInvitado` 151 leads, 49,8 score, 30,5% A+B; `ViajeSinEstres` 122 leads, 49,3 score, 28,7% A+B; `FiltroBilletes_AutoSegmentacion` 49 leads, 54,6 score, 42,9% A+B. |
| Operación aplicada | Comparative Analysis + Quality/Volume Trade-off + Ranking. |
| Resultado intermedio | Las piezas de mayor volumen no son las de mayor calidad relativa. |
| Finding | `FiltroBilletes` filtra mejor, aunque aporta menos volumen. |
| Knowledge | La creatividad puede funcionar como mecanismo de auto-segmentación, no solo como generadora de alcance. |
| Implicación | Las decisiones creativas no deben basarse solo en volumen o CPL. |
| Recomendación | Incorporar score medio y % A+B a la evaluación de campañas y creatividades. |

### Cadena histórica C: variable explicativa de calidad

| Paso | Reconstrucción |
|---|---|
| Pregunta analítica | ¿Qué variables explican mejor la calidad declarada? |
| Evidencia utilizada | Informe 2026-07-01: billetes `solo mirando` 5,3% qualified; `en proceso` 59,6%; `sí, ya los tengo` 89,0% y 28,0% high quality. |
| Operación aplicada | Segmentation + Gradient Analysis + Explanatory Variable Assessment. |
| Resultado intermedio | La cualificación aumenta de forma marcada al avanzar el estado de billetes. |
| Finding | Billetes comprados o en proceso son señales fuertes de intención. |
| Knowledge | La intención declarada de viaje es más explicativa que el volumen agregado de leads. |
| Implicación | El equipo comercial y Meta CAPI deben distinguir señales de intención. |
| Recomendación | Priorizar leads con billetes y considerar señales como `LeadWithTickets`. |

### Cadena histórica D: eficiencia económica y decisión creativa

| Paso | Reconstrucción |
|---|---|
| Pregunta analítica | ¿Qué anuncios conviene escalar, revisar o limitar? |
| Evidencia utilizada | Informe 2026-07-01: creatividad, spend, leads, CPL, score, qualified, CPQL, high quality, CPHQL. |
| Operación aplicada | Cost Efficiency Analysis + Quality Segmentation + Decision Matrix. |
| Resultado intermedio | Algunas piezas con bajo CPL no son las mejores por qualified/high quality; otras con bajo volumen muestran mejor CPHQL. |
| Finding | La eficiencia real aparece al cruzar coste con calidad, no al mirar CPL aislado. |
| Knowledge | La escala debe balancear volumen, calidad, coste y robustez de muestra. |
| Implicación | Una matriz de decisión reduce el riesgo de escalar tráfico barato de baja calidad. |
| Recomendación | Escalar/priorizar piezas con buen CPQL/CPHQL y revisar piezas con volumen pero baja cualificación. |

### Observación histórica

En los outputs históricos, findings y knowledge aparecen mezclados dentro del informe final, pero existen pasos intermedios reconocibles: distribución, segmentación, comparación, relación entre variables, evaluación de robustez por volumen, lectura estratégica, implicación y recomendación. La profundidad no aparece como una única operación, sino como composición repetida de operaciones.

## 7. Reconstrucción del proceso actual

### Cadena actual A: concentración en una referencia de anuncio

| Paso | Reconstrucción |
|---|---|
| Pregunta analítica | ¿Dónde se concentra la evidencia matched de calidad y spend? |
| Evidencia utilizada | Evidence actual EVD-003: `ViajeSinEstres_AlivioEmocional` con 519 leads, 152 A/B y 374,79 spend en junio de 2026. |
| Operación aplicada | Concentration Analysis + Maxima Identification. |
| Resultado intermedio | Una referencia es la mayor por leads, A/B y spend dentro de matched. |
| Finding | La evidencia matched está concentrada en una referencia de anuncio. |
| Knowledge | INS-001: concentración observada, sin causalidad ni recomendación. |
| Implicación | Debe tratarse como concentración, no como superioridad creativa. |
| Recomendación | REC-001: usar evidencia matched ad-level como base primaria para discusiones de eficiencia. |

### Cadena actual B: separación RTG lead-only

| Paso | Reconstrucción |
|---|---|
| Pregunta analítica | ¿Puede compararse RTG con CAPTACION por eficiencia económica? |
| Evidencia utilizada | EVD-004: CAPTACION/ABO matched con 680 leads, 191 A/B y 494,36 spend; RTG/CBO lead-only con 92 leads y 35 A/B sin spend emparejado. |
| Operación aplicada | Coverage Classification + Boundary Reasoning. |
| Resultado intermedio | RTG aporta calidad lead-side pero no eficiencia comercial emparejada. |
| Finding | Existen dos coverage states distintos. |
| Knowledge | INS-002/HYP-002: RTG debe interpretarse como caso separado. |
| Implicación | No se debe inferir coste o rentabilidad de RTG. |
| Recomendación | REC-002 y REC-003: separar RTG lead-only y validar mapping antes de recomendaciones de spend por campaña/adset. |

### Cadena actual C: limitación creativa

| Paso | Reconstrucción |
|---|---|
| Pregunta analítica | ¿Qué puede decirse sobre creatividades? |
| Evidencia utilizada | Evidence actual: solo `ad_id_norm` y `ad_name`; no hay metadata de asset creativo. |
| Operación aplicada | Evidence Sufficiency Check + Scope Limitation. |
| Resultado intermedio | Se puede razonar a nivel referencia de anuncio, no a nivel asset, formato, visual o copy. |
| Finding | La metadata creativa es insuficiente para causalidad creativa. |
| Knowledge | RSK-003/UNC-004: riesgo de convertir concentración en causalidad creativa. |
| Implicación | Cualquier lectura creativa debe quedar limitada al nombre de anuncio. |
| Recomendación | REC-004: mantener recomendaciones creativas a nivel ad reference salvo que se añada metadata. |

### Qué está definido explícitamente

- Separación de Context, Evidence, Knowledge, Recommendations y Presentation.
- Dependencia de Evidence Contract antes de Knowledge.
- Prohibición de crear evidencia en Knowledge.
- Prohibición de crear conocimiento o recomendaciones en Presentation.
- Propagación de limitations, UNKNOWN y coverage states.

### Qué está solo sugerido

- Qué operaciones analíticas concretas debe aplicar Knowledge Generation.
- Cómo priorizar entre comparación, concentración, temporalidad, segmentación, robustez y eficiencia.
- Cómo convertir una tabla de evidencia en preguntas de negocio.
- Cómo decidir que un insight es suficientemente profundo.

### Qué depende de la iniciativa del modelo

- Elegir las preguntas analíticas relevantes.
- Componer operaciones.
- Evaluar trade-offs entre volumen, calidad, coste y robustez.
- Detectar variables explicativas.
- Transformar hallazgos en lectura estratégica.

### Qué ha desaparecido o se ha debilitado

- La obligación explícita de analizar todas las variables relevantes.
- La estructura histórica por variables, relaciones, creatividad, campaña, eficiencia, temporalidad, plataformas y combinaciones.
- La matriz de decisión calidad/coste.
- El salto guiado desde métrica a implicación de negocio.
- La sobreprescripción de preguntas ejecutivas del prompt histórico.

### Qué se ha trasladado a otra capa

- La estructura narrativa se trasladó a Presentation.
- La validación de límites y trazabilidad se reforzó en contracts/checklist.
- La forma ejecutiva se trasladó a Presentation Policy.
- Parte de la pregunta “qué significa para Dirección” queda en Presentation, aunque Presentation no puede generar nuevo knowledge.

## 8. Pipeline Evidence → Knowledge observado

Pipeline observado en outputs de mayor profundidad:

```text
Evidence table
→ segmentation / comparison / ranking / ratio
→ intermediate pattern
→ materiality or robustness check
→ business meaning
→ finding
→ knowledge statement
→ implication
→ recommendation
```

Pipeline actual formal:

```text
Evidence Set
→ traceable insight / hypothesis / conclusion
→ reasoning priority / risk / uncertainty
→ recommendation
→ presentation
```

Brecha observada:

El pipeline formal define estados y límites, pero no define con suficiente granularidad el conjunto de operaciones que convierten evidencia en findings intermedios. El prompt histórico sí fuerza esas operaciones, aunque mezcladas con salida final y dominio.

## 9. Preguntas analíticas identificadas

Preguntas históricas explícitas:

- ¿Estamos captando suficiente volumen?
- ¿Estamos captando calidad?
- ¿Qué variables explican la calidad?
- ¿Qué campañas funcionan mejor?
- ¿Qué creatividades funcionan mejor?
- ¿Qué anuncios son rentables?
- ¿Dónde se invierte sin generar calidad?
- ¿Qué señales deben alimentar Meta?
- ¿Qué acciones se priorizan?

Preguntas actuales explícitas en runbook:

- ¿Qué patrones aparecen?
- ¿Qué está cambiando?
- ¿Qué explica mejor el rendimiento?
- ¿Qué anomalías existen?
- ¿Qué riesgos aparecen?
- ¿Qué incertidumbres permanecen?

Observación:

Las preguntas actuales son metodológicamente generales y correctas, pero menos operacionalizadas. Las históricas son menos limpias arquitectónicamente, pero activan más operaciones concretas sobre la evidencia.

## 10. Métodos analíticos identificados

| Método | Descripción general | Evidencia de aparición |
|---|---|---|
| Distribution Analysis | Distribuir entidades por categoría o score. | Tiers A/B/C/D en outputs históricos y actuales. |
| Thresholding | Aplicar umbrales para clasificar calidad. | Score >= 60, Tier A/B. |
| Comparative Analysis | Comparar segmentos, campañas, creatividades o plataformas. | Creatividades, campañas, Facebook/Instagram, CAPTACION/RTG. |
| Segmentation | Separar por variable explicativa o coverage state. | Billetes, fecha, experiencia, `matched`/`lead_only`/`spend_only`. |
| Cost Efficiency Analysis | Relacionar gasto con calidad. | CPL, CPQL, CPHQL, spend per qualified. |
| Concentration Analysis | Identificar dependencia de pocos elementos. | INS-001 y outputs históricos sobre piezas dominantes. |
| Temporal Trend Analysis | Comparar evolución por día, semana o mes. | Evolución temporal en outputs históricos y Git. |
| Robustness Evaluation | Condicionar lectura por volumen o muestra. | Bajo volumen en piezas con buena tasa; current boundary states. |
| Coverage Analysis | Determinar qué cruces soporta el modelo. | `matched`, `lead_only`, `spend_only`. |
| Variable Explanatory Assessment | Valorar qué variables explican calidad. | Billetes, fecha, experiencia. |
| Decision Matrix | Traducir patrones a acciones por cuadrantes. | Prompt histórico y output 2026-07-01. |
| Uncertainty Propagation | Mantener límites hasta recomendaciones. | Contracts y handoffs actuales. |

## 11. Aplicaciones específicas de dominio

| Dominio | Aplicación |
|---|---|
| Meta Ads | Comparar campañas, adsets y ad references. |
| Lead Quality | Separar Lead, Qualified Lead, High Quality Lead. |
| Scoring | Usar score o tiers A/B/C/D como señal de calidad. |
| Conversion API | Diferenciar evento `Lead`, `QualifiedLead`, `HighQualityLead`. |
| Marketing Efficiency | Priorizar CPQL/CPHQL frente a CPL. |
| Creative Strategy | Distinguir creatividades de volumen y creatividades de filtro. |
| Commercial Operations | Priorizar leads por intención, urgencia y encaje. |

## 12. Dependencias concretas del dataset

| Dataset / campo | Uso analítico |
|---|---|
| `ad_id`, `ad_id_norm`, `ad_name` | Grano de análisis por referencia de anuncio. |
| `campaign_name`, `adset_name` | Lectura por campaña y conjunto cuando está disponible. |
| `lead_tier`, score | Clasificación A/B/C/D y qualified. |
| `lead_tier IN ('A','B')` | Regla actual de Qualified Lead. |
| `spend_amount` | Eficiencia económica. |
| `campaign_signal = 'COMMERCIAL'` | Filtro de spend comercial. |
| `coverage_status` | Separación matched, lead_only, spend_only. |
| Respuestas de formulario | Billetes, fecha, experiencia, número de personas. |
| Plataforma | Comparación Facebook/Instagram en outputs históricos. |
| Fecha / semana / mes | Evolución temporal. |

## 13. Patrones de composición entre operaciones

Patrones observados:

| Composición | Resultado típico |
|---|---|
| Distribution + Thresholding | Definir Qualified Lead y High Quality Lead. |
| Segmentation + Comparative Analysis | Detectar variables o grupos con mayor calidad. |
| Comparative Analysis + Cost Efficiency | Distinguir volumen barato de calidad eficiente. |
| Concentration + Robustness Evaluation | Identificar piezas dominantes sin sobregeneralizar muestras pequeñas. |
| Coverage Analysis + Cost Efficiency | Evitar eficiencia falsa en `lead_only` o `spend_only`. |
| Temporal Trend + Quality Rate | Detectar deterioro o estabilidad de calidad. |
| Variable Assessment + Business Interpretation | Convertir respuestas de formulario en señales de intención. |
| Quality + Cost + Decision Matrix | Formular acciones de escalar, revisar, limitar o pausar. |
| Limitation Propagation + Recommendation | Formular recomendaciones condicionadas por UNKNOWN. |

Conclusión observacional:

Los findings relevantes rara vez surgen de una sola operación. La profundidad histórica aparece cuando al menos tres operaciones se encadenan: comparación, cualificación de relevancia y traducción a implicación.

## 14. Qué se ganó con el lifecycle actual

Se ganó:

- Trazabilidad fuerte entre evidencia, conocimiento y recomendaciones.
- Separación clara entre Analysis, Reasoning, Recommendations y Presentation.
- Menor riesgo de inventar evidencia.
- Mejor propagación de UNKNOWN, limitations y coverage states.
- Control de alcance por Data Contract y Presentation Contract.
- Capacidad de auditar por IDs de evidence, insight, hypothesis, conclusion y recommendation.
- Protección contra causalidad creativa no soportada.

## 15. Qué se perdió

Se perdió o se debilitó:

- Scaffolding analítico específico para explorar variables, relaciones y combinaciones.
- Presión del prompt para interpretar cada tabla.
- Preguntas ejecutivas que activaban operaciones concretas.
- Evaluación sistemática de trade-offs volumen/calidad/coste.
- Matrices de decisión orientadas a marketing.
- Lectura de madurez comercial a partir de variables de formulario.
- Profundidad narrativa entre finding, implication y recommendation.

Matiz importante:

No todo lo perdido pertenece necesariamente a Foundation. Parte es dominio marketing, parte es AUC-001, parte es prompt histórico y parte depende de columnas concretas disponibles en el dataset.

## 16. Hipótesis alternativas

### Hipótesis 1: el lifecycle actual es correcto, pero AUC-001 está insuficientemente especializado

Evidencia a favor:

- SPEC-001 y contracts definen fases correctas, pero no operaciones de dominio.
- El runbook pregunta “qué explica mejor el rendimiento”, pero no obliga a analizar billetes, fecha, experiencia, CPQL o CPHQL.
- El output de prueba en Git muestra más profundidad cuando se especifica mejor la tarea.

Evidencia en contra:

- AUC-001 sí menciona volumen, calidad, eficiencia, campañas, creatividades y oportunidades.
- La skill histórica inicial también enumeraba esos elementos antes del refactor.

Incertidumbre:

- No está probado si una especialización AUC-001 basta sin cambiar Foundation.

Valoración:

Hipótesis fuerte. La evidencia sugiere que el framework necesita especialización analítica por caso o por dominio para activar operaciones profundas.

### Hipótesis 2: el refactor de la skill eliminó scaffolding analítico necesario

Evidencia a favor:

- En `4d6b8e3`, la skill pedía reunir volumen, conversiones, costes, campañas, creatividades, señales de calidad, segmentos y periodo.
- En versiones posteriores se refuerzan estados canónicos y límites, pero se reduce la lista operativa.
- RUNBOOK actual añade preguntas generales, no un repertorio operativo detallado.

Evidencia en contra:

- La skill actual aún menciona calidad, volumen, evolución, eficiencia, campañas y scoring como activadores.
- El runbook indica que Knowledge no debe repetir cifras.

Incertidumbre:

- No puede aislarse el efecto del refactor de la disponibilidad de evidencia y del prompt de ejecución.

Valoración:

Hipótesis fuerte, especialmente para AUC-001. El refactor parece haber mejorado gobernanza y reducido andamiaje de análisis concreto.

### Hipótesis 3: el prompt monolítico producía calidad por sobreprescripción difícil de generalizar

Evidencia a favor:

- El prompt histórico exige 23 secciones, análisis individual de variables, relaciones, creatividad, campaña, economía, temporalidad, plataforma, combinaciones, reglas y matriz.
- Mucho de su valor es dominio marketing y dataset-specific.
- Mezcla Evidence, Knowledge, Recommendations y Presentation en un único documento.

Evidencia en contra:

- Algunas operaciones son claramente generales: comparar, segmentar, evaluar concentración, robustez y eficiencia.
- La sobreprescripción no impide extraer patrones reutilizables.

Incertidumbre:

- Falta probar estos patrones en otro Analytical Use Case no marketing.

Valoración:

Hipótesis parcialmente cierta. El prompt era sobreprescriptivo, pero contenía operaciones analíticas reutilizables si se separan del dominio.

### Hipótesis 4: existe un pipeline reusable de razonamiento analítico no formalizado

Evidencia a favor:

- Se repiten composiciones como comparación + segmentación + robustez + implicación.
- SPEC-001 ya menciona patrones, comparaciones, anomalías, tendencias, oportunidades y riesgos.
- Los outputs históricos y actuales de prueba comparten operaciones aunque difieren en forma.

Evidencia en contra:

- La evidencia procede principalmente de AUC-001 y marketing.
- No hay demostración cross-domain.
- No existe todavía un contrato de “operación analítica” o “finding intermedio”.

Incertidumbre:

- Falta evidencia con casos no publicitarios y datasets distintos.

Valoración:

Hipótesis plausible, pero no demostrada como Foundation capability.

### Hipótesis 5: el problema es una combinación de factores

Evidencia a favor:

- Hay cambios de skill, cambios de workflow, diferencias de output, diferencias de evidencia y cambios de restricciones.
- El output actual canónico de handoff es más limitado que el output de prueba en Git, aunque ambos pertenecen al marco actual.
- El prompt histórico incluía dominio, método y presentación juntos.

Evidencia en contra:

- La comparación no está controlada experimentalmente con la misma evidencia, mismo prompt y solo una variable cambiada.

Incertidumbre:

- Falta un experimento A/B controlado con misma evidencia y diferentes scaffolds.

Valoración:

Hipótesis más probable.

### Hipótesis 6: la diferencia se debe parcialmente a cambios de evidencia, cobertura o contexto

Evidencia a favor:

- El handoff actual de junio usa 772 leads y 496,56 de spend; outputs históricos usan 342, 1.339 o 1.319 leads según corpus y Git.
- El modelo actual separa `matched`, `lead_only`, `spend_only` y restringe campaign/adset spend attribution.
- Algunas fuentes como impressions, clicks, CTR y creative metadata están ausentes.

Evidencia en contra:

- Incluso con evidencia limitada, podrían haberse generado más findings de trade-off dentro de los límites.
- El output de prueba en Git produjo más interpretación usando evidencia histórica hasta 2026-06-30.

Incertidumbre:

- No se ejecutaron nuevas consultas ni se reconstruyó una evidencia homogénea.

Valoración:

Factor relevante, pero no explicación completa.

## 17. Evaluación de reusabilidad

Hay evidencia suficiente para hablar de operaciones analíticas potencialmente reutilizables:

- comparación;
- segmentación;
- ranking;
- concentración;
- robustez;
- cobertura;
- tendencia;
- eficiencia;
- propagación de incertidumbre;
- traducción finding → implication.

No hay evidencia suficiente para elevarlas todavía a capacidad Foundation cerrada.

La parte reusable parece ser el patrón de operaciones, no las preguntas de marketing ni las métricas concretas. Para Foundation, la unidad candidata no debería ser “comparar campañas”, sino:

```text
Método: Comparative Analysis
Dominio: rendimiento de campañas
Dataset: campaign_name, spend, qualified_leads, cpql
```

## 18. Incertidumbres y evidencia pendiente

Incertidumbres:

- No se hizo una nueva ejecución controlada con la misma evidencia bajo prompt histórico y lifecycle actual.
- No se validó el patrón en otro dominio distinto de Meta Lead Quality.
- No se pudo separar completamente efecto skill, efecto prompt, efecto dataset y efecto Presentation.
- El corpus histórico mezcla informe final con reasoning, por lo que los pasos intermedios se reconstruyen inferencialmente.
- El output actual de handoff y el output de prueba en Git no son estrictamente equivalentes en alcance.

Evidencia pendiente:

- Experimento con Evidence Set fijo y tres condiciones: Knowledge actual sin scaffold, Knowledge con repertorio de operaciones, prompt histórico monolítico.
- Segundo AUC no marketing para probar si las operaciones se transfieren.
- Registro explícito de findings intermedios antes de Knowledge.
- Taxonomía experimental de métodos analíticos separada de dominio y dataset.
- Criterios de suficiencia para “Knowledge profundo” sin depender del formato de informe.

## 19. Conclusión experimental

La profundidad histórica no parece depender de un único factor. El prompt monolítico generaba profundidad porque combinaba:

- preguntas de negocio;
- métodos analíticos;
- conocimiento de dominio;
- estructura de informe;
- reglas de decisión;
- presión para interpretar cada tabla.

El lifecycle actual corrige una debilidad real: separa evidencia, conocimiento, recomendaciones y presentación, y mejora trazabilidad. Sin embargo, esa separación deja un hueco operativo: Knowledge Generation sabe qué no debe hacer, pero tiene menos instrucciones sobre qué operaciones analíticas debe aplicar para transformar evidencia en findings intermedios.

La observación principal es:

```text
La pérdida no es la separación Evidence → Knowledge en sí.
La pérdida es la falta de un scaffold explícito de operaciones analíticas entre Evidence y Knowledge.
```

Ese scaffold parece parcialmente reusable, pero todavía no está demostrado como capability de Foundation. En este momento debe tratarse como hipótesis experimental.

## 20. Siguiente experimento recomendado

Ejecutar un experimento controlado sin cambiar specifications:

1. Fijar un único Evidence Set de AUC-001.
2. Producir tres Knowledge Sets:
   - baseline con runbook actual;
   - Knowledge con repertorio experimental de operaciones analíticas;
   - reconstrucción monolítica estilo prompt histórico.
3. Exigir que los tres separen método, dominio y dataset.
4. Evaluar:
   - número y calidad de findings intermedios;
   - composiciones de operaciones;
   - trazabilidad;
   - utilidad para recomendaciones;
   - riesgo de inventar evidencia;
   - transferencia potencial a otro AUC.

El resultado debería decidir si conviene formalizar una capability reusable o si basta con especializar AUC-001 mediante skill/runbook.

