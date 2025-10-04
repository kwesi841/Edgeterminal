from sqlalchemy.orm import Session
from ..models.market import MarketCandle
from ..models.signal import Signal
from ..services.indicators import rsi_wilder, obv, vpoc, ema, true_range, rolling_zscore
from ..services.risk_engine import realized_vol, risk_score
from ..services.conviction import conviction_score
from ..models.token import Token
import pandas as pd
from typing import Dict, Any


def compute_latest_signal(db: Session, token_id: int) -> None:
    candles = db.query(MarketCandle).filter(MarketCandle.token_id == token_id).order_by(MarketCandle.ts.asc()).all()
    if len(candles) < 20:
        return
    df = pd.DataFrame([
        {"ts": c.ts, "open": c.open, "high": c.high, "low": c.low, "close": c.close, "volume": c.volume}
        for c in candles
    ])
    close = df["close"]
    volume = df["volume"]
    high = df["high"]
    low = df["low"]

    rsi = float(rsi_wilder(close).iloc[-1])
    obv_series = obv(close, volume)
    obv_roc = obv_series.pct_change(periods=24).fillna(0)
    price_roc = close.pct_change(periods=24).fillna(0)
    obv_divergence = float((obv_roc - price_roc).iloc[-1])

    v_vpoc, nodes = vpoc(high, low, close, volume)

    n = 20
    basis = (close - ema(close, n)) / ema(close, n)
    funding_skew_proxy = float(basis.ewm(span=n, adjust=False).mean().iloc[-1])

    tr = true_range(high, low, close)
    oi_delta_proxy = float(rolling_zscore(volume * tr, window=30).fillna(0).iloc[-1])

    vol_ma = ema(volume, 20)
    whale_inflow_proxy = float(((volume - vol_ma) / (volume.rolling(20).std().replace(0, 1))).clip(lower=0).fillna(0).iloc[-1])

    social_chain_divergence = float((price_roc - obv_roc).iloc[-1])

    # Float stress proxy: normalize market cap vs 30D realized vol
    tok = db.query(Token).filter(Token.id == token_id).first()
    mcap = float(tok.market_cap or 0.0)
    rv = realized_vol(close, 30)  # ~annualized
    # Simple normalization heuristics
    mcap_norm = min(1.0, mcap / 1e10)  # 10B reference
    rv_norm = min(1.0, rv / 1.0)       # 1.0 annualized reference
    float_stress_proxy = float(max(0.0, min(1.0, (mcap_norm + rv_norm) / 2)))

    # Compose features and compute scores
    momentum = max(0.0, min(1.0, (rsi - 50.0) / 50.0))
    features_conv = {
        "momentum": momentum,
        "whale_inflow_proxy": max(0.0, min(1.0, whale_inflow_proxy)),
        "narrative": 0.0,
        "correlation_fit": 0.5,
        "float_stress_inv": 1.0 - float_stress_proxy,
        "funding_skew_proxy": max(0.0, min(1.0, funding_skew_proxy + 0.5)),
    }
    conviction = conviction_score(features_conv)

    features_risk = {
        "realized_vol": min(1.0, rv / 1.0),
        "float_stress_proxy": float_stress_proxy,
        "volume_tr_z": max(0.0, min(1.0, abs(oi_delta_proxy) / 3.0)),
        "corr_btc_eth": 0.5,
        "funding_skew_proxy_abs": max(0.0, min(1.0, abs(funding_skew_proxy))),
    }
    risk = risk_score(features_risk)

    sig = Signal(
        token_id=token_id,
        ts=df["ts"].iloc[-1],
        rsi=rsi,
        obv=float(obv_series.iloc[-1]),
        vpoc=float(v_vpoc),
        funding_skew_proxy=funding_skew_proxy,
        oi_delta_proxy=oi_delta_proxy,
        whale_inflow_proxy=whale_inflow_proxy,
        social_chain_divergence=social_chain_divergence,
        narrative_freq=0.0,
        float_stress_proxy=float_stress_proxy,
        conviction_score=conviction,
        risk_score=risk,
        sniper_flag=0,
        details={"volume_nodes": nodes, "proxy_flags": {"funding": True, "oi": True, "whale": True}},
    )
    db.merge(sig)
