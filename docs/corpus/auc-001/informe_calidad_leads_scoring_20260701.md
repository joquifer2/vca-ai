# Informe Ejecutivo de Calidad de Leads, Scoring y Eficiencia de Inversión — Meta Lead Ads

> Nota de clasificación:
> - Artefacto histórico experimental.
> - Se utiliza como evidencia para investigar la construcción del Knowledge Set.
> - No es una plantilla normativa.
> - No define la estructura obligatoria de los informes.
> - No es una Presentation Policy.
> - No constituye evidencia de negocio vigente.
> - Sus fortalezas y debilidades deben analizarse, no copiarse.

## 1. Resumen ejecutivo

Se han analizado **1.339 leads** procedentes de formularios nativos de Meta y se han cruzado con los datos de inversión disponibles a nivel de `ad_id`.

| Métrica | Resultado |
|---|---:|
| Leads analizados | 1.339 |
| Inversión analizada | 1.097,69 € |
| CPL medio | 0,82 € |
| Score medio | 49,0 |
| Qualified Leads | 396 |
| % Qualified Leads | 29,6% |
| Coste por Qualified Lead | 2,77 € |
| High Quality Leads | 65 |
| % High Quality Leads | 4,9% |
| Coste por High Quality Lead | 16,89 € |

La captación genera **volumen suficiente y a un CPL bajo**, pero la calidad está concentrada en una parte reducida del tráfico. El dato clave para Dirección no es el CPL, sino el **coste por lead cualificado** y, especialmente, el **coste por lead de alta calidad**.

Actualmente ya se está enviando a Meta el evento **QualifiedLead** desde hace aproximadamente una semana para los leads con scoring **A y B**. Sin embargo, todavía **no se ha activado la optimización de campañas sobre este evento**, porque el volumen acumulado es todavía reducido: **19 eventos QualifiedLead**. El evento **HighQualityLead** todavía no está activo.

La lectura principal es que Meta está comprando volumen barato, pero no todo ese volumen tiene el mismo valor comercial. La estrategia correcta es seguir alimentando el algoritmo con señales de calidad y activar la optimización sobre `QualifiedLead` cuando exista suficiente volumen para hacerlo con menor riesgo.

---

## 2. Objetivo del análisis

El objetivo es evaluar si los formularios nativos de Meta están generando leads con suficiente calidad comercial y si la inversión está generando oportunidades accionables.

Este análisis permite responder a:

- si el volumen captado es suficiente;
- si la calidad captada justifica la inversión;
- qué variables explican mejor la calidad;
- qué campañas, conjuntos y creatividades son más eficientes;
- qué señales deben enviarse a Meta mediante Conversion API;
- qué riesgos existen si se optimiza únicamente hacia volumen de leads.

---

## 3. Metodología aplicada

### Fuentes de datos

| Fuente | Registros | Uso |
|---|---:|---|
| Formularios ISLA | 1.197 | Leads, variables de formulario y scoring existente |
| Formularios DIASPORA | 142 | Leads y variables de formulario |
| Costes Meta Ads | 7.191 filas | Inversión por campaña, conjunto, anuncio, región y día |

### Cruce de datos

El cruce se ha realizado mediante `ad_id`.

El archivo de costes estaba desglosado por región y fecha, por lo que se ha agregado previamente a nivel de anuncio para evitar duplicidades de inversión.

| Validación | Resultado |
|---|---:|
| Leads con `ad_id` cruzado con costes | 100% |
| Anuncios con coste y sin leads asociados | 3 |
| Inversión sin leads asociados | 2,88 € |

### Scoring

En ISLA se ha utilizado el score existente incluido en el dataset.

En DIASPORA no existía score original, por lo que se ha inferido a partir de las variables disponibles:

- billetes de avión;
- fecha prevista de viaje;
- número de personas;
- tipo de experiencia buscada.

### Criterios utilizados

| Categoría | Regla |
|---|---|
| Qualified Lead | Score ≥ 60 |
| High Quality Lead | Score ≥ 80 |
| Tier A | 80–100 |
| Tier B | 60–79 |
| Tier C | 40–59 |
| Tier D | 0–39 |

