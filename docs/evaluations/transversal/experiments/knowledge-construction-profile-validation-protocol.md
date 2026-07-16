# Knowledge Construction Profile Validation Protocol

## Metadata

| Field | Value |
|---|---|
| Protocol ID | KCP-VALIDATION-PROTOCOL-001 |
| Protocol Name | Knowledge Construction Profile Validation Protocol |
| Status | Canonical for experimental package |
| Version | 1.0.0-remediated |
| Analytical Use Case | AUC-001 - Meta Lead Quality Analysis |
| Experiment Category | Controlled Comparative Evaluation |
| Package Manifest | docs/evaluations/transversal/experiments/knowledge-construction-experimental-package.md |
| Last Remediated | 2026-07-15 |

## 1. Objective

Definir un protocolo controlado para validar si una guia explicita de construccion de conocimiento mejora la profundidad analitica del workflow actual en AUC-001.

El protocolo compara tres condiciones sobre el mismo Evidence Set y bajo las mismas restricciones operativas disponibles.

La validacion busca decidir si la hipotesis principal puede aceptarse, rechazarse o quedar parcialmente soportada despues de evaluacion ciega. Este protocolo no ejecuta el experimento ni puntua los resultados.

## 2. Experimental Hypotheses

### Main hypothesis

Una guia explicita de construccion de conocimiento produce informes de mayor profundidad analitica que el workflow actual.

### Secondary hypotheses

- H1: Knowledge Construction Profile v0.1 mejora respecto al baseline.
- H2: Knowledge Construction Profile v0.2 mantiene la mejora con menor complejidad.
- H3: La mejora proviene principalmente de Analytical Operations, Composition Patterns y Finding Construction.

## 3. Experimental Conditions

### Condition A - Baseline

Usar el workflow actual sin ninguna guia experimental adicional durante Knowledge Generation.

### Condition B - Knowledge Construction Profile v0.1

Usar el workflow actual y aplicar `docs/experiments/knowledge-construction-profile-v0.1.md` como guia de razonamiento solo durante Knowledge Generation.

### Condition C - Knowledge Construction Profile v0.2

Usar el workflow actual y aplicar `docs/experiments/knowledge-construction-profile-v0.2.md` como guia de razonamiento solo durante Knowledge Generation.

### Constant elements across all conditions

Las tres condiciones deben mantener constantes, salvo el profile aplicado durante Knowledge Generation:

- mismo AUC: AUC-001;
- mismo Execution Context;
- mismo periodo;
- mismo Evidence Set congelado;
- mismos Evidence blocks;
- mismos Contracts;
- mismo Skill, Runbook y Checklist;
- misma Presentation Policy;
- mismo formato de salida;
- mismo orden de lectura de artefactos base;
- mismas restricciones de no reconsulta de evidencia;
- misma configuracion de modelo expuesta por el entorno.

La unica variable independiente es el mecanismo de razonamiento aplicado durante Knowledge Generation.

## 4. Controlled Variables

| Variable | Value | Control Rule |
|---|---|---|
| AUC | AUC-001 | No change |
| Execution Context | `docs/handoffs/auc-001-execution-context.md` | No change |
| Period | 2026-06-01 to 2026-06-30 | No change |
| Evidence Set | `docs/handoffs/auc-001-evidence-set.md` | No change |
| Evidence Contract | `docs/handoffs/auc-001-evidence-contract.md` | No change |
| Knowledge Contract | `docs/handoffs/auc-001-knowledge-contract.md` | No change |
| Recommendation Contract | `docs/handoffs/auc-001-recommendation-contract.md` | No change |
| Presentation Contract | `docs/handoffs/auc-001-presentation-contract.md` | No change |
| Skill | `.github/skills/meta-lead-quality-analysis/SKILL.md` | No change |
| Runbook | `.github/skills/meta-lead-quality-analysis/RUNBOOK.md` | No change |
| Checklist | `.github/skills/meta-lead-quality-analysis/CHECKLIST.md` | No change |
| Presentation Policy | `.github/presentation_policies/executive-decision-support.md` | No change |
| Model | Same available model/configuration for all runs | Record exact exposed value; do not claim unavailable details |
| Temperature | Environment-controlled if not exposed | Record as not configurable when unavailable |
| Sampling parameters | Environment-controlled if not exposed | Record as not configurable when unavailable |
| Seed/determinism | Not guaranteed unless environment exposes it | Record limitation explicitly |
| Output format | Same artifact schema | No change |
| Evaluation rubric | Criteria in this protocol | No change |

