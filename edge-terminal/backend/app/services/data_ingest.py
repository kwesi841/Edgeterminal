from typing import List, Dict, Any
from datetime import datetime
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


def fetch_ohlc(coingecko_id: str, days: int = 90) -> List[List[float]]:
    url = f"{COINGECKO}/coins/{coingecko_id}/ohlc"
    params = {"vs_currency": "usd", "days": days}
    data = http_client.get(url, params=params, ttl_seconds=900)
    return data
