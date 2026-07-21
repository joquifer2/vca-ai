# Análisis arquitectónico del Contrato de Producto Analítico P01 de AUC-001

## Metadatos

| Campo | Valor |
|---|---|
| Document ID | VCA-AUC-001-P01-ARCH-ANALYSIS-001 |
| Tipo de documento | Architectural Analysis / Decision Memo |
| Agente | Architect Agent |
| Caso de uso padre | AUC-001 - Meta Lead Quality Analysis |
| Fecha | 2026-07-21 |
| Estado | Input arquitectónico propuesto para Specification |
| Fase solicitada | P01 |
| Identidad formal recomendada | AUC-001-P01 - Analytical Product Contract Definition |
| Alcance | Definir el límite arquitectónico de un Analytical Product Contract específico de AUC-001 antes de Specification |

Este memo no es una Specification, task plan, gate, implementación de runtime ni ejecución analítica.

No se ejecutó BigQuery. No se modificó ningún output histórico. Este memo no promueve ninguna capacidad a AIF Foundation.

---

## 1. Estado reconstruido

### 1.1 Estado vigente verificado

El estado canónico vigente es:

```text
P0 PASS WITH RESIDUAL OBSERVATIONS - READY FOR P01
```

Hechos verificados:

| Hecho | Estado | Fuente |
|---|---|---|
| AUC-001 sigue activo y validado | Verificado | `analytical_use_cases/auc-001/README.md`; `analytical_use_cases/meta_lead_quality_analysis.md` |
| El ciclo experimental original permanece cerrado | Verificado | `gates/auc-001-experimental-closure-gate.md`; README de AUC-001 |
| SPEC-012 fue ejecutada como AUC-001-PCI-001 | Verificado | `specs/spec-012-auc-001-canonical-cost-quality-model.md`; README de AUC-001 |
| SPEC-013 está aceptada y su brecha de persistencia física fue cerrada por PCI-002 | Verificado | `specs/spec-013-auc-001-structured-reconciliation-output.md`; gates de PCI-002 |
| El Exit Gate de AUC-001-PCI-002 es PASS | Verificado | `gates/auc-001-pci-002-exit-gate.md` |
| El gate final de P0 está listo para P01 | Verificado | `gates/auc-001-p0-operational-closure-gate.md`; validación QA final |
| El runtime físico existe y es consumible | Verificado | `outputs/auc-001/pci-002/2026-06-30/execution/runtime-output.json` |
| Los outputs históricos permanecen protegidos y no sobrescritos | Verificado | Validación QA final de P0; QA físico de PCI-002 |

### 1.2 Baseline técnico actual

Los siguientes elementos deben tratarse como estables para P01 salvo que Specification descubra una contradicción material:

- Execution Scope Canonicalization.
- Presentation Projection Selection.
- Communication Context Representation Transformation.
- Modelo canónico coste-calidad de SPEC-012.
- Structured Reconciliation Output de SPEC-013.
- Familia y versionado del schema de runtime output.
- Persistencia física.
- Lineage y packaging.
- Adapter y protección de namespaces.
- Proceso de QA físico.

P01 no debe introducir mejoras de runtime, persistencia, packaging o modelo técnico por defecto.

### 1.3 Estado de la evidencia histórica

El prompt histórico y los informes históricos son referencias válidas de comparación, no evidencia de negocio vigente ni expected values.

Uso permitido:

- recuperar expectativas funcionales del producto;
- comparar cobertura analítica y utilidad;
- identificar capacidades históricas con valor real;
- detectar brechas entre el producto actual y el producto objetivo.

Uso prohibido:

- tratar cifras históricas como expected values;
- reutilizar findings históricos como nuevo Knowledge;
- copiar la estructura del prompt histórico como plantilla normativa;
- saltarse la cadena canónica Context -> Evidence -> Knowledge -> Recommendations -> Presentation.

---

## 2. Problema arquitectónico

### 2.1 Formulación del problema

AUC-001 tiene ahora una arquitectura, una trazabilidad y una consumibilidad de runtime más sólidas que el proceso histórico basado en prompt. Sin embargo, un output de AUC-001 puede ser formalmente correcto y aun así resultar funcionalmente insuficiente como producto analítico.

