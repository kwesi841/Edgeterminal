from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..schemas.token import Token as TokenSchema
from ..models.token import Token
from ..db.session import SessionLocal
from ..deps import get_db
from ..services.data_ingest import fetch_top_tokens
from datetime import datetime

router = APIRouter(prefix="/api/tokens", tags=["tokens"])

@router.get("", response_model=List[TokenSchema])
def list_tokens(limit: int = Query(default=25, ge=1, le=200), db: Session = Depends(get_db)):
    rows = db.query(Token).limit(limit).all()
    if not rows:
        # seed from coingecko once
        top = fetch_top_tokens(limit=limit)
        for t in top:
            tok = Token(
                symbol=t["symbol"].upper(),
                name=t["name"],
                chain=None,
                coingecko_id=t["id"],
                tags=t.get("categories"),
                market_cap=t.get("market_cap"),
                price=t.get("current_price"),
                volume_24h=t.get("total_volume"),
                last_updated=datetime.utcnow(),
            )
            db.merge(tok)
        db.commit()
        rows = db.query(Token).limit(limit).all()
    return rows

@router.get("/{token_id}", response_model=TokenSchema)
def get_token(token_id: int, db: Session = Depends(get_db)):
    token = db.query(Token).filter(Token.id == token_id).first()
    if not token:
        raise HTTPException(status_code=404, detail="Token not found")
    return token
