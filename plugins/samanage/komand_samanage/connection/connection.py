import insightconnect_plugin_runtime
from .schema import ConnectionSchema

# Custom imports below
from insightconnect_plugin_runtime.exceptions import ConnectionTestException
from komand_samanage.util.api import SamanageAPI


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        token = params.get("token")["secretKey"]
        is_eu_customer = params.get("eu_customer")
        ssl_verify = params.get("ssl_verify")

        if not token:
            raise ConnectionTestException(
                cause="Missing API key from Connection. This is a required field.",
                assistance="The API authentication token can be obtained from your Solarwinds account.",
            )

        self.logger.info("Connect: Connecting...")
        self.api = SamanageAPI(token, is_eu_customer, ssl_verify, self.logger)

        self.logger.info("Connect: Connection successful")

    def test(self):
        try:
            self.api.list_incidents_check()
            return {"success": True}
        except Exception as error:
            raise ConnectionTestException(cause=error.cause, assistance=error.assistance, data=error.data)
