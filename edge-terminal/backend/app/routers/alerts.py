from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..db.session import SessionLocal
from ..models.alert import Alert as AlertModel
from ..schemas.alert import Alert as AlertSchema

router = APIRouter(prefix="/api/alerts", tags=["alerts"])

@router.get("", response_model=List[AlertSchema])
def list_alerts():
    db: Session = SessionLocal()
    try:
        rows = db.query(AlertModel).all()
        return [AlertSchema.model_validate(r) for r in rows]
    finally:
        db.close()

@router.post("", response_model=AlertSchema)
def create_alert(alert: AlertSchema):
    db: Session = SessionLocal()
    try:
        a = AlertModel(
            id=alert.id,
            user_id=alert.user_id,
            type=alert.type,
            token_id=alert.token_id,
            condition=alert.condition,
            active=1 if alert.active else 0,
            created_at=alert.created_at,
        )
        db.merge(a)
        db.commit()
        return alert
    finally:
        db.close()
