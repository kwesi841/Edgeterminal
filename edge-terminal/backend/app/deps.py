from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from .db.session import SessionLocal
from jose import jwt, JWTError
from datetime import datetime, timedelta
from typing import Optional
from .config import settings

ALGORITHM = "HS256"

# DB session dependency

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# JWT helpers

def create_access_token(subject: str, expires_minutes: int = 60 * 24) -> str:
    expire = datetime.utcnow() + timedelta(minutes=expires_minutes)
    to_encode = {"sub": subject, "exp": expire}
    return jwt.encode(to_encode, settings.jwt_secret, algorithm=ALGORITHM)


def get_current_user_email(token: str) -> str:
    try:
        payload = jwt.decode(token, settings.jwt_secret, algorithms=[ALGORITHM])
        sub: Optional[str] = payload.get("sub")
        if sub is None:
            raise JWTError("missing sub")
        return sub
    except JWTError as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token") from e
