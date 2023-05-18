import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_okta.actions.update_blacklist_zones import UpdateBlacklistZones
from unit_test.util import Util
from unittest.mock import patch
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException
from komand_okta.util.exceptions import ApiException


@patch("requests.request", side_effect=Util.mock_request)
class TestUpdateBlacklistZones(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(UpdateBlacklistZones())

    @parameterized.expand(
        [
            [
                "success",
                Util.read_file_to_dict("inputs/update_blacklist_zone.json.inp"),
                Util.read_file_to_dict("expected/update_blacklist_zone.json.exp"),
            ],
            [
                "ip_range",
                Util.read_file_to_dict("inputs/update_blacklist_zone_ip_range.json.inp"),
                Util.read_file_to_dict("expected/update_blacklist_zone.json.exp"),
            ],
            [
                "cidr",
                Util.read_file_to_dict("inputs/update_blacklist_zone_cidr.json.inp"),
                Util.read_file_to_dict("expected/update_blacklist_zone_cidr.json.exp"),
            ],
            [
                "ipv6",
                Util.read_file_to_dict("inputs/update_blacklist_zone_ipv6.json.inp"),
                Util.read_file_to_dict("expected/update_blacklist_zone_ipv6.json.exp"),
            ],
            [
                "remove_ipv4",
                Util.read_file_to_dict("inputs/update_blacklist_zone_remove_ipv4.json.inp"),
                Util.read_file_to_dict("expected/update_blacklist_zone_remove_ipv4.json.exp"),
            ],
            [
                "remove_cidr",
                Util.read_file_to_dict("inputs/update_blacklist_zone_remove_cidr.json.inp"),
                Util.read_file_to_dict("expected/update_blacklist_zone_remove_cidr.json.exp"),
            ],
        ]
    )
    def test_update_blacklist_zones(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "zone_not_found",
                Util.read_file_to_dict("inputs/update_blacklist_zone_not_found.json.inp"),
                "Name Invalid Zone does not exist in Okta zones.",
                "Please enter valid zone name and try again.",
            ],
            [
                "dynamic_zone",
                Util.read_file_to_dict("inputs/update_blacklist_zone_dynamic_zone.json.inp"),
                "Cannot perform operation on 1.1.1.1 because the provided zone 'Test Dynamic Zone' is of dynamic type.",
                "To perform the requested operation, the specified zone must be of IP type. Please check if the given zone name is correct and try again.",
            ],
            [
                "address_exists",
                Util.read_file_to_dict("inputs/update_blacklist_zone_address_exists.json.inp"),
                "The address 1.2.3.4 already exist in provided Okta zone Test IP Zone.",
                "Please enter an address that is not in the blacklist zone.",
            ],
            [
                "invalid_ip",
                Util.read_file_to_dict("inputs/update_blacklist_zone_remove_invalid_ip.json.inp"),
                "The address 2.2.2.2 does not exist in provided Okta zone Test IP Zone.",
                "Please enter an address that is blacklisted and try again.",
            ],
        ]
    )
    def test_update_blacklist_zone_bad(self, mock_request, test_name, input_parameters, cause, assistance):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_parameters)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
