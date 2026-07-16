# AUC-001 Informe analítico - Calidad de leads hasta 2026-06-30

## Contexto de ejecución

| Campo | Valor |
|---|---|
| Solicitud | Genera el informe analítico de calidad de leads hasta el 30 de junio de 2026 |
| Modo | Ejecución completa |
| Fecha de corte | 2026-06-30 |
| Periodo resuelto | 2026-04-18 a 2026-06-30 |
| Regla temporal aplicada | El usuario indicó una fecha de corte sin fecha inicial; la fecha inicial se resolvió desde la primera cobertura disponible en el proveedor autorizado |
| Canal | Meta Ads / Meta Lead Ads |
| Regla de calidad del lead | Qualified Lead = `lead_tier` A o B |
| Data Provider | Exclusivamente BigQuery MCP Server |
| Workspace | vca |
| Proyecto autorizado | datamart-vca-494114 |
| Proyección de salida | Analítica |

Contexto oficial utilizado: `analytical_use_cases/meta_lead_quality_analysis.md`, `docs/context_refs.md`, `project_brief.md`, `knowledge/client/ccd.md`, `docs/contracts/context.contract.md`, `docs/contracts/data.contract.md`, `docs/handoffs/auc-001-data-contract.md`, `docs/contracts/evidence.contract.md`, `docs/contracts/knowledge.contract.md`, `docs/contracts/recommendation.contract.md`, `docs/contracts/presentation.contract.md`, `specs/spec-010-presentation-projection-selection.md`, `specs/spec-011-communication-context-representation-transformation.md`.

## Validación del Data Provider

Tablas autorizadas verificadas mediante descubrimiento de metadatos MCP:

| Dataset | Tabla | Estado |
|---|---|---|
| `marts` | `fct_lead_enriched` | Verificada |
| `marts` | `fct_spend` | Verificada |
| `marts` | `dim_campaign_signal` | Verificada |
| `intermediate` | `int_faro_lead_scoring` | Verificada |

Cobertura resuelta mediante consultas MCP exitosas:

| Fuente | Fecha mínima | Fecha máxima | Conteo |
|---|---:|---:|---:|
| `marts.fct_lead_enriched` | 2026-04-18 | 2026-06-30 | 1.322 registros de lead / 1.322 leads distintos |
| `intermediate.int_faro_lead_scoring` | 2026-04-18 | 2026-06-30 | 1.322 registros con scoring / 1.322 leads distintos |
| `marts.fct_spend` | 2026-04-18 | 2026-06-30 | 7.332 registros de inversión / 1.406,23 de inversión total |

Consultas rechazadas y no utilizables:

| Request ID | Motivo | Tratamiento |
|---|---|---|
| `auc-001-2026-06-30-evidence-coverage-001` | `ERR_SCOPE_DENIED` en consulta de modelo preparado multi-tabla | Excluida de la evidencia |
| `auc-001-2026-06-30-join-validation-001` | `ERR_SCOPE_DENIED` en join entre `fct_lead_enriched` y `fct_spend` | Excluida de la evidencia |

Limitación material: el MCP aceptó adquisición de evidencia sobre tablas individuales, pero rechazó joins entre tablas autorizadas. Por tanto, esta ejecución soporta lecturas de calidad de lead, scoring, inversión por señal y concentración de inversión, pero no soporta un modelo plenamente emparejado de coste por lead cualificado a nivel anuncio o campaña.

## Evidence Set

### EVD-001 - Distribución de calidad de leads

| Lead tier | Leads | Cualificados A/B |
|---|---:|---:|
| A | 57 | 57 |
| B | 338 | 338 |
| C | 553 | 0 |
| D | 374 | 0 |
| Total | 1.322 | 395 |

Tasa global de cualificados A/B: 29,88%.

### EVD-002 - Calidad mensual de leads

