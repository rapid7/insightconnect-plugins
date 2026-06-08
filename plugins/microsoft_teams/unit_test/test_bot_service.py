import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock, patch

from icon_microsoft_teams.util.bot_service import BotService
from insightconnect_plugin_runtime.exceptions import PluginException


class TestBotServiceSendChatMessage(TestCase):
    """Tests for the BotService.send_chat_message auto-install logic."""

    def setUp(self) -> None:
        self.bot = BotService.__new__(BotService)
        self.bot._service_url = "https://smba.trafficmanager.net/teams"
        self.bot._logger = MagicMock()
        self.bot._get_auth_headers = MagicMock(return_value={"Authorization": "Bearer token"})
        self.bot._call_api = MagicMock()
        self.bot._graph_client = MagicMock()
        self.bot._app_catalog_id = "APP-CATALOG-123"
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
        self.bot._graph_client.install_app_in_chat.assert_not_called()

    def test_send_chat_message_403_auto_install_and_retry(self) -> None:
        """On 403, installs app and retries — second attempt succeeds."""
        mock_403 = MagicMock()
        mock_403.status_code = 403
        mock_403.text = "Bot not authorized"

        mock_200 = MagicMock()
        mock_200.status_code = 200
        mock_200.json.return_value = {"id": "msg-002"}

        self.bot._call_api.side_effect = [mock_403, mock_200]

        result = self.bot.send_chat_message("19:chat-id@thread.v2", "Hello")

        self.assertEqual(result["id"], "msg-002")
        self.bot._graph_client.install_app_in_chat.assert_called_once_with("19:chat-id@thread.v2", "APP-CATALOG-123")

    def test_send_chat_message_403_no_app_catalog_id_raises(self) -> None:
        """On 403 without app_catalog_id configured, raises PluginException."""
        self.bot._app_catalog_id = ""

        mock_403 = MagicMock()
        mock_403.status_code = 403
        mock_403.text = "Bot not authorized"
        self.bot._call_api.return_value = mock_403

        with self.assertRaises(PluginException) as context:
            self.bot.send_chat_message("19:chat-id@thread.v2", "Hello")
        self.assertIn("not authorized", context.exception.cause)

    def test_send_chat_message_403_no_graph_client_raises(self) -> None:
        """On 403 without graph_client configured, raises PluginException."""
        self.bot._graph_client = None

        mock_403 = MagicMock()
        mock_403.status_code = 403
        mock_403.text = "Bot not authorized"
        self.bot._call_api.return_value = mock_403

        with self.assertRaises(PluginException) as context:
            self.bot.send_chat_message("19:chat-id@thread.v2", "Hello")
        self.assertIn("not authorized", context.exception.cause)

    def test_send_chat_message_403_retry_still_fails(self) -> None:
        """On 403, installs app, retries, but still gets 403 — raises."""
        mock_403 = MagicMock()
        mock_403.status_code = 403
        mock_403.text = "Bot not authorized"

        self.bot._call_api.return_value = mock_403

        with self.assertRaises(PluginException) as context:
            self.bot.send_chat_message("19:chat-id@thread.v2", "Hello")
        self.assertIn("not authorized", context.exception.cause)
        self.bot._graph_client.install_app_in_chat.assert_called_once()

    def test_send_chat_message_404_raises(self) -> None:
        """On 404, raises without attempting install."""
        mock_404 = MagicMock()
        mock_404.status_code = 404
        mock_404.text = "Not found"
        self.bot._call_api.return_value = mock_404

        with self.assertRaises(PluginException) as context:
            self.bot.send_chat_message("19:bad-id@thread.v2", "Hello")
        self.assertIn("not found", context.exception.cause)
        self.bot._graph_client.install_app_in_chat.assert_not_called()

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
