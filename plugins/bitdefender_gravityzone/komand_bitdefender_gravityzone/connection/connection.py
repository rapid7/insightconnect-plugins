import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input
from insightconnect_plugin_runtime.exceptions import ConnectionTestException

# Custom imports below
from komand_bitdefender_gravityzone.util.api import BitdefenderGravityZoneAPI


class Connection(insightconnect_plugin_runtime.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.api = None

    def connect(self, params):
        self.logger.info("Connect: Connecting...")
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        api_key = params.get(Input.API_KEY)
        url = params.get(Input.URL)
        # END INPUT BINDING - DO NOT REMOVE

        self.api = BitdefenderGravityZoneAPI(
            base_url=url.strip(),
            api_key=api_key.get("secretKey", "").strip(),
            logger=self.logger,
        )

    def test(self):
        try:
            self.api.test_connection()
        except Exception as error:
            raise ConnectionTestException(
                cause="Connection test failed.",
                assistance="Please verify that your API key is valid and the Access URL is correct.",
                data=str(error),
            )
        return {"success": True}
