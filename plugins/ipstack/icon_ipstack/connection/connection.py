import insightconnect_plugin_runtime
from .schema import ConnectionSchema
from insightconnect_plugin_runtime.exceptions import ConnectionTestException

# Custom imports below


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.token = None

    def connect(self, params):
        self.token = params["cred_token"]["secretKey"]

    def test(self):
        # TODO - Implement connection test
        return {"success": True}
