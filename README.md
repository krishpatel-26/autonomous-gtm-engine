# Autonomous GTM Engine

AI-assisted GTM decision engine that converts account signals into scored opportunities, confidence-aware reasoning, and auditable next actions. Deterministic locally; ready for CRM/enrichment adapters.

## Decision pipeline

`signals -> normalized features -> weighted score -> confidence -> action`

The scorer uses explicit weights for company scale, AI hiring, funding, technology fit, and buying intent. Confidence is deliberately separate from the opportunity score: low-confidence accounts are routed to enrichment instead of being pushed directly into outreach.

## Run

`pip install -r requirements.txt`

`uvicorn app.api:app --reload`

POST `/v1/score` with account signals.
