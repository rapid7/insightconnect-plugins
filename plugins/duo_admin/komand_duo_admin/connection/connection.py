import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input
from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException

# Custom imports below
from komand_duo_admin.util.api import DuoAdminAPI


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.admin_api = None

    def connect(self, params={}):
        self.logger.info("Connect: Connecting...")
        self.admin_api = DuoAdminAPI(
            hostname=params.get(Input.HOSTNAME),
            integration_key=params.get(Input.INTEGRATIONKEY).get("secretKey"),
            secret_key=params.get(Input.SECRETKEY).get("secretKey"),
            logger=self.logger,
        )

    def test(self):
        try:
            self.admin_api.get_users()
            return {"success": True}
        except PluginException as error:
            raise ConnectionTestException(cause=error.cause, assistance=error.assistance, data=error.data)
