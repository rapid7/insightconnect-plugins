import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase, mock
from unittest.mock import Mock
from icon_microsoft_teams.actions.create_teams_chat import CreateTeamsChat
from parameterized import parameterized
from util import Util
from insightconnect_plugin_runtime.exceptions import PluginException


@mock.patch("requests.post", side_effect=Util.mocked_requests)
class TestCreateTeamsChat(TestCase):
    @classmethod
    def setUp(cls) -> None:
        cls.action = Util.default_connector(CreateTeamsChat())

    @parameterized.expand(
        [
            [
                "valid_one_on_one",
                Util.load_data("input_valid_oneonone_create_teams_chat"),
                Util.load_data("expected_valid_oneonone_create_teams_chat"),
            ],
            [
                "valid_group",
                Util.load_data("input_valid_group_create_teams_chat"),
                Util.load_data("expected_valid_group_create_teams_chat"),
            ],
        ]
    )
    def test_create_teams_chat_valid(self, _mock_request: Mock, _test_name: str, input_params: dict, expected: dict):
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "less than members",
                Util.load_data("input_invalid_create_teams_chat"),
                "Create chat failed.",
                "Less than 2 valid members were provided",
            ],
            [
                "server erro",
                Util.load_data("input_invalid_create_teams_chat_server"),
                "Create chat failed.",
                "Error message",
            ],
        ]
    )
    def test_list_messages_in_chat_invalid(
        self, _mock_request: Mock, _test_name: str, input_params: dict, cause: str, assistance: str
    ):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_params)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
