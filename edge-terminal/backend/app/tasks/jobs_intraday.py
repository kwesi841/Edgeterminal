from ..services.data_ingest import fetch_top_tokens, fetch_ohlc_and_volume
from ..db.session import SessionLocal
from ..models.token import Token
from ..models.market import MarketCandle
from datetime import datetime

def run() -> None:
    db = SessionLocal()
    try:
        tokens = db.query(Token).all()
        if not tokens:
            top = fetch_top_tokens(limit=25)
            for t in top:
                token = Token(symbol=t["symbol"].upper(), name=t["name"], chain=None, coingecko_id=t["id"], tags=t.get("categories"))
                db.add(token)
            db.commit()
            tokens = db.query(Token).all()
        for tok in tokens:
            candles = fetch_ohlc_and_volume(tok.coingecko_id, days=1)
            for c in candles:
                candle = MarketCandle(
                    token_id=tok.id,
                    ts=c["ts"],
                    open=c["open"],
                    high=c["high"],
                    low=c["low"],
                    close=c["close"],
                    volume=c["volume"],
                )
                db.merge(candle)
            db.commit()
    finally:
        db.close()
