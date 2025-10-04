from pydantic_settings import BaseSettings
from pydantic import AnyHttpUrl
from typing import List

class Settings(BaseSettings):
    jwt_secret: str = "change_me"
    timezone: str = "America/New_York"
    coingecko_api_base: AnyHttpUrl = "https://api.coingecko.com/api/v3"
    rss_sources: List[AnyHttpUrl] = [
        "https://www.coindesk.com/arc/outboundfeeds/rss/?outputType=xml",
        "https://cointelegraph.com/rss",
        "https://decrypt.co/feed",
    ]
    universe_size: int = 25
    smtp_host: str | None = None
    smtp_port: int | None = None
    smtp_username: str | None = None
    smtp_password: str | None = None
    smtp_use_tls: bool = True

    class Config:
        env_file = ".env"
        env_prefix = ""
        case_sensitive = False

settings = Settings()
