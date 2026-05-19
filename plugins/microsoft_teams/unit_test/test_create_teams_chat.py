import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase

from icon_microsoft_teams.actions.create_teams_chat import CreateTeamsChat
from icon_microsoft_teams.actions.create_teams_chat.schema import CreateTeamsChatInput, CreateTeamsChatOutput
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