La brecha no es principalmente una brecha de runtime.

La brecha consiste en que ningún contrato vigente define todavía el valor mínimo de producto que AUC-001 debe entregar a sus consumidores analíticos y ejecutivos.

### 2.2 Diagnóstico por capa

| Área | Diagnóstico |
|---|---|
| Evidence | Los contratos actuales definen evidencia observable, coverage states, tratamiento de UNKNOWN y trazabilidad, pero no el conjunto completo de preguntas de negocio que el producto debe cubrir satisfactoriamente o marcar explícitamente como no disponibles. |
| Knowledge | El Knowledge Contract exige insights, hipótesis, conclusiones y prioridades trazables. El Runbook exige investigación analítica y narrativa, pero no existe una matriz de suficiencia de producto que determine si el Knowledge Set responde a las preguntas necesarias del producto. |
| Recommendations | El Recommendation Contract exige acciones justificadas y trazables. No exige que las recomendaciones se formulen como experimentos medibles ni define umbrales de accionabilidad a nivel de producto. |
| Presentation | SPEC-010, SPEC-011 y el Presentation Contract gobiernan proyección, representación y equivalencia semántica. No deciden qué contenido analítico debe existir antes de representar. |
| Producto | Capa ausente. AUC-001 necesita un contrato local de producto que defina qué hace que el producto analítico sea útil, suficientemente completo, comparable y apto para soportar decisiones. |

### 2.3 Vacío verificado

Los contratos existentes son contratos de frontera. Definen qué puede producir cada capa y qué no debe mezclar.

No responden a estas preguntas:

- qué preguntas de negocio de AUC-001 son obligatorias, condicionales o no disponibles;
- qué evidencia requiere cada pregunta;
- qué desgloses, tablas e interpretaciones son exigibles cuando existe evidencia;
- cuándo un producto está completo, parcialmente completo o no es apto para una proyección determinada;
- cómo comparar el producto actual con el valor del producto histórico sin copiar sus cifras;
- cuándo las recomendaciones deben expresarse como experimentos medibles.

Este es el vacío contractual que permite que un informe sea metodológicamente válido y, aun así, demasiado débil para su rol como producto analítico.

---

## 3. Capacidades existentes relevantes

| Capacidad | Rol actual | Límite para P01 |
|---|---|---|
| Execution Scope Canonicalization | Congela el alcance de la solicitud antes de la ejecución | P01 puede depender de ella; no debe redefinirla. |
| SPEC-010 Presentation Projection Selection | Selecciona proyección Analytical o Executive desde el contexto canónico | P01 debe respetar las proyecciones hermanas; la completitud del producto precede a la proyección. |
| SPEC-011 Communication Context Representation Transformation | Adapta la representación sin deriva semántica | P01 puede definir contenido común de producto, mientras SPEC-011 gobierna cómo se expresa. |
| Analytical Narrative | Construye una tesis integrada desde el Knowledge estabilizado | P01 puede exigir suficiencia narrativa, pero no como reescritura de Presentation. |
| SPEC-012 | Define modelo coste-calidad canónico, coverage states, métricas y blockers | P01 debe consumirla como baseline técnico/de evidencia. |
| SPEC-013 | Hace consumible la reconciliación de runtime sin Markdown | P01 debe consumir el runtime estructurado, no cambiar su schema. |
| Analytical Contract de AUC-001 | Lista preguntas y capacidades analíticas | P01 debe especializar suficiencia de producto, no duplicar capacidades analíticas operativas. |
| Evidence/Knowledge/Recommendation Contracts | Preservan separación y trazabilidad | P01 debe añadir expectativas de producto transversales sin fusionar capas. |

---

## 4. Comparación funcional requerida para Specification

Specification debe comparar tres objetos:

1. Prompt histórico e informes históricos.
2. Producto actual.
3. Producto objetivo.

La comparación no debe limitarse a contar secciones.

### 4.1 Dimensiones de comparación

Specification debe comparar, como mínimo:

