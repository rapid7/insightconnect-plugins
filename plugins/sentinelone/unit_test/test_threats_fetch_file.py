import sys
import os

from parameterized import parameterized

sys.path.append(os.path.abspath("../"))

from unittest.mock import patch
from komand_sentinelone.actions.threats_fetch_file import ThreatsFetchFile
from insightconnect_plugin_runtime.exceptions import PluginException
from util import Util
from unittest import TestCase


@patch("requests.request", side_effect=Util.mocked_requests_get)
class TestThreatsFetchFile(TestCase):
    @classmethod
    @patch("requests.post", side_effect=Util.mocked_requests_get)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(ThreatsFetchFile())

    @parameterized.expand(
        [
            [
                "threats_fetch_file",
                Util.read_file_to_dict("inputs/threats_fetch_file.json.inp"),
                Util.read_file_to_dict("expected/threats_fetch_file.json.exp"),
            ],
        ]
    )
    def test_threats_fetch_file(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "threats_fetch_file_invalid_id",
                Util.read_file_to_dict("inputs/threats_fetch_file_invalid_id.json.inp"),
                "Invalid threat IDs provided.",
                "Please provide valid threat ID and try again.",
            ],
            [
                "threats_fetch_file_password_too_short",
                Util.read_file_to_dict("inputs/threats_fetch_file_password_too_short.json.inp"),
                "Wrong password.",
                "Password must have more than 10 characters and cannot contain whitespace.",
            ],
            [
                "threats_fetch_file_password_with_space",
                Util.read_file_to_dict("inputs/threats_fetch_file_password_with_space.json.inp"),
                "Wrong password.",
                "Password must have more than 10 characters and cannot contain whitespace.",
            ],
        ]
    )
    def test_threats_fetch_file_raise_exception(self, mock_request, test_name, input_params, cause, assistance):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_params)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
