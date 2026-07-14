# Decisión arquitectónica sobre la transformación de representación guiada por contexto comunicativo de AUC-001

## Metadata

| Field | Value |
|---|---|
| Decision ID | VCA-AUC-001-ARCH-003 |
| Decision Type | Decisión arquitectónica |
| Analytical Use Case | AUC-001 - Meta Lead Quality Analysis |
| Status | Documented |
| Version | 1.0.0 |
| Last Updated | 2026-07-14 |
| Owner | Equipo VCA |
| Scope | Decisión sobre la responsabilidad reusable de Presentation Layer para adaptar la representación del contenido validado a un contexto comunicativo compuesto sin alterar su significado |

---

## Nota de terminología

Los nombres canónicos de artefactos, specs y capacidades se mantienen en inglés cuando así aparecen en el repositorio para conservar trazabilidad y reutilización documental. El resto del texto se redacta en español.

En esta decisión, el contenido aprobado pertenece al núcleo canónico del caso: Evidence Set, Knowledge Set y Recommendation Set.

Presentation Layer no genera ese contenido; lo consume y lo reexpresa bajo condiciones comunicativas distintas.

---

## Decisión

La responsabilidad arquitectónica reusable debe modelarse como una transformación de representación guiada por un **Communication Context** compuesto, aplicado sobre contenido ya validado y sobre una proyección de presentación ya seleccionada.

Esta transformación adapta la forma de comunicar el mismo contenido canónico para una instancia comunicativa concreta sin alterar:

- el significado del contenido;
- la prioridad de las recomendaciones;
- la cobertura de la evidencia;
- la trazabilidad hacia los artefactos fuente;
- la condición de sibling projection de la salida seleccionada.

La transformación no selecciona la proyección.
La transformación no genera conocimiento.
La transformación no genera recomendaciones.
La transformación no canonicaliza el alcance de ejecución.

---

## Justificación de la decisión

El problema arquitectónico no reside en determinar qué proyección existe, ni en decidir qué contenido es válido.

Esos problemas ya se resuelven en otros límites del sistema:

- el alcance de ejecución se canonicaliza antes de congelar el Execution Context;
- la proyección se selecciona a partir del Execution Context canonicalizado;
- el contenido canónico aprobado se conserva en Evidence, Knowledge y Recommendation Sets.

La responsabilidad ausente es la forma en que Presentation Layer adapta la representación del contenido validado a un contexto comunicativo concreto sin modificar su semántica.

Si esa adaptación se confundiera con Projection Selection, la arquitectura mezclaría selección de salida con adaptación de salida.
Si se confundiera con Knowledge Generation o Recommendation Generation, mezclaría representación con producción de contenido.
Si se confundiera con Execution Scope Canonicalization, mezclaría el límite de entrada con el límite de comunicación.

La separación es reusable porque cualquier proyecto derivado puede necesitar el mismo contenido validado expresado de manera distinta según audiencia, propósito, decisión soportada, densidad informativa y trazabilidad visible.

---

## Contexto comunicativo

La transformación no está gobernada únicamente por la audiencia.

La evidencia de AUC-001 muestra que la comunicación depende de un contexto compuesto que debe considerarse de forma conjunta:

- audiencia;
- propósito comunicativo;
- tipo de decisión soportada;
- nivel de abstracción esperado;
- densidad informativa admisible;
- visibilidad requerida de la trazabilidad;
- organización narrativa compatible con la audiencia;
- restricciones de formato que no alteren el significado.

La audiencia sigue siendo relevante, pero no explica por sí sola la transformación completa.
El contexto comunicativo es la unidad arquitectónica adecuada porque describe las condiciones bajo las cuales el mismo contenido debe representarse de forma diferente sin perder equivalencia semántica.

---

## Operación de transformación

La operación no transforma hechos, conclusiones ni prioridades.

La operación transforma propiedades observables de la representación:

- nivel de abstracción;
- densidad informativa;
- jerarquía comunicativa;
- organización narrativa;
- vocabulario de presentación;
- visibilidad de trazabilidad;
- granularidad de soporte por sección o bloque;
- orden de exposición compatible con la audiencia y el propósito.

La operación no transforma:

