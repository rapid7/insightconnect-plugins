import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException, ConnectionTestException
from .schema import ConnectionSchema

# Custom imports below
from ..util.api import VMRay


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.api = None

    def connect(self, params):
        _api_key = params.get("api_key").get("secretKey")
        self.logger.info("Connect: Connecting...")
        self.api = VMRay(url=params.get("url"), api_key=_api_key, logger=self.logger)

    def test(self):
        try:
            self.api.call_api("GET", "/rest/system_info")
        except PluginException as exception:
            raise ConnectionTestException(cause=exception.cause, assistance=exception.assistance, data=exception.data)
        return {"success": True}
