import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from icon_microsoft_intune.actions.get_autopilot_device import GetAutopilotDevice
from util import Util
from insightconnect_plugin_runtime.exceptions import PluginException
from parameterized import parameterized


@patch("requests.request", side_effect=Util.mocked_requests)
class TestGetAutopilotDevice(TestCase):
    @classmethod
    @patch("requests.request", side_effect=Util.mocked_requests)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(GetAutopilotDevice())

    @parameterized.expand(
        [
            [
                "valid_device_id",
                Util.read_file_to_dict("inputs/get_autopilot_device.json.inp"),
                Util.read_file_to_dict("expected/get_autopilot_device.json.exp"),
            ],
        ]
    )
    def test_get_autopilot_device(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertDictEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "invalid_device_id",
                Util.read_file_to_dict("inputs/get_autopilot_device_invalid_id.json.inp"),
                "Resource not found.",
                "Please provide valid inputs and try again.",
            ],
        ]
    )
    def test_get_autopilot_device_raise_exception(self, mock_request, test_name, input_params, cause, assistance):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_params)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
