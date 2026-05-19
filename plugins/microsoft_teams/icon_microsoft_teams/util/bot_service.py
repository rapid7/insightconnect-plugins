import requests
from logging import Logger
from insightconnect_plugin_runtime.exceptions import PluginException

from icon_microsoft_teams.util.constants import (
    TIMEOUT,
    BOT_FRAMEWORK_SCOPE,
    BOT_SERVICE_URL,
)


class BotService:
    """
    Bot Framework service for sending messages to Microsoft Teams.

    Uses the Bot Framework REST API to send messages as a bot identity,
    eliminating the need for a user account. The bot must be registered
    in Azure and installed in the target teams/channels.
    """

    def __init__(self, app_id: str, app_secret: str, tenant_id: str, logger: Logger):
        """
        Initialize the Bot Service.

        :param app_id: The Azure Bot / App Registration client ID
        :param app_secret: The Azure Bot / App Registration client secret
        :param tenant_id: The Azure AD tenant ID (used for single-tenant bot auth)
        :param logger: Logger instance
        """
        self._app_id = app_id
        self._app_secret = app_secret
        self._tenant_id = tenant_id
        self._logger = logger
        self._session = requests.Session()
        self._token = None
        self._service_url = BOT_SERVICE_URL

    def _get_bot_token(self) -> str:
        """Authenticate with the Bot Framework and get an access token."""
        if self._token:
            return self._token

        # For single-tenant bots, authenticate against the app's own tenant
        # For multi-tenant bots, use botframework.com
        token_url = f"https://login.microsoftonline.com/{self._tenant_id}/oauth2/v2.0/token"

        body = {
            "grant_type": "client_credentials",
            "client_id": self._app_id,
            "client_secret": self._app_secret,
            "scope": BOT_FRAMEWORK_SCOPE,
        }

        self._logger.info(f"Authenticating with Bot Framework via tenant: {self._tenant_id}")

        try:
            response = self._session.post(token_url, data=body, timeout=TIMEOUT)
        except requests.exceptions.Timeout as error:
            raise PluginException(
                cause="Bot Framework authentication timed out",
                assistance="Please verify network connectivity and try again.",
                data=str(error),
            ) from error
        except requests.exceptions.ConnectionError as error:
            raise PluginException(
                cause="Unable to connect to Bot Framework token endpoint",
                assistance="Please verify network connectivity.",
                data=str(error),
            ) from error

        if response.status_code != 200:
            raise PluginException(
                cause="Bot Framework authentication failed",
                assistance="Please verify the Application ID and Application Secret are correct, "
                "and that the app registration is configured as a Bot.",
                data=response.text,
            )

        try:
            result = response.json()
            self._token = result.get("access_token")
        except (ValueError, KeyError) as error:
            raise PluginException(
                cause="Failed to parse Bot Framework token response",
                assistance="Unexpected response from the token endpoint.",
                data=str(error),
            ) from error

        self._logger.info("Bot Framework authentication successful.")
        return self._token

    def _get_bot_headers(self) -> dict:
        """Get headers with Bot Framework bearer token."""
        token = self._get_bot_token()
        return {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        }

    def invalidate_token(self):
        """Force token refresh on next request."""
        self._token = None

    def send_channel_message(  # pylint: disable=too-many-arguments,too-many-positional-arguments
        self,
        team_id: str,
        channel_id: str,
        message: str,
        content_type: str = "text",
        thread_id: str = None,
    ) -> dict:
        """
        Send a message to a Teams channel via Bot Framework.

        The bot must be installed in the team for this to work.

        :param team_id: The team ID (group ID)
        :param channel_id: The channel ID
        :param message: Message content
        :param content_type: 'text' or 'html'
        :param thread_id: Optional parent message ID for threaded replies
        :return: Activity response dict
        """
        conversation_id = channel_id
        if thread_id:
            conversation_id = f"{channel_id};messageid={thread_id}"

        endpoint = f"{self._service_url}/v3/conversations/{conversation_id}/activities"

        activity = {
            "type": "message",
            "text": message if content_type == "text" else None,
            "textFormat": "plain" if content_type == "text" else "xml",
            "channelData": {
                "teamsChannelId": channel_id,
                "teamsTeamId": team_id,
            },
        }

        if content_type == "html":
            activity["text"] = message
            activity["textFormat"] = "xml"

        return self._send_activity(endpoint, activity)

    def send_chat_message(self, chat_id: str, message: str, content_type: str = "text") -> dict:
        """
        Send a message to a Teams chat via Bot Framework.

        The bot must be a participant in the chat for this to work.

        :param chat_id: The chat ID
        :param message: Message content
        :param content_type: 'text' or 'html'
        :return: Activity response dict
        """
        endpoint = f"{self._service_url}/v3/conversations/{chat_id}/activities"

        activity = {
            "type": "message",
            "text": message,
            "textFormat": "plain" if content_type == "text" else "xml",
        }

        return self._send_activity(endpoint, activity)

    def _send_activity(self, endpoint: str, activity: dict) -> dict:
        """
        Send an activity to the Bot Framework.

        Includes a single retry on 401 (token expiry).
        """
        headers = self._get_bot_headers()

        self._logger.info(f"Sending bot activity to: {endpoint}")

        response = self._post_activity(endpoint, activity, headers)

        # Single retry on 401 (token expired)
        if response.status_code == 401:
            self._logger.info("Bot token expired, refreshing and retrying...")
            self.invalidate_token()
            headers = self._get_bot_headers()
            response = self._post_activity(endpoint, activity, headers)

        return self._handle_activity_response(response)

    def _post_activity(self, endpoint: str, activity: dict, headers: dict) -> requests.Response:
        """Post an activity to the Bot Framework endpoint with error handling."""
        try:
            return self._session.post(endpoint, json=activity, headers=headers, timeout=TIMEOUT)
        except requests.exceptions.Timeout as error:
            raise PluginException(
                cause="Bot message send timed out",
                assistance="Please verify network connectivity and try again.",
                data=str(error),
            ) from error
        except requests.exceptions.ConnectionError as error:
            raise PluginException(
                cause="Unable to connect to Bot Framework service",
                assistance=f"Could not connect to {self._service_url}. Please verify network connectivity.",
                data=str(error),
            ) from error

    def _handle_activity_response(self, response: requests.Response) -> dict:
        """Handle the response from a Bot Framework activity post."""
        if response.status_code in (200, 201):
            try:
                return response.json()
            except ValueError:
                return {"id": "sent"}

        if response.status_code == 403:
            raise PluginException(
                cause="Bot is not authorized to send messages to this conversation",
                assistance="Ensure the bot app is installed in the target team or added to the chat. "
                "Go to the Teams channel > Manage channel > Apps and add your bot.",
                data=response.text,
            )

        if response.status_code == 404:
            raise PluginException(
                cause="Conversation not found",
                assistance="The specified team/channel/chat was not found. "
                "Verify the IDs are correct and the bot is installed in the target team.",
                data=response.text,
            )

        raise PluginException(
            cause=f"Bot message send failed with status {response.status_code}",
            assistance="Please verify the bot is properly configured and installed in the target team.",
            data=response.text[:1000],
        )
