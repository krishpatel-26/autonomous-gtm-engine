from pydantic import BaseModel, Field

class AccountSignal(BaseModel):
    company: str = Field(min_length=2, max_length=200)
    employee_count: int = Field(ge=1)
    hiring_ai: int = Field(ge=0)
    recent_funding: bool = False
    tech_fit: float = Field(ge=0, le=1)
    intent: float = Field(ge=0, le=1)

class GTMResult(BaseModel):
    company: str
    score: int
    tier: str
    confidence: float
    reasons: list[str]
    next_action: str