- preguntas de negocio respondidas;
- profundidad analítica;
- utilidad y riqueza de las tablas;
- análisis de concentración;
- comparativas temporales;
- comparativas entre segmentos;
- identificación de patrones;
- calidad interpretativa;
- formulación y contraste de hipótesis;
- robustez y limitaciones;
- separación entre Evidence, Knowledge e interpretación;
- accionabilidad de las recomendaciones;
- transformación de recomendaciones en experimentos medibles;
- calidad de la narrativa analítica;
- legibilidad para el destinatario;
- trazabilidad.

### 4.2 Fuentes para la comparación

| Fuente | Uso en P01 |
|---|---|
| `docs/corpus/auc-001/prompt_historico_monolitico.md` | Referencia funcional histórica únicamente. |
| `docs/corpus/auc-001/informe_calidad_leads_scoring_20260701.md` | Referencia histórica de valor de producto únicamente. |
| `docs/corpus/auc-001/informe_calidad_leads_20260510.md` | Referencia histórica de valor de producto solo si Specification necesita un segundo ejemplo. |
| `outputs/auc-001/2026-06-30/analytical-report.md` | Referencia del producto analítico validado actual; no fuente de nuevo Knowledge. |
| `outputs/auc-001/pci-002/2026-06-30/` | Referencia del runtime/package estructurado actual; no definición por sí misma del producto objetivo. |
| Validaciones de Knowledge Depth y Analytical Narrative | Evidencia de método y narrativa. |
| Validaciones QA de P0/PCI-002 | Evidencia de estado y cierre técnico. |

### 4.3 Capacidades históricas con valor real

El prompt/informe histórico contenía capacidades de producto que merece evaluar:

- conexión directa entre preguntas de negocio y secciones;
- análisis de variables con interpretación;
- relaciones entre variables y combinaciones de señales;
- vistas de eficiencia por creatividad y campaña;
- lectura de evolución temporal;
- comparación por plataforma;
- concentración y matrices de decisión;
- interpretación estratégica para stakeholders senior;
- implicaciones operativas para optimización de Meta y CAPI;
- recomendaciones organizadas por prioridad y siguientes pasos.

### 4.4 Componentes históricos que no deben recuperarse

No deben recuperarse como requisitos del contrato de producto:

- ingesta automática de CSV y normalización flexible de columnas;
- joins automáticos entre datasets arbitrarios;
- scoring inferido cuando existen reglas oficiales FARO/scoring o cuando falta evidencia;
- estructura rígida obligatoria de más de 20 secciones Markdown;
- CPQL/CPHQL sin universo y coverage autorizados actualmente;
- afirmaciones de estado operativo CAPI sin evidencia vigente;
- reglas operativas para Sales/CRM/automatización salvo que estén soportadas por contrato y evidencia;
- acumulación monolítica de roles como sustituto de boundaries arquitectónicos.

---

## 5. Boundary recomendado

### 5.1 Tipo de contrato recomendado

Recomendación:

```text
Crear un Analytical Product Contract específico de AUC-001 como nueva categoría contractual local experimental dentro de AUC-001.
```

No debe ser todavía un contrato de Foundation.

No debe implementarse como una simple extensión del Analytical Contract o del Presentation Contract existentes.

### 5.2 Responsabilidad

El Analytical Product Contract debe gobernar la suficiencia de producto de AUC-001:

- qué preguntas analíticas debe responder el producto o marcar explícitamente como no disponibles;
- qué evidencia y desgloses requiere cada pregunta;
- qué tablas son exigibles cuando aplican;
- qué interpretaciones son exigibles cuando la evidencia las soporta;
- cómo Knowledge y Recommendations deben cubrir las preguntas de negocio del producto;
- cuándo el producto está completo, parcial, no aplicable o no disponible;
- cómo las proyecciones analítica y ejecutiva comparten el mismo núcleo de producto y difieren solo en representación.

### 5.3 Entradas

El contrato debe consumir:

- Stabilized Context Definition.
- Evidence Set.
- Knowledge Set.
- Recommendation Set.
- Outputs de runtime/reconciliación de SPEC-012 cuando apliquen.
- Coverage states, UNKNOWNs, limitaciones y blockers.
- Presentation Projection y Communication Context solo como restricciones downstream, no como generadores de contenido de producto.

