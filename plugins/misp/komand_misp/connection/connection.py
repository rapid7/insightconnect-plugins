import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException

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
        self.ssl = params.get(Input.SSL)
        try:
            self.client = pymisp.PyMISP(self.url, self.key, self.ssl, "json", debug=False)
            self.logger.info("Connect: Connected!")
        except:
            self.logger.error("Connect: Not Connected")
            raise PluginException(preset=PluginException.Preset.UNAUTHORIZED)

    def test(self):
        output = self.client.test_connection()
        self.logger.info(output)
        return {"status": True}