### Limitaciones

- No hay datos de ventas, llamadas, visitas, ingresos ni conversión comercial posterior.
- El análisis mide calidad declarada e intención comercial, no rentabilidad final.
- El scoring de DIASPORA es inferido y debería validarse contra resultados comerciales reales.
- El estado de envío de `QualifiedLead` se incorpora como dato operativo actual del proyecto: **19 eventos enviados aproximadamente durante la última semana**.

---

## 4. Resultado global del scoring

| Tier   |   Leads | % Leads   | Score medio   |   Qualified |
|:-------|--------:|:----------|:--------------|------------:|
| D      |     410 | 30,6%     | 28,4          |           0 |
| C      |     533 | 39,8%     | 48,7          |           0 |
| B      |     331 | 24,7%     | 67,7          |         331 |
| A      |      65 | 4,9%      | 85,8          |          65 |

| Origen   |   Leads | Score medio   |   Qualified | % Qualified   |   High Quality | % High Quality   |
|:---------|--------:|:--------------|------------:|:--------------|---------------:|:-----------------|
| DIASPORA |     142 | 44,8          |          45 | 31,7%         |             15 | 10,6%            |
| ISLA     |    1197 | 49,5          |         351 | 29,3%         |             50 | 4,2%             |
| TOTAL    |    1339 | 49,0          |         396 | 29,6%         |             65 | 4,9%             |

La captación tiene una base amplia, pero la calidad se concentra en una minoría. El **29,6%** de los leads alcanza nivel cualificado y solo el **4,9%** llega a High Quality Lead.

Esto confirma que el sistema no debe optimizarse únicamente por volumen de formularios enviados. El evento `Lead` es útil para medir captación, pero no representa por sí solo la calidad comercial real.

---

## 5. Análisis de cada variable relevante

### 5.1 Billetes de avión

| Billetes                   |   Leads | Score   |   Qualified | % Qualified   |   High Quality | % High Quality   |
|:---------------------------|--------:|:--------|------------:|:--------------|---------------:|:-----------------|
| no, solo estoy mirando     |     838 | 39,4    |          44 | 5,3%          |              0 | 0,0%             |
| estoy en proceso de compra |     319 | 60,4    |         190 | 59,6%         |             14 | 4,4%             |
| sí, ya los tengo           |     182 | 73,5    |         162 | 89,0%         |             51 | 28,0%            |

La variable más explicativa de calidad es tener billetes o estar en proceso de compra. Los leads que ya tienen billetes presentan una tasa de cualificación muy superior y concentran la mayoría de los High Quality Leads.

Conclusión: **tener billetes comprados** debe tratarse como señal prioritaria para el equipo comercial y para Conversion API.

### 5.2 Fecha prevista de viaje

| Fecha prevista        |   Leads | Score   |   Qualified | % Qualified   |   High Quality | % High Quality   |
|:----------------------|--------:|:--------|------------:|:--------------|---------------:|:-----------------|
| aún no lo tengo claro |     464 | 37,2    |          25 | 5,4%          |              0 | 0,0%             |
| entre 3 y 6 meses     |     347 | 51,7    |         104 | 30,0%         |              6 | 1,7%             |
| entre 1 y 3 meses     |     144 | 63,8    |          95 | 66,0%         |             17 | 11,8%            |
| en menos de 1 mes     |      82 | 75,5    |          76 | 92,7%         |             30 | 36,6%            |
| septiembre 2026       |      47 | 55,6    |          25 | 53,2%         |              3 | 6,4%             |
| octubre 2026          |      46 | 48,1    |          11 | 23,9%         |              0 | 0,0%             |
| noviembre 2026        |      36 | 53,1    |          12 | 33,3%         |              0 | 0,0%             |
| agosto 2026           |      25 | 64,2    |          16 | 64,0%         |              4 | 16,0%            |
| mayo 2027             |      24 | 43,8    |           6 | 25,0%         |              0 | 0,0%             |
| marzo 2027            |      24 | 38,8    |           2 | 8,3%          |              0 | 0,0%             |
| junio 2027            |      22 | 40,2    |           2 | 9,1%          |              0 | 0,0%             |
| abril 2027            |      19 | 36,1    |           0 | 0,0%          |              0 | 0,0%             |
| julio 2026            |      18 | 72,6    |          15 | 83,3%         |              4 | 22,2%            |
| diciembre 2026        |      17 | 48,7    |           4 | 23,5%         |              1 | 5,9%             |
| enero 2027            |      12 | 44,1    |           2 | 16,7%         |              0 | 0,0%             |
| febrero 2027          |      12 | 42,5    |           1 | 8,3%          |              0 | 0,0%             |

