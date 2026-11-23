import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException

from .schema import ConnectionSchema, Input

# Custom imports below
from icon_bitdefender_gravityzone.util.api import BitdefenderGravityZoneAPI


class Connection(insightconnect_plugin_runtime.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.api = None

    def connect(self, params={}):
        self.logger.info("Connect: Connecting...")
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        self.api_key = params.get(Input.API_KEY)
        self.url = params.get(Input.URL)
        # END INPUT BINDING - DO NOT REMOVE

        self.api = BitdefenderGravityZoneAPI(
            url=self.url or "",
            api_key=(self.api_key or {}).get("secretKey", ""),
            logger=self.logger,
        )

    def test(self):
        try:
            self.api.test_connection()
        except PluginException as error:
            raise ConnectionTestException(cause=error.cause, assistance=error.assistance, data=error.data) from error
        return {"success": True}
