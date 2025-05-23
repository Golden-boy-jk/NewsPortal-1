import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "NewsPortal.settings")
app = Celery("NewsPortal")
app.config_from_object("django.conf:settings", namespace="CELERY")
# Настройка регулярных задач
app.conf.beat_schedule = {
    "send-weekly-newsletter": {
        "task": "news.tasks.send_weekly_newsletter",
        "schedule": crontab(minute="0", hour="8", day_of_week="1"),
    },
}
app.autodiscover_tasks(["news"])