La proximidad temporal incrementa de forma clara la calidad. Un lead con fecha definida y cercana está mucho más cerca de una decisión real.

Los leads sin fecha clara generan volumen, pero su tasa de cualificación es muy baja. Esto los convierte en perfiles adecuados para nutrición, no necesariamente para contacto comercial prioritario.

Conclusión: la fecha prevista debe utilizarse como criterio de priorización y como señal avanzada para Meta.

### 5.3 Tipo de experiencia

| Experiencia                         |   Leads | Score   |   Qualified | % Qualified   |   High Quality | % High Quality   |
|:------------------------------------|--------:|:--------|------------:|:--------------|---------------:|:-----------------|
| aún estoy valorando opciones        |     565 | 37,4    |          58 | 10,3%         |              0 | 0,0%             |
| organización completa del viaje     |     438 | 55,6    |         157 | 35,8%         |             23 | 5,3%             |
| experiencia privada y personalizada |     181 | 61,7    |          98 | 54,1%         |             32 | 17,7%            |
| solo me interesa algún tour suelto  |     155 | 58,0    |          83 | 53,5%         |             10 | 6,5%             |

La experiencia privada y personalizada es la categoría de mayor valor relativo. No es la de más volumen, pero sí la que muestra mayor proporción de High Quality Leads.

Conclusión: las campañas deberían reforzar mensajes orientados a experiencia personalizada, viaje organizado y planificación con valor añadido.

### 5.4 Número de personas

| Personas          |   Leads | Score   |   Qualified | % Qualified   |   High Quality | % High Quality   |
|:------------------|--------:|:--------|------------:|:--------------|---------------:|:-----------------|
| 1-2 personas      |     906 | 47,3    |         249 | 27,5%         |             34 | 3,8%             |
| 3-4 personas      |     307 | 51,5    |          96 | 31,3%         |             19 | 6,2%             |
| 5-8 personas      |      90 | 55,8    |          38 | 42,2%         |              8 | 8,9%             |
| más de 9 personas |      36 | 53,4    |          13 | 36,1%         |              4 | 11,1%            |

Los grupos grandes tienen mayor potencial, aunque representan poco volumen. La mayoría de leads viajan en pareja o individualmente.

Conclusión: el número de personas no debe ser la señal principal de calidad, pero sí una variable útil para estimar valor potencial.

---

## 6. Relaciones entre variables

La calidad aumenta claramente cuando se combinan tres factores:

1. billetes comprados o en proceso de compra;
2. fecha de viaje cercana o definida;
3. experiencia personalizada u organización completa.

La combinación opuesta —sin billetes, sin fecha clara y todavía valorando opciones— genera mucho volumen, pero escaso valor comercial inmediato.

La relación más importante para negocio no es una única respuesta aislada, sino la acumulación de señales de intención.

---

## 7. Análisis por creatividad

