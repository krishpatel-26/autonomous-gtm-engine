from app.consent import evaluate_outreach_eligibility

def test_suppression_takes_precedence():
    result = evaluate_outreach_eligibility(has_valid_contact=True, has_required_consent=True,
                                           is_suppressed=True, human_approved=True)
    assert not result.eligible and result.reason == "contact_is_suppressed"

def test_approval_is_required():
    result = evaluate_outreach_eligibility(has_valid_contact=True, has_required_consent=True,
                                           is_suppressed=False, human_approved=False)
    assert not result.eligible and result.reason == "awaiting_human_approval"

def test_eligible_only_when_all_gates_pass():
    result = evaluate_outreach_eligibility(has_valid_contact=True, has_required_consent=True,
                                           is_suppressed=False, human_approved=True)
    assert result.eligible
