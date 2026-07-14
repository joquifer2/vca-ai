---
name: meta-lead-quality-analysis
description: Ejecuta el caso de uso analítico de calidad de leads de Meta Ads para VCA IA utilizando el lifecycle metodológico de AIF Foundation y BigQuery MCP Server como Data Provider principal.
id: SDD-SKILL-006
user-invocable: true
disable-model-invocation: false
---

# Skill — Meta Lead Quality Analysis

## Propósito

Ejecutar el caso de uso analítico AUC-001 para producir un conjunto canónico de evidencia, conocimiento y recomendaciones sobre la calidad de leads de Meta Ads.

Esta skill orquesta el workflow analítico.

No define la arquitectura del sistema.

No sustituye las Specifications.

No determina la estructura del informe final.

La representación final deberá materializarse mediante las capacidades de Presentation Layer disponibles en el framework.

---

# Cuándo utilizar esta skill

Utilizar esta skill cuando el objetivo sea analizar la calidad de captación de Meta Ads para VCA IA utilizando evidencia procedente de BigQuery.

Aplicarla especialmente ante solicitudes como:

- analiza la calidad de leads de Meta Ads;
- genera el informe ejecutivo de lead quality;
- genera el informe analítico de lead quality;
- revisa eficiencia y calidad de captación;
- evalúa campañas, conjuntos o creatividades.

---

# Responsabilidades

Esta skill es responsable de:

- delimitar correctamente el caso de uso;
- adquirir el contexto necesario;
- obtener evidencia verificable;
- construir conocimiento trazable;
- formular recomendaciones justificadas;
- entregar contenido canónico listo para representación.

No es responsable de:

- seleccionar la Presentation Projection;
- transformar la comunicación según la audiencia;
- redefinir la estructura narrativa del informe;
- reinterpretar conocimiento ya aprobado.

---

# Reglas

- Tratar AIF Foundation como dependencia metodológica.
- Utilizar BigQuery MCP Server como Data Provider principal cuando exista disponibilidad.
- Consultar CCD, FARO, CLARO, KPIs oficiales y docs/context_refs.md antes del análisis.
- No inventar evidencia ni completar datos ausentes mediante inferencias.
- Separar estrictamente:
  - Context Definition
  - Evidence Acquisition
  - Knowledge Generation
  - Recommendation Generation
  - Presentation
- Mantener trazabilidad entre evidencia, conocimiento y recomendaciones.
- Si falta contexto o evidencia suficiente, detener el flujo o solicitar aclaración.
- No convertir esta skill en una Specification ni en una implementación técnica.

---

# Trazabilidad

Esta skill implementa el caso de uso definido en:

analytical_use_cases/meta_lead_quality_analysis.md

Debe permanecer alineada con:

- objetivo;
- alcance;
- criterios de éxito;
- Specifications aprobadas;
- decisiones arquitectónicas vigentes.

---

# Flujo operativo

## 1. Canonicalizar el contexto de ejecución

Determinar:

- periodo;
- alcance;
- definición operativa de calidad;
- audiencia;
- objetivo del análisis.

Resolver ambigüedades únicamente cuando sean materiales.

---

## 2. Cargar contexto oficial

Consultar cuando exista disponibilidad:

- CCD
- FARO
- CLARO
- KPIs oficiales
- docs/context_refs.md
- project_brief.md

---

## 3. Identificar Data Providers

Priorizar:

BigQuery MCP Server.

Identificar únicamente Data Providers adicionales cuando el caso de uso lo requiera.

---

## 4. Adquirir evidencia

Construir el Evidence Set utilizando exclusivamente fuentes verificables.

Como mínimo considerar:

- volumen;
- calidad;
- eficiencia;
- campañas;
- creatividades;
- segmentos;
- evolución temporal;
- limitaciones de cobertura.

---

## 5. Generar conocimiento

Transformar la evidencia en un Knowledge Set aprobado.

Separar claramente:

- hechos observables;
- conocimiento derivado;
- interpretación autorizada;
- limitaciones;
- incertidumbres.

---

## 6. Generar recomendaciones

Construir un Recommendation Set priorizado.

Cada recomendación deberá:

- estar sustentada por conocimiento aprobado;
- conservar trazabilidad;
- ser accionable;
- respetar el contexto del cliente.

---

## 7. Materializar la representación

Una vez estabilizados:

- Context Definition;
- Evidence Set;
- Knowledge Set;
- Recommendation Set;

la representación final deberá delegarse en Presentation Layer.

La representación deberá utilizar:

- la Presentation Projection previamente seleccionada;
- el Communication Context resuelto;
- las restricciones de representación correspondientes.

La materialización no podrá:

- crear evidencia nueva;
- reinterpretar conocimiento;
- modificar prioridades;
- alterar la equivalencia semántica del contenido canónico.

---

# Comandos

No existen comandos obligatorios.

Cuando el entorno lo permita, utilizar las capacidades del Workspace y del Data Provider principal para adquirir evidencia.

---

# Criterios de bloqueo

Detener el flujo cuando:

- el alcance no pueda canonicalizarse;
- no exista evidencia verificable suficiente;
- BigQuery no esté disponible;
- falte contexto obligatorio;
- el análisis requiera asumir datos inexistentes;
- la representación exija modificar contenido canónico.

---

# Definition of Done

La skill se considera completada cuando:

- el Context Definition queda resuelto;
- el Evidence Set queda adquirido y trazado;
- el Knowledge Set queda estabilizado;
- el Recommendation Set queda priorizado;
- la representación final conserva equivalencia semántica;
- el artefacto generado es coherente con la Presentation Projection y el Communication Context;
- no se introducen hechos, interpretaciones ni recomendaciones no verificadas.

---

# Complementos

No existen complementos definidos actualmente.