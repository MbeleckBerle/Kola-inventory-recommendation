from pydantic import BaseModel
from typing import List, Optional


class RecommendationRequest(BaseModel):
    region: str
    quarter: str
    top_n: Optional[int] = 5


class RecommendationResponse(BaseModel):
    region: str
    quarter: str
    recommendations: List[str]
    scores: List[float]
