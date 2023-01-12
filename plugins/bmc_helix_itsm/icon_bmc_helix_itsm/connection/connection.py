import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException

from icon_bmc_helix_itsm.util.api import BmcHelixItsmApi
from .schema import ConnectionSchema, Input

# Custom imports below


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.api_client = None

    def connect(self, params: dict = None):
        self.logger.info("Connect: Connecting...")

        self.api_client = BmcHelixItsmApi(
            username_password=params.get(Input.USERNAMEPASSWORD),
            base_url=params.get(Input.BASEURL).strip("/"),
            ssl_verify=params.get(Input.SSLVERIFY),
            logger=self.logger,
        )

    def test(self):
        try:
            self.api_client.get_headers()
            return {"success": True}
        except PluginException as error:
            raise ConnectionTestException(cause=error.cause, assistance=error.assistance, data=error.data)
