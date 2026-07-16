# Decisión arquitectónica sobre las proyecciones de presentación de AUC-001

## Metadata

| Campo | Valor |
|---|---|
| Decision ID | VCA-AUC-001-ARCH-002 |
| Decision Type | Decisión arquitectónica |
| Analytical Use Case | AUC-001 - Meta Lead Quality Analysis |
| Status | Documented |
| Version | 1.0.0 |
| Last Updated | 2026-07-13 |
| Owner | Equipo VCA |
| Scope | Decisión sobre la responsabilidad reusable de Presentation Layer para proyectar conocimiento validado hacia distintas audiencias |

---

## Nota de terminología

Los nombres canónicos de artefactos, specs y capacidades se mantienen en inglés cuando así aparecen en el repositorio para conservar trazabilidad y reutilización documental. El resto del texto se redacta en español.

En esta decisión, la conservación del contenido aprobado pertenece al núcleo canónico de conocimiento del caso: Evidence Set, Knowledge Set y Recommendation Set.

Presentation Layer no conserva ese contenido; lo consume y lo proyecta hacia audiencias distintas.

---

## Decisión

La capacidad arquitectónica reusable debe modelarse como una Presentation Layer que genera dos proyecciones paralelas a partir del mismo conocimiento validado:

- **Proyección analítica** como representación analítica;
- **Executive Report** como representación ejecutiva.

Ambas proyecciones consumen exactamente el mismo material aprobado y trazable.

Ninguna de las dos debe derivarse de la otra.

Ninguna de las dos debe reintroducir evidencia, reinterpretar conclusiones ni reordenar prioridades.

---

## Justificación de la decisión

El problema arquitectónico no está en la conservación del contenido aprobado.

Esa conservación ya se resuelve en el núcleo canónico mediante Evidence, Knowledge y Recommendation Sets.

La responsabilidad ausente es la forma en que Presentation Layer transforma ese núcleo validado en salidas diferenciadas por audiencia sin alterar su significado.

Si el sistema modelara solo un Output Artifact genérico, tendería a mezclar dos necesidades distintas:

- una representación analítica orientada a lectura técnica, revisión o auditoría;
- una representación ejecutiva orientada a decisión y comunicación de negocio.

Separar esas dos proyecciones dentro de una misma Presentation Layer evita que el Executive Report herede innecesariamente la estructura técnica de la proyección analítica, pero sin crear dos capas de responsabilidad completamente independientes.

La arquitectura resultante es reusable porque cualquier proyecto derivado puede necesitar la misma base validada y dos formas de salida distintas según audiencia.

---

## Evidencia del repositorio

| Evidencia | Relevancia |
|---|---|
| [AUC-001 Presentation Contract](/docs/handoffs/auc-001-presentation-contract.md) | Delimita contenido aprobado para la capa de presentación, prohíbe nueva evidencia, nueva interpretación y cambios de prioridad. |
| [AUC-001 Executive Output Artifact](/docs/handoffs/auc-001-executive-report.md) | Muestra la salida ejecutiva actual y confirma que consume el Presentation Contract sin ampliar el alcance. |
| [AUC-001 Presentation and Output Documentary Evaluation](/docs/evaluations/auc-001/validations/auc-001-presentation-output-evaluation.md) | Evalúa que la salida actual es coherente, trazable y boundary-compliant, aunque todavía usa un concepto genérico de Output Artifact. |
| [AUC-001 Execution Scope Canonicalization](/docs/decisions/auc-001/auc-001-execution-scope-canonicalization-architectural-decision.md) | Demuestra que el repositorio ya adopta decisiones arquitectónicas reuseables para canonizar responsabilidades antes de su materialización documental. |
| [SPEC-001 Analytical Lifecycle](/specs/spec-001-analytical-lifecycle.md) | Define el cierre del ciclo analítico y la generación de salida sin reabrir la obtención de evidencia. |
| [SPEC-002 Component Boundaries](/specs/spec-002-component-boundaries.md) | Refuerza la separación entre componentes y evita mezclar consumo de conocimiento con nueva interpretación. |
| [SPEC-004 Transversal Contracts](/specs/spec-004-transversal-contracts.md) | Sostiene la existencia de contracts transversales para Knowledge, Recommendation y Presentation. |

---

## Interpretación arquitectónica

El núcleo canónico define qué contenido es válido.

Presentation Layer define cómo ese contenido se representa para una audiencia concreta.

La distinción importante es esta:

- el núcleo canónico preserva contenido autorizado y trazabilidad;
- Presentation Layer produce una representación analítica o ejecutiva de ese contenido.

La proyección analítica no debe interpretarse como una segunda capa de conservación.
Debe interpretarse como una representación analítica del mismo conocimiento validado.

La distincion interna entre formatos, vistas o submodos de la proyeccion analitica queda deliberadamente pospuesta hasta que exista evidencia experimental adicional que la justifique.

---

## Modelo de salida propuesto

```text
Evidence Set
Knowledge Set
Recommendation Set
        │
        ▼
 Presentation Layer
        │
 ┌──────┴────────┐
 │               │
 ▼               ▼
Analytical     Executive
Projection        Report
```

Las dos proyecciones consumen el mismo conocimiento validado.

Las dos mantienen trazabilidad hacia el núcleo canónico.

Las dos pueden coexistir sin encadenarse secuencialmente.

---

## Responsabilidades de cada componente

