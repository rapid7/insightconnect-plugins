import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock, patch, PropertyMock

from icon_microsoft_teams.actions.create_teams_chat import CreateTeamsChat
from icon_microsoft_teams.actions.create_teams_chat.schema import CreateTeamsChatInput, CreateTeamsChatOutput
from icon_microsoft_teams.util.graph_api_client import GraphApiClient
from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate

from util import Util


class TestCreateTeamsChat(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(CreateTeamsChat())

    def test_create_one_on_one_chat(self) -> None:
        expected_result = {
            "chatType": "oneOnOne",
            "id": "19:abc123@thread.v2",
            "createdDateTime": "2023-11-09T12:07:43.167Z",
        }
        self.action.connection.client.create_chat.return_value = expected_result

        test_input = {
            "members": [
                {"user_info": "user1@example.com", "role": "owner"},
                {"user_info": "user2@example.com", "role": "owner"},
            ]
        }
        validate(test_input, CreateTeamsChatInput.schema)
        actual = self.action.run(test_input)
        self.assertEqual(actual["chat"]["chatType"], "oneOnOne")
        validate(actual, CreateTeamsChatOutput.schema)

    def test_create_group_chat(self) -> None:
        expected_result = {
            "chatType": "group",
            "id": "19:def456@thread.v2",
            "topic": "Test Topic",
            "createdDateTime": "2023-11-09T12:07:43.167Z",
        }
        self.action.connection.client.create_chat.return_value = expected_result

        test_input = {
            "members": [
                {"user_info": "user1@example.com", "role": "owner"},
                {"user_info": "user2@example.com", "role": "owner"},
                {"user_info": "user3@example.com", "role": "guest"},
            ],
            "topic": "Test Topic",
        }
        validate(test_input, CreateTeamsChatInput.schema)
        actual = self.action.run(test_input)
        self.assertEqual(actual["chat"]["chatType"], "group")
        validate(actual, CreateTeamsChatOutput.schema)

    def test_create_chat_with_installed_apps(self) -> None:
        expected_result = {
            "chatType": "oneOnOne",
            "id": "19:ghi789@unq.gbl.spaces",
            "createdDateTime": "2023-11-09T12:07:43.167Z",
        }
        self.action.connection.client.create_chat.return_value = expected_result

        test_input = {
            "members": [
                {"user_info": "user1@example.com", "role": "owner"},
                {"user_info": "user2@example.com", "role": "owner"},
            ],
            "installed_apps": ["05F59CEC-A742-4A50-A62E-202A57E478A4"],
        }
        validate(test_input, CreateTeamsChatInput.schema)
        actual = self.action.run(test_input)
        self.assertEqual(actual["chat"]["id"], "19:ghi789@unq.gbl.spaces")
        validate(actual, CreateTeamsChatOutput.schema)
        self.action.connection.client.create_chat.assert_called_once_with(
            test_input["members"],
            None,
            installed_apps=["05F59CEC-A742-4A50-A62E-202A57E478A4"],
        )

    def test_create_group_chat_with_installed_apps(self) -> None:
        expected_result = {
            "chatType": "group",
            "id": "19:jkl012@thread.v2",
            "topic": "Bot Chat",
            "createdDateTime": "2023-11-09T12:07:43.167Z",
        }
        self.action.connection.client.create_chat.return_value = expected_result

        test_input = {
            "members": [
                {"user_info": "user1@example.com", "role": "owner"},
                {"user_info": "user2@example.com", "role": "owner"},
                {"user_info": "user3@example.com", "role": "owner"},
            ],
            "topic": "Bot Chat",
            "installed_apps": ["05F59CEC-A742-4A50-A62E-202A57E478A4", "ANOTHER-APP-ID-HERE"],
        }
        validate(test_input, CreateTeamsChatInput.schema)
        actual = self.action.run(test_input)
        self.assertEqual(actual["chat"]["chatType"], "group")
        self.assertEqual(actual["chat"]["topic"], "Bot Chat")
        validate(actual, CreateTeamsChatOutput.schema)


class TestGraphApiClientCreateChat(TestCase):
    """Tests for the GraphApiClient.create_chat method and async handling."""

    def setUp(self) -> None:
        self.client = GraphApiClient.__new__(GraphApiClient)
        self.client._base_url = "https://graph.microsoft.com"
        self.client._logger = MagicMock()
        self.client._get_auth_headers = MagicMock(return_value={"Authorization": "Bearer token"})
        self.client._call_api = MagicMock()
        self.client._make_request = MagicMock()
        self.client._raise_for_status = MagicMock()

    def test_create_chat_201_response(self) -> None:
        """Test successful synchronous chat creation (201)."""
        mock_response = MagicMock()
        mock_response.status_code = 201
        mock_response.json.return_value = {"id": "19:abc@thread.v2", "chatType": "oneOnOne"}
        self.client._call_api.return_value = mock_response

        result = self.client.create_chat(
            members=[
                {"user_info": "user1@example.com", "role": "owner"},
                {"user_info": "user2@example.com", "role": "owner"},
            ]
        )
        self.assertEqual(result["id"], "19:abc@thread.v2")

    def test_create_chat_with_installed_apps_payload(self) -> None:
        """Test that installed_apps are included in the request payload."""
        mock_response = MagicMock()
        mock_response.status_code = 201
        mock_response.json.return_value = {"id": "19:abc@thread.v2", "chatType": "oneOnOne"}
        self.client._call_api.return_value = mock_response

        self.client.create_chat(
            members=[
                {"user_info": "user1@example.com", "role": "owner"},
                {"user_info": "user2@example.com", "role": "owner"},
            ],
            installed_apps=["APP-ID-123"],
        )

        call_kwargs = self.client._call_api.call_args
        payload = call_kwargs.kwargs.get("json") or call_kwargs[1].get("json")
        self.assertIn("installedApps", payload)
        self.assertEqual(
            payload["installedApps"][0]["teamsApp@odata.bind"],
            "https://graph.microsoft.com/v1.0/appCatalogs/teamsApps/APP-ID-123",
        )

    @patch("icon_microsoft_teams.util.graph_api_client.sleep")
    def test_create_chat_202_direct_fetch_success(self, mock_sleep) -> None:
        """Test 202 response where direct chat fetch succeeds immediately."""
        mock_response = MagicMock()
        mock_response.status_code = 202
        mock_response.headers = {"Location": "/chats('19:test-chat-id@unq.gbl.spaces')/operations('op-123')"}
        self.client._call_api.return_value = mock_response
        self.client._make_request.return_value = {
            "id": "19:test-chat-id@unq.gbl.spaces",
            "chatType": "group",
        }

        result = self.client.create_chat(
            members=[
                {"user_info": "user1@example.com", "role": "owner"},
                {"user_info": "user2@example.com", "role": "owner"},
            ],
            installed_apps=["APP-ID"],
        )

        self.assertEqual(result["id"], "19:test-chat-id@unq.gbl.spaces")
        self.client._make_request.assert_called_with("GET", "/v1.0/chats/19:test-chat-id@unq.gbl.spaces")

    @patch("icon_microsoft_teams.util.graph_api_client.sleep")
    def test_create_chat_202_polling_success(self, mock_sleep) -> None:
        """Test 202 response where direct fetch fails but polling succeeds."""
        # Initial POST returns 202
        mock_post_response = MagicMock()
        mock_post_response.status_code = 202
        mock_post_response.headers = {"Location": "/chats('19:chat-id@unq.gbl.spaces')/operations('op-456')"}

        # Polling returns succeeded
        mock_poll_response = MagicMock()
        mock_poll_response.status_code = 200
        mock_poll_response.json.return_value = {"status": "succeeded"}

        self.client._call_api.side_effect = [mock_post_response, mock_poll_response]
        # First _make_request raises (direct fetch fails), second succeeds (after poll)
        self.client._make_request.side_effect = [
            PluginException(cause="Not found", assistance=""),
            {"id": "19:chat-id@unq.gbl.spaces", "chatType": "group"},
        ]

        result = self.client.create_chat(
            members=[
                {"user_info": "user1@example.com", "role": "owner"},
                {"user_info": "user2@example.com", "role": "owner"},
            ],
            installed_apps=["APP-ID"],
        )

        self.assertEqual(result["id"], "19:chat-id@unq.gbl.spaces")

    @patch("icon_microsoft_teams.util.graph_api_client.sleep")
    def test_create_chat_202_no_location_no_chat_id_raises(self, mock_sleep) -> None:
        """Test 202 response with no Location header raises PluginException."""
        mock_response = MagicMock()
        mock_response.status_code = 202
        mock_response.headers = {}
        self.client._call_api.return_value = mock_response

        with self.assertRaises(PluginException) as context:
            self.client.create_chat(
                members=[
                    {"user_info": "user1@example.com", "role": "owner"},
                    {"user_info": "user2@example.com", "role": "owner"},
                ],
                installed_apps=["APP-ID"],
            )
        self.assertIn("no Location header", context.exception.cause)

    def test_create_chat_insufficient_members_raises(self) -> None:
        """Test that less than 2 members raises PluginException."""
        with self.assertRaises(PluginException) as context:
            self.client.create_chat(members=[{"user_info": "user1@example.com", "role": "owner"}])
        self.assertIn("At least 2 members", context.exception.assistance)

    def test_build_chat_payload_one_on_one(self) -> None:
        """Test payload structure for oneOnOne chat."""
        payload = self.client._build_chat_payload(
            members=[
                {"user_info": "user1@example.com", "role": "owner"},
                {"user_info": "user2@example.com", "role": "owner"},
            ]
        )
        self.assertEqual(payload["chatType"], "oneOnOne")
        self.assertEqual(len(payload["members"]), 2)
        self.assertNotIn("installedApps", payload)

    def test_build_chat_payload_group_with_apps(self) -> None:
        """Test payload structure for group chat with installed apps."""
        payload = self.client._build_chat_payload(
            members=[
                {"user_info": "user1@example.com", "role": "owner"},
                {"user_info": "user2@example.com", "role": "owner"},
                {"user_info": "user3@example.com", "role": "guest"},
            ],
            topic="Test Topic",
            installed_apps=["APP-1", "APP-2"],
        )
        self.assertEqual(payload["chatType"], "group")
        self.assertEqual(payload["topic"], "Test Topic")
        self.assertEqual(len(payload["installedApps"]), 2)

    def test_extract_chat_id_from_location(self) -> None:
        """Test chat ID extraction from Location header."""
        location = "/chats('19:abc-123@unq.gbl.spaces')/operations('op-456')"
        result = GraphApiClient._extract_chat_id_from_location(location)
        self.assertEqual(result, "19:abc-123@unq.gbl.spaces")

    def test_extract_chat_id_from_empty_location(self) -> None:
        """Test chat ID extraction returns empty string for empty input."""
        self.assertEqual(GraphApiClient._extract_chat_id_from_location(""), "")
        self.assertEqual(GraphApiClient._extract_chat_id_from_location(None), "")
