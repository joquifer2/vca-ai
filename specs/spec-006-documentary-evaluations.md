# Specification

## Metadata

### Spec ID

SPEC-006

### Title

Documentary Evaluations

### Status

Draft

### Owner

Foundation maintainers

### Last Updated

2026-07-10

---

## 1. Purpose

Definir el marco fundacional de evaluaciones documentales que la Foundation utilizara para verificar la suficiencia, coherencia y trazabilidad de artefactos, contracts y gates antes de tomar decisiones de avance.

---

## 2. Background

El roadmap fundacional sitúa las evaluaciones documentales inmediatamente despues de los readiness gates.

La Foundation ya dispone de un lifecycle analitico, de limites entre componentes, de un modelo de extensibilidad, de contracts transversales y de gates de readiness. Ese conjunto requiere un mecanismo documental estable que permita evaluar calidad, completitud, coherencia y evidencia sin confundir la evaluacion con la aprobacion final.

El QA Gate Agent evalua gates. Esta specification formaliza el artefacto documental que documenta evaluaciones, hallazgos, huecos, riesgos y recomendaciones para esos gates y para otros artefactos relevantes.

---

## 3. Objective

Esta capacidad debe conseguir que la Foundation disponga de un marco comun para producir evaluaciones documentales reutilizables.

El resultado debe permitir analizar artefactos y evidencia de forma conservadora, dejando trazabilidad suficiente para justificar una decision de gate, una correccion documental o una nueva iteracion metodologica.

---

## 4. Scope

### Included

- definicion de categorias fundacionales de evaluaciones documentales;
- definicion de metadata minima obligatoria para cualquier evaluation;
- definicion de criterios de analisis documental, evidencia y conclusiones;
- definicion de la relacion entre evaluations, gates, specs, contracts y context refs.

### Excluded

- aprobacion humana final;
- automatizacion ejecutable de evaluaciones;
- validaciones tecnicas de runtime o infraestructura;
- criterios especificos de un proyecto derivado o cliente concreto.

---

## 5. Actors

| Actor | Description |
| --- | --- |
| Reviewer | Revisa coherencia, completitud y calidad documental |
| QA Gate Agent | Consume evaluaciones como evidencia para decidir gates |
| Documentation Agent | Produce y mantiene evaluaciones documentales |
| Specification Agent | Consume evaluaciones para refinar o ampliar specs |
| Foundation Maintainers | Toman decisiones humanas cuando la evaluacion no basta |
| Derived Project Team | Reutiliza el marco de evaluaciones en proyectos derivados |

---

## 6. Inputs

| Input | Description |
| --- | --- |
| Artifact Set | Documentos, specs, contracts, gates o referencias que seran evaluados |
| Context References | Fuentes de contexto oficiales relevantes para la evaluacion |
| Gate Requirements | Requisitos de un gate o decision que requiera evidencia documental |
| Evidence Set | Hallazgos observables, huecos y riesgos documentales |
| Evaluation Criteria | Criterios de suficiencia, coherencia, trazabilidad y bloqueo |

---

## 7. Outputs

| Output | Description |
| --- | --- |
| Evaluation Categories | Tipos fundacionales de evaluaciones admitidos |
| Evaluation Metadata Rules | Campos minimos obligatorios para describir una evaluation |
| Assessment Model | Modelo normalizado para separar hallazgos, riesgos, unknowns y recomendaciones |
| Decision Support | Evidencia documental que puede apoyar o bloquear una decision de gate |

---

## 7.1 Evaluation Categories

La Foundation debe reconocer como minimo las siguientes categorias de evaluaciones documentales:

| Category | Purpose |
| --- | --- |
| Artifact Evaluation | Evaluar la suficiencia y coherencia de un artefacto o conjunto de artefactos |
| Gate Evaluation | Evaluar si un gate tiene suficiente base documental para emitir una decision |
| Contract Evaluation | Evaluar si un contract es usable, trazable y compatible con el marco fundacional |
| Boundary Evaluation | Evaluar si se preservan limites, handoffs y responsabilidades entre componentes |
| Context Evaluation | Evaluar si el contexto disponible es suficiente y coherente para continuar |
| Readiness Evaluation | Evaluar si el estado documental general permite avanzar al siguiente paso |

