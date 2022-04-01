import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input
from ..util.api import ManageEngineAPI

# Custom imports below


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.client = None

    def connect(self, params):
        self.logger.info("Connect: Connecting...")
        apiKey = params.get(Input.API_KEY).get("secretKey")

        self.client = ManageEngineAPI(api_key=apiKey)

    def test(self):
        # TODO: Implement connection test
        pass
