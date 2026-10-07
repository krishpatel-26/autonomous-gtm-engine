from .models import AccountSignal, GTMResult

WEIGHTS = {
    "scale": 0.15,
    "hiring": 0.25,
    "funding": 0.20,
    "tech_fit": 0.20,
    "intent": 0.20,
}

def _clamp(value: float) -> float:
    return max(0.0, min(1.0, value))

def score(s: AccountSignal) -> GTMResult:
    scale = _clamp(s.employee_count / 500)
    hiring = _clamp(s.hiring_ai / 5)
    funding = 1.0 if s.recent_funding else 0.0

    normalized = {
        "scale": scale,
        "hiring": hiring,
        "funding": funding,
        "tech_fit": s.tech_fit,
        "intent": s.intent,
    }
    score_value = round(sum(normalized[k] * WEIGHTS[k] for k in WEIGHTS) * 100)

    reasons = []
    if scale >= 0.4:
        reasons.append("meaningful company scale")
    if hiring >= 0.6:
        reasons.append("active AI hiring")
    if s.recent_funding:
        reasons.append("recent funding signal")
    if s.tech_fit >= 0.7:
        reasons.append("strong technology fit")
    if s.intent >= 0.7:
        reasons.append("strong buying intent")

    signal_strength = sum(normalized.values()) / len(normalized)
    confidence = round(0.4 + 0.6 * signal_strength, 2)
    tier = "hot" if score_value >= 75 else "warm" if score_value >= 50 else "cold"

    if confidence < 0.60:
        action = "enrich missing signals before outreach"
    elif tier == "hot":
        action = "prioritize personalized outreach"
    elif tier == "warm":
        action = "add to targeted sequence"
    else:
        action = "nurture and enrich"

    return GTMResult(
        company=s.company,
        score=score_value,
        tier=tier,
        confidence=confidence,
        reasons=reasons,
        next_action=action,
    )
