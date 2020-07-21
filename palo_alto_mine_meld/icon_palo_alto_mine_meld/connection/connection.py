import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input
# Custom imports below
from insightconnect_plugin_runtime.exceptions import ConnectionTestException
from icon_palo_alto_mine_meld.util.api import PaloAltoMineMeldAPI


class Connection(insightconnect_plugin_runtime.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.client = None

    def connect(self, params=None):
        if params is None:
            params = {}

        url = params.get(Input.URL, "").rstrip("/")
        port = params.get(Input.PORT, 443)
        ssl_verify = params.get(Input.SSL_VERIFY, None)

        try:
            self.logger.info("Connect: Connecting..")
            self.client = PaloAltoMineMeldAPI(
                f"{url}:{port}",
                params.get(Input.CREDENTIALS).get('username'),
                params.get(Input.CREDENTIALS).get('password'),
                ssl_verify,
                self.logger
            )
            self.logger.info("Connected")
        except Exception:
            self.logger.error("Error connecting to Palo Alto MineMeld")
            raise ConnectionTestException(
                cause="Error connecting to Palo Alto MineMeld.",
                assistance="Please check your connection credentials and that the orchestrator has network access to the MindMeld server."
            )

    def test(self):
        try:
            if self.client.health_check():
                return {"success": True}
            else:
                raise ConnectionTestException(
                    cause="Connection error.",
                    assistance="An unexpected error occurred during the API request"
                )
        except Exception:
            self.logger.error("An unexpected error occurred during the API request")
            raise ConnectionTestException(
                cause="Connection error.",
                assistance="An unexpected error occurred during the API request"
            )
