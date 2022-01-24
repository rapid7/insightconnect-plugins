import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super().__init__(input=ConnectionSchema())
        self.username = ""
        self.password = ""
        self.host_url = ""
        self.verify_ssl = False

    def connect(self, params={}):
        """TO read the connection configuration.

        :param params: Config Params required for connection
        :return: None
        """
        self.username = params.get(Input.USERNAME)
        self.password = params.get(Input.PASSWORD)
        self.host_url = params.get(Input.HOST_URL)
        self.verify_ssl = params.get(Input.VERIFY_SSL, False)

    def test(self, params):
        """TO test the connection."""
        self.username = params.get(Input.USERNAME)
        self.password = params.get(Input.PASSWORD)
        self.host_url = params.get(Input.HOST_URL)
        self.verify_ssl = params.get(Input.VERIFY_SSL, False)

        return {"connection": "successful"}
