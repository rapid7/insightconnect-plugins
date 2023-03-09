import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_cloudflare.actions.getZoneAccessRules import GetZoneAccessRules
from unit_test.util import Util
from unittest.mock import patch
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException


@patch("requests.request", side_effect=Util.mock_request)
class TestGetZoneAccessRules(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetZoneAccessRules())

    @parameterized.expand(
        [
            [
                "all",
                Util.read_file_to_dict("inputs/get_zone_access_rules_all.json.inp"),
                Util.read_file_to_dict("expected/get_zone_access_rules_all.json.exp"),
            ],
            [
                "ip",
                Util.read_file_to_dict("inputs/get_zone_access_rules_ip.json.inp"),
                Util.read_file_to_dict("expected/get_zone_access_rules_ip.json.exp"),
            ],
            [
                "ip_range",
                Util.read_file_to_dict("inputs/get_zone_access_rules_ip_range.json.inp"),
                Util.read_file_to_dict("expected/get_zone_access_rules_ip_range.json.exp"),
            ],
            [
                "asn",
                Util.read_file_to_dict("inputs/get_zone_access_rules_asn.json.inp"),
                Util.read_file_to_dict("expected/get_zone_access_rules_asn.json.exp"),
            ],
            [
                "country",
                Util.read_file_to_dict("inputs/get_zone_access_rules_country.json.inp"),
                Util.read_file_to_dict("expected/get_zone_access_rules_country.json.exp"),
            ],
            [
                "empty",
                Util.read_file_to_dict("inputs/get_zone_access_rules_empty.json.inp"),
                Util.read_file_to_dict("expected/get_zone_access_rules_empty.json.exp"),
            ],
        ]
    )
    def test_get_zone_access_rules(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "invalid_zone_id",
                Util.read_file_to_dict("inputs/get_zone_access_rules_invalid_zone_id.json.inp"),
                "Resource not found.",
                "Verify your input is correct and not malformed and try again. If the issue persists, please contact support.",
            ]
        ]
    )
    def test_get_zone_access_rules_bad(self, mock_request, test_name, input_parameters, cause, assistance):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_parameters)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
