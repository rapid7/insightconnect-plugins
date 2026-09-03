import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock

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


class TestGraphApiClientCreateChat(TestCase):
    """Tests for the GraphApiClient.create_chat method."""

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

    def test_build_chat_payload_group_with_topic(self) -> None:
        """Test payload structure for group chat with topic."""
        payload = self.client._build_chat_payload(
            members=[
                {"user_info": "user1@example.com", "role": "owner"},
                {"user_info": "user2@example.com", "role": "owner"},
                {"user_info": "user3@example.com", "role": "guest"},
            ],
            topic="Test Topic",
        )
        self.assertEqual(payload["chatType"], "group")
        self.assertEqual(payload["topic"], "Test Topic")
        self.assertEqual(len(payload["members"]), 3)

    def test_create_chat_error_calls_raise_for_status(self) -> None:
        """Test that non-201 response calls _raise_for_status."""
        mock_response = MagicMock()
        mock_response.status_code = 400
        self.client._call_api.return_value = mock_response

        self.client.create_chat(
            members=[
                {"user_info": "user1@example.com", "role": "owner"},
                {"user_info": "user2@example.com", "role": "owner"},
            ]
        )
        self.client._raise_for_status.assert_called_once_with(mock_response)
