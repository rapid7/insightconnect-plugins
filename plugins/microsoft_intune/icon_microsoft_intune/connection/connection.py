import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
from insightconnect_plugin_runtime.exceptions import ConnectionTestException
from icon_microsoft_intune.util.api import MicrosoftIntuneAPI


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.api = None

    def connect(self, params={}):
        self.logger.info("Connect: Connecting...")
        url = "https://graph.microsoft.com"
        self.api = MicrosoftIntuneAPI(
            username=params.get(Input.CREDENTIALS, {}).get("username"),
            password=params.get(Input.CREDENTIALS, {}).get("password"),
            client_id=params.get(Input.CLIENTID),
            client_secret=params.get(Input.CLIENTSECRET, {}).get("secretKey"),
            tenant_id=params.get(Input.TENANTID),
            api_url=f"{url}/v1.0/",
            logger=self.logger,
        )

        self.api.refresh_access_token()

    def test(self):
        self.logger.info("Starting the connection test.")
        try:
            self.api.search_managed_devices("nonexistinguser@example.com")
            self.logger.info("The connection test completed successfully.")
            return {"success": True}
        except PluginException as error:
            raise ConnectionTestException(cause=error.cause, assistance=error.assistance, data=error.data)
