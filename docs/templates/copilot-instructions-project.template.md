# Copilot Instructions - Project

## Rol del repositorio

Este repositorio corresponde a un proyecto gestionado bajo la metodología SDD.

La gobernanza metodológica se basa en la Foundation:

```text
jqf-sdd-foundation
```

Antes de realizar cualquier trabajo, comprender el contexto, estado y artefactos oficiales del proyecto.

## Referencia metodológica principal

Antes de ejecutar cualquier tarea metodológica, revisar y respetar:

```text
.github/instructions/sdd.instructions.md
```

Este documento constituye la referencia metodológica principal del proyecto.

Si existe conflicto entre artefactos, prevalece la jerarquía definida en `sdd.instructions.md`.

## Context Governance

Antes de generar o modificar cualquiera de los siguientes artefactos:

* Project Brief
* Specifications
* Architecture
* Tasks
* Código
* Documentación técnica

comprobar si existe:

```text
docs/context_refs.md
```

Si existe:

* utilizarlo como mapa oficial de referencias;
* consultar las fuentes obligatorias indicadas;
* respetar las versiones y estados documentados;
* no sustituir contexto documentado por inferencias.

Si no existe:

* crearlo a partir del template correspondiente;
* marcar referencias faltantes como `PENDING`.

## Estado del proyecto

Antes de iniciar cualquier trabajo:

* identificar la fase SDD actual;
* revisar los artefactos existentes;
* verificar decisiones previas;
* respetar los límites definidos por la fase vigente.

No asumir que el proyecto se encuentra en Development.

## Agentes metodológicos

Cuando la tarea corresponda a una responsabilidad definida por un agente metodológico, utilizar la definición correspondiente en:

```text
.github/agents/
```

Los agentes gobiernan el proceso de evolución del proyecto.

## Skills

Cuando exista una skill aplicable, utilizarla como procedimiento de trabajo preferente:

```text
.github/skills/
```

Las skills complementan a los agentes.

No sustituyen las responsabilidades definidas por ellos.

## Uso de Templates

Antes de crear o modificar artefactos documentales, comprobar si existen templates oficiales en:

```text
docs/templates/
sdd_docs/templates/
```

Si existe un template compatible:

* utilizarlo como estructura base;
* mantener coherencia documental;
* evitar crear variantes incompatibles.

Si no existe un template adecuado:

* utilizar la convención SDD correspondiente;
* indicar que se ha utilizado una estructura inferida.

## Principios generales

* Priorizar evidencia sobre suposiciones.
* Mantener trazabilidad documental.
* Evitar implementación prematura.
* Respetar la precedencia documental.
* Mantener alineación con la fase SDD vigente.
* No inventar requisitos, restricciones o decisiones si existe una fuente oficial documentada.
* Mantener coherencia con la metodología definida por la Foundation.

## Objetivo

Asegurar que todas las decisiones, documentos y cambios realizados en el proyecto sean coherentes, trazables y compatibles con la metodología SDD.
