# SPEC-015 - AUC-001 Canonical Projection Consolidation

## Estado

Approved - Implemented and closed by AUC-001-P04 Exit Gate PASS.

## Fecha

2026-07-22

## Ambito

AUC-001-P04.

## Titulo

Consolidacion canonica de proyecciones analitica y ejecutiva de AUC-001.

## Decision base

Esta Specification materializa el memo arquitectonico de AUC-001-P04 emitido por Architect Agent.

La Specification no modifica SPEC-010, SPEC-011 ni SPEC-014.

La Specification no modifica P02, P03, outputs historicos, codigo, tareas ni gates.

---

## 1. Proposito

Definir de forma verificable como las proyecciones analitica y ejecutiva de AUC-001 deben derivar del mismo artefacto canonico intermedio, del mismo Knowledge Set, del mismo Recommendation Set y del Contrato de Producto Analitico vigente.

El objetivo es impedir que las proyecciones vuelvan a depender de prompts distintos, criterios narrativos independientes o transformaciones no trazables.

---

## 2. Estado canonico reconstruido

El estado real vigente de AUC-001 antes de P04 es:

* P01 cerro documentalmente SPEC-014 con `PASS`.
* P02 materializo una ejecucion real conforme a SPEC-014 y quedo cerrado con `PASS WITH DECLARED LIMITATIONS`.
* P02 persistio un nucleo comun en `outputs/auc-001/p02/2026-07-17/product-core/common-product-core.json`.
* P03 cerro una revision experimental de representacion con `PASS`, consumiendo exclusivamente P02.
* P03 demostro que la riqueza analitica mejora cuando la vista integrada de senales, la narrativa y los criterios de exito son visibles.
* P03 tambien confirmo que Presentation no puede introducir valoraciones comparativas, conocimiento nuevo ni contenido no derivado del nucleo canonico.

Los gaps dependientes de evidencia futura permanecen fuera de P04:

* revenue/CRM o conversion comercial reconciliada: `not_available`;
* causalidad creativa: `UNKNOWN`;
* metadata creativa adicional mas alla de `ad_name`: `not_available`;
* temporalidad coste-calidad completa: `partial`, condicionada por proveedor.

---

## 3. Relacion con Specifications existentes

| Specification | Rol | Relacion con SPEC-015 |
|---|---|---|
| SPEC-010 | Seleccion de proyeccion | Mantiene que Analytical y Executive son proyecciones hermanas seleccionadas desde contexto canonicalizado. |
| SPEC-011 | Transformacion por Communication Context | Mantiene que la forma puede variar si preserva equivalencia semantica. |
| SPEC-014 | Contrato de Producto Analitico AUC-001 | Define suficiencia, preguntas, vistas, cobertura, profundidad, nucleo comun y restricciones interpretativas. |

SPEC-015 no sustituye estas Specifications. Las especializa para cerrar el hueco observado entre el nucleo comun y la materializacion final de las proyecciones AUC-001.

---

## 4. Boundary de AUC-001-P04

### Incluye

* definicion del artefacto canonico intermedio para proyecciones;
* contenido compartido obligatorio;
* variaciones permitidas por proyeccion;
* reglas de equivalencia semantica;
* bloqueos por nuevo conocimiento en Presentation;
* preservacion de limitaciones, `UNKNOWN`, coverage states y recomendaciones;
* criterios de aceptacion para analytical y executive.

### Excluye

* adquisicion de evidencia;
* consultas BigQuery o BigQuery MCP;
* generacion de nuevos Evidence Sets;
* generacion de nuevos Knowledge Sets;
* generacion de nuevos Recommendation Sets;
* generacion de outputs;
* modificacion de P02 o P03;
* implementacion runtime;
* cambios de codigo;
* creacion de tareas;
* creacion de gates;
* ampliacion del Data Contract;
* resolucion de gaps dependientes de evidencia futura.

---

## 5. Artefacto canonico intermedio

### 5.1 Nombre

El artefacto canonico intermedio se denomina:

```text
Canonical Projection Source
```

### 5.2 Definicion

El `Canonical Projection Source` es el artefacto estabilizado que autoriza el contenido comun del que deben derivar todas las proyecciones de Presentation para AUC-001.

Debe construirse despues de estabilizar:

1. Context Definition.
2. Evidence Set.
3. Knowledge Set.
4. Recommendation Set.
5. Coverage Matrix SPEC-014.
6. Common Product Core.

Debe existir antes de materializar cualquier proyeccion analitica o ejecutiva.

### 5.3 Funcion

El `Canonical Projection Source` no crea evidencia, conocimiento ni recomendaciones.

Su funcion es reunir y normalizar para Presentation el contenido ya aprobado:

* contenido obligatorio compartido;
* tesis analitica autorizada;
* vista integrada de senales y combinaciones;
* patrones de decision;
* limitaciones materiales;
* `UNKNOWN`, `partial`, `not_available` y `not_applicable`;
* recomendaciones aprobadas con criterios de exito;
* restricciones de transformacion por proyeccion;
* trazabilidad minima requerida.

### 5.4 Relacion con common product core

El `common-product-core.json` de P02 es antecedente valido y evidencia experimental de la necesidad del `Canonical Projection Source`.

SPEC-015 no exige modificar ese output.

En ejecuciones futuras, el `Canonical Projection Source` debe extender conceptualmente al common core para incluir de forma explicita los elementos que P03 tuvo que reforzar en Presentation:

* vista integrada de senales y combinaciones;
* combinacion explicativa principal;
* patrones de decision;
* criterios de exito o cierre de recomendaciones;
* reglas de visibilidad de limites por proyeccion.

---

## 6. Contenido compartido obligatorio

Toda proyeccion AUC-001 debe compartir semantica e identidad con el `Canonical Projection Source` en estos elementos:

| Bloque | Contenido obligatorio |
|---|---|
| Identidad | use case, phase, periodo, cutoff, scope, fuente canonica y contrato aplicable. |
| Fuentes | fuentes autorizadas consultadas y referencias a Evidence Set. |
| Metricas canonicas | metricas aprobadas de volumen, calidad y coste-calidad, con universo y denominador. |
| Coverage | coverage states por AQ/CQ/NAQ y estados matched, lead_only, spend_only cuando apliquen. |
| Knowledge | claims, riesgos, hipotesis, conclusiones y analytical narrative estabilizada. |
| Vista integrada | senales, combinaciones, trade-offs, concentraciones, temporalidad y patrones que explican calidad. |
| Recomendaciones | recomendaciones aprobadas, categoria, prioridad, soporte, metrica primaria, guardrail, criterio de exito, ventana y condicion de revision. |
| Limitaciones | limitaciones materiales, gaps futuros, `UNKNOWN`, `partial`, `not_available` y restricciones interpretativas. |
| Exclusiones | acciones, inferencias o claims expresamente no autorizados. |
| Trazabilidad | referencias suficientes a Evidence, Knowledge, Recommendation, Coverage Matrix y Product Contract. |

Ninguna proyeccion puede omitir un bloque compartido cuando su omision cambie la lectura, el riesgo o la decision soportada.

---

## 7. Variaciones permitidas por proyeccion

### 7.1 Variaciones comunes permitidas

Presentation puede variar:

* orden de exposicion;
* densidad informativa;
* vocabulario;
* agrupacion de bloques;
* extension narrativa;
* granularidad de tablas;
* visibilidad de trazabilidad no material;
* enfasis comunicativo.

Estas variaciones son validas solo si preservan equivalencia semantica.

### 7.2 Proyeccion analitica

La proyeccion analitica debe preservar detalle suficiente para revision, auditoria y validacion metodologica.

Debe poder incluir:

* matriz de cobertura completa o equivalente;
* vistas analiticas requeridas por SPEC-014;
* lectura integrada de senales y combinaciones;
* evidencia, comparacion, interpretacion e implicacion por pregunta;
* trazabilidad explicita a Evidence, Knowledge y Recommendations;
* notas metodologicas y restricciones interpretativas;
* distincion de universos matched, lead_only y spend_only;
* criterios de exito de recomendaciones accionables.

No puede crear submodos analiticos no definidos por SPEC-010.

### 7.3 Proyeccion ejecutiva

La proyeccion ejecutiva debe condensar para decision sin convertirse en informe tecnico completo.

Puede priorizar:

* mensaje principal;
* implicacion de negocio;
* senales clave;
* decisiones recomendadas;
* riesgos y limites materiales;
* criterios de exito de experimentos o acciones;
* idea memorable.

