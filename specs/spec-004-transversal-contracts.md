# Specification

## Metadata

### Spec ID

SPEC-004

### Title

Transversal Contracts

### Status

Draft

### Owner

Foundation maintainers

### Last Updated

2026-07-10

---

## 1. Purpose

Definir el modelo comun de contracts transversales que la Foundation utilizara para desacoplar componentes, fases y extensiones sin fijar implementaciones ejecutables ni tecnologia concreta.

---

## 2. Background

El roadmap fundacional prioriza specifications adicionales para contracts transversales despues de completar el lifecycle, los component boundaries y el extensibility model.

Las specs ya publicadas dependen de la existencia de contracts reutilizables para intercambiar datos, evidencia, conocimiento, recomendaciones y reglas de extension sin recurrir a dependencias implicitas.

Esta specification formaliza ese nivel comun para que futuros artefactos contractuales mantengan coherencia metodologica.

---

## 3. Objective

Esta capacidad debe conseguir que la Foundation disponga de un marco estable para describir contracts reutilizables entre componentes y artefactos metodologicos.

El resultado debe permitir identificar que estructuras de intercambio son admisibles, que informacion minima deben declarar y que reglas deben preservar para sostener trazabilidad, desacoplamiento y evolucion controlada.

---

## 4. Scope

### Included

- definicion de categorias fundacionales de contracts transversales;
- definicion de metadata minima obligatoria para cualquier contract transversal;
- definicion de reglas de trazabilidad, estabilidad y validacion documental;
- definicion de relaciones entre contracts, lifecycle, boundaries y extensiones.

### Excluded

- definicion de schemas tecnicos ejecutables;
- contratos de integracion productiva con APIs, eventos o bases de datos concretas;
- reglas de negocio o campos especificos de un dominio;
- automatizacion operativa de validacion de contratos.

---

## 5. Actors

| Actor | Description |
| --- | --- |
| Framework | Coordina el uso metodologico de contracts entre fases y componentes |
| Contract Author | Define contracts reutilizables compatibles con la Foundation |
| Data Provider | Publica contracts de datos o contexto estructurado |
| Analytical Layer | Consume o produce contracts de evidencia y modelos analiticos |
| Reasoning Layer | Consume evidencia y produce contracts de conocimiento y recomendacion |
| Presentation Layer | Consume contracts aprobados para construir artefactos de salida |
| Skill Author | Declara contracts adicionales o especializados sin romper el core |
| Reviewer | Valida que un contract preserve trazabilidad, desacoplamiento y neutralidad tecnologica |

---

## 6. Inputs

| Input | Description |
| --- | --- |
| Lifecycle Requirements | Necesidades de intercambio derivadas del ciclo analitico comun |
| Boundary Rules | Limites entre componentes y handoffs permitidos |
| Extension Rules | Restricciones de extensibilidad aplicables a Skills, Routines, Templates y Contracts |
| Context References | Fuentes oficiales de contexto relevantes para definir un contract |
| Artifact Template | Template o estructura base que permita documentar el contract |

---

## 7. Outputs

| Output | Description |
| --- | --- |
| Contract Categories | Tipos fundacionales de contracts admitidos por la Foundation |
| Contract Metadata Rules | Campos minimos obligatorios que todo contract debe declarar |
| Stability Rules | Reglas que preservan compatibilidad y evitan acoplamiento impropio |
| Validation Rules | Criterios documentales para considerar un contract utilizable |

---

## 7.1 Contract Categories

La Foundation debe reconocer como minimo las siguientes categorias de contracts transversales:

