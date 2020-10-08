import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input
# Custom imports below
from icon_zscaler.util.api import ZscalerAPI
from insightconnect_plugin_runtime.exceptions import PluginException, ConnectionTestException


class Connection(insightconnect_plugin_runtime.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.client = None

    def connect(self, params={}):
        self.logger.info("Connect: Connecting...")
        self.client = ZscalerAPI(
            params.get(Input.URL),
            params.get(Input.API_KEY).get("secretKey"),
            params.get(Input.CREDENTIALS).get("username"),
            params.get(Input.CREDENTIALS).get("password"),
            self.logger
        )

    def test(self):
        try:
            return {
                "success": self.client.get_status() != {}
            }
        except PluginException as e:
            raise ConnectionTestException(cause=e.cause, assistance=e.assistance, data=e.data)
