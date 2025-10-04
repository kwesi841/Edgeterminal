from typing import List, Dict
from datetime import datetime
import os
import plotly.graph_objects as go
from sqlalchemy.orm import Session
from ..db.session import SessionLocal
from ..models.token import Token
from ..models.market import MarketCandle
from ..models.signal import Signal

REPORT_ROOT = "/tmp/reports"


def ensure_dir(p: str):
    os.makedirs(p, exist_ok=True)


def build_daily_micro_alpha() -> str:
    db: Session = SessionLocal()
    try:
        ts = datetime.utcnow().strftime("%Y-%m-%d")
        out_dir = os.path.join(REPORT_ROOT, ts)
        ensure_dir(out_dir)

        tokens = db.query(Token).limit(3).all()
        charts: List[str] = []
        for t in tokens:
            candles = (
                db.query(MarketCandle)
                .filter(MarketCandle.token_id == t.id)
                .order_by(MarketCandle.ts.asc())
                .all()
            )
            if len(candles) < 10:
                continue
            fig = go.Figure(
                data=[
                    go.Candlestick(
                        x=[c.ts for c in candles],
                        open=[c.open for c in candles],
                        high=[c.high for c in candles],
                        low=[c.low for c in candles],
                        close=[c.close for c in candles],
                        name=t.symbol,
                    )
                ]
            )
            png_path = os.path.join(out_dir, f"{t.symbol}.png")
            fig.write_image(png_path, engine="kaleido", scale=2, width=800, height=400)
            charts.append(png_path)

        html_path = os.path.join(out_dir, "index.html")
        with open(html_path, "w") as f:
            f.write("<html><body><h1>Daily Micro Alpha</h1>")
            for png in charts:
                f.write(f"<div><img src='{png}' style='max-width:800px' /></div>")
            f.write("</body></html>")
        return out_dir
    finally:
        db.close()
