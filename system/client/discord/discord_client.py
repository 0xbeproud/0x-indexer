import datetime

import pendulum
import requests


class DiscordClient:
    def __init__(self, web_hook_url):
        self.web_hook_url = web_hook_url
    def send_message(self, payload):
        return requests.post(self.web_hook_url, json=payload)

    def faucet_done(self, name):
        return self.send_message({'content': f'[{pendulum.now().format("YYYY-MM-DD HH:mm:ss")}][{name}] has been claimed.'})