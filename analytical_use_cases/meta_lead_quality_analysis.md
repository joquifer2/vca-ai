---
type: analytical-use-case
id: AUC-001
name: Meta Lead Quality Analysis
status: Proposed
priority: High
---

# Analytical Use Case · Lead Quality Analysis

## Objetivo

Definir el primer caso de uso analítico de VCA IA (AUC-001) que servirá para validar la arquitectura analítica del sistema, el lifecycle definido por AIF Foundation y el BigQuery MCP Server como Data Provider principal.

---

# Problema de negocio

Actualmente el análisis periódico de calidad de leads, scoring y eficiencia de inversión en Meta Ads se realiza mediante un único prompt monolítico.

Aunque el proceso produce resultados satisfactorios, concentra en una única ejecución responsabilidades que deberían permanecer desacopladas, dificultando su reutilización, evolución y trazabilidad.

---

# Objetivo del caso de uso

Construir una capacidad analítica que permita generar un informe ejecutivo sobre la calidad de los leads captados mediante Meta Ads, separando claramente:

- contexto;
- obtención de evidencia;
- preparación de datos;
- análisis;
- razonamiento;
- recomendaciones;
- construcción del informe.

---

# Usuarios

## Principal

Analista de negocio.

## Secundarios

- Dirección.
- Responsable de Marketing.
- Especialistas de Meta Ads.
- Equipo Comercial.

---

# Contexto requerido

La capacidad analítica deberá utilizar, cuando resulte necesario:

- Client Context Document (CCD).
- FARO.
- CLARO.
- KPIs oficiales.
- Knowledge Base del proyecto.

---

# Data Providers previstos

Como fuente principal de evidencia se utilizará:

- BigQuery MCP Server.

Podrán incorporarse otros Data Providers compatibles cuando resulte necesario.

---

# Resultado esperado

El resultado del análisis será un informe ejecutivo que permita comprender:

- volumen de captación;
- calidad de los leads;
- eficiencia económica;
- campañas y creatividades más eficientes;
- oportunidades de optimización;
- recomendaciones priorizadas.

---

# Criterios de éxito

El caso de uso se considerará validado cuando la skill meta-lead-quality-analysis sea capaz de producir un informe equivalente o superior al proceso actual, manteniendo la trazabilidad entre contexto, evidencia, razonamiento y recomendaciones.

---

# Próximo paso

Este caso de uso deberá servir como entrada para la skill meta-lead-quality-analysis y para futuras iteraciones de validación del caso de uso dentro de VCA IA.

No constituye una specification ni una implementación.

---

# Evidencia de validación

## Registro

- Fecha: 2026-07-11
- Evidencia: la skill [meta-lead-quality-analysis](../.github/skills/meta-lead-quality-analysis/SKILL.md) queda alineada con este caso de uso y puede utilizarse para ejecutar y validar el primer análisis de VCA IA.
- Resultado: validación documental y trazable del caso de uso AUC-001 como primer caso analítico del proyecto.
- Referencias de soporte:
	- [docs/context_refs.md](../docs/context_refs.md)
	- [project_brief.md](../project_brief.md)
	- [meta-lead-quality-analysis skill](../.github/skills/meta-lead-quality-analysis/SKILL.md)