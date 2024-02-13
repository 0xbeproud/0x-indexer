import atexit

from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore

from scheduler.faucet.berachain import faucet_berachain_job


def start():
    scheduler = BackgroundScheduler(timezone='Asia/Seoul')
    # scheduler.add_jobstore(DjangoJobStore(), 'default')
    scheduler.add_job(faucet_berachain_job, 'interval', hours=8, minutes=5, name='faucet-berachain', max_instances=1)
    # scheduler.add_job(scraper, 'interval', seconds=30, name='scraper-me')
    scheduler.start()
    atexit.register(lambda: scheduler.shutdown())
