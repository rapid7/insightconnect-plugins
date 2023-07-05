import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input
from insightconnect_plugin_runtime.exceptions import PluginException, ConnectionTestException

# Custom imports below
from icon_armorblox.util.api import ArmorbloxAPI


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.api = None

    def connect(self, params):
        self.logger.info("Connect: Connecting...")
        api_key = params.get(Input.API_KEY, {}).get("secretKey")
        tenant_name = params.get(Input.TENANT_NAME)
        self.api = ArmorbloxAPI(api_key=api_key, tenant_name=tenant_name, logger=self.logger)

    def test(self):
        try:
            self.api.test_api()
            return {"success": True}
        except PluginException as error:
            raise ConnectionTestException(cause=error.cause, assistance=error.assistance, data=error.data)
