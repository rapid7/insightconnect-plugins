import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from icon_microsoft_intune.actions.full_scan import FullScan
from util import Util
from insightconnect_plugin_runtime.exceptions import PluginException
from parameterized import parameterized


@patch("requests.request", side_effect=Util.mocked_requests)
class TestFullScan(TestCase):
    @classmethod
    @patch("requests.request", side_effect=Util.mocked_requests)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(FullScan())

    @parameterized.expand(
        [
            [
                "valid_device_id",
                Util.read_file_to_dict("inputs/full_scan.json.inp"),
                Util.read_file_to_dict("expected/full_scan.json.exp"),
            ],
        ]
    )
    def test_full_scan(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "invalid_device_id",
                Util.read_file_to_dict("inputs/full_scan_invalid_device_id.json.inp"),
                "Resource not found.",
                "Please provide valid inputs and try again.",
            ],
        ]
    )
    def test_full_scan_raise_exception(self, mock_request, test_name, input_params, cause, assistance):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_params)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
