Analiza la calidad de los leads procedentes de Meta Ads durante el periodo comprendido entre el 1 y el 30 de junio de 2026 y prepara un informe ejecutivo dirigido a Dirección.

El informe debe identificar, dentro de las posibilidades reales de los datos disponibles:

* qué campañas, conjuntos de anuncios o creatividades están generando leads de mayor calidad;
* cómo se relacionan la calidad de los leads y la inversión;
* qué diferencias relevantes existen entre los elementos analizados;
* qué limitaciones, UNKNOWN o problemas de cobertura afectan a las conclusiones;
* qué acciones se recomiendan y con qué prioridad.

Antes de comenzar:

1. Revisa las instrucciones, specifications, contracts, Analytical Use Case AUC-001, skill y fuentes de contexto oficiales del repositorio.
2. Reconstruye el workflow aplicable desde los artefactos canónicos, sin asumir que los documentos de salida anteriores son correctos.
3. Utiliza el BigQuery MCP Server como Data Provider cuando el scope requerido esté soportado.
4. Distingue claramente cualquier evidencia obtenida mediante MCP de evidencia histórica adquirida mediante CLI.
5. No utilices `docs/handoffs/auc-001-executive-report.md`, el Knowledge Set ni el Recommendation Set existentes como fuente de conclusiones. Pueden consultarse únicamente después de generar el nuevo informe, para realizar una comparación independiente.
6. No modifiques ningún archivo del repositorio ni actualices Tasks, contracts, handoffs, evaluations o specifications.
7. No inventes relaciones entre campañas, conjuntos, anuncios, inversión y calidad cuando los datos no permitan establecerlas.
8. Mantén separados hechos observados, interpretación, hipótesis y recomendaciones.

Genera el resultado en un archivo nuevo:

`outputs/evaluations/auc-001-report-quality-test-2026-06.md`

El informe debe incluir:

* resumen ejecutivo;
* objetivo y alcance;
* datos y cobertura utilizados;
* principales resultados;
* análisis por nivel disponible;
* conclusiones;
* recomendaciones priorizadas;
* limitaciones y UNKNOWN;
* trazabilidad hacia las fuentes utilizadas.

Al finalizar, añade una sección separada titulada `Execution record` que indique:

* artefactos del repositorio consultados;
* herramientas utilizadas;
* consultas o acciones ejecutadas mediante MCP;
* datos que no pudieron obtenerse;
* decisiones tomadas por limitaciones de cobertura;
* confirmación de que el informe ejecutivo anterior no fue usado como fuente de conclusiones.

No implementes correcciones en el framework aunque detectes problemas. Regístralos al final como observaciones para una evaluación posterior.
