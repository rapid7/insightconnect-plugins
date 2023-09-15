import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from icon_microsoft_intune.actions.delete_device_from_autopilot import DeleteDeviceFromAutopilot
from util import Util
from insightconnect_plugin_runtime.exceptions import PluginException
from parameterized import parameterized


@patch("requests.request", side_effect=Util.mocked_requests)
class TestDeleteDeviceFromAutopilot(TestCase):
    @classmethod
    @patch("requests.request", side_effect=Util.mocked_requests)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(DeleteDeviceFromAutopilot())

    @parameterized.expand(
        [
            [
                "success",
                Util.read_file_to_dict("inputs/delete_device_from_autopilot.json.inp"),
                Util.read_file_to_dict("expected/success.json.exp"),
            ],
        ]
    )
    def test_delete_device_from_autopilot(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "invalid_device_id",
                Util.read_file_to_dict("inputs/delete_device_from_autopilot_invalid_id.json.inp"),
                "Resource not found.",
                "Please provide valid inputs and try again.",
            ],
        ]
    )
    def test_delete_device_from_autopilot_raise_exception(
        self, mock_request, test_name, input_params, cause, assistance
    ):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_params)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
