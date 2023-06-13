import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_duo_admin.actions.get_logs import GetLogs
from util import Util
from unittest.mock import patch
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException
from komand_duo_admin.util.constants import Cause, Assistance, PossibleInputs


@patch("requests.request", side_effect=Util.mock_request)
class TestGetLogs(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetLogs())

    @parameterized.expand(
        [
            [
                "found",
                Util.read_file_to_dict("inputs/get_auth_logs.json.inp"),
                Util.read_file_to_dict("expected/get_auth_logs.json.exp"),
            ],
            [
                "found_2",
                Util.read_file_to_dict("inputs/get_auth_logs_2.json.inp"),
                Util.read_file_to_dict("expected/get_auth_logs_2.json.exp"),
            ],
            [
                "empty",
                Util.read_file_to_dict("inputs/get_auth_logs_empty.json.inp"),
                Util.read_file_to_dict("expected/get_auth_logs_empty.json.exp"),
            ],
        ]
    )
    def test_get_logs(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertDictEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "invalid_input",
                Util.read_file_to_dict("inputs/get_auth_logs_invalid_input.json.inp"),
                Cause.INVALID_INPUT,
                Assistance.INVALID_INPUT.format(given_input="invalid", possible_inputs=PossibleInputs.possible_results),
            ]
        ]
    )
    def test_get_logs_raise_plugin_exception(self, mock_request, test_name, input_parameters, cause, assistance):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_parameters)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
