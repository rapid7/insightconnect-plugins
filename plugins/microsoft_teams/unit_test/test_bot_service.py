import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock

from icon_microsoft_teams.util.bot_service import BotService
from insightconnect_plugin_runtime.exceptions import PluginException


class TestBotServiceSendChatMessage(TestCase):
    """Tests for the BotService.send_chat_message method."""

    def setUp(self) -> None:
        self.bot = BotService.__new__(BotService)
        self.bot._service_url = "https://smba.trafficmanager.net/teams"
        self.bot._logger = MagicMock()
        self.bot._get_auth_headers = MagicMock(return_value={"Authorization": "Bearer token"})
        self.bot._call_api = MagicMock()
        self.bot._token = "fake-token"
        self.bot._token_acquired_at = 9999999999
        self.bot._token_lifetime = 3500

    def test_send_chat_message_success(self) -> None:
        """Successful send returns message dict."""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"id": "msg-001"}
        self.bot._call_api.return_value = mock_response

        result = self.bot.send_chat_message("19:chat-id@thread.v2", "Hello")
        self.assertEqual(result["id"], "msg-001")

    def test_send_chat_message_403_raises(self) -> None:
        """On 403, raises PluginException."""
        mock_response = MagicMock()
        mock_response.status_code = 403
        mock_response.text = "Bot not authorized"
        self.bot._call_api.return_value = mock_response

        with self.assertRaises(PluginException) as context:
            self.bot.send_chat_message("19:chat-id@thread.v2", "Hello")
        self.assertIn("not authorized", context.exception.cause)

    def test_send_chat_message_404_raises(self) -> None:
        """On 404, raises PluginException."""
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_response.text = "Not found"
        self.bot._call_api.return_value = mock_response

        with self.assertRaises(PluginException) as context:
            self.bot.send_chat_message("19:bad-id@thread.v2", "Hello")
        self.assertIn("not found", context.exception.cause)

    def test_send_chat_message_html(self) -> None:
        """HTML content type is passed correctly."""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"id": "msg-003"}
        self.bot._call_api.return_value = mock_response

        result = self.bot.send_chat_message("19:chat-id@thread.v2", "<b>Hello</b>", content_type="html")
        self.assertEqual(result["id"], "msg-003")

        call_kwargs = self.bot._call_api.call_args
        activity = call_kwargs.kwargs.get("json") or call_kwargs[1].get("json")
        self.assertEqual(activity["textFormat"], "xml")

    def test_send_chat_message_401_retries_with_fresh_token(self) -> None:
        """On 401, refreshes token and retries."""
        mock_401 = MagicMock()
        mock_401.status_code = 401

        mock_200 = MagicMock()
        mock_200.status_code = 200
        mock_200.json.return_value = {"id": "msg-004"}

        self.bot._call_api.side_effect = [mock_401, mock_200]

        result = self.bot.send_chat_message("19:chat-id@thread.v2", "Hello")
        self.assertEqual(result["id"], "msg-004")
        self.bot._get_auth_headers.assert_called_with(force_refresh=True)