### 5.4 Salidas gobernadas

El contrato debe gobernar:

- estado de completitud del producto analítico;
- matriz de cobertura;
- cobertura obligatoria por pregunta analítica;
- tablas y desgloses requeridos;
- cobertura requerida de Knowledge;
- readiness de recomendaciones/experimentos;
- núcleo de producto neutral a la proyección;
- requisitos mínimos de visibilidad específicos por proyección.

### 5.5 Lo que no puede hacer

El contrato no puede:

- adquirir evidencia;
- crear nuevo Evidence, Knowledge o Recommendations;
- saltarse las reglas de BigQuery MCP;
- redefinir SPEC-012 o SPEC-013;
- decidir la proyección de presentación;
- transformar la representación;
- convertir informes históricos en expected values;
- promoverse a AIF Foundation.

### 5.6 Relación con contratos existentes

| Contrato existente | Relación |
|---|---|
| Analytical Contract | Define capacidades analíticas y límites del modelo preparado. El Product Contract define la suficiencia del producto resultante. |
| Evidence Contract | Define integridad de la evidencia observable. El Product Contract exige cobertura de evidencia por pregunta analítica. |
| Knowledge Contract | Define razonamiento válido. El Product Contract exige cobertura de Knowledge por pregunta de producto. |
| Recommendation Contract | Define acciones trazables. El Product Contract puede exigir recomendaciones en forma de experimento cuando la pregunta de producto demande optimización medible. |
| Presentation Contract | Define contenido aprobado para representación. El Product Contract define qué contenido debe existir antes de que Presentation lo represente. |

---

## 6. Alternativas consideradas

| Alternativa | Evaluación |
|---|---|
| A. Contrato específico de AUC-001 | Buen encaje de dominio, bajo riesgo de sobregeneralización y compatible con la gobernanza actual. Es demasiado local para reutilización inmediata, pero eso es correcto ahora. |
| B. Extensión del Analytical Contract | Modelo documental más simple, pero arriesga sobrecargar el Analytical Contract con requisitos de consumo de producto y reglas de aceptación transversales. |
| C. Extensión del Presentation Contract | Captura parte de la utilidad del output, pero ubica incorrectamente la suficiencia de producto dentro de representación y arriesga que Presentation cree contenido. |
| D. Nueva categoría contractual local experimental | Mejor encaje arquitectónico: la suficiencia de producto es transversal, local a AUC y no está lista para Foundation. Exige naming claro y control estricto de boundary. |

Decisión recomendada: combinar A y D.

Crear un Analytical Product Contract específico de AUC-001 como nueva categoría contractual local experimental.

---

## 7. Tratamiento de la matriz de cobertura

La matriz de cobertura analítica debe formar parte del Analytical Product Contract.

No debe ser un artefacto independiente con autoridad separada.

Columnas mínimas de la matriz:

| Columna | Propósito |
|---|---|
| analytical_question_id | Identificador estable de pregunta. |
| business_question | Pregunta decisional en lenguaje claro. |
| required_evidence | Evidencia requerida para responder. |
| required_breakdowns | Desgloses por segmento, campaña, anuncio, temporalidad, plataforma o variable. |
| required_tables | Tablas/vistas esperadas cuando apliquen. |
| required_interpretation | Operación de Knowledge esperada, no solo una métrica. |
| recommendation_requirement | Si se requiere recomendación o experimento. |
| applicability_conditions | Condiciones en las que la fila aplica. |
| unknown_handling | Cómo marcar evidencia no disponible o insuficiente. |
| coverage_status | complete, partial, not_applicable, not_available. |
| traceability | Links a Evidence/Knowledge/Recommendation. |

### Riesgo

La matriz podría degradarse hasta convertirse en una checklist superficial.

### Mitigación

Cada fila debe exigir una operación analítica, no solo la presencia de una sección. Una fila solo está completa cuando evidencia, interpretación, tratamiento de limitaciones y trazabilidad están satisfechos. Reviewer y QA deben rechazar filas que marquen cumplimiento solo porque existe una tabla.

