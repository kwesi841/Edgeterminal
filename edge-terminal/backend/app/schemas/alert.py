from pydantic import BaseModel
from datetime import datetime
from typing import Dict, Any

class Alert(BaseModel):
    id: int
    user_id: int
    type: str
    token_id: int | None
    condition: Dict[str, Any]
    active: bool
    created_at: datetime

    class Config:
        from_attributes = True
