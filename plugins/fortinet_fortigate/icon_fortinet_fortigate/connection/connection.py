import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input

# Custom imports below
from icon_fortinet_fortigate.util.api import FortigateAPI
from insightconnect_plugin_runtime.exceptions import PluginException, ConnectionTestException


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.host = None
        self.api_key = None
        self.ssl_verify = None
        self.api = None

    def connect(self, params):
        self.host = params.get(Input.HOSTNAME)
        self.api_key = params.get(Input.API_KEY).get("secretKey")
        self.ssl_verify = params.get(Input.SSL_VERIFY)

        # Strip http:// or https://
        if self.host.startswith("http://"):
            self.host = self.host[7:]
        if self.host.startswith("https://"):
            self.host = self.host[8:]
        # Strip out any URL character after /
        self.host = self.host.split("/", 1)[0]

        self.api = FortigateAPI(self.host, self.api_key, self.logger, self.ssl_verify)

    def test(self):
        try:
            self.api.get_policies({})
        except PluginException:
            raise ConnectionTestException(
                cause="Connection Test Failed.",
                assistance="Verify that your API key and hostname are correct, and ensure the hostname is a trusted host in Fortigate.",
            )
        return {"status": "Success"}
