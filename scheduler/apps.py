import os

from apscheduler.schedulers.background import BackgroundScheduler
from django.apps import AppConfig


class SchedulerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'scheduler'

    def ready(self):
        super().ready()
        if os.environ.get('RUN_MAIN', None) != 'true':
            print('scheduler ready')
            from scheduler.faucet.berachain import faucet_berachain_job
            faucet_berachain_job.start()
            from scheduler.scraper.me import scraper_me_job
            scraper_me_job.start()

