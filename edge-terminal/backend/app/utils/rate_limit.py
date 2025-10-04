import time
from collections import deque
from typing import Deque, Dict


class InMemoryRateLimiter:
    def __init__(self, max_requests: int, window_seconds: int):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self._buckets: Dict[str, Deque[float]] = {}

    def allow(self, key: str) -> bool:
        now = time.time()
        dq = self._buckets.setdefault(key, deque())
        while dq and now - dq[0] > self.window_seconds:
            dq.popleft()
        if len(dq) >= self.max_requests:
            return False
        dq.append(now)
        return True


login_limiter = InMemoryRateLimiter(max_requests=10, window_seconds=60 * 5)
