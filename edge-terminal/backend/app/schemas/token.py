from pydantic import BaseModel
from typing import Optional, List

class Token(BaseModel):
    id: int
    symbol: str
    name: str
    chain: Optional[str]
    coingecko_id: str
    tags: Optional[List[str]]

    class Config:
        from_attributes = True
