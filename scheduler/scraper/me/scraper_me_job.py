from datetime import timezone

from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore


def start():
    scheduler = BackgroundScheduler(timezone=timezone('Asia/Seoul'))
    scheduler.add_jobstore(DjangoJobStore(), 'djangojobstore')

    # https://apscheduler.readthedocs.io/en/master/userguide.html#combining-multiple-triggers
    @scheduler.scheduled_job('interval', seconds=30, name='scraper-me')
    def job():
        from .scraper import scraper
        scraper()

    scheduler.start()
