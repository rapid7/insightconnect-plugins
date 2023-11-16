import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase, mock
from unittest.mock import Mock
from icon_microsoft_teams.actions.list_messages_in_chat import ListMessagesInChat
from icon_microsoft_teams.actions.list_messages_in_chat.schema import ListMessagesInChatInput, ListMessagesInChatOutput
from parameterized import parameterized
from util import Util
from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate


@mock.patch("requests.get", side_effect=Util.mocked_requests)
class TestListMessagesInChat(TestCase):
    @classmethod
    def setUp(cls) -> None:
        cls.action = Util.default_connector(ListMessagesInChat())

    @parameterized.expand(
        [
            [
                "valid",
                {"chat_id": "valid_chat_id"},
                Util.load_data("expected_valid_list_messages_in_chat"),
            ]
        ]
    )
    def test_list_messages_in_chat_valid(
        self, _mock_request: Mock, _test_name: str, input_params: dict, expected: dict
    ):
        validate(input_params, ListMessagesInChatInput.schema)
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)
        validate(actual, ListMessagesInChatOutput.schema)

    @parameterized.expand(
        [
            [
                "bad_request_invalid",
                {"chat_id": "invalid_chat_id_bad_rquest"},
                "The server is unable to process the request.",
                "Verify your plugin input is correct and not malformed and try again. If the issue persists, please contact support.",
            ],
            [
                "invalid_json",
                {"chat_id": "invalid_chat_id_empty_json"},
                "Received an unexpected response from the server.",
                "(non-JSON or no response was received).",
            ],
        ]
    )
    def test_list_messages_in_chat_invalid(
        self, _mock_request: Mock, _test_name: str, input_params: dict, cause: str, assistance: str
    ):
        validate(input_params, ListMessagesInChatInput.schema)
        with self.assertRaises(PluginException) as error:
            self.action.run(input_params)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
