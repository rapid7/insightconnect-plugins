import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException, ConnectionTestException

from .schema import ConnectionSchema, Input

# Custom imports below
from icon_connectwise.util.api import ConnectWiseAPI


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.api_client = None

    def connect(self, params: dict = None):
        self.logger.info("Connect: Connecting...")
        self.api_client = ConnectWiseAPI(
            public_key=params.get(Input.PUBLIC_KEY),
            private_key=params.get(Input.PRIVATE_KEY).get("secretKey"),
            company=params.get(Input.COMPANY),
            client_id=params.get(Input.CLIENT_ID).get("secretKey"),
            region=params.get(Input.REGION),
            logger=self.logger,
        )

    def test(self):
        try:
            self.api_client.get_tickets()
        except PluginException:
            raise ConnectionTestException(
                cause="Connection error.",
                assistance="Please make sure that your API key and Sdp Base URL are correct",
            )
        return {"status": "Success"}
