# Specification

## Metadata

### Spec ID

SPEC-007

### Title

Extension Compatibility and Reusability

### Status

Draft

### Owner

Foundation maintainers

### Last Updated

2026-07-10

---

## 1. Purpose

Definir el marco fundacional para documentar, evaluar y reutilizar extensiones compatibles con la Foundation sin alterar el nucleo metodologico comun.

---

## 2. Background

La Foundation ya define el modelo general de extensibilidad en SPEC-003, junto con los contratos transversales, los readiness gates y las evaluaciones documentales necesarias para gobernar su evolucion.

Ese marco necesita una formalizacion especifica para los artefactos que permiten declarar si una extension es compatible con la Foundation, si puede reutilizarse en mas de un contexto y que restricciones deben preservarse para no romper el core.

Esta specification no redefine la extensibilidad general. SPEC-003 sigue siendo la definicion del modelo general de extensibilidad; esta spec formaliza unicamente los artefactos documentales necesarios para describir y evaluar una extension concreta de forma consistente.

---

## 3. Objective

Esta capacidad debe conseguir que la Foundation disponga de un modelo comun para declarar, revisar y registrar la compatibilidad y reutilizacion de extensiones.

El resultado debe permitir diferenciar extensiones compatibles, extensiones reutilizables y extensiones limitadas a un caso puntual, dejando trazabilidad suficiente para su revision documental y para futuras decisiones metodologicas.

---

## 4. Scope

### Included

- definicion del Extension Compatibility Dossier como artefacto fundacional;
- definicion de los campos minimos que debe declarar cualquier extension compatible o reusable;
- definicion de criterios de compatibilidad con el core fundacional;
- definicion de criterios de reusabilidad entre mas de un caso de uso;
- definicion de la relacion entre extensiones, contracts, gates y evaluaciones documentales.

### Excluded

- implementacion tecnica de extensiones;
- packaging, instalacion o despliegue operativo;
- evaluacion automatizada de extensiones;
- criterios especificos de un proyecto derivado o dominio concreto.

---

## 5. Actors

| Actor | Description |
| --- | --- |
| Extension Author | Declara la extension y su compatibilidad o reusabilidad |
| Reviewer | Revisa coherencia, limites y trazabilidad de la extension |
| QA Gate Agent | Puede consumir el dossier para decidir si una extension es apta para avanzar |
| Documentation Agent | Mantiene indices, referencias y artefactos de extensiones |
| Foundation Maintainers | Toman la decision humana final cuando una extension requiere validacion |
| Derived Project Team | Reutiliza el marco para extensiones en proyectos derivados |

---

## 6. Inputs

| Input | Description |
| --- | --- |
| Core Methodology | Principios, limites y fases fundacionales de la Foundation |
| Extension Candidate | Extension propuesta para evaluar compatibilidad o reusabilidad |
| Boundary Requirements | Restricciones de componentes, contratos y handoffs aplicables |
| Contract Requirements | Contracts que la extension debe consumir, producir o respetar |
| Use Case Context | Casos de uso plausibles donde la extension podria aplicarse |
| Evidence Set | Evidencia documental que respalda la evaluacion |

---

## 7. Outputs

| Output | Description |
| --- | --- |
| Extension Compatibility Dossier | Dossier fundacional que resume compatibilidad y reusabilidad |
| Extension Profile | Descripcion basica de la extension y su superficie del sistema |
| Compatibility Profile | Declaracion de que limites y dependencias respeta la extension |
| Reusability Profile | Declaracion de en que contextos puede reutilizarse la extension |
| Review Summary | Resumen documentado de hallazgos, riesgos y recomendaciones |

---

## 7.1 Dossier Components

La Foundation debe reconocer como minimo los siguientes componentes del Extension Compatibility Dossier:

