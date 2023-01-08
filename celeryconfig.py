from celery.schedules import crontab


CELERY_IMPORTS = ('app.tasks.tasklist')
CELERY_TASK_RESULT_EXPIRES = 30
CELERY_TIMEZONE = 'UTC'

CELERY_ACCEPT_CONTENT = ['json', 'msgpack', 'yaml']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

CELERYBEAT_SCHEDULE = {
    'test-celery': {
        'task': 'app.tasks.tasklist.print_hello',
        # Every minute
        'schedule': crontab(minute="*"),
    },
    'num-writer': {
        'task': 'app.tasks.tasklist.number_writer',
        # Every minute
        'schedule': crontab(minute="*"),
    },
    # fetching youtube data every 60s
    'video-fetcher': {
        'task': 'app.tasks.tasklist.videofetch',
        # Every minute
        'schedule': crontab(minute="*"),
    }
}
