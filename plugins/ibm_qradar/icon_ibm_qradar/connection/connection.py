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
        credentials = params.get(Input.CREDENTIALS)
        self.username = credentials.get("username")
        self.password = credentials.get("password")
        self.host_url = params.get(Input.HOST_URL)
        self.verify_ssl = params.get(Input.VERIFY_SSL, False)

    def test(self, params):
        """To test the connection."""
        credentials = params.get(Input.CREDENTIALS, {"username": "user1", "password": "password"})
        self.username = credentials.get("username")
        self.password = credentials.get("password")
        self.host_url = params.get(Input.HOST_URL, "https://hostname.com")
        self.verify_ssl = params.get(Input.VERIFY_SSL, False)

        return {"connection": "successful"}
