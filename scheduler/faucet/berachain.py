import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from scheduler.utils.local_storage import LocalStorage
from system.client.discord.faucet_discrod_client import FaucetDiscordClient


def faucet_berachain_job() -> None:
    print("faucet-berachain")

    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    options.add_argument(
        "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
    )
    options.add_argument("lang=ko_KR")
    options.add_argument("no-sandbox")

    driver = webdriver.Chrome(options=options)
    driver.get(url="https://artio.faucet.berachain.com/")
    driver.implicitly_wait(3)

    local_storage = LocalStorage(driver)
    local_storage.set("FIRST_TIME_USER", "false")
    driver.refresh()
    time.sleep(2)

    wallet_address = driver.find_element(By.XPATH,
                                         '/html/body/div[1]/div[2]/main/div/div[1]/div/div[2]/div[2]/div/input')
    wallet_address.send_keys('0xB243b7a98C305fA5866c008d1B0452A474d8c398')

    claim_button = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/main/div/div[1]/div/button')
    claim_button.click()
    time.sleep(5)

    drip_button = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/main/div/div[1]/div/button')
    drip_button.click()

    FaucetDiscordClient().faucet_done('berachain')

    time.sleep(5)
    driver.quit()