| Mes | Leads | Cualificados A/B | Tier A | Tier B | Tier C | Tasa A/B |
|---|---:|---:|---:|---:|---:|---:|
| 2026-04 parcial | 179 | 54 | 7 | 47 | 80 | 30,17% |
| 2026-05 | 369 | 112 | 19 | 93 | 135 | 30,35% |
| 2026-06 | 774 | 229 | 31 | 198 | 338 | 29,59% |

### EVD-003 - Patrón semanal de calidad

| Semana iniciada | Leads | Cualificados A/B | Tasa A/B |
|---|---:|---:|---:|
| 2026-04-13 | 34 | 9 | 26,47% |
| 2026-04-20 | 138 | 41 | 29,71% |
| 2026-04-27 | 7 | 4 | 57,14% |
| 2026-05-04 | 180 | 58 | 32,22% |
| 2026-05-11 | 182 | 54 | 29,67% |
| 2026-05-18 | 7 | 0 | 0,00% |
| 2026-06-01 | 213 | 53 | 24,88% |
| 2026-06-08 | 182 | 57 | 31,32% |
| 2026-06-15 | 194 | 75 | 38,66% |
| 2026-06-22 | 153 | 41 | 26,80% |
| 2026-06-29 | 32 | 3 | 9,38% |

### EVD-004 - Calidad por plataforma

| Plataforma | Orgánico | Leads | Cualificados A/B | Tasa A/B |
|---|---|---:|---:|---:|
| Facebook | false | 893 | 279 | 31,24% |
| Instagram | false | 429 | 116 | 27,04% |

### EVD-005 - Formulario y proxy de audiencia

| Formulario | Leads | Cualificados A/B | Tasa A/B |
|---|---:|---:|---:|
| `[META]-[CAPTACION]-[NATIVE FORM]-[ISLA]` | 1.180 | 342 | 28,98% |
| `[META]-[CAPTACION]-[NATIVE FORM]-[DIASPORA]` | 142 | 53 | 37,32% |

### EVD-006 - Calidad por campaña y conjunto de anuncios

| Campaña | Conjunto | Leads | Cualificados A/B | Tasa A/B |
|---|---|---:|---:|---:|
| `[META]_[CLP]_[CAPTACION]_[ABO]` | `[PR]_[NATIVE FORM]_[AVG+]_[ISLA]` | 1.180 | 342 | 28,98% |
| `[META]_[CLP]_[RTG]_[CBO]` | `[RTG]_[NATIVE FORM]_[INTERACCIONES + 50% VIDEO]_[DIASPORA]` | 141 | 53 | 37,59% |
| `[META]_[CLP]_[RTG]_[CBO]` | `[RTG]_[NATIVE FORM]_[INTERACCIONES + 50% VIDEO]_[DIASPORA] - Copia` | 1 | 0 | 0,00% |

Los valores de campaña y conjunto proceden únicamente de metadata del lado lead en esta ejecución.

### EVD-007 - Principales anuncios por cualificados A/B

| Referencia de anuncio | Leads | Cualificados A/B | Tasa A/B |
|---|---:|---:|---:|
| ViajeSinEstres_AlivioEmocional_ViajeSinEstres_Reel_v1 | 642 | 187 | 29,13% |
| ViajaComoInvitado_Identidad_ViajarComoLocal_Reel_v1 | 358 | 102 | 28,49% |
| FiltroBilletes_EscasezReal_3TipsDeViaje_Reel_v1 | 118 | 42 | 35,59% |
| FiltroBilletes_AutoSegmentacion_PrimeraVez_Reel_v1 | 53 | 19 | 35,85% |
| FiltroBilletes_EscasezReal_3TipsDeViaje_Reel_v1 | 19 | 10 | 52,63% |
| MasCaroPorqueMejor_CalidadVsCantidad_ViajesConCalidad_Reel_v1 | 18 | 9 | 50,00% |
| ExperienciasUnicas_ViajesConAlma_BoriWine2026_Reel_v1 | 67 | 8 | 11,94% |
| ViajaComoInvitado_Estatus_ExperienciaCalidad_Reel_v1 | 20 | 8 | 40,00% |
| ViajeSinEstres_PrevencionDeRiesgo_ErroresViaje_Reel_v1 | 16 | 6 | 37,50% |

