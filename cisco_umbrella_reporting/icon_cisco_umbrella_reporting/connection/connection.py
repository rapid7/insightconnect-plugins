import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input
from icon_cisco_umbrella_reporting.util.api import CiscoUmbrellaReportingAPI
from insightconnect_plugin_runtime.exceptions import PluginException, ConnectionTestException


class Connection(insightconnect_plugin_runtime.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.client = None

    def connect(self, params):
        self.logger.info("Connect: Connecting...")
        self.client = CiscoUmbrellaReportingAPI(
            params.get(Input.API_KEY).get("secretKey"),
            params.get(Input.API_SECRET).get("secretKey"),
            params.get(Input.ORGANIZATION_ID),
            self.logger
        )

    def test(self):
        try:
            self.client.security_activity_report()
            return {
                "success": True
            }
        except PluginException as e:
            raise ConnectionTestException(
                cause=e.cause,
                assistance=e.assistance,
                data=e.data
            )
