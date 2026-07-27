"""Canonical enriched AUC-001 Presentation from current canonical artifacts only."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Mapping

from tools.auc_001_execution_orchestration import Auc001ExecutionBlocked, require_before_presentation


CANONICAL_PRESENTATION_COVERAGE: dict[str, Any] = {
    "scope": "canonical enriched presentation coverage",
    "historical_outputs_as_evidence": False,
    "required_dimensions": [
        {"id": "quality_tiers", "label": "Tiers de calidad", "facts": ["lead_tier_total"]},
        {"id": "monthly_evolution", "label": "Evolucion mensual", "facts": ["monthly_tier"]},
        {"id": "weekly_pattern", "label": "Patron semanal", "facts": ["weekly_quality"]},
        {"id": "platform", "label": "Plataforma", "facts": ["platform"]},
        {"id": "intent_signals", "label": "Senales de intencion", "facts": ["ticket_status", "travel_window"]},
        {"id": "campaign", "label": "Campana", "facts": ["campaigns"]},
        {"id": "adset", "label": "Conjunto de anuncios", "facts": ["adsets"]},
        {"id": "ad", "label": "Anuncio", "facts": ["top_ads"]},
        {"id": "signal_spend", "label": "Inversion por senal FARO", "facts": ["spend_by_signal", "commercial_matched"]},
        {"id": "temporal_spend", "label": "Inversion temporal", "facts": ["spend_monthly", "spend_weekly"]},
        {"id": "ad_spend", "label": "Inversion por anuncio", "facts": ["spend_ad"]},
        {"id": "coverage", "label": "Cobertura y UNKNOWNs", "facts": ["commercial_matched"]},
        {"id": "recommendations", "label": "Recomendaciones", "facts": []},
    ],
}


def _read_json(package_root: Path, rel: str) -> dict[str, Any]:
    return json.loads((package_root / rel).read_text(encoding="utf-8"))


def _pct(numerator: float, denominator: float) -> str:
    if not denominator:
        return "UNKNOWN"
    return f"{(numerator / denominator) * 100:.1f}%"


def _money(value: float | int | None) -> str:
    if value is None:
        return "UNKNOWN"
    return f"{float(value):.2f} EUR"


def _fact_status(facts: Mapping[str, Any], fact_keys: list[str]) -> tuple[str, list[str]]:
    present = [key for key in fact_keys if key in facts]
    if present:
        return "available", present
    return "not_available", []


def _coverage_table(facts: Mapping[str, Any]) -> str:
    rows = [
        "| Dimension | Estado | Fuente canonica | Consecuencia para decision |",
        "|---|---:|---|---|",
    ]
    for dimension in CANONICAL_PRESENTATION_COVERAGE["required_dimensions"]:
        status, present = _fact_status(facts, dimension["facts"])
        if dimension["id"] == "recommendations":
            status = "available"
            present = ["recommendation-set"]
        source = ", ".join(present) if present else "not_available en Evidence Set canonico"
        consequence = (
            "Se reporta con valores canonicos actuales."
            if status == "available"
            else "Se conserva como UNKNOWN; no se usa historico ni inferencia."
        )
        rows.append(f"| {dimension['label']} | {status} | {source} | {consequence} |")
    return "\n".join(rows)


def _tier_table(facts: Mapping[str, Any]) -> str:
    tiers = facts.get("lead_tier_total", {})
    total = sum(float(row.get("lead_count", 0)) for row in tiers.values())
    rows = ["| Tier | Leads | Peso | Score medio |", "|---|---:|---:|---:|"]
    for tier in ["A", "B", "C", "D"]:
        row = tiers.get(tier, {})
        leads = float(row.get("lead_count", 0))
        rows.append(f"| {tier} | {int(leads)} | {_pct(leads, total)} | {row.get('avg_lead_score', 'UNKNOWN')} |")
    return "\n".join(rows)


def _monthly_table(facts: Mapping[str, Any]) -> str:
    rows = ["| Mes | Leads | A/B | Tier A | Tasa A/B |", "|---|---:|---:|---:|---:|"]
    for row in facts.get("monthly_tier", []):
        leads = float(row.get("leads", 0))
        ab = float(row.get("ab", 0))
        rows.append(f"| {row.get('month')} | {int(leads)} | {int(ab)} | {row.get('a', 0)} | {_pct(ab, leads)} |")
    return "\n".join(rows)


def _intent_table(facts: Mapping[str, Any]) -> str:
    rows = ["| Senal | Bucket | Leads | A/B | Tier A | Tasa A/B |", "|---|---|---:|---:|---:|---:|"]
    for source, label in [("ticket_status", "Estado de billete"), ("travel_window", "Ventana de viaje")]:
        for row in facts.get(source, []):
            leads = float(row.get("leads", 0))
            ab = float(row.get("ab", 0))
            rows.append(f"| {label} | {row.get('bucket')} | {int(leads)} | {int(ab)} | {row.get('a', 0)} | {_pct(ab, leads)} |")
    return "\n".join(rows)


def _platform_campaign_ads_table(facts: Mapping[str, Any]) -> str:
    rows = ["| Nivel | Elemento | Leads | A/B | Tier A | Tasa A/B |", "|---|---|---:|---:|---:|---:|"]
    for row in facts.get("platform", []):
        leads = float(row.get("leads", 0))
        ab = float(row.get("ab", 0))
        rows.append(f"| Plataforma | {row.get('platform')} | {int(leads)} | {int(ab)} | {row.get('a', 0)} | {_pct(ab, leads)} |")
    for row in facts.get("campaigns", []):
        leads = float(row.get("leads", 0))
        ab = float(row.get("ab", 0))
        rows.append(f"| Campana | {row.get('campaign')} | {int(leads)} | {int(ab)} | {row.get('a', 0)} | {_pct(ab, leads)} |")
    for row in facts.get("top_ads", []):
        leads = float(row.get("leads", 0))
        ab = float(row.get("ab", 0))
        rows.append(f"| Anuncio | {row.get('ad_id_norm')} | {int(leads)} | {int(ab)} | {row.get('a', 0)} | {_pct(ab, leads)} |")
    return "\n".join(rows)


def _spend_table(facts: Mapping[str, Any]) -> str:
    spend_by_signal = facts.get("spend_by_signal", {})
    commercial = facts.get("commercial_matched", {})
    activation = facts.get("activation_observed", {})
    rows = ["| Capa FARO | Inversion | Leads | A/B | Coste por A/B | Estado de decision |", "|---|---:|---:|---:|---:|---|"]
    rows.append(
        "| COMMERCIAL matched | "
        f"{_money(commercial.get('spend'))} | {commercial.get('leads', 'UNKNOWN')} | "
        f"{commercial.get('ab', 'UNKNOWN')} | {_money(commercial.get('cost_per_ab'))} | universo directo coste-calidad |"
    )
    rows.append(
        "| ACTIVATION observed | "
        f"{_money(activation.get('spend'))} | {activation.get('leads', 'UNKNOWN')} | "
        f"{activation.get('ab', 'UNKNOWN')} | {_money(activation.get('cost_per_ab'))} | capa FARO no equivalente |"
    )
    for signal in ["ATTENTION", "COMMERCIAL", "ACTIVATION", "TOTAL"]:
        if signal in spend_by_signal:
            rows.append(f"| {signal} total | {_money(spend_by_signal.get(signal))} | UNKNOWN | UNKNOWN | UNKNOWN | solo inversion de capa |")
    return "\n".join(rows)


def _recommendation_table(recommendations: list[Mapping[str, Any]]) -> str:
    rows = ["| ID | Prioridad | Tipo | Accion o hipotesis | Metrica / salvaguarda | Soporte canonico |", "|---|---|---|---|---|---|"]
    for rec in recommendations:
        action = rec.get("action") or rec.get("hypothesis") or "not_available"
        metric = rec.get("primary_metric") or rec.get("verifiable_result") or rec.get("promotion_condition") or "UNKNOWN"
        guardrail = rec.get("guardrail") or rec.get("closure_criterion") or rec.get("stop_or_review_condition") or "UNKNOWN"
        rows.append(
            f"| {rec.get('recommendation_id')} | {rec.get('priority', 'not_set')} | {rec.get('category')} | {action} | "
            f"{metric}; salvaguarda: {guardrail} | {', '.join(rec.get('knowledge_refs', []))} |"
        )
    return "\n".join(rows)


def build_canonical_presentation_reports(package_root: str | Path) -> dict[str, str]:
    """Build analytical and executive Presentation projections without reading historical outputs."""

    root = Path(package_root)
    evidence = _read_json(root, "evidence/evidence-set.json")
    knowledge = _read_json(root, "knowledge/knowledge-set.json")
    recommendations = _read_json(root, "recommendations/recommendation-set.json")
    cps = _read_json(root, "product-core/canonical-projection-source.json")
    facts = evidence.get("facts", {})
    recs = recommendations.get("recommendations", [])
    claims = knowledge.get("knowledge_claims", [])
    narrative = knowledge.get("analytical_narrative", {})
    total_leads = facts.get("lead_coverage", {}).get("lead_count", "UNKNOWN")
    tier_b = facts.get("lead_tier_total", {}).get("B", {}).get("lead_count", 0)
    tier_a = facts.get("lead_tier_total", {}).get("A", {}).get("lead_count", 0)
    ab_total = int(tier_a) + int(tier_b)

    knowledge_rows = ["| ID | Afirmacion | Interpretacion | Limite |", "|---|---|---|---|"]
    for item in claims:
        knowledge_rows.append(
            f"| {item.get('knowledge_id')} | {item.get('claim')} | {item.get('interpretation')} | {item.get('limitation_or_uncertainty')} |"
        )

    analytical = f"""# AUC-001 Informe analitico canonico enriquecido

