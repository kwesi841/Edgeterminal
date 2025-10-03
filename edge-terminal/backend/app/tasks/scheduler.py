from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from . import jobs_intraday, jobs_daily

def create_scheduler() -> BackgroundScheduler:
    scheduler = BackgroundScheduler()
    # Every 15 minutes ET (use system TZ configurable elsewhere)
    scheduler.add_job(jobs_intraday.run, CronTrigger(minute="*/15"), id="intraday")
    # Daily job 07:30 ET
    scheduler.add_job(jobs_daily.run, CronTrigger(hour=7, minute=30), id="daily")
    return scheduler
