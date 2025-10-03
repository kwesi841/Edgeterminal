from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey, String
from .base import Base
from datetime import datetime

class Portfolio(Base):
    __tablename__ = "portfolios"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    starting_value = Column(Float, default=0.0)
    cash = Column(Float, default=0.0)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

class Holding(Base):
    __tablename__ = "holdings"

    id = Column(Integer, primary_key=True)
    portfolio_id = Column(Integer, ForeignKey("portfolios.id"), index=True, nullable=False)
    token_id = Column(Integer, ForeignKey("tokens.id"), index=True, nullable=False)
    qty = Column(Float, default=0.0)
    avg_cost = Column(Float, default=0.0)
    last_mark = Column(Float, default=0.0)
    pnl = Column(Float, default=0.0)
    updated_at = Column(DateTime, default=datetime.utcnow, nullable=False)