| Component | Purpose |
| --- | --- |
| Extension Profile | Identificar la extension, su categoria y su finalidad |
| Compatibility Profile | Declarar limites, dependencias permitidas y dependencias prohibidas |
| Reusability Profile | Declarar casos de uso plausibles y criterios para reutilizacion |
| Review Summary | Recoger hallazgos, gaps, riesgos y decision documental |

---

## 7.2 Minimum Dossier Metadata

Todo dossier de compatibilidad y reutilizacion debe declarar, como minimo, lo siguiente:

| Field | Required Content |
| --- | --- |
| Extension ID | Identificador unico y estable |
| Extension Name | Nombre claro y reutilizable |
| Extension Category | Skill, Routine, Template o Contract |
| Core Surface | Parte del sistema que amplifica o especializa |
| Purpose | Valor funcional de la extension |
| Supported Phases | Fases SDD donde aplica o no aplica |
| Required Contracts | Contracts que la extension requiere para operar |
| Produced Contracts | Contracts que la extension puede emitir |
| Allowed Dependencies | Dependencias explicitas que puede usar |
| Forbidden Dependencies | Dependencias que no puede asumir |
| Compatibility Statement | Declaracion de compatibilidad con el core fundacional |
| Reuse Statement | Declaracion de reutilizacion mas alla de un unico caso |
| Evidence Links | Referencias a specs, gates, evaluaciones o context refs |
| Unknowns | Huecos, limitaciones o supuestos no verificados |

---

## 7.3 Compatibility Rules

Estas reglas complementan las reglas generales de compatibilidad definidas en SPEC-003 y las aterrizan al nivel de un dossier concreto.

Una extension solo puede considerarse compatible cuando:

- no elimina fases ni altera la secuencia metodologica comun;
- no reasigna responsabilidades fundacionales entre componentes;
- no introduce dependencias obligatorias sobre una unica tecnologia, proveedor o runtime;
- declara de forma explicita los contracts que necesita y los que produce;
- mantiene trazabilidad hacia las fuentes o artefactos que justifican su compatibilidad;
- separa con claridad conocimiento de dominio y reglas fundacionales;
- documenta limitaciones, exclusiones y estados UNKNOWN cuando falte contexto verificable.

---

## 7.4 Reusability Rules

Estas reglas complementan los criterios generales de reuso de SPEC-003 y los convierten en criterios verificables dentro del dossier.

Una extension solo puede considerarse reusable cuando:

- aplica a mas de un caso de uso plausible dentro de la metodologia;
- se describe por su procedimiento, estructura o regla general y no por un incidente aislado;
- puede revisarse sin depender de conocimiento tacito no documentado;
- explicita que parte del sistema amplifica y que parte permanece inalterada;
- declara de forma clara en que contextos no debe reutilizarse;
- mantiene un nivel de abstraccion suficiente para no quedar atada a un unico proyecto derivado.

---

## 8. Functional Requirements

### FR-001

La Foundation debe definir un Extension Compatibility Dossier reutilizable para documentar compatibilidad y reusabilidad de extensiones.

### FR-002

Toda extension documentada como compatible o reusable debe declarar metadata minima suficiente para identificar su superficie de core, contracts requeridos, dependencias, limits y evidencia asociada.

### FR-003

La Foundation debe permitir distinguir entre extensiones compatibles, extensiones reusables y extensiones especificas de un unico caso.

### FR-004

Las extensiones compatibles deben mantener independencia respecto a tecnologia, proveedor y dominio especifico.

### FR-005

Las extensiones reusables deben poder demostrar aplicacion plausible en mas de un caso de uso sin recurrir a supuestos tacitos.

### FR-006

Una extension compatible o reusable puede ser consumida por gates, evaluaciones documentales o reviewers sin requerir redescubrimiento del core.

### FR-007

La Foundation debe permitir que futuros templates o documentos de extension reutilicen este marco sin redefinir sus reglas nucleares.

---

## 9. Business Rules

### BR-001

Toda extension debe declarar de forma explicita si se pretende compatible, reusable o especifica de un unico caso.

### BR-002

