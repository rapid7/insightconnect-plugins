import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input

# Custom imports below
from insightconnect_plugin_runtime.exceptions import ConnectionTestException
from ..util.api import API


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.api = None

    def connect(self, params):
        self.logger.info("Connect: Connecting..")
        server = params.get(Input.URL)
        self.api = API(url=server)

    def test(self):
        endpoint = "cuckoo/status"
        try:
            self.api.send(endpoint)
            return {"success": True}
        except Exception as exception:
            self.logger.error(f"Error: {str(exception)}")
            raise ConnectionTestException(preset=ConnectionTestException.Preset.UNAUTHORIZED, data=exception)