If any controlled documentary input changes after package freeze, the experiment must be blocked and the package must be refrozen.

## 5. Evaluation Criteria

Cada salida se evaluara con criterios observables, no con impresiones generales.

### Depth of Findings

Evalua si los Findings van mas alla de describir la evidencia y capturan diferencias relevantes, concentracion, trade-offs o explicaciones comparadas.

### Knowledge Quality

Evalua si el Knowledge Set consolida observaciones en insights, hypotheses, conclusions, priorities, risks y uncertainties de forma coherente.

### Insight Clarity

Evalua si los insights explican el patron observado sin perder precision ni caer en vaguedad.

### Separation Discipline

Evalua si Insight, Hypothesis y Conclusion permanecen claramente diferenciados.

### Traceability

Evalua si cada afirmacion sustantiva puede seguirse hasta evidencia identificable.

### Uncertainty Handling

Evalua si faltantes, UNKNOWNs, coverage states y limitaciones permanecen visibles.

### Executive Utility

Evalua si el informe permite lectura ejecutiva sin sacrificar rigor analitico.

### Overinterpretation Control

Evalua si la salida evita causalidad injustificada, sobrelectura de concentracion y extrapolacion fuera del coverage.

### Redundancy Control

Evalua si el informe evita repeticiones innecesarias de tablas, metricas o ideas ya estabilizadas.

### Complexity Efficiency

Evalua si la mejora obtenida justifica la complejidad adicional introducida por el profile.

## 6. Scoring Rubric

Cada criterio se puntuara de 1 a 5:

| Score | Meaning |
|---|---|
| 1 | Muy deficiente. No cumple el criterio de forma util. |
| 2 | Debil. Cumplimiento parcial y poco consistente. |
| 3 | Aceptable. Cumplimiento suficiente, pero con margen claro de mejora. |
| 4 | Bueno. Cumplimiento claro y estable. |
| 5 | Excelente. Cumplimiento sobresaliente y muy dificil de mejorar. |

### Criterion-specific guidance

- Depth of Findings: 1 = descripcion plana; 5 = findings profundos, comparados y diferenciados.
- Knowledge Quality: 1 = knowledge desordenado o fragmentado; 5 = knowledge coherente y bien consolidado.
- Insight Clarity: 1 = insights vagos; 5 = insights precisos y explicativos.
- Separation Discipline: 1 = Insight/Hypothesis/Conclusion mezclados; 5 = fronteras muy claras.
- Traceability: 1 = trazabilidad ausente; 5 = cada afirmacion relevante esta anclada.
- Uncertainty Handling: 1 = incertidumbre ocultada; 5 = incertidumbre visible y bien propagada.
- Executive Utility: 1 = inutil para lectura ejecutiva; 5 = util sin perder rigor.
- Overinterpretation Control: 1 = causalidad injustificada; 5 = lectura estrictamente acotada.
- Redundancy Control: 1 = repeticion alta; 5 = informacion compacta y sin relleno.
- Complexity Efficiency: 1 = coste no justificado; 5 = mejora clara con complejidad contenida.

### Aggregation rule

El resultado de cada condicion sera la media simple de los 10 criterios, con dos vistas adicionales:

