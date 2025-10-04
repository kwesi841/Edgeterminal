from fastapi import APIRouter
from sqlalchemy.orm import Session
from typing import Dict
from ..db.session import SessionLocal
from ..models.token import Token
from ..models.market import MarketCandle
from ..models.signal import Signal
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
            latest = db.query(Signal).filter(Signal.token_id == t.id).order_by(Signal.ts.desc()).first()
            if latest:
                out[t.symbol] = latest.risk_score or 0.0
        return out
    finally:
        db.close()
