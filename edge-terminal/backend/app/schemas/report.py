from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class Report(BaseModel):
    id: int
    created_at: datetime
    title: str
    html_path: str
    png_paths: Optional[List[str]]
    recipients: Optional[List[str]]
    sent_via_smtp: bool
    send_status: Optional[str]
    send_ts: Optional[datetime]

    class Config:
        from_attributes = True
