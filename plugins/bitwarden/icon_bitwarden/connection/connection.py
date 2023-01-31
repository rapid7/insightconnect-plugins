import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input

# Custom imports below
from icon_bitwarden.util.api import BitwardenAPI


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.api_client = None

    def connect(self, params: dict = None):
        self.logger.info("Connect: Connecting...")
        self.api_client = BitwardenAPI(
            client_id=params.get(Input.CLIENTID),
            client_secret=params.get(Input.CLIENTSECRET).get("secretKey"),
            logger=self.logger,
        )

    def test(self):
        try:
            self.api_client.get_headers()
            return {"success": True}
        except PluginException as error:
            raise ConnectionTestException(cause=error.cause, assistance=error.assistance, data=error.data)
