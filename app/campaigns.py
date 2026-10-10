from dataclasses import dataclass
from .models import GTMResult


@dataclass(frozen=True)
class CampaignStep:
    name: str
    status: str
    reason: str


def build_campaign(result: GTMResult, approved: bool = False) -> list[CampaignStep]:
    """Build a deterministic campaign plan with explicit safety stop conditions."""
    if result.confidence < 0.60:
        return [
            CampaignStep("enrich_signals", "ready", "Confidence is below outreach threshold."),
            CampaignStep("stop", "blocked", "Do not personalize or contact until signals are verified."),
        ]
    if result.tier == "cold":
        return [
            CampaignStep("nurture", "ready", "Low-fit accounts enter a low-pressure nurture path."),
            CampaignStep("stop", "ready", "No direct outbound step is scheduled for cold accounts."),
        ]

    steps = [CampaignStep("research_account", "ready", "Collect account context before personalization.")]
    if result.tier == "warm":
        steps.append(CampaignStep("enrich_signals", "ready", "Fill signal gaps before campaign entry."))
    steps.append(CampaignStep("personalize_message", "ready", "Use verified account signals only."))
    steps.append(CampaignStep(
        "send_outreach",
        "approved" if approved else "approval_required",
        "Human approval is required before external outreach.",
    ))
    if not approved:
        steps.append(CampaignStep("stop", "blocked", "Execution halts until approval is recorded."))
    return steps
