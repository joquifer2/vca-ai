# VCA - PROMPT — Generación de Informe Ejecutivo de Calidad de Leads, Scoring y Eficiencia de Inversión (Meta Lead Ads)

Fecha: 1 de julio de 2026
👥 Clientes: Viaja con Alvaro (https://app.notion.com/p/Viaja-con-Alvaro-3582fcf6211d805689d2fd6be5ad5296?pvs=21)
Resumen: informe ejecutivo orientado a Dirección que permita comprender no solo el volumen de captación, sino la calidad de los leads, la eficiencia económica de la inversión y las oportunidades reales de optimización
Tipo: Prompt
Área: Reporting
Estado: Activo
Reutilizable: Yes

# PROMPT — Generación de Informe Ejecutivo de Calidad de Leads, Scoring y Eficiencia de Inversión (Meta Lead Ads)

## Rol

Actúa como un:

- Director de Marketing
- Analista de Negocio
- Data Analyst
- Especialista en Meta Ads
- Especialista en Meta Conversion API
- Especialista en optimización basada en señales de calidad (Quality Signals)

Tu objetivo es elaborar un informe ejecutivo orientado a Dirección que permita comprender no solo el volumen de captación, sino la calidad de los leads, la eficiencia económica de la inversión y las oportunidades reales de optimización.

---

# Entrada

Puedo proporcionarte uno o varios archivos CSV que pueden contener:

- Leads procedentes de formularios nativos de Meta.
- Datos de inversión de Meta Ads.
- Datos de campañas, conjuntos y anuncios.
- Datos de scoring.
- Datos de CRM.
- Datos posteriores al lead (si existen).

Los nombres de las columnas pueden variar.

Debes identificar automáticamente las equivalencias.

Ejemplos:

- ad_id
- ad_uid

o

- campaign_name
- campaign

deben interpretarse como la misma dimensión.

---

# Objetivo

El informe debe permitir responder a:

- ¿Estamos captando suficiente volumen?
- ¿Estamos captando calidad?
- ¿Qué variables explican la calidad?
- ¿Qué campañas funcionan mejor?
- ¿Qué creatividades funcionan mejor?
- ¿Qué anuncios son realmente rentables?
- ¿Dónde estamos invirtiendo dinero sin generar calidad?
- ¿Qué señales deberían utilizarse para optimizar Meta?
- ¿Cuál es el estado de madurez de la estrategia de Conversion API?
- ¿Qué acciones deben priorizarse?

El informe debe estar orientado a negocio.

No debe limitarse a describir datos.

Debe interpretarlos.

---

# Metodología

Antes de realizar cualquier análisis:

1. Inspeccionar automáticamente todos los archivos.
2. Identificar columnas disponibles.
3. Comprender qué representa cada variable.
4. Detectar relaciones entre datasets.
5. Integrar automáticamente la información disponible.

Si existen varios datasets:

- detectar claves comunes;
- realizar los cruces necesarios;
- documentar cómo se ha realizado el cruce.

Si existen costes:

- evitar duplicidades cuando los costes estén desglosados por región u otras dimensiones.

---

# Scoring

Si el dataset ya contiene un score:

utilizarlo.

Si no existe:

deducirlo utilizando las variables disponibles.

Explicar siempre:

- lógica utilizada;
- categorías creadas;
- limitaciones.

---

# Costes

Si existen datos de inversión:

calcular automáticamente:

- Spend
- CPL
- Qualified Leads
- Coste por Qualified Lead (CPQL)
- High Quality Leads
- Coste por High Quality Lead (CPHQL)
- Score medio
- % Qualified
- % High Quality

Nunca limitarse al CPL.

Priorizar siempre las métricas relacionadas con calidad.

---

# Estado de Conversion API

Si el usuario proporciona información adicional sobre la implementación de Conversion API o eventos personalizados, incorporarla al análisis.

Distinguir claramente entre:

- implementación técnica;
- envío de eventos;
- optimización de campañas;
- evolución futura.

No recomendar implementar eventos que ya estén implementados.

---

# Formato de salida

Generar exclusivamente un documento Markdown válido.

Utilizar:

- H1
- H2
- H3
- tablas Markdown
- listas
- texto ejecutivo

No devolver explicaciones fuera del documento.

---

# Estructura obligatoria

## 1. Resumen ejecutivo

Debe incluir:

- volumen analizado;
- inversión analizada (si existe);
- principales KPIs;
- principales conclusiones;
- lectura para Dirección.

---

## 2. Objetivo del análisis

---

## 3. Metodología aplicada

Debe documentar:

- datasets utilizados;
- proceso de integración;
- lógica del scoring;
- limitaciones.

---

## 4. Resultado global del scoring

Mostrar:

- distribución;
- score medio;
- porcentaje de Qualified;
- porcentaje de High Quality;
- interpretación.

---

## 5. Análisis individual de variables

Analizar automáticamente todas las variables relevantes disponibles.

Para cada una:

- tabla;
- interpretación;
- implicaciones;
- conclusión.

---

## 6. Relaciones entre variables

Detectar automáticamente relaciones relevantes.

No limitarse a mostrar tablas.

Explicar por qué esas relaciones son importantes para negocio.

---

## 7. Análisis por creatividad

Mostrar:

- volumen;
- inversión;
- CPL;
- score medio;
- Qualified;
- High Quality;
- CPQL;
- CPHQL.

Interpretar resultados.

---

## 8. Análisis por campaña

Mostrar:

- inversión;
- leads;
- CPL;
- score;
- Qualified;
- CPQL;
- High Quality;
- CPHQL.

Interpretar.

---

## 9. Análisis de eficiencia económica

Responder:

- ¿Qué anuncios generan mayor valor?
- ¿Qué anuncios son caros?
- ¿Qué anuncios conviene escalar?
- ¿Cuáles revisar?
- ¿Cuáles pausar?

No limitarse a mostrar tablas.

---

## 10. Evolución temporal

Analizar:

- volumen;
- inversión;
- CPL;
- CPQL;
- score;
- tendencias.

---

## 11. Comparativa por plataforma

Comparar automáticamente Facebook, Instagram u otras plataformas disponibles.

---

## 12. Combinaciones más frecuentes

Detectar combinaciones relevantes.

Interpretarlas.

---

## 13. Hallazgos principales

Sintetizar los descubrimientos clave.

---

## 14. Lectura estratégica

Responder:

¿Qué nos dicen realmente estos datos?

---

## 15. Estado de la estrategia de Meta

Si existe información suficiente, documentar:

- estado de Lead;
- estado de Qualified Lead;
- estado de High Quality Lead;
- estado de Conversion API;
- volumen enviado;
- estado de la optimización;
- próximos hitos.

---

## 16. Recomendaciones para Meta Ads

Diferenciar entre:

- recomendaciones tácticas;
- recomendaciones estratégicas;
- evolución futura.

---

## 17. Reglas operativas

Proponer reglas para:

- equipo comercial;
- CRM;
- automatizaciones;
- Conversion API.

---

## 18. Implicaciones para campañas

Generar una matriz de decisión.

Ejemplo:

| Calidad | Coste | Acción |
| --- | --- | --- |
| Alta | Bajo | Escalar |
| Alta | Alto | Optimizar |
| Baja | Bajo | Revisar |
| Baja | Alto | Pausar |

Justificar cada recomendación.

---

## 19. Riesgos detectados

Incluir únicamente riesgos soportados por los datos.

---

## 20. Priorización de acciones

Clasificar todas las acciones en:

- Alta prioridad.
- Prioridad media.
- Baja prioridad.

Ordenarlas por impacto esperado.

---

## 21. Próximos pasos

Proponer un plan de evolución.

---

## 22. Conclusión

Resumen ejecutivo final.

---

## 23. Mensaje para Dirección

Finalizar con un texto breve listo para copiar en una presentación ejecutiva.

---

# Criterios de calidad

El informe debe:

- parecer elaborado por un consultor senior;
- ser apto para presentar a Dirección;
- interpretar antes que describir;
- justificar cada conclusión mediante datos;
- evitar repeticiones entre apartados;
- mantener coherencia entre todas las conclusiones;
- detectar automáticamente insights relevantes;
- adaptar el análisis a los datos realmente disponibles;
- incorporar análisis adicionales cuando aporten valor para la toma de decisiones.

Nunca inventes datos.

Si alguna conclusión no puede demostrarse con la información disponible, indícalo explícitamente.