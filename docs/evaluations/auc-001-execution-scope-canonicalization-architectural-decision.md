# Decisión arquitectónica sobre canonicalización del alcance de ejecución de AUC-001

## Metadata

| Campo | Valor |
|---|---|
| Decision ID | VCA-AUC-001-ARCH-001 |
| Decision Type | Decisión arquitectónica |
| Analytical Use Case | AUC-001 - Meta Lead Quality Analysis |
| Status | Documented |
| Version | 1.0.0 |
| Last Updated | 2026-07-13 |
| Owner | Equipo VCA |
| Scope | Decisión sobre una capacidad reusable del framework entre Analysis Request y Execution Context |

---

## Nota de terminología

Los nombres canónicos de artefactos, specs y capacidades se mantienen en inglés cuando así aparecen en el repositorio para conservar trazabilidad y reutilización documental. El resto del texto se redacta en español.

---

## Decisión

La capacidad arquitectónica reusable debe denominarse **Execution Scope Canonicalization**.

**Temporal Request Normalization** es el subcaso más preciso dentro de esa capacidad, pero resulta demasiado estrecho para describir la responsabilidad reusable de AIF Foundation.

---

## Justificación de la decisión

El problema observado en AUC-001 fue temporal, pero la responsabilidad arquitectónica es más amplia que el simple análisis de fechas.

El framework parece necesitar una capacidad reusable que canonice el alcance de ejecución antes de que se convierta en una instancia de ejecución congelada. En la práctica, ese alcance puede incluir:

- periodo de análisis;
- alcance de campañas, conjuntos de anuncios y creatividades;
- filtros;
- audiencia;
- solicitud de salida;
- criterio de calidad del lead;
- cualquier otro parámetro específico de la ejecución que deba fijarse antes de los pasos posteriores del ciclo de vida.

Si la capacidad se llamara solo Temporal Request Normalization, el framework estaría describiendo el síntoma y no la responsabilidad. Eso reduciría el valor de reutilización y obligaría a renombrar o duplicar el concepto cuando aparezca una ambigüedad no temporal.

Execution Scope Canonicalization encaja mejor porque preserva la intención arquitectónica reusable de AIF Foundation: normalizar la solicitud humana en una instancia de ejecución canónica, con independencia de que la ambigüedad sea temporal, semántica, operativa o estructural.

---

## Evidencia del repositorio

| Evidencia | Relevancia |
|---|---|
| [AUC-001 Analysis Request](../handoffs/auc-001-analysis-request.md) | Captura la solicitud humana antes de la normalización de ejecución y ya contiene un periodo, un alcance, filtros y una definición de calidad del lead explícitos. |
| [AUC-001 Execution Context](../handoffs/auc-001-execution-context.md) | Congela la instancia operativa después de la normalización, pero no define una responsabilidad reusable de canonicalización. |
| [AUC-001 Context Resolution](../handoffs/auc-001-context-resolution.md) | Resuelve objetivo, periodo, alcance y proveedor previsto, mostrando que el framework ya realiza resolución, pero no un paso explícito de canonicalización. |
| [AUC-001 Context Definition](../handoffs/auc-001-context-definition.md) | Materializa el alcance de ejecución validado y confirma la necesidad de una forma canónica antes de los handoffs posteriores. |
| [SPEC-001 Analytical Lifecycle](../../specs/spec-001-analytical-lifecycle.md) | Exige objetivo, restricciones y fuentes oficiales antes de Discovery, pero no define una responsabilidad distinta para canonicalizar el alcance de ejecución en lenguaje natural. |
| [SPEC-002 Component Boundaries](../../specs/spec-002-component-boundaries.md) | Define la separación de responsabilidades, pero no la regla concreta de normalización previa a la ejecución necesaria aquí. |
| [Context Contract](../contracts/context.contract.md) | Exige objetivo, decisión soportada, alcance de análisis, supuestos, unknowns y trazabilidad, que son entradas para la canonicalización, no la regla de canonicalización en sí. |
| [meta-lead-quality-analysis Skill](../../.github/skills/meta-lead-quality-analysis/SKILL.md) | Exige verificar periodo y alcance, pero no prescribe la canonicalización explícita de la intención del usuario en un alcance de ejecución congelado. |

