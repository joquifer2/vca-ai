# AUC-001 - Validación experimental de Analytical Narrative

## Metadata

| Campo | Valor |
|---|---|
| Evaluación | AUC-001 Analytical Narrative / Strategic Interpretation Validation |
| Fecha de ejecución | 2026-07-16 |
| Solicitud ejecutada | Genera el informe analítico de calidad de leads hasta el 30 de junio de 2026 |
| Agente responsable solicitado | Implementation Agent |
| Modo | Ejecución completa |
| Periodo resuelto | 2026-04-18 a 2026-06-30 |
| Fecha de corte | 2026-06-30 |
| Data Provider | BigQuery MCP Server only |
| Proyección | Analítica |
| Resultado | PASS WITH OBSERVATIONS |

---

## 1. Cambios realizados en artefactos operativos

En esta intervención se modificaron únicamente artefactos operativos propios de AUC-001 y se creó este documento de validación:

| Artefacto | Cambio | Justificación |
|---|---|---|
| `.github/skills/meta-lead-quality-analysis/SKILL.md` | Añadida sección `Analytical Narrative / Strategic Interpretation`. | Declara que AUC-001 debe producir una lectura integrada del fenómeno, no solo insights independientes, sin introducir arquitectura nueva. |
| `.github/skills/meta-lead-quality-analysis/RUNBOOK.md` | Ampliada Fase 09 para incluir `Knowledge Synthesis / Analytical Narrative` después de estabilizar el Knowledge Set y antes de Recommendation Generation. | Convierte la síntesis narrativa en operación explícita dentro de Knowledge Generation, con inputs, preguntas obligatorias, prohibiciones, output, gate y DoD. |
| `.github/skills/meta-lead-quality-analysis/CHECKLIST.md` | Añadidas comprobaciones específicas para validar Analytical Narrative. | Permite bloquear salidas que solo renombren una sección como “narrativa” sin construir una tesis integrada trazable. |

No se modificaron `references.md`, SPEC-010, SPEC-011, Presentation Policies, contratos globales, BigQuery, Dataform, Data Contract, Evidence Contract ni Analytical Contract de AUC-001.

`references.md` no se modificó porque no existe un perfil o artefacto externo nuevo que declarar como dependencia obligatoria. La operación queda definida dentro del Runbook y Checklist.

---

## 2. Context Definition estabilizado

| Campo | Valor |
|---|---|
| Objetivo | Analizar calidad de leads de Meta Ads hasta el 30 de junio de 2026 |
| Regla temporal | Fecha indicada tratada como cutoff; inicio resuelto desde cobertura del proveedor autorizado |
| Periodo final | 2026-04-18 a 2026-06-30 |
| Canal | Meta Ads / Meta Lead Ads |
| Criterio de calidad | Qualified Lead = `lead_tier IN ('A', 'B')` |
| Alcance | Leads, scoring FARO y spend autorizado por Data Contract/workspace |
| Data Provider | BigQuery MCP Server |
| Audiencia | Analítica / Marketing |
| Tipo de salida | Informe analítico trazable con validación experimental de narrativa |

---

## 3. Data Provider Validation y adquisición de evidencia

Tablas verificadas mediante MCP:

| Request ID | Recurso | Resultado |
|---|---|---|
| `auc-001-narrative-2026-06-30-schema-lead-001` | `datamart-vca-494114.marts.fct_lead_enriched` | success |
| `auc-001-narrative-2026-06-30-schema-spend-001` | `datamart-vca-494114.marts.fct_spend` | success |
| `auc-001-narrative-2026-06-30-schema-faro-001` | `datamart-vca-494114.intermediate.int_faro_lead_scoring` | success |

Cobertura temporal resuelta:

| Fuente | Request ID | Cobertura | Conteo |
|---|---|---|---:|
| `marts.fct_lead_enriched` | `auc-001-narrative-2026-06-30-coverage-leads-001` | 2026-04-18 a 2026-06-30 | 1.322 leads distintos |
| `intermediate.int_faro_lead_scoring` | `auc-001-narrative-2026-06-30-coverage-scoring-001` | 2026-04-18 a 2026-06-30 | 1.322 leads distintos |
| `marts.fct_spend` | `auc-001-narrative-2026-06-30-coverage-spend-001` | 2026-04-18 a 2026-06-30 | 7.332 registros / 1.406,23 inversión total |

