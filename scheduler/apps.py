import os

from django.apps import AppConfig

from scheduler.scraper.me import job


class SchedulerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'scheduler'

    def ready(self):
        super().ready()
        if os.environ.get('RUN_MAIN', None) != 'true':
            job.start()
