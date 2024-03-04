import sys
import os

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_anomali_threatstream.actions.get_observables import GetObservables
from util import Util
from unittest.mock import patch
from parameterized import parameterized


@patch("requests.Session.send", side_effect=Util.mock_request)
class TestGetObservables(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetObservables())


    @parameterized.expand(
        [
            [
                "Success",
                Util.read_file_to_dict("inputs/get_observables_success.json.inp"),
                Util.read_file_to_dict("expected/get_observables_success.json.exp"),
            ],
        ]
    )
    def test_get_observables(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertEqual(expected, actual)

    @parameterized.expand(
        [
            [
                "400",
                Util.read_file_to_dict("inputs/get_observables_400.json.inp"),
                "The server is unable to process the request.",
                "Verify your plugin input is correct and not malformed and try again. If the issue persists, "
                "please contact support.",
                "{}"
            ],
            [
                "401",
                Util.read_file_to_dict("inputs/get_observables_401.json.inp"),
                "Invalid username or password provided.",
                "Verify your username and password are correct.",
                "{}"
            ],
            [
                "403",
                Util.read_file_to_dict("inputs/get_observables_403.json.inp"),
                "Invalid API key provided.",
                "Verify your API key configured in your connection is correct.",
                "{}"
            ],
            [
                "404",
                Util.read_file_to_dict("inputs/get_observables_404.json.inp"),
                "Invalid or unreachable endpoint provided.",
                "Verify the URLs or endpoints in your configuration are correct.",
                "{}"
            ],
            [
                "409",
                Util.read_file_to_dict("inputs/get_observables_409.json.inp"),
                "Something unexpected occurred.",
                "Check the logs and if the issue persists please contact support.",
                "{}"
            ],
            [
                "500",
                Util.read_file_to_dict("inputs/get_observables_500.json.inp"),
                "Server error occurred",
                "Verify your plugin connection inputs are correct and not malformed and try again. If the issue persists, please contact support.",
                "{}"
            ],
        ]
    )
    def test_get_observables(self, mock_request, test_name, input_params, cause, assistance, data):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_params)
        self.assertEqual(cause, error.exception.cause)
        self.assertEqual(assistance, error.exception.assistance)
        self.assertEqual(data, error.exception.data)
