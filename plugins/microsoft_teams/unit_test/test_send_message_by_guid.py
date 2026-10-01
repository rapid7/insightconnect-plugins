import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase

from icon_microsoft_teams.actions.send_message_by_guid import SendMessageByGuid
from icon_microsoft_teams.actions.send_message_by_guid.schema import Input, SendMessageByGuidOutput
from jsonschema import validate

from util import Util


class TestSendMessageByGuid(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(SendMessageByGuid())
        self.action.connection.bot.send_channel_message.return_value = {"id": "msg-001"}

    def test_send_message_by_guid(self) -> None:
        test_input = {
            Input.TEAM_GUID: "team-guid-123",
            Input.CHANNEL_GUID: "channel-guid-456",
            Input.IS_HTML: False,
            Input.MESSAGE: "Hello World",
        }
        response = self.action.run(test_input)
        self.assertEqual(response["message"]["body"]["content"], "Hello World")
        self.assertEqual(response["message"]["body"]["contentType"], "text")
        validate(response, SendMessageByGuidOutput.schema)
        self.action.connection.bot.send_channel_message.assert_called_once_with(
            team_id="team-guid-123",
            channel_id="channel-guid-456",
            message="Hello World",
            content_type="text",
        )

    def test_send_html_message_by_guid(self) -> None:
        test_input = {
            Input.TEAM_GUID: "team-guid-123",
            Input.CHANNEL_GUID: "channel-guid-456",
            Input.IS_HTML: True,
            Input.MESSAGE: "<b>Bold</b>",
        }
        response = self.action.run(test_input)
        self.assertEqual(response["message"]["body"]["contentType"], "html")
        validate(response, SendMessageByGuidOutput.schema)