Consulta rechazada y no utilizable:

| Request ID | Resultado | Tratamiento |
|---|---|---|
| `auc-001-narrative-2026-06-30-join-validation-001` | `ERR_SCOPE_DENIED` | No se usa como evidencia. CPQL emparejado queda como UNKNOWN. |

---

## 4. Evidence Set estabilizado

### EVD-001 - Distribución de calidad

| Lead tier | Leads | Cualificados A/B |
|---|---:|---:|
| A | 57 | 57 |
| B | 338 | 338 |
| C | 553 | 0 |
| D | 374 | 0 |
| Total | 1.322 | 395 |

Tasa global A/B: 29,88%.

### EVD-002 - Evolución mensual

| Mes | Leads | A/B | Tasa A/B |
|---|---:|---:|---:|
| Abril parcial | 179 | 54 | 30,17% |
| Mayo | 369 | 112 | 30,35% |
| Junio | 774 | 229 | 29,59% |

### EVD-003 - Formularios / proxy de audiencia

| Formulario | Leads | A/B | Tasa A/B |
|---|---:|---:|---:|
| Isla | 1.180 | 342 | 28,98% |
| Diáspora | 142 | 53 | 37,32% |

### EVD-004 - Campaña/adset del lado lead

| Campaña / adset | Leads | A/B | Tasa A/B |
|---|---:|---:|---:|
| Captación Isla | 1.180 | 342 | 28,98% |
| RTG Diáspora | 141 | 53 | 37,59% |
| RTG Diáspora copia | 1 | 0 | 0,00% |

### EVD-005 - Principales anuncios por A/B

| Referencia | Leads | A/B | Tasa A/B |
|---|---:|---:|---:|
| `ViajeSinEstres_AlivioEmocional_ViajeSinEstres_Reel_v1` | 642 | 187 | 29,13% |
| `ViajaComoInvitado_Identidad_ViajarComoLocal_Reel_v1` | 358 | 102 | 28,49% |
| `FiltroBilletes_EscasezReal_3TipsDeViaje_Reel_v1` | 118 | 42 | 35,59% |
| `FiltroBilletes_AutoSegmentacion_PrimeraVez_Reel_v1` | 53 | 19 | 35,85% |

### EVD-006 - Spend por señal

| Señal | Inversión | Anuncios con spend |
|---|---:|---:|
| COMMERCIAL | 875,83 | 10 |
| ATTENTION | 308,54 | 7 |
| ACTIVATION | 221,86 | 6 |

### EVD-007 - Scoring FARO

| Estado | Tier | Leads | Score medio |
|---|---|---:|---:|
| en_proceso | B | 179 | 67,19 |
| tiene_billetes | B | 111 | 71,09 |
| solo_mirando | B | 48 | 63,71 |
| tiene_billetes | A | 46 | 88,11 |
| en_proceso | A | 11 | 82,91 |
| solo_mirando | C | 410 | 48,23 |
| solo_mirando | D | 374 | 29,21 |

Limitación material: el Evidence Set no contiene CPQL emparejado a nivel anuncio/campaña porque la consulta de join fue rechazada por el MCP.

---

## 5. Analytical Investigation Record

| Finding | Soporte | Lectura | Incertidumbre |
|---|---|---|---|
| FND-001 | EVD-001, EVD-002 | La calidad agregada permanece estable mientras junio escala volumen. | La lectura semanal fina no es el foco de esta validación y la última semana es parcial. |
| FND-002 | EVD-005 | Dos anuncios explican la mayor parte del volumen cualificado: 289 de 395 A/B. | Concentración no equivale a causalidad creativa. |
| FND-003 | EVD-003, EVD-004 | RTG/diáspora muestra mayor tasa A/B con menor volumen. | No está demostrado que escale sin diluir calidad. |
| FND-004 | EVD-007 | FARO discrimina intención de forma coherente: A/B tiene mayor score y señales más fuertes que C/D. | No sustituye validación comercial posterior en CRM. |
| FND-005 | EVD-006, consulta join rechazada | La inversión comercial existe y está concentrada, pero no se puede cerrar eficiencia coste-calidad emparejada. | CPQL por anuncio/campaña queda UNKNOWN. |

