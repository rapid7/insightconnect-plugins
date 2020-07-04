import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input
# Custom imports below
from komand_mcafee_epo.util.mcafee import Client
from insightconnect_plugin_runtime.exceptions import ConnectionTestException


class Connection(insightconnect_plugin_runtime.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.client = None

    def connect(self, params=None):
        if params is None:
            params = {}

        url = params.get(Input.URL, "").rstrip("/")
        port = params.get(Input.PORT)

        try:
            self.logger.info("Connect: Connecting..")
            self.client = Client(
                f"{url}:{port}",
                params.get(Input.CREDENTIALS).get('username'),
                params.get(Input.CREDENTIALS).get('password'),
                verify=False
            )
            if self.client is not None:
                self.logger.info("Connected")
        except Exception:
            self.logger.error("Error connecting to Mcafee EPO")
            raise ConnectionTestException(
                cause="Connection error",
                assistance="Error connecting to McAfee EPO"
            )

    def test(self):
        try:
            mc = self.client
            if mc.epo.getVersion():
                return {"success": True}
        except Exception:
            self.logger.error("An unexpected error occurred during the API request")
            raise ConnectionTestException(
                cause="Connection error",
                assistance="An unexpected error occurred during the API request"
            )