---

## 8. Observaciones residuales de P0

Clasificación preliminar para Specification:

| Observación | Clasificación preliminar | Rationale |
|---|---|---|
| Incluir `ad_name` junto a `ad_id_norm` | Requisito condicional de producto | `ad_id_norm` sigue siendo la clave. `ad_name` es útil como label descriptivo para legibilidad analítica y comprensión ejecutiva. Nunca debe convertirse en clave de join ni fallback. |
| Recuperar `ticket_status` | Requisito condicional de producto / posible evidence gap | Pertenece al producto solo si la evidencia autorizada vigente lo expone y soporta una pregunta de negocio. Si no, debe ir a evidencia/backlog, no a Presentation. |
| Evolución semanal enriquecida | Requisito de producto cuando se solicite soporte decisional temporal | No es una mejora de runtime. Es un requisito de suficiencia de producto para análisis temporal si la evidencia soporta semanas completas comparables. |
| Recomendaciones como experimentos medibles | Requisito de producto para calidad de recomendaciones | Pertenece al límite Recommendation/Product: cuando se propone optimización, las recomendaciones deben ser testeables con hipótesis, métrica, criterio de éxito y ventana de validación. |

Specification debe decidir el estado final tras revisar evidencia y contratos.

---

## 9. Producto para analistas vs producto para Dirección

Núcleo común de producto:

- preguntas canónicas de producto;
- estado de cobertura de evidencia;
- hechos y tablas clave requeridas por AUC-001;
- cobertura de Knowledge;
- trazabilidad de recomendaciones/experimentos;
- limitaciones y UNKNOWNs.

Proyección analítica:

- más tablas;
- matriz de cobertura más completa;
- lineage e IDs;
- limitaciones metodológicas;
- trazabilidad Evidence-to-Knowledge.

Proyección ejecutiva:

- menos tablas;
- jerarquía narrativa más fuerte;
- implicaciones listas para decisión;
- limitaciones visibles pero comprimidas;
- siguientes pasos medibles sin sobrecarga técnica.

La distinción entre producto para analistas y producto para Dirección pertenece a Presentation Projection y Communication Context solo después de que el núcleo de producto esté completo. El Product Contract debe definir contenido compartido y requisitos mínimos de visibilidad por proyección, no dos productos separados.

---

## 10. Hipótesis de instrucciones pequeñas

Hipótesis:

```text
La instrucción identifica la tarea; el repositorio proporciona el contexto.
```

Clasificación arquitectónica:

No es un requisito del Analytical Product Contract.

Pertenece a routing, gobernanza del repositorio y execution readiness.

### Dónde validarla

Debe validarse dentro del roadmap de P01 como hipótesis de gobernanza/readiness después de especificar e indexar el Product Contract, y antes de autorizar implementación.

Posible punto de validación:

- Reviewer Agent verifica que una instrucción breve puede enrutar al AUC, contrato, fase y restricciones correctas.
- QA Gate Agent verifica después que no puede iniciarse implementación desde una instrucción breve si el estado canónico y las fuentes requeridas no son inequívocos.

### Precondiciones

El repositorio necesita:

- estado canónico de AUC-001 sin contradicciones vigentes;
- ruta source-of-truth de P01 indexada en `docs/context_refs.md` cuando exista la Specification;
- distinción clara entre referencias históricas y estado vigente;
- routing explícito desde el README de AUC-001 hacia contrato/spec/gate de P01 cuando se creen;
- ausencia de lenguaje obsoleto de "siguiente acción" que contradiga gates vigentes;
- naming estable para la identidad P01 y cualquier ID posterior de iteración.

---

## 11. Identidad formal recomendada para P01

Recomendación:

```text
AUC-001-P01 - Analytical Product Contract Definition
```

Clasificación:

```text
Fase de producto posterior al cierre operativo P0, dentro de la gobernanza post-cierre de AUC-001.
```

No debe asumirse automáticamente que P01 equivale a `AUC-001-PCI-003`.

Rationale:

- P01 es una fase objetivo nombrada por el P0 Closure Gate.
- Los IDs PCI han representado hasta ahora iteraciones post-cierre con namespaces de ejecución/gate.
- El trabajo solicitado ahora es arquitectónico y previo a Specification, no una iteración de ejecución.

Namespace documental recomendado:

```text
docs/decisions/auc-001/auc-001-p01-analytical-product-contract-architectural-analysis.md
```

La ruta futura de Specification, a decidir por Specification Agent, podría seguir:

```text
specs/spec-014-auc-001-analytical-product-contract.md
```

Este memo no crea esa Specification.

Si más adelante se requiere implementación o ejecución, Tasks Planner y QA Gate Agent podrán decidir si hace falta una nueva identidad PCI.

---

## 12. Riesgos y mitigaciones

| Riesgo | Severidad | Mitigación |
|---|---|---|
| El Product Contract duplica el Analytical Contract | Alta | Mantener el Analytical Contract centrado en capacidades/modelo; Product Contract en suficiencia y cobertura de producto. |
| El Product Contract se convierte en Presentation Contract | Alta | La completitud de producto debe evaluarse antes de representación; Presentation solo expresa contenido aprobado. |
| El prompt histórico se convierte en plantilla oculta | Alta | Comparar capacidades, no estructura ni cifras. |
| La matriz se vuelve checklist superficial | Alta | Exigir evidencia + interpretación + trazabilidad + tratamiento de UNKNOWN por fila. |
| P01 reabre runtime/persistencia | Alta | Tratar SPEC-012/013 como estables salvo contradicción material documentada. |
| `ad_name` se convierte en clave de join | Alta | Permitirlo solo como label; mantener `ad_id_norm` como clave canónica. |
| Las recomendaciones se leen como autorización operativa | Media | Expresarlas como experimentos medibles, no como órdenes de ejecución. |
| El output ejecutivo oculta limitaciones | Media | Exigir visibilidad mínima de UNKNOWNs y limitaciones por proyección. |
| La hipótesis de instrucción breve se sobreexpande | Media | Validarla en routing/gobernanza, no dentro del contrato de producto. |

---

## 13. Inputs obligatorios para Specification Agent

Specification Agent debe recibir:

- este memo;
- README de AUC-001 y README raíz en su estado vigente;
- Analytical Contract de AUC-001;
- contratos base de Data, Evidence, Knowledge, Recommendation y Presentation;
- SPEC-010, SPEC-011, SPEC-012 y SPEC-013;
- ARCH-001 a ARCH-004;
- validación QA final de P0 y P0 Operational Closure Gate;
- PCI-002 Exit Gate y validación QA física del runtime;
- informe analítico actual y paquete PCI-002;
- prompt histórico e informes históricos solo como referencias comparativas;
- Knowledge Depth Recovery validation;
- Analytical Narrative validation;
- Presentation Output y Projection Readiness evaluations;
- `docs/tasks.md` como estado del backlog, no como autorización para añadir tareas.

Specification Agent debe resolver:

- nombre y ubicación final del contrato;
- taxonomía exacta de preguntas de producto;
- schema exacto de la matriz de cobertura;
- qué observaciones residuales pasan a ser obligatorias, condicionales o backlog;
- si recomendaciones-como-experimentos aplica a toda recomendación o solo a recomendaciones de optimización;
- si la completitud de producto se gradúa por proyección o una sola vez en el núcleo de producto;
- si `ticket_status` está disponible bajo la autorización de evidencia vigente;
- cómo documentar la comparación histórica sin crear expected values.

---

## 14. Criterios que deben bloquear implementación prematura

La implementación no debe comenzar hasta que:

- exista una Specification de P01 y haya sido revisada;
- el boundary del Analytical Product Contract esté aprobado;
- la matriz de cobertura esté especificada dentro del contrato;
- las reglas de comparación histórica sean explícitas;
- las observaciones residuales estén clasificadas por Specification;
- no se incluyan cambios de runtime/persistencia/modelo sin contradicción material documentada;
- no se asuman nuevas fuentes de evidencia sin autorización del Data Contract;
- QA Gate Agent haya abierto el Entry Gate para el alcance real de implementación;
- los outputs históricos protegidos sigan siendo inmutables;
- la identidad de P01 esté indexada y sea inequívoca en el contexto del repositorio.