No puede ocultar limitaciones materiales, suprimir `UNKNOWN` relevante, degradar incertidumbre a certeza, transformar hipotesis en conclusion ni presentar una recomendacion como decision ya aprobada.

---

## 8. Reglas de equivalencia semantica

Una proyeccion es semanticamente equivalente al `Canonical Projection Source` solo si cumple todas estas reglas:

| Regla | Criterio verificable |
|---|---|
| Sin claims nuevos | Todo claim narrativo existe en Knowledge, Recommendation Set, Coverage Matrix, common core o Product Contract. |
| Sin nuevas metricas | Toda metrica procede de Evidence o common core y conserva universo, denominador y cobertura. |
| Sin reinterpretacion | La proyeccion no cambia significado, causalidad, certeza, alcance ni implicacion aprobada. |
| Sin reordenacion de prioridad | La prioridad de recomendaciones y riesgos se conserva. |
| Sin derivacion entre proyecciones | Analytical y Executive derivan del `Canonical Projection Source`, no una de otra. |
| Limitaciones visibles | Toda limitacion material que afecte a una decision aparece cerca de esa decision. |
| `UNKNOWN` preservado | Ningun `UNKNOWN` se reescribe como conclusion, oportunidad confirmada o accion lista. |
| Coverage preservado | Los estados `complete`, `partial`, `not_available`, `not_applicable`, `UNKNOWN` y `blocked` no cambian durante Presentation. |
| Recomendaciones equivalentes | Categoria, prioridad, soporte, metrica, guardrail, criterio de exito y condicion de revision permanecen equivalentes. |
| Exclusiones conservadas | Acciones excluidas no reaparecen como recomendacion, insight o sugerencia implicita. |

La equivalencia no exige igualdad textual ni misma estructura documental.

---

## 9. Bloqueos por nuevo conocimiento en Presentation

Presentation debe bloquearse o quedar no conforme si ocurre cualquiera de estas condiciones:

| Condicion de bloqueo | Motivo |
|---|---|
| Introduce evidencia no presente en Evidence Set o common core. | Rompe cadena Context -> Evidence -> Knowledge -> Recommendations -> Presentation. |
| Calcula metricas nuevas o ratios no autorizados. | Crea evidencia derivada fuera de Evidence/Knowledge. |
| Introduce una comparacion historica como conclusion de producto. | Los historicos no son expected values ni fuente de conocimiento vigente. |
| Declara que el producto recupera o supera valor historico dentro de Presentation. | Es una valoracion experimental, no contenido canonico de producto. |
| Afirma causalidad creativa, causalidad de plataforma o causalidad comercial no validada. | Viola restricciones de SPEC-014. |
| Convierte `lead_only` en coste cero o `spend_only` en ausencia real de leads. | Rompe coverage states. |
| Oculta revenue/CRM `not_available` cuando afecta a decisiones de negocio. | Sobrestima accionabilidad. |
| Convierte recomendacion experimental en orden operativo definitivo. | Modifica naturaleza de Recommendation Set. |
| Reprioriza recomendaciones por conveniencia ejecutiva. | Altera Recommendation Contract. |
| Deriva Executive desde Analytical o Analytical desde Executive. | Rompe regla de proyecciones hermanas. |

Ante bloqueo, la correccion debe hacerse en el artefacto canonico correspondiente si falta contenido aprobado, o en la transformacion si el contenido existe pero fue representado incorrectamente.

Presentation no puede corregir Knowledge ni Recommendations.

---

## 10. Tratamiento de limitaciones, UNKNOWN y coverage states

### 10.1 Limitaciones

Las limitaciones deben conservar:

* descripcion;
* alcance afectado;
* decision que condicionan;
* impacto sobre recomendacion;
* condicion necesaria para resolverlas.

La proyeccion ejecutiva puede resumirlas, pero no puede eliminarlas si condicionan la decision.

### 10.2 UNKNOWN

`UNKNOWN` debe tratarse como resultado analitico valido.

Debe preservarse cuando:

* la evidencia permite observar un fenomeno pero no concluir causa;
* falta robustez suficiente para afirmar tendencia;
* no existe base para declarar ganador, desperdicio, revenue o conversion;
* una hipotesis requiere validacion posterior.

### 10.3 Coverage states

