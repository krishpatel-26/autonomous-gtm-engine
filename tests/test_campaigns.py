from app.campaigns import build_campaign
from app.models import GTMResult

def result(tier="hot", confidence=0.9):
    return GTMResult(company="ExampleCo", score=82, tier=tier, confidence=confidence, reasons=["strong fit"], next_action="prioritize personalized outreach")

def test_outreach_requires_approval_by_default():
    steps = build_campaign(result())
    outreach = next(step for step in steps if step.name == "send_outreach")
    assert outreach.status == "approval_required"

def test_approved_campaign_marks_outreach_approved():
    steps = build_campaign(result(), approved=True)
    outreach = next(step for step in steps if step.name == "send_outreach")
    assert outreach.status == "approved"

def test_low_confidence_only_enriches():
    steps = build_campaign(result(confidence=0.4))
    assert [step.name for step in steps] == ["enrich_signals"]
