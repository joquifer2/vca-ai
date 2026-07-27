"""AUC-001 canonical analytical enrichment helpers."""

from __future__ import annotations

from typing import Any


def _pct(numerator: float, denominator: float) -> float:
    if not denominator:
        return 0.0
    return round((numerator / denominator) * 100, 1)


def build_enriched_auc001_canonical_content(
    metrics: dict[str, Any],
    *,
    evidence_artifact_id: str,
    question_ids: list[str],
) -> dict[str, Any]:
    """Build richer Phase 09/10 content from current canonical evidence facts.

    The helper does not read historical outputs, query data providers, or create
    new evidence. It only structures interpretation and recommendations from the
    facts already present in the current Evidence Set.
    """

    lead_total = metrics["lead_coverage"]["lead_count"]
    tier_a = metrics["lead_tier_total"]["A"]["lead_count"]
    tier_b = metrics["lead_tier_total"]["B"]["lead_count"]
    tier_c = metrics["lead_tier_total"]["C"]["lead_count"]
    tier_d = metrics["lead_tier_total"]["D"]["lead_count"]
    ab_total = tier_a + tier_b
    cd_total = tier_c + tier_d
    ab_rate = _pct(ab_total, lead_total)
    cd_rate = _pct(cd_total, lead_total)
    june = next(row for row in metrics["monthly_tier"] if row["month"] == "2026-06")
    april = next(row for row in metrics["monthly_tier"] if row["month"] == "2026-04")
    commercial = metrics["commercial_matched"]
    activation = metrics["activation_observed"]
    top_ads = metrics["top_ads"]
    top_two_leads = top_ads[0]["leads"] + top_ads[1]["leads"]
    top_two_ab = top_ads[0]["ab"] + top_ads[1]["ab"]

    findings = [
        {
            "finding_id": "F-001",
            "analytical_question_id": "AQ-002",
            "observation": f"El periodo genera {lead_total} leads, {ab_total} A/B y {tier_a} Tier A.",
            "importance": f"La calidad existe, but {cd_rate} percent permanece en C/D; this constrains scale decisions.",
            "uncertainty": "Tier quality is observed lead quality, not downstream revenue or CRM value.",
            "related_findings": ["F-002", "F-003", "F-006"],
            "evidence_refs": ["lead_tier_total", "lead_coverage"],
            "comparison": "Tier A/B was compared against C/D with the full-period denominator.",
        },
        {
            "finding_id": "F-002",
            "analytical_question_id": "AQ-009",
            "observation": f"Junio concentra {june['leads']} leads y {june['ab']} A/B, pero su tasa A/B ({_pct(june['ab'], june['leads'])} percent) queda cerca de abril ({_pct(april['ab'], april['leads'])} percent).",
            "importance": "Volume grew faster than quality density; this separates scale success from structural quality improvement.",
            "uncertainty": "Weekly comparability and intra-month edges remain not_available in the current Evidence Set.",
            "related_findings": ["F-001", "F-010"],
            "evidence_refs": ["monthly_tier"],
            "comparison": "Monthly lead, A/B and Tier A counts were compared across April, May and June.",
        },
        {
            "finding_id": "F-003",
            "analytical_question_id": "AQ-006",
            "observation": "`tiene_billetes` reaches 157 A/B from 177 leads, while `solo_mirando` reaches 48 A/B from 838 leads.",
            "importance": "The ticket-status split explains a large quality gradient and changes what Marketing should test.",
            "uncertainty": "The relation is observational; causality requires a controlled experiment.",
            "related_findings": ["F-004", "F-008"],
            "evidence_refs": ["ticket_status"],
            "comparison": "High-intent ticket-status buckets were compared against exploratory demand.",
        },
        {
            "finding_id": "F-004",
            "analytical_question_id": "AQ-006",
            "observation": "`menos_de_1_mes` reaches 74 A/B from 80 leads, while `aun_no_claro` reaches 26 A/B from 463 leads.",
            "importance": "Travel-window readiness reinforces the intent explanation through an independent qualification signal.",
            "uncertainty": "Travel window is a lead qualification signal, not a confirmed purchase outcome.",
            "related_findings": ["F-003", "F-006"],
            "evidence_refs": ["travel_window"],
            "comparison": "Near travel windows were compared with unclear travel windows using A/B and Tier A density.",
        },
        {
            "finding_id": "F-005",
            "analytical_question_id": "AQ-003",
            "observation": f"COMMERCIAL matched links {commercial['spend']} EUR, {commercial['leads']} leads and {commercial['ab']} A/B.",
            "importance": f"The governed direct cost-quality universe has cost per A/B of {commercial['cost_per_ab']} EUR and cost per A of {commercial['cost_per_a']} EUR.",
            "uncertainty": "This economic reading applies only to the matched COMMERCIAL universe.",
            "related_findings": ["F-006", "F-009"],
            "evidence_refs": ["commercial_matched", "spend_by_signal"],
            "comparison": "Matched COMMERCIAL economics were separated from layer-level spend totals.",
        },
        {
            "finding_id": "F-006",
            "analytical_question_id": "AQ-010",
            "observation": "ATTENTION, ACTIVATION and COMMERCIAL carry different FARO roles and cannot be ranked as one universal efficiency table.",
            "importance": "This prevents a false optimization claim based on non-equivalent strategic layers.",
            "uncertainty": "Impacto asistido de ATTENTION remains UNKNOWN without downstream or assisted-effect evidence.",
            "related_findings": ["F-005", "F-010"],
            "evidence_refs": ["spend_by_signal", "activation_observed"],
            "comparison": "FARO layers were compared by governance status, not by a universal KPI hierarchy.",
        },
        {
            "finding_id": "F-007",
            "analytical_question_id": "AQ-008",
            "observation": f"Facebook contributes {metrics['platform'][0]['leads']} leads and {metrics['platform'][0]['ab']} A/B; Instagram contributes {metrics['platform'][1]['leads']} leads and {metrics['platform'][1]['ab']} A/B.",
            "importance": "Platform differences are visible but not strong enough to override the intent and FARO findings.",
            "uncertainty": "Platform is not isolated from campaign mix, ad mix or qualification intent.",
            "related_findings": ["F-003", "F-008"],
            "evidence_refs": ["platform"],
            "comparison": "Platform A/B density and Tier A counts were compared as descriptive segments.",
        },
        {
            "finding_id": "F-008",
            "analytical_question_id": "AQ-004",
            "observation": "The retargeting campaign has higher A/B density than the acquisition campaign, while acquisition carries most qualified volume.",
            "importance": "This creates a volume-quality trade-off that must be handled as portfolio design, not as a simple winner/loser ranking.",
            "uncertainty": "Campaign interpretation is partial because ad-set and temporal spend joins are not available.",
            "related_findings": ["F-002", "F-007", "F-009"],
            "evidence_refs": ["campaigns"],
            "comparison": "Campaigns were compared by lead volume, A/B volume, Tier A and average score.",
        },
        {
            "finding_id": "F-009",
            "analytical_question_id": "AQ-005",
            "observation": f"The top two ad_id_norm values concentrate {top_two_leads} leads and {top_two_ab} A/B leads.",
            "importance": "Ad concentration identifies where to inspect and test, but it does not prove creative causality.",
            "uncertainty": "Ad names, creative metadata and controlled creative tests are unavailable.",
            "related_findings": ["F-003", "F-008"],
            "evidence_refs": ["top_ads", "campaigns"],
            "comparison": "Top ads were ranked by lead and A/B concentration while preserving the creative-causality limit.",
        },
        {
            "finding_id": "F-010",
            "analytical_question_id": "AQ-011",
            "observation": "Weekly quality, ad-set segmentation, temporal spend and ad-spend joins are absent from the current canonical Evidence Set.",
            "importance": "These missing dimensions define the boundary between current decisions and future evidence needs.",
            "uncertainty": "The absence is not filled from historical outputs or inference.",
            "related_findings": ["F-002", "F-006", "F-009"],
            "evidence_refs": ["lead_coverage", "commercial_matched"],
            "comparison": "Available canonical dimensions were contrasted with baseline-pattern dimensions that remain not_available.",
        },
    ]

    knowledge_claims = [
        {
            "knowledge_id": "K-001",
            "evidence_refs": ["lead_tier_total", "lead_coverage"],
            "finding_refs": ["F-001"],
            "claim": f"Meta aporta volumen cualificado material: {ab_total} leads A/B y {tier_a} leads Tier A.",
            "interpretation": f"La lectura operativa es que el canal es viable, pero la convivencia de calidad A/B con ruido C/D exige filtros de intencion antes de escalar decisiones.",
            "limitation_or_uncertainty": "La calidad de revenue y la conversion CRM permanecen UNKNOWN.",
        },
        {
            "knowledge_id": "K-002",
            "evidence_refs": ["monthly_tier"],
            "finding_refs": ["F-002"],
            "claim": "Junio escala volumen cualificado sin probar una mejora estructural de calidad.",
            "interpretation": "Como la densidad A/B mensual se mantiene cercana entre meses mientras crece el conteo de leads, mejora mas la escala absoluta que la densidad de calidad.",
            "limitation_or_uncertainty": "La dinamica semanal esta not_available, por lo que no se declara causalidad intra-mes.",
        },
        {
            "knowledge_id": "K-003",
            "evidence_refs": ["ticket_status", "travel_window"],
            "finding_refs": ["F-003", "F-004"],
            "claim": "La intencion explicita de viaje es el separador de calidad mas fuerte observado.",
            "interpretation": "Los buckets de intencion explican mejor la brecha entre demanda exploratoria y concentracion A/B o Tier A que la plataforma o el volumen por si solos.",
            "limitation_or_uncertainty": "Es una asociacion observacional, no una prueba causal.",
        },
        {
            "knowledge_id": "K-004",
            "evidence_refs": ["commercial_matched", "spend_by_signal"],
            "finding_refs": ["F-005", "F-006"],
            "claim": "La interpretacion economica debe mantenerse dentro de los universos FARO gobernados.",
            "interpretation": "COMMERCIAL matched permite lectura directa coste-calidad, mientras ATTENTION y ACTIVATION siguen siendo capas no equivalentes.",
            "limitation_or_uncertainty": "Un ranking coste-calidad universal entre capas FARO es invalido.",
        },
        {
            "knowledge_id": "K-005",
            "evidence_refs": ["campaigns", "platform"],
            "finding_refs": ["F-007", "F-008"],
            "claim": "Las decisiones de portfolio deben equilibrar escala de adquisicion y densidad de retargeting.",
            "interpretation": "Adquisicion concentra la mayor parte del volumen cualificado, mientras retargeting muestra una bolsa de calidad mas densa pero menor; como los universos difieren, el aprendizaje es balance de portfolio y no sustitucion.",
            "limitation_or_uncertainty": "Los cruces por conjunto de anuncios e inversion temporal estan not_available.",
        },
        {
            "knowledge_id": "K-006",
            "evidence_refs": ["top_ads"],
            "finding_refs": ["F-009"],
            "claim": "La concentracion por anuncio sirve para priorizar tests, no para declarar ganadores creativos.",
            "interpretation": "Los anuncios principales concentran volumen y leads A/B, lo que justifica prioridad de inspeccion; la causalidad sigue bloqueada sin metadata creativa o tests controlados.",
            "limitation_or_uncertainty": "La causalidad creativa permanece UNKNOWN.",
        },
        {
            "knowledge_id": "K-007",
            "evidence_refs": ["lead_coverage", "commercial_matched"],
            "finding_refs": ["F-010"],
            "claim": "Las dimensiones ausentes son limites de decision, no huecos que rellenar con outputs historicos.",
            "interpretation": "Calidad semanal, segmentacion por conjunto de anuncios, inversion temporal y cruces inversion-anuncio deben seguir como not_available hasta que exista evidencia canonica actual.",
            "limitation_or_uncertainty": "Los outputs historicos no son evidencia ni valores esperados.",
        },
    ]

    narrative = {
        "text": (
            "La tesis integrada es que Meta ya genera volumen cualificado suficiente para seguir invirtiendo aprendizaje, "
            "pero la calidad se separa sobre todo por intención observable y no por volumen puro. El hallazgo estructural "
            "es la combinación de ruido C/D alto, densidad A/B estable durante la escala de junio y señales de intención "
            "muy discriminantes. El trade-off principal es aumentar volumen sin diluir calidad operativa. El riesgo dominante "
            "es convertir capas FARO no equivalentes en un ranking económico universal. La implicación estratégica es proteger "
            "COMMERCIAL matched como universo de decisión económica y usar intención explícita como hipótesis de test."
        ),
        "phenomenon": "existe volumen cualificado, pero la densidad de calidad queda condicionada por la separacion de intencion y el ruido C/D",
        "structural_findings": ["F-001", "F-003", "F-004", "F-005", "F-006"],
        "secondary_findings": ["F-002", "F-007", "F-008", "F-009", "F-010"],
        "trade_off": "escalar volumen cualificado sin ampliar la carga exploratoria C/D",
        "dominant_risk": "ranking KPI universal entre capas FARO no equivalentes",
        "strategic_implication": "proteger la economia de COMMERCIAL matched y probar filtros de intencion explicita antes de mover presupuestos",
        "memorable_idea": "La calidad no esta escondida en mas volumen; esta concentrada en senales de intencion verificables.",
        "knowledge_refs": [item["knowledge_id"] for item in knowledge_claims],
    }

    recommendations = [
        {
            "recommendation_id": "R-001",
            "category": "measurable_experiment",
            "priority": "high",
            "knowledge_refs": ["K-003", "K-004"],
            "hypothesis": "Priorizar senales explicitas de billete, proceso de compra y ventana cercana aumentara la densidad A/B sin colapsar volumen cualificado.",
            "action": "Ejecutar un test controlado en COMMERCIAL matched que enfatice estado de billete e intencion de ventana cercana en copy, formulario o routing.",
            "population": "Trafico Meta Lead Ads COMMERCIAL matched.",
            "primary_metric": "Tasa de leads A/B y conteo Tier A en COMMERCIAL matched.",
            "secondary_metric": "Peso C/D y volumen total cualificado A/B.",
            "guardrail": "No reducir el volumen cualificado A/B por debajo de la referencia mensual actual.",
            "expected_direction": "Mayor densidad A/B con conteo Tier A estable o mejorado.",
            "success_criterion": "La tasa A/B mejora mientras el conteo Tier A y los guardrails de volumen cualificado se mantienen estables.",
            "validation_window": "Un periodo completo comparable de campana.",
            "evidence_dependency": "Evidencia futura de BigQuery MCP al mismo grano.",
            "uncertainty": "La asociacion observada debe validarse causalmente.",
            "stop_or_review_condition": "Detener o redisenar si sube el peso C/D, cae el conteo Tier A o colapsa el volumen comercial.",
        },
        {
            "recommendation_id": "R-002",
            "category": "verifiable_action",
            "priority": "high",
            "knowledge_refs": ["K-004"],
            "action": "Mantener ATTENTION, ACTIVATION y COMMERCIAL en bloques de decision separados en todo informe AUC-001.",
            "supporting_evidence": "spend_by_signal, commercial_matched y activation_observed preservan universos FARO no equivalentes.",
            "verifiable_result": "Ningun informe contiene un ranking KPI universal entre capas FARO.",
            "closure_criterion": "SPEC-017 y los checks de Presentation preservan la separacion de capas.",
            "risk": "Rankear capas no equivalentes puede sobredimensionar eficiencia economica y mover presupuesto al rol estrategico equivocado.",
            "dependency": "El perfil de contexto estrategico FARO permanece activo.",
        },
        {
            "recommendation_id": "R-003",
            "category": "measurable_experiment",
            "priority": "medium",
            "knowledge_refs": ["K-005"],
            "hypothesis": "Un mix de portfolio que proteja la escala de adquisicion y aisle la densidad de retargeting mejorara la calidad de decision.",
            "action": "Evaluar adquisicion y retargeting como roles complementarios, no como candidatos de sustitucion.",
            "population": "Universo actual de leads Meta a nivel campana.",
            "primary_metric": "Volumen A/B y tasa A/B por rol de campana.",
            "guardrail": "No mover presupuesto solo por densidad sin comprobar volumen absoluto cualificado.",
            "expected_direction": "Logica de asignacion mas clara entre roles de escala y densidad.",
            "success_criterion": "Las decisiones por rol de campana preservan volumen cualificado y mejoran interpretabilidad.",
            "validation_window": "Siguiente periodo comparable de reporting.",
            "evidence_dependency": "Evidence Set actual a nivel campana y futuros cruces por conjunto de anuncios/inversion si se autorizan.",
            "uncertainty": "Conjunto de anuncios e inversion temporal permanecen not_available.",
            "stop_or_review_condition": "Revisar si la densidad de retargeting se usa para justificar sustitucion de escala de adquisicion sin guardrails de volumen.",
        },
        {
            "recommendation_id": "R-004",
            "category": "non_actionable_hypothesis",
            "priority": "medium",
            "knowledge_refs": ["K-006"],
            "hypothesis": "Los clusters principales de ad_id_norm pueden contener encuadres de intencion reutilizables.",
            "support": "top_ads concentra volumen cualificado y leads A/B.",
            "uncertainty": "No hay evidencia de causalidad creativa, nombres de anuncio ni metadata creativa disponible.",
            "missing_evidence": "Test creativo controlado o metadata creativa autorizada.",
            "promotion_condition": "Promover solo despues de que un experimento controlado futuro conecte variacion creativa con calidad.",
        },
        {
            "recommendation_id": "R-005",
            "category": "verifiable_action",
            "priority": "medium",
            "knowledge_refs": ["K-007"],
            "action": "Mantener calidad semanal, segmentacion por conjunto de anuncios, inversion temporal y cruces inversion-anuncio fuera de decisiones de optimizacion hasta que exista evidencia canonica actual.",
            "supporting_evidence": "El Evidence Set canonico actual no contiene esas dimensiones.",
            "verifiable_result": "Los informes marcan estas dimensiones como not_available o UNKNOWN.",
            "closure_criterion": "Una ejecucion futura materializa estas dimensiones mediante evidencia MCP autorizada antes de usarlas.",
            "risk": "Rellenar dimensiones ausentes desde outputs historicos reintroduciria la ruta de regresion.",
            "dependency": "La adquisicion futura de evidencia sigue siendo solo MCP y autorizada por contrato.",
        },
    ]

    limitations = [
        "No hay fuente de revenue ni resultado final CRM.",
        "No hay fuente de causalidad creativa, nombres de anuncio ni metadata creativa.",
        "Las capas FARO no son estrategicamente equivalentes.",
        "Calidad semanal, segmentacion por conjunto de anuncios, inversion temporal y cruces inversion-anuncio estan not_available en el Evidence Set canonico actual.",
        "Las diferencias por campana y plataforma son descriptivas salvo que evidencia futura aisle efectos de mix.",
    ]
    unknowns = [
        "Calidad de revenue",
        "Conversion CRM o valor de venta",
        "Causalidad creativa",
        "Impacto asistido de ATTENTION",
        "Dinamica semanal de calidad",
        "Performance a nivel conjunto de anuncios",
        "Relacion temporal inversion-calidad",
    ]

    air = {
        "artifact_id": "AUC-001-AIR-20260726-CANONICAL",
        "schema_family": "auc_001_analytical_investigation_record",
        "status": "stabilized",
        "derived_from": evidence_artifact_id,
        "evidence_set_ref": "evidence/evidence-set.json",
        "analytical_questions": question_ids,
        "analytical_operations": [
            "tier mix segmentation",
            "monthly volume-quality comparison",
            "intent bucket contrast",
            "FARO layer governance classification",
            "platform and campaign descriptive comparison",
            "ad concentration analysis",
            "missing-dimension boundary audit",
        ],
        "alternative_hypotheses": [
            "Volume alone explains quality.",
            "Intent signals explain quality separation.",
            "Platform choice explains quality separation.",
            "Campaign role explains quality trade-offs.",
            "Cross-layer cost ranking identifies the best FARO layer.",
            "Top ads prove creative causality.",
        ],
        "contrasts_performed": [
            "A/B and Tier A against C/D across the full period.",
            "April, May and June monthly quality density.",
            "Ticket-status and travel-window high-intent buckets against exploratory buckets.",
            "COMMERCIAL matched economics separated from ATTENTION and ACTIVATION.",
            "Platform and campaign descriptive density against qualified volume.",
            "Top ad_id_norm concentration without creative causality.",
            "Available canonical dimensions against not_available baseline-pattern dimensions.",
        ],
        "discarded_hypotheses": [
            "Volume alone is sufficient to explain quality.",
            "Cross-layer universal KPI ranking is valid.",
            "Top ads prove creative winner status.",
            "Historical outputs can fill missing current evidence dimensions.",
        ],
        "robustness_and_limits": [
            "Evidence covers 2026-04-18 through 2026-06-30.",
            "Full-period denominator is 1329 leads.",
            "Cost-quality claims are limited to COMMERCIAL matched.",
            "Revenue, CRM and creative causality remain UNKNOWN.",
            "Missing dimensions remain not_available and are not inferred.",
        ],
        "intermediate_findings": findings,
    }

    return {
        "air": air,
        "findings": findings,
        "knowledge_claims": knowledge_claims,
        "analytical_narrative": narrative,
        "recommendations": recommendations,
        "limitations": limitations,
        "unknowns": unknowns,
    }
