from ..services.data_ingest import fetch_top_tokens, fetch_ohlc_and_volume
from ..db.session import SessionLocal
from ..models.token import Token
from ..models.market import MarketCandle
from datetime import datetime
import argparse
from ..config import settings
from ..services.signal_builder import compute_latest_signal

def run() -> None:
    db = SessionLocal()
    try:
        tokens = db.query(Token).all()
        if not tokens:
            top = fetch_top_tokens(limit=settings.universe_size)
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
            compute_latest_signal(db, tok.id)
            db.commit()
    finally:
        db.close()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--once", action="store_true", help="Run once and exit")
    args = parser.parse_args()
    run()


if __name__ == "__main__":
    main()
