# Analytical Intelligence Foundation

## Foundation de Inteligencia Analitica

Analytical Intelligence Foundation (AIF) es una foundation reutilizable basada en SDD para definir la metodologia comun de analisis asistido por inteligencia artificial.

Su proposito es transformar el razonamiento analitico experto en un marco documental, modular y trazable que pueda reutilizarse en distintos dominios sin depender de una fuente de datos, un proveedor tecnologico o un runtime concreto.

Esta foundation no contiene logica de negocio, implementacion productiva ni automatizacion operativa.

---

## Proposito del repositorio

El repositorio existe para gobernar y documentar los artefactos metodologicos de AIF:

- principios de diseno y arquitectura conceptual;
- ciclo de vida del analisis;
- limites entre componentes;
- modelo de extensibilidad;
- templates reutilizables;
- instrucciones y reglas de gobierno SDD;
- referencias de contexto oficiales.

El objetivo no es automatizar la generacion de informes.
El objetivo es estandarizar el proceso de razonamiento analitico para que los informes sean un resultado trazable, no el centro del sistema.

---

## Que incluye

- metodologia analitica comun.
- ciclo de vida del analisis.
- componentes reutilizables como Framework, Skills, Routines, Templates y Contracts.
- principios arquitectonicos y criterios de separacion de responsabilidades.
- artefactos documentales para Specification y Structure.
- gobierno SDD y trazabilidad de contexto.

## Que no incluye

- runtimes de agentes.
- implementaciones productivas.
- conocimiento de cliente o dominio especifico.
- herramientas reales de BI, ETL, RAG, dashboarding o orquestacion.
- pipelines ejecutables o workflows operativos.

---

## Principios rectores

- La simplicidad prevalece sobre la complejidad.
- La reutilizacion prevalece sobre la duplicacion.
- La metodologia prevalece sobre la implementacion.
- El analisis precede a la presentacion.
- La evidencia precede a las conclusiones.
- Las responsabilidades deben permanecer claramente separadas.
- La foundation debe permanecer independiente del dominio y de las fuentes de datos.

---

## Artefactos canonicos

### Contexto y gobierno

- [docs/context_refs.md](docs/context_refs.md)
- [docs/glosario_terminos.md](docs/glosario_terminos.md)
- [.github/instructions/sdd.instructions.md](.github/instructions/sdd.instructions.md)
- [.github/copilot-instructions.md](.github/copilot-instructions.md)

### Definicion fundacional

- [project_brief.md](project_brief.md)

### Specifications iniciales

- [specs/spec-001-analytical-lifecycle.md](specs/spec-001-analytical-lifecycle.md)
- [specs/spec-002-component-boundaries.md](specs/spec-002-component-boundaries.md)
- [specs/spec-003-extensibility-model.md](specs/spec-003-extensibility-model.md)

### Templates reutilizables

- [docs/templates/project_brief.template.md](docs/templates/project_brief.template.md)
- [docs/templates/context_refs.template.md](docs/templates/context_refs.template.md)
- [docs/templates/system_overview.template.md](docs/templates/system_overview.template.md)
- [docs/templates/architecture_as_is.template.md](docs/templates/architecture_as_is.template.md)
- [docs/templates/contracts.template.md](docs/templates/contracts.template.md)
- [docs/templates/data_lineage.template.md](docs/templates/data_lineage.template.md)
- [docs/templates/retrospective_spec.template.md](docs/templates/retrospective_spec.template.md)
- [docs/templates/sdd_readiness_assessment.template.md](docs/templates/sdd_readiness_assessment.template.md)
- [docs/templates/copilot-instructions.template.md](docs/templates/copilot-instructions.template.md)
- [docs/templates/copilot-instructions-project.template.md](docs/templates/copilot-instructions-project.template.md)
- [docs/templates/AGENTS.template.md](docs/templates/AGENTS.template.md)

---

## Como leer este repositorio

1. Leer primero [docs/context_refs.md](docs/context_refs.md) para entender el contexto oficial.
2. Leer [project_brief.md](project_brief.md) para comprender el proposito y el alcance de la Foundation.
3. Revisar [specs/](specs/) para ver la definicion inicial del ciclo analitico, los limites entre componentes y el modelo de extensibilidad.
4. Consultar [docs/glosario_terminos.md](docs/glosario_terminos.md) si necesitas definiciones de artefactos o conceptos SDD.
5. Aplicar [.github/instructions/sdd.instructions.md](.github/instructions/sdd.instructions.md) antes de crear o modificar artefactos metodologicos.

---

## Estado SDD actual

Estado vigente:

- SDD -> Specification / Structure.

No estamos en Development.

Eso implica que este repositorio debe permanecer documental, no ejecutable, y no debe introducir implementacion prematura.

---

## Flujo recomendado

```text
Project Brief
↓
Context References
↓
Specifications
↓
Structure
↓
Tasks
↓
Development
↓
Validation
```

---

## Estructura del repositorio

```text
AGENTS.md
README.md

.github/
├── agents/
├── instructions/
├── prompts/
├── copilot-instructions.md
└── skills/

docs/
├── glosario_terminos.md
├── context_refs.md
└── templates/

specs/
├── spec-001-analytical-lifecycle.md
├── spec-002-component-boundaries.md
├── spec-003-extensibility-model.md
└── templates/

gates/
memory/
tests/
tools/
workflows/
```

---

## Forma de trabajo esperada

- Mantener separacion entre metodologia, gobernanza y posible implementacion futura.
- Crear artefactos reutilizables, no instancias especificas de cliente.
- Marcar ausencias de contexto como PENDING cuando corresponda.
- Evitar duplicar contenido ya cubierto por otro artefacto canonico.
- Priorizar claridad, trazabilidad y coherencia documental.

---

## Criterios de exito

Esta foundation sera util cuando:

- la misma metodologia pueda reutilizarse en distintos dominios;
- nuevas Skills puedan incorporarse sin modificar el nucleo metodologico;
- el proceso de analisis permanezca desacoplado de la presentacion;
- la evidencia pueda trazarse hasta las conclusiones y recomendaciones;
- el repositorio sirva como base comun para futuros proyectos de analisis asistido por IA.

---

## Siguiente paso recomendado

Crear specifications adicionales para contracts transversales, gates de readiness y evaluaciones documentales cuando el alcance lo requiera.