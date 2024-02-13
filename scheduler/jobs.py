import atexit

from apscheduler.schedulers.background import BackgroundScheduler

from scheduler.faucet.berachain import faucet_berachain_job
from scheduler.faucet.berachain_sapo import faucet_berachain_job_sapo


def start():
    scheduler = BackgroundScheduler(timezone='Asia/Seoul')

    scheduler.add_job(faucet_berachain_job, 'interval', hours=4, minutes=5, name='faucet-berachain', max_instances=1)
    scheduler.add_job(faucet_berachain_job_sapo, 'interval', hours=4, minutes=5, name='faucet-berachain-sapo', max_instances=1)
    # scheduler.add_job(faucet_berachain_job, 'interval', minutes=1, name='faucet-berachain', max_instances=1)
    # scheduler.add_job(faucet_berachain_job_sapo, 'interval', minutes=1, name='faucet-berachain', max_instances=1)
    # scheduler.add_job(scraper, 'interval', seconds=30, name='scraper-me')
    scheduler.start()
    atexit.register(lambda: scheduler.shutdown())
