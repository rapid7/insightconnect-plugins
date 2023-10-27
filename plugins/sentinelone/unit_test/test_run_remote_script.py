import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from komand_sentinelone.actions.run_remote_script import RunRemoteScript
from util import Util
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException


@patch("requests.request", side_effect=Util.mocked_requests_get)
class TestRunRemoteScript(TestCase):
    @classmethod
    @patch("requests.post", side_effect=Util.mocked_requests_get)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(RunRemoteScript())

    @parameterized.expand(
        [
            [
                "success",
                Util.read_file_to_dict("inputs/run_remote_script.json.inp"),
                Util.read_file_to_dict("expected/affected_2.json.exp"),
            ],
            [
                "success_2",
                Util.read_file_to_dict("inputs/run_remote_script_2.json.inp"),
                Util.read_file_to_dict("expected/affected.json.exp"),
            ],
            [
                "success_3",
                Util.read_file_to_dict("inputs/run_remote_script_3.json.inp"),
                Util.read_file_to_dict("expected/affected.json.exp"),
            ],
        ]
    )
    def test_run_remote_script(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertEqual(expected, actual)

    @parameterized.expand(
        [
            [
                "without_output_directory",
                Util.read_file_to_dict("inputs/run_remote_script_without_output_directory.json.inp"),
                "Local output destination selected but no output directory provided.",
                "Please provide an output directory.",
            ],
            [
                "invalid_password",
                Util.read_file_to_dict("inputs/run_remote_script_invalid_password.json.inp"),
                "Invalid password.",
                "The password must be 10 or more characters with a mix of upper and lower case letters, numbers, and "
                "symbols.",
            ],
        ]
    )
    def test_run_remote_script_raise_exception(self, mock_request, test_name, input_params, cause, assistance):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_params)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
