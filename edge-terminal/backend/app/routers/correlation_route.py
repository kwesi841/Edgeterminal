from fastapi import APIRouter
from sqlalchemy.orm import Session
from ..db.session import SessionLocal
from ..models.token import Token
from ..models.market import MarketCandle
import pandas as pd
from ..services.correlation import correlation_matrix

router = APIRouter(prefix="/api/risk", tags=["risk"]) 

@router.get("/correlation")
def correlation():
    db: Session = SessionLocal()
    try:
        prices = {}
        tokens = db.query(Token).all()
        for t in tokens:
            candles = db.query(MarketCandle).filter(MarketCandle.token_id == t.id).order_by(MarketCandle.ts.asc()).all()
            if len(candles) >= 90:
                prices[t.symbol] = pd.Series([c.close for c in candles])
        return correlation_matrix(prices)
    finally:
        db.close()
