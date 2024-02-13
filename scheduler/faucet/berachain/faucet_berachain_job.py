from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore

from indexer.settings.base import TIME_ZONE


def start():
    scheduler = BackgroundScheduler(timezone=TIME_ZONE)
    scheduler.add_jobstore(DjangoJobStore(), 'djangojobstore')

    # https://apscheduler.readthedocs.io/en/master/userguide.html#combining-multiple-triggers
    # @scheduler.scheduled_job('cron', hours='*/8', name='berachain-faucet')
    @scheduler.scheduled_job('interval', seconds=30, name='berachain-faucet')
    def job():
        from .faucet import faucet
        faucet()

    scheduler.start()