| Componente | Responsabilidad |
|---|---|
| Evidence Set | Preservar la evidencia observable y sus límites. |
| Knowledge Set | Transformar evidencia en insights, hipótesis, conclusiones, prioridades, riesgos e incertidumbres trazables. |
| Recommendation Set | Convertir conocimiento en acciones sugeridas justificadas y priorizadas. |
| Presentation Layer | Seleccionar, estructurar y proyectar el contenido validado hacia una audiencia concreta sin crear nuevo razonamiento. |
| Proyección analítica | Exponer una representación analítica fiel al material validado, con trazabilidad suficiente para revisión y auditoría. |
| Executive Report | Exponer una representación ejecutiva sintética, orientada a decisión y comunicación de negocio. |

---

## Relaciones y proyecciones

Presentation Layer consume los tres conjuntos canónicos y materializa dos proyecciones conceptuales:

- una proyección analítica, que privilegia fidelidad, detalle y trazabilidad;
- una proyección ejecutiva, que privilegia síntesis, legibilidad y foco decisional.

La selección entre la proyección analítica y Executive Report no es una decisión propia de Presentation Layer.

La selección entre la proyección analítica y Executive Report viene determinada por el Execution Context previamente canonicalizado, utilizando atributos como la audiencia, el propósito del artefacto y el tipo de decisión que debe soportarse.

Presentation Layer únicamente materializa la proyección solicitada por ese contexto.

Ambas proyecciones deben respetar las mismas restricciones de entrada:

- no agregar evidencia nueva;
- no reescribir conclusiones;
- no alterar prioridades;
- no introducir recomendaciones nuevas;
- no ocultar limitaciones materiales.

---

## Dependencias

| Dependencia | Tipo | Observación |
|---|---|---|
| Evidence Set | Funcional | Base de contenido observable. |
| Knowledge Set | Funcional | Base de interpretación ya validada. |
| Recommendation Set | Funcional | Base de acciones sugeridas aprobadas. |
| Presentation Contract | Contractual | Delimita contenido autorizado para ambas proyecciones. |
| SPEC-001 | Fundacional | Cierra la fase analítica y habilita la salida. |
| SPEC-002 | Fundacional | Mantiene separación de responsabilidades. |
| SPEC-004 | Fundacional | Formaliza contracts transversales. |

---

## Restricciones técnicas

- La proyección ejecutiva no debe heredar la estructura técnica completa de la proyección analítica.
- La proyección analítica no debe convertirse en un segundo mecanismo de conservación.
- El núcleo canónico debe seguir siendo la única fuente de verdad para contenido aprobado.
- La terminología usada en los artefactos debe preservar trazabilidad con los nombres canónicos del repositorio.

---

## Riesgos técnicos

| Riesgo | Severidad | Impacto |
|---|---|---|
| Tratar la proyección analítica como un mecanismo de conservación | Important | Duplica responsabilidades y diluye el rol del núcleo canónico. |
| Derivar Executive Report de la proyección analítica | Important | Introduce acoplamiento estructural innecesario y aumenta el riesgo de divergencia. |
| Mantener un único Output Artifact genérico | Important | Mezcla dos propósitos de salida con necesidades de audiencia distintas. |
| Ocultar limitaciones en la proyección ejecutiva | Important | Reduce trazabilidad y puede inducir interpretación incorrecta. |

---

## Alternativas consideradas

### 1. Un único Output Artifact genérico

Ventaja: máxima simplicidad nominal.

Inconveniente: no diferencia la audiencia ni la función de la salida.

Riesgo: la estructura ejecutiva termina heredando forma técnica innecesaria.

### 2. Executive Report derivado de la proyección analítica

Ventaja: flujo lineal fácil de entender.

Inconveniente: convierte la proyección analítica en intermediario estructural.

Riesgo: divergencia semántica y acoplamiento documental entre salidas.

### 3. Presentation Layer con dos proyecciones paralelas desde el núcleo canónico

Ventaja: separa conservación de representación y minimiza acoplamiento.

Ventaja: mantiene trazabilidad y reutilización en AIF Foundation.

Inconveniente: exige disciplina terminológica y control explícito de límites.

Esta es la opción seleccionada.

---

## Decisiones arquitectónicas propuestas

1. Considerar Evidence, Knowledge y Recommendation Sets como el lugar de conservación canónica del contenido aprobado.
2. Modelar Presentation Layer como una capa de proyección y no de conservación.
3. Nombrar la salida analítica como proyección analítica, sin subdivisiones vigentes adicionales.
4. Mantener Executive Report como proyección ejecutiva independiente.
5. Evitar cualquier dependencia secuencial entre la proyección analítica y Executive Report.

---

## Impacto sobre AIF Foundation

Esta decisión parece reusable a nivel Foundation.

La necesidad no es específica de vca-ai: cualquier proyecto derivado puede requerir una salida analítica y una salida ejecutiva construidas sobre el mismo núcleo validado.

La evidencia obtenida en `vca-ai` sugiere que esta responsabilidad es candidata a ser incorporada a `AIF Foundation` una vez completada su validación experimental.

---

## Siguiente paso recomendado

Usar esta terminología como base conceptual para cualquier futura formalización documental de Presentation Layer:

- núcleo canónico para conservación;
- proyección analítica para representación analítica;
- Executive Report para representación ejecutiva.

Si el repositorio necesitara formalizarlo más adelante, la ampliación debería hacerlo sin reintroducir la idea de conservación dentro de Presentation Layer.

---

## Conclusión

La terminología correcta para la responsabilidad ausente no es una proyección de conservación analítica.

La responsabilidad reusable es una **Presentation Layer** que produce una **proyección analítica** y un **Executive Report** como proyecciones paralelas desde el mismo contenido validado.

La conservación pertenece al núcleo canónico.

Presentation Layer pertenece a la representación.