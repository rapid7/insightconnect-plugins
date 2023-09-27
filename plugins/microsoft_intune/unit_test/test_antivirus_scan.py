import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from icon_microsoft_intune.actions.antivirus_scan import AntivirusScan
from util import Util
from insightconnect_plugin_runtime.exceptions import PluginException
from parameterized import parameterized


@patch("requests.request", side_effect=Util.mocked_requests)
class TestAntivirusScan(TestCase):
    @classmethod
    @patch("requests.request", side_effect=Util.mocked_requests)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(AntivirusScan())

    @parameterized.expand(
        [
            [
                "success",
                Util.read_file_to_dict("inputs/antivirus_scan_by_device_id.json.inp"),
                Util.read_file_to_dict("expected/success.json.exp"),
            ],
            [
                "success2",
                Util.read_file_to_dict("inputs/antivirus_scan_by_device_name.json.inp"),
                Util.read_file_to_dict("expected/success.json.exp"),
            ],
            [
                "success3",
                Util.read_file_to_dict("inputs/antivirus_scan_by_email_address.json.inp"),
                Util.read_file_to_dict("expected/success.json.exp"),
            ],
            [
                "success4",
                Util.read_file_to_dict("inputs/antivirus_scan_by_user_principal_name.json.inp"),
                Util.read_file_to_dict("expected/success.json.exp"),
            ],
        ]
    )
    def test_antivirus_scan(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "not_found",
                Util.read_file_to_dict("inputs/antivirus_scan_device_not_found.json.inp"),
                "Resource not found.",
                "Unable to find a device using device details provided.",
            ]
        ]
    )
    def test_antivirus_scan_raise_exception(self, mock_request, test_name, input_params, cause, assistance):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_params)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
