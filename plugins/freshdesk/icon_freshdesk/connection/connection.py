import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException, ConnectionTestException

from .schema import ConnectionSchema, Input

# Custom imports below
from icon_freshdesk.util.api import FreshDeskAPI


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.api_client = None

    def connect(self, params: dict = None):
        self.logger.info("Connect: Connecting...")
        self.api_client = FreshDeskAPI(
            api_key=params.get(Input.APIKEY).get("secretKey"),
            domain=params.get(Input.DOMAINNAME),
            logger=self.logger,
        )

    def test(self):
        try:
            self.api_client.get_ticket_fields()
        except PluginException:
            raise ConnectionTestException(
                cause="Connection error.",
                assistance="Please make sure that your API Key and domain name are correct",
            )
        return {"status": "Success"}
