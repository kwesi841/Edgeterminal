from typing import Dict


def conviction_score(features: Dict[str, float]) -> float:
    weights = {
        "momentum": 0.25,
        "whale_inflow_proxy": 0.20,
        "narrative": 0.15,
        "correlation_fit": 0.10,
        "float_stress_inv": 0.15,
        "funding_skew_proxy": 0.15,
    }
    score = 0.0
    for k, w in weights.items():
        score += w * float(features.get(k, 0.0))
    return round(max(0.0, min(100.0, score * 100.0)), 2)
