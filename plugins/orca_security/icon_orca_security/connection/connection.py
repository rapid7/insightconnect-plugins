import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input

# Custom imports below
from icon_orca_security.util.api import OrcaSecurityAPI
from insightconnect_plugin_runtime.exceptions import PluginException, ConnectionTestException


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.api = None

    def connect(self, params={}):
        self.logger.info("Connect: Connecting...")
        base_url = f"https://app.{params.get(Input.REGION).lower()}.orcasecurity.io"
        self.api = OrcaSecurityAPI(base_url, params.get(Input.API_TOKEN).get("secretKey"), self.logger)

    def test(self):
        try:
            self.api.get_alerts_scheme()
            return {"success": True}
        except PluginException as error:
            raise ConnectionTestException(cause=error.cause, assistance=error.assistance, data=error.data)
