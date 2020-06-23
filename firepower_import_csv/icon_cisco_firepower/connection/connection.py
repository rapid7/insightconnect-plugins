import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input
# Custom imports below


class Connection(insightconnect_plugin_runtime.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        self.logger.info("Connect: Connecting...")
        self.username = params.get(Input.USERNAME_PASSWORD).get("username")
        self.password = params.get(Input.USERNAME_PASSWORD).get("password")
        self.host = params.get(Input.SERVER)
        self.key = params.get(Input.KEY)

    def test(self):
        # TODO: Implement connection test
        pass
