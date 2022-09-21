import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input

# Custom imports below
from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException
from icon_jamf.util.api import ApiClient


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())

    def connect(self, params):
        self.logger.info("Connect: Connecting...")
        base_url = params.get(Input.URL, "")
        username = params.get(Input.CLIENT_LOGIN, {}).get("username", "")
        password = params.get(Input.CLIENT_LOGIN, {}).get("password", "")
        self.client = ApiClient(base_url, username, password, self.logger)

    def test(self):
        try:
            self.client.test_connection()
        except PluginException as error:
            raise ConnectionTestException(cause=error.cause, assistance=error.assistance, data=error.data)
        return {"connection": "successful"}
