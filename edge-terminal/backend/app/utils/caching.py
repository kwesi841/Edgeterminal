import os
import json
import time
from typing import Any

CACHE_DIR = os.path.join('.cache', 'http')


def clear_expired(ttl_seconds: int = 0) -> int:
    if not os.path.isdir(CACHE_DIR):
        return 0
    removed = 0
    now = int(time.time())
    for name in os.listdir(CACHE_DIR):
        p = os.path.join(CACHE_DIR, name)
        try:
            with open(p, 'r') as f:
                j = json.load(f)
            if ttl_seconds and j.get('fetched_at', now) + ttl_seconds < now:
                os.remove(p)
                removed += 1
        except Exception:
            continue
    return removed
