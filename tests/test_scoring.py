from app.models import AccountSignal
from app.scoring import score
def test_hot_account():
 r=score(AccountSignal(company='Acme',employee_count=500,hiring_ai=5,recent_funding=True,tech_fit=1,intent=1))
 assert r.tier=='hot' and r.score>=75
