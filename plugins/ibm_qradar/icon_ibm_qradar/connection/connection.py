import insightconnect_plugin_runtime

from .schema import ConnectionSchema, Input


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super().__init__(input=ConnectionSchema())
        self.username = ""
        self.password = ""
        self.hostname = ""

    def connect(self, params={}):
        """TO read the connection configuration.

        :param params: Config Params required for connection
        :return: None
        """
        self.username = params.get(Input.USERNAME)
        self.password = params.get(Input.PASSWORD)
        self.hostname = params.get(Input.HOSTNAME)

    def test(self, params):
        """TO test the connection."""
        self.username = params.get(Input.USERNAME)
        self.password = params.get(Input.PASSWORD)
        self.hostname = params.get(Input.HOSTNAME)

        return {"connection": "successful"}
