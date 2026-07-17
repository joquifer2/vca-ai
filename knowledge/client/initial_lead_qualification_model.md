# Initial Lead Qualification Model

## (VCA) - Viaja con Álvaro

**Estado:** Activo
**Tipo:** Conocimiento gobernado
**Ámbito:** Interpretación de la calidad inicial de leads captados mediante Meta Lead Ads
**Cliente:** VCAS
**Framework relacionado:** FARO
**Documento relacionado:** `knowledge/client/ccd.md`

---

# 1. Propósito

Este documento define el modelo conceptual utilizado por el ecosistema FARO para interpretar la calidad inicial de un lead captado mediante formularios nativos de Meta Ads.

Su finalidad no es describir una implementación concreta ni un algoritmo de scoring, sino establecer el conocimiento de negocio que permite distinguir entre un formulario recibido y una oportunidad potencial de valor.

Este modelo constituye la primera capa de interpretación del embudo de captación y sirve de referencia para dashboards, análisis, automatizaciones, agentes de IA y futuras implementaciones del sistema.

---

# 2. Estado del conocimiento

El contenido de este documento corresponde al modelo actualmente implementado dentro del ecosistema FARO.

Actualmente el sistema:

* interpreta información declarada por el usuario durante la captación;
* estima la calidad inicial del lead;
* clasifica los leads en distintos niveles de prioridad;
* identifica los leads considerados **Qualified Lead**;
* proporciona una señal de calidad utilizada por Meta Conversions API;
* permite analizar la calidad de la captación.

Actualmente el sistema **no**:

* incorpora información procedente del CRM;
* evalúa el comportamiento comercial del lead;
* estima probabilidad de venta;
* recalibra automáticamente el modelo;
* utiliza aprendizaje basado en resultados comerciales.

Estas capacidades forman parte de la evolución prevista del ecosistema, pero no de la versión actualmente implementada.

---

# 3. Principios del modelo

El modelo parte de una premisa sencilla:

> No todos los formularios representan la misma probabilidad inicial de convertirse en una oportunidad real.

Por ello, la calidad inicial de un lead no debe medirse por el hecho de haber completado un formulario, sino por las señales declaradas que permiten estimar su grado de intención y su afinidad con la propuesta de valor de Viaja con Álvaro.

El objetivo del modelo es priorizar la calidad sobre el volumen.

---

# 4. Dimensiones de interpretación

La calidad inicial de un lead se interpreta combinando cuatro dimensiones principales.

## Intención

Evalúa el grado de compromiso declarado con el viaje.

La señal más representativa es la situación de los billetes de avión.

Disponer ya de los billetes representa una intención más fuerte que encontrarse todavía en una fase de exploración.

---

## Madurez temporal

Evalúa la proximidad prevista del viaje.

Un viaje cercano suele indicar una oportunidad más inmediata, mientras que un horizonte lejano refleja un proceso de decisión todavía inmaduro.

La urgencia temporal debe interpretarse siempre junto con el resto de señales.

---

## Encaje con la propuesta de valor

Evalúa el nivel de afinidad entre lo que busca el viajero y el tipo de servicio que ofrece Viaja con Álvaro.

La organización integral del viaje y las experiencias personalizadas representan un mayor grado de alineación con la propuesta de valor que la contratación de servicios aislados.

---

## Potencial del viaje

Evalúa el contexto general del desplazamiento, considerando factores como el tamaño del grupo o el alcance del viaje.

Esta dimensión no pretende estimar rentabilidad económica, sino aportar contexto para interpretar la oportunidad inicial.

---

# 5. Principios de interpretación

Las señales nunca deben analizarse de forma aislada.

Una única respuesta rara vez determina la calidad de un lead.

La interpretación debe realizarse considerando la combinación de todas las dimensiones disponibles.

El modelo representa una estimación inicial basada en información declarada.

No constituye una validación comercial.

---

# 6. Clasificación inicial

El modelo organiza los leads en cuatro niveles de prioridad.

## Tier A

