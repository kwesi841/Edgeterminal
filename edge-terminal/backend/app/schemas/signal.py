from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List, Dict, Any

class Signal(BaseModel):
    token_id: int
    ts: datetime
    rsi: Optional[float]
    obv: Optional[float]
    vpoc: Optional[float]
    funding_skew_proxy: Optional[float]
    oi_delta_proxy: Optional[float]
    whale_inflow_proxy: Optional[float]
    social_chain_divergence: Optional[float]
    narrative_freq: Optional[float]
    float_stress_proxy: Optional[float]
    conviction_score: Optional[float]
    risk_score: Optional[float]
    sniper_flag: Optional[bool]
    details: Optional[Dict[str, Any]]