| Creatividad                                                | Spend    |   Leads | CPL    | Score medio   |   Qualified | CPQL   |   High Quality | CPHQL   |
|:-----------------------------------------------------------|:---------|--------:|:-------|:--------------|------------:|:-------|---------------:|:--------|
| ViajeSinEstres_AlivioEmocional_ViajeSinEstres              | 468,06 € |     648 | 0,72 € | 49,9          |         190 | 2,46 € |             23 | 20,35 € |
| ViajaComoInvitado_Identidad_ViajarComoLocal                | 245,84 € |     362 | 0,68 € | 48,4          |         103 | 2,39 € |             18 | 13,66 € |
| FiltroBilletes_EscasezReal_3TipsDeViaje                    | 155,64 € |     118 | 1,32 € | 43,6          |          34 | 4,58 € |             12 | 12,97 € |
| ExperienciasUnicas_ViajesConAlma_BoriWine2026              | 50,01 €  |      67 | 0,75 € | 44,3          |           8 | 6,25 € |              0 | —       |
| FiltroBilletes_AutoSegmentacion_PrimeraVez                 | 48,96 €  |      60 | 0,82 € | 53,7          |          24 | 2,04 € |              4 | 12,24 € |
| ViajaComoInvitado_Estatus_ExperienciaCalidad               | 18,22 €  |      20 | 0,91 € | 54,8          |           8 | 2,28 € |              1 | 18,22 € |
| FiltroBilletes_EscasezReal_3TipsDeViaje                    | 25,16 €  |      19 | 1,32 € | 59,5          |          10 | 2,52 € |              2 | 12,58 € |
| MasCaroPorqueMejor_CalidadVsCantidad_ViajesConCalidad      | 44,95 €  |      18 | 2,50 € | 52,8          |           9 | 4,99 € |              3 | 14,98 € |
| ViajeSinEstres_PrevencionDeRiesgo_ErroresViaje             | 12,52 €  |      16 | 0,78 € | 49,9          |           6 | 2,09 € |              2 | 6,26 €  |
| ExperienciasUnicas_OportunidadIrrepetible_EclipseSolar2026 | 4,86 €   |       5 | 0,97 € | 50,6          |           2 | 2,43 € |              0 | —       |
| FiltroBilletes_AutoSegmentacion_PrimeraVez                 | 5,69 €   |       3 | 1,90 € | 26,7          |           0 | —      |              0 | —       |
| ExperienciasUnicas_OportunidadIrrepetible_EclipseSolar2026 | 11,75 €  |       2 | 5,88 € | 70,0          |           2 | 5,88 € |              0 | —       |
| ExperienciasUnicas_LugaresSorprendentes_CamposLavanda      | 3,15 €   |       1 | 3,15 € | 35,0          |           0 | —      |              0 | —       |

### Interpretación

**ViajeSinEstres_AlivioEmocional** y **ViajaComoInvitado_Identidad** son las principales piezas de volumen. Ambas tienen CPL bajo y CPQL competitivo, aunque su capacidad para generar High Quality Leads es distinta.

**FiltroBilletes_AutoSegmentacion** destaca por su buen equilibrio entre coste y calidad: CPL bajo, CPQL competitivo y una tasa de cualificación superior a la media.

**BoriWine2026** genera volumen a bajo CPL, pero presenta una baja tasa de cualificación y no genera High Quality Leads en el periodo analizado. No debería escalarse sin revisar ángulo, segmentación o formulario.

**PrevencionDeRiesgo_ErroresViaje** muestra buena eficiencia inicial, especialmente en CPHQL, pero el volumen todavía es bajo. Conviene testarlo con inversión controlada antes de extraer conclusiones definitivas.

---

## 8. Análisis por campaña

| Campaña                        | Spend    |   Leads | CPL    |   Qualified | % Qualified   | CPQL   |   High Quality | CPHQL   |
|:-------------------------------|:---------|--------:|:-------|------------:|:--------------|:-------|---------------:|:--------|
| [META] [CLP] [CAPTACIÓN] [ABO] | 873,63 € |    1197 | 0,73 € |         351 | 29,3%         | 2,49 € |             50 | 17,47 € |
| [META] [CLP] [RTG] [CBO]       | 221,86 € |     142 | 1,56 € |          45 | 31,7%         | 4,93 € |             15 | 14,79 € |

La campaña de captación es más eficiente en CPL y CPQL. La campaña de retargeting presenta un CPL y CPQL más elevados, pero muestra mejor proporción de High Quality Leads y un CPHQL más competitivo.

Conclusión: captación funciona bien para volumen cualificado barato; retargeting puede ser más interesante para capturar leads de mayor valor, aunque necesita control de eficiencia.

---

## 9. Evolución temporal

