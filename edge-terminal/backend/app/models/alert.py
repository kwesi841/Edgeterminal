from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.dialects.sqlite import JSON
from .base import Base
from datetime import datetime

class Alert(Base):
    __tablename__ = "alerts"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), index=True, nullable=False)
    type = Column(String, nullable=False)
    token_id = Column(Integer, ForeignKey("tokens.id"), index=True, nullable=True)
    condition = Column(JSON, nullable=False)
    active = Column(Integer, default=1)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
