# AUC-001 Knowledge Methodology Investigation

## 1. Propósito

Reconstruir qué significa Knowledge dentro de AIF Foundation desde una perspectiva metodológica, no semántica.

Esta investigación no propone nuevas capas, no modifica Foundation, no diseña capabilities y no redefine Specifications. Solo observa, a partir de artefactos internos del repositorio, qué propiedades, límites e invariantes están asociados a Knowledge y cómo se diferencia de Evidence, Finding, Insight, Hypothesis, Conclusion y Recommendation.

## 2. Corpus y método

### Corpus primario revisado

- [specs/spec-001-analytical-lifecycle.md](../../specs/spec-001-analytical-lifecycle.md)
- [specs/spec-002-component-boundaries.md](../../specs/spec-002-component-boundaries.md)
- [specs/spec-004-transversal-contracts.md](../../specs/spec-004-transversal-contracts.md)
- [specs/spec-006-documentary-evaluations.md](../../specs/spec-006-documentary-evaluations.md)
- [docs/contracts/evidence.contract.md](../../docs/contracts/evidence.contract.md)
- [docs/contracts/knowledge.contract.md](../../docs/contracts/knowledge.contract.md)
- [docs/contracts/recommendation.contract.md](../../docs/contracts/recommendation.contract.md)
- [docs/handoffs/auc-001-evidence-set.md](../../docs/handoffs/auc-001-evidence-set.md)
- [docs/handoffs/auc-001-evidence-contract.md](../../docs/handoffs/auc-001-evidence-contract.md)
- [docs/handoffs/auc-001-knowledge-set.md](../../docs/handoffs/auc-001-knowledge-set.md)
- [docs/handoffs/auc-001-knowledge-contract.md](../../docs/handoffs/auc-001-knowledge-contract.md)
- [docs/handoffs/auc-001-recommendation-set.md](../../docs/handoffs/auc-001-recommendation-set.md)
- [docs/handoffs/auc-001-executive-report.md](../../docs/handoffs/auc-001-executive-report.md)
- [docs/glosario_terminos.md](../../docs/glosario_terminos.md)
- [docs/evaluations/auc-001-evidence-to-knowledge-independent-research.md](auc-001-evidence-to-knowledge-independent-research.md)
- [docs/evaluations/auc-001-knowledge-construction-comparative-analysis.md](auc-001-knowledge-construction-comparative-analysis.md)
- [analytical_use_cases/meta_lead_quality_analysis.md](../../analytical_use_cases/meta_lead_quality_analysis.md)

### Método

1. Leer las definiciones explícitas de lifecycle, contracts y glosario.
2. Comparar la definición de Knowledge entre specs, contracts, handoffs y evaluations.
3. Distinguir entre artefactos fundacionales y vocabulario de evaluación documental.
4. Localizar inconsistencias semánticas internas.
5. Inferir solo lo que queda respaldado por la evidencia del repositorio.

## 3. Definición metodológica de Knowledge

Dentro de AIF Foundation, Knowledge no es un dato, ni un hallazgo observable, ni una recomendación.

Knowledge es el resultado estabilizado de la fase de Razonamiento: un conjunto estructurado de interpretaciones respaldadas por evidencia, con trazabilidad explícita hacia los hechos observables y con límites declarados sobre lo que no puede afirmarse.

En el corpus actual, Knowledge se describe de forma consistente como un conjunto que incluye:

- insights;
- hipótesis;
- conclusiones;
- prioridades de lectura o prioridades metodológicas;
- riesgos;
- incertidumbres o UNKNOWN;
- y, en algunas definiciones fundacionales, oportunidades.

La propiedad esencial no es que Knowledge sea narrativo, resumido o ejecutivo. La propiedad esencial es que Knowledge esté justificado por evidencia identificable y que su contenido permanezca separado de la producción de nuevas observaciones o de acciones sugeridas.

## 4. Qué puede contener Knowledge

Según las contracts, handoffs y la specification del lifecycle, Knowledge puede contener:

- insights trazables a evidencia concreta;
- hipótesis plausibles pero no necesariamente causales;
- conclusiones dentro del alcance declarado;
- prioridades de lectura o de relevancia metodológica;
- oportunidades identificadas desde el análisis;
- riesgos interpretativos, de negocio o de evidencia;
- incertidumbres, UNKNOWN y limitaciones materiales;
- relaciones explícitas entre cada interpretación y la evidencia que la respalda.

