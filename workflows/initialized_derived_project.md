# Workflow · Initialize Derived Project

## Objetivo

Este workflow transforma una copia de **AIF Foundation** en un proyecto derivado preparado para comenzar su adaptación y desarrollo.

Su finalidad es eliminar únicamente los artefactos que documentan la construcción de la Foundation y conservar el núcleo metodológico reutilizable que servirá como base del nuevo proyecto.

No modifica specifications, agentes metodológicos ni la arquitectura de AIF Foundation.

---

# Cuándo utilizar este workflow

Ejecutar este workflow inmediatamente después de crear un nuevo repositorio a partir de **AIF Foundation** y antes de adaptar cualquier documento al nuevo proyecto derivado.

Ejemplos:

* `vca-ia`
* `bkm-ia`
* `neuvaltech-ia`

---

# Instrucciones

Actúa como **Documentation Agent**.

El repositorio actual es una copia de **AIF Foundation** que va a convertirse en un proyecto derivado.

Tu objetivo es preparar el repositorio para iniciar el proyecto sin alterar el núcleo metodológico heredado de AIF Foundation.

Realiza las siguientes acciones:

## 1. Verificar el origen

Confirma que el repositorio procede de AIF Foundation.

Si detectas que no es una copia de AIF Foundation, detén el proceso e informa del motivo.

---

## 2. Conservar el núcleo metodológico

Mantén sin modificaciones los siguientes elementos, salvo instrucción explícita:

* specifications;
* agentes metodológicos;
* templates;
* instrucciones;
* glosario;
* workflows reutilizables;
* gates reutilizables;
* evaluaciones reutilizables;
* estructura de carpetas de AIF Foundation.

No elimines ningún artefacto reutilizable de la Foundation.

---

## 3. Eliminar artefactos exclusivos de la construcción de AIF Foundation

Elimina únicamente aquellos documentos cuyo propósito sea registrar la construcción, validación, planificación o cierre de la propia AIF Foundation.

Esto incluye, por ejemplo:

- gates de cierre de la Foundation;
- handoffs utilizados exclusivamente durante el desarrollo de AIF Foundation;
- dossiers creados únicamente como demostración metodológica;
- actas o decisiones cuyo alcance sea exclusivamente la evolución de AIF Foundation;
- backlogs, tareas o planes de trabajo ya completados cuya única finalidad haya sido construir AIF Foundation.

No elimines ningún artefacto metodológico reutilizable.

Si existe duda razonable sobre un documento, consérvalo y señala la duda en el informe final.

---

## 4. Preparar los documentos que deberán adaptarse

Los documentos que definen la identidad del proyecto no deben adaptarse por sustitución de nombres. Deben regenerarse utilizando AIF Foundation únicamente como referencia metodológica y estructural

No reescribas todavía su contenido.

Prepara los siguientes documentos para su adaptación al proyecto derivado:

- `project_brief.md`
- `README.md`
- `docs/context_refs.md`

En el caso de `docs/tasks.md`:

- conservar únicamente la estructura metodológica reutilizable;
- eliminar tareas, planes de trabajo, estados y registros históricos propios de la construcción de AIF Foundation;
- preparar el backlog para que refleje exclusivamente el trabajo del nuevo proyecto derivado.

---

### Regeneración de los artefactos de identidad del proyecto

Los siguientes documentos describen la identidad del repositorio y, por tanto, **no deben adaptarse parcialmente** desde AIF Foundation:

- `README.md`
- `project_brief.md`
- `docs/context_refs.md`

Estos documentos deberán regenerarse para describir exclusivamente el proyecto derivado.

AIF Foundation debe utilizarse únicamente como referencia estructural y metodológica.

Su contenido no debe reutilizarse cuando describa la propia Foundation.

Al regenerar estos documentos:

- conservar únicamente la estructura que siga siendo útil;
- sustituir completamente cualquier contenido cuyo sujeto continúe siendo AIF Foundation;
- describir el propósito, alcance y objetivos del proyecto derivado;
- incorporar el contexto real del dominio cuando ya exista;
- reflejar los activos, fuentes de contexto y capacidades propias del proyecto;
- registrar únicamente decisiones, dependencias y conocimiento pertenecientes al proyecto derivado;
- presentar AIF Foundation exclusivamente como dependencia metodológica reutilizable;
- eliminar cualquier referencia al roadmap fundacional, evolución histórica o construcción de AIF Foundation que no aporte contexto al nuevo proyecto.

Cada documento debe cumplir además su responsabilidad específica.

#### README

Debe explicar el proyecto derivado, incluyendo como mínimo:

- qué es el proyecto;
- qué problema resuelve;
- cuál es su propósito;
- qué capacidades proporciona;
- cómo está organizado;
- su arquitectura conceptual;
- cuáles son sus artefactos principales y su Source of Truth;
- cuál es su estado SDD;
- cómo evolucionará el proyecto.

#### Project Brief

Debe definir exclusivamente el proyecto derivado, incluyendo:

- problema;
- objetivo;
- alcance;
- restricciones;
- riesgos;
- criterios de éxito;
- dependencias;
- contexto del dominio.

No debe describir AIF Foundation como objeto del proyecto.

#### Context References

Debe convertirse en el índice oficial de contexto del proyecto derivado.

Debe identificar:

