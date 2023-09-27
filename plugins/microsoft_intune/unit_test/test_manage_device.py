import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from icon_microsoft_intune.actions.manage_device import ManageDevice
from util import Util
from insightconnect_plugin_runtime.exceptions import PluginException
from parameterized import parameterized


@patch("requests.request", side_effect=Util.mocked_requests)
class TestManageDevice(TestCase):
    @classmethod
    @patch("requests.request", side_effect=Util.mocked_requests)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(ManageDevice())

    @parameterized.expand(
        [
            [
                "success",
                Util.read_file_to_dict("inputs/manage_device_by_id.json.inp"),
                Util.read_file_to_dict("expected/success.json.exp"),
            ],
            [
                "success2",
                Util.read_file_to_dict("inputs/manage_device_by_name.json.inp"),
                Util.read_file_to_dict("expected/success.json.exp"),
            ],
            [
                "success3",
                Util.read_file_to_dict("inputs/manage_device_by_email_address.json.inp"),
                Util.read_file_to_dict("expected/success.json.exp"),
            ],
            [
                "success4",
                Util.read_file_to_dict("inputs/manage_device_by_user_principal_name.json.inp"),
                Util.read_file_to_dict("expected/success.json.exp"),
            ],
            [
                "whitelisted",
                Util.read_file_to_dict("inputs/manage_device_whitelisted.json.inp"),
                Util.read_file_to_dict("expected/whitelisted.json.exp"),
            ],
        ]
    )
    def test_manage_device(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "not_found",
                Util.read_file_to_dict("inputs/manage_device_not_found.json.inp"),
                "Managed device '9de5069c-5afe-602b-2ea0-a04b66beb200' was not found.",
                "Check if the provided input is correct and try again.",
            ],
            [
                "too_many_results",
                Util.read_file_to_dict("inputs/manage_device_too_many_results.json.inp"),
                "Search criteria 'ac222ffe-222a-22a1-bbf2-e2222457e464b' returned too many results. Results returned: 2.",
                "Check if the provided input is correct and try again.",
            ],
        ]
    )
    def test_manage_device_raise_exception(self, mock_request, test_name, input_params, cause, assistance):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_params)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
