from fastapi import FastAPI
from pydantic import BaseModel, Field
from .models import AccountSignal, GTMResult
from .scoring import score, score_many

app = FastAPI(title="Autonomous GTM Engine", version="1.1.0")

class BatchScoreRequest(BaseModel):
    accounts: list[AccountSignal] = Field(min_length=1, max_length=500)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/v1/score", response_model=GTMResult)
def score_account(signal: AccountSignal):
    return score(signal)

@app.post("/v1/score/batch", response_model=list[GTMResult])
def score_accounts(request: BatchScoreRequest):
    return score_many(request.accounts)