- Primary Analytical Score: promedio de Depth of Findings, Knowledge Quality, Insight Clarity, Separation Discipline y Traceability.
- Control Score: promedio de Uncertainty Handling, Overinterpretation Control, Redundancy Control, Executive Utility y Complexity Efficiency.

## 7. Evaluation Procedure

### Step 1 - Prepare the evaluation package

Usar exactamente el paquete definido en `docs/evaluations/transversal/experiments/knowledge-construction-experimental-package.md`.

No modificar AUC, Skill, Runbook, Checklist, Contracts, Evidence, Presentation Policy ni profiles durante la ejecucion.

### Step 2 - Define all prompts before execution

Definir y guardar los tres prompts completos antes de ejecutar ninguna condicion.

Los prompts deben diferir solo en el mecanismo de razonamiento de Knowledge Generation:

- Condition A: sin profile.
- Condition B: profile v0.1.
- Condition C: profile v0.2.

### Step 3 - Run the three conditions

Ejecutar las tres condiciones con el mismo paquete de entrada, mismo formato de salida y misma configuracion de modelo expuesta por el entorno.

No ejecutar BigQuery, no consultar fuentes externas y no reutilizar Knowledge, Recommendations o Presentation de una condicion como entrada de otra.

### Step 4 - Record non-controllable variables

Registrar en cada execution record cualquier variable que el entorno no permita controlar o conocer, incluyendo temperatura, sampling, seed, determinismo y version exacta del modelo si no esta expuesta.

No declarar determinismo si el entorno no lo garantiza.

### Step 5 - Blind review

La evaluacion debe ser ciega respecto a la identidad de la condicion. Los evaluadores no deben saber si estan leyendo baseline, v0.1 o v0.2.

### Step 6 - Independent scoring

Cada evaluador puntua cada condicion de forma independiente usando esta misma rubrica.

### Step 7 - Disagreement resolution

Si dos evaluadores difieren en mas de 1 punto en un criterio, deben revisar ese criterio una segunda vez con la misma evidencia.

Si el desacuerdo persiste, un tercer evaluador actua como desempate.

### Step 8 - Record the results

Documentar para cada condicion:

- puntuacion por criterio;
- media global;
- Primary Analytical Score;
- Control Score;
- observaciones cualitativas breves;
- riesgos de interpretacion;
- decision provisional.

### Step 9 - Compare the conditions

Comparar B y C contra A, y C contra B, solo despues de completar la evaluacion ciega y abrir la clave de anonimización.

## 8. Expected Outputs

Cada condicion debe producir, en carpeta separada:

- `knowledge-set.md`
- `recommendation-set.md`
- `presentation.md`
- `execution-record.md`
- `prompt-used.md`

La preparacion de evaluacion ciega debe producir:

- `blind-review/output-x/knowledge-set.md`
- `blind-review/output-x/recommendation-set.md`
- `blind-review/output-x/presentation.md`
- `blind-review/output-y/knowledge-set.md`
- `blind-review/output-y/recommendation-set.md`
- `blind-review/output-y/presentation.md`
- `blind-review/output-z/knowledge-set.md`
- `blind-review/output-z/recommendation-set.md`
- `blind-review/output-z/presentation.md`
- `blind-review/blinding-key.md`
- `blind-review/evaluation-form.md`

## 9. Acceptance Criteria

### Success

La hipotesis principal se acepta si:

- al menos una variante experimental supera al baseline en el Primary Analytical Score;
- la mejora es consistente en al menos 4 de los 5 criterios primarios;
- no aparecen regresiones criticas en Overinterpretation Control o Traceability;
- v0.2 no es peor que v0.1 en Complexity Efficiency y mantiene una mejora comparable en el Primary Analytical Score.

### Partial success

El resultado se considera exito parcial si:

- una variante mejora solo en parte de los criterios primarios;
- la mejora es real pero pequena o inconsistente;
- la mejora viene acompañada de un coste de complejidad que reduce su valor neto;
- v0.2 mejora menos que v0.1 pero sigue siendo claramente superior al baseline en algunos criterios clave.