Una extension no puede presentarse como reusable si solo esta validada para un unico contexto puntual.

### BR-003

Si una extension requiere inventar evidencia o inferir contexto no documentado, debe marcarse como no compatible o no reusable hasta que la evidencia sea verificable.

### BR-004

Los conflictos entre compatibilidad declarada y evidencias observadas deben resolverse mediante evaluacion documental o gate antes de asumir reutilizacion.

---

## 10. Constraints

- esta specification debe permanecer documental y no ejecutable;
- no debe definir packaging, despliegue ni automatizacion operativa;
- no debe sustituir las reglas generales de extensibilidad ya definidas en SPEC-003;
- debe mantenerse compatible con contracts, readiness gates y evaluaciones documentales.

---

## 11. Assumptions

- los proyectos derivados necesitaran distinguir entre extensiones puntuales y extensiones reutilizables;
- existe valor en registrar de forma formal la compatibilidad antes de introducir una extension en un flujo de trabajo;
- los contracts y los gates pueden actuar como evidencia de soporte para validar compatibilidad y reutilizacion.

---

## 12. Risks

| Risk | Impact | Notes |
| --- | --- | --- |
| Declarar reutilizable una extension puntual | Alto | Reduce coherencia y aumenta acoplamiento |
| Mezclar compatibilidad documental con despliegue operativo | Alto | Rompe el alcance SDD de la Foundation |
| Definir dossiers demasiado abstractos | Medio | Puede dificultar su uso en proyectos derivados |

---

## 13. Acceptance Criteria

### AC-001

La spec define el Extension Compatibility Dossier y sus componentes fundacionales.

### AC-002

La spec deja explicita la metadata minima que cualquier extension compatible o reusable debe declarar.

### AC-003

La spec fija reglas suficientes para preservar compatibilidad, reusabilidad y trazabilidad sin introducir acoplamiento operativo.

---

## 14. Dependencies

- project_brief.md;
- docs/context_refs.md;
- spec-003-extensibility-model.md;
- spec-004-transversal-contracts.md;
- spec-005-readiness-gates.md;
- spec-006-documentary-evaluations.md;
- .github/agents/specification.agent.md;
- .github/agents/qa-gate.agent.md;
- .github/agents/documentation.agent.md.

---

## 15. Open Questions

- si convendra crear en el futuro templates distintos para extensiones compatibles y extensiones reusables;
- que nivel de formalismo deberia tener la evidencia para aceptar una extension como reusable;
- si convendra especializar templates complementarios por categoria de extension ademas del dossier general ya existente.

---

## 16. Future Considerations

- mantener alineado el template reutilizable de extension dossiers con este marco a medida que se documenten nuevas extensiones;
- instanciar evaluaciones documentales especificas para compatibilidad de extensiones cuando el alcance lo requiera;
- definir un registro o catalogo de extensiones compatibles y reusables cuando el volumen lo requiera.

---

## 17. Related Artifacts

| Artifact | Relationship |
| --- | --- |
| project_brief.md | Define el roadmap fundacional que prioriza la compatibilidad de extensiones |
| docs/context_refs.md | Actua como fuente oficial de contexto y decisiones para esta spec |
| spec-003-extensibility-model.md | Define las reglas generales de extensibilidad |
| spec-004-transversal-contracts.md | Define contracts que una extension puede requerir o producir |
| spec-005-readiness-gates.md | Define gates que pueden validar la compatibilidad de una extension |
| spec-006-documentary-evaluations.md | Define evaluaciones que pueden sustentar una decision sobre la extension |
| docs/templates/extension_compatibility_dossier.template.md | Template reutilizable para documentar el dossier definido por esta spec |
| .github/agents/specification.agent.md | Define el agente que crea formalizaciones SDD |
| .github/agents/qa-gate.agent.md | Define el agente que valida gates sobre artefactos |
| .github/agents/documentation.agent.md | Define el agente que mantiene navegacion y coherencia documental |

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