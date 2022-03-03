import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input

# Custom imports below
from OTXv2 import OTXv2
from insightconnect_plugin_runtime.exceptions import PluginException, ConnectionTestException


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.client = None

    def connect(self, params={}):
        self.client = OTXv2(params.get(Input.API_KEY).get("secretKey"), server=params.get(Input.URL))

    def test(self):
        try:
            self.client.search_users("")
            return {"success": True}
        except Exception:
            raise ConnectionTestException(preset=PluginException.Preset.API_KEY)
