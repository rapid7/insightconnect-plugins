import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input
from icon_cortex_v2.util.api import API

# Custom imports below
from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.API = None

    def connect(self, params={}):
        url = f"{params.get(Input.PROTOCOL).lower()}://{params.get(Input.HOST)}:{params.get(Input.PORT)}"
        api_key = params.get(Input.API_KEY).get("secretKey")
        verify = params.get(Input.VERIFY, True)
        self.logger.info(f"URL: {url}")

        proxy = {}
        if params.get(Input.PROXY):
            proxy = params.get(Input.PROXY)
            self.logger.info(f"Proxy specified: {proxy}")

        self.logger.info("Connect: Connecting...")
        self.API = API(url, api_key, verify_cert=verify, proxies=proxy)

    def test(self):
        try:
            response = self.API.status()
            # Expected = {"versions":{"Cortex":"1.1.4","Play":"2.5.9"},"config":{"authType":"none","capabilities":[]}}
            # Returns the BOOLEAN of whether Cortex exists in "versions" in the response data
            return "Cortex" in response.get("versions", {})
        except PluginException as error:
            self.logger.error(error)
            raise ConnectionTestException(error)
