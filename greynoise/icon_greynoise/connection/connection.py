import insightconnect_plugin_runtime
from .schema import ConnectionSchema

# Custom imports below

from greynoise import GreyNoise
from greynoise.exceptions import RequestFailure
from insightconnect_plugin_runtime.exceptions import ConnectionTestException


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.api_key = None
        self.server = None
        self.user_agent = None
        self.gn_client = None

    def connect(self, params):
        self.api_key = params.get("credentials").get("secretKey", "")
        self.server = "https://api.greynoise.io"
        self.user_agent = f"rapid7-insightconnect-v{self.meta.version}"
        self.gn_client = GreyNoise(api_server=self.server, api_key=self.api_key, integration_name=self.user_agent)
        self.logger.info("Connect: Connecting...")

    def test(self):
        try:
            resp = self.gn_client.test_connection()

        except RequestFailure as e:
            if e.args[0] == 401:
                raise ConnectionTestException(preset=ConnectionTestException.Preset.API_KEY, data=e.args[1])
            elif e.args[0] == 429:
                raise ConnectionTestException(preset=ConnectionTestException.Preset.RATE_LIMIT, data=e.args[1])
            elif e.args[0] == 500:
                raise ConnectionTestException(preset=ConnectionTestException.Preset.SERVER_ERROR, data=e.args[1])

        return resp
