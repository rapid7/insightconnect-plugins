import insightconnect_plugin_runtime
from .schema import ConnectionSchema

# Custom imports below
from cortex4py.api import Api
from cortex4py.exceptions import ServiceUnavailableError, AuthenticationError
from insightconnect_plugin_runtime.exceptions import ConnectionTestException


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params={}):
        url = "{}://{}:{}".format(params.get("protocol").lower(), params.get("host"), params.get("port"))
        api_key = params.get("api_key").get("secretKey")
        self.verify = params.get("verify", True)
        self.logger.info("URL: %s", url)

        if not params.get("proxy"):
            self.proxy = {}
        else:
            self.proxy = params.get("proxy")
            self.logger.info("Proxy specified: %s", self.proxy)

        self.logger.info("Connect: Connecting..")
        self.api = Api(url, api_key, verify_cert=self.verify, proxies=self.proxy)

    def test(self):
        try:
            self.api.analyzers.definitions()
        except AuthenticationError as e:
            self.logger.error(e)
            raise ConnectionTestException(preset=ConnectionTestException.Preset.API_KEY)
        except ServiceUnavailableError as e:
            self.logger.error(e)
            raise ConnectionTestException(preset=ConnectionTestException.Preset.SERVICE_UNAVAILABLE)
        return {}
