# https://docs.celeryq.dev/en/stable/userguide/periodic-tasks.html#crontab-schedules
# https://github.com/sibson/redbeat

from app import create_app
from celery.schedules import crontab

## Scheduled
from app.jobs.support_queries import notify_new_queries

## Event Based
from app.jobs.support_queries import notify_status

flask_app = create_app()
celery_app = flask_app.extensions["celery"]
celery_app.conf.timezone = 'UTC'

celery_app.conf.beat_schedule = {
    'notify_new_queries': {
        'task': 'app.jobs.support_queries.notify_new_queries.call',
        'schedule': flask_app.config['CELERY_SCHEDULE_NOTIFY_NEW_QUERIES'],
        'relative': True,
        'args': ()
    },
}
