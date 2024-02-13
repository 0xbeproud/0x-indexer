from system.client.discord.discord_client import DiscordClient


class FaucetDiscordClient(DiscordClient):
    WEB_HOOK_URL = 'https://discord.com/api/webhooks/1194080074765434930/3IGjEQ7iAhNvPNzLp72oZUGLn3d84GCWelvx9UnX43Yksty1YJGg4Ki9oiHQ7-vYd_US'

    def __init__(self):
        super().__init__(web_hook_url=self.WEB_HOOK_URL)