| Semana     | Spend    |   Leads | CPL    |   Qualified | % Qualified   | CPQL    |   High Quality |
|:-----------|:---------|--------:|:-------|------------:|:--------------|:--------|---------------:|
| 2026-04-13 | 20,73 €  |      36 | 0,58 € |          10 | 27,8%         | 2,07 €  |              2 |
| 2026-04-20 | 114,62 € |     145 | 0,79 € |          47 | 32,4%         | 2,44 €  |              7 |
| 2026-04-27 | 10,94 €  |       8 | 1,37 € |           5 | 62,5%         | 2,19 €  |              0 |
| 2026-05-04 | 141,19 € |     182 | 0,78 € |          59 | 32,4%         | 2,39 €  |             14 |
| 2026-05-11 | 148,87 € |     183 | 0,81 € |          54 | 29,5%         | 2,76 €  |             10 |
| 2026-05-18 | 10,98 €  |       7 | 1,57 € |           0 | 0,0%          | —       |              0 |
| 2026-06-01 | 173,59 € |     214 | 0,81 € |          53 | 24,8%         | 3,28 €  |              8 |
| 2026-06-08 | 144,74 € |     183 | 0,79 € |          56 | 30,6%         | 2,58 €  |             12 |
| 2026-06-15 | 144,95 € |     194 | 0,75 € |          69 | 35,6%         | 2,10 €  |              6 |
| 2026-06-22 | 149,42 € |     155 | 0,96 € |          40 | 25,8%         | 3,74 €  |              6 |
| 2026-06-29 | 37,66 €  |      32 | 1,18 € |           3 | 9,4%          | 12,55 € |              0 |

La eficiencia no es completamente estable. La semana del **22 de junio de 2026** muestra un deterioro respecto a semanas anteriores: sube el CPL, empeora el CPQL y cae el porcentaje de leads cualificados.

La semana del **29 de junio de 2026** todavía debe leerse con cautela porque el volumen es menor, pero apunta a una caída adicional de eficiencia.

Conclusión: conviene revisar cambios recientes en inversión, creatividades, audiencias, aprendizaje de campañas o fatiga de anuncios.

---

## 10. Comparativa por plataforma

| Plataforma   |   Leads | Score   |   Qualified | % Qualified   |   High Quality | % High Quality   |
|:-------------|--------:|:--------|------------:|:--------------|---------------:|:-----------------|
| Facebook     |     903 | 49,2    |         276 | 30,6%         |             44 | 4,9%             |
| Instagram    |     436 | 48,6    |         120 | 27,5%         |             21 | 4,8%             |

Facebook aporta más volumen y una calidad ligeramente superior. Instagram no debe descartarse, pero debería analizarse con inversión por plataforma para poder comparar CPL, CPQL y CPHQL de forma completa.

Conclusión: no conviene tomar decisiones de presupuesto por plataforma únicamente con volumen y score; falta el coste desglosado por plataforma.

---

## 11. Combinaciones más frecuentes

| Combinación                                                                                         |   Leads | Score medio   |   Qualified | % Qualified   |   High Quality |
|:----------------------------------------------------------------------------------------------------|--------:|:--------------|------------:|:--------------|---------------:|
| no, solo estoy mirando + aún no lo tengo claro + 1-2 personas + aún estoy valorando opciones        |     127 | 24,3          |           0 | 0,0%          |              0 |
| no, solo estoy mirando + aún no lo tengo claro + 1-2 personas + organización completa del viaje     |      96 | 43,8          |           0 | 0,0%          |              0 |
| no, solo estoy mirando + aún no lo tengo claro + 3-4 personas + aún estoy valorando opciones        |      58 | 29,0          |           0 | 0,0%          |              0 |
| no, solo estoy mirando + entre 3 y 6 meses + 1-2 personas + aún estoy valorando opciones            |      58 | 30,6          |           0 | 0,0%          |              0 |
| no, solo estoy mirando + entre 3 y 6 meses + 1-2 personas + organización completa del viaje         |      57 | 50,5          |           0 | 0,0%          |              0 |
| no, solo estoy mirando + aún no lo tengo claro + 3-4 personas + organización completa del viaje     |      37 | 49,5          |           0 | 0,0%          |              0 |
| estoy en proceso de compra + entre 3 y 6 meses + 1-2 personas + organización completa del viaje     |      30 | 65,8          |          30 | 100,0%        |              0 |
| no, solo estoy mirando + aún no lo tengo claro + 1-2 personas + experiencia privada y personalizada |      29 | 41,2          |           0 | 0,0%          |              0 |
| estoy en proceso de compra + entre 3 y 6 meses + 1-2 personas + aún estoy valorando opciones        |      25 | 46,9          |           0 | 0,0%          |              0 |
| no, solo estoy mirando + entre 3 y 6 meses + 3-4 personas + organización completa del viaje         |      21 | 56,4          |           0 | 0,0%          |              0 |

