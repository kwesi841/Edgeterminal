from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
from .base import Base

class MarketCandle(Base):
    __tablename__ = "market_candles"

    id = Column(Integer, primary_key=True)
    token_id = Column(Integer, ForeignKey("tokens.id"), index=True, nullable=False)
    ts = Column(DateTime, index=True, nullable=False)
    open = Column(Float, nullable=False)
    high = Column(Float, nullable=False)
    low = Column(Float, nullable=False)
    close = Column(Float, nullable=False)
    volume = Column(Float, nullable=False)
