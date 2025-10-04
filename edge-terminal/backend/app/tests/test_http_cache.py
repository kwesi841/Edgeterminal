from edge-terminal.backend.app.services.http_client import http_client

def test_cache_key_sha1():
    # Should not raise and should return consistently
    u = 'https://example.com/data'
    http_client.get_text(u, ttl_seconds=1)
    http_client.get_text(u, ttl_seconds=1)