Readiness Evaluation es la categoria paraguas. Gate Evaluation es una especializacion de Readiness Evaluation cuando el objeto principal de la evaluacion es un gate concreto.

---

## 7.2 Minimum Evaluation Metadata

Toda evaluation documental debe declarar, como minimo, lo siguiente:

| Field | Required Content |
| --- | --- |
| Evaluation ID | Identificador unico y estable |
| Evaluation Name | Nombre claro y reutilizable |
| Evaluation Category | Categoria fundacional a la que pertenece |
| Evaluation Scope | Artefacto, gate, boundary, contract o contexto evaluado |
| Source Artifacts | Artefactos revisados durante la evaluation |
| Context References | Referencias de contexto utilizadas |
| Purpose | Proposito metodologico de la evaluacion |
| Criteria Reviewed | Criterios documentales que se revisaron |
| Findings | Hallazgos observables identificados |
| Gaps | Huecos, ausencias o limitaciones observadas |
| Risks | Riesgos derivados de los hallazgos o de los gaps |
| Recommendations | Recomendaciones documentales o de avance |
| Traceability Links | Referencias a evidencia, specs, gates o artefactos relacionados |

---

## 7.3 Assessment Model

Toda evaluation documental debe estructurar su contenido en las siguientes capas conceptuales:

| Layer | Meaning |
| --- | --- |
| Observations | Hechos documentales observables |
| Findings | Interpretacion controlada de las observaciones |
| Gaps | Informacion faltante o insuficiente |
| Risks | Consecuencias de los gaps o de incoherencias |
| Recommendations | Acciones sugeridas para corregir o avanzar |

---

## 7.4 Evaluation Rules

Una evaluation documental solo puede considerarse utilizable cuando:

- identifica de forma explicita el objeto evaluado y su scope;
- separa observaciones, hallazgos, gaps, riesgos y recomendaciones;
- se apoya en artefactos y contexto verificables;
- no confunde una evaluacion documental con una aprobacion final;
- puede ser consumida por un gate, un reviewer o un maintainer sin redescubrir el sistema desde cero;
- explicita cuando una conclusion depende de evidencia insuficiente;
- mantiene trazabilidad hacia los artefactos y referencias que la justifican.

---

## 8. Functional Requirements

### FR-001

La Foundation debe definir un conjunto minimo de categorias de evaluaciones documentales reutilizables entre artefactos, gates y fases.

### FR-002

Toda evaluation documental debe declarar metadata minima suficiente para identificar su scope, artefactos fuente, criterios revisados, hallazgos, gaps y recomendaciones.

### FR-003

Las evaluaciones documentales deben poder consumirse como evidencia para readiness gates, reviews y decisiones metodologicas sin requerir automatizacion ejecutable.

### FR-004

La Foundation debe exigir que toda evaluacion documente de forma explicita los artefactos revisados y la trazabilidad utilizada.

### FR-005

Las evaluaciones documentales deben permanecer independientes de tecnologia, proveedor y dominio especifico.

### FR-006

Una evaluacion reusable puede especializar criterios o scope, pero debe preservar el assessment model comun y la separacion entre observacion, hallazgo, gap, riesgo y recomendacion.

### FR-007

La Foundation debe permitir que futuros templates o documentos de evaluacion reutilicen este marco sin redefinir sus reglas nucleares.

---

## 9. Business Rules

### BR-001

Toda evaluacion documental debe basarse en artefactos y contexto identificables, no en intuicion o memoria informal.

### BR-002

Una evaluation no puede encubrir huecos documentales; los gaps deben quedar explicitados.

### BR-003