- el significado del contenido canónico;
- la cobertura observada;
- los estados de UNKNOWN o las limitaciones materiales;
- la prioridad de las recomendaciones;
- la existencia de evidencia o conclusiones ya aprobadas;
- la proyección seleccionada;
- la canonicalización del alcance de ejecución.

---

## Equivalencia semántica

La transformación debe preservar la equivalencia semántica del contenido canónico.

Esto no exige conservar:

- la misma terminología;
- la misma estructura documental;
- la misma secuencia narrativa.

Sí exige conservar:

- el mismo significado autorizado;
- la misma interpretación aprobada;
- la misma prioridad relativa;
- la misma trazabilidad hacia Evidence, Knowledge y Recommendation Sets;
- la misma visibilidad de limitaciones materiales.

La equivalencia semántica no es un detalle de estilo ni un criterio de redacción.
Es un principio arquitectónico reusable porque define la frontera entre una representación válida y una representación que ha alterado el contenido aprobado.

Dentro de esta responsabilidad, su alcance es el siguiente:

- la adaptación puede variar forma, terminología y orden;
- la adaptación no puede variar significado, prioridad ni cobertura;
- la adaptación debe permitir que la salida siga siendo reconocible como representación del mismo contenido canónico.

---

## Relación con Presentation Layer

Presentation Layer sigue siendo la capa que materializa la salida.

La responsabilidad aquí descrita no sustituye a Presentation Layer ni la duplica.
La precisión arquitectónica es otra:

- Presentation Projection Selection determina qué proyección se materializa;
- la transformación de representación guiada por contexto comunicativo determina cómo se expresa esa proyección para una instancia comunicativa concreta.

Presentation Layer consume ambas decisiones de forma encadenada, pero no las fusiona.

La capa permanece como contenedor de representación.
La nueva responsabilidad permanece como función interna de adaptación comunicativa dentro de esa capa, o inmediatamente adyacente a ella, sin convertirse en una capa funcional separada de conocimiento o recomendación.

---

## Límites arquitectónicos

### Fuera de Execution Scope Canonicalization

Esta responsabilidad no resuelve el alcance de ejecución.
No determina periodo, filtros, audiencia de ejecución ni parámetros metodológicos heredados.
Solo actúa una vez que el Execution Context ya está congelado y la salida ya puede ser representada.

### Fuera de Presentation Projection Selection

Esta responsabilidad no decide entre proyección analítica y Executive Report.
La selección de proyección es una decisión anterior y distinta.
La transformación aquí descrita opera sobre la proyección ya seleccionada, no sobre la elección de la proyección.

### Fuera de Knowledge Generation

Esta responsabilidad no produce insights, hipótesis, conclusiones ni riesgos nuevos.
Solo reexpresa conocimiento ya validado.

### Fuera de Recommendation Generation

Esta responsabilidad no formula acciones nuevas, no prioriza recomendaciones y no reordena el set aprobado.
Solo preserva la forma semántica en que esas recomendaciones se comunican.

### Relación con Presentation Layer sin duplicación

Presentation Layer sigue siendo responsable de la salida final.
La nueva responsabilidad no compite con la capa, sino que especifica una condición interna de materialización: la salida debe ser comunicable para un contexto concreto sin perder equivalencia semántica.

Eso evita duplicar la capa y evita convertir la adaptación comunicativa en un mero detalle de formato.

---

## Impacto sobre AIF Foundation

La necesidad observada en vca-ai es reusable y no depende del dominio de Meta Ads.

La razón es estructural:

- cualquier caso de uso analítico puede necesitar presentar el mismo contenido validado a públicos distintos;
- cualquier caso de uso analítico puede exigir diferente nivel de abstracción o densidad informativa;
- cualquier caso de uso analítico puede requerir que la trazabilidad sea explícita para revisión, auditoría o decisión;
- cualquier caso de uso analítico puede necesitar preservar significado mientras cambia la forma de representación.

Por tanto, la responsabilidad es candidata natural a AIF Foundation porque expresa una regla general de representación analítica, no una particularidad de AUC-001.

Lo que vca-ai ha revelado es el patrón reusable: una misma base canónica debe poder expresarse bajo contextos comunicativos diferentes sin romper su semántica.

---

