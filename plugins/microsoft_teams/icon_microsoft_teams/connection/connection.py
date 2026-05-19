import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input

# Custom imports below
from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException

from icon_microsoft_teams.util.constants import RESOURCE_URL
from icon_microsoft_teams.util.graph_api_client import GraphApiClient
from icon_microsoft_teams.util.bot_service import BotService


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super().__init__(input=ConnectionSchema())
        self.client = None
        self.bot = None
        self.resource_endpoint = None

    def connect(self, params):  # pylint: disable=signature-differs
        app_id = params.get(Input.APPLICATION_ID, "").strip()
        tenant_id = params.get(Input.DIRECTORY_ID, "").strip()
        endpoint = params.get(Input.ENDPOINT, "Normal")
        app_secret = params.get(Input.APPLICATION_SECRET, {}).get("secretKey", "").strip()

        self.resource_endpoint = RESOURCE_URL.get(endpoint)

        # Initialize the Graph API client (handles its own authentication)
        self.client = GraphApiClient(
            app_id=app_id,
            app_secret=app_secret,
            tenant_id=tenant_id,
            base_url=self.resource_endpoint,
            endpoint=endpoint,
            logger=self.logger,
        )

        # Initialize the Bot Framework service (handles its own authentication)
        self.bot = BotService(
            app_id=app_id,
            app_secret=app_secret,
            tenant_id=tenant_id,
            endpoint=endpoint,
            logger=self.logger,
        )

    def get_headers(self, force_refresh=False) -> dict:
        """Get Graph API authorization headers (delegates to client)."""
        return self.client.get_auth_headers(force_refresh)

    def test(self):
        try:
            self.client.authenticate()
        except PluginException as error:
            raise ConnectionTestException(
                cause="Unable to get authentication token.",
                assistance="Please verify your Application ID, Directory ID, and Application Secret. "
                "Ensure the app registration has Microsoft Graph application permissions with admin consent.",
            ) from error

        # Verify we can actually call the Graph API
        try:
            self.client._make_request("GET", "/v1.0/organization")  # pylint: disable=protected-access
        except PluginException as error:
            raise ConnectionTestException(
                cause="Authentication succeeded but API call failed.",
                assistance="The token was obtained but could not access Microsoft Graph. "
                "Verify the app has Organization.Read.All or similar permissions.",
            ) from error

        return {"success": True}
