from logging import Logger

import requests
from insightconnect_plugin_runtime.exceptions import PluginException

from icon_microsoft_teams.util.base_client import BaseClient
from icon_microsoft_teams.util.constants import BOT_FRAMEWORK_SCOPE, BOT_SERVICE_URL, AUTH_URL


class BotService(BaseClient):
    """
    Bot Framework service for sending messages to Microsoft Teams.

    Uses the Bot Framework REST API to send messages as a bot identity,
    eliminating the need for a user account. The bot must be registered
    in Azure and installed in the target teams/channels.
    """

    def __init__(  # pylint: disable=too-many-arguments,too-many-positional-arguments
        self, app_id: str, app_secret: str, tenant_id: str, endpoint: str, logger: Logger
    ):
        """
        Initialize the Bot Service.

        :param app_id: Azure Bot / App Registration client ID
        :param app_secret: Azure Bot / App Registration client secret
        :param tenant_id: Azure AD tenant ID (used for single-tenant bot auth)
        :param endpoint: Endpoint type (Normal, GCC, etc.) for auth URL resolution
        :param logger: Logger instance
        """
        super().__init__(
            app_id=app_id,
            app_secret=app_secret,
            tenant_id=tenant_id,
            auth_url=AUTH_URL.get(endpoint, "https://login.microsoftonline.com"),
            scope=BOT_FRAMEWORK_SCOPE,
            logger=logger,
        )
        self._service_url = BOT_SERVICE_URL

    def test(self):
        """
        Test Bot Service connectivity by authenticating.

        :raises PluginException: If authentication fails
        """
        try:
            self._authenticate()
        except PluginException:
            raise
        except Exception as error:
            raise PluginException(
                cause="Bot Service connection test failed.",
                assistance="Please verify your Application ID and Application Secret are correct for the Bot Service. "
                "Ensure the bot app registration has the Bot Framework API permissions.",
                data=error,
            ) from error

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
            "text": message,
            "textFormat": "plain" if content_type == "text" else "xml",
            "channelData": {
                "teamsChannelId": channel_id,
                "teamsTeamId": team_id,
            },
        }

        if content_type == "html":
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
        headers = self._get_auth_headers()
        self._logger.info(f"Sending bot activity to: {endpoint}")

        response = self._post_activity(endpoint, activity, headers)

        # Single retry on 401 (token expired)
        if response.status_code == 401:
            self._logger.info("Bot token expired, refreshing and retrying...")
            headers = self._get_auth_headers(force_refresh=True)
            response = self._post_activity(endpoint, activity, headers)

        return self._handle_activity_response(response)

    def _post_activity(self, endpoint: str, activity: dict, headers: dict) -> requests.Response:
        """Post an activity to the Bot Framework endpoint."""
        return self._call_api("POST", endpoint, headers=headers, json=activity)

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
                "If you have configured the App Catalog ID in the connection, the bot will "
                "attempt to auto-install itself on retry.",
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
