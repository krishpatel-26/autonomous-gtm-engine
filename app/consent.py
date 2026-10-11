from dataclasses import dataclass

@dataclass(frozen=True)
class OutreachEligibility:
    eligible: bool
    reason: str

def evaluate_outreach_eligibility(*, has_valid_contact: bool, has_required_consent: bool,
                                  is_suppressed: bool, human_approved: bool) -> OutreachEligibility:
    if is_suppressed:
        return OutreachEligibility(False, "contact_is_suppressed")
    if not has_valid_contact:
        return OutreachEligibility(False, "missing_or_invalid_contact")
    if not has_required_consent:
        return OutreachEligibility(False, "required_consent_missing")
    if not human_approved:
        return OutreachEligibility(False, "awaiting_human_approval")
    return OutreachEligibility(True, "eligible_for_authorized_delivery")
