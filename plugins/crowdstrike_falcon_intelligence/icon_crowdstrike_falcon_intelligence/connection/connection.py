import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException

from icon_crowdstrike_falcon_intelligence.util.api import CrowdStrikeAPI
from .schema import ConnectionSchema, Input

# Custom imports below


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.api_client = None

    def connect(self, params: dict = None):
        self.logger.info("Connect: Connecting...")

        self.api_client = CrowdStrikeAPI(
            client_id=params.get(Input.CLIENTID),
            client_secret=params.get(Input.CLIENTSECRET).get("secretKey"),
            base_url=params.get(Input.BASEURL).strip("/"),
            logger=self.logger,
        )

    def test(self):
        try:
            self.api_client.get_reports_ids()
            return {"success": True}
        except PluginException as error:
            raise ConnectionTestException(cause=error.cause, assistance=error.assistance, data=error.data)
