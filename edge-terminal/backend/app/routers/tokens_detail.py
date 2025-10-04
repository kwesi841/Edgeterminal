from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from ..deps import get_db
from ..models.token import Token
from ..models.market import MarketCandle
from ..models.signal import Signal

router = APIRouter(prefix="/api/tokens", tags=["tokens"]) 

@router.get("/{token_id}/detail")
def token_detail(token_id: int, db: Session = Depends(get_db)):
    tok = db.query(Token).filter(Token.id == token_id).first()
    if not tok:
        raise HTTPException(status_code=404, detail="Token not found")
    candles = db.query(MarketCandle).filter(MarketCandle.token_id == token_id).order_by(MarketCandle.ts.desc()).limit(300).all()
    latest_signal = db.query(Signal).filter(Signal.token_id == token_id).order_by(Signal.ts.desc()).first()
    return {
        "token": {
            "id": tok.id,
            "symbol": tok.symbol,
            "name": tok.name,
            "market_cap": tok.market_cap,
            "price": tok.price,
            "volume_24h": tok.volume_24h,
        },
        "candles": [
            {
                "ts": c.ts.isoformat(),
                "open": c.open,
                "high": c.high,
                "low": c.low,
                "close": c.close,
                "volume": c.volume,
            } for c in reversed(candles)
        ],
        "signal": {c.name: getattr(latest_signal, c.name) for c in latest_signal.__table__.columns} if latest_signal else None,
    }
