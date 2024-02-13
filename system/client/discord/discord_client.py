import requests


class DiscordClient:
    def __init__(self, web_hook_url):
        self.web_hook_url = web_hook_url
    def send_message(self, payload):
        print(f"Sending message: {payload}")
        return requests.post(self.web_hook_url, json=payload)