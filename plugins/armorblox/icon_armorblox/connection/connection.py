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
        self.logger.info(params)
        self.api = ArmorbloxAPI(
            api_key = params.get('api_key').get('secretKey'),
            tenant_name = params.get('tenant_name'),
            logger=self.logger,
        )

    def test(self):

        try:
            result = self.api.test_api()
        except PluginException:
            raise ConnectionTestException(
                cause="Connection Test Failed.", assistance="Please check that your API key is correct."
            )
        return result
