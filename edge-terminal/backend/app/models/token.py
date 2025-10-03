from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.dialects.sqlite import JSON
from .base import Base
from datetime import datetime

class Token(Base):
    __tablename__ = "tokens"

    id = Column(Integer, primary_key=True)
    symbol = Column(String, index=True, nullable=False)
    name = Column(String, nullable=False)
    chain = Column(String, nullable=True)
    coingecko_id = Column(String, unique=True, index=True, nullable=False)
    tags = Column(JSON, nullable=True)
    last_updated = Column(DateTime, default=datetime.utcnow)
