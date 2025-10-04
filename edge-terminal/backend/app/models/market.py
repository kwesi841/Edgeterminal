from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey, UniqueConstraint
from .base import Base

class MarketCandle(Base):
    __tablename__ = "market_candles"
    __table_args__ = (
        UniqueConstraint("token_id", "ts", name="uix_token_ts"),
    )

    id = Column(Integer, primary_key=True)
    token_id = Column(Integer, ForeignKey("tokens.id"), index=True, nullable=False)
    ts = Column(DateTime, index=True, nullable=False)
    open = Column(Float, nullable=False)
    high = Column(Float, nullable=False)
    low = Column(Float, nullable=False)
    close = Column(Float, nullable=False)
    volume = Column(Float, nullable=False)