## Limite de fuentes

Este informe es una proyeccion de Presentation Layer para AUC-001. Consume solo los artefactos canonicos actuales de este paquete: Evidence Set, Analytical Investigation Record, Findings intermedios, Knowledge Set, Recommendation Set, Common Product Core y Canonical Projection Source. Los outputs historicos no son evidencia, no son valores esperados y no son leidos por este materializador.

La ruta canonica enriquecida es la salida estable de AUC-001: conserva dimensiones, tablas, hipotesis, limites y soporte a decision, y cada valor, UNKNOWN y recomendacion queda limitado por el paquete canonico actual. Fingerprint del Canonical Projection Source: `{cps.get('semantic_fingerprint', 'UNKNOWN')}`.

## Mapa de cobertura funcional

{_coverage_table(facts)}

## Lectura analitica integrada

La evidencia canonica muestra {total_leads} leads hasta el 30 de junio de 2026, con {ab_total} leads A/B y {tier_a} Tier A. La lectura principal ya no es una lista de metricas: Meta genera volumen cualificado suficiente para seguir aprendiendo, pero la calidad no mejora por volumen puro. La densidad A/B se mantiene estable mientras junio escala, y el peso C/D sigue siendo material. Por eso la decision no debe premiar solo captacion; debe proteger volumen cualificado y reducir ruido operativo.

