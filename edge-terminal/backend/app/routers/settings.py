from fastapi import APIRouter
from ..config import settings

router = APIRouter(prefix="/api/settings", tags=["settings"])

@router.get("")
def get_settings():
    return {
        "smtp_host": settings.smtp_host,
        "smtp_port": settings.smtp_port,
        "smtp_username": settings.smtp_username,
        "smtp_use_tls": settings.smtp_use_tls,
    }
