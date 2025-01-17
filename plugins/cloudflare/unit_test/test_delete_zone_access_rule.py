import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_cloudflare.actions.deleteZoneAccessRule import DeleteZoneAccessRule
from util import Util
from unittest.mock import patch
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException


@patch("requests.request", side_effect=Util.mock_request)
class TestDeleteZoneAccessRule(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(DeleteZoneAccessRule())

    @parameterized.expand(
        [
            [
                "success",
                Util.read_file_to_dict("inputs/delete_zone_access_rule.json.inp"),
                Util.read_file_to_dict("expected/delete_zone_access_rule.json.exp"),
            ]
        ]
    )
    def test_delete_zone_access_rule(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "invalid_zone_id",
                Util.read_file_to_dict("inputs/delete_zone_access_rule_invalid_zone_id.json.inp"),
                "Resource not found.",
                "Verify your input is correct and not malformed and try again. If the issue persists, please contact support.",
            ],
            [
                "invalid_rule_id",
                Util.read_file_to_dict("inputs/delete_zone_access_rule_invalid_rule_id.json.inp"),
                "Resource not found.",
                "Verify your input is correct and not malformed and try again. If the issue persists, please contact support.",
            ],
        ]
    )
    def test_delete_zone_access_rule_bad(self, mock_request, test_name, input_parameters, cause, assistance):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_parameters)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
