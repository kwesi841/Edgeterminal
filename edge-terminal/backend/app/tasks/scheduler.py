from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from pytz import timezone
from ..config import settings
from . import jobs_intraday, jobs_daily

def create_scheduler() -> BackgroundScheduler:
    scheduler = BackgroundScheduler(timezone=timezone(settings.timezone))
    scheduler.add_job(jobs_intraday.run, CronTrigger(minute="*/15", timezone=settings.timezone), id="intraday")
    scheduler.add_job(jobs_daily.run, CronTrigger(hour=7, minute=30, timezone=settings.timezone), id="daily")
    return scheduler
