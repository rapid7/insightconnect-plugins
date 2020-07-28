from .schema import ConnectionSchema, Input
import insightconnect_plugin_runtime
# Custom imports below
from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException
import requests
from komand_microsoft_atp.util.api import WindwosDefenderATP_API


class Connection(insightconnect_plugin_runtime.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.session = requests.Session()
        self.resource_url = "https://api.securitycenter.windows.com"
        self.client = None

    def connect(self, params):
        self.logger.info("Connecting...")

        self.client = WindwosDefenderATP_API(
            params.get(Input.APPLICATION_ID),
            params.get(Input.APPLICATION_SECRET).get("secretKey"),
            params.get(Input.DIRECTORY_ID),
            self.logger
        )

    def test(self):
        try:
            self.client.get_all_alerts("?$top=1")
            return {"status": True}
        except PluginException as e:
            raise ConnectionTestException(
                cause=e.cause,
                assistance=e.assistance,
                data=e.data
            )