---

## Interpretación arquitectónica

El fallo no está en Discovery, Analytics ni Reasoning.

El fallo está en el límite entre la solicitud humana y la instancia de ejecución congelada.

Ese límite depende actualmente de la combinación de los artefactos Analysis Request, Execution Context, Context Resolution y Context Definition. Esos artefactos resuelven y congelan la instancia concreta de ejecución, pero no definen una responsabilidad arquitectónica reusable y explícita que establezca:

- qué campos deben resolverse a partir de lenguaje natural;
- qué campos deben canonicalizarse antes de la ejecución;
- qué campos pueden permanecer heredados del AUC más amplio y cuáles deben reinstanciarse para la solicitud específica;
- cómo evitar que un alcance de ejecución previo se filtre en una nueva solicitud.

En otras palabras, los artefactos existentes resuelven una instancia concreta de solicitud. La capacidad ausente definiría la regla reusable para canonicalizar cualquier instancia de solicitud antes de que esos artefactos la congelen.

Por eso, el problema observado es reusable entre proyectos y debería pertenecer a AIF Foundation.

---

## Alcance de la capacidad ausente

Execution Scope Canonicalization debería cubrir las siguientes categorías de normalización de la solicitud:

- alcance temporal;
- alcance de entidades;
- alcance de filtros;
- alcance de audiencia;
- alcance de salida;
- alcance de decisión;
- alcance de restricciones.

Temporal Request Normalization sigue siendo un subcaso válido dentro de esa capacidad más amplia, pero no el nombre principal.

### Reglas de canonicalización

La capacidad debe distinguir entre dos categorías de parámetros:

| Categoría | Definición | Tratamiento por defecto |
|---|---|---|
| Parámetros de ejecución | Parámetros que definen la instancia concreta de ejecución y pueden variar entre corridas del mismo AUC. Pueden provenir de la solicitud del usuario o resolverse durante la canonicalización. | Deben canonicalizarse de forma explícita y quedar congelados en el Execution Context |
| Parámetros metodológicos | Parámetros heredados del AUC, la Skill o los artefactos fundacionales salvo modificación explícita | Deben heredarse automáticamente y solo cambiar si la solicitud lo indica de forma inequívoca |

En el caso validado por AUC-001, el periodo constituye un parámetro de ejecución y, cuando la solicitud no determine de forma inequívoca su alcance, deberá resolverse explícitamente antes de construir el Execution Context.

Regla operativa:

- si está completamente definido, no preguntar;
- si puede resolverse mediante una regla documentada, resolver;
- si sigue siendo materialmente ambiguo, preguntar.

### Regla de precedencia

Cuando exista conflicto entre los parámetros de ejecución derivados de la solicitud actual y los valores heredados de ejecuciones anteriores, prevalecerán siempre los parámetros de la solicitud actual una vez canonicalizados.

Los parámetros metodológicos se heredarán automáticamente del Analytical Use Case, la Skill y los artefactos fundacionales. Solo dejarán de heredarse cuando la solicitud requiera explícitamente un comportamiento diferente y dicho cambio sea compatible con el alcance del Analytical Use Case. En caso contrario, deberá resolverse como un cambio de alcance o un nuevo caso de uso.

La señal de campaña, el criterio de calidad del lead y el alcance de entidades pertenecen por defecto a la categoría de parámetros metodológicos cuando ya están fijados por el AUC y sus artefactos asociados. Solo deben volver a resolverse si la solicitud expresa una modificación explícita, una restricción nueva o un conflicto documental relevante.

Con esa regla, la canonicalización evita sobrecargar la solicitud con preguntas innecesarias y reduce la posibilidad de reheredar periodos o filtros de ejecuciones previas sin intención documental.

---

## Impacto en AIF Foundation

Esta capacidad parece ser una candidata sólida a necesidad de nivel Foundation, no una particularidad de vca-ai.

