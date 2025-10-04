import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import List
from ..config import settings


def send_html_email(subject: str, recipients: List[str], html: str) -> str:
    if not (settings.smtp_host and settings.smtp_port and settings.smtp_username and settings.smtp_password):
        return "SMTP not configured"
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = settings.smtp_username
    msg['To'] = ", ".join(recipients)
    part = MIMEText(html, 'html')
    msg.attach(part)

    with smtplib.SMTP(settings.smtp_host, settings.smtp_port) as server:
        if settings.smtp_use_tls:
            server.starttls()
        server.login(settings.smtp_username, settings.smtp_password)
        server.sendmail(settings.smtp_username, recipients, msg.as_string())
    return "sent"
