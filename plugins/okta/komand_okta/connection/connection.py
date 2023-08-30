import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input
from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException

# Custom imports below
from komand_okta.util.api import OktaAPI


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.api_client = None

    def connect(self, params={}):
        self.logger.info("Connect: Connecting...")
        self.api_client = OktaAPI(
            params.get(Input.OKTAKEY).get("secretKey"), params.get(Input.OKTAURL), logger=self.logger
        )

    def test(self):
        try:
            self.api_client.list_groups()
            return {"success": True}
        except PluginException as error:
            raise ConnectionTestException(cause=error.cause, assistance=error.assistance, data=error.data)
