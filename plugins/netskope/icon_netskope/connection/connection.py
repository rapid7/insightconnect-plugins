import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException

from icon_netskope.util.api import ApiClient
from .schema import ConnectionSchema, Input


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params={}):
        self.logger.info("Connect: Connecting...")
        self.client = ApiClient(
            params.get(Input.TENANT),
            params.get(Input.API_KEY_V1, {}).get("secretKey"),
            params.get(Input.API_KEY_V2, {}).get("secretKey"),
            self.logger,
        )

    def test(self):
        try:
            self.client.test_api()
            return {"success": True}
        except PluginException as error:
            raise ConnectionTestException(cause=error.cause, assistance=error.assistance, data=error.data)
