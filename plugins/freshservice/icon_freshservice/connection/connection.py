import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input

# Custom imports below
from icon_freshservice.util.api import FreshServiceAPI
from insightconnect_plugin_runtime.exceptions import PluginException, ConnectionTestException


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.api = None

    def connect(self, params={}):
        self.logger.info("Connect: Connecting...")
        base_url = f"https://{params.get(Input.SUBDOMAIN)}.freshservice.com"
        self.api = FreshServiceAPI(base_url, params.get(Input.APIKEY, {}).get("secretKey"), self.logger)

    def test(self):
        try:
            self.api.list_sla_policies()
            return {"success": True}
        except PluginException as error:
            raise ConnectionTestException(cause=error.cause, assistance=error.assistance, data=error.data)
