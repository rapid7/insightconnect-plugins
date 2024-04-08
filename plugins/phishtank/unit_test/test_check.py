import sys
import os
from unittest.mock import patch, MagicMock
from unittest import TestCase
from komand_phishtank.actions.check import Check
from insightconnect_plugin_runtime.exceptions import PluginException
from util import Util
from parameterized import parameterized

sys.path.append(os.path.abspath('../'))


class TestCheck(TestCase):

    @classmethod
    def setUp(cls) -> None:
        cls.action = Util.default_connector(Check())

    @parameterized.expand(
     [
         [
            "check",
            Util.read_file_to_dict("inputs/check.json.inp"),
            Util.read_file_to_dict("expected/check.json.exp"),
         ],
     ]
    )
    @patch("requests.post", side_effect=Util.mock_request)
    def test_check(self, test_name, input, expected, _test_mock: MagicMock):
        actual = self.action.run(input)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "check_403",
                Util.read_file_to_dict("inputs/check_403.json.inp"),
                "Invalid API key provided.",
                "Verify your API key configured in your connection is correct.",
            ],
            [
                "check_400",
                Util.read_file_to_dict("inputs/check_400.json.inp"),
                "The server is unable to process the request.",
                "Verify your plugin input is correct and not malformed and try again. "
                "If the issue persists, please contact support.",
            ],
            [
                "check_401",
                Util.read_file_to_dict("inputs/check_401.json.inp"),
                "The account configured in your connection is unauthorized to access this service.",
                "Verify the permissions for your account and try again.",
            ],
            [
                "check_404",
                Util.read_file_to_dict("inputs/check_404.json.inp"),
                "Invalid or unreachable endpoint provided.",
                "Verify the URLs or endpoints in your configuration are correct.",
            ],
            [
                "check_429",
                Util.read_file_to_dict("inputs/check_429.json.inp"),
                "Too Many Requests",
                "With no API key, phishtank does not support"
                "more than a few requests per day. Please try again later",
            ],
            [
                "check_server",
                Util.read_file_to_dict("inputs/check_server.json.inp"),
                "Server error occurred",
                "Verify your plugin connection inputs are correct and not malformed and try again. "
                "If the issue persists, please contact support.",
            ],
            [
                "check_unknown",
                Util.read_file_to_dict("inputs/check_unknown.json.inp"),
                "Something unexpected occurred.",
                "Check the logs and if the issue persists please contact support.",
            ],
            [
                "check_json_decoder",
                Util.read_file_to_dict("inputs/check_json_error.json.inp"),
                "Something unexpected occurred.",
                "Check the logs and if the issue persists please contact support.",
            ],
        ]
    )
    @patch("requests.post", side_effect=Util.mock_request)
    def test_check_errors(self, _test_name: str, input_params: str, cause: str, assistance: str, _test_mock: MagicMock):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_params)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