Representa leads con una combinación de señales que indican una intención elevada y un buen encaje con la propuesta de valor.

Constituyen la máxima prioridad de atención.

---

## Tier B

Representa leads con buena calidad inicial, aunque con algún elemento que reduce ligeramente la confianza respecto al Tier A.

Siguen considerándose adecuados para atención prioritaria.

---

## Tier C

Representa leads cuya información declarada refleja un interés potencial, pero insuficiente para ser considerados inicialmente de alta calidad.

Pueden evolucionar favorablemente durante el proceso comercial.

---

## Tier D

Representa leads con señales iniciales débiles o insuficientes para justificar una priorización inmediata.

Esta clasificación no implica necesariamente un descarte definitivo.

---

# 7. Qualified Lead

En la versión actual del ecosistema, un **Qualified Lead** es un lead cuya calidad inicial supera el umbral establecido por el modelo de pre-cualificación.

Esta condición representa exclusivamente una estimación realizada a partir de la información disponible durante la captación.

No constituye una validación comercial ni garantiza la existencia de una oportunidad real.

El concepto de **Qualified Lead** debe entenderse siempre como una señal de marketing y nunca como una confirmación comercial.

---

# 8. Papel dentro del ecosistema FARO

El modelo de pre-cualificación constituye la primera capa de interpretación del sistema.

Su responsabilidad termina en la estimación inicial de la calidad declarada del lead.

A partir de ese momento corresponde a otros procesos del ecosistema:

* contactar al lead;
* validar la información;
* determinar su interés real;
* convertirlo, o no, en una oportunidad comercial.

Esta separación evita confundir la calidad estimada durante la captación con el resultado real obtenido posteriormente.

---

# 9. Qué no hace este modelo

Este modelo no:

* sustituye la evaluación comercial;
* determina la probabilidad de venta;
* estima el valor económico del cliente;
* incorpora información procedente del CRM;
* aprende automáticamente del comportamiento comercial;
* decide por sí mismo qué campañas deben escalarse;
* reemplaza el criterio del equipo comercial.

Su finalidad es proporcionar una estimación inicial consistente y gobernada de la calidad declarada del lead.

---

# 10. Gobierno

Este documento constituye la referencia funcional para interpretar la calidad inicial de los leads dentro del ecosistema FARO.

Las implementaciones técnicas pueden evolucionar sin modificar este conocimiento siempre que mantengan los principios aquí definidos.

Los cambios en reglas, pesos, umbrales o algoritmos deberán preservar el significado funcional del modelo o, en caso contrario, actualizar este documento para reflejar la nueva interpretación.

---

# 11. Evolución prevista

La arquitectura de FARO contempla una evolución futura hacia un sistema de aprendizaje progresivo basado en el comportamiento real de los leads.

Cuando esa capacidad exista podrán incorporarse nuevos modelos relacionados con:

* cualificación comercial;
* validación de oportunidades;
* aprendizaje basado en resultados;
* recalibración del modelo;
* mejora continua de las señales utilizadas durante la captación.

Estos elementos no forman parte del alcance del presente documento y deberán documentarse como artefactos independientes cuando sean implementados.

---

# 12. Relación con otros documentos

Este documento debe interpretarse conjuntamente con:

* `knowledge/client/ccd.md`, como fuente principal de contexto del cliente.
* `knowledge/marketing/meta-lead-qualification-framework.md`, que describe el significado de las señales obtenidas mediante el formulario de Meta.

La implementación técnica del modelo pertenece a los artefactos del proyecto FARO y no forma parte del conocimiento gobernado descrito aquí.

---

# 13. Principio rector

La calidad inicial de un lead no se mide por haber completado un formulario.

Se mide por las señales que permiten estimar, de forma consistente y gobernada, su grado de intención y su afinidad con la propuesta de valor de Viaja con Álvaro.

Este modelo transforma información declarada en conocimiento útil para la toma de decisiones, manteniendo siempre separadas la interpretación inicial y la validación comercial posterior.
