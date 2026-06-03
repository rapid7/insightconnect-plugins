import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase

from icon_microsoft_teams.actions.get_reply_list import GetReplyList
from icon_microsoft_teams.actions.get_reply_list.schema import GetReplyListInput, GetReplyListOutput, Input
from jsonschema import validate

from util import Util


class TestGetReplyList(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(GetReplyList())
        self.action.connection.client.get_teams.return_value = [{"id": "12345", "displayName": "Example Team"}]
        self.action.connection.client.get_channels.return_value = [{"id": "56789", "displayName": "Example Channel"}]

    def test_get_reply_list(self) -> None:
        expected_replies = [
            {"id": "reply-1", "body": {"content": "First reply", "contentType": "text"}},
            {"id": "reply-2", "body": {"content": "Second reply", "contentType": "text"}},
        ]
        self.action.connection.client.get_message_replies.return_value = expected_replies

        test_input = {
            Input.TEAM_NAME: "Example Team",
            Input.CHANNEL_NAME: "Example Channel",
            Input.MESSAGE_ID: "1234567890",
        }
        validate(test_input, GetReplyListInput.schema)
        response = self.action.run(test_input)
        self.assertEqual(response["messages"], expected_replies)
        validate(response, GetReplyListOutput.schema)
        self.action.connection.client.get_message_replies.assert_called_once_with("12345", "56789", "1234567890")
