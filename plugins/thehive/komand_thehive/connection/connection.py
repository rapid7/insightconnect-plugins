import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input

# Custom imports below
from ..util.api import HiveAPI


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.api_key = None
        self.password = None
        self.username = None
        self.verify = None
        self.client = None
        self.proxy = None

    def connect(self, params={}):
        protocol = params.get(Input.PROTOCOL)
        host = params.get(Input.HOST)
        port = params.get(Input.PORT)

        self.api_key = params.get(Input.API_KEY).get("secretKey")
        self.password = params.get(Input.CREDENTIALS).get("password")
        self.username = params.get(Input.CREDENTIALS).get("username")
        self.verify = params.get(Input.VERIFY, True)
        self.proxy = params.get(Input.PROXY, {})

        url = f"{protocol}://{host}:{port}/"
        self.logger.info(f"URL: {url}")

        if self.proxy:
            self.logger.info(f"Proxy specified: {self.proxy}")

        self.logger.info("Connect: Connecting...")
        self.logger.info(f"SSL Verify: {str(self.verify)}")

        self.client = HiveAPI(
            url=url,
            username=self.username,
            password=self.password,
            api_key=self.api_key,
            proxies=self.proxy,
            cert=self.verify,
        )

        self.logger.info("Setup Complete")

    # def test(self):
    #     client = self.client
    #     try:
    #         user = client.get_current_user()
    #     except requests.exceptions.HTTPError:
    #         self.logger.error("Test failed")
    #         raise
    #     return user.json()
