import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase

from icon_microsoft_teams.actions.get_message_in_chat import GetMessageInChat
from icon_microsoft_teams.actions.get_message_in_chat.schema import Input, GetMessageInChatInput, GetMessageInChatOutput
from jsonschema import validate

from util import Util


class TestGetMessageInChat(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetMessageInChat())

    def test_get_message_in_chat(self) -> None:
        expected_message = {
            "id": "1234567890",
            "messageType": "message",
            "body": {"contentType": "text", "content": "Hello World"},
            "from": {"user": {"id": "user-123", "displayName": "Test User"}},
        }
        self.action.connection.client.get_chat_message.return_value = expected_message

        test_input = {
            Input.CHAT_ID: "19:abc123@thread.v2",
            Input.MESSAGE_ID: "1234567890",
        }
        validate(test_input, GetMessageInChatInput.schema)
        actual = self.action.run(test_input)

        self.action.connection.client.get_chat_message.assert_called_once_with("19:abc123@thread.v2", "1234567890")
        self.assertEqual(actual["message"]["id"], "1234567890")
        self.assertEqual(actual["message"]["body"]["content"], "Hello World")
        validate(actual, GetMessageInChatOutput.schema)
