from fastapi import APIRouter
from sqlalchemy.orm import Session
from typing import List
from ..db.session import SessionLocal
from ..models.narrative import Narrative as NarrativeModel
from ..schemas.narrative import Narrative as NarrativeSchema

router = APIRouter(prefix="/api/narratives", tags=["narratives"])

@router.get("", response_model=List[NarrativeSchema])
def list_narratives():
    db: Session = SessionLocal()
    try:
        rows = db.query(NarrativeModel).all()
        return [NarrativeSchema.model_validate(row) for row in rows]
    finally:
        db.close()