| Category | Purpose |
| --- | --- |
| Context Contract | Delimitar objetivo, restricciones y fuentes de contexto aplicables |
| Data Contract | Describir la estructura intercambiada por un Data Provider antes del trabajo analitico |
| Discovery Contract | Formalizar el Discovery Model y sus limitaciones observadas |
| Analytical Contract | Formalizar el Analytical Model resultante de la preparacion |
| Evidence Contract | Formalizar hallazgos observables separados de interpretacion |
| Knowledge Contract | Formalizar insights, hipotesis, prioridades e incertidumbres |
| Recommendation Contract | Formalizar acciones sugeridas y su justificacion |
| Presentation Contract | Delimitar que contenido aprobado puede consumir la capa de presentacion |
| Extension Contract | Declarar reglas de entrada y salida que una extension introduce sin alterar el core |

Mapeo minimo con el lifecycle fundacional:

- Context Definition se formaliza mediante Context Contract;
- Discovery Model se formaliza mediante Discovery Contract;
- Analytical Model se formaliza mediante Analytical Contract;
- Evidence Set se formaliza mediante Evidence Contract;
- Knowledge Set se formaliza mediante Knowledge Contract;
- Recommendation Set se formaliza mediante Recommendation Contract;
- Output Artifact puede consumir un Presentation Contract, pero la aprobacion metodologica previa del Framework hacia la capa de presentacion no constituye por si misma un contract transversal y debe tratarse como artefacto de gate o readiness en futuros artefactos fundacionales.

---

## 7.2 Minimum Contract Metadata

Todo contract transversal debe declarar, como minimo, lo siguiente:

| Field | Required Content |
| --- | --- |
| Contract ID | Identificador unico y estable |
| Contract Name | Nombre claro y reutilizable |
| Contract Category | Categoria fundacional a la que pertenece |
| Producer | Componente, capa o artefacto que lo emite |
| Consumer | Componente, capa o artefacto que lo consume |
| Purpose | Funcion metodologica del contract |
| Inputs | Informacion o precondiciones necesarias |
| Outputs | Informacion estructurada que entrega |
| Critical Fields | Campos o bloques minimos cuya ausencia invalida el contract |
| Validation Rules | Reglas documentales para verificar completitud y consistencia |
| Traceability Links | Referencias a evidencia, conocimiento, spec o artefactos relacionados |
| Unknown Handling | Como se documentan huecos, estados UNKNOWN o limitaciones |

---

## 7.3 Validation Rules

Un contract transversal solo puede considerarse utilizable cuando:

- identifica de forma explicita productor y consumidor;
- explicita su categoria y su proposito metodologico;
- separa hechos, evidencia, conocimiento y recomendaciones cuando corresponda;
- declara campos criticos y reglas minimas de validacion;
- mantiene trazabilidad hacia las fuentes o artefactos que justifican su contenido;
- no depende de una tecnologia concreta para ser comprendido a nivel fundacional;
- documenta limitaciones y estados UNKNOWN cuando falte contexto verificable.

---

## 7.4 Stability Rules

- un contract no puede reasignar responsabilidades entre componentes fundacionales;
- un contract no puede introducir logica de negocio propia del dominio dentro del core metodologico;
- un contract de presentacion no puede sustituir ni reescribir contracts de evidencia o conocimiento;
- una extension puede especializar un contract, pero no eliminar metadata minima ni romper trazabilidad;
- los cambios sobre contracts transversales deben preservar compatibilidad documental o explicitar ruptura controlada.

---

## 8. Functional Requirements

### FR-001

La Foundation debe definir un conjunto minimo de categorias de contracts transversales reutilizables entre fases y componentes.

### FR-002

Todo contract transversal debe declarar metadata minima suficiente para identificar productor, consumidor, proposito, inputs, outputs y validaciones.

### FR-003

Los contracts deben poder soportar handoffs entre Data Provider, capa analitica, capa de razonamiento, Framework, capa de presentacion y extensiones sin recurrir a dependencias implicitas.

### FR-004

La Foundation debe exigir trazabilidad explicita entre contracts y los artefactos que justifican su contenido.

### FR-005

Los contracts transversales deben permanecer independientes de tecnologia, proveedor y dominio especifico.

### FR-006

