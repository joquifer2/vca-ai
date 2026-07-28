# Evaluations

`docs/evaluations/` contiene evaluaciones, investigaciones, experimentos, diagnosticos y validaciones documentales. No contiene gates, decisiones estabilizadas, corpus ni outputs canonicos.

## Que pertenece aqui

- Investigations: analisis exploratorios o comparativos.
- Experiments: protocolos, paquetes y records experimentales.
- Validations: QA, readiness, equivalence, integration y test reports.
- Diagnostics: root-cause analyses, blockers, remediations y failure diagnostics.
- Historical: planes ejecutados, assessments preliminares o documentos superados que se conservan por trazabilidad.

## Que no pertenece aqui

| Tipo | Ubicacion |
|---|---|
| Gates | [../../gates/](/gates/) |
| Decisiones estabilizadas | [../decisions/](/docs/decisions/) |
| Corpus historico | [../corpus/](/docs/corpus/) |
| Outputs canonicos | [../../outputs/](/outputs/) |
| Handoffs operativos | [../handoffs/](/docs/handoffs/) |

## Scopes

| Scope | Carpeta |
|---|---|
| AUC-001 | [auc-001/](auc-001/) |
| SPEC-011 | [spec-011/](spec-011/) |
| Transversal | [transversal/](transversal/) |

## Regla local para documentos superados

Dentro de `docs/evaluations/`, los documentos superados no se eliminan. Se clasifican bajo `historical/` dentro de su scope cuando son planes ya ejecutados, assessments preliminares o registros intermedios sin vigencia operativa.

Esta regla es local para la clasificacion interna de `docs/evaluations/`. No redefine la precedencia documental general del repositorio. Para resolver conflictos entre artefactos, aplicar exclusivamente la precedencia publicada en `.github/instructions/sdd.instructions.md`.