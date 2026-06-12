import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException, ConnectionTestException

from ..util.api import SentinelOneAPI


class Connection(insightconnect_plugin_runtime.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        self.logger.info("Connect: Connecting...")
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        self.api_key = params.get(Input.API_KEY)
        self.instance = params.get(Input.INSTANCE)
        # END INPUT BINDING - DO NOT REMOVE

        api_key = self.api_key.get("secretKey", "").strip()
        instance = self.instance.strip()
        base_url = f"https://{instance}.sentinelone.net"

        self.client = SentinelOneAPI(base_url, api_key, self.logger)

    def test(self):
        try:
            self.client.test_connection()
            return {"success": True}
        except PluginException as error:
            raise ConnectionTestException(cause=error.cause, assistance=error.assistance, data=error.data)
