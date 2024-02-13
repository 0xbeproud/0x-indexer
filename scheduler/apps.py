import os

from django.apps import AppConfig


class SchedulerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'scheduler'

    def ready(self):
        super().ready()
        if os.environ.get('RUN_MAIN', None) != 'true':
            print("APP STARTED!!!")
            from scheduler import jobs
            jobs.start()