### EVD-008 - Inversión por señal de campaña

| Señal de campaña | Registros de inversión | Inversión | Anuncios con inversión distintos |
|---|---:|---:|---:|
| COMMERCIAL | 7.099 | 875,83 | 10 |
| ATTENTION | 141 | 308,54 | 7 |
| ACTIVATION | 92 | 221,86 | 6 |

La inversión comercial representó el 62,29% de la inversión total observada en el periodo.

### EVD-009 - Inversión mensual por señal

| Mes | Señal | Inversión |
|---|---|---:|
| 2026-04 parcial | ATTENTION | 62,90 |
| 2026-04 parcial | COMMERCIAL | 146,29 |
| 2026-05 | ACTIVATION | 68,06 |
| 2026-05 | ATTENTION | 88,94 |
| 2026-05 | COMMERCIAL | 232,98 |
| 2026-06 | ACTIVATION | 153,80 |
| 2026-06 | ATTENTION | 156,70 |
| 2026-06 | COMMERCIAL | 496,56 |

### EVD-010 - Principales anuncios por inversión

| Referencia de anuncio | Señal | Inversión |
|---|---|---:|
| ViajeSinEstres_AlivioEmocional_ViajeSinEstres_Reel_v1 | COMMERCIAL | 468,06 |
| MadridNoGoogle_MiedoAPerdida_OrganizacionViaje_Reel_v1 | ATTENTION | 279,69 |
| ViajaComoInvitado_Identidad_ViajarComoLocal_Reel_v1 | COMMERCIAL | 245,84 |
| FiltroBilletes_EscasezReal_3TipsDeViaje_Reel_v1 | ACTIVATION | 155,64 |
| ExperienciasUnicas_ViajesConAlma_BoriWine2026_Reel_v1 | COMMERCIAL | 50,01 |
| FiltroBilletes_AutoSegmentacion_PrimeraVez_Reel_v1 | COMMERCIAL | 48,96 |

### EVD-011 - Señales de scoring

| Estado de billetes | Tiene billetes | Lead tier | Leads | Score inicial medio |
|---|---|---|---:|---:|
| en_proceso | false | B | 179 | 67,19 |
| tiene_billetes | true | B | 111 | 71,09 |
| solo_mirando | false | B | 48 | 63,71 |
| tiene_billetes | true | A | 46 | 88,11 |
| en_proceso | false | A | 11 | 82,91 |
| solo_mirando | false | C | 410 | 48,23 |
| solo_mirando | false | D | 374 | 29,21 |
| en_proceso | false | C | 123 | 49,81 |
| tiene_billetes | true | C | 20 | 55,25 |

Los 1.322 leads tenían marcados como `true` los cinco flags de mapeo de scoring/formulario.

## Analytical Investigation Record

| Finding | Soporte | Importancia | Incertidumbre |
|---|---|---|---|
| FND-001: La calidad se mantiene estable a nivel agregado pese al crecimiento de volumen | EVD-001, EVD-002 | Junio produjo el 58,55% de los leads y el 57,97% de los cualificados A/B, manteniendo una tasa A/B cercana a abril y mayo | La semana final de junio cae con fuerza, pero es una semana parcial |
| FND-002: La mayor parte del volumen cualificado se concentra en dos referencias de anuncio de alto volumen | EVD-007 | Los dos principales anuncios generaron 289 de 395 leads A/B, el 73,16% del total A/B | La concentración no demuestra causalidad creativa |
| FND-003: Diáspora/RTG tiene menor volumen, pero una tasa A/B materialmente superior a Isla/captación | EVD-005, EVD-006 | Diáspora/formulario y adset alcanzan alrededor de 37,3%-37,6% A/B frente a 29,0% de Isla/captación | La muestra RTG es mucho menor; el riesgo de escala permanece |
| FND-004: Facebook concentra la mayor parte del volumen y una calidad observada algo superior a Instagram | EVD-004 | Facebook produjo el 67,55% de leads y el 70,63% de A/B | La atribución por plataforma es del lado lead; no se validó eficiencia de inversión por plataforma |
| FND-005: La inversión comercial se concentra en referencias nombradas que también concentran volumen de leads, pero la eficiencia emparejada no está validada | EVD-008, EVD-010, consultas join rechazadas | La inversión comercial es el 62,29% de la inversión y las principales referencias comerciales por spend coinciden por nombre con grandes generadores de leads | Los joins fueron rechazados; no hay conclusión CPQL autorizada a nivel anuncio |
| FND-006: El scoring FARO separa de forma coherente las señales de intención | EVD-011 | Los leads A/B tienen scores medios materialmente superiores a C/D, y `tiene_billetes` aparece en grupos A/B de mayor score | Esto valida coherencia del scoring, no conversión comercial posterior |