Una extension compatible puede especializar contracts existentes o declarar nuevos contracts, pero debe preservar metadata minima, claridad de categoria y cumplimiento de limites.

### FR-007

La Foundation debe permitir que futuros templates o documentos de contracts reutilicen este marco sin redefinir sus reglas nucleares.

---

## 9. Business Rules

### BR-001

Todo intercambio relevante entre componentes debe expresarse mediante un contract o artefacto contractual equivalente, no mediante contexto informal.

La aprobacion metodologica previa a la presentacion puede apoyarse en un artefacto de gate o readiness separado del contract transversal que describe el contenido aprobado.

### BR-002

Los contracts de evidencia, conocimiento y recomendacion deben mantenerse separados para preservar trazabilidad y auditabilidad.

### BR-003

La metadata minima de un contract transversal es obligatoria incluso cuando el contract se especialice en una Skill o Routine concreta.

### BR-004

Si un contract necesita inferir informacion no verificable, debe marcar el hueco como UNKNOWN en lugar de completar contenido por suposicion.

---

## 10. Constraints

- esta specification debe permanecer documental y no ejecutable;
- no debe definir schemas tecnicos de serializacion, API payloads ni contratos productivos concretos;
- no debe duplicar el contenido de un documento de contracts instanciado para un proyecto derivado;
- debe mantenerse compatible con los limites definidos por lifecycle, boundaries y extensibility.

---

## 11. Assumptions

- los proyectos derivados necesitaran contracts reutilizables para sostener trazabilidad entre fases;
- la metadata minima comun permitira especializaciones posteriores sin rehacer el core contractual;
- los templates de contracts podran reutilizar este marco para documentar contratos concretos o inferidos.

---

## 12. Risks

| Risk | Impact | Notes |
| --- | --- | --- |
| Definir contracts demasiado abstractos | Medio | Puede dificultar su uso en artefactos concretos |
| Mezclar categorias contractuales | Alto | Rompe trazabilidad entre evidencia, conocimiento y recomendacion |
| Permitir especializaciones que eliminen metadata minima | Alto | Debilita comparabilidad y validacion |

---

## 13. Acceptance Criteria

### AC-001

La spec define categorias fundacionales de contracts transversales y su proposito diferenciado.

### AC-002

La spec deja explicita la metadata minima que cualquier contract transversal debe declarar.

### AC-003

La spec fija reglas suficientes para preservar trazabilidad, boundary compliance y neutralidad tecnologica en futuros contracts reutilizables.

---

## 14. Dependencies

- project_brief.md;
- docs/context_refs.md;
- spec-001-analytical-lifecycle.md;
- spec-002-component-boundaries.md;
- spec-003-extensibility-model.md;
- docs/templates/contracts.template.md.

---

## 15. Open Questions

- que nivel de granularidad deberian tener los critical fields de cada categoria contractual;
- si convendra separar en el futuro contracts fundacionales y contracts de proyecto derivado;
- que criterio formal se utilizara para versionar cambios incompatibles en contracts transversales.

---

## 16. Future Considerations

- crear un template especifico o ajustar el template de contracts para alinearlo explicitamente con estas categorias fundacionales;
- definir gates de readiness para validar contracts antes de su uso en handoffs criticos;
- definir evaluaciones documentales que verifiquen trazabilidad entre contracts de evidencia, conocimiento y recomendacion.

---

## 17. Related Artifacts

| Artifact | Relationship |
| --- | --- |
| project_brief.md | Define el proposito fundacional y el roadmap de evolucion documental |
| docs/context_refs.md | Actua como fuente oficial de contexto y decisiones para esta spec |
| spec-001-analytical-lifecycle.md | Define las fases que intercambian contracts |
| spec-002-component-boundaries.md | Define handoffs y boundary rules soportados por contracts |
| spec-003-extensibility-model.md | Define como las extensiones pueden especializar contracts sin romper el core |
| docs/templates/contracts.template.md | Template reutilizable que puede alinearse con este marco fundacional |

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