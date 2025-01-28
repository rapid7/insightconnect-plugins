import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException, ConnectionTestException
from .schema import ConnectionSchema, Input
from icon_mimecast_v2.util.api import API
# Custom imports below


class Connection(insightconnect_plugin_runtime.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        self.logger.info("Connect: Connecting...")
        self.client_secret = params.get(Input.CLIENT_SECRET).get("secretKey")
        self.client_id = params.get(Input.CLIENT_ID).get("secretKey")
        self.api = API(client_id=self.client_id, client_secret=self.client_secret, logger=self.logger)
        self.api.authenticate()



    def test(self):
        try:
            self.api.health_check()
            return {"success": True}
        except PluginException as error:
            raise ConnectionTestException(cause=error.cause, assistance=error.assistance, data=error.data)
