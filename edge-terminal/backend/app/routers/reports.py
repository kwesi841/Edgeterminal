from fastapi import APIRouter, HTTPException
import os
from os import makedirs
from typing import List
from ..services.report_builder import build_daily_micro_alpha
from ..services.smtp_sender import send_html_email

router = APIRouter(prefix="/api/reports", tags=["reports"])

REPORTS_DIR = "/tmp/reports"

@router.get("")
def list_reports() -> List[str]:
    if not os.path.isdir(REPORTS_DIR):
        makedirs(REPORTS_DIR, exist_ok=True)
        return []
    return sorted(os.listdir(REPORTS_DIR))

@router.get("/{name}")
def get_report(name: str) -> str:
    path = os.path.join(REPORTS_DIR, name, "index.html")
    if not os.path.isfile(path):
        raise HTTPException(status_code=404, detail="Report not found")
    with open(path, "r") as f:
        return f.read()


@router.post("/build/today")
def build_today():
    return {"dir": build_daily_micro_alpha()}


@router.post("/send/{name}")
def send_report(name: str, recipients: List[str]):
    path = os.path.join(REPORTS_DIR, name, "index.html")
    if not os.path.isfile(path):
        raise HTTPException(status_code=404, detail="Report not found")
    with open(path, "r") as f:
        html = f.read()
    status = send_html_email(f"Edge Report {name}", recipients, html)
    return {"status": status}