---

## 15. Decisión recomendada

Decisión recomendada:

```text
Avanzar a Specification para un Analytical Product Contract específico de AUC-001 como nueva categoría contractual local experimental.
```

El contrato debe definir suficiencia de producto, cobertura analítica y criterios de aceptación a nivel de producto para AUC-001. Debe consumir los contratos existentes de Evidence, Knowledge, Recommendation y Presentation sin reemplazarlos.

P01 debe formalizarse como:

```text
AUC-001-P01 - Analytical Product Contract Definition
```

y no automáticamente como `AUC-001-PCI-003`.

---

## 16. Archivos revisados

### Estado vigente y routing

- `.github/skills/meta-lead-quality-analysis/SKILL.md`
- `.github/skills/meta-lead-quality-analysis/RUNBOOK.md`
- `.github/skills/meta-lead-quality-analysis/references.md`
- `README.md`
- `project_brief.md`
- `docs/context_refs.md`
- `analytical_use_cases/meta_lead_quality_analysis.md`
- `analytical_use_cases/auc-001/README.md`
- `docs/tasks.md`

### Contratos y specifications

- `analytical_use_cases/auc-001/analytical-contract.md`
- `docs/contracts/analytical.contract.md`
- `docs/contracts/data.contract.md`
- `docs/contracts/evidence.contract.md`
- `docs/contracts/knowledge.contract.md`
- `docs/contracts/recommendation.contract.md`
- `docs/contracts/presentation.contract.md`
- `specs/spec-010-presentation-projection-selection.md`
- `specs/spec-011-communication-context-representation-transformation.md`
- `specs/spec-012-auc-001-canonical-cost-quality-model.md`
- `specs/spec-013-auc-001-structured-reconciliation-output.md`

### Decisiones y gates

- `docs/decisions/auc-001/auc-001-execution-scope-canonicalization-architectural-decision.md`
- `docs/decisions/auc-001/auc-001-presentation-projection-architectural-decision.md`
- `docs/decisions/auc-001/auc-001-communication-context-representation-transformation-architectural-decision.md`
- `docs/decisions/auc-001/auc-001-canonical-cost-quality-model-architectural-decision.md`
- `gates/auc-001-p0-operational-closure-gate.md`
- `gates/auc-001-pci-002-exit-gate.md`

### Evaluaciones y productos

- `docs/evaluations/auc-001/validations/auc-001-p0-operational-closure-final-qa-validation.md`
- `docs/evaluations/auc-001/validations/auc-001-pci-002-physical-runtime-qa-validation.md`
- `docs/evaluations/auc-001/validations/auc-001-knowledge-depth-recovery-validation.md`
- `docs/evaluations/auc-001/validations/auc-001-analytical-narrative-validation.md`
- `docs/evaluations/auc-001/validations/auc-001-presentation-output-evaluation.md`
- `docs/evaluations/auc-001/validations/auc-001-presentation-projection-readiness-evaluation.md`
- `outputs/auc-001/2026-06-30/analytical-report.md`
- `outputs/auc-001/pci-002/2026-06-30/analytical-report/analytical-report.md`
- `outputs/auc-001/pci-002/2026-06-30/execution/runtime-output.json`
- `outputs/auc-001/pci-002/2026-06-30/execution/context-definition.json`
- `outputs/auc-001/pci-002/2026-06-30/evidence/evidence-set.json`
- `outputs/auc-001/pci-002/2026-06-30/knowledge/knowledge-set.json`
- `outputs/auc-001/pci-002/2026-06-30/recommendations/recommendation-set.json`

### Referencias históricas de comparación

- `docs/corpus/auc-001/prompt_historico_monolitico.md`
- `docs/corpus/auc-001/informe_calidad_leads_scoring_20260701.md`
- `docs/corpus/auc-001/informe_calidad_leads_20260510.md` listado como disponible; no leído en este pase porque el informe 20260701 y el prompt fueron suficientes para la base comparativa requerida.
