# Copilot Instructions - JQF SDD Foundation

## Rol del repositorio

Este repositorio es una Foundation reutilizable basada en SDD.

No contiene lógica de negocio ni proyectos concretos.

Su propósito es proporcionar metodología, gobernanza, agentes, skills, templates y artefactos reutilizables para proyectos derivados.

## Referencia metodológica principal

Antes de ejecutar cualquier tarea metodológica, revisar y respetar:

```text
.github/instructions/sdd.instructions.md
```

Este documento constituye la referencia metodológica principal (SDD Harness) del repositorio.

Si existe conflicto entre cualquier artefacto y `sdd.instructions.md`, prevalece `sdd.instructions.md`.

## Reglas obligatorias

* No añadir referencias a clientes o proyectos específicos.
* No introducir runtime, frameworks o tools reales como implementación ejecutable dentro de la Foundation.
* No crear agentes operativos concretos.
* Mantener los artefactos reutilizables.
* Respetar la metodología SDD vigente.
* Respetar la gobernanza definida por el SDD Harness.
* Priorizar plantillas, agentes metodológicos y governance.
* Mantener separadas las capacidades de Discovery respecto a las capacidades metodológicas generales de SDD.

### Excepción metodológica controlada

Se permite mencionar tecnologías, servicios cloud o herramientas reales exclusivamente en artefactos de discovery metodológico (agentes, skills, complementos o plantillas) cuando sea necesario para reconstruir contexto As-Is de proyectos existentes.

Estas referencias deben mantenerse documentales, no ejecutables y orientadas a trazabilidad.

No deben incluir:

* despliegues;
* implementación técnica productiva;
* automatizaciones operativas;
* secretos;
* configuraciones sensibles.

## Agentes, Skills y Complementos

Cuando la tarea corresponda a una responsabilidad definida por un agente metodológico, utilizar la definición correspondiente en:

```text
.github/agents/
```

Cuando exista una skill aplicable, utilizarla como procedimiento de trabajo preferente:

```text
.github/skills/
```

Las skills complementan a los agentes.

No sustituyen las responsabilidades definidas por ellos.

Los complementos amplían capacidades específicas de las skills.

No deben utilizarse de forma aislada salvo que la skill correspondiente así lo indique.

## Uso de Templates

Antes de crear o modificar artefactos documentales, comprobar si existen templates oficiales en:

```text
docs/templates/
sdd_docs/templates/

Los templates constituyen la estructura oficial de referencia para los artefactos documentales del framework.
```
```


Si existe un template compatible:

* utilizarlo como estructura base;
* mantener coherencia con el resto del repositorio;
* evitar crear variantes incompatibles.

Si no existe un template adecuado:

* utilizar la convención SDD correspondiente;
* indicar que se ha utilizado una estructura inferida.

## Cuando trabajes en este repositorio

* Si se crea un nuevo documento, debe ser reutilizable.
* Si se propone una regla, debe ser genérica.
* Si algo es específico de proyecto, debe ir a una plantilla o quedar fuera de la Foundation.
* Si hay duda, mantenerlo como placeholder o ejemplo genérico.
* Evitar introducir implementación prematura.
* Mantener separación entre diseño, gobernanza e implementación.


## Precedencia documental

La precedencia documental oficial se define exclusivamente en:

```text
.github/instructions/sdd.instructions.md
```

No duplicar reglas de precedencia en otros documentos.

## Principio general

Esta Foundation gobierna diseño, documentación, revisión, trazabilidad y evolución controlada de capacidades bajo SDD.

No gobierna runtime, infraestructura, herramientas operativas ni implementaciones productivas.