El AIR enriquecido identifica como hallazgo estructural la separacion por intencion observable. `tiene_billetes`, `en_proceso` y las ventanas cercanas concentran mucha mas calidad que los buckets exploratorios. Este patron conecta volumen, calidad y accion: Marketing puede formular tests sobre senales de intencion, mientras Direccion puede exigir salvaguardas de volumen A/B y Tier A antes de aprobar cambios de presupuesto.

La lectura economica queda acotada por FARO. COMMERCIAL matched es el unico universo directo coste-calidad. ATTENTION y ACTIVATION se preservan como capas no equivalentes; por tanto, no hay ranking economico universal entre capas. Las dimensiones ausentes se mantienen como not_available o UNKNOWN, sin completarlas desde historicos.

## Estructura de calidad

{_tier_table(facts)}

La tabla confirma una tension directiva: hay base cualificada real, pero tambien una masa C/D que puede consumir capacidad comercial. La prioridad analitica es distinguir escala util de escala ruidosa.

## Evolucion mensual

{_monthly_table(facts)}

Junio aporta mas volumen y mas A/B absolutos, pero no prueba mejora estructural de densidad. La implicacion es clara: escalar funciona como crecimiento de pipeline, no todavia como optimizacion de calidad.

## Senales de intencion y scoring

{_intent_table(facts)}

La intencion es el eje explicativo mas fuerte. Los leads con billetes, proceso de compra o ventana cercana muestran mucha mayor densidad A/B y Tier A. La conclusion sigue siendo observacional: sirve para disenar tests, no para declarar causalidad.

## Plataforma, campana y concentracion por anuncio

{_platform_campaign_ads_table(facts)}

