import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException

# Custom imports below
from ..util.api import MicrosoftDefenderClientAPI
from .schema import ConnectionSchema, Input


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        self.logger.info("Connect: Connecting...")
        self.client = MicrosoftDefenderClientAPI(
            params.get(Input.CLIENT_ID),
            params.get(Input.CLIENT_SECRET).get("secretKey"),
            params.get(Input.TENANT_ID),
            self.logger,
        )

    def test(self):
        try:
            self.client.test_connection()
            return {"success": True}
        except PluginException as error:
            raise ConnectionTestException(cause=error.cause, assistance=error.assistance, data=error.data)
