import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException
from .schema import ConnectionSchema

# Custom imports below
from komand_redhat_advisory.util.api import RedHatSecurityDataAPI


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super().__init__(input=ConnectionSchema())
        self.client = None

    def connect(self, params: dict = {}) -> None:
        self.client = RedHatSecurityDataAPI()

    def test(self) -> dict:
        try:
            self.client.test_connection()
            return {"success": True}
        except PluginException as error:
            raise ConnectionTestException(cause=error.cause, assistance=error.assistance, data=error.data)
