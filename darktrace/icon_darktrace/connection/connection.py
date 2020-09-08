import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input
# Custom imports below
from icon_darktrace.util.api import DarkTraceAPI
from insightconnect_plugin_runtime.exceptions import PluginException, ConnectionTestException


class Connection(insightconnect_plugin_runtime.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.client = None

    def connect(self, params={}):
        self.logger.info("Connect: Connecting...")
        self.client = DarkTraceAPI(
            params.get(Input.URL),
            params.get(Input.API_PUBLIC_TOKEN).get("secretKey"),
            params.get(Input.API_PRIVATE_TOKEN).get("secretKey"),
            self.logger
        )

    def test(self):
        try:
            return {
                "success": self.client.get_status() != {}
            }
        except PluginException as e:
            raise ConnectionTestException(cause=e.cause, assistance=e.assistance, data=e.data)