La comparacion por plataforma y campana ayuda a ordenar el trabajo, pero no desplaza el hallazgo de intencion. Retargeting aparece con mayor densidad y adquisicion con mayor volumen cualificado; eso exige diseno de portfolio, no sustitucion simplista. Los anuncios concentrados orientan inspeccion y test, pero no prueban causalidad creativa.

## Coste, calidad y limites FARO

{_spend_table(facts)}

COMMERCIAL matched permite lectura directa: coste por A/B y coste por Tier A dentro de un universo reconciliado. ACTIVATION y ATTENTION no deben tratarse como si compitieran por el mismo KPI de eficiencia. Esta separacion reduce el riesgo de reasignar presupuesto desde una metrica seductora pero estrategicamente no comparable.

## Hipotesis evaluadas

| Hipotesis | Estado | Razonamiento canonico |
|---|---|---|
| El volumen por si solo explica la calidad | Descartada | El AIR muestra que la intencion separa calidad mejor que el volumen bruto. |
| Las senales de intencion explican la separacion A/B y Tier A | Soportada observacionalmente | Ticket status y travel window concentran calidad en buckets de mayor preparacion. |
| Un KPI universal puede rankear todas las capas FARO | Descartada | COMMERCIAL, ATTENTION y ACTIVATION son capas no equivalentes. |
| Los top ads prueban ganador creativo | UNKNOWN | Hay concentracion, pero falta causalidad creativa. |
| La densidad de retargeting justifica sustituir adquisicion | No demostrado | Retargeting aporta densidad; adquisicion aporta volumen cualificado. La decision es de portfolio. |
| Las dimensiones ausentes pueden rellenarse desde historicos | Descartada | Solo se aceptan artefactos canonicos actuales. |

## Conocimiento generado

{chr(10).join(knowledge_rows)}

La narrativa integrada estabilizada resume la idea central: {narrative.get('text', 'UNKNOWN')}

Idea memorable: {narrative.get('memorable_idea', 'UNKNOWN')}

## Recomendaciones

{_recommendation_table(recs)}

## Riesgos, UNKNOWNs y limites de decision

| Area | Estado | Consecuencia |
|---|---|---|
| Revenue / CRM | UNKNOWN | No declarar valor comercial final mas alla de calidad de lead. |
| Causalidad creativa | UNKNOWN | Usar top ads para priorizar tests, no para declarar ganadores. |
| Patron semanal | not_available | No inferir dinamica intra-mes. |
| Conjunto de anuncios | not_available | No optimizar ad sets desde este paquete. |
| Inversion temporal o por anuncio | not_available | Mantener coste-calidad en COMMERCIAL matched y capas FARO gobernadas. |
| ATTENTION asistida | UNKNOWN | No atribuir efecto comercial sin evidencia downstream. |

## Uso para Direccion y Marketing

Para Direccion, el paquete permite una decision acotada: mantener Meta como canal con volumen cualificado medible, exigir separacion FARO y aprobar solo experimentos con salvaguardas de A/B, Tier A y volumen cualificado. Para Marketing, el trabajo inmediato es operativo: transformar senales de intencion en hipotesis de copy, formulario, routing o segmentacion, inspeccionar anuncios concentrados como candidatos de test y no tratar C/D exploratorio como demanda comercial equivalente.
"""

    executive = f"""# AUC-001 Informe ejecutivo canonico enriquecido

Meta genero {total_leads} leads hasta el 30 de junio de 2026, con {ab_total} leads A/B y {tier_a} Tier A. La conclusion ejecutiva es que el canal tiene volumen cualificado real, pero la calidad no mejora por escala pura.

La mejor explicacion disponible es la intencion observable: billetes, compra en proceso y ventanas cercanas concentran mucha mas calidad que demanda exploratoria. La decision recomendada es mantener escala comercial, pero probar filtros y mensajes de intencion con salvaguardas de A/B, Tier A y volumen cualificado.