Hallazgos estructurales: FND-001, FND-002, FND-004 y FND-005.

Hallazgo secundario o de oportunidad: FND-003, por su menor base de volumen y necesidad de validación de escala.

---

## 6. Knowledge Set estabilizado

### Insights

INS-001 - Meta Lead Ads está produciendo una señal de calidad real y estable, no solo volumen: 395 de 1.322 leads fueron A/B y junio escaló volumen sin degradación agregada material.

INS-002 - El aprendizaje útil está concentrado en pocas referencias. Dos anuncios generan el 73,16% de los leads A/B, por lo que gran parte de la lectura del sistema depende de esos activos.

INS-003 - RTG/diáspora muestra una tasa A/B superior a Isla/captación, pero con una base mucho menor; es una señal prometedora, no una prueba de escalabilidad.

INS-004 - FARO funciona como lenguaje operativo de calidad: el scoring separa intención alta y baja mejor que el volumen agregado.

INS-005 - La principal limitación para decidir inversión no es ausencia de calidad, sino falta de atribución económica emparejada autorizada por MCP.

### Hipótesis

HYP-001 - Las referencias `FiltroBilletes` pueden actuar como filtro de calidad, aunque todavía no desplazan a los anuncios dominantes en volumen cualificado.

HYP-002 - RTG/diáspora puede ser una vía de crecimiento de calidad si conserva su tasa A/B al aumentar volumen.

HYP-003 - La inversión comercial parece alinearse por nombre con las referencias que generan más aprendizaje, pero esa alineación no puede convertirse en eficiencia CPQL sin join autorizado.

### Conclusiones

CON-001 - El sistema ya genera una base cualificada suficiente para análisis: 395 leads A/B.

CON-002 - La calidad agregada se sostiene al escalar junio.

CON-003 - El fenómeno dominante es una combinación de calidad estable y aprendizaje concentrado.

CON-004 - La evidencia permite orientar aprendizaje y calidad, pero no decisiones definitivas de eficiencia económica por anuncio/campaña.

### Prioridades analíticas

PRI-001 - Entender la dependencia de los dos activos principales.

PRI-002 - Separar crecimiento de volumen de crecimiento de aprendizaje cualificado.

PRI-003 - Mantener visible la limitación CPQL antes de cualquier lectura económica fuerte.

PRI-004 - Leer RTG/diáspora y `FiltroBilletes` como oportunidades de validación, no como conclusiones cerradas.

### Riesgos e incertidumbres

RSK-001 - Sobreinterpretar la concentración como superioridad creativa causal.

RSK-002 - Convertir señales de menor volumen en decisiones de escala prematuras.

RSK-003 - Presentar eficiencia económica sin CPQL emparejado.

UNKNOWN-001 - CPQL por anuncio/campaña.

UNKNOWN-002 - Evolución post-lead en CRM y ventas.

UNKNOWN-003 - Clics, impresiones y CTR.

---

## 7. Analytical Narrative estabilizada

La captación de Meta Lead Ads ya no puede describirse como simple compra de volumen barato: la evidencia estabilizada muestra una señal real de calidad, con 395 leads A/B sobre 1.322 y una tasa agregada que se mantiene en torno al 30% incluso cuando junio concentra el mayor crecimiento. El fenómeno principal es, por tanto, una captación que escala sin perder calidad agregada, pero cuyo aprendizaje útil no está distribuido de forma amplia.

Esa estabilidad depende de una estructura concentrada. Dos referencias de anuncio explican la mayor parte del volumen cualificado, mientras FARO aporta el lenguaje que permite distinguir intención real de volumen exploratorio. En conjunto, el sistema tiene capacidad para reconocer calidad, pero todavía aprende desde pocos activos dominantes y desde señales del lado lead.

