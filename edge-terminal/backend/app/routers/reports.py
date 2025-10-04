from fastapi import APIRouter, HTTPException
import os
from os import makedirs
from typing import List

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
