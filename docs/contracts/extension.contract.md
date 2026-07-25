# Extension Contract

## Metadata

| Field | Value |
|---|---|
| Contract ID | VCA-EXT-001 |
| Contract Name | Extension Contract |
| Contract Category | Extension Contract |
| Status | Documented |
| Version | 1.0.0 |
| Last Updated | 2026-07-12 |
| Owner | Equipo VCA |
| Source Index | [docs/contracts.md](/docs/contracts.md) |

---

## Purpose

Formalizar las reglas de entrada, salida, compatibilidad y reuso que debe declarar cualquier extension del proyecto VCA IA.

Este contract aplica a Skills, Routines, Templates y Contracts que amplian o especializan el sistema analitico sin modificar el core metodologico.

Este contract no implementa extensiones concretas.

Este contract no define packaging, instalacion, runtime ni despliegue operativo.

Este contract no permite eliminar fases, reasignar responsabilidades o mover conocimiento de dominio al core.

---

## Producer

Extension Author, con revision metodologica posterior por Reviewer, Documentation Agent o QA Gate Agent cuando aplique.

## Consumer

- Framework, para validar compatibilidad antes de usar una extension.
- Reviewer, para revisar limites y trazabilidad.
- QA Gate Agent, cuando la extension requiera gate o evidence support.
- Documentation Agent, para mantener indices, dossiers y referencias.
- Derived Project Team, cuando proponga o reutilice extensiones.

## Inputs

| Input | Description | Source |
|---|---|---|
| Core Methodology | Lifecycle, boundaries, contracts y reglas de extensibilidad que la extension debe preservar | Specs aplicables |
| Extension Candidate | Skill, Routine, Template o Contract propuesto | Extension Author |
| System Surface | Parte del sistema que la extension amplifica o especializa | Extension declaration |
| Required Contracts | Contracts que la extension necesita para operar | Extension declaration; docs/contracts.md |
| Produced Contracts | Contracts o artefactos que la extension puede emitir | Extension declaration |
| Dependency Statement | Dependencias permitidas, prohibidas y contexto requerido | Extension declaration |
| Reuse Rationale | Justificacion de reutilizacion o declaracion de alcance especifico | Extension declaration |
| Evidence Links | Specs, gates, context refs, dossiers o evaluaciones que soportan la extension | Source artifacts |

## Outputs

| Output | Description |
|---|---|
| Extension Declaration | Perfil minimo de la extension y su categoria |
| Compatibility Profile | Declaracion de limites, dependencias permitidas/prohibidas y preservacion del core |
| Reusability Profile | Declaracion de uso reusable, especifico o no reusable |
| Contract Interface | Inputs, outputs, required contracts y produced contracts |
| Boundary Impact | Capas, responsabilidades y limites afectados o preservados |
| Unknowns | Huecos, supuestos no verificados y condiciones pendientes |
| Review Readiness | Indicacion de si la extension puede pasar a dossier, review o gate |

## Critical Fields

| Field | Required | Description |
|---|---|---|
| contract_id | Yes | Identificador estable del Extension Contract |
| extension_id | Yes | Identificador unico de la extension candidata |
| extension_name | Yes | Nombre claro y estable |
| extension_category | Yes | Skill, Routine, Template o Contract |
| system_surface | Yes | Parte del sistema que amplifica o especializa |
| purpose | Yes | Valor funcional o metodologico de la extension |
| applicable_phases | Yes | Fases del lifecycle donde aplica o no aplica |
| required_contracts | Yes | Contracts necesarios para operar |
| produced_contracts | Yes | Contracts o artefactos que puede emitir |
| allowed_dependencies | Yes | Dependencias permitidas |
| forbidden_dependencies | Yes | Dependencias prohibidas |
| boundary_impact | Yes | Limites y responsabilidades afectadas o preservadas |
| compatibility_statement | Yes | Declaracion de compatibilidad con el core |
| reuse_statement | Yes | Declaracion de reuso o alcance especifico |
| evidence_links | Yes | Evidencia documental que respalda la declaracion |
| unknowns | Yes | Huecos, limitaciones y supuestos no verificados |

## Validation Rules

