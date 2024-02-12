from apscheduler.schedulers.background import BackgroundScheduler

from indexer import settings


def start():
    scheduler = BackgroundScheduler(timezone=settings.TIME_ZONE)

    # https://apscheduler.readthedocs.io/en/master/userguide.html#combining-multiple-triggers
    @scheduler.scheduled_job('cron', hours='*/8', name='berachain-faucet')
    def job():
        from .faucet import faucet
        faucet()

    scheduler.start()