La evidencia del repositorio muestra que vca-ai puso de manifiesto la brecha, pero la brecha en sí es genérica:

- cualquier proyecto derivado puede recibir una solicitud expresada en lenguaje natural;
- cualquier proyecto derivado puede necesitar que la solicitud se normalice antes de la ejecución;
- cualquier proyecto derivado puede sufrir filtración de alcance si el paso de canonicalización es implícito.

Eso hace que la capacidad sea plausiblemente reusable y, por tanto, apta para AIF Foundation, pendiente de una validación más amplia fuera de este caso único.

---

## Ubicación arquitectónica

La capacidad debe situarse conceptualmente entre la solicitud humana y la instancia de ejecución congelada, como parte de la fase de Contexto del ciclo de vida.

Debe reforzar el ciclo de vida existente y el límite de contexto, en lugar de sortearlos.

A nivel de arquitectura, la evolución más natural es:

1. ampliar las reglas de la fase Contexto en [SPEC-001 Analytical Lifecycle](../../specs/spec-001-analytical-lifecycle.md);
2. reforzar el [Context Contract](../contracts/context.contract.md) para exigir la canonicalización explícita del alcance de ejecución;
3. mantener sin cambios los handoffs posteriores, porque el objetivo es mejorar el límite de entrada y no rediseñar Discovery ni Reasoning.

---

## Implicaciones de la decisión

Esta decisión no define implementación.

No define una nueva specification.

No define contratos ni skills.

Sí establece que el framework debe tratar la canonicalización del alcance de ejecución como una responsabilidad reusable de primera clase, con la normalización temporal como instancia específica de esa responsabilidad.

---

## Validación experimental en vca-ai

vca-ai adoptará esta responsabilidad de forma experimental para validar la evolución arquitectónica identificada por el Architect Agent.

La validación experimental consistirá en aplicar la canonicalización del alcance de ejecución entre la Analysis Request y el Execution Context para nuevas solicitudes analíticas, con el objetivo de verificar que el framework:

- resuelve de forma explícita el alcance de ejecución antes de congelarlo;
- evita la reutilización implícita de periodos o filtros heredados de corridas previas;
- mantiene trazabilidad entre solicitud humana, alcance canónico y ejecución congelada;
- preserva la separación entre la validación experimental en vca-ai y la futura adopción canónica en AIF Foundation.

Esta validación experimental no altera el estado de SPEC-001, SPEC-002 ni del Context Contract como artefactos fundacionales; solo ejercita la responsabilidad arquitectónica propuesta en el flujo documental de vca-ai.

---

## Recomendación

Si AIF Foundation evoluciona formalmente, la arquitectura debería usar esta jerarquía de nombres:

- **Capacidad principal:** Execution Scope Canonicalization
- **Subcaso específico:** Temporal Request Normalization

Esta nomenclatura preserva la reutilización, evita la sobreespecialización y mantiene el framework extensible para futuras ambigüedades de la solicitud más allá de las expresiones temporales.

---

## Riesgos residuales si no se aborda

| Riesgo | Impacto |
|---|---|
| Filtración de alcance entre ejecuciones | Un análisis posterior puede heredar un periodo o alcance de una ejecución anterior. |
| Ajustar el framework en exceso a expresiones temporales | Futuras ambigüedades en audiencia, alcance de entidades o filtros pueden requerir un concepto nuevo. |
| Comportamiento de normalización implícito | Distintos equipos o agentes pueden canonicalizar las solicitudes de forma inconsistente. |
| Acoplamiento oculto entre solicitud y artefactos de ejecución | El framework puede parecer consistente mientras sigue apoyándose en convenciones no declaradas. |

---

## Conclusión

El concepto arquitectónico reusable debe ser **Execution Scope Canonicalization**.

Este es el nombre más general y, por tanto, el más alineado con Foundation.

**Temporal Request Normalization** sigue siendo la mejor etiqueta descriptiva para la parte temporal concreta del problema, pero no es suficiente como capacidad paraguas para AIF Foundation.