La combinación más frecuente es también una de las menos valiosas: usuarios sin billetes, sin fecha clara, 1–2 personas y todavía valorando opciones.

La combinación más accionable es usuario en proceso de compra, con fecha definida y búsqueda de organización completa. Aunque no siempre genera el mayor volumen, representa una intención comercial mucho más clara.

---

## 12. Hallazgos principales

1. El CPL medio es bajo: **0,82 €**.
2. El coste por Qualified Lead es razonable: **2,77 €**.
3. El coste por High Quality Lead sube a **16,89 €**, que es una métrica más exigente y cercana a valor de negocio.
4. La variable más explicativa de calidad es tener billetes comprados o estar en proceso de compra.
5. La fecha prevista de viaje es la segunda gran señal de intención.
6. Las experiencias privadas y personalizadas concentran mayor calidad relativa.
7. Las creatividades de volumen no siempre son las mejores para calidad.
8. El evento `Lead` no es suficiente para entrenar a Meta hacia perfiles de valor.
9. El evento `QualifiedLead` ya se está enviando, pero todavía no se utiliza como evento de optimización.
10. La evolución reciente muestra señales de pérdida de eficiencia que deben revisarse.

---

## 13. Lectura estratégica

Los datos muestran que el sistema de captación funciona, pero todavía está optimizado principalmente hacia volumen.

El negocio no necesita únicamente más leads. Necesita que Meta aprenda a encontrar más usuarios con intención real de viaje, fecha definida, billetes comprados o necesidad clara de organización.

Como primer paso en esta estrategia, hace aproximadamente una semana se ha comenzado a enviar a Meta mediante Conversion API el evento **QualifiedLead**, correspondiente a los leads clasificados con **Tier A y Tier B** según el modelo de scoring.

En el momento de elaboración de este informe únicamente se han enviado **19 eventos QualifiedLead**, un volumen todavía insuficiente para activar la optimización de campañas sobre este evento con garantías.

Por este motivo, las campañas continúan optimizando actualmente sobre el evento **Lead**, mientras se acumula un volumen suficiente de conversiones cualificadas que permita cambiar el objetivo de optimización minimizando el riesgo de inestabilidad en el algoritmo.

El evento **HighQualityLead** todavía no se encuentra implementado y constituye el siguiente paso evolutivo del sistema de optimización.

---

## 14. Recomendaciones para Meta Ads

### Estado actual de la integración

| Evento | Estado actual | Uso actual |
|---|---|---|
| Lead | Activo | Optimización actual de campañas |
| QualifiedLead | Implementado y enviándose por Conversion API | Recogida de volumen; todavía no usado como evento de optimización |
| HighQualityLead | No implementado | Pendiente de activación futura |

Actualmente el sistema ya envía mediante Conversion API los eventos **QualifiedLead** correspondientes a los leads clasificados como **Tier A y Tier B**.

Hasta la fecha se han registrado **19 eventos**, por lo que todavía no existe masa crítica suficiente para que Meta pueda optimizar de forma estable utilizando este evento como objetivo principal.

Por este motivo se recomienda mantener temporalmente la optimización sobre el evento **Lead**, continuando el envío de **QualifiedLead** para alimentar el algoritmo hasta alcanzar un volumen suficiente de conversiones.

### Próxima evolución recomendada

Una vez se alcance un volumen estable de Qualified Leads se recomienda:

1. cambiar progresivamente la optimización de campañas desde **Lead** hacia **QualifiedLead**;
2. monitorizar durante varias semanas la evolución del coste por Qualified Lead y del volumen de conversión;
3. implementar posteriormente el evento **HighQualityLead** para disponer de una segunda señal de calidad más restrictiva y de mayor valor comercial.

