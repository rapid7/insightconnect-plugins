import insightconnect_plugin_runtime
from .schema import ConnectionSchema
from icon_cortex_v2.util.api import API

# Custom imports below
from insightconnect_plugin_runtime.exceptions import ConnectionTestException


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

        self.logger.info("Connect: Connecting..")
        self.API = API(url, api_key, verify_cert=verify, proxies=proxy)

    def test(self):
        try:
            self.API.analyzers.definitions()
        except AuthenticationError as e:
            self.logger.error(e)
            raise ConnectionTestException(preset=ConnectionTestException.Preset.API_KEY)
        except ServiceUnavailableError as e:
            self.logger.error(e)
            raise ConnectionTestException(preset=ConnectionTestException.Preset.SERVICE_UNAVAILABLE)
        return {}