Observaciones descartadas o limitadas: referencias de anuncio con una sola fila o muy bajo volumen y tasas A/B extremas no se elevaron a conclusiones; referencias `ATTENTION`/`ACTIVATION` solo con spend no se trataron como evidencia de eficiencia comercial de leads; CTR, clics, impresiones, conversión CRM y resultados de ventas no están disponibles en la evidencia autorizada.

## Knowledge Set

### Insights

INS-001 - El sistema está comprando volumen y señal de calidad, no solo ruido. Sobre 1.322 leads, 395 fueron A/B cualificados, con una tasa A/B del 29,88%. Junio escaló materialmente hasta 774 leads sin una caída agregada relevante de calidad.

INS-002 - La calidad está concentrada. Las dos referencias dominantes, `ViajeSinEstres_AlivioEmocional` y `ViajaComoInvitado_Identidad`, explican la mayor parte del volumen A/B. Deben tratarse como la base principal de aprendizaje del sistema actual.

INS-003 - Retargeting/diáspora se comporta como un segmento de mayor calidad y menor volumen. Su tasa A/B está materialmente por encima del formulario Isla/captación, pero su menor base obliga a leerlo como prometedor, no como plenamente probado a escala.

INS-004 - La variable explicativa más fuerte en la evidencia disponible no es la inversión bruta ni el CPL; es el scoring FARO combinado con segmentación del lado lead. El estado de billetes y el lead tier separan leads útiles de volumen de baja intención con más claridad que el conteo agregado.

INS-005 - La eficiencia coste-calidad solo es parcialmente observable en esta ejecución. La inversión comercial está disponible y concentrada, pero el MCP rechazó los joins necesarios para estabilizar CPQL emparejado por anuncio o campaña.

### Hipótesis

HYP-001 - La familia de mensajes `FiltroBilletes` puede funcionar como filtro de calidad y no solo como generador de volumen. Muestra tasas A/B superiores en varias referencias, pero su volumen cualificado es menor que el de los dos anuncios dominantes.

HYP-002 - Diáspora/RTG puede ser una vía valiosa de expansión de calidad si consigue escalar sin diluir la tasa A/B. La evidencia actual respalda potencial de calidad, no escalabilidad final.

HYP-003 - La inversión comercial parece alinearse direccionalmente, por nombre, con los principales anuncios de volumen y calidad, pero sigue siendo una observación cautelosa hasta que exista modelado spend-lead emparejado autorizado por MCP.

### Conclusiones

CON-001 - Hasta 2026-06-30, Meta Lead Ads produjo una base cualificada relevante: 395 leads A/B sobre 1.322 leads totales.

CON-002 - Junio fue el mes principal de volumen y no degradó materialmente la tasa A/B agregada frente a abril/mayo.

CON-003 - Las unidades de decisión más sólidas en esta ejecución son referencias de anuncio y segmentos formulario/adset del lado lead, no unidades completas de eficiencia coste-calidad emparejada.

CON-004 - La evidencia es suficiente para orientar optimización basada en calidad, pero insuficiente para decisiones definitivas de eficiencia de inversión por anuncio o campaña.