### Señales recomendadas

| Señal | Regla recomendada | Uso |
|---|---|---|
| Lead | Todo formulario recibido | Medición base |
| QualifiedLead | Score ≥ 60 / Tier A o B | Optimización principal futura |
| HighQualityLead | Score ≥ 80 / Tier A | Señal premium pendiente de implementación |
| LeadWithTickets | Tiene billetes comprados | Señal de intención fuerte |
| LeadTravelSoon | Viaje en menos de 1 mes o 1–3 meses | Señal de urgencia |
| LeadPrivateExperience | Busca experiencia privada | Señal de valor potencial |

---

## 15. Reglas operativas

### Equipo comercial

| Condición | Acción |
|---|---|
| Score ≥ 80 | Contacto prioritario inmediato |
| Score 60–79 | Contacto en primera ola |
| Tiene billetes | Prioridad alta |
| Viaje en menos de 1 mes | Prioridad alta |
| Sin billetes y sin fecha clara | Nutrición automatizada |

### CRM

- Guardar score inicial.
- Guardar tier.
- Guardar motivo de cualificación.
- Registrar resultado comercial posterior.
- Medir conversión por tier, campaña y creatividad.

### Conversion API

Estado actual:

- Se envía el evento **Lead** para todos los formularios recibidos.
- Se envía el evento **QualifiedLead** para los leads clasificados como **Tier A y Tier B**.
- Actualmente se han enviado **19 eventos QualifiedLead**.
- Todavía no se ha activado la optimización de campañas sobre **QualifiedLead**.
- El evento **HighQualityLead** todavía no está implementado.

Próximos pasos técnicos:

- Mantener el envío de QualifiedLead hasta acumular volumen suficiente.
- Evaluar el momento adecuado para cambiar la optimización hacia QualifiedLead.
- Implementar el envío del evento HighQualityLead.
- Monitorizar la estabilidad de campaña tras el cambio de evento de optimización.

---

## 16. Implicaciones para campañas

### Matriz de eficiencia de creatividades

| Creatividad                                           |   Leads | % Qualified   | CPQL   |   High Quality | CPHQL   | Acción                       |
|:------------------------------------------------------|--------:|:--------------|:-------|---------------:|:--------|:-----------------------------|
| FiltroBilletes_AutoSegmentacion_PrimeraVez            |      60 | 40,0%         | 2,04 € |              4 | 12,24 € | Escalar / priorizar          |
| ViajeSinEstres_PrevencionDeRiesgo_ErroresViaje        |      16 | 37,5%         | 2,09 € |              2 | 6,26 €  | Escalar / priorizar          |
| ViajaComoInvitado_Estatus_ExperienciaCalidad          |      20 | 40,0%         | 2,28 € |              1 | 18,22 € | Escalar / priorizar          |
| ViajaComoInvitado_Identidad_ViajarComoLocal           |     362 | 28,5%         | 2,39 € |             18 | 13,66 € | Revisar mensaje / formulario |
| ViajeSinEstres_AlivioEmocional_ViajeSinEstres         |     648 | 29,3%         | 2,46 € |             23 | 20,35 € | Revisar mensaje / formulario |
| FiltroBilletes_EscasezReal_3TipsDeViaje               |      19 | 52,6%         | 2,52 € |              2 | 12,58 € | Mantener y optimizar coste   |
| FiltroBilletes_EscasezReal_3TipsDeViaje               |     118 | 28,8%         | 4,58 € |             12 | 12,97 € | Limitar o replantear         |
| MasCaroPorqueMejor_CalidadVsCantidad_ViajesConCalidad |      18 | 50,0%         | 4,99 € |              3 | 14,98 € | Mantener y optimizar coste   |
| ExperienciasUnicas_ViajesConAlma_BoriWine2026         |      67 | 11,9%         | 6,25 € |              0 | —       | Limitar o replantear         |

### Escalar con control

