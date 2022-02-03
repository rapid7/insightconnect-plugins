import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input

# Custom imports below
from insightconnect_plugin_runtime.exceptions import ConnectionTestException
from icon_automox.util.api_client import ApiClient


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.automox_api = None
        self.api_key = None

    def connect(self, params):
        self.logger.info("Connect: Creating Client to Automox")
        self.api_key = params.get(Input.API_KEY).get("secretKey")
        self.automox_api = ApiClient(self.logger, self.api_key)

    def test(self):
        try:
            self.automox_api.get_orgs()
        except Exception as e:
            raise ConnectionTestException(cause=e.cause, assistance=e.assistance, data=e)

        return {}
