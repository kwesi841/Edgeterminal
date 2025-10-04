import numpy as np
import pandas as pd
from typing import Dict


def realized_vol(close: pd.Series, window: int = 30) -> float:
    returns = close.pct_change().dropna()
    return float(returns.tail(window).std() * np.sqrt(365))


def risk_score(features: Dict[str, float]) -> float:
    # weights per spec
    weights = {
        "realized_vol": 0.30,
        "float_stress_proxy": 0.25,
        "volume_tr_z": 0.20,
        "corr_btc_eth": 0.15,
        "funding_skew_proxy_abs": 0.10,
    }
    score = 0.0
    for k, w in weights.items():
        score += w * float(max(0.0, min(1.0, features.get(k, 0.0))))
    return round(score * 100.0, 2)
