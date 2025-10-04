from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime, timedelta
from ..db.session import SessionLocal
from ..models.signal import Signal as SignalModel
from ..models.token import Token
from ..schemas.signal import Signal as SignalSchema

router = APIRouter(prefix="/api/signals", tags=["signals"])

@router.get("/top", response_model=List[SignalSchema])
def top_signals(metric: str = Query(default="conviction_score"), limit: int = Query(default=25, ge=1, le=100), db: Session = Depends(lambda: SessionLocal())):
    if metric not in {"conviction_score", "risk_score", "whale_inflow_proxy", "rsi"}:
        raise HTTPException(status_code=400, detail="unsupported metric")
    q = db.query(SignalModel).order_by(getattr(SignalModel, metric).desc()).limit(limit)
    return [SignalSchema(**{c.name: getattr(row, c.name) for c in SignalModel.__table__.columns}) for row in q.all()]

@router.get("/token/{token_id}", response_model=List[SignalSchema])
def token_signals(token_id: int, window: str = Query(default="7d"), db: Session = Depends(lambda: SessionLocal())):
    token = db.query(Token).filter(Token.id == token_id).first()
    if not token:
        raise HTTPException(status_code=404, detail="Token not found")
    now = datetime.utcnow()
    delta = timedelta(days=int(window[:-1])) if window.endswith("d") else timedelta(hours=int(window[:-1]))
    since = now - delta
    q = db.query(SignalModel).filter(SignalModel.token_id == token_id, SignalModel.ts >= since).order_by(SignalModel.ts.asc())
    return [SignalSchema(**{c.name: getattr(row, c.name) for c in SignalModel.__table__.columns}) for row in q.all()]