### Failure

El resultado se considera fracaso si:

- ninguna variante supera al baseline en el Primary Analytical Score;
- la mejora observada no es consistente entre evaluadores;
- aparecen regresiones criticas en trazabilidad, incertidumbre o control de sobreinterpretacion;
- la complejidad adicional no produce una mejora observable.

## 10. Threats to Validity

- Evaluator bias: un evaluador puede preferir una redaccion mas limpia o mas larga sin relacion con la calidad real.
- Model variability: pequenas variaciones del modelo pueden cambiar la salida aunque el paquete documental sea constante.
- Non-controllable generation settings: temperatura, sampling o seed pueden no estar expuestos por el entorno.
- Length effect: una condicion puede parecer mejor solo por producir mas texto.
- Context effect: el orden de lectura de las condiciones puede influir en la puntuacion.
- Overfitting to AUC-001: el resultado puede capturar mejoras especificas del caso sin generalizar.
- Rubric drift: si los evaluadores reinterpretan los criterios durante la revision, la comparacion pierde estabilidad.
- Hidden leakage: cualquier pista sobre la condicion puede contaminar la ceguera.
- Output format bias: una salida mas compacta puede parecer peor aunque sea mas eficiente.
- Familiarity effect: una variante parecida al workflow actual puede obtener ventaja por inercia.
- Confirmation bias: esperar mejora puede sesgar la lectura de findings similares.

## 11. Decision Matrix

| Scenario | Decision | Meaning |
|---|---|---|
| Baseline wins | Reject the hypothesis | The workflow actual remains preferred. |
| v0.1 wins | Accept the hypothesis for v0.1 | The explicit guide improves analytical depth, but its complexity must still be justified. |
| v0.2 wins | Accept the hypothesis for v0.2 | The reduced profile improves analytical depth with better efficiency. |
| v0.1 and v0.2 both beat baseline, but v0.2 is simpler | Prefer v0.2 | The smaller profile is the better experimental outcome. |
| No variant clearly wins | Inconclusive | The experiment does not support a decision yet. |
| Variants improve depth but regress traceability or uncertainty control | Reject | A depth gain that weakens methodological discipline is not acceptable. |

## 12. Reproducibility Notes

This is a Controlled Comparative Evaluation, not a Strict Reproducible Experiment.

The experiment can reproduce the documentary input package, prompts, output schema, condition definitions, blind review package and scoring rubric.

The experiment cannot guarantee bit-for-bit model output reproducibility unless the execution environment exposes and fixes model version, temperature, sampling parameters and seed.

Execution records must explicitly state:

- model identity exposed by the environment;
- model version if available;
- temperature if configurable, otherwise `not exposed / not configurable`;
- sampling parameters if configurable, otherwise `not exposed / not configurable`;
- seed or determinism support if available, otherwise `not guaranteed`;
- actual condition execution order;
- any isolation limitation.

If future tooling exposes stricter controls, the protocol may record them without changing the experimental objective.

## 13. Blocking Conditions

Block execution if any of the following is true:

- the package manifest is missing;
- the protocol is not this canonical single-version protocol;
- v0.1 or v0.2 has pending edits not intentionally included in the package freeze;
- any frozen input path is missing;
- the Execution Context, Evidence Set or Contracts no longer match the package manifest;
- any condition would require new BigQuery queries or external sources;
- prompts cannot be defined before running any condition;
- outputs from one condition would be used as input to another;
- the execution cannot record non-controllable model variables;
- blind review outputs cannot hide the condition identity.

## 14. Conclusion

This protocol defines a controlled comparison between baseline, Knowledge Construction Profile v0.1 and Knowledge Construction Profile v0.2 for AUC-001.

The decisive question is whether an explicit knowledge construction profile improves analytical depth without weakening traceability, uncertainty handling or overinterpretation control.