En AUC-001, el Knowledge Set materializado además conserva una selección muy concreta de prioridades de lectura y de riesgos ligados a cobertura, ad-level reasoning, lead-only evidence y spend-only evidence.

## 5. Qué no debería contener Knowledge

La evidencia del repositorio es consistente en que Knowledge no debe contener:

- nueva evidencia;
- reinterpretación de los hechos observables como si fueran datos nuevos;
- recomendaciones o acciones sugeridas;
- planes de ejecución;
- estimaciones operativas no verificadas;
- esfuerzo, dependencias o prioridad de ejecución como si fueran recomendaciones;
- causalidad no demostrada;
- claims fuera del alcance o fuera del modelo autorizado;
- sustitución de limitaciones por inferencias.

El límite clave es este: Knowledge puede interpretar, pero no puede reescribir hechos ni anticipar la fase de Recomendaciones.

## 6. Diferencia entre conceptos

| Término | Función metodológica | Relación con Knowledge |
|---|---|---|
| Evidence | Hechos observables y evidencia derivada, trazables al modelo analítico | Es la base de entrada de Knowledge |
| Finding | Interpretación controlada derivada de observaciones; en la práctica, un puente documental entre observación e interpretación | Puede servir como expresión intermedia, pero no está definido como artefacto fundacional del lifecycle |
| Insight | Interpretación respaldada por evidencia identificable | Es una de las piezas nucleares de Knowledge |
| Hypothesis | Interpretación plausible, condicionada y no necesariamente causal | Es una pieza nuclear de Knowledge, pero con menor compromiso que una conclusión |
| Conclusion | Afirmación respaldada por evidencia y alcance declarado | Es una pieza nuclear de Knowledge cuando la evidencia lo soporta |
| Recommendation | Acción sugerida, justificada y evaluable | Es un artefacto posterior; deriva de Knowledge, no lo compone |

### Observación importante sobre Finding

La evidencia interna no trata Finding como un artefacto independiente del lifecycle fundacional.

En el glosario, Finding es una interpretación controlada derivada de una o más observaciones. En la spec de evaluaciones documentales, Findings son hallazgos observables identificados o interpretación controlada de observaciones, según la capa evaluativa usada. En AUC-001, la palabra aparece también como lenguaje intermedio en reconstrucciones analíticas.

Conclusión metodológica: Finding no es un cuarto pilar del lifecycle comparable a Evidence, Knowledge o Recommendation. Es un término puente, transitorio o documental, según el contexto. Su función más estable es la de interpretar observaciones sin llegar todavía a acción sugerida.

## 7. ¿Knowledge es un artefacto generado o un estado emergente?

La evidencia apunta a una respuesta dual:

1. Operativamente, Knowledge es un artefacto generado por la fase de Razonamiento, porque así lo nombran el lifecycle, los contracts y los handoffs.
2. Metodológicamente, Knowledge es un estado emergente y consolidado que surge de la composición de múltiples insights, hipótesis, conclusiones y prioridades trazables.

Es decir, Knowledge no es una sola frase ni un único finding. Es la estabilización de varias interpretaciones compatibles con la misma base de evidencia.

La forma correcta de leerlo en AIF es esta:

- Evidence produce observaciones y derivaciones;
- Findings o interpretaciones intermedias pueden aparecer como puente;
- Knowledge consolida múltiples interpretaciones en un conjunto coherente;
- Recommendations convierten ese conjunto en acciones sugeridas.

Por tanto, Knowledge es generado como artefacto, pero su contenido es emergente respecto de la agregación y validación de varias operaciones interpretativas.

## 8. Invariantes que debe cumplir Knowledge

Para que algo pueda llamarse Knowledge dentro de AIF, la evidencia del repositorio sugiere que debe cumplir al menos estas invariantes:

