import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException, ConnectionTestException

from .schema import ConnectionSchema, Input

# Custom imports below
import pymisp


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.key = None
        self.url = None
        self.ssl = None

    def connect(self, params):
        self.logger.info("Connect: Connecting...")
        self.url = params.get(Input.URL)
        self.key = params.get(Input.AUTOMATION_CODE).get("secretKey")
        self.ssl = params.get(Input.SSL, True)
        try:
            self.client = pymisp.PyMISP(self.url, self.key, self.ssl, debug=False)
            self.logger.info("Connect: Connected!")
        except:
            self.logger.error("Connect: Not Connected")
            raise PluginException(preset=PluginException.Preset.UNAUTHORIZED)

    def test(self):
        try:
            _ = self.client.version
            return {"status": True}
        except Exception:
            raise ConnectionTestException(
                cause="The connection to the Misp server has failed",
                assistance="Verify your plugin connection inputs are correct and not malformed and try again.",
            )
