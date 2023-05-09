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
        # URL inputs and formation
        protocol = params.get(Input.PROTOCOL)
        host = params.get(Input.HOST)
        port = params.get(Input.PORT)

        url = f"{protocol}://{host}:{port}"
        self.logger.info(f"URL: {url}")

        # Credentials and others
        self.username = params.get(Input.PRINCIPAL).get("username")
        self.password = params.get(Input.PRINCIPAL).get("password", None)
        self.verify = params.get(Input.VERIFY, True)
        self.proxy = params.get(Input.PROXY, {})
        if self.proxy:
            self.logger.info(f"Proxy specified: {self.proxy}")

        self.logger.info("Connect: Connecting...")
        self.logger.info(f"SSL Verify: {str(self.verify)}")
        self.client = TheHiveApi(
            url=url,
            principal=self.username,
            password=self.password,
            proxies=self.proxy,
            cert=self.verify,
            version=4
        )

        self.logger.info("Setup Complete.")

    # def test(self):
    #     client = self.client
    #     try:
    #         user = client.get_current_user()
    #     except requests.exceptions.HTTPError:
    #         self.logger.error("Test failed")
    #         raise
    #     return user.json()
