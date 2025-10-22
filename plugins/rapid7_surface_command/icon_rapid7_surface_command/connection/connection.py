import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input

# Custom imports below

from icon_rapid7_surface_command.util.api_connection import (
    ApiConnection,
)
from insightconnect_plugin_runtime.exceptions import (
    ConnectionTestException,
    PluginException,
)


class Connection(insightconnect_plugin_runtime.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params=None):
        self.logger.info("Connect: Connecting...")
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        self.api_key = params.get(Input.API_KEY)
        self.region = params.get(Input.REGION)
        # END INPUT BINDING - DO NOT REMOVE

        self.api = ApiConnection(self.api_key.get("secretKey"), self.region, self.logger)
        self.logger.info("Setup Complete")
        return self

    def test(self):
        if not self.api_key or not self.region:
            raise ConnectionTestException("API Key and Region are required to test the connection.")
        try:
            # This is a usually fast query we can use to test.
            self.api.run_query("rapid7.insightplatform.admin_user_mfa_false_count")
        except PluginException as e:
            raise ConnectionTestException(f"Connection test failed: {e}")

        return {"success": True}
