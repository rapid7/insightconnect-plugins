import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input

# Custom imports below
from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException
from grr_api_client import api


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

        self.grrapi = None
        self.api_endpoint = None
        self.username = None
        self.password = None
        self.ssl_verify = None

    def connect(self, params):
        self.logger.info("Connect: Connecting...")
        self.api_endpoint = params.get(Input.API_ENDPOINT)
        self.username = params.get(Input.CREDENTIALS, {}).get("username")
        self.password = params.get(Input.CREDENTIALS, {}).get("password")
        self.ssl_verify = params.get(Input.SSL_VERIFY)
        try:
            self.grrapi = api.InitHttp(
                api_endpoint=self.api_endpoint,
                auth=(self.username, self.password),
                verify=self.ssl_verify,
            )
        except Exception as error:
            self.logger.error("Please provide valid options to connect to the GRR API endpoint")
            raise ConnectionTestException(preset=PluginException.Preset.UNKNOWN, data=error)

    def test(self) -> None:
        try:
            self.grrapi.ListHunts()
            return {"success": True}
        except Exception as error:
            raise ConnectionTestException(preset=PluginException.Preset.UNKNOWN, data=error)