- trazabilidad explícita hacia Evidence Contract y Evidence Set;
- dependencia clara de contexto y alcance;
- separación respecto de nueva evidencia;
- declaración de incertidumbres y UNKNOWN;
- prohibición de recomendaciones o planes de ejecución;
- cautela causal cuando solo exista correlación o asociación;
- prioridad justificada por evidencia o limitación, no por intuición gratuita;
- compatibilidad con las limitaciones de cobertura del modelo;
- estabilidad si se repite con el mismo contexto, evidencia y reglas de dominio;
- capacidad de consumirse por Recomendaciones sin reabrir la adquisición de datos.

En el caso de AUC-001, además, Knowledge debe conservar explícitamente las restricciones de cobertura `matched`, `lead_only` y `spend_only`, así como las limitaciones sobre campaign/adset spend attribution, creative asset metadata e impressions/clicks/CTR.

## 9. Inconsistencias encontradas

### 9.1 Knowledge en la spec versus Knowledge en los contracts

La spec del lifecycle presenta Knowledge como “insights, hipótesis priorizadas y conclusiones respaldadas por evidencia”.

El Knowledge Contract transversal amplía esa definición e incluye oportunidades, riesgos e incertidumbres.

El Knowledge Contract de AUC-001 añade además prioridades de lectura, y el Knowledge Set materializado usa un subconjunto de esa formulación.

Conclusión: la definición no es completamente uniforme entre spec, contract y handoff. Hay una ampliación progresiva del concepto.

### 9.2 Knowledge y Recommendations en la spec de componentes

La spec de component boundaries contiene una tabla donde Knowledge Contract aparece descrito como “insights, hipotesis y recomendaciones generados por razonamiento”, pero el cuerpo del contrato y los handoffs de AUC-001 excluyen las recomendaciones de Knowledge.

Conclusión: existe una inconsistencia textual en SPEC-002 entre la tabla de inputs y el comportamiento contractual real. El resto del repositorio trata Knowledge y Recommendations como capas distintas.

### 9.3 Priorización de lectura versus priorización de ejecución

En Knowledge aparecen prioridades de lectura o prioridades metodológicas.

En Recommendation aparecen prioridades de ejecución o de acción.

Conclusión: el repositorio usa el mismo término “prioridad” en dos niveles distintos y eso puede inducir confusión si no se explicita el tipo de prioridad.

### 9.4 Finding como término puente

El glosario define Finding como interpretación controlada de observaciones, mientras que el lifecycle no lo consagra como artefacto fundacional.

Conclusión: Finding existe como noción útil, pero no como entidad estabilizada del core lifecycle al mismo nivel que Evidence, Knowledge o Recommendation.

## 10. Qué estabilizado está Knowledge y qué no

### Bastante estabilizado

- Knowledge es posterior a Evidence y anterior a Recommendation.
- Knowledge contiene interpretaciones trazables, no hechos nuevos.
- Knowledge debe declarar incertidumbre y límites.
- Knowledge no debe contener acciones sugeridas.

### No completamente estabilizado

- El perímetro exacto entre insight, finding, hypothesis y conclusion.
- El peso relativo de priorities, opportunities y risks dentro de Knowledge.
- Si Finding es solo lenguaje evaluativo o una pieza intermedia reusable.
- La frontera entre prioridades de lectura y prioridades de ejecución.
- La granularidad mínima de un Knowledge Set suficientemente completo.

## 11. Conclusión

Knowledge dentro de AIF Foundation es un artefacto metodológico de consolidación interpretativa: un conjunto trazable de insights, hipótesis, conclusiones, prioridades de lectura, riesgos e incertidumbres, generado desde Evidence y destinado a sostener Recomendations sin volver a razonar desde la fuente original.

No es un resumen de datos. No es una lista de findings. No es una colección de recomendaciones.

Si hay que fijar una definición corta, la más fiel a la evidencia del repositorio es esta:

Knowledge es la forma estabilizada que adopta la interpretación de la evidencia cuando esa interpretación ha sido trazada, limitada y separada de la acción.

## 12. Implicación metodológica

Sin proponer aún ninguna solución, la evidencia sugiere que el concepto de Knowledge está suficientemente operativo para trabajar en AUC-001, pero todavía no está completamente normalizado en toda la Foundation.

La semántica básica está clara; la frontera fina entre finding, insight, hypothesis y conclusion todavía requiere estabilización documental si se quiere evitar ambigüedad entre specs, contracts y evaluaciones.