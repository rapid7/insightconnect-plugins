import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_cloudflare.actions.createZoneAccessRule import CreateZoneAccessRule
from unit_test.util import Util
from unittest.mock import patch
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException


@patch("requests.request", side_effect=Util.mock_request)
class TestCreateZoneAccessRule(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(CreateZoneAccessRule())

    @parameterized.expand(
        [
            [
                "ipv4",
                Util.read_file_to_dict("inputs/create_zone_access_rule_ipv4.json.inp"),
                Util.read_file_to_dict("expected/create_zone_access_rule_ipv4.json.exp"),
            ],
            [
                "ipv6",
                Util.read_file_to_dict("inputs/create_zone_access_rule_ipv6.json.inp"),
                Util.read_file_to_dict("expected/create_zone_access_rule_ipv6.json.exp"),
            ],
            [
                "ipv4_range",
                Util.read_file_to_dict("inputs/create_zone_access_rule_ipv4_range.json.inp"),
                Util.read_file_to_dict("expected/create_zone_access_rule_ipv4_range.json.exp"),
            ],
            [
                "ipv6_range",
                Util.read_file_to_dict("inputs/create_zone_access_rule_ipv6_range.json.inp"),
                Util.read_file_to_dict("expected/create_zone_access_rule_ipv6_range.json.exp"),
            ],
            [
                "asn",
                Util.read_file_to_dict("inputs/create_zone_access_rule_asn.json.inp"),
                Util.read_file_to_dict("expected/create_zone_access_rule_asn.json.exp"),
            ],
            [
                "country",
                Util.read_file_to_dict("inputs/create_zone_access_rule_country.json.inp"),
                Util.read_file_to_dict("expected/create_zone_access_rule_country.json.exp"),
            ],
        ]
    )
    def test_create_zone_access_rule(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "invalid_zone_id",
                Util.read_file_to_dict("inputs/create_zone_access_rule_invalid_zone_id.json.inp"),
                "Resource not found.",
                "Verify your input is correct and not malformed and try again. If the issue persists, please contact support.",
            ],
            [
                "invalid_target",
                Util.read_file_to_dict("inputs/create_zone_access_rule_invalid_target.json.inp"),
                "Invalid target was provided: invalid_target.",
                "Only IPv4, IPv6, IP range, AS number and two-letter ISO-3166-1 alpha-2 country code are supported. For IP ranges, you can only use prefix lengths /16 and /24 for IPv4 ranges, and prefix lengths /32, /48, and /64 for IPv6 ranges.",
            ],
        ]
    )
    def test_create_zone_access_rule_bad(self, mock_request, test_name, input_parameters, cause, assistance):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_parameters)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