### Prioridades de atención

PRI-001 - Proteger y entender las dos referencias dominantes de volumen cualificado antes de reasignar presupuesto de forma agresiva.

PRI-002 - Investigar el segmento RTG/diáspora de mayor calidad como oportunidad de escala controlada.

PRI-003 - Mejorar o autorizar el modelado emparejado spend-lead para convertir CPQL en una métrica fiable de optimización.

PRI-004 - Tratar anuncios de poco volumen y alta tasa como señales exploratorias, no como ganadores inmediatos.

### Riesgos y UNKNOWNs

RSK-001 - Presentar coste por lead cualificado por anuncio o campaña sería engañoso en esta ejecución porque los joins fueron rechazados por el MCP.

RSK-002 - Las conclusiones creativas se limitan a referencia/nombre de anuncio; no existe metadata de asset creativo.

RSK-003 - Progresión CRM, conversión a venta e ingresos posteriores no están disponibles; la calidad de lead es calidad según scoring FARO, no calidad de venta cerrada.

RSK-004 - La semana iniciada el 2026-06-29 es parcial y no debe interpretarse como deterioro semanal completo.

UNKNOWN-001 - CPQL emparejado a nivel anuncio.

UNKNOWN-002 - Atribución de inversión por campaña/adset frente a calidad de leads.

UNKNOWN-003 - Clics, impresiones, CTR y eficiencia pre-lead del embudo.

UNKNOWN-004 - Resultado comercial posterior al lead.

## Recommendation Set

| ID | Prioridad | Recomendación | Soporte | Impacto esperado | Validación |
|---|---|---|---|---|---|
| REC-001 | P1 | Mantener la optimización centrada en volumen de leads A/B cualificados, no en volumen total de leads. | INS-001, INS-004, CON-001 | Mayor protección frente al crecimiento de leads baratos y de baja calidad | Monitorizar semanalmente volumen A/B y tasa A/B |
| REC-002 | P1 | Tratar `ViajeSinEstres_AlivioEmocional` y `ViajaComoInvitado_Identidad` como referencias principales de aprendizaje. | INS-002, CON-003 | Preservar las principales fuentes de volumen cualificado mientras se prueban variantes | Comparar futuras variantes contra volumen y tasa A/B |
| REC-003 | P1 | No publicar CPQL por anuncio o campaña como definitivo hasta autorizar modelado spend-lead emparejado. | INS-005, RSK-001, UNKNOWN-001 | Evitar decisiones falsas de eficiencia | Reejecutar con modelo emparejado aprobado o política MCP que permita joins |
| REC-004 | P2 | Ejecutar tests controlados de expansión RTG/diáspora en lugar de escalar ampliamente de inmediato. | INS-003, HYP-002 | Validar si la mayor calidad se sostiene con más volumen | Medir tasa A/B y volumen bajo incremento de inversión |
| REC-005 | P2 | Usar referencias `FiltroBilletes` como candidatas a filtro de calidad en nuevos tests. | HYP-001 | Mejorar filtrado de intención sin depender solo de retargeting | Exigir volumen mínimo antes de declarar ganador |
| REC-006 | P2 | Mantener separadas las decisiones sobre Facebook e Instagram hasta validar eficiencia de inversión por plataforma. | FND-004, RSK-001 | Evitar reasignar presupuesto solo por calidad observada del lado lead | Añadir o autorizar evidencia emparejada de inversión-calidad por plataforma |
| REC-007 | P3 | Incorporar clics, impresiones y outcomes CRM a un futuro scope ampliado si la eficiencia de embudo se convierte en requisito de decisión. | UNKNOWN-003, UNKNOWN-004 | Permitir diagnóstico más completo más allá de calidad de lead | Actualizar Data Contract antes de adquirir evidencia |

## Presentación - Informe analítico

### Lectura ejecutiva