| Rule | Description |
|---|---|
| Core preservation | La extension no puede eliminar fases ni alterar la secuencia metodologica comun |
| Boundary preservation | La extension no puede reasignar responsabilidades entre Data Provider, Analytical Layer, Reasoning Layer o Presentation Layer |
| Input output clarity | La extension debe declarar inputs, outputs, required contracts y produced contracts |
| Domain containment | El conocimiento de dominio debe permanecer dentro de la extension, no moverse al core |
| Technology neutrality | La extension no puede imponer una tecnologia obligatoria al core fundacional |
| Reuse clarity | La extension debe declarar si es reusable, compatible especifica o no reusable |
| Unknown explicitness | Supuestos, huecos o contexto no verificado deben declararse UNKNOWN o PENDING |
| Evidence traceability | La compatibilidad debe enlazarse a specs, contracts, gates, context refs o dossiers aplicables |

## Traceability

- [project_brief.md](/project_brief.md)
- [docs/context_refs.md](/docs/context_refs.md)
- [docs/contracts.md](/docs/contracts.md)
- [docs/templates/extension_compatibility_dossier.template.md](../templates/extension_compatibility_dossier.template.md)
- [specs/spec-003-extensibility-model.md](/specs/spec-003-extensibility-model.md)
- [specs/spec-004-transversal-contracts.md](/specs/spec-004-transversal-contracts.md)
- [specs/spec-007-extension-compatibility-reusability.md](/specs/spec-007-extension-compatibility-reusability.md)
- [analytical_use_cases/meta_lead_quality_analysis.md](/analytical_use_cases/meta_lead_quality_analysis.md)
- [.github/skills/meta-lead-quality-analysis/SKILL.md](/.github/skills/meta-lead-quality-analysis/SKILL.md)
- [gates/spec-008-development-entry-phase-gate.md](/gates/spec-008-development-entry-phase-gate.md)

## Unknown Handling

| Unknown | Handling |
|---|---|
| Extension category not declared | Block review readiness until declared |
| Required contracts unclear | Mark PENDING and block compatibility claim |
| Produced contracts unclear | Mark PENDING and block downstream consumption |
| Boundary impact unclear | Block compatibility until reviewed |
| Reuse rationale missing | Mark as not reusable until evidence exists |
| Domain dependency unverifiable | Mark UNKNOWN and prevent core adoption |
| Technology dependency mandatory but unjustified | Mark incompatible with core until resolved |
| Evidence links missing | Block compatibility or reusability statement |

## Idempotency Rules

Este contract es documental y no instala ni ejecuta extensiones.

Una instancia concreta del Extension Contract debe producir la misma declaracion de compatibilidad cuando consume la misma extension candidate, las mismas specs, los mismos contracts requeridos y la misma evidencia documental.

## Dependencies

| Dependency | Type |
|---|---|
| SPEC-003 | Extensibility model |
| SPEC-004 | Contract framework |
| SPEC-007 | Compatibility and reusability framework |
| Context References | Source of Truth |
| Extension Compatibility Dossier Template | Dossier structure |
| docs/contracts.md | Contract index |

## Evidence

- SPEC-003 define Skills, Routines, Templates y Contracts como categorias de extension y exige preservar core, boundaries, dominio y neutralidad tecnologica.
- SPEC-004 reconoce el Extension Contract como categoria fundacional para declarar reglas de entrada y salida introducidas por una extension.
- SPEC-007 define metadata, compatibility profile, reusability profile y evidence links para extensiones compatibles o reusables.

## Risks

| Risk | Severity | Impact | Evidence |
|---|---|---|---|
| Extension muta el core | Important | Rompe estabilidad y reuso del sistema | SPEC-003 |
| Extension reasigna responsabilidades | Important | Rompe boundary compliance | SPEC-002; SPEC-003 |
| Reuso declarado sin evidencia | Important | Introduce acoplamiento y falsas expectativas | SPEC-007 |
| Dependencia tecnologica obligatoria | Important | Reduce neutralidad y compatibilidad del core | SPEC-003; SPEC-007 |
| Unknowns ocultos | Important | Debilita review, gates y trazabilidad | SPEC-007 |

## Definition of Done

Este contract cumple T-014 cuando:

1. Declara reglas de entrada y salida para extensiones.
2. Declara criterios de compatibilidad con el core y preservacion de boundaries.
3. Declara criterios de reuso o alcance especifico.
4. Exige required contracts, produced contracts, dependencias, evidence links y UNKNOWN handling.
5. No implementa packaging, runtime, instalacion ni una extension concreta.