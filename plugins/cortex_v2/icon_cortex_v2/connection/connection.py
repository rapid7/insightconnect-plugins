import insightconnect_plugin_runtime
from .schema import ConnectionSchema
from icon_cortex_v2.util.api import API

# Custom imports below
from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.API = None

    def connect(self, params={}):
        url = f"{params.get('protocol').lower()}://{params.get('host')}:{params.get('port')}"
        api_key = params.get("api_key").get("secretKey")
        verify = params.get("verify", True)
        self.logger.info(f"URL: {url}")

        if not params.get("proxy"):
            proxy = {}
        else:
            proxy = params.get("proxy")
            self.logger.info(f"Proxy specified: {proxy}")

        self.logger.info("Connect: Connecting...")
        self.API = API(url, api_key, verify_cert=verify, proxies=proxy)

    def test(self):
        try:
            response = self.API.status()
            # Expected = {"versions":{"Cortex":"1.1.4","Play":"2.5.9"},"config":{"authType":"none","capabilities":[]}}
            return "Cortex" in response.get("versions", {})
        except PluginException as e:
            self.logger.error(e)
            raise ConnectionTestException(e)
