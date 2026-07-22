# AUC-001 Post-P04 End-to-End Acceptance Real Execution Authorization Gate

## Metadatos

| Campo | Valor |
| --- | --- |
| Gate ID | AUC-001-POST-P04-E2E-ACCEPTANCE-REAL-EXECUTION-AUTHORIZATION-GATE |
| Caso de uso | AUC-001 - Meta Lead Quality Analysis |
| Tipo | Real Execution Authorization Gate |
| Fase origen | Posterior a AUC-001-P04 |
| Agente | QA Gate Agent |
| Fecha | 2026-07-22 |
| Decision | PASS WITH CONDITIONS |
| Ejecucion autorizada | Si, condicionada |
| Ejecutado por este gate | No |

---

## Proposito

Autorizar, si procede, una ejecucion real end-to-end de aceptacion de AUC-001 tras el cierre de P04, previa a la consolidacion integral.

La prueba debe validar que una instruccion breve en lenguaje natural permite reconstruir el contexto desde el repositorio, ejecutar AUC-001 con BigQuery MCP, generar los artefactos canonicos y materializar las proyecciones analitica y ejecutiva desde el mismo `Canonical Projection Source`.

Este gate no ejecuta el analisis, no consulta BigQuery MCP, no adquiere evidencia y no crea outputs.

---

## Decision

```text
PASS WITH CONDITIONS
```

Se autoriza al Implementation Agent a ejecutar una prueba real end-to-end de aceptacion de AUC-001 tras P04, limitada al namespace autorizado y a las condiciones de este gate.

---

## Namespace autorizado

```text
outputs/auc-001/p04-acceptance/2026-07-22/
```

Estado previo verificado por QA:

```text
namespace_exists = false
```

El namespace queda reservado como nuevo y protegido para esta prueba. No se permite escribir, sobrescribir, renombrar ni mover contenido en:

- `outputs/auc-001/2026-06-30/`;
- `outputs/auc-001/pci-001/2026-06-30/`;
- `outputs/auc-001/pci-002/2026-06-30/`;
- `outputs/auc-001/p02/2026-07-17/`;
- `outputs/auc-001/p03/2026-07-22/`.

---

## Instruccion breve autorizada para la prueba

Implementation Agent debe iniciar la prueba desde una instruccion breve, sin mencionar internamente SPEC-014, SPEC-015, P04 ni rutas de artefactos en la propia instruccion de usuario simulada:

```text
Analiza la calidad de los leads de Meta Ads y genera un informe analitico y un informe ejecutivo.
```

La ejecucion debe registrar esta instruccion original en el manifest o execution record y demostrar que el contexto, contratos, runbook, fuentes, proyecciones y restricciones se reconstruyeron desde el repositorio.

---

## Alcance autorizado

| Elemento | Autorizacion |
| --- | --- |
| Reconstruccion del contexto desde repositorio | Autorizado |
| Validacion del Data Provider | Autorizado exclusivamente via BigQuery MCP Server |
| Adquisicion de evidencia nueva | Autorizada exclusivamente via BigQuery MCP Server |
| Evidence Set | Autorizado |
| Knowledge Set | Autorizado |
| Recommendation Set | Autorizado |
| Common Product Core o nucleo equivalente | Autorizado |
| Canonical Projection Source | Obligatorio |
| Analytical report | Autorizado, derivado del CPS |
| Executive report | Autorizado, derivado del CPS |
| Validacion SPEC-014 | Obligatoria |
| Validacion SPEC-015 | Obligatoria |
| Validacion de equivalencia semantica entre proyecciones | Obligatoria |
| Persistencia en namespace nuevo | Obligatoria |

---

## Condiciones obligatorias para Implementation Agent

