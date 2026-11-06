import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase

from icon_microsoft_teams.actions.list_messages_in_chat import ListMessagesInChat
from icon_microsoft_teams.actions.list_messages_in_chat.schema import ListMessagesInChatInput, ListMessagesInChatOutput
from jsonschema import validate

from util import Util


class TestListMessagesInChat(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(ListMessagesInChat())

    def test_list_messages_in_chat_valid(self) -> None:
        expected_messages = [
            {"id": "msg-1", "body": {"content": "Hello", "contentType": "text"}},
            {"id": "msg-2", "body": {"content": "World", "contentType": "text"}},
        ]
        self.action.connection.client.list_chat_messages.return_value = expected_messages

        test_input = {"chat_id": "valid_chat_id"}
        validate(test_input, ListMessagesInChatInput.schema)
        actual = self.action.run(test_input)
        self.assertEqual(actual, {"messages": expected_messages})
        validate(actual, ListMessagesInChatOutput.schema)
        self.action.connection.client.list_chat_messages.assert_called_once_with("valid_chat_id")
