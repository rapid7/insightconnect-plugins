import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input

# Custom imports below
from icon_zscaler.util.zia_client import ZIAClient
from icon_zscaler.util.zpa_client import ZPAClient
from insightconnect_plugin_runtime.exceptions import PluginException, ConnectionTestException


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.zia_client = None
        self.zpa_client = None

    def connect(self, params={}):
        self.logger.info("Connect: Connecting...")

        client_id = params.get(Input.CLIENT_ID)
        private_key = params.get(Input.PRIVATE_KEY, {}).get("privateKey")
        vanity_domain = params.get(Input.VANITY_DOMAIN)
        cloud = params.get(Input.CLOUD) or "zsapi.net"

        self.zia_client = ZIAClient(client_id, private_key, vanity_domain, cloud, self.logger)
        self.zpa_client = ZPAClient(client_id, private_key, vanity_domain, cloud, self.logger)

    def test(self):
        try:
            self.zia_client.test()
        except PluginException as e:
            raise ConnectionTestException(cause=e.cause, assistance=e.assistance, data=e.data)

        try:
            self.zpa_client.test()
        except PluginException as e:
            raise ConnectionTestException(cause=e.cause, assistance=e.assistance, data=e.data)

        return {"success": True}