El sistema de Meta Lead Ads generó volumen cualificado relevante hasta el 30 de junio de 2026. Entre el 18 de abril de 2026 y el 30 de junio de 2026 produjo 1.322 leads distintos, de los cuales 395 fueron leads cualificados A/B. En términos prácticos, aproximadamente tres de cada diez leads cumplieron el umbral de calidad FARO.

El punto más importante es que junio escaló volumen sin romper la calidad agregada. Junio entregó 774 leads y 229 cualificados A/B, con una tasa A/B del 29,59%, muy cercana a abril y mayo. Esto sugiere que el sistema no está comprando únicamente volumen barato: mantiene una señal cualificada estable mientras crece.

### Qué está funcionando

Dos referencias de anuncio dominan la base de leads cualificados:

- `ViajeSinEstres_AlivioEmocional_ViajeSinEstres_Reel_v1`: 642 leads, 187 A/B.
- `ViajaComoInvitado_Identidad_ViajarComoLocal_Reel_v1`: 358 leads, 102 A/B.

Juntas generaron 289 leads A/B, el 73,16% de todos los A/B observados. Estas referencias deben tratarse como la base principal de aprendizaje del sistema actual de Meta Lead Ads.

El segmento RTG/diáspora es más pequeño, pero muestra una tasa de calidad superior. El formulario diáspora produjo 53 A/B sobre 142 leads, una tasa A/B del 37,32%, frente a 342 A/B sobre 1.180 leads y una tasa del 28,98% en Isla/captación. Es una señal prometedora, pero aún no sustituye a escala la línea principal de captación.

### Qué requiere cautela

La principal restricción analítica es la atribución de eficiencia. La inversión está disponible y la inversión comercial totalizó 875,83 en el periodo, pero el MCP rechazó los joins necesarios para construir un modelo emparejado spend-lead. Por ello, este informe no afirma CPQL definitivo por anuncio, campaña o conjunto.

La inversión comercial está direccionalmente concentrada alrededor de referencias nombradas que también producen volumen de leads, especialmente `ViajeSinEstres_AlivioEmocional` y `ViajaComoInvitado_Identidad`, pero eso sigue siendo una señal cautelosa de alineación, no una conclusión de eficiencia emparejada.

### Mecánica de calidad

El scoring FARO se comporta de forma coherente en la evidencia disponible. Los grupos A y B muestran scores medios superiores y señales de intención relacionadas con billetes más fuertes que C y D. El modelo es útil como lenguaje operativo de calidad para este análisis.

Distribución de tiers:

- A: 57 leads.
- B: 338 leads.
- C: 553 leads.
- D: 374 leads.

El reto principal del sistema no es la ausencia de leads cualificados. Es separar las fuentes de alto volumen cualificado de las bolsas amplias de leads C/D de menor intención, y tomar decisiones de inversión sin sobreafirmar precisión coste-calidad.

### Postura recomendada de decisión

Priorizar escala preservando calidad. Mantener protegidas las dos referencias dominantes de volumen cualificado como anclas de aprendizaje, probar expansión RTG/diáspora de forma incremental y usar `FiltroBilletes` como hipótesis de filtro de calidad, no como ganador declarado.

Antes de hacer reasignaciones fuertes de inversión por anuncio o campaña, conviene estabilizar una vía aprobada de evidencia emparejada spend-lead. Hasta entonces, las decisiones más seguras son tests creativos y de segmento guiados por calidad, no movimientos definitivos basados en CPQL.

## Resultado del checklist final

| Área | Resultado |
|---|---|
| Execution Context | Pass |
| Contexto oficial | Pass |
| Data Provider | Pass tras renovación ADC y reinicio del MCP |
| Evidence Set | Pass con limitación declarada sobre joins MCP |
| Knowledge Set | Pass |
| Recommendation Set | Pass |
| Presentation | Pass |
| Aislamiento histórico | Pass; no se usaron informes ni sets anteriores como input analítico |

Equivalencia semántica preservada: la presentación consume el Context Definition, Evidence Set, Knowledge Set y Recommendation Set anteriores sin añadir evidencia, conocimiento nuevo ni recomendaciones nuevas.