Si una conclusion requiere evidencia no disponible, la evaluation debe marcarla como insuficiente en lugar de asumir completitud.

### BR-004

Una evaluacion puede apoyar o bloquear un gate, pero no sustituir la decision humana final cuando esta sea necesaria.

---

## 10. Constraints

- esta specification debe permanecer documental y no ejecutable;
- no debe definir automatizaciones operativas ni checks tecnicos productivos;
- no debe duplicar contenido de una evaluacion instanciada en un proyecto derivado;
- debe mantenerse compatible con el SDD Harness, con QA Gate Agent y con readiness gates.

---

## 11. Assumptions

- los proyectos derivados necesitaran evaluaciones documentales para justificar decisiones de gates y refinamientos de specs;
- existe valor en normalizar hallazgos, gaps y recomendaciones para hacer comparables las evaluaciones;
- las evaluaciones documentales seran reutilizables como evidencia dentro del proceso SDD.

---

## 12. Risks

| Risk | Impact | Notes |
| --- | --- | --- |
| Definir evaluations demasiado abstractas | Medio | Puede dificultar su uso en revisiones concretas |
| Mezclar evaluation con approval | Alto | Debilita la trazabilidad y el control conservador |
| No separar observaciones de recomendaciones | Alto | Confunde evidencia con conclusion |

---

## 13. Acceptance Criteria

### AC-001

La spec define categorias fundacionales de evaluaciones documentales y su proposito diferenciado.

### AC-002

La spec deja explicita la metadata minima que cualquier evaluation documental debe declarar.

### AC-003

La spec fija reglas suficientes para preservar trazabilidad, separacion entre observacion y recomendacion, y utilidad como evidencia para gates y reviews.

---

## 14. Dependencies

- project_brief.md;
- docs/context_refs.md;
- spec-001-analytical-lifecycle.md;
- spec-004-transversal-contracts.md;
- spec-005-readiness-gates.md;
- spec-007-extension-compatibility-reusability.md;
- .github/agents/qa-gate.agent.md;
- .github/agents/documentation.agent.md.

---

## 15. Open Questions

- si convendra separar en el futuro artifact evaluations de gate evaluations con templates distintos;
- que nivel de formalismo deberian tener las recomendaciones documentales para ser reutilizables por QA Gate Agent;
- si alguna categoria de evaluation deberia derivarse en un template especifico adicional.

---

## 16. Future Considerations

- crear un template reutilizable para documentary evaluations alineado con este marco;
- definir la relacion exacta entre evaluaciones documentales y readiness gates de fase;
- instanciar evaluaciones especializadas para contracts, boundaries, context governance o compatibilidad de extensiones cuando el alcance lo requiera.

---

## 17. Related Artifacts

| Artifact | Relationship |
| --- | --- |
| project_brief.md | Define el roadmap fundacional que prioriza evaluaciones documentales |
| docs/context_refs.md | Actua como fuente oficial de contexto y decisiones para esta spec |
| spec-001-analytical-lifecycle.md | Define las fases cuyo progreso puede requerir evaluation support |
| spec-004-transversal-contracts.md | Define contracts que pueden ser objeto de evaluation |
| spec-005-readiness-gates.md | Define gates que pueden consumir evaluaciones como evidencia |
| spec-007-extension-compatibility-reusability.md | Define un caso de uso donde las evaluaciones documentales pueden sustentar compatibilidad de extensiones |
| .github/agents/qa-gate.agent.md | Define el agente que consume evaluaciones para decidir gates |
| .github/agents/documentation.agent.md | Define el agente que produce y mantiene evaluaciones documentales |

---

## Definition of Done

La specification esta completa cuando:

- el objetivo esta definido;
- el alcance esta definido;
- los limites estan definidos;
- los inputs estan definidos;
- los outputs estan definidos;
- los requisitos funcionales estan definidos;
- las reglas principales estan documentadas;
- los riesgos relevantes estan identificados;
- existen criterios de aceptacion verificables.