- las fuentes oficiales de contexto;
- la Knowledge Base cuando exista;
- los activos reutilizables;
- las decisiones del proyecto;
- las dependencias relevantes;
- las fuentes técnicas;
- el conocimiento reutilizable;
- las reglas de carga de contexto.

No debe conservar referencias propias de la construcción o evolución de AIF Foundation.

### Criterio de validación

Un lector que únicamente disponga de estos tres documentos debe poder comprender correctamente el proyecto derivado sin necesidad de conocer previamente AIF Foundation.

Si cualquiera de ellos todavía puede interpretarse como un documento de AIF Foundation con algunos nombres sustituidos, la adaptación deberá considerarse incompleta.

---

## 5. Inicializar la Base de Conocimiento del proyecto

Evaluar si el proyecto derivado requiere una Base de Conocimiento (Knowledge Base) independiente de la documentación metodológica.

Una Base de Conocimiento agrupa el conocimiento persistente del dominio del proyecto y constituye el conjunto de artefactos que pueden ser utilizados por múltiples agentes, procesos o casos de uso sin depender de un análisis concreto.

Cuando el proyecto requiera gestionar conocimiento reutilizable, crear la estructura inicial:

```text
knowledge/
├── client/
├── domain/
├── research/
└── reports/
```

Esta estructura no forma parte de la documentación metodológica heredada de AIF Foundation, sino del conocimiento propio del proyecto derivado.

Cuando exista conocimiento previo (por ejemplo, un Client Context Document, documentación de dominio, procesos de negocio o investigación existente), incorporarlo dentro de `knowledge/` y referenciarlo posteriormente desde `docs/context_refs.md`.

No crear la Base de Conocimiento cuando el proyecto no requiera mantener conocimiento persistente separado de la documentación del repositorio.

---

## 6. Verificar coherencia

Comprueba que:

* no existen referencias rotas;
* no quedan referencias al cierre de la Foundation;
* la estructura sigue siendo consistente;
* el repositorio permanece alineado con AIF Foundation.

## 6.1 Validar la naturaleza de los artefactos conservados

Antes de conservar un documento, comprobar si su propósito es:

- describir la metodología reutilizable de AIF Foundation; o
- documentar la construcción o evolución histórica de AIF Foundation.

Solo deben conservarse los artefactos pertenecientes a la metodología reutilizable.

Los artefactos cuyo único propósito sea registrar la construcción de AIF Foundation deben eliminarse o reinicializarse según corresponda.

---

## 7. Generar informe

Entrega un informe indicando:

### Artefactos conservados

Lista de documentos reutilizados desde AIF Foundation.

### Artefactos eliminados

Lista de documentos eliminados y motivo.

### Artefactos reinicializados

Documentos que se han conservado, pero cuyo contenido operativo o histórico ha sido reiniciado para comenzar el nuevo proyecto.

Por ejemplo:
docs/tasks.md

### Artefactos pendientes de adaptación

Documentos que deberán personalizarse para el nuevo proyecto.

### Incidencias

Cualquier duda, referencia ambigua o decisión que requiera validación humana.

---

# Definition of Done

Este workflow se considera completado cuando:

* el repositorio mantiene íntegro el núcleo metodológico de AIF Foundation;
* se han eliminado únicamente los artefactos exclusivos de la construcción de la Foundation;
* los documentos específicos del proyecto han quedado identificados para su adaptación;
* no existen referencias documentales inconsistentes;
* el repositorio está preparado para comenzar la personalización del Project Brief.
* cuando el proyecto lo requiera, la estructura `knowledge/` ha sido inicializada y preparada para alojar las fuentes de conocimiento del proyecto.
* cuando el proyecto lo requiera, la Base de Conocimiento ha sido inicializada y las fuentes principales de conocimiento han quedado preparadas para ser referenciadas desde `docs/context_refs.md`.

---

# Siguiente workflow

Una vez completado este workflow, el siguiente paso es:

**Adaptar el `Project Brief` al nuevo proyecto derivado a partir de AIF Foundation.**

## Principios para adaptar el Project Brief

Al convertir AIF Foundation en un proyecto derivado, el Project Brief debe describir exclusivamente el proyecto que se va a construir y no la Foundation de la que procede.

Antes de redactarlo, aplicar las siguientes reglas:

- Considerar AIF Foundation como una dependencia metodológica y no como el objeto del proyecto.
- Describir el problema específico que resuelve el proyecto derivado.
- Incorporar el contexto real del dominio cuando ya exista y esté documentado.
- Distinguir claramente entre la plataforma existente y el sistema que se va a construir sobre ella.
- Evitar reutilizar texto del Project Brief de AIF cuando describa objetivos exclusivos de la Foundation.
- Identificar desde el inicio los principales activos existentes (plataformas, documentación, Data Providers, procesos o conocimiento reutilizable) que el proyecto consumirá.
- Plantear el proyecto como una plataforma para múltiples casos de uso cuando ese sea su propósito, evitando orientarlo a un único análisis.

### Validación del Project Brief derivado

Antes de considerar completada la adaptación, comprobar que:

- el Project Brief ya no describe AIF Foundation;
- el problema pertenece al dominio del proyecto derivado;
- el contexto de negocio sustituye al contexto fundacional;
- AIF aparece únicamente como dependencia metodológica;
- el sistema descrito consume los activos existentes del proyecto y no los redefine.