import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException

# Custom imports below
from icon_threatminer.util.api import ThreatminerAPI

from .schema import ConnectionSchema


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self) -> None:
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.api_client = None

    def connect(self, params={}):
        # pylint: disable=unused-argument
        self.api_client = ThreatminerAPI()

    def test(self):
        try:
            self.api_client.test()
            return {"success": True}
        except PluginException as error:
            raise ConnectionTestException(cause=error.cause, assistance=error.assistance, data=error.data)
