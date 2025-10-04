from fastapi import APIRouter
from sqlalchemy.orm import Session
from typing import Dict
from ..db.session import SessionLocal
from ..models.token import Token
from ..models.market import MarketCandle
import pandas as pd
from ..services.risk_engine import realized_vol, risk_score

router = APIRouter(prefix="/api/risk", tags=["risk"])

@router.get("/heatmap")
def heatmap():
    db: Session = SessionLocal()
    try:
        out: Dict[str, float] = {}
        tokens = db.query(Token).all()
        for t in tokens:
            candles = db.query(MarketCandle).filter(MarketCandle.token_id == t.id).order_by(MarketCandle.ts.asc()).all()
            if len(candles) < 30:
                continue
            close = pd.Series([c.close for c in candles])
            vol = realized_vol(close, 30)
            features = {
                "realized_vol": min(1.0, vol / 1.0),
                "float_stress_proxy": 0.5,
                "volume_tr_z": 0.5,
                "corr_btc_eth": 0.5,
                "funding_skew_proxy_abs": 0.2,
            }
            out[t.symbol] = risk_score(features)
        return out
    finally:
        db.close()
