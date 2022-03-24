import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_microsoft_teams.actions.send_message import SendMessage
from icon_microsoft_teams.actions.send_message.schema import Input, Output
from unit_test.util import Util
from unittest.mock import patch
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException


@patch("requests.get", side_effect=Util.mocked_requests)
@patch("requests.post", side_effect=Util.mocked_requests)
class TestSendMessage(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(SendMessage())

    @parameterized.expand(Util.load_data("send_message_parameters").get("parameters"))
    def test_send_message(self, mocked_get, mocked_post, name, team, channel, thread_id, chat_id, message, expected):
        actual = self.action.run(
            {
                Input.TEAM_NAME: team,
                Input.CHANNEL_NAME: channel,
                Input.THREAD_ID: thread_id,
                Input.CHAT_ID: chat_id,
                Input.MESSAGE: message,
            }
        )
        self.assertEqual(actual, expected)

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
        with self.assertRaises(PluginException) as e:
            self.action.run(
                {
                    Input.TEAM_NAME: team,
                    Input.CHANNEL_NAME: channel,
                    Input.THREAD_ID: thread_id,
                    Input.CHAT_ID: chat_id,
                    Input.MESSAGE: message,
                }
            )
        self.assertEqual(e.exception.cause, cause)
        self.assertEqual(e.exception.assistance, assistance)
