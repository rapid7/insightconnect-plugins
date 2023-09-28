import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest.mock import patch
from komand_sentinelone.actions.mark_as_benign import MarkAsBenign
from util import Util
from unittest import TestCase
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException


@patch("requests.post", side_effect=Util.mocked_requests_get)
@patch("requests.request", side_effect=Util.mocked_requests_get)
class TestMarkAsBenign(TestCase):
    @classmethod
    @patch("requests.post", side_effect=Util.mocked_requests_get)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(MarkAsBenign())

    @parameterized.expand(
        [
            [
                "success",
                Util.read_file_to_dict("inputs/mark_as_benign_success.json.inp"),
                Util.read_file_to_dict("expected/mark_as_benign_success.json.exp"),
            ],
            [
                "success_no_affected",
                Util.read_file_to_dict("inputs/mark_as_benign_success_no_affected.json.inp"),
                Util.read_file_to_dict("expected/mark_as_benign_success_no_affected.json.exp"),
            ],
            [
                "success_with_whitening_option",
                Util.read_file_to_dict("inputs/mark_as_benign_success_with_whitening_option.json.inp"),
                Util.read_file_to_dict("expected/mark_as_benign_success.json.exp"),
            ],
        ]
    )
    def test_mark_as_benign(self, mock_request, mock_post, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertEqual(expected, actual)

    @parameterized.expand(
        [
            [
                "invalid_threat_id",
                Util.read_file_to_dict("inputs/mark_as_benign_invalid_threat_id.json.inp"),
                "The server is unable to process the request.",
                "Verify your plugin input is correct and not malformed and try again. If the issue persists, please contact support.",
            ],
        ]
    )
    def test_mark_as_benign_raise_exception(self, mock_request, mock_post, test_name, input_params, cause, assistance):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_params)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
