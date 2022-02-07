import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input

# Custom imports below
from typing import Optional
from icon_rapid7_intsights.util.api import IntSightsAPI
from insightconnect_plugin_runtime.exceptions import PluginException, ConnectionTestException


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.client: Optional[IntSightsAPI] = None

    def connect(self, params={}):
        self.client = IntSightsAPI(
            params.get(Input.ACCOUNT_ID),
            params.get(Input.API_KEY, {}).get("secretKey"),
            self.logger,
        )
        self.logger.info("Connect: Connecting...")

    def test(self):
        try:
            return {"success": self.client.test_credentials()}
        except PluginException as e:
            raise ConnectionTestException(cause=e.cause, assistance=e.assistance)
