from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..schemas.token import Token as TokenSchema
from ..models.token import Token
from ..db.session import SessionLocal
from ..deps import get_db

router = APIRouter(prefix="/api/tokens", tags=["tokens"])

@router.get("", response_model=List[TokenSchema])
def list_tokens(limit: int = Query(default=25, ge=1, le=200), db: Session = Depends(get_db)):
    return db.query(Token).limit(limit).all()

@router.get("/{token_id}", response_model=TokenSchema)
def get_token(token_id: int, db: Session = Depends(get_db)):
    token = db.query(Token).filter(Token.id == token_id).first()
    if not token:
        raise HTTPException(status_code=404, detail="Token not found")
    return token