| ID | Condicion |
| --- | --- |
| C01 | Activar AUC-001 desde `.github/skills/meta-lead-quality-analysis/SKILL.md` y seguir `RUNBOOK.md` como orden operativo canonico. |
| C02 | Tratar la prueba como ejecucion completa, no como representacion de Evidence Set existente. |
| C03 | No usar `bq`, BigQuery CLI, clientes directos, outputs historicos, Evidence Sets anteriores ni informes anteriores como sustituto de evidencia. |
| C04 | Ejecutar Data Provider Validation en Fase 05 mediante BigQuery MCP `discover_metadata` con selectores canonicos publicados. |
| C05 | Si aparece `ERR_AUTH_REQUIRED`, `ERR_SELECTOR_INVALID`, `ERR_RESOURCE_NOT_ALLOWLISTED`, alcance no corregible o respuesta MCP no interpretable, detener la ejecucion y registrar bloqueo. |
| C06 | No ampliar fuentes, tablas, campos, Data Contract ni workspace durante la prueba. |
| C07 | Resolver periodo, cutoff, cobertura temporal y campos dependientes del proveedor conforme al Runbook; no inventar fecha inicial ni sustituir cobertura limitada por inferencia. |
| C08 | Construir y persistir Context Definition, Evidence Set, Knowledge Set y Recommendation Set antes de Presentation. |
| C09 | Generar Knowledge exclusivamente desde Evidence estabilizado, con investigacion analitica, limitaciones, `UNKNOWN` y coverage states visibles. |
| C10 | Generar Recommendations exclusivamente desde Knowledge estabilizado, con categoria, prioridad, soporte, metrica o resultado verificable, guardrail, criterio de exito y condicion de revision cuando aplique. |
| C11 | Construir `Canonical Projection Source` despues de los artefactos canonicos y antes de cualquier reporte. |
| C12 | Derivar analytical report y executive report directamente desde el mismo CPS; queda prohibida la derivacion de una proyeccion desde la otra. |
| C13 | Validar cumplimiento de SPEC-014: cobertura por preguntas, profundidad minima, vistas requeridas, robustez, separacion de capas, recomendaciones y tratamiento de limitaciones. |
| C14 | Validar cumplimiento de SPEC-015: CPS, contenido compartido obligatorio, variaciones permitidas, equivalencia semantica, bloqueos de nuevo conocimiento en Presentation y trazabilidad. |
| C15 | La Presentation no puede introducir claims, metricas, causalidad, prioridades, comparaciones historicas ni recomendaciones no presentes en CPS. |
| C16 | Los gaps revenue/CRM, causalidad creativa, metadata creativa adicional y temporalidad limitada por proveedor deben mantenerse como gaps dependientes de evidencia futura salvo que el Data Contract y la evidencia vigente autoricen expresamente otra cosa; no se pueden resolver por inferencia. |
| C17 | Persistir manifest con instruccion original, modo de ejecucion, namespace, fuentes MCP, SQL/query records, hashes o fingerprints, CPS id/fingerprint, validaciones SPEC-014/SPEC-015 y resultado de equivalencia. |
| C18 | No modificar P02, P03, outputs historicos, SPEC-010, SPEC-011, SPEC-014, SPEC-015 ni contratos base. |
| C19 | Preparar handoff a Reviewer Agent y QA Gate Agent con comandos ejecutados, artefactos generados, bloqueos si los hubo y resultados de validacion. |
| C20 | No declarar aceptacion final de la prueba; la aceptacion posterior requiere Reviewer Agent y QA Gate Agent sobre el paquete persistido. |

---

## Artefactos esperados en el namespace

El paquete debe persistir, como minimo, artefactos equivalentes a:

```text
outputs/auc-001/p04-acceptance/2026-07-22/
  execution/
    manifest.json
    context-definition.json
    data-provider-validation.json
    evidence-acquisition-record.json
    canonical-content-validation.json
    semantic-equivalence-validation.json
  evidence/
    evidence-set.json
  knowledge/
    knowledge-set.json
    analytical-investigation-record.json
  recommendations/
    recommendation-set.json
  product-core/
    common-product-core.json
    canonical-projection-source.json
  coverage-matrix/
    coverage-matrix.json
  presentations/
    analytical/
      analytical-report.md
    executive/
      executive-report.md
  validations/
    spec-014-validation.json
    spec-015-validation.json
```

Los nombres pueden variar solo si el manifest permite reconstruir inequívocamente los mismos roles.

---

## Validaciones previas ejecutadas por QA

| Validacion | Resultado |
| --- | --- |
| P04 cerrado con Exit Gate | PASS |
| SPEC-014 disponible y vigente | PASS |
| SPEC-015 disponible, aprobada e implementada | PASS |
| `python -m py_compile tools/auc_001_analytical_product_contract.py` | PASS |
| `tests/evals/auc_001_canonical_projection_source_tests.ps1` | PASS, 4 tests |
| `tests/evals/auc_001_analytical_product_contract_tests.ps1` | PASS, 11 tests |
| Namespace autorizado inexistente antes de ejecucion | PASS |

---

## Criterios de bloqueo durante la ejecucion

La ejecucion debe detenerse y no entregar paquete aceptable si ocurre cualquiera de estas condiciones:

- no se puede reconstruir contexto desde repositorio a partir de la instruccion breve;
- BigQuery MCP no valida identidad, workspace, allowlist, tablas o cobertura;
- se requiere una fuente no autorizada para completar el producto;
- una pregunta obligatoria critica queda `blocked` sin justificacion contractual aceptable;
- Evidence, Knowledge, Recommendations, CPS o Presentation se mezclan o se generan fuera de orden;
- falta el CPS antes de los reports;
- analytical y executive no comparten CPS id/fingerprint;
- Presentation introduce conocimiento nuevo;
- SPEC-014 o SPEC-015 fallan;
- se escribe fuera del namespace autorizado;
- se modifica un output historico.

---

## Handoff requerido

Al finalizar la ejecucion, Implementation Agent debe entregar un handoff con:

- instruccion breve usada;
- namespace materializado;
- resultado de Data Provider Validation MCP;
- artefactos generados;
- resultado SPEC-014;
- resultado SPEC-015;
- resultado de equivalencia semantica analytical/executive;
- confirmacion de no uso de CLI/fallback;
- confirmacion de no modificacion de outputs historicos;
- limitaciones, `UNKNOWN` y gaps futuros preservados;
- bloqueos o desviaciones, si existen.

---

## Decision formal

```text
PASS WITH CONDITIONS - REAL E2E ACCEPTANCE EXECUTION AUTHORIZED VIA BIGQUERY MCP
```

Implementation Agent puede iniciar la ejecucion real end-to-end de aceptacion AUC-001 post-P04 exclusivamente bajo las condiciones anteriores.