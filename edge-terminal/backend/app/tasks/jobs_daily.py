from ..services.data_ingest import fetch_top_tokens, fetch_ohlc
from ..db.session import SessionLocal
from ..models.token import Token
from ..models.market import MarketCandle
from datetime import datetime

def run() -> None:
    db = SessionLocal()
    try:
        top = fetch_top_tokens(limit=25)
        existing = {t.coingecko_id: t for t in db.query(Token).all()}
        for t in top:
            tok = existing.get(t["id"]) or Token(symbol=t["symbol"].upper(), name=t["name"], chain=None, coingecko_id=t["id"], tags=t.get("categories"))
            db.merge(tok)
        db.commit()
        tokens = db.query(Token).all()
        for tok in tokens:
            ohlc = fetch_ohlc(tok.coingecko_id, days=90)
            for row in ohlc:
                ts = datetime.utcfromtimestamp(row[0] / 1000)
                open_, high_, low_, close_ = map(float, row[1:5])
                candle = MarketCandle(token_id=tok.id, ts=ts, open=open_, high=high_, low=low_, close=close_, volume=0.0)
                db.merge(candle)
            db.commit()
    finally:
        db.close()
