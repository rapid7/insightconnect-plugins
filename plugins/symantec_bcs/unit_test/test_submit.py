import sys
import os

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath('../'))

from unittest import TestCase
from komand_symantec_bcs.actions.submit import Submit
from komand_symantec_bcs.actions.submit.schema import SubmitOutput
from util import Util
from unittest.mock import patch
from parameterized import parameterized
from jsonschema import validate

class TestSubmit(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Submit()

    @parameterized.expand(
        [
            [
                "Success",
                Util.read_file_to_dict("input/submit_success.json.inp"),
                Util.read_file_to_dict("expected/submit_success.json.exp"),
            ],
        ]
    )
    @patch("requests.post", side_effect=Util.mock_request)
    def test_submit(self, test_name, input, expected, mock_request):
        actual = self.action.run(input)
        self.assertEqual(expected, actual)
        validate(actual, SubmitOutput.schema)

    @parameterized.expand(
        [
            [
                "400",
                Util.read_file_to_dict("input/submit_400.json.inp"),
                "HTTP error occurred",
                "Error: 400"
            ],
            [
                "ConnectionError",
                Util.read_file_to_dict("input/submit_connection.json.inp"),
                "A network problem occurred",
                "Error: ConnectionError"
            ],
            [
                "Timeout",
                Util.read_file_to_dict("input/submit_timeout.json.inp"),
                "timeout",
                "Error: Timeout"
            ],
            [
                "TooManyRedirects",
                Util.read_file_to_dict("input/submit_redirect.json.inp"),
                "Too many redirects!",
                "Error: TooManyRedirects"
            ]
        ]
    )
    @patch("requests.post", side_effect=Util.mock_request)
    def test_submit_error(self, test_name, input_params, cause, assistance, mock_request):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_params)
        self.assertEqual(cause, error.exception.cause)
        self.assertEqual(assistance, error.exception.assistance)
