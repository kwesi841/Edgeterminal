from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..db.session import SessionLocal
from ..models.portfolio import Portfolio as PortfolioModel, Holding as HoldingModel
from ..models.token import Token
from ..schemas.portfolio import Portfolio as PortfolioSchema, Holding as HoldingSchema

router = APIRouter(prefix="/api/portfolios", tags=["portfolios"])

@router.get("", response_model=List[PortfolioSchema])
def list_portfolios():
    db: Session = SessionLocal()
    try:
        rows = db.query(PortfolioModel).all()
        if not rows:
            p = PortfolioModel(name="Demo", starting_value=200.0, cash=200.0)
            db.add(p)
            db.commit()
            db.refresh(p)
            rows = [p]
        return [PortfolioSchema.model_validate(p) for p in rows]
    finally:
        db.close()

@router.get("/{portfolio_id}")
def get_portfolio(portfolio_id: int):
    db: Session = SessionLocal()
    try:
        p = db.query(PortfolioModel).filter(PortfolioModel.id == portfolio_id).first()
        if not p:
            raise HTTPException(status_code=404, detail="Not found")
        holdings = db.query(HoldingModel).filter(HoldingModel.portfolio_id == p.id).all()
        return {
            "portfolio": PortfolioSchema.model_validate(p),
            "holdings": [HoldingSchema.model_validate(h) for h in holdings],
        }
    finally:
        db.close()
