import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase

from icon_microsoft_teams.actions.get_message_in_channel import GetMessageInChannel
from icon_microsoft_teams.actions.get_message_in_channel.schema import (
    GetMessageInChannelInput,
    GetMessageInChannelOutput,
    Input,
)
from jsonschema import validate

from util import Util


class TestGetMessageInChannel(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(GetMessageInChannel())

    def test_get_message_in_channel(self) -> None:
        expected_message = {
            "id": "1234567890",
            "messageType": "message",
            "body": {"contentType": "text", "content": "Hello World"},
            "from": {"user": {"id": "user-123", "displayName": "Test User"}},
            "channelIdentity": {"teamId": "example-team-id", "channelId": "11:examplechannel.name"},
        }
        self.action.connection.client.get_channel_message.return_value = expected_message

        test_input = {
            Input.TEAM_ID: "example-team-id",
            Input.CHANNEL_ID: "11:examplechannel.name",
            Input.MESSAGE_ID: "1234567890",
            Input.REPLY_ID: "1234567891",
        }
        validate(test_input, GetMessageInChannelInput.schema)
        response = self.action.run(test_input)
        self.assertEqual(response["message"], expected_message)
        validate(response, GetMessageInChannelOutput.schema)
        self.action.connection.client.get_channel_message.assert_called_once_with(
            "example-team-id", "11:examplechannel.name", "1234567890", "1234567891"
        )