Los estados de coverage se heredan desde la Coverage Matrix y no pueden modificarse en Presentation.

Si una proyeccion condensa una pregunta `partial`, `not_available` o `UNKNOWN`, debe conservar el estado o su significado equivalente.

### 10.4 Recomendaciones

Toda recomendacion presentada debe conservar:

* ID o identidad estable;
* categoria;
* prioridad;
* Knowledge refs o soporte equivalente;
* accion;
* metrica primaria o resultado verificable;
* guardrail si aplica;
* criterio de exito o cierre;
* ventana o condicion de revision;
* incertidumbre.

Las recomendaciones excluidas por el Recommendation Set no pueden aparecer como alternativas blandas, sugerencias narrativas o implicaciones ejecutivas.

---

## 11. Responsabilidades por capa

| Capa | Responsabilidad | Prohibicion |
|---|---|---|
| Evidence | Registrar hechos, metricas y coverage observables. | Interpretar o recomendar. |
| Knowledge | Derivar findings, insights, hipotesis, conclusiones, riesgos y narrative desde Evidence. | Crear recomendaciones o consultar Presentation. |
| Recommendations | Formular acciones aprobadas, clasificadas y evaluables desde Knowledge. | Introducir acciones sin Knowledge refs. |
| Product Contract | Validar suficiencia, profundidad, coverage y separacion de capas. | Sustituir Evidence, Knowledge o Recommendations. |
| Canonical Projection Source | Preparar contenido aprobado y comun para Presentation. | Crear nuevo contenido analitico. |
| Presentation | Transformar forma segun proyeccion y Communication Context. | Crear evidencia, conocimiento, recomendaciones, prioridades o valoraciones nuevas. |

---

## 12. Criterios de aceptacion del Canonical Projection Source

El `Canonical Projection Source` es aceptable si:

* existe antes de cualquier proyeccion;
* referencia Context Definition, Evidence Set, Knowledge Set, Recommendation Set, Coverage Matrix y common core;
* declara el Product Contract aplicable;
* incluye contenido compartido obligatorio;
* incluye vista integrada de senales y combinaciones;
* incluye patrones de decision trazados a Knowledge;
* incluye recomendaciones con criterios de exito;
* incluye limitaciones y `UNKNOWN` con impacto;
* incluye exclusiones;
* incluye reglas de variacion por proyeccion;
* declara un estado de equivalencia inicial apto para Presentation;
* no contiene evidencia, conocimiento ni recomendaciones nuevos.

---

## 13. Criterios de aceptacion de la proyeccion analitica

La proyeccion analitica es aceptable si:

* declara que deriva del `Canonical Projection Source`;
* conserva todas las preguntas obligatorias y condicionales aplicables o sus equivalentes verificables;
* muestra coverage states y limitaciones materiales;
* preserva detalle suficiente de evidencia, comparacion, interpretacion, implicacion y trazabilidad;
* incluye vista integrada de senales y combinaciones;
* incluye recomendaciones con categoria, prioridad y criterio de exito;
* distingue matched, lead_only y spend_only cuando afecten a lectura economica;
* no introduce claims, metricas o recomendaciones nuevas;
* no deriva de la proyeccion ejecutiva.

---

## 14. Criterios de aceptacion de la proyeccion ejecutiva

La proyeccion ejecutiva es aceptable si:

* declara que deriva del `Canonical Projection Source`;
* conserva el mensaje principal autorizado;
* preserva implicaciones de negocio sin cambiar significado;
* muestra las senales clave que explican la calidad;
* mantiene visibles las limitaciones materiales que condicionan decision;
* conserva `UNKNOWN`, `partial` y `not_available` relevantes;
* presenta recomendaciones sin cambiar categoria, prioridad, condicion ni criterio de exito;
* no convierte hipotesis en conclusion;
* no declara causalidad no validada;
* no introduce valoraciones comparativas historicas;
* no deriva de la proyeccion analitica.

---

## 15. Criterios de aceptacion cruzados

Ambas proyecciones son aceptables como conjunto si:

* derivan del mismo `Canonical Projection Source`;
* comparten el mismo common core o fingerprint canonico;
* comparten Knowledge refs y Recommendation refs;
* conservan identico conjunto de limitaciones materiales;
* no contradicen coverage states;
* no contienen recomendaciones divergentes;
* no presentan prioridades incompatibles;
* no ocultan exclusiones;
* pasan verificacion de equivalencia semantica;
* pueden ser auditadas sin consultar prompts originales.

