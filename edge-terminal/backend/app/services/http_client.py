import os
import json
import time
from typing import Dict, Any, Optional
import requests

CACHE_DIR = os.path.join(".cache", "http")
os.makedirs(CACHE_DIR, exist_ok=True)

DEFAULT_TIMEOUT = 20

class HttpClient:
    def __init__(self):
        self.session = requests.Session()

    def _cache_path(self, url: str, params: Optional[Dict[str, Any]]) -> str:
        key = url
        if params:
            key += "?" + "&".join(f"{k}={v}" for k, v in sorted(params.items()))
        safe = key.replace("/", "_").replace(":", "_").replace("?", "_").replace("&", "_")
        return os.path.join(CACHE_DIR, safe + ".json")

    def _load_cache(self, path: str) -> Optional[Dict[str, Any]]:
        try:
            with open(path, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return None

    def _save_cache(self, path: str, payload: Dict[str, Any]) -> None:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w") as f:
            json.dump(payload, f)

    def get(self, url: str, params: Optional[Dict[str, Any]] = None, ttl_seconds: int = 900) -> Dict[str, Any]:
        cache_path = self._cache_path(url, params)
        cached = self._load_cache(cache_path)

        headers: Dict[str, str] = {}
        now = int(time.time())
        if cached:
            if "etag" in cached:
                headers["If-None-Match"] = cached["etag"]
            if "last_modified" in cached:
                headers["If-Modified-Since"] = cached["last_modified"]
            if cached.get("fetched_at", 0) + ttl_seconds > now and "body" in cached:
                return cached["body"]

        resp = self.session.get(url, params=params, timeout=DEFAULT_TIMEOUT, headers=headers)
        if resp.status_code == 304 and cached and "body" in cached:
            return cached["body"]
        resp.raise_for_status()
        body = resp.json()
        payload = {
            "fetched_at": now,
            "etag": resp.headers.get("ETag"),
            "last_modified": resp.headers.get("Last-Modified"),
            "body": body,
        }
        self._save_cache(cache_path, payload)
        return body

http_client = HttpClient()
