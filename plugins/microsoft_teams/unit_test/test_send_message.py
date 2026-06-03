import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase

from icon_microsoft_teams.actions.send_message import SendMessage
from icon_microsoft_teams.actions.send_message.schema import Input, SendMessageInput, SendMessageOutput
from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate
from parameterized import parameterized

from util import Util


class TestSendMessage(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(SendMessage())

    def test_send_message_to_channel(self) -> None:
        self.action.connection.client.get_teams.return_value = [{"id": "12345", "displayName": "Example Team"}]
        self.action.connection.client.get_channels.return_value = [{"id": "56789", "displayName": "Example Channel"}]
        self.action.connection.bot.send_channel_message.return_value = {"id": "msg-001"}

        test_input = {
            Input.MESSAGE: "Hello World",
            Input.TEAM_NAME: "Example Team",
            Input.CHANNEL_NAME: "Example Channel",
        }
        validate(test_input, SendMessageInput.schema)
        actual = self.action.run(test_input)

        self.action.connection.bot.send_channel_message.assert_called_once_with(
            team_id="12345",
            channel_id="56789",
            message="Hello World",
            content_type="text",
            thread_id=None,
        )
        self.assertEqual(actual["message"]["body"]["content"], "Hello World")
        self.assertEqual(actual["message"]["id"], "msg-001")
        validate(actual, SendMessageOutput.schema)

    def test_send_message_to_chat(self) -> None:
        self.action.connection.bot.send_chat_message.return_value = {"id": "msg-002"}

        test_input = {
            Input.MESSAGE: "Chat message",
            Input.CHAT_ID: "19:abc123@thread.v2",
        }
        validate(test_input, SendMessageInput.schema)
        actual = self.action.run(test_input)

        self.action.connection.bot.send_chat_message.assert_called_once_with("19:abc123@thread.v2", "Chat message")
        self.assertEqual(actual["message"]["body"]["content"], "Chat message")
        validate(actual, SendMessageOutput.schema)

    def test_send_message_to_thread(self) -> None:
        self.action.connection.client.get_teams.return_value = [{"id": "12345", "displayName": "Example Team"}]
        self.action.connection.client.get_channels.return_value = [{"id": "56789", "displayName": "Example Channel"}]
        self.action.connection.bot.send_channel_message.return_value = {"id": "msg-003"}

        test_input = {
            Input.MESSAGE: "Thread reply",
            Input.TEAM_NAME: "Example Team",
            Input.CHANNEL_NAME: "Example Channel",
            Input.THREAD_ID: "1636037542013",
        }
        validate(test_input, SendMessageInput.schema)
        actual = self.action.run(test_input)

        self.action.connection.bot.send_channel_message.assert_called_with(
            team_id="12345",
            channel_id="56789",
            message="Thread reply",
            content_type="text",
            thread_id="1636037542013",
        )
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
            ],
            [
                "without_channel",
                "Example Team",
                None,
                None,
                None,
                "test message",
                "No chat ID or team ID with channel ID was provided.",
            ],
            [
                "without_team",
                None,
                "Example Channel",
                None,
                None,
                "test message",
                "No chat ID or team ID with channel ID was provided.",
            ],
        ]
    )
    def test_send_message_bad(self, name, team, channel, thread_id, chat_id, message, cause) -> None:
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
        with self.assertRaises(PluginException) as context:
            self.action.run(test_input)
        self.assertEqual(context.exception.cause, cause)
