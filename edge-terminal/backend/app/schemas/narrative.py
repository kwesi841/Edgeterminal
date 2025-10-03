from pydantic import BaseModel
from datetime import datetime
from typing import List

class Narrative(BaseModel):
    id: int
    name: str
    keywords: List[str]
    freq_score: float
    status: str
    updated_at: datetime

    class Config:
        from_attributes = True
