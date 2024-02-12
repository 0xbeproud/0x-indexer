import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from scheduler.utils.local_storage import LocalStorage


def faucet() -> None:
    print("me_faucet")

    faucet_url = "https://artio.faucet.berachain.com/"

    driver = webdriver.Chrome()
    driver.get(url=faucet_url)
    time.sleep(2)

    local_storage = LocalStorage(driver)
    local_storage.set("FIRST_TIME_USER", "false")
    driver.refresh()
    time.sleep(2)

    wallet_address = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/main/div/div[1]/div/div[2]/div[2]/div/input')
    wallet_address.send_keys('0xB243b7a98C305fA5866c008d1B0452A474d8c398')

    claim_button = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/main/div/div[1]/div/button')
    claim_button.click()
    time.sleep(5)

    drip_button = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/main/div/div[1]/div/button')
    drip_button.click()

    time.sleep(5)
    driver.quit()
