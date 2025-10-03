from pydantic import BaseModel
from datetime import datetime
from typing import List

class Holding(BaseModel):
    id: int
    token_id: int
    qty: float
    avg_cost: float
    last_mark: float
    pnl: float
    updated_at: datetime

    class Config:
        from_attributes = True

class Portfolio(BaseModel):
    id: int
    name: str
    starting_value: float
    cash: float
    created_at: datetime
    
    class Config:
        from_attributes = True
