from app.models import AccountSignal
from app.scoring import score

def test_hot_account():
    r = score(AccountSignal(company="Acme", employee_count=500, hiring_ai=5, recent_funding=True, tech_fit=1, intent=1))
    assert r.tier == "hot" and r.score >= 75
    assert r.confidence == 1.0

def test_low_signal_account_gets_enrichment_action():
    r = score(AccountSignal(company="SmallCo", employee_count=1, hiring_ai=0, recent_funding=False, tech_fit=0, intent=0))
    assert r.tier == "cold"
    assert r.next_action == "enrich missing signals before outreach"
    assert r.confidence < 0.60