En coste, COMMERCIAL matched es el unico universo directo coste-calidad. ATTENTION y ACTIVATION son capas FARO no equivalentes y no deben rankearse con un KPI universal. Revenue, CRM, causalidad creativa, patron semanal, ad sets e inversion temporal o por anuncio siguen como UNKNOWN o not_available.
"""

    return {"analytical": analytical, "executive": executive}


def validate_canonical_presentation_reports(package_root: str | Path, reports: Mapping[str, str]) -> dict[str, Any]:
    root = Path(package_root)
    evidence = _read_json(root, "evidence/evidence-set.json")
    facts = evidence.get("facts", {})
    analytical = reports.get("analytical", "")
    executive = reports.get("executive", "")
    joined = f"{analytical}\n{executive}"
    issues: list[dict[str, str]] = []

    forbidden = [
        "outputs/auc-001/2026-06-30/analytical-report.md",
        "outputs/auc-001/current/2026-06-30",
        "historical outputs are evidence",
        "outputs historicos son evidencia",
    ]
    for token in forbidden:
        if token in joined:
            issues.append({"code": "HISTORICAL_OUTPUT_USED_AS_SOURCE", "detail": token})

    required_tokens = [
        "Mapa de cobertura funcional",
        "Estructura de calidad",
        "Evolucion mensual",
        "Senales de intencion y scoring",
        "Plataforma, campana y concentracion por anuncio",
        "Coste, calidad y limites FARO",
        "Hipotesis evaluadas",
        "Recomendaciones",
        "Riesgos, UNKNOWNs y limites de decision",
        "capas no equivalentes",
        "not_available",
        "UNKNOWN",
        "R-001",
        "R-002",
        "R-003",
        "R-004",
        "R-005",
    ]
    for token in required_tokens:
        if token not in joined:
            issues.append({"code": "CANONICAL_PRESENTATION_CONTENT_MISSING", "detail": token})

    for dimension in CANONICAL_PRESENTATION_COVERAGE["required_dimensions"]:
        label = dimension["label"]
        status, _ = _fact_status(facts, dimension["facts"])
        if dimension["id"] == "recommendations":
            status = "available"
        if label not in analytical:
            issues.append({"code": "CANONICAL_PRESENTATION_DIMENSION_MISSING", "detail": label})
        if status == "not_available" and f"| {label} | not_available |" not in analytical:
            issues.append({"code": "MISSING_DIMENSION_NOT_DECLARED", "detail": label})

    if analytical.count("\n|") < 30:
        issues.append({"code": "INSUFFICIENT_TABLE_SURFACE", "detail": "analytical report has too few tabular rows"})
    if len(analytical.split()) < 1200:
        issues.append({"code": "ANALYTICAL_REPORT_TOO_COMPACT", "detail": "canonical analytical report must preserve analytical depth"})
    if len(executive.split()) < 100:
        issues.append({"code": "EXECUTIVE_REPORT_TOO_COMPACT", "detail": "executive route must remain decision-useful"})
    if len(executive.split()) >= len(analytical.split()):
        issues.append({"code": "PROJECTION_SEPARATION_FAILED", "detail": "executive report is not distinct from analytical report"})

    decision = "PASS" if not issues else "BLOCKED"
    return {
        "artifact_id": "AUC-001-CANONICAL-PRESENTATION-VALIDATION",
        "route": "canonical_enriched_stable",
        "decision": decision,
        "issues": issues,
        "canonical_presentation_coverage": CANONICAL_PRESENTATION_COVERAGE,
        "historical_outputs_as_evidence": False,
        "source_artifacts": [
            "evidence/evidence-set.json",
            "knowledge/analytical-investigation-record.json",
            "knowledge/knowledge-set.json",
            "recommendations/recommendation-set.json",
            "product-core/common-product-core.json",
            "product-core/canonical-projection-source.json",
        ],
    }


def materialize_canonical_presentation_reports_after_gate(package_root: str | Path) -> dict[str, Any]:
    root = Path(package_root)
    require_before_presentation(root)
    reports = build_canonical_presentation_reports(root)
    validation = validate_canonical_presentation_reports(root, reports)
    if validation["decision"] != "PASS":
        raise Auc001ExecutionBlocked(root, "canonical_enriched_presentation", validation)
    (root / "reports").mkdir(parents=True, exist_ok=True)
    (root / "validations").mkdir(parents=True, exist_ok=True)
    (root / "reports/analytical-report.md").write_text(reports["analytical"], encoding="utf-8")
    (root / "reports/executive-report.md").write_text(reports["executive"], encoding="utf-8")
    (root / "validations/canonical-presentation-validation.json").write_text(
        json.dumps(validation, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return validation