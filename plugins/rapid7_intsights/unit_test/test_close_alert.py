import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from unit_test.util import Util
from parameterized import parameterized
from icon_rapid7_intsights.actions.close_alert import CloseAlert
from insightconnect_plugin_runtime.exceptions import PluginException


@patch("requests.request", side_effect=Util.mock_request)
class TestCloseAlert(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(CloseAlert())

    @parameterized.expand(
        [
            [
                "false_positive",
                Util.read_file_to_dict("inputs/close_alert.json.inp"),
                Util.read_file_to_dict("expecteds/success.json.exp"),
            ],
            [
                "problem_solved",
                Util.read_file_to_dict("inputs/close_alert2.json.inp"),
                Util.read_file_to_dict("expecteds/success.json.exp"),
            ],
            [
                "informational_only",
                Util.read_file_to_dict("inputs/close_alert3.json.inp"),
                Util.read_file_to_dict("expecteds/success.json.exp"),
            ],
            [
                "not_related",
                Util.read_file_to_dict("inputs/close_alert4.json.inp"),
                Util.read_file_to_dict("expecteds/success.json.exp"),
            ],
        ]
    )
    def test_close_alert(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "invalid_id",
                Util.read_file_to_dict("inputs/close_alert_bad.json.inp"),
                "The server is unable to process the request.",
                "Verify your plugin input is correct and not malformed and try again. If the issue persists, please contact support.",
            ]
        ]
    )
    def test_close_alert_bad(self, mock_request, test_name, input_parameters, cause, assistance):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_parameters)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
