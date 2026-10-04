# Autonomous GTM Engine

AI-assisted GTM decision engine that converts account signals into scored opportunities, reasons, and auditable next actions. Deterministic locally; ready for CRM/enrichment adapters.

## Run
`pip install -r requirements.txt` then `uvicorn app.api:app --reload`.
POST `/v1/score` with account signals.
