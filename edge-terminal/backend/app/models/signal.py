from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey, UniqueConstraint, Index
from sqlalchemy.dialects.sqlite import JSON
from .base import Base

class Signal(Base):
    __tablename__ = "signals"
    __table_args__ = (
        UniqueConstraint("token_id", "ts", name="uix_signal_token_ts"),
        Index("ix_signal_ts", "ts"),
    )

    id = Column(Integer, primary_key=True)
    token_id = Column(Integer, ForeignKey("tokens.id"), index=True, nullable=False)
    ts = Column(DateTime, index=True, nullable=False)
    rsi = Column(Float)
    obv = Column(Float)
    vpoc = Column(Float)
    funding_skew_proxy = Column(Float)
    oi_delta_proxy = Column(Float)
    whale_inflow_proxy = Column(Float)
    social_chain_divergence = Column(Float)
    narrative_freq = Column(Float)
    float_stress_proxy = Column(Float)
    conviction_score = Column(Float)
    risk_score = Column(Float)
    sniper_flag = Column(Integer)
    details = Column(JSON)
