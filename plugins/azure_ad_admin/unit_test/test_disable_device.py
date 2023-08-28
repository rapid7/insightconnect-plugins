import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_azure_ad_admin.actions.disable_device import DisableDevice
from unittest.mock import patch
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException
from util import Util


@patch("requests.request", side_effect=Util.mocked_requests)
class TestDisableDevice(TestCase):
    @classmethod
    @patch("requests.post", side_effect=Util.mocked_requests)
    def setUpClass(cls, mock_post) -> None:
        cls.action = Util.default_connector(DisableDevice())

    @parameterized.expand(
        [
            [
                "success",
                Util.read_file_to_dict("inputs/disable_device.json.inp"),
                Util.read_file_to_dict("expected/success.json.exp"),
            ]
        ]
    )
    def test_disable_device(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "not_found",
                Util.read_file_to_dict("inputs/disable_device_invalid.json.inp"),
                "Resource not found.",
                "Please provide valid inputs and try again.",
            ]
        ]
    )
    def test_disable_device_raise_exception(self, mock_request, test_name, input_params, cause, assistance):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_params)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
