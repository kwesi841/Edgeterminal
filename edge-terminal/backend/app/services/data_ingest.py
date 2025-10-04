from typing import List, Dict, Any, Tuple
from datetime import datetime
import pandas as pd
from ..config import settings
from .http_client import http_client

COINGECKO = settings.coingecko_api_base

# Minimal CoinGecko ingest wrappers with caching TTLs

def fetch_top_tokens(limit: int = 25) -> List[Dict[str, Any]]:
    url = f"{COINGECKO}/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "volume_desc",
        "per_page": 100,
        "page": 1,
        "sparkline": "false",
        "price_change_percentage": "24h",
    }
    data = http_client.get(url, params=params, ttl_seconds=3600)
    return data[:limit]


def fetch_ohlc_and_volume(coingecko_id: str, days: int = 90, interval: str | None = None) -> List[Dict[str, Any]]:
    # OHLC
    url_ohlc = f"{COINGECKO}/coins/{coingecko_id}/ohlc"
    params_ohlc = {"vs_currency": "usd", "days": days}
    ohlc = http_client.get(url_ohlc, params=params_ohlc, ttl_seconds=900)

    # Volumes via market_chart
    url_mc = f"{COINGECKO}/coins/{coingecko_id}/market_chart"
    params_mc = {"vs_currency": "usd", "days": days}
    if interval:
        params_mc["interval"] = interval
    mc = http_client.get(url_mc, params=params_mc, ttl_seconds=900)
    volumes = mc.get("total_volumes", [])

    # Build per-candle volume by differencing and aligning timestamps
    vol_df = pd.DataFrame(volumes, columns=["ts_ms", "cum_volume"]).set_index("ts_ms")
    vol_df.sort_index(inplace=True)
    vol_df["volume"] = vol_df["cum_volume"].diff().clip(lower=0).fillna(vol_df["cum_volume"])  # first value

    out: List[Dict[str, Any]] = []
    for row in ohlc:
        ts_ms, o, h, l, c = int(row[0]), float(row[1]), float(row[2]), float(row[3]), float(row[4])
        # Find nearest volume timestamp (CoinGecko uses same sampling grid)
        vol = float(vol_df.reindex(vol_df.index.union([ts_ms])).loc[ts_ms].get("volume", 0.0)) if ts_ms in vol_df.index else 0.0
        out.append({
            "ts": datetime.utcfromtimestamp(ts_ms / 1000),
            "open": o,
            "high": h,
            "low": l,
            "close": c,
            "volume": vol,
        })
    return out