| Creatividad | Motivo |
|---|---|
| FiltroBilletes_AutoSegmentacion | Buen CPQL y buena capacidad de filtro |
| ViajeSinEstres_PrevencionDeRiesgo | Muy buen CPHQL inicial, aunque con volumen bajo |
| ViajaComoInvitado_Identidad | Gran volumen y CPQL competitivo |

### Mantener y optimizar

| Creatividad | Motivo |
|---|---|
| ViajeSinEstres_AlivioEmocional | Gran volumen y CPQL razonable, pero CPHQL más alto |
| FiltroBilletes_EscasezReal | Puede filtrar intención, pero hay diferencias relevantes entre campañas |
| MasCaroPorqueMejor | Buena calidad relativa, pero coste alto y bajo volumen |

### Revisar antes de escalar

| Creatividad | Motivo |
|---|---|
| BoriWine2026 | CPL bajo, pero baja cualificación y sin High Quality Leads |
| Creatividades con bajo volumen | No permiten conclusiones definitivas |

---

## 17. Riesgos detectados

1. Optimizar hacia CPL bajo y no hacia calidad real.
2. Escalar creatividades con volumen pero baja calidad.
3. Penalizar creatividades con CPL alto que generan mejores leads.
4. Usar solo `Lead` como señal de optimización durante demasiado tiempo.
5. Cambiar demasiado pronto la optimización a `QualifiedLead` sin suficiente volumen.
6. Sobrecargar al equipo comercial con leads exploratorios.
7. No disponer todavía de datos de venta para validar rentabilidad final.
8. Tomar decisiones definitivas sobre anuncios con poco volumen.
9. No investigar el deterioro observado en la segunda mitad de junio.

---

## 18. Próximos pasos

1. Continuar acumulando volumen de eventos **QualifiedLead** enviados mediante Conversion API.
2. Evaluar el momento adecuado para activar la optimización de campañas utilizando **QualifiedLead** como evento principal.
3. Implementar el envío del evento **HighQualityLead**.
4. Crear un dashboard que monitorice diariamente:
   - Leads.
   - Qualified Leads.
   - High Quality Leads.
   - CPL.
   - Coste por Qualified Lead.
   - Coste por High Quality Lead.
5. Revisar la pérdida de eficiencia observada durante la semana del 22 de junio de 2026 y la semana del 29 de junio de 2026.
6. Incrementar progresivamente la inversión en creatividades con mejor CPQL y CPHQL.
7. Integrar los datos del CRM para medir la conversión desde Qualified Lead hasta venta.
8. Validar el modelo de scoring utilizando datos reales de conversión comercial.

---

## 19. Conclusión

La captación de Meta está funcionando correctamente en términos de volumen y coste inicial. Sin embargo, el verdadero indicador de rendimiento no es el coste por Lead, sino el coste por Lead Cualificado y por Lead de Alta Calidad.

Actualmente ya se ha iniciado la transición hacia un modelo de optimización basado en calidad. Desde hace aproximadamente una semana el sistema envía mediante Conversion API los eventos **QualifiedLead** correspondientes a los leads clasificados como **Tier A y Tier B**.

No obstante, el volumen acumulado (**19 eventos**) todavía es insuficiente para activar con garantías la optimización de campañas sobre este evento. Por ello, la estrategia actual consiste en seguir alimentando el algoritmo mientras las campañas continúan optimizando sobre **Lead**.

La siguiente evolución natural será implementar el evento **HighQualityLead** y, una vez exista suficiente histórico de conversiones cualificadas, migrar progresivamente la optimización hacia eventos que representen mejor el valor real para el negocio.

---

## 20. Mensaje para dirección

Meta está generando volumen a bajo coste, pero el valor real está concentrado en una parte reducida de los leads. El coste por lead cualificado es de **2,77 €** y el coste por lead de alta calidad es de **16,89 €**. La estrategia de calidad ya está en marcha: desde hace aproximadamente una semana se está enviando el evento **QualifiedLead** a Meta, aunque todavía no se ha activado la optimización sobre este evento porque solo hay **19 eventos acumulados**. La recomendación es seguir recogiendo volumen, implementar posteriormente **HighQualityLead** y migrar la optimización de campañas hacia señales que reflejen mejor el valor real del negocio.
