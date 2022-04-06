import insightconnect_plugin_runtime
from icon_azure_sentinel.util.api import AzureSentinelClient
from insightconnect_plugin_runtime.exceptions import ConnectionTestException
from .schema import ConnectionSchema, Input


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.auth_token = ""  # nosec
        self.api_client = None
        self.logger = None

    def connect(self, params):
        tenant_id = params.get(Input.TENANT_ID)
        client_id = params.get(Input.CLIENT_ID)
        client_secret = params.get(Input.CLIENT_SECRET).get("secretKey")
        self.api_client = AzureSentinelClient(self.logger, tenant_id, client_id, client_secret)

    def test(self):
        if not isinstance(self.api_client, AzureSentinelClient):
            raise ConnectionTestException(
                cause="AzureSentinelClient not initialized",
                assistance="Please initialize the client " "with correct data",
            )
        if not self.api_client.auth_token:
            raise ConnectionTestException(
                cause="Unable to authorize against Microsoft graph API.",
                assistance="The plugin connection configured may not be authorized to connect "
                "Please check your connection information, and contact "
                "your Azure administrator if you need more assistance.",
            )
