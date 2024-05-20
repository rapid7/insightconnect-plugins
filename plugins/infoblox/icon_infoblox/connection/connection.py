import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input

# Custom imports below
from icon_infoblox.util.infoblox import InfobloxConnection


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.infoblox_connection = None

    def connect(self, params):
        self.logger.info("Connect: Connecting...")

        url = params.get(Input.URL)
        api_version = params.get(Input.API_VERSION)
        username = params.get(Input.CREDENTIALS).get("username")
        password = params.get(Input.CREDENTIALS).get("password")
        ssl_verify = params.get(Input.SSL_VERIFY)

        self.infoblox_connection = InfobloxConnection(url, api_version, username, password, ssl_verify, self.logger)

        self.logger.info("Connect: Infoblox connection established successfully")

    def test(self):
        return {"success": True}