---

## 16. Requisitos de trazabilidad

Cada paquete futuro que reclame conformidad con SPEC-015 debe permitir reconstruir:

1. que `Canonical Projection Source` fue usado;
2. que common core o artefacto equivalente lo alimenta;
3. que Knowledge Set y Recommendation Set fueron consumidos;
4. que Product Contract aplica;
5. que proyeccion fue seleccionada segun SPEC-010;
6. que transformacion comunicativa aplica segun SPEC-011;
7. que Presentation no introdujo contenido nuevo;
8. que limitaciones y `UNKNOWN` fueron preservados.

---

## 17. Riesgos

| Riesgo | Impacto | Mitigacion |
|---|---|---|
| Convertir SPEC-015 en un prompt de redaccion | Alto | Definir artefacto intermedio, reglas verificables y bloqueos. |
| Hacer la proyeccion ejecutiva demasiado tecnica | Medio | Permitir condensacion mientras conserve limites y decision. |
| Duplicar SPEC-014 | Medio | Limitar SPEC-015 a derivacion de proyecciones, no a suficiencia del producto. |
| Generalizar prematuramente a Foundation | Alto | Mantener alcance local AUC-001. |
| Ocultar gaps futuros bajo mejor narrativa | Alto | Mantener revenue/CRM, causalidad creativa, metadata y temporalidad como gaps no resueltos. |

---

## 18. Dependencias

* `specs/spec-010-presentation-projection-selection.md`
* `specs/spec-011-communication-context-representation-transformation.md`
* `specs/spec-014-auc-001-analytical-product-contract.md`
* `docs/contracts/presentation.contract.md`
* `analytical_use_cases/auc-001/README.md`
* `.github/skills/meta-lead-quality-analysis/SKILL.md`
* `.github/skills/meta-lead-quality-analysis/RUNBOOK.md`
* `outputs/auc-001/p02/2026-07-17/product-core/common-product-core.json`
* `outputs/auc-001/p02/2026-07-17/knowledge/knowledge-set.json`
* `outputs/auc-001/p02/2026-07-17/recommendations/recommendation-set.json`
* `outputs/auc-001/p02/2026-07-17/coverage-matrix/coverage-matrix.json`
* `gates/auc-001-p02-closure-gate.md`
* `gates/auc-001-p03-experimental-closure-gate.md`
* `docs/handoffs/auc-001-p03-revalidation-handoff.md`
* `docs/evaluations/auc-001/validations/auc-001-p03-future-evidence-gaps-record.md`

---

## 19. No objetivos

SPEC-015 no pretende:

* ejecutar AUC-001;
* generar nuevos informes;
* corregir P02 o P03;
* modificar los prompts existentes;
* definir tareas de implementacion;
* abrir gates;
* consultar nuevas fuentes;
* resolver gaps dependientes de evidencia futura;
* crear una capability transversal de Foundation.

---

## 20. Criterios de aceptacion de la Specification

SPEC-015 esta lista para Reviewer Agent si:

* define el `Canonical Projection Source`;
* distingue responsabilidades entre nucleo comun, artefacto intermedio y Presentation;
* enumera contenido compartido obligatorio;
* define variaciones permitidas para analytical y executive;
* establece reglas verificables de equivalencia semantica;
* establece bloqueos por nuevo conocimiento en Presentation;
* preserva limitaciones, `UNKNOWN`, coverage states y recomendaciones;
* define criterios de aceptacion para ambas proyecciones;
* mantiene SPEC-010, SPEC-011 y SPEC-014 como dependencias;
* no modifica P02/P03;
* no introduce codigo, outputs, tareas ni gates.

---

## 21. Readiness para Reviewer Agent

La Specification queda preparada para revision metodologica por Reviewer Agent.

La revision deberia comprobar:

* consistencia con SPEC-010, SPEC-011 y SPEC-014;
* suficiencia del `Canonical Projection Source`;
* verificabilidad de las reglas de equivalencia;
* fortaleza de los bloqueos anti-nuevo-conocimiento;
* preservacion de limitaciones y gaps futuros;
* ausencia de implementacion, outputs, tareas y gates.

