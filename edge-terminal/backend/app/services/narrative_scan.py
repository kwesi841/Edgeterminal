from typing import Dict, List
import feedparser
from datetime import datetime, timezone
from ..config import settings

DEFAULT_KEYWORDS = {
    "ETF": ["etf", "spot etf"],
    "DeFi": ["defi", "dex", "amm"],
    "NFT": ["nft", "non-fungible"],
    "Layer2": ["layer 2", "l2", "optimistic", "zk"],
    "AI": ["ai", "artificial intelligence"],
}


def scan_rss(sources: List[str] | None = None, keywords_map: Dict[str, List[str]] | None = None) -> Dict[str, float]:
    sources = sources or settings.rss_sources
    keywords_map = keywords_map or DEFAULT_KEYWORDS
    counts = {k: 0 for k in keywords_map}
    total = 0
    for src in sources:
        feed = feedparser.parse(src)
        for entry in feed.entries[:100]:
            text = (entry.get("title", "") + " " + entry.get("summary", "")).lower()
            for name, keys in keywords_map.items():
                if any(k in text for k in keys):
                    counts[name] += 1
            total += 1
    if total == 0:
        return {k: 0.0 for k in counts}
    return {k: v / total for k, v in counts.items()}
