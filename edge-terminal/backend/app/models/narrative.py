from sqlalchemy import Column, Integer, String, DateTime, Float
from sqlalchemy.dialects.sqlite import JSON
from .base import Base
from datetime import datetime

class Narrative(Base):
    __tablename__ = "narratives"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    keywords = Column(JSON, nullable=False)
    freq_score = Column(Float, default=0.0)
    status = Column(String, default="Ready")
    updated_at = Column(DateTime, default=datetime.utcnow, nullable=False)
