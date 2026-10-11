# Campaign approval state machine

Suggested lifecycle:

DRAFT -> NEEDS_REVIEW -> APPROVED -> READY_TO_DELIVER -> DELIVERED

NEEDS_REVIEW may transition to REJECTED. APPROVED may transition to PAUSED.

Rules:
- Drafting does not imply approval.
- Approval references the exact plan/draft version reviewed.
- Material content or audience changes invalidate prior approval.
- Suppression and consent checks run again immediately before delivery.
- Rejected or paused campaigns cannot be delivered.
- Every transition records actor, timestamp, reason, and version.

This is a control contract; external delivery integration is not implied.
