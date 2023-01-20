import sys
import os
from unittest import TestCase
from unittest.mock import patch

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))

from unit_test.util import Util
from parameterized import parameterized
from icon_rdap.actions.ipLookup import IpLookup


@patch("requests.request", side_effect=Util.mock_request)
class TestIpLookup(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = IpLookup()

    @parameterized.expand(
        [
            [
                "existing_ip_address_no_asn",
                Util.read_file_to_dict("inputs/ip_lookup.json.inp"),
                Util.read_file_to_dict("expected/ip_lookup.json.exp"),
            ],
            [
                "existing_ip_address_with_asn",
                Util.read_file_to_dict("inputs/ip_lookup_with_asn.json.inp"),
                Util.read_file_to_dict("expected/ip_lookup_with_asn.json.exp"),
            ],
        ]
    )
    @patch("icon_rdap.util.ipwhois_lookup.IPWhoisLookup.perform_lookup_rdap", side_effect=Util.mock_rdap_lookup)
    def test_ip_lookup(self, test_name, input_params, expected, mock_rdap_lookup, mock_request):
        actual = self.action.run(input_params)
        self.assertDictEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "ip_not_found",
                Util.read_file_to_dict("inputs/ip_lookup_not_found.json.inp"),
                "Resource not found.",
                "Verify your plugin input is correct and not malformed and try again. If the issue persists, please contact support.",
            ],
            [
                "invalid_ip_address",
                Util.read_file_to_dict("inputs/ip_lookup_bad.json.inp"),
                "The server is unable to process the request.",
                "Verify your plugin input is correct and not malformed and try again. If the issue persists, please contact support.",
            ],
            [
                "ip_not_found_with_asn_requested",
                Util.read_file_to_dict("inputs/ip_lookup_with_asn_not_found.json.inp"),
                "Resource not found.",
                "Verify your plugin input is correct and not malformed and try again. If the issue persists, please contact support.",
            ],
            [
                "invalid_ip_address_with_asn_requested",
                Util.read_file_to_dict("inputs/ip_lookup_with_asn_bad.json.inp"),
                "The server is unable to process the request.",
                "Verify your plugin input is correct and not malformed and try again. If the issue persists, please contact support.",
            ],
        ]
    )
    def test_ip_lookup_raise_exception(self, mock_request, test_name, input_parameters, cause, assistance):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_parameters)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
