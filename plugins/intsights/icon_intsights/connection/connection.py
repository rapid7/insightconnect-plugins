import insightconnect_plugin_runtime
from typing import Optional
from .schema import ConnectionSchema, Input
# Custom imports below
from icon_intsights.util.api import IntSightAPI
from insightconnect_plugin_runtime.exceptions import PluginException, ConnectionTestException


class Connection(insightconnect_plugin_runtime.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.client: Optional[IntSightAPI] = None

    def connect(self, params={}):
        self.client = IntSightAPI(
            params.get(Input.ACCOUNT_ID, {}).get('secretKey'),
            params.get(Input.API_KEY, {}).get('secretKey')
        )
        self.logger.info("Connect: Connecting...")

    def test(self):
        try:
            return {"success": self.client.test_credentials()}
        except PluginException as e:
            raise ConnectionTestException(
                cause=e.cause,
                assistance=e.assistance
            )
