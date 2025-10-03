from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.dialects.sqlite import JSON
from .base import Base
from datetime import datetime

class Report(Base):
    __tablename__ = "reports"

    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    title = Column(String, nullable=False)
    html_path = Column(String, nullable=False)
    png_paths = Column(JSON, nullable=True)
    recipients = Column(JSON, nullable=True)
    sent_via_smtp = Column(Integer, default=0)
    send_status = Column(String, nullable=True)
    send_ts = Column(DateTime, nullable=True)
