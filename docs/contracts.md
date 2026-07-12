# Contracts Index

## Purpose

This document is the index and navigation map for canonical contracts in VCA IA.

It does not contain the full contract bodies.

Each contract lives in its own file under [docs/contracts/](contracts/).

---

## General Information

| Field | Value |
|---|---|
| Project Name | VCA IA |
| Repository | vca-ai |
| Last Updated | 2026-07-12 |
| Owner | Equipo VCA |
| Model | One contract per artifact |

---

## Index Purpose

- list all canonical contracts;
- provide the entry point for human review and agent consumption;
- expose status and location for each contract;
- keep the index small and stable while contract bodies evolve independently.

---

## Canonical Structure

```text
docs/
  contracts.md
  contracts/
    context.contract.md
    data.contract.md
    discovery.contract.md
    analytical.contract.md
    evidence.contract.md
    knowledge.contract.md
    recommendation.contract.md
    presentation.contract.md
    extension.contract.md
```

---

## Contract Inventory

| Contract ID | Contract Name | Category | File | Status |
|---|---|---|---|---|
| VCA-CTX-001 | Context Contract | Context Contract | [docs/contracts/context.contract.md](contracts/context.contract.md) | Documented |
| VCA-DATA-001 | Data Provider Principal Contract | Data Contract | [docs/contracts/data.contract.md](contracts/data.contract.md) | Documented |
| VCA-DISC-001 | Discovery Contract | Discovery Contract | [docs/contracts/discovery.contract.md](contracts/discovery.contract.md) | Documented |
| VCA-ANL-001 | Analytical Contract | Analytical Contract | [docs/contracts/analytical.contract.md](contracts/analytical.contract.md) | Documented |
| VCA-EVD-001 | Evidence Contract | Evidence Contract | [docs/contracts/evidence.contract.md](contracts/evidence.contract.md) | Documented |
| VCA-KNW-001 | Knowledge Contract | Knowledge Contract | [docs/contracts/knowledge.contract.md](contracts/knowledge.contract.md) | Documented |
| VCA-REC-001 | Recommendation Contract | Recommendation Contract | [docs/contracts/recommendation.contract.md](contracts/recommendation.contract.md) | Documented |
| VCA-PRS-001 | Presentation Contract | Presentation Contract | [docs/contracts/presentation.contract.md](contracts/presentation.contract.md) | Documented |
| VCA-EXT-001 | Extension Contract | Extension Contract | [docs/contracts/extension.contract.md](contracts/extension.contract.md) | Documented |

---

## Critical Contracts

| Contract | Impact | Notes |
|---|---|---|
| VCA-CTX-001 | High | Delimits objective, scope, restrictions and official sources before Discovery |
| VCA-DATA-001 | High | Defines the data exposure boundary before Discovery and preparation |

---

## Maintenance Rules

- add a new file in [docs/contracts/](contracts/) for each new canonical contract;
- keep this index synchronized with the actual files and their status;
- do not expand contract bodies inside this file;
- preserve stable contract IDs across migrations and revisions.

---

## Related Artifacts

- [project_brief.md](../project_brief.md)
- [docs/context_refs.md](context_refs.md)
- [docs/tasks.md](tasks.md)
- [specs/spec-001-analytical-lifecycle.md](../specs/spec-001-analytical-lifecycle.md)
- [specs/spec-002-component-boundaries.md](../specs/spec-002-component-boundaries.md)
- [specs/spec-004-transversal-contracts.md](../specs/spec-004-transversal-contracts.md)
- [gates/spec-008-development-entry-phase-gate.md](../gates/spec-008-development-entry-phase-gate.md)
- [docs/templates/contracts.template.md](templates/contracts.template.md)

---

## Migration Notes

The Context Contract and the Data Contract have been migrated out of the former monolithic document into their canonical locations under [docs/contracts/](contracts/).

The initial transversal contract block VCA-CTX-001 through VCA-EXT-001 is now materialized as individual canonical artifacts under [docs/contracts/](contracts/).
