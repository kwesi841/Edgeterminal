from typing import Dict


def sniper_flag(metrics: Dict[str, float]) -> bool:
    return (
        metrics.get("rsi", 100.0) < 35.0
        and metrics.get("obv_divergence", 0.0) > 0.0
        and metrics.get("whale_inflow_proxy", 0.0) > 2.0
        and metrics.get("ret_30m", 1.0) <= 0.02
    )
