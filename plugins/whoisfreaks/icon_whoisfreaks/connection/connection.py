import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException

from .schema import ConnectionSchema, Input

# Custom imports below
from icon_whoisfreaks.util import constants
from icon_whoisfreaks.util.client import WhoisFreaksClient
from icon_whoisfreaks.util.errors import Kind, WhoisFreaksError

# The key is valid in these cases; the account only lacks lookup credits or a product
_VALID_KEY_KINDS = {Kind.NO_CREDITS, Kind.NOT_ENTITLED, Kind.PLAN_LIMIT}


def _secret(value) -> str:
    if isinstance(value, dict):
        value = value.get("secretKey")
    return str(value or "").strip()


class Connection(insightconnect_plugin_runtime.Connection):

    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.client = None

    def connect(self, params={}):
        self.logger.info("Connect: Connecting...")
        api_key = _secret(params.get(Input.API_KEY))
        if not api_key:
            raise PluginException(
                cause="The WhoisFreaks API key is empty",
                assistance="Enter the API key from the WhoisFreaks dashboard in the plugin connection",
            )
        self.client = WhoisFreaksClient(api_key, self.logger)

    def test(self):
        try:
            result = self.client.lookup("Connection test", "GET", constants.PATH_ACCOUNT_USAGE)
        except WhoisFreaksError as error:
            if error.kind in _VALID_KEY_KINDS:
                self.logger.warning("The API key is valid, but: %s. %s", error.cause, error.assistance)
                return {"success": True}
            raise ConnectionTestException(cause=error.cause, assistance=error.assistance, data=error.data)
        if not result.found:
            raise ConnectionTestException(
                cause=f"Connection test: WhoisFreaks does not recognise the API key. WhoisFreaks said: {result.message}",
                assistance="Verify the API key in the plugin connection",
                data=f"HTTP {result.status_code}",
            )
        return {"success": True}
