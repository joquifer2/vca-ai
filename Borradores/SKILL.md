---
name: meta-lead-quality-analysis
description: Esta skill ejecuta el caso de uso analitico de calidad de leads en Meta Ads para VCA IA, separando contexto, evidencia, analisis, razonamiento y recomendaciones.
id: SDD-SKILL-006
user-invocable: true
disable-model-invocation: false
---

# Skill - Meta Lead Quality Analysis

## Propósito

Ejecutar el primer caso de uso analítico de VCA IA para analizar la calidad de leads captados mediante Meta Ads, utilizando el lifecycle metodológico heredado de AIF Foundation y BigQuery MCP Server como Data Provider principal.

Esta skill no define una specification ni sustituye la arquitectura analítica del proyecto. Su función es describir el procedimiento reutilizable para producir un análisis trazable y un informe ejecutivo coherente.

Esta skill implementa el caso de uso AUC-001 y sirve para validar la arquitectura analítica de VCA IA, el lifecycle metodológico y el uso de BigQuery MCP Server como Data Provider principal.

## Cuándo usar esta skill

Usar esta skill cuando el objetivo sea analizar la calidad de leads de Meta Ads en VCA y producir una salida ejecutiva trazable.

Aplicarla especialmente cuando la solicitud sea similar a:

- "analiza la calidad de los leads de Meta Ads";
- "genera el informe ejecutivo de lead quality";
- "revisa eficiencia y calidad de captación en Meta Ads";
- "prepara el caso de uso de lead quality analysis";
- "evalúa campañas y creatividades de Meta Ads".

## Reglas

- Tratar AIF Foundation como dependencia metodologica, no como objeto del analisis.
- Usar BigQuery MCP Server como fuente principal de evidencia cuando existan datos disponibles.
- Consultar contexto relevante antes de analizar: CCD, FARO, CLARO, KPIs oficiales y docs/context_refs.md como mapa oficial de contexto.
- No inventar datos, segmentos, campañas, periodos ni conclusiones no sustentadas.
- Separar siempre contexto, evidencia, preparación de datos, análisis, razonamiento, recomendaciones y construcción del informe.
- Mantener trazabilidad entre cada afirmación y su fuente o evidencia.
- Si falta contexto o acceso a datos, marcarlo explícitamente como pendiente en lugar de asumirlo.
- No convertir esta skill en una especificación del sistema ni en una implementación técnica.

## Trazabilidad

Esta skill está asociada al caso de uso [analytical_use_cases/meta_lead_quality_analysis.md](../../../analytical_use_cases/meta_lead_quality_analysis.md) y debe mantenerse alineada con su objetivo, alcance y criterios de éxito.

## Flujo operativo

1. Confirmar el objetivo del análisis.

   Verificar:

   - periodo a analizar;
   - alcance de campañas o conjuntos de anuncios;
   - definición operativa de lead de calidad;
   - audiencia del informe;
   - criterios de éxito esperados.

   Confirmar también que el análisis se usará para validar la arquitectura analítica, el lifecycle y el uso de BigQuery MCP Server definidos por el caso de uso AUC-001.

2. Cargar contexto oficial.

   Revisar, cuando exista disponibilidad:

   - Client Context Document (CCD);
   - FARO;
   - CLARO;
   - KPIs oficiales;
   - docs/context_refs.md;
   - project_brief.md.

3. Identificar Data Providers.

   Priorizar BigQuery MCP Server como fuente principal de evidencia.

   Si el caso lo requiere, identificar Data Providers complementarios compatibles con el análisis.

4. Preparar la evidencia.

   Reunir y estructurar, como minimo:

   - volumen de captación;
   - conversiones y tasas relevantes;
   - coste y eficiencia económica;
   - campañas y creatividades de mejor rendimiento;
   - señales de calidad del lead;
   - hallazgos por segmento o periodo si aplican.

5. Analizar la información.

   Separar claramente:

   - hechos observables;
   - evidencia derivada;
   - interpretaciones;
   - conclusiones;
   - limitaciones del análisis.

6. Construir el razonamiento.

   Explicar por qué la evidencia conduce a cada conclusión.

   Evitar saltos lógicos y distinguir correlación de interpretación.

7. Formular recomendaciones.

   Priorizar acciones concretas, justificadas y alineadas con el contexto de negocio de VCA.

   Las recomendaciones deben poder ejecutarse o validarse en ciclos posteriores.

8. Redactar el informe ejecutivo.

   El informe debe incluir, como mínimo:

   - contexto del análisis;
   - fuentes de evidencia utilizadas;
   - preparación de datos;
   - análisis;
   - razonamiento;
   - recomendaciones priorizadas;
   - limitaciones y pendientes.

## Comandos base

No aplica ejecución de comandos fija.

Cuando el entorno lo permita, utilizar las capacidades disponibles del workspace y del Data Provider principal para recuperar evidencia y preparar el análisis.

## Criterios de bloqueo

Detener el flujo si:

- no existe definición suficiente del periodo o alcance;
- no hay acceso a evidencia mínima verificable;
- la fuente de datos principal no está disponible;
- faltan referencias contextuales obligatorias;
- el análisis exigiría asumir datos no publicados;
- la salida pretendida mezcla análisis con implementación.

## Definition of Done

La skill se considera completa cuando:

- el caso de uso queda delimitado;
- el contexto relevante queda identificado;
- la evidencia queda trazada hasta la fuente principal;
- el análisis separa hechos, interpretación y recomendación;
- el informe ejecutivo resultante es reutilizable y auditable;
- no se introducen supuestos no verificados.

## Complementos

Esta skill no tiene complementos definidos actualmente.