El trade-off central es escala frente a robustez del aprendizaje. Aumentar volumen parece posible sin deterioro agregado inmediato, pero hacerlo desde pocas referencias y sin atribución económica emparejada aumenta el riesgo de confundir concentración con eficiencia. RTG/diáspora y `FiltroBilletes` aparecen como señales de calidad potencial, aunque siguen siendo secundarios frente al peso estructural de los activos dominantes.

La limitación que más condiciona la lectura es la falta de CPQL emparejado autorizado por MCP. Sin ese enlace, el análisis puede explicar dónde aparece la calidad y dónde se concentra la inversión, pero no puede cerrar qué unidad compra calidad con mayor eficiencia económica.

La implicación estratégica es que el sistema ha superado la fase de demostrar que existe calidad en Meta Lead Ads, pero aún no ha completado la fase de demostrar cómo escalar esa calidad con precisión económica. Si el lector recordara una sola idea, debería ser esta: Meta ya genera calidad estable, pero el reto decisivo es ampliar el aprendizaje sin depender de pocos activos y sin tomar decisiones económicas antes de resolver la atribución coste-calidad.

Trazabilidad: INS-001, INS-002, INS-004, INS-005, HYP-001, HYP-002, CON-003, CON-004, PRI-001, PRI-003, RSK-001, RSK-003, UNKNOWN-001.

---

## 8. Recommendation Set

| ID | Prioridad | Recomendación | Derivación |
|---|---|---|---|
| REC-001 | P1 | Mantener la optimización analítica centrada en A/B, no en leads totales. | INS-001, CON-001 |
| REC-002 | P1 | Tratar las dos referencias dominantes como activos principales de aprendizaje y vigilancia. | INS-002, PRI-001 |
| REC-003 | P1 | No usar CPQL por anuncio/campaña como métrica definitiva hasta disponer de modelado emparejado autorizado. | INS-005, RSK-003, UNKNOWN-001 |
| REC-004 | P2 | Validar RTG/diáspora con incrementos controlados antes de considerarlo línea de escala. | INS-003, HYP-002 |
| REC-005 | P2 | Evaluar `FiltroBilletes` como hipótesis de filtro de calidad con umbrales mínimos de volumen. | HYP-001, PRI-004 |
| REC-006 | P2 | Preservar las limitaciones de creatividad y atribución económica en toda salida ejecutiva. | RSK-001, RSK-003 |

Las recomendaciones derivan del Knowledge Set. La Analytical Narrative no introduce acciones nuevas; solo integra la explicación.

---

## 9. Nuevo informe analítico con Analytical Narrative

### Lectura integrada

Meta Lead Ads está generando una señal de calidad consistente: casi tres de cada diez leads alcanzan Tier A/B y junio escala el volumen sin romper esa proporción. La lectura ya no es “hay volumen barato” ni “hay calidad aislada”, sino que existe una base cualificada real sobre la que el sistema puede aprender.

La tensión está en cómo se distribuye ese aprendizaje. La mayor parte de los leads cualificados procede de dos referencias de anuncio, mientras FARO permite separar intención real de volumen exploratorio. Esto hace que el sistema sea útil para leer calidad, pero todavía vulnerable a depender demasiado de pocos activos.

RTG/diáspora y `FiltroBilletes` aportan señales secundarias relevantes: muestran potencial para mejorar la calidad relativa, pero aún necesitan validación de escala. No conviene leerlos como ganadores cerrados; sí como caminos de aprendizaje que pueden reducir la dependencia de los activos dominantes si mantienen calidad al crecer.

El límite dominante es económico: la ejecución no puede afirmar CPQL emparejado por anuncio o campaña porque el MCP rechazó el join spend-lead. Por eso, el informe permite decidir qué aprender y qué proteger, pero no permite cerrar con precisión qué anuncio compra calidad al menor coste.

### Datos principales

| Métrica | Valor |
|---|---:|
| Leads distintos | 1.322 |
| Leads A/B | 395 |
| Tasa A/B | 29,88% |
| Leads en junio | 774 |
| A/B en junio | 229 |
| Tasa A/B junio | 29,59% |
| Inversión total observada | 1.406,23 |
| Inversión comercial | 875,83 |

### Implicación para Marketing

El mensaje central para Marketing es que Meta ya está entregando calidad suficiente para aprender, pero todavía no la distribuye de forma robusta ni permite medir eficiencia económica completa. La siguiente lectura de gestión debe separar tres planos: mantener la señal A/B como brújula de calidad, vigilar la dependencia de los dos activos dominantes y no convertir inversión en eficiencia hasta que exista CPQL emparejado autorizado.

### Recomendaciones presentables

1. Mantener A/B como KPI principal de calidad.
2. Proteger y estudiar las dos referencias dominantes antes de reasignar inversión de forma agresiva.
3. Validar RTG/diáspora y `FiltroBilletes` como líneas de aprendizaje, no como escalados automáticos.
4. Bloquear conclusiones de CPQL por anuncio/campaña hasta resolver la atribución spend-lead.

### Limitaciones visibles

- No hay CPQL emparejado por anuncio/campaña.
- No hay lectura de ventas, CRM o ingresos posteriores.
- No hay metadata de asset creativo.
- No hay clics, impresiones ni CTR.
- La evidencia de RTG/diáspora tiene menor volumen que la línea Isla/captación.

---

## 10. Comparación obligatoria

### Fuentes comparadas

| Fuente | Uso permitido en esta evaluación |
|---|---|
| `docs/corpus/auc-001/informe_calidad_leads_scoring_20260701.md` | Comparación histórica; no usado como fuente analítica de la nueva ejecución |
| `docs/handoffs/auc-001-analytical-report-2026-06-30.md` | Último informe analítico previo; no usado para construir evidencia, Knowledge ni Recommendations |
| Nueva ejecución con Analytical Narrative | Base de validación experimental actual |

### Matriz comparativa

| Criterio | Histórico 20260701 | Informe previo | Nueva ejecución con Analytical Narrative |
|---|---|---|---|
| Tesis central | Alta, pero mezclada con recomendaciones operativas y CPQL histórico. | Parcial: tiene lectura ejecutiva, pero los insights quedan relativamente separados. | Alta: tesis explícita sobre calidad estable, aprendizaje concentrado y límite económico. |
| Integración entre findings | Alta en narrativa, menor en separación metodológica. | Media: conecta algunos patrones, pero no declara una síntesis canónica. | Alta: conecta volumen, concentración, scoring, RTG y limitación CPQL. |
| Jerarquía de hallazgos | Existe, pero mezcla hallazgos, acciones y próximos pasos. | Media: prioridades aparecen, pero sin separar estructural/secundario. | Alta: diferencia estructurales y secundarios antes de narrar. |
| Fenómeno principal | Optimización de Meta desde volumen hacia calidad. | Calidad estable con limitación de eficiencia. | Captación con calidad estable, aprendizaje concentrado y medición económica incompleta. |
| Trade-off | Calidad vs volumen y Lead vs QualifiedLead. | Calidad vs eficiencia atribuible. | Escala vs robustez del aprendizaje / calidad vs precisión económica. |
| Implicación estratégica | Clara, pero dependiente de datos operativos históricos no vigentes. | Útil, aunque más dispersa. | Clara y memorable: ya hay calidad, falta ampliar aprendizaje y cerrar atribución coste-calidad. |
| Mensaje recordable | Fuerte. | Moderado. | Fuerte. |
| Trazabilidad | Menor bajo SDD actual; usa cruces y supuestos históricos. | Alta. | Alta, con trazabilidad explícita a Knowledge items. |
| Riesgo de sobreinterpretación | Alto en CPQL y acciones por creatividad bajo criterios históricos. | Bajo-medio. | Bajo: CPQL queda UNKNOWN y RTG/FiltroBilletes quedan como hipótesis. |
| Redundancia | Alta por extensión y múltiples secciones operativas. | Media. | Menor: la narrativa comprime la explicación. |
| Utilidad para Director de Marketing | Alta, pero más operativa y menos controlada metodológicamente. | Media-alta. | Alta: explica qué ocurre, por qué importa, tensión dominante y límite principal. |

### Evaluación cualitativa

El informe histórico es más rico en lectura de negocio y tiene una narrativa fuerte, pero no respeta las restricciones actuales de AUC-001: incluye CPQL emparejado, High Quality Lead, eventos CAPI y recomendaciones operativas que esta ejecución no puede reproducir sin evidencia autorizada equivalente.

