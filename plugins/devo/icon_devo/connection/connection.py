import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input

# Custom imports below
from icon_devo.util.api import DevoAPI


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        self.logger.info("Connect: Connecting...")
        self.api = DevoAPI(
            self.logger, params.get(Input.AUTHENTICATION_TOKEN).get("secretKey"), params.get(Input.REGION)
        )

    def test(self):
        self.api.test_connection()
        return {"result":"pass"}
