import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException

from .schema import ConnectionSchema, Input

# Custom imports below
from icon_ipgeolocation_io.util.api import IPGeolocationAPI


class Connection(insightconnect_plugin_runtime.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.api_key = None
        self.api = None

    def connect(self, params):
        self.logger.info("Connect: Connecting...")
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        self.api_key = params.get(Input.API_KEY)
        # END INPUT BINDING - DO NOT REMOVE

        secret_key = (self.api_key or {}).get("secretKey", "")
        secret_key = secret_key.strip() if isinstance(secret_key, str) else ""

        if not secret_key:
            raise PluginException(
                cause="No IPGeolocation.io API key was provided.",
                assistance="Add the API key from https://app.ipgeolocation.io to the connection and try again.",
            )

        self.api = IPGeolocationAPI(api_key=secret_key, logger=self.logger)
        self.logger.info("Connect: Connected")

    def test(self):
        """
        Verify the API key by geolocating the orchestrator's own public IP.

        /v3/ipgeo is the only endpoint every subscription tier can reach, so a
        failure here means the key itself is bad rather than the plan lacking a
        particular module. The call costs one credit.
        """

        try:
            self.api.test_connection()
        except PluginException as error:
            raise ConnectionTestException(
                cause=error.cause,
                assistance=error.assistance,
                data=error.data,
            )

        return {"success": True}
