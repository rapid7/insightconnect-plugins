import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase

from komand_pagerduty.actions.get_user_by_id import GetUserById
from unittest.mock import patch, MagicMock
from parameterized import parameterized
from util import Util
from insightconnect_plugin_runtime.exceptions import PluginException


@patch("requests.Session.request", side_effect=Util.mock_request)
class TestGetUserById(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetUserById())

    @parameterized.expand(
        [
            [
                "get_user_valid",
                {"id": "valid_id"},
                Util.read_file_to_dict("expected/get_user_valid.json.exp"),
            ]
        ]
    )
    def test_get_user_by_id(self, mock_request: MagicMock, test_name: str, input_params: dict, expected: dict):
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "api_error_invalid",
                {"id": "invalid_id"},
                "Invalid or unreachable endpoint provided.",
                "Verify the URLs or endpoints in your configuration are correct.",
            ]
        ]
    )
    def test_api_error_invalid(
        self, mock_request: MagicMock, test_name: str, input_params: dict, cause: str, assistance: str
    ):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_params)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
