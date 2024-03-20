import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_cuckoo.actions.view_machine import ViewMachine
from komand_cuckoo.actions.view_machine.schema import ViewMachineOutput
from insightconnect_plugin_runtime.exceptions import PluginException
from util import Util
from unittest.mock import patch
from parameterized import parameterized
from jsonschema import validate


class TestViewMachine(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(ViewMachine())

    @parameterized.expand(
        [
            [
                "Success",
                Util.read_file_to_dict("input/view_machine_success.json.inp"),
                Util.read_file_to_dict("expected/view_machine_success.json.exp"),
            ],
        ]
    )
    @patch("requests.request", side_effect=Util.mock_request)
    def test_view_machine(self, test_name, input, expected, mock_request):
        actual = self.action.run(input)
        self.assertEqual(expected, actual)
        validate(actual, ViewMachineOutput.schema)

    @parameterized.expand(
        [
            [
                "400",
                Util.read_file_to_dict("input/view_machine_400.json.inp"),
                "The server is unable to process the request.",
                "Verify your plugin input is correct and not malformed and try again. If the issue persists, "
                "please contact support.",
                "{}",
            ],
            [
                "401",
                Util.read_file_to_dict("input/view_machine_401.json.inp"),
                "The account configured in your connection is unauthorized to access this service.",
                "Verify the permissions for your account and try again.",
                "{}",
            ],
            [
                "403",
                Util.read_file_to_dict("input/view_machine_403.json.inp"),
                "Invalid API key provided.",
                "Verify your API key configured in your connection is correct.",
                "{}",
            ],
            [
                "404",
                Util.read_file_to_dict("input/view_machine_404.json.inp"),
                "Invalid or unreachable endpoint provided.",
                "Verify the URLs or endpoints in your configuration are correct.",
                "{}",
            ],
            [
                "418",
                Util.read_file_to_dict("input/view_machine_418.json.inp"),
                "Something unexpected occurred.",
                "Check the logs and if the issue persists please contact support.",
                "{}",
            ],
            [
                "500",
                Util.read_file_to_dict("input/view_machine_500.json.inp"),
                "Server error occurred",
                "Verify your plugin connection inputs are correct and not malformed and try again. If the issue persists, please contact support.",
                "{}",
            ],
        ]
    )
    @patch("requests.request", side_effect=Util.mock_request)
    def test_view_machines_error(self, test_name, input_params, cause, assistance, data, mock_request):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_params)
        self.assertEqual(cause, error.exception.cause)
        self.assertEqual(assistance, error.exception.assistance)
        self.assertEqual(data, error.exception.data)
