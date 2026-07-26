# CCD - Viaja con Álvaro

Fecha de creación: 28 de junio de 2026 12:08
🧑 Clientes: Viaja con Alvaro (https://app.notion.com/p/Viaja-con-Alvaro-3582fcf6211d805689d2fd6be5ad5296?pvs=21)
Estado: Activo
Resumen: Diseño y comercialización de viajes personalizados a España para viajeros puertorriqueños y su diáspora
Uso IA : Yes

# **Índice**

1. Identidad del Cliente
2. Resumen Ejecutivo
3. Modelo de Negocio
4. Mental Model
5. Objetivos Estratégicos
6. Problemas de Negocio Identificados
7. Restricciones Conocidas
8. Ecosistema Tecnológico
9. Arquitectura Actual
10. KPIs Oficiales
11. Glosario de Negocio
12. Proyectos Realizados
13. Decisiones Relevantes
14. Conocimiento del Dominio
15. Aprendizajes Reales
16. Oportunidades Detectadas
17. Referencias Documentales
18. Preferencias del Cliente
19. Riesgos Actuales
20. Relaciones
21. Metadatos
22. Instrucciones para IA
23. Estado del Documento

# **1. Identidad del Cliente**

cliente:

nombre: Viaja con Álvaro (VCA)

marca_comercial: Viaja con Álvaro
abreviatura: VCA

sector: Turismo

subsector: Agencia de viajes experienciales y turismo receptivo

tipo_negocio: Agencia especializada en viajes personalizados y experiencias premium en España

pais_principal: España

mercado_principal: Puerto Rico

mercados_secundarios:

- Comunidad puertorriqueña (diáspora), especialmente Florida (EE. UU.)
- Mercado hispanohablante interesado en viajar a España

web: [https://viajaconalvaro.com](https://viajaconalvaro.com/)

estado_relacion: Cliente activo

contactos_principales:

- nombre: Álvaro García Cañizares
cargo: Fundador y Director
email:
rol: Dirección general, desarrollo de negocio y marca personal

fecha_inicio_relacion:

responsable_cuenta: Jordi Quiroga

# **2. Resumen Ejecutivo**

# **Descripción General**

Viaja con Álvaro es una agencia especializada en el diseño y comercialización de viajes personalizados a España para viajeros puertorriqueños y su diáspora, con un posicionamiento basado en la especialización, la confianza y la creación de experiencias de alto valor.

Dentro del ámbito de actuación de VCA Project, la colaboración se centra en el diseño, implantación y evolución del ecosistema de captación, inteligencia comercial, analítica y automatización que soporta el proceso de adquisición de clientes.

Este ecosistema se articula principalmente sobre el framework estratégico **FARO**, la plataforma de datos **CLARO**, las integraciones con plataformas externas (Meta Conversions API, GIAV y otros sistemas) y el conjunto de dashboards, modelos de datos y procesos de decisión asociados.

# **Situación Actual**

Actualmente dispone de una arquitectura funcional que diferencia las capas de Atención, Activación y Comercial, un modelo de pre-cualificación inicial de leads, una plataforma de datos centralizada en BigQuery y una integración operativa con Meta Conversions API mediante el envío del evento `QualifiedLead`. 

El alcance actualmente implementado del modelo se limita a la información declarada durante la captación mediante formularios nativos de Meta.

El sistema calcula un Score Inicial, clasifica los leads en los tiers A, B, C y D e identifica como Qualified Lead aquellos que cumplen los criterios vigentes. 

La integración con GIAV, la incorporación sistemática de información comercial, la validación de oportunidades y el aprendizaje basado en resultados forman parte de la evolución prevista del ecosistema y todavía no están implementados de forma completa y gobernada. 

El objetivo de esta evolución es cerrar progresivamente el ciclo entre captación, pre-cualificación, resultado comercial y optimización, manteniendo siempre diferenciadas las capacidades disponibles de las capacidades previstas.

# **Alcance del CCD**

Este Client Context Document describe el cliente exclusivamente desde el ámbito de responsabilidad de VCA.

Su alcance comprende la estrategia de captación, publicidad digital, inteligencia comercial, analítica, plataforma de datos, automatización, integraciones y sistemas de apoyo a la decisión desarrollados o mantenidos por VCA Project.

No pretende documentar la totalidad del negocio de Viaja con Álvaro ni sus procesos internos de operaciones, organización o gestión empresarial. Estos aspectos únicamente se incluyen cuando resultan necesarios para proporcionar contexto al ecosistema descrito en este documento.

Este documento constituye la fuente principal de contexto permanente del cliente dentro del ámbito cubierto por este CCD. Puede ser utilizado por múltiples proyectos, agentes de IA y procesos que requieran conocimiento del negocio. Los proyectos derivados deberán referenciar este documento como fuente de contexto cuando resulte aplicable, evitando duplicar la información aquí contenida y manteniendo este CCD como referencia canónica del contexto del cliente.

# **3. Modelo de Negocio**

modelo_negocio:

tipo:

Agencia de viajes experienciales especializada en turismo receptivo en España para viajeros puertorriqueños y la diáspora puertorriqueña, basada en una estrategia de marca personal, comunidad y experiencias premium.

productos_servicios:

- Tours privados en España.
- Paquetes de viaje personalizados.
- Viajes en grupo de edición limitada (Bori Tours).
- Experiencias gastronómicas, culturales y enológicas.
- Travel Coaching para planificación del viaje.
- Guías de viaje propias.
- Asesoramiento integral del viaje.
- Gestión de hoteles y otros servicios turísticos.

fuentes_ingresos:

- Venta de tours privados.
- Venta de paquetes turísticos.
- Venta de viajes experienciales de grupo.
- Venta de sesiones de Travel Coaching.
- Venta de guías de viaje.
- Margen sobre servicios turísticos comercializados.

mercados:

- Puerto Rico (mercado principal).
- Diáspora puertorriqueña, especialmente Florida (EE. UU.).
- Mercado hispanohablante interesado en viajar a España.

clientes_objetivo:

- Viajeros puertorriqueños.
- Puertorriqueños residentes en EE. UU.
- Parejas.
- Familias.
- Pequeños grupos.
- Viajeros que priorizan experiencias auténticas y personalizadas sobre el turismo convencional.

proceso_comercial:

- Generación de audiencia mediante contenido y marca personal.
- Construcción de confianza a través de redes sociales, testimonios y eventos.
- Captación de leads mediante la web, WhatsApp y formularios.
- Asesoramiento personalizado.
- Diseño del viaje o selección de experiencia.
- Reserva y pago.
- Ejecución del viaje.
- Fidelización mediante una experiencia diferencial y recomendaciones.

propuesta_valor:

No vende únicamente viajes a España. Vende experiencias cuidadosamente diseñadas, personalizadas y acompañadas, apoyándose en la confianza generada por la marca personal de Álvaro y en una comunidad de viajeros principalmente puertorriqueños.

# **4. Mental Model**

## **Cómo debe entenderse este negocio**

- El producto no es un viaje, sino una experiencia transformadora y emocional en España.
- El principal activo del negocio es la confianza generada por la marca personal de Álvaro y la comunidad que ha construido, especialmente en Puerto Rico.
- El cliente compra tranquilidad, cercanía, autenticidad y la seguridad de sentirse acompañado durante todo el proceso, más que un itinerario turístico.
- La diferenciación no reside en ofrecer destinos exclusivos, sino en la forma de vivirlos: grupos reducidos, atención personalizada, experiencias locales y cuidado del detalle.
- El negocio se basa en relaciones a largo plazo. Un viajero satisfecho se convierte en prescriptor y genera nuevas oportunidades mediante recomendaciones y redes sociales.
- La estrategia comercial debe priorizar la generación de confianza antes que la venta directa. El contenido, los testimonios y las experiencias compartidas son parte esencial del proceso de captación.
- El mercado objetivo no es el turista internacional en general, sino principalmente el viajero puertorriqueño y la diáspora puertorriqueña, cuya cultura, lenguaje y forma de comunicarse deben estar presentes en toda la estrategia.

## **Factores críticos de éxito**

- Mantener una reputación excelente y un alto nivel de satisfacción del viajero.
- Continuar fortaleciendo la marca personal y la comunidad alrededor de Viaja con Álvaro.
- Diseñar experiencias memorables que generen recomendaciones orgánicas y repetición de compra.
- Comprender profundamente la cultura y las expectativas del cliente puertorriqueño.
- Mantener una comunicación cercana, auténtica y altamente personalizada durante todo el ciclo del viaje.

## **Factores que suelen generar problemas**

- Comunicar el servicio como un viaje convencional en lugar de una experiencia diferencial.
- Escalar el negocio sacrificando la atención personalizada o la calidad de la experiencia.
- Captar volumen de leads sin mantener la calidad y afinidad con el cliente ideal.
- Depender excesivamente de un único canal de captación o de la marca personal sin desarrollar activos complementarios.
- No gestionar adecuadamente las expectativas del viajero antes del inicio del viaje.

# **5. Objetivos Estratégicos**

objetivos:

- Consolidarse como la marca de referencia para los viajeros puertorriqueños que desean descubrir España mediante experiencias auténticas y personalizadas.
- Incrementar el volumen de viajeros manteniendo un posicionamiento premium basado en la calidad de la experiencia, evitando competir por precio.
- Fortalecer la marca personal de Álvaro como principal generador de confianza, diferenciación y captación de nuevos clientes.
- Desarrollar una comunidad de viajeros fieles que impulse la recomendación, la repetición de compra y el crecimiento orgánico de la marca.
- Diversificar la oferta de experiencias y viajes temáticos de edición limitada para aumentar el valor medio por cliente y la diferenciación.
- Escalar el negocio mediante la estandarización de procesos y el crecimiento del equipo, preservando la atención personalizada que caracteriza a la marca.
- Consolidar el liderazgo en el mercado puertorriqueño y ampliar progresivamente la presencia entre la diáspora puertorriqueña, especialmente en Florida (EE. UU.).
- Expandir el modelo de negocio hacia el mercado hispanohablante interesado en viajar a España, adaptando la propuesta de valor y la estrategia de comunicación sin perder el posicionamiento diferencial de la marca.

# **6. Problemas de Negocio Identificados**

problemas:

- Alta dependencia de la marca personal de Álvaro como principal activo para la captación, generación de confianza y conversión de nuevos clientes.
- Mercado objetivo relativamente limitado (Puerto Rico), lo que condiciona el crecimiento orgánico y obliga a maximizar la eficiencia de la captación o expandirse hacia nuevos mercados.
- El valor diferencial del servicio no siempre es evidente para clientes que comparan únicamente precio o paquetes turísticos tradicionales, por lo que es necesario educar al mercado antes de vender.
- Una parte importante del mercado potencial todavía no percibe el valor de contratar un servicio especializado para organizar un viaje a España. Muchos viajeros desconocen las ventajas de una experiencia personalizada frente a la planificación por cuenta propia, lo que hace necesario desarrollar estrategias de generación de conciencia, educación y construcción de confianza antes de la venta.
- Escalar el negocio sin perder el nivel de personalización, cercanía y calidad de la experiencia que constituye su principal ventaja competitiva.
- Dependencia significativa de canales digitales (especialmente redes sociales y contenido) para alimentar el embudo comercial.
- Necesidad de diversificar progresivamente los mercados de captación hacia la diáspora puertorriqueña y otros segmentos hispanohablantes interesados en viajar a España.
- Convertir el conocimiento, la reputación y la comunidad construidos alrededor de la marca en activos escalables (eventos, experiencias temáticas, productos digitales y programas de fidelización) que reduzcan la dependencia de la venta individual de viajes.

# **7. Restricciones Conocidas**

Una **restricción** no es un problema ni un objetivo, sino una condición que limita las decisiones del negocio.

De la información pública y del conocimiento que tenemos del cliente…

restricciones:

- El negocio debe mantener un alto nivel de personalización y acompañamiento durante todo el ciclo del viaje, ya que constituye uno de sus principales elementos diferenciales.
- La propuesta de valor está fuertemente vinculada a la marca personal de Álvaro, por lo que cualquier estrategia de crecimiento debe preservar la autenticidad y la confianza construidas alrededor de ella.
- La expansión del negocio no debe comprometer la calidad de las experiencias ni la satisfacción del viajero, incluso si ello limita la velocidad de crecimiento.
- La actividad depende de terceros (aerolíneas, hoteles, proveedores locales, bodegas, restaurantes y otros operadores turísticos), por lo que parte de la experiencia final queda condicionada por estos colaboradores.
- El negocio está sujeto a la normativa aplicable a agencias de viajes y viajes combinados, incluyendo requisitos legales, seguros, condiciones de contratación y protección del viajero.
- El mercado principal continúa siendo Puerto Rico, por lo que la comunicación, el contenido y la estrategia comercial deben adaptarse a las particularidades culturales y lingüísticas de este público mientras se desarrolla la expansión hacia otros mercados.

# **8. Ecosistema Tecnológico**

crm:

- GIAV
    
    CRM propio del cliente utilizado como destino comercial para la sincronización de leads preparados desde BigQuery/CLARO.
    

erp:

- 

ads:

- Meta Ads
    
    Canal principal de captación documentado actualmente, especialmente mediante formularios nativos de Meta Lead Ads.
    

analytics:

- Meta Events Manager
- Meta Dataset / Events Manager

data_platform:

- Google BigQuery
- Google Cloud Platform
- dbt / SQL models dentro de CLARO
- Secret Manager

visualizacion:

- Looker Studio

automatizacion:

- BigQuery Scheduled Queries
- Cloud Functions 2nd gen
- Cloud Scheduler
- Cloud Run / Cloud Run Job
- Meta Conversions API
- Webhooks / workers HTTP

otros_sistemas:

- Sitio web corporativo HTML
- Formularios nativos de Meta Lead Ads
- WhatsApp Business
- GitHub
- CLARO
- FARO
- GIAV
- Meta CAPI Worker

componentes_relevantes:

- CLARO: capa de modelado, scoring, preparación de leads y control técnico en BigQuery.
- FARO: sistema estratégico de captación, scoring inicial y activación de señales hacia Meta.
- GIAV: CRM propio del cliente y destino comercial de los leads preparados.
- Meta CAPI Worker: worker HTTP desplegado en Cloud Functions 2nd gen para enviar eventos `Lead` y `QualifiedLead` desde BigQuery hacia Meta Conversions API.
- BigQuery control layer: tablas y vistas operativas para colas, estados de sincronización y control de procesamiento.

# **9. Arquitectura Actual**

## **Arquitectura de Negocio**

Este apartado documenta exclusivamente la arquitectura correspondiente al ámbito gestionado dentro del proyecto VCA: estrategia de captación, publicidad digital, plataforma de datos, inteligencia comercial, automatización, activación y reporting.

La arquitectura se organiza en cinco capas funcionales:

```
Captación
    ↓
FARO
(Estrategia e Inteligencia Comercial)
    ↓
CLARO
(Data Platform y Materialización Técnica)
    ↓
Integraciones
    ↓
Reporting y Analítica
```

Cada capa tiene una responsabilidad claramente definida y desacoplada del resto del ecosistema.

---

## **Arquitectura Tecnológica**

```
                  Meta Ads
                      │
              Meta Lead Forms
                      │
                      ▼
                    FARO
─────────────────────────────────────────────
• Estrategia de captación
• Investigación de mercado
• Posicionamiento
• Sistema de decisión
• Framework de campañas
• Sistema de scoring
• Señales de atención
• Señales de activación
• Contratos lógicos
• Dashboards funcionales
─────────────────────────────────────────────
                      │
                      ▼
                   CLARO
─────────────────────────────────────────────
• Google BigQuery
• Modelos dbt / SQL
• Procedures
• Seeds
• Control de pipelines
• Materialización técnica
• Gobierno del dato
• Fuente única de verdad
─────────────────────────────────────────────
          │                    │
          │                    │
          ▼                    ▼
 Meta CAPI Worker        Looker Studio
          │
          ▼
 Meta Conversions API
          │
          ▼
 Meta Events Manager

          │
          ▼
GIAV CRM
(Integración actualmente en desarrollo por el proveedor del CRM)
```

---

## **Responsabilidades por plataforma**

### Captación

Responsable de la adquisición de nuevos leads mediante campañas digitales.

Componentes actuales:

- Meta Ads
- Formularios nativos de Meta

---

### FARO — Estrategia e Inteligencia Comercial

FARO constituye la plataforma funcional del ecosistema.

Define la estrategia, la lógica comercial y los criterios de decisión que posteriormente serán materializados técnicamente.

Responsabilidades:

- Investigación de mercado.
- Estrategia de captación.
- Framework de campañas.
- Sistema de decisión.
- Posicionamiento.
- Definición del scoring.
- Definición de señales de atención.
- Definición de señales de activación.
- Alineación Marketing–Comercial.
- Definición de dashboards funcionales.
- Definición de contratos lógicos que posteriormente consume CLARO.

---

### CLARO — Data Platform

CLARO constituye la plataforma de datos del ecosistema.

Su función es materializar técnicamente la lógica definida por FARO y convertirla en modelos analíticos operativos.

Responsabilidades:

- Ingesta de datos.
- Modelado mediante dbt y SQL.
- Materialización de contratos analíticos.
- Normalización y calidad del dato.
- Gobierno del dato.
- Gestión de pipelines.
- Materialización de estructuras físicas.
- Fuente única de verdad para captación, scoring, activación y reporting.

Infraestructura principal:

- Google BigQuery
- dbt
- Procedures SQL
- Scheduled Queries
- Tablas de control
- Seeds

---

### Integraciones

Responsable de sincronizar la información preparada por CLARO con plataformas externas.

Estado actual:

- Meta Conversions API mediante Meta CAPI Worker (operativo).

Estado previsto:

- Integración con GIAV CRM para sincronización automática de leads preparados y señales comerciales (actualmente en desarrollo por el proveedor del CRM).

Principio arquitectónico:

Las integraciones consumen información preparada por CLARO. No contienen lógica de negocio.

---

### Reporting y Analítica

Responsable de proporcionar visibilidad operativa y soporte a la toma de decisiones.

Componentes:

- Looker Studio
- Dashboards definidos por FARO y alimentados por CLARO

---

## **Principios Arquitectónicos**

- FARO constituye la capa estratégica del ecosistema y define la lógica de negocio.
- CLARO constituye la plataforma de datos y materializa técnicamente las definiciones realizadas por FARO.
- BigQuery es la infraestructura central sobre la que opera CLARO.
- CLARO es la fuente única de verdad para el ecosistema de captación y datos.
- Los workers de integración únicamente sincronizan información; no implementan reglas de negocio.
- Las plataformas externas (Meta, GIAV y futuras integraciones) consumen datos preparados por CLARO.
- La arquitectura está desacoplada para permitir incorporar nuevos canales, CRMs o plataformas sin modificar la lógica central de FARO ni la plataforma de datos CLARO.

---

## **Artefactos Arquitectónicos**

La arquitectura del ecosistema se documenta de forma modular. Cada uno de los siguientes artefactos constituye la fuente de verdad para un ámbito específico de la solución.

- **FARO — Estrategia e Inteligencia Comercial**
    
    Documentación principal: `FARO/`
    
- **CLARO — Plataforma de Datos**
    
    Documentación principal: `CLARO/`
    
- **GIAV — Integración con el CRM**
    
    Documentación principal: `GIAV/`
    
- **Meta CAPI Worker — Integración con Meta Conversions API**
    
    Documentación principal: `meta-capi-worker/README.md`
    

# **10. KPIs Oficiales**

Este apartado documenta los KPIs oficiales del ecosistema FARO/CLARO para captación, lectura de señal, activación comercial y toma de decisiones.

Todos los dashboards, análisis, automatizaciones y agentes de IA deberán utilizar estas definiciones como referencia oficial.

---

## **KPIs Oficiales**

### KPI 1 — CPAU v1 (Coste por Atención Útil)

**Dominio:** FARO Atención

**Definición**

Coste medio necesario para generar una unidad de atención útil en campañas clasificadas como `ATTENTION`.

**Fórmula**

```
CPAU = Spend / Atención útil
```

**Objetivo**

Medir la eficiencia de las campañas de Atención para identificar qué conceptos, ángulos y creatividades generan consumo útil de contenido.

---

### KPI 2 — % Activación Cualificada

**Dominio:** FARO Activación

**Definición**

Porcentaje de la audiencia impactada que genera una respuesta considerada útil dentro de la fase de Activación.

**Fórmula**

```
Leads cualificados / Audiencia impactada relevante
```

**Objetivo**

Evaluar la capacidad del retargeting para transformar interés previo en oportunidades útiles.

---

### KPI 3 — CPL Cualificado

**Dominio:** FARO Comercial

**Definición**

Coste medio necesario para generar un lead pre-cualificado según las reglas oficiales de FARO.

En la versión actual del sistema corresponde a los leads clasificados como **A + B**.

**Fórmula**

```
Inversión publicitaria / Leads cualificados
```

**Objetivo**

Es el KPI principal para la toma de decisiones de inversión.

Tiene prioridad sobre el CPL total.

---

### KPI 4 — Tasa de Cualificación

**Dominio:** FARO Comercial

**Definición**

Porcentaje de leads captados que alcanzan la categoría de lead cualificado según el sistema FARO.

**Fórmula**

```
Leads cualificados / Leads totales
```

**Objetivo**

Medir la calidad de la captación.

---

### KPI previsto — Ratio Lead Cualificado → Oportunidad

**Dominio:** FARO Comercial

**Estado:** No implementado actualmente

**Definición prevista**

Porcentaje de leads pre-cualificados por FARO que, tras la evaluación comercial, avanzan hasta convertirse en una oportunidad.

**Fórmula prevista**

Oportunidades / Leads cualificados

**Objetivo previsto**

Contrastar la estimación inicial realizada durante la captación con el avance comercial real de los leads.

Este indicador requiere una definición gobernada de oportunidad y la integración sistemática de información procedente del proceso comercial.

Actualmente no debe utilizarse como KPI oficial disponible del sistema.

---

### KPI previsto — Ratio Oportunidad → Venta

**Dominio:** Proceso comercial

**Estado:** No implementado actualmente

**Definición prevista**

Porcentaje de oportunidades comerciales que finalmente se convierten en venta.

**Fórmula prevista**



Ventas / Oportunidades


**Objetivo previsto**

Medir la eficacia del proceso comercial posterior a la captación.

Este indicador depende de la integración gobernada con GIAV y de la disponibilidad de estados comerciales consistentes.

Actualmente no debe utilizarse como KPI oficial disponible de FARO/CLARO.

---

## **Variables Estratégicas del Sistema**

Las siguientes variables forman parte del modelo de decisión actualmente implementado en FARO, pero **no constituyen KPIs**. 

Se utilizan para clasificar, segmentar y enriquecer la interpretación de los indicadores anteriores. 

- Score Inicial. 
- Lead Tier (A, B, C y D). 
- Qualified Lead. 
- `campaign_signal` (`ATTENTION`, `ACTIVATION` y `COMMERCIAL`). 
- Estados FARO (`CLEAR`, `WEAK` y `NOISE`, según la capa correspondiente). 

La validación comercial, un posible Score Validado y el aprendizaje basado en resultados forman parte de la evolución prevista del ecosistema y no deben considerarse variables actualmente disponibles.

---

## **Notas de Gobierno**

- Cada capa de FARO (Atención, Activación y Comercial) posee sus propios KPIs y no deben compararse entre sí utilizando un único indicador.
- El **CPL Total** puede utilizarse como métrica de contexto, pero nunca como KPI principal de decisión cuando exista un **CPL Cualificado**.
- Las definiciones de los KPIs deberán mantenerse alineadas con los contratos funcionales de FARO y los contratos analíticos de CLARO.

# **11. Glosario de Negocio**

Este apartado constituye el glosario oficial del ecosistema FARO/CLARO.

Su objetivo es establecer un lenguaje común para todos los proyectos, dashboards, automatizaciones, modelos analíticos y agentes de IA.

Todas las definiciones recogidas en este documento deberán considerarse la referencia oficial del proyecto.

---

# Flujo conceptual del sistema

El flujo debe diferenciar entre las capacidades actualmente implementadas y la evolución prevista del ecosistema. ## Estado actualmente implementado

```
Lead
│
▼
Modelo de Pre-cualificación Inicial FARO
│
▼
Score Inicial
│
▼
Lead Tier
(A, B, C o D)
│
▼
Qualified Lead
(Pre-cualificación de marketing)
│
▼
Evento QualifiedLead
(Meta Conversions API)

```
## Evolución prevista

```
Qualified Lead
│
▼
Evaluación Comercial
│
▼
Cualificación Comercial
│
▼
Oportunidad
│
▼
Cliente
│
▼
Aprendizaje y recalibración

```
La integración sistemática de información comercial, la validación de oportunidades, la recalibración del scoring y el aprendizaje basado en resultados todavía no forman parte de la versión actualmente implementada.

---

## Lead

Persona que ha mostrado interés en los servicios de Viaja con Álvaro mediante un formulario de captación o cualquier otro canal integrado en el ecosistema.

Representa la unidad mínima de análisis del sistema FARO.

---

## Modelo de Pre-cualificación Inicial FARO 

Modelo oficial utilizado por FARO para interpretar la calidad inicial de los leads captados mediante formularios nativos de Meta Ads. Su finalidad es estimar, antes de cualquier interacción comercial, el grado inicial de intención y afinidad del lead con la propuesta de valor de Viaja con Álvaro. 

El modelo utiliza exclusivamente información declarada durante la captación. Actualmente: 
- calcula un Score Inicial; 
- clasifica los leads mediante los tiers A, B, C y D; 
- identifica los leads considerados Qualified Lead; 
- permite generar el evento `QualifiedLead` para Meta Conversions API. 

El modelo no incorpora actualmente información procedente del CRM, evaluación comercial, oportunidades, ventas ni aprendizaje basado en resultados comerciales. La interpretación funcional del modelo se documenta en: `knowledge/scoring/initial-lead-qualification-model.md` 

Las reglas de cálculo, ponderaciones y umbrales concretos pertenecen a la implementación funcional y técnica de FARO/CLARO.

---

## Score Inicial

Puntuación obtenida por un lead tras aplicar el Modelo de Pre-cualificación Inicial FARO.

Representa una estimación de la calidad declarada del lead utilizando exclusivamente la información disponible durante la captación. 

No representa una validación comercial, una probabilidad de venta ni una estimación del valor económico del cliente. 

Su rango actual es de 0 a 100 puntos.
---

## Qualified Lead

Lead que cumple los criterios definidos por el Modelo de Pre-cualificación Inicial FARO. 

Representa la pre-cualificación automática realizada a partir de la información declarada durante la captación. 

En la versión actualmente implementada, esta entidad: 
- corresponde a los leads clasificados en los tiers A o B; 
- se utiliza como referencia para el análisis de calidad de captación; 
- permite generar el evento `QualifiedLead` mediante Meta Conversions API. 

Un Qualified Lead no constituye una validación comercial y no garantiza que exista una oportunidad o una venta. La definición funcional se documenta en: `knowledge/scoring/initial-lead-qualification-model.md` Las reglas concretas de cálculo, ponderaciones y umbrales pertenecen a la implementación de FARO/CLARO.

---

## Cualificación Comercial 

Evaluación realizada por el equipo comercial para determinar si un lead presenta interés real, encaje y viabilidad suficientes para continuar dentro del proceso de ventas. 

Esta capacidad forma parte de la arquitectura objetivo del ecosistema, pero todavía no se encuentra integrada de forma gobernada en FARO/CLARO. 

Actualmente no existe una entidad oficial denominada Sales Qualified Lead materializada y disponible como parte del sistema analítico.

---

## Oportunidad

Lead que, después de la evaluación comercial, pasa a formar parte del pipeline activo al existir una posibilidad real de contratación. 

La oportunidad pertenece al dominio comercial. 

Su definición operativa y su integración gobernada con FARO/CLARO todavía están pendientes de la evolución de la integración con GIAV. 

Por tanto, no debe considerarse una entidad actualmente disponible para el cálculo del Modelo de Pre-cualificación Inicial FARO.

---

## Cliente

Persona que ha contratado uno o varios servicios comercializados por Viaja con Álvaro.

Representa la conversión final del embudo comercial.

---

## Venta

Conversión efectiva de una oportunidad comercial en un cliente.

Constituye el resultado final del proceso de captación y gestión comercial.

---

## Validación y aprendizaje comercial previstos 

La arquitectura objetivo de FARO contempla la posibilidad de contrastar, en el futuro, la estimación inicial del lead con los resultados observados durante el proceso comercial. 

Esta evolución podría permitir: - validar la capacidad del modelo para identificar leads de calidad; 

- analizar diferencias entre la estimación inicial y el resultado real; 
- revisar reglas, pesos y umbrales; 
- mejorar progresivamente las señales enviadas a las plataformas publicitarias. 

Esta capacidad todavía no está implementada. No existe actualmente un Score Validado gobernado ni un proceso automático de aprendizaje o recalibración dentro de FARO/CLARO.

---

## Campaign Signal

Clasificación estratégica que identifica la finalidad principal de una campaña dentro del framework FARO.

Valores oficiales:

- ATTENTION
- ACTIVATION
- COMMERCIAL

Cada categoría posee objetivos, KPIs y criterios de interpretación propios.

---

## Señal FARO

Resultado de interpretar los KPIs oficiales mediante las reglas de negocio definidas por FARO.

Las señales transforman datos en decisiones de negocio.

Estados oficiales:

### Atención

- CLEAR ATTENTION
- WEAK ATTENTION
- NOISE

### Activación

- CLEAR ACTIVATION
- WEAK ACTIVATION
- NOISE

### Comercial

- CLEAR SIGNAL
- WEAK SIGNAL
- NOISE

---

## FARO

Framework estratégico de captación e inteligencia comercial.

Define la arquitectura funcional del ecosistema, incluyendo:

- Estrategia de captación.
- Modelo de Scoring.
- KPIs oficiales.
- Sistema de Señales.
- Framework de decisión.
- Contratos funcionales.
- Dashboards funcionales.

FARO responde a la pregunta:

> **¿Qué debe medirse, cómo debe interpretarse y qué decisiones deben tomarse?**
> 

---

## CLARO

Plataforma de datos del ecosistema.

Materializa técnicamente las definiciones realizadas por FARO mediante contratos analíticos, modelos de datos y estructuras gobernadas.

Constituye la fuente única de verdad para el ámbito de captación, activación, aprendizaje y reporting.

CLARO responde a la pregunta:

> **¿Cómo se implementa, gobierna y materializa técnicamente lo definido por FARO?**
> 

# **12. Proyectos Realizados**

Este apartado documenta los principales proyectos desarrollados dentro del ámbito de responsabilidad del ecosistema VCA.

Su objetivo es proporcionar una visión global de las iniciativas estratégicas, analíticas y tecnológicas implementadas o en desarrollo.

| **Proyecto** | **Descripción** | **Estado** | **Resultado / Objetivo** |
| --- | --- | --- | --- |
| **FARO** | Framework estratégico de captación e inteligencia comercial. Define la estrategia de campañas, el modelo de scoring, los KPIs, las señales, los dashboards funcionales y el framework de decisión. | En evolución | Constituye el núcleo funcional del ecosistema de captación y toma de decisiones. |
| **CLARO** | Plataforma de datos responsable de materializar técnicamente la lógica definida por FARO mediante contratos analíticos, modelos de datos y estructuras gobernadas. | En desarrollo | Consolidar una plataforma de datos gobernada, escalable y reutilizable. |
| **Meta CAPI Worker** | Integración entre BigQuery y Meta Conversions API para el envío de los eventos `Lead` y `QualifiedLead`. | Operativo | Mejorar la medición, atribución y optimización de campañas en Meta Ads mediante señales de calidad. |
| **Dashboard FARO Comercial** | Dashboard de lectura de señal comercial basado en el KPI principal CPL Cualificado. | Operativo | Identificar campañas, conceptos y creatividades que generan demanda rentable. |
| **Dashboard FARO Atención** | Dashboard para la lectura de la Señal de Atención mediante el KPI CPAU v1. | En diseño | Detectar conceptos capaces de generar atención útil antes de la fase comercial. |
| **Dashboard FARO Activación** | Dashboard para la lectura de la Señal de Activación mediante el KPI % Activación Cualificada. | En diseño | Medir la capacidad del sistema para transformar interés previo en oportunidades útiles. |
| **Integración GIAV** | Integración entre CLARO y el CRM GIAV para la sincronización de leads preparados y señales comerciales. El desarrollo del CRM corresponde al proveedor de GIAV. | En desarrollo | Automatizar el traspaso de información entre marketing y ventas preservando la lógica definida por FARO. |

## **Principios de Gobierno**

- Este catálogo documenta únicamente proyectos incluidos dentro del ámbito de responsabilidad de VCA Project.
- El estado de cada proyecto deberá mantenerse actualizado durante la evolución del ecosistema.
- La documentación detallada de cada proyecto reside en su correspondiente artefacto del repositorio (`FARO/`, `CLARO/`, `GIAV/`, `meta-capi-worker/`).
- Los proyectos podrán evolucionar mediante nuevas versiones sin perder la trazabilidad histórica de sus objetivos y resultados.

# **13. Decisiones Relevantes**

Esta sección no sustituye a la base oficial de decisiones del SO Profesional.

Documenta exclusivamente las decisiones estratégicas, funcionales y arquitectónicas adoptadas dentro del ámbito de responsabilidad de VCA Project.

No recoge decisiones propias del negocio de Viaja con Álvaro (operaciones, producto, pricing, organización, procesos internos o estrategia empresarial), sino únicamente aquellas que afectan al ecosistema de captación, datos, inteligencia comercial, automatización, integraciones y reporting desarrollado y mantenido por VCA Project.

Toda nueva decisión que afecte a este ámbito deberá registrarse en esta sección y mantenerse alineada con los artefactos del repositorio.

# **2026-03**

**Decisión**

El ecosistema se estructura sobre dos plataformas complementarias:

- **FARO**, como framework estratégico e inteligencia comercial.
- **CLARO**, como plataforma de datos y materialización técnica.

**Motivo**

Separar la lógica funcional de la implementación técnica para facilitar la evolución, el mantenimiento y la reutilización del sistema.

**Impacto**

Toda nueva funcionalidad deberá desarrollarse respetando esta separación de responsabilidades.

# **2026-03**

**Decisión**

BigQuery constituye la fuente única de verdad para el ecosistema de captación, scoring, activación y reporting.

**Motivo**

Garantizar consistencia, trazabilidad y una única interpretación de los datos.

**Impacto**

Las reglas de negocio, los modelos analíticos y los dashboards deberán consumir datos preparados por CLARO.

# **2026-03**

**Decisión**

El ecosistema adopta un modelo de lectura de señales compuesto por tres capas independientes:

- Atención
- Activación
- Comercial

Cada una posee sus propios KPIs, estados y criterios de interpretación.

**Motivo**

Analizar cada fase del embudo con indicadores específicos, evitando interpretar todo el sistema únicamente mediante métricas comerciales.

**Impacto**

Toda campaña deberá clasificarse mediante campaign_signal y evaluarse utilizando los KPIs definidos para su capa correspondiente.

# **2026-05**

**Decisión**

La pre-cualificación automática de los leads se realiza mediante el Modelo de Scoring FARO y se representa mediante la entidad **Qualified Lead**.

**Motivo**

Disponer de un criterio único y gobernado para priorizar la atención comercial y alimentar las integraciones con plataformas externas.

**Impacto**

Todas las integraciones, dashboards y automatizaciones deberán utilizar la definición oficial de **Qualified Lead** establecida por FARO.

# **2026-07-07 — Campaña de escalado optimizada a QualifiedLead**

**Decisión**

Crear una campaña específica de escalado en Meta Ads que optimice con el evento `QualifiedLead`, manteniéndola como una capa diferenciada de las campañas de prueba y captación.

Dentro de FARO, la campaña se clasifica mediante `campaign_signal = COMMERCIAL`. No pertenece a `ATTENTION` ni a `ACTIVATION`: su función es generar y escalar leads con calidad comercial a un coste sostenible.

La señal `QualifiedLead` procede de los leads A+B identificados mediante el scoring FARO y enviados a Meta mediante Conversions API.

**Motivo**

Orientar progresivamente el aprendizaje de Meta hacia la calidad comercial del lead, en lugar de optimizar exclusivamente por volumen de formularios recibidos. La separación de la campaña permite probar y escalar este criterio sin trasladar de inmediato todo el presupuesto ni alterar simultáneamente el aprendizaje del resto de campañas.

**Impacto y criterios de seguimiento**

- Las configuraciones, audiencias o creatividades deben acumular evidencia suficiente antes de escalarse.
- La campaña debe evaluarse exclusivamente con la lógica y los KPIs oficiales de la capa `COMMERCIAL` de FARO; no mediante CPAU ni métricas propias de Atención o Activación.
- Sus indicadores principales son volumen de `QualifiedLead`, tasa de cualificación, coste por `QualifiedLead`, CPL, capacidad de entrega y calidad comercial posterior.
- Deben vigilarse la estabilidad y latencia de la señal, la fase de aprendizaje y el solapamiento con otras campañas.
- Los incrementos presupuestarios deben apoyarse en una muestra suficiente.
- La estrategia deberá revisarse si el volumen de señales no permite un aprendizaje estable, aparecen problemas de atribución o la mejora de calidad no compensa el incremento del coste.

# **14. Conocimiento del Dominio**

Este apartado recoge el conocimiento de dominio necesario para interpretar correctamente el ecosistema de captación, scoring, activación y reporting desarrollado por VCA Project.

No sustituye la documentación estratégica de FARO. Resume únicamente los principios de mercado y de interpretación que cualquier persona o agente de IA debe conocer antes de analizar datos o proponer cambios.

---

## **Estacionalidad y ciclo de decisión**

consideraciones:

- La contratación de viajes internacionales premium no suele ser inmediata. El ciclo de decisión puede extenderse durante semanas o meses.
- El usuario puede encontrarse en distintos niveles de madurez: inspiración, planificación, compra de billetes, organización logística o decisión final.
- Tener billetes comprados o estar en proceso de compra representa una señal de intención más fuerte que estar simplemente explorando.
- Los resultados de captación deben interpretarse considerando el desfase entre atención, activación, lead, cualificación comercial, oportunidad y venta.



---

## **Señales declaradas de cualificación inicial**

Los formularios nativos de Meta utilizados por Viaja con Álvaro no tienen únicamente la función de recoger datos de contacto.

También recogen información declarada por el usuario que permite obtener una primera lectura sobre su intención de viajar y su afinidad con la propuesta de valor.

Actualmente, las principales dimensiones observadas durante la captación son:

* **Compromiso con el viaje:** situación declarada respecto a la compra de los billetes de avión.
* **Madurez temporal:** ventana prevista para realizar el viaje.
* **Encaje con la propuesta de valor:** tipo de experiencia o nivel de acompañamiento buscado.
* **Contexto del viaje:** número de personas que participarían en el desplazamiento.

Estas dimensiones deben interpretarse de forma conjunta.

Ninguna respuesta aislada determina por sí sola la calidad del lead. Su combinación aporta una estimación inicial que posteriormente utiliza el Modelo de Pre-cualificación Inicial FARO.

La información recogida durante la captación:

* representa intención declarada;
* permite diferenciar distintos niveles iniciales de madurez y encaje;
* sirve como base para la clasificación inicial de los leads;
* no constituye una validación comercial;
* no garantiza que exista una oportunidad o una venta.

La interpretación gobernada de estas señales se documenta en:

`knowledge/scoring/initial-lead-qualification-model.md`

---

## **Señales declaradas de cualificación inicial** 

Los formularios nativos de Meta utilizados por Viaja con Álvaro no tienen únicamente la función de recoger datos de contacto. También recogen información declarada por el usuario que permite obtener una primera lectura sobre su intención de viajar y su afinidad con la propuesta de valor. Actualmente, las principales dimensiones observadas durante la captación son: 

- **Compromiso con el viaje:** situación declarada respecto a la compra de los billetes de avión. 
- **Madurez temporal:** ventana prevista para realizar el viaje. 
- **Encaje con la propuesta de valor:** tipo de experiencia o nivel de acompañamiento buscado. 
- **Contexto del viaje:** número de personas que participarían en el desplazamiento. Estas dimensiones deben interpretarse de forma conjunta. Ninguna respuesta aislada determina por sí sola la calidad del lead. Su combinación aporta una estimación inicial que posteriormente utiliza el Modelo de Pre-cualificación Inicial FARO. La información recogida durante la captación: - representa intención declarada; - permite diferenciar distintos niveles iniciales de madurez y encaje; - sirve como base para la clasificación inicial de los leads; - no constituye una validación comercial; - no garantiza que exista una oportunidad o una venta. La interpretación gobernada de estas señales se documenta en: `knowledge/scoring/initial-lead-qualification-model.md`

---

## **Particularidades del mercado**

- El mercado trabajado en FARO se centra principalmente en viajeros puertorriqueños y diáspora puertorriqueña interesada en viajar a España.
- Es un nicho con baja saturación específica en paid media cuando se combina turismo experiencial, viajes premium y comunicación culturalmente adaptada al público puertorriqueño.
- El usuario valora autenticidad, exclusividad, cercanía, confianza y reducción del estrés logístico.
- El ticket premium puede generar fricción, por lo que la comunicación debe explicar claramente el valor diferencial frente a alternativas genéricas.
- La confianza es crítica: el usuario necesita saber quién está detrás del servicio, qué incluye la experiencia y por qué la propuesta es diferente.

---

## **Patrones de comportamiento del usuario**

- El usuario no siempre está preparado para dejar sus datos en el primer impacto publicitario.
- La atención previa, el consumo de contenido y la interacción con la marca son señales relevantes antes de solicitar una conversión directa.
- El formulario debe actuar como filtro de cualificación, no solo como mecanismo de captación barata.
- Un lead de Meta no equivale automáticamente a un lead cualificado.
- Un CPL bajo puede ser negativo si genera leads que no responden, no tienen viaje previsto, no tienen presupuesto o no avanzan comercialmente.

---

## **Principios de interpretación FARO**

- No todas las campañas deben evaluarse con la misma lógica.
- Cada campaña debe interpretarse según su `campaign_signal`:
    - `ATTENTION`
    - `ACTIVATION`
    - `COMMERCIAL`
- Una campaña de Atención no debe evaluarse por leads directos.
- Una campaña Comercial no debe evaluarse por métricas de consumo de vídeo.
- Una campaña de Activación no debe mezclarse con tráfico frío sin separación.
- No debe utilizarse un único KPI universal para todo el sistema.
- La calidad del lead manda sobre el CPL total.
- Las decisiones deben tomarse por concepto y funnel, no por anuncio aislado, métrica suelta o resultado de un único día.

---

## **Lectura multicapa del embudo**

FARO organiza la lectura del sistema en tres capas:

- **Atención:** identifica qué ideas generan atención útil y merecen seguir recibiendo inversión.
- **Activación:** mide qué mensajes convierten interés previo en avance real.
- **Comercial:** evalúa qué ideas generan leads útiles a coste sostenible.

Esta separación evita interpretar erróneamente campañas que cumplen funciones distintas dentro del embudo.

---

## **Reglas de decisión y aprendizaje**

- FARO separa la lectura de señal de la decisión operativa. 
- Una señal clara no implica escalar automáticamente; indica que el concepto puede evaluarse para escalar. 
- No debe detenerse un concepto sin evidencia suficiente. 
- El escalado debe realizarse de forma progresiva. 
- En la versión actualmente implementada, las decisiones se apoyan principalmente en señales publicitarias y en la calidad inicial observada durante la captación. 
- El feedback comercial puede utilizarse como evidencia adicional cuando esté disponible, pero todavía no se encuentra integrado de forma sistemática y gobernada en FARO/CLARO. 
- La conexión automática entre señal publicitaria, señal de captación y señal comercial forma parte de la evolución prevista del ecosistema.

---

## **Competencia y posicionamiento**

- La competencia incluye marketplaces de tours, agencias receptivas, plataformas de experiencias y propuestas de turismo premium.
- Muchos competidores utilizan claims genéricos como “tour privado”, “experiencia exclusiva” o “guía experto”.
- La oportunidad diferencial está en la personalización cultural, el tono cercano, la conexión con el público puertorriqueño y la promesa de acompañamiento experto.
- Los mensajes impersonales, demasiado formales, genéricos o centrados en precio bajo pueden erosionar la percepción premium.

---

## **Factores externos relevantes**

- El precio y disponibilidad de vuelos puede afectar directamente a la intención real de compra.
- La situación económica del mercado objetivo puede modificar la sensibilidad al ticket premium.
- La confianza en compras digitales desde el extranjero es un factor crítico.
- El algoritmo de Meta puede optimizar hacia formularios baratos si no se alimenta con señales de calidad.
- La eficiencia publicitaria debe interpretarse junto con calidad posterior, contactabilidad, cualificación comercial y avance real en ventas.

**15. Aprendizajes Reales**

Este apartado solo debe completarse cuando existan aprendizajes derivados de implementación real, incidencias, errores, validaciones, cambios de enfoque o decisiones corregidas por la experiencia.

No debe utilizarse para repetir principios, reglas o definiciones ya documentadas en FARO, CLARO, arquitectura, KPIs, glosario o decisiones relevantes.

# **16. Oportunidades Detectadas**

Este apartado recoge oportunidades de mejora identificadas dentro del ámbito de actuación de VCA Project.

No constituye un compromiso de ejecución ni sustituye al roadmap del proyecto. Su finalidad es mantener visibles aquellas iniciativas que podrían aportar valor al ecosistema y que deberán evaluarse en función de su impacto, viabilidad y prioridades del cliente.

opportunidades:

- Evolucionar el Modelo de Scoring FARO incorporando información procedente del proceso comercial para mejorar su capacidad predictiva.
- Completar la integración con GIAV para cerrar el ciclo entre captación, cualificación comercial y aprendizaje del sistema.
- Incorporar nuevos dashboards de ayuda a la decisión y aprendizaje definidos en FARO.
- Ampliar las señales enviadas a Meta Conversions API conforme evolucione el Modelo de Scoring y la disponibilidad de datos comerciales.
- Consolidar CLARO como plataforma única para la materialización de modelos analíticos, contratos de datos y procesos gobernados.
- Incrementar el uso de datos propios (first-party data) para reducir la dependencia de las plataformas publicitarias y mejorar la capacidad de optimización.
- Explorar nuevos modelos de IA y analítica predictiva que permitan anticipar calidad de leads, oportunidades comerciales y comportamiento futuro de la demanda.
- Evolucionar el ecosistema FARO hacia un sistema de aprendizaje continuo basado en la comparación entre predicciones, resultados comerciales y decisiones adoptadas.

# **19. Preferencias del Cliente**

Este apartado documenta las preferencias de trabajo observadas durante la colaboración entre el cliente y VCA Project.

Su objetivo es facilitar la continuidad del proyecto y mantener una forma de trabajo coherente entre todas las personas o agentes que participen en el ecosistema.

Este apartado únicamente deberá completarse cuando existan preferencias claramente identificadas y validadas durante la relación con el cliente.

# **Reporting**

**Frecuencia**

**Formato preferido**

# **Comunicación**

**Canal principal**

**Frecuencia de contacto**

# **Proceso de Trabajo**

# **Nivel Técnico**

# **Expectativas**

# **20. Riesgos Actuales**

Este apartado documenta los riesgos actualmente identificados dentro del ámbito de actuación de VCA Project.

No recoge riesgos generales del negocio del cliente, sino aquellos que pueden afectar al correcto funcionamiento, evolución o mantenimiento del ecosistema de captación, datos, inteligencia comercial y automatización.

**Riesgos identificados**

- La integración con GIAV todavía se encuentra en fase de desarrollo por parte del proveedor del CRM, lo que limita temporalmente la automatización completa del ciclo comercial.
- El ciclo de aprendizaje de FARO aún no dispone de toda la información comercial necesaria para validar y recalibrar el Modelo de Scoring de forma completamente automatizada.
- Parte de la arquitectura funcional continúa evolucionando, por lo que algunos componentes documentados pueden sufrir cambios hasta alcanzar su versión estable.
- La calidad de las decisiones depende de la correcta gobernanza de los datos y de mantener alineadas las definiciones funcionales entre FARO, CLARO y las distintas integraciones.
- Este apartado deberá revisarse periódicamente para incorporar nuevos riesgos o eliminar aquellos que hayan sido mitigados.

# **21. Relaciones**

Este apartado documenta las relaciones externas relevantes para el ecosistema desarrollado por VCA Project cuando dichas relaciones condicionen el diseño, funcionamiento o evolución del sistema.

No pretende reflejar la totalidad de proveedores, colaboradores o relaciones comerciales del cliente.

> *Actualmente no disponemos de conocimiento relevante para este apartado.*
> 

# **Clientes Relacionados**

# **Proveedores Relevantes**

# **Partners**

# **Plataformas Estratégicas**

# **22. Metadatos**

cliente_id:

ultima_revision:

proxima_revision:

responsable_documento: Jordi Quiroga

estado:

- Borrador
- En revisión
- Vigente
- Archivado

version:

repositorio:

ruta_documento:

fecha_creacion:

ultima_actualizacion:

ambito:

Captación · Inteligencia Comercial · Analítica · Plataforma de Datos · Automatización · IA

fuente_principal:

Repositorio vca_project

# **23. Instrucciones para IA**

Antes de iniciar cualquier proyecto, análisis, propuesta, arquitectura, especificación funcional o desarrollo relacionado con este cliente:

1. Consultar este CCD como fuente principal de contexto del cliente.
2. Verificar el alcance del CCD para comprender el ámbito de actuación de VCA Project y evitar realizar suposiciones sobre áreas fuera de su responsabilidad.
3. Revisar la sección **Decisiones Relevantes** antes de proponer cambios funcionales o arquitectónicos.
4. Consultar las **Referencias Documentales** para localizar la fuente de verdad correspondiente al área de trabajo (FARO, CLARO, GIAV, Meta CAPI Worker, etc.).
5. Utilizar las definiciones oficiales recogidas en el **Glosario de Negocio** y los **KPIs Oficiales**.
6. Respetar la separación de responsabilidades entre los distintos componentes del ecosistema:
    - FARO → Estrategia e inteligencia comercial.
    - CLARO → Plataforma de datos y materialización técnica.
    - GIAV → Integración CRM.
    - Meta CAPI Worker → Integración con Meta Conversions API.
7. No duplicar reglas de negocio ya documentadas en FARO ni lógica técnica ya implementada en CLARO.
8. En caso de conflicto entre documentos, prevalecerá la fuente de verdad indicada en la sección **Referencias Documentales**, salvo que exista una decisión posterior registrada en este CCD.
9. Toda decisión arquitectónica o funcional que modifique el ecosistema deberá registrarse en la sección **Decisiones Relevantes**.
10. Toda nueva información relevante sobre el cliente deberá incorporarse al CCD para mantener actualizado el contexto del proyecto.
11. Evitar duplicar documentación. Siempre que exista un documento específico que actúe como fuente de verdad, el CCD deberá limitarse a resumir el contexto y referenciar dicho documento.

# **24. Estado del Documento**

# **Naturaleza del Documento**

El Client Context Document (CCD) constituye la fuente principal de contexto del cliente dentro del ámbito de actuación de VCA Project.

Su objetivo es proporcionar el conocimiento necesario para comprender el cliente, el ecosistema desarrollado y las decisiones que condicionan su evolución.

No sustituye la documentación funcional, metodológica o técnica del repositorio, sino que actúa como punto de entrada y contexto para acceder a ella.

El CCD es un artefacto transversal al cliente. Su ciclo de vida es independiente del de los proyectos que lo consumen y deberá evolucionar conforme aumente el conocimiento del negocio, con independencia de la creación, modificación o finalización de proyectos específicos.

El Client Context Document (CCD) constituye la fuente principal de contexto del cliente dentro del ámbito de actuación de VCA Project.

Su objetivo es proporcionar el conocimiento necesario para comprender el cliente, el ecosistema desarrollado y las decisiones que condicionan su evolución.

No sustituye la documentación funcional, metodológica o técnica de los proyectos relacionados, sino que actúa como punto de entrada y contexto para acceder a ella.

**El CCD es un artefacto transversal al cliente y constituye la referencia canónica del contexto de negocio dentro de su ámbito de aplicación. Su ciclo de vida es independiente del de los proyectos que lo consumen y deberá evolucionar conforme aumente el conocimiento del negocio, con independencia de la creación, modificación o finalización de proyectos específicos. Los proyectos y agentes de IA deberán referenciar este documento como fuente de contexto cuando resulte aplicable, evitando duplicar la información aquí contenida.**

# **Mantenimiento**

El CCD deberá mantenerse actualizado durante toda la relación con el cliente.

Toda modificación relevante en el contexto del cliente, la arquitectura del ecosistema, las decisiones estratégicas o las fuentes de conocimiento deberá reflejarse en este documento.

Los cambios de implementación, especificaciones funcionales, contratos, modelos de datos o procedimientos deberán documentarse en sus respectivos artefactos y únicamente referenciarse desde el CCD cuando resulte necesario.

# **Criterios de Calidad**

Para preservar la utilidad y fiabilidad del CCD deberán cumplirse los siguientes principios:

- Documentar únicamente información contrastada.
- Evitar duplicar documentación existente en otras fuentes de verdad.
- Mantener el documento centrado en el contexto y no en la implementación.
- Referenciar siempre la documentación específica cuando exista.
- Dejar sin completar aquellos apartados para los que todavía no exista conocimiento suficiente.
- Revisar periódicamente el documento para asegurar su vigencia y coherencia con el ecosistema documental