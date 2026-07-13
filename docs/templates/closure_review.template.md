# Closure Review Template

## Propósito

Este documento sirve como plantilla para revisiones de cierre y aceptacion de Analytical Use Cases.

Su objetivo es documentar si un caso analitico puede considerarse completo, aceptado y reutilizable desde el punto de vista documental.

No debe reutilizarse para autorizar entrada a Development.

No debe mezclarse con evaluaciones de artefactos concretos.

No debe sustituir la revision humana ni la decision del QA Gate Agent.

---

# Información General

| Campo | Valor |
|---|---|
| Review ID | |
| Review Name | |
| Review Type | Closure Review / Reconciliation / Documentary Validation |
| Analytical Use Case | |
| Status | Draft / Documented / Completed |
| Version | |
| Last Updated | |
| Owner | |
| Scope | |

---

# Objetivo Declarado

Describir en una o dos frases que se pretende validar con la revisión de cierre.

La redaccion debe dejar claro:

- que caso se cierra;
- que evidencias se usan;
- que no se reabre el analisis;
- que no se redefine ninguna fase SDD.

---

# Evidencia Consolidada Utilizada

| Artefacto | Rol en el cierre | Estado observado |
|---|---|---|
| | | |

Incluir aqui los artefactos canónicos que soportan el cierre del caso.

---

# Resumen de Cierre

## Etapa o tarea relevante

Describir cada etapa relevante del caso y su contribucion al cierre.

### Evidencia concreta

- ...
- ...
- ...

Repetir esta estructura para cada tramo de cierre relevante.

---

# Resultado Final

| Opción | Estado |
|---|---|
| Pass | |
| Pass with observations | |
| Blocked | |

Indicar la opcion seleccionada y justificarla con evidencia documental.

---

# Estado de Observaciones

| Tarea o area | Estado de las observaciones | Estado de cierre | Nota concreta |
|---|---|---|---|
| | | | |

Usar esta seccion para separar observaciones resueltas, activas, historicas o aceptadas como deuda metodologica.

---

# Deuda Aceptada

Describir de forma explicita cualquier deuda aceptada o limitacion residual.

La redaccion debe indicar:

- que se acepta;
- por que no bloquea el cierre;
- que debe permanecer visible.

---

# Consistencia Transversal

| Artefacto | Estado | Observación |
|---|---|---|
| docs/tasks.md | | |
| README.md | | |
| docs/context_refs.md | | |
| Handoffs del caso | | |
| Gate relevante | | |

Indicar si los artefactos relacionados permanecen consistentes con el cierre.

---

# Estado Real de Dependencias o MCP

Si aplica, documentar el estado real de dependencias, proveedores o integraciones que afectan al cierre.

Separar con claridad:

- evidencia ya validada;
- validaciones pendientes;
- observaciones no bloqueantes.

---

# Definition of Done

Este documento está completo cuando:

- el caso analitico queda identificado;
- la evidencia de cierre está consolidada;
- el resultado final está declarado;
- las observaciones quedan separadas por estado;
- la deuda aceptada queda explícita;
- la consistencia transversal está documentada;
- la diferencia con cualquier Phase Gate queda explícita.