import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input

# Custom imports below
from thehive4py.api import TheHiveApi
import requests


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.password = None
        self.username = None
        self.verify = None
        self.client = None
        self.proxy = None

    def connect(self, params):
        url = f"{params.get(Input.PROTOCOL)}://{params.get(Input.HOST).rstrip('/')}:{params.get(Input.PORT)}"
        self.password = params.get(Input.CREDENTIALS).get("password")
        self.username = params.get(Input.CREDENTIALS).get("username")
        self.verify = params.get(Input.VERIFY, True)
        self.logger.info(f"URL: {url}")

        if not params.get(Input.PROXY):
            self.proxy = {}
        else:
            self.proxy = params.get(Input.PROXY)
            self.logger.info(f"Proxy specified: {self.proxy}")

        self.logger.info("Connect: Connecting...")
        self.logger.info(f"SSL Verify: {str(self.verify)}")
        self.client = TheHiveApi(
            url=url,
            principal=self.username,
            password=self.password,
            proxies=self.proxy,
            cert=self.verify,
        )

    def test(self):
        client = self.client
        try:
            user = client.get_current_user()
        except requests.exceptions.HTTPError:
            self.logger.error("Test failed")
            raise
        return user.json()
