import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_okta.actions.get_factors import GetFactors
from unit_test.util import Util
from unittest.mock import patch
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException


@patch("requests.request", side_effect=Util.mock_request)
class TestGetFactors(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetFactors())

    @parameterized.expand(
        [
            [
                "existing_user",
                Util.read_file_to_dict("inputs/get_factors_existing_user.json.inp"),
                Util.read_file_to_dict("expected/get_factors_existing_user.json.exp"),
            ],
            [
                "existing_user_without_factors",
                Util.read_file_to_dict("inputs/get_factors_existing_user_without_factors.json.inp"),
                Util.read_file_to_dict("expected/get_factors_existing_user_without_factors.json.exp"),
            ],
        ]
    )
    def test_get_factors(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertDictEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "user_not_found",
                Util.read_file_to_dict("inputs/get_factors_user_not_found.json.inp"),
                "Resource not found.",
                "Verify your input is correct and not malformed and try again. If the issue persists, please contact support.",
            ],
        ]
    )
    def test_get_factors_raise_exception(self, mock_request, test_name, input_parameters, cause, assistance):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_parameters)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
