from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from django.conf import settings
from django_apscheduler.jobstores import register_events

from .views import get_dbdata

def start():
    scheduler = BackgroundScheduler(timezone=settings.TIME_ZONE)
    register_events(scheduler)
    scheduler.add_executor
    scheduler.add_job(
        get_dbdata,
<<<<<<< HEAD
        trigger=CronTrigger(hour="09", minute="23"),
=======
        trigger=CronTrigger(hour="0", minute="0"),
>>>>>>> cf3ea15e45e15483bfbbfbc129b33fc8c15916b0
        max_instances=1,
        name="DB_update(movie,genre)",
    )

    scheduler.start()