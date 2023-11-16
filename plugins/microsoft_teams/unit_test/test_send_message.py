import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException

from icon_microsoft_teams.actions.send_message import SendMessage
from icon_microsoft_teams.actions.send_message.schema import Input, SendMessageInput, SendMessageOutput
from util import Util
from jsonschema import validate


@patch("requests.get", side_effect=Util.mocked_requests)
@patch("requests.post", side_effect=Util.mocked_requests)
class TestSendMessage(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(SendMessage())

    @parameterized.expand(Util.load_data("send_message_parameters").get("parameters"))
    def test_send_message(self, mocked_get, mocked_post, name, team, channel, thread_id, chat_id, message, expected):
        test_input = {Input.MESSAGE: message}
        if team:
            test_input[Input.TEAM_NAME] = team
        if channel:
            test_input[Input.CHANNEL_NAME] = channel
        if thread_id:
            test_input[Input.THREAD_ID] = thread_id
        if chat_id:
            test_input[Input.CHAT_ID] = chat_id
        validate(test_input, SendMessageInput.schema)
        actual = self.action.run(test_input)
        self.assertEqual(actual, expected)
        validate(actual, SendMessageOutput.schema)

    @parameterized.expand(
        [
            [
                "only_message",
                None,
                None,
                None,
                None,
                "test message",
                "No chat ID or team ID with channel ID was provided.",
                "Please provide the chat ID to send the chat message or the team and channel details(name or GUID) to "
                "send the message to a specific channel.",
            ],
            [
                "without_channel",
                "Example Team",
                None,
                None,
                None,
                "test message",
                "No chat ID or team ID with channel ID was provided.",
                "Please provide the chat ID to send the chat message or the team and channel details(name or GUID) to "
                "send the message to a specific channel.",
            ],
            [
                "without_team",
                None,
                "Example Channel",
                None,
                None,
                "test message",
                "No chat ID or team ID with channel ID was provided.",
                "Please provide the chat ID to send the chat message or the team and channel details(name or GUID) to "
                "send the message to a specific channel.",
            ],
            [
                "without_channel_and_team",
                None,
                None,
                "1636037542013",
                None,
                "test message",
                "No chat ID or team ID with channel ID was provided.",
                "Please provide the chat ID to send the chat message or the team and channel details(name or GUID) to "
                "send the message to a specific channel.",
            ],
        ]
    )
    def test_send_message_bad(
        self, mocked_get, mocked_post, name, team, channel, thread_id, chat_id, message, cause, assistance
    ):
        test_input = {Input.MESSAGE: message}
        if team:
            test_input[Input.TEAM_NAME] = team
        if channel:
            test_input[Input.CHANNEL_NAME] = channel
        if thread_id:
            test_input[Input.THREAD_ID] = thread_id
        if chat_id:
            test_input[Input.CHAT_ID] = chat_id
        validate(test_input, SendMessageInput.schema)
        with self.assertRaises(PluginException) as e:
            self.action.run(test_input)
        self.assertEqual(e.exception.cause, cause)
        self.assertEqual(e.exception.assistance, assistance)
