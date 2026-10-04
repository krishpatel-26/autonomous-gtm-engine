from fastapi import FastAPI
from .models import AccountSignal,GTMResult
from .scoring import score
app=FastAPI(title='Autonomous GTM Engine',version='1.0.0')
@app.get('/health')
def health(): return {'status':'ok'}
@app.post('/v1/score',response_model=GTMResult)
def score_account(signal:AccountSignal): return score(signal)
