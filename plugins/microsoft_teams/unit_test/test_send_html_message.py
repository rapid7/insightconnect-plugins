import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase

from icon_microsoft_teams.actions.send_html_message import SendHtmlMessage
from icon_microsoft_teams.actions.send_html_message.schema import Input, SendHtmlMessageOutput
from jsonschema import validate

from util import Util


class TestSendHtmlMessage(TestCase):
    def setUp(self) -> None:
        self.action = Util.default_connector(SendHtmlMessage())
        self.action.connection.client.get_teams.return_value = [{"id": "team-123", "displayName": "Example Team"}]
        self.action.connection.client.get_channels.return_value = [
            {"id": "channel-456", "displayName": "Example Channel"}
        ]
        self.action.connection.bot.send_channel_message.return_value = {"id": "msg-001"}

    def test_send_html_message(self) -> None:
        test_input = {
            Input.TEAM_NAME: "Example Team",
            Input.CHANNEL_NAME: "Example Channel",
            Input.MESSAGE_CONTENT: "<b>Hello World</b>",
        }
        response = self.action.run(test_input)
        self.assertEqual(response["message"]["body"]["content"], "<b>Hello World</b>")
        self.assertEqual(response["message"]["body"]["contentType"], "html")
        validate(response, SendHtmlMessageOutput.schema)
        self.action.connection.bot.send_channel_message.assert_called_once_with(
            team_id="team-123",
            channel_id="channel-456",
            message="<b>Hello World</b>",
            content_type="html",
            thread_id=None,
        )
