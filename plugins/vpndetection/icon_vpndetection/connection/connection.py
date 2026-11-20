import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException

from icon_vpndetection.util.api import VPNDetectionAPI

from .schema import ConnectionSchema, Input

# Cloudflare's resolver: an address that is always answered, so a failure is the key's or the network's.
TEST_ADDRESS = "1.1.1.1"


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.client = None

    def connect(self, params):
        self.logger.info("Connect: Connecting...")
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        self.api_key = params.get(Input.API_KEY, {})
        # END INPUT BINDING - DO NOT REMOVE
        self.client = VPNDetectionAPI((self.api_key or {}).get("secretKey", ""), self.logger)

    def test(self):
        try:
            self.client.lookup(TEST_ADDRESS)
            return {"success": True}
        except PluginException as error:
            raise ConnectionTestException(cause=error.cause, assistance=error.assistance, data=error.data)