El informe previo cumple trazabilidad y evita sobreinterpretación, pero se lee más como una suma de Evidence, Findings, Knowledge y Recommendations. Tiene una lectura ejecutiva aceptable, aunque no contiene una tesis canónica explícita que explique cómo se relacionan los hallazgos.

La nueva ejecución conserva la seguridad metodológica del informe previo y recupera parte de la fuerza sintética del histórico sin copiarlo ni reabrir evidencia. La mejora no está en longitud ni en número de secciones, sino en que el lector puede recordar una explicación integrada: Meta ya genera calidad estable, pero el aprendizaje está concentrado y la precisión económica sigue limitada por la falta de atribución spend-lead.

---

## 11. Checklist de Analytical Narrative

| Criterio | Resultado | Evidencia |
|---|---|---|
| Deriva exclusivamente del Knowledge Set | Pass | Trazabilidad a INS/HYP/CON/PRI/RSK/UNKNOWN |
| No introduce recomendaciones encubiertas | Pass | Las acciones aparecen solo en Recommendation Set |
| No reabre Evidence Generation | Pass | La narrativa se construye después de Evidence y Knowledge |
| Mejora síntesis sin degradar trazabilidad | Pass | Incluye trazabilidad explícita |
| Deja de parecer colección de insights | Pass | Construye tesis con fenómeno, factores, trade-off, límite e implicación |
| Comunica explicación integrada | Pass | Relaciona calidad estable, concentración, scoring y CPQL UNKNOWN |
| Útil para Director de Marketing | Pass with observations | Alto valor ejecutivo, pero limitado por CPQL y CRM UNKNOWN |

---

## 12. Limitaciones pendientes

- El MCP sigue rechazando joins spend-lead; CPQL emparejado queda fuera de esta ejecución.
- No hay outcomes CRM, ventas ni ingresos posteriores.
- No hay metadata de asset creativo.
- No hay clicks, impresiones ni CTR.
- La implementación es experimental y no modifica specs ni contratos globales.
- La Analytical Narrative queda definida en artefactos operativos AUC-001, pendiente de observarse en más ejecuciones antes de promoverla a capability reusable.

---

## 13. Evaluación sobre nivel de consultor senior

Resultado: PASS WITH OBSERVATIONS.

La nueva salida alcanza un nivel más cercano al de consultor senior porque no solo enumera métricas o insights, sino que explica el fenómeno dominante y sus condiciones de decisión: calidad estable, dependencia de pocos activos, FARO como sistema de lectura y limitación económica por falta de atribución emparejada.

La mejora principal es la memorabilidad estratégica. Un Director de Marketing puede identificar con claridad:

- qué ocurre: Meta genera calidad estable mientras escala volumen;
- por qué importa: ya existe base A/B suficiente para aprendizaje;
- qué tensión condiciona el rendimiento: escalar sin depender de pocos activos;
- cuál es el límite principal: ausencia de CPQL emparejado autorizado;
- qué debe recordar: hay calidad, pero el reto es ampliar aprendizaje y cerrar atribución coste-calidad antes de decisiones económicas fuertes.

La observación residual es que el informe todavía no puede alcanzar una lectura completa de eficiencia de inversión al nivel del histórico porque el Data Provider actual no autoriza el cruce spend-lead. Esa limitación es metodológicamente correcta y debe permanecer visible.

---

## 14. Resultado final

La implementación experimental de Analytical Narrative se considera completada para AUC-001.

Definition of Done:

1. La Analytical Narrative deriva exclusivamente del Knowledge Set: PASS.
2. No introduce recomendaciones encubiertas: PASS.
3. No reabre Evidence Generation: PASS.
4. Mejora la síntesis sin degradar trazabilidad: PASS.
5. El informe deja de parecer una colección de insights independientes: PASS.
6. El informe comunica una explicación integrada del fenómeno: PASS.
7. Un Director de Marketing puede identificar qué ocurre, por qué importa, qué tensión condiciona el rendimiento, cuál es el principal límite y qué debe recordar: PASS.
