import insightconnect_plugin_runtime

from .schema import ConnectionSchema, Input
from insightconnect_plugin_runtime.exceptions import PluginException, ConnectionTestException

# Custom imports below
from ..util.api import CiscoUmbrellaEnforcementAPI


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.client = None

    def connect(self, params={}):
        self.logger.info("Connect: Connecting..")

        key = params.get(Input.API_KEY).get("secretKey")
        ssl_verify = params.get(Input.SSL_VERIFY)

        self.client = CiscoUmbrellaEnforcementAPI(key, ssl_verify)

    def test(self):
        try:
            self.client.get_domains()
            return {"success": True}
        except PluginException as error:
            raise ConnectionTestException(cause=error.cause, assistance=error.assistance, data=error.data)
