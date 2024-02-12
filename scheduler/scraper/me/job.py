from apscheduler.schedulers.background import BackgroundScheduler

from indexer import settings


def start():
    scheduler = BackgroundScheduler(timezone=settings.TIME_ZONE)

    # https://apscheduler.readthedocs.io/en/master/userguide.html#combining-multiple-triggers
    @scheduler.scheduled_job('cron', minute='*/1', name='me')
    def job():
        from .scraper import scraper
        scraper()

    scheduler.start()