## Validación experimental en vca-ai

La validación experimental de esta decisión debe demostrar, dentro de vca-ai, que:

- el mismo contenido canónico puede representarse de forma distinta bajo contextos comunicativos distintos;
- la variación afecta a forma, densidad, orden y visibilidad, no al significado;
- la salida conserva trazabilidad suficiente para reconstruir el contenido fuente;
- la salida no modifica prioridades, conclusiones ni recomendaciones aprobadas;
- la salida no depende de una nueva selección de proyección;
- la salida no introduce conocimiento nuevo;
- la salida no reabre el alcance de ejecución.

La validación no requiere todavía una Specification ni una implementación.
Solo requiere poder observar que la transformación preserva equivalencia semántica y cambia únicamente la representación comunicativa conforme al contexto declarado.

---

## Implicaciones de la decisión

Esta decisión no define implementación.

No define una Specification.

No define Tasks.

No modifica contracts existentes.

No altera la Foundation metodológica.

Sí establece que la representación de salida debe considerar un contexto comunicativo compuesto y que la equivalencia semántica constituye una regla arquitectónica de control para esa representación.

### Artifact Alignment

Esta decisión arquitectónica no implica por sí misma la modificación de artefactos consumidores (skills, plantillas, documentación operativa u otros). Dicho alineamiento deberá realizarse únicamente después de que la capacidad derivada de esta decisión haya sido implementada y validada experimentalmente dentro de `vca-ai`, conforme a la metodología Specification Driven Development.

---

## Evidencia del repositorio

| Evidencia | Relevancia |
|---|---|
| [AUC-001 Execution Scope Canonicalization](auc-001-execution-scope-canonicalization-architectural-decision.md) | Establece el límite previo de ejecución que no debe confundirse con la adaptación comunicativa de salida. |
| [AUC-001 Presentation Projection Architecture](auc-001-presentation-projection-architectural-decision.md) | Define las proyecciones hermanas y la separación entre conservación canónica y representación. |
| [AUC-001 Presentation Contract](../handoffs/auc-001-presentation-contract.md) | Delimita el contenido aprobado para presentacion y prohíbe nueva evidencia, nueva interpretación y cambios de prioridad. |
| [AUC-001 Executive Output Artifact](../handoffs/auc-001-executive-report.md) | Muestra que la salida ejecutiva consume contenido aprobado sin ampliar el alcance. |
| [SPEC-001 Analytical Lifecycle](../../specs/spec-001-analytical-lifecycle.md) | Define el cierre del ciclo analítico y la representación final del conocimiento ya validado. |
| [SPEC-002 Component Boundaries](../../specs/spec-002-component-boundaries.md) | Refuerza la separación entre consumo de conocimiento y nueva interpretación. |
| [SPEC-004 Transversal Contracts](../../specs/spec-004-transversal-contracts.md) | Sostiene la existencia de contracts transversales para Knowledge, Recommendation y Presentation. |
| [SPEC-010 Presentation Projection Selection](../../specs/spec-010-presentation-projection-selection.md) | Define que la selección de proyección viene del Execution Context canonicalizado y no de Presentation Layer. |
| [docs/glosario_terminos.md](../glosario_terminos.md) | Define trazabilidad, auditabilidad y UNKNOWN como conceptos de control relevantes para la representación. |

---

## Modelo conceptual consolidado

```text
Evidence / Knowledge / Recommendation Sets
                │
                ▼
   Presentation Projection Selection
                │
                ▼
 Communication Context-driven Representation
                │
                ▼
        Presentation Layer Output
```

La selección decide la proyección.
El contexto comunicativo decide la forma de representación.
La equivalencia semántica controla que la forma no altere el contenido aprobado.

---

## Conclusión

La responsabilidad reusable no es solo “cambiar el estilo” de una salida.
La responsabilidad reusable es adaptar una representación ya seleccionada a un contexto comunicativo compuesto, preservando equivalencia semántica, trazabilidad y boundaries metodológicos.

Esta responsabilidad es independiente de Execution Scope Canonicalization, Presentation Projection Selection, Knowledge Generation y Recommendation Generation.

Y es suficientemente general como para aparecer de forma natural en otros casos de uso analíticos construidos sobre AIF Foundation.