from .models import AccountSignal,GTMResult
def score(s:AccountSignal)->GTMResult:
    pts=0; reasons=[]
    if s.employee_count>=200: pts+=15; reasons.append('meaningful company scale')
    if s.hiring_ai>=3: pts+=25; reasons.append('active AI hiring')
    if s.recent_funding: pts+=20; reasons.append('recent funding signal')
    pts+=round(s.tech_fit*20)+round(s.intent*20)
    tier='hot' if pts>=75 else 'warm' if pts>=50 else 'cold'
    action='prioritize personalized outreach' if tier=='hot' else 'add to targeted sequence' if tier=='warm' else 'nurture and enrich'
    return GTMResult(company=s.company,score=pts,tier=tier,reasons=reasons,next_action=action)
