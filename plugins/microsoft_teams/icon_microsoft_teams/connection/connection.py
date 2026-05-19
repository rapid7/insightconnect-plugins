import insightconnect_plugin_runtime
from .schema import ConnectionSchema, Input

# Custom imports below
from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException
import requests
import time

from icon_microsoft_teams.util.constants import TIMEOUT, RESOURCE_URL, AUTH_URL, GRAPH_SCOPE_DEFAULT
from icon_microsoft_teams.util.graph_api_client import GraphApiClient
from icon_microsoft_teams.util.bot_service import BotService


class Connection(insightconnect_plugin_runtime.Connection):
    def __init__(self):
        super(self.__class__, self).__init__(input=ConnectionSchema())
        self.client = None
        self.bot = None
        self.app_id = None
        self.tenant_id = None
        self.app_secret = None
        self.api_token = None
        self.resource_endpoint = None

    def connect(self, params):
        self.app_id = params.get(Input.APPLICATION_ID, "").strip()
        self.tenant_id = params.get(Input.DIRECTORY_ID, "").strip()
        self.endpoint = params.get(Input.ENDPOINT, "Normal")
        self.app_secret = params.get(Input.APPLICATION_SECRET, {}).get("secretKey", "").strip()

        self.resource_endpoint = RESOURCE_URL.get(self.endpoint)

        # Auth tokens expire after 1 hour. Track when we last authenticated.
        self.time_ago = 0
        self.time_now = time.time()

        # Authenticate using client_credentials (app-only)
        self._get_app_token()

        # Initialize the Graph API client
        self.client = GraphApiClient(
            base_url=self.resource_endpoint,
            logger=self.logger,
            get_headers_func=self.get_headers,
        )

        # Initialize the Bot Framework service for sending messages
        self.bot = BotService(
            app_id=self.app_id,
            app_secret=self.app_secret,
            tenant_id=self.tenant_id,
            logger=self.logger,
        )

    def _get_app_token(self):
        """Authenticate using OAuth2 client_credentials flow (app-only, no user account)."""
        self.logger.info("Authenticating with client_credentials flow...")
        token_url = f"{AUTH_URL.get(self.endpoint)}/{self.tenant_id}/oauth2/v2.0/token"

        body = {
            "grant_type": "client_credentials",
            "client_id": self.app_id,
            "client_secret": self.app_secret,
            "scope": GRAPH_SCOPE_DEFAULT,
        }

        self.logger.info(f"Getting token from: {token_url}")

        try:
            result = requests.post(token_url, data=body, timeout=TIMEOUT)
        except requests.exceptions.Timeout as error:
            raise PluginException(
                cause="Authentication request timed out",
                assistance="Please verify network connectivity and try again.",
                data=str(error),
            ) from error
        except requests.exceptions.ConnectionError as error:
            raise PluginException(
                cause="Unable to connect to authentication endpoint",
                assistance=f"Could not connect to {token_url}. Please verify network connectivity.",
                data=str(error),
            ) from error

        if result.status_code != 200:
            raise PluginException(
                cause="Authentication to Microsoft Graph failed.",
                assistance="Please verify your Application ID, Directory ID, and Application Secret are correct. "
                "Ensure the app registration has the required Microsoft Graph application permissions "
                "with admin consent granted.",
                data=result.text,
            )

        try:
            result_json = result.json()
            self.api_token = result_json.get("access_token")
        except (ValueError, KeyError) as error:
            raise PluginException(
                cause="Failed to parse authentication response",
                assistance="Unexpected response from the token endpoint.",
                data=str(error),
            ) from error

        self.time_ago = time.time()
        self.logger.info(f"Authentication successful, token is: ******************{self.api_token[-5:]}")

    def check_and_refresh_api_token(self, force_refresh=False):
        """Refresh the token if it's expired (tokens last ~1 hour)."""
        self.time_now = time.time()
        if (self.time_now - self.time_ago) > 3500 or force_refresh:
            self.logger.info("Refreshing auth token...")
            self._get_app_token()
        else:
            self.logger.info("Token is valid, not refreshing.")

    def get_headers(self, force_refresh=False) -> dict:
        """Get authorization headers, refreshing the token if needed."""
        self.check_and_refresh_api_token(force_refresh)
        return {
            "Authorization": f"Bearer {self.api_token}",
            "Content-Type": "application/json",
        }

    def test(self):
        try:
            self._get_app_token()
        except PluginException as error:
            raise ConnectionTestException(
                cause="Unable to get authentication token.",
                assistance="Please verify your Application ID, Directory ID, and Application Secret. "
                "Ensure the app registration has Microsoft Graph application permissions with admin consent.",
            ) from error

        if not self.api_token:
            raise ConnectionTestException(
                cause="No authentication token received.",
                assistance="Please check your connection settings.",
            )

        # Verify we can actually call the Graph API
        try:
            headers = self.get_headers()
            test_result = requests.get(
                f"{self.resource_endpoint}/v1.0/organization",
                headers=headers,
                timeout=TIMEOUT,
            )
            test_result.raise_for_status()
        except Exception as error:
            raise ConnectionTestException(
                cause="Authentication succeeded but API call failed.",
                assistance="The token was obtained but could not access Microsoft Graph. "
                "Verify the app has Organization.Read.All or similar permissions.",
            ) from error

        return {"success": True}
