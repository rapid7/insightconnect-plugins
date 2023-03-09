import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException
from icon_cloudflare.util.helpers import clean, convert_dict_keys_to_camel_case, set_configuration


class TestHelpers(TestCase):
    @parameterized.expand(
        [
            ["empty_dict", {}, {}],
            [
                "clean_dict",
                {
                    "key": "value",
                    "next": {"key_in_value": [9, 8, 7, 6, 5, 4], "id": "908"},
                    "id": 2,
                },
                {
                    "key": "value",
                    "next": {"key_in_value": [9, 8, 7, 6, 5, 4], "id": "908"},
                    "id": 2,
                },
            ],
            [
                "to_be_cleaned",
                {
                    "key": "value",
                    "next": {"key_in_value": [], "request_i": "123", "none": None},
                    "team": {"id": 1234, "name": "John"},
                    "empty_string": "",
                    "number": 0,
                },
                {"key": "value", "next": {"request_i": "123"}, "team": {"id": 1234, "name": "John"}},
            ],
        ]
    )
    def test_clean(self, test_name, input_params, expected):
        actual = clean(input_params)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "1",
                [
                    {"example_key": "example_value", "another_example_key": 12345, "key": "value"},
                    {
                        "example_key": [{"test_key": "value"}],
                        "another_example_key": 12345,
                        "key": {"example_key": "example_value"},
                    },
                ],
                [
                    {"exampleKey": "example_value", "anotherExampleKey": 12345, "key": "value"},
                    {
                        "exampleKey": [{"testKey": "value"}],
                        "anotherExampleKey": 12345,
                        "key": {"exampleKey": "example_value"},
                    },
                ],
            ]
        ]
    )
    def test_convert_dict_keys_to_camel_case(self, test_name, input_params, expected):
        actual = convert_dict_keys_to_camel_case(input_params)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            ["ipv4", "198.51.100.1", {"target": "ip", "value": "198.51.100.1"}],
            ["ipv6", "2001:db8:1:1:1:1:1:1", {"target": "ip6", "value": "2001:db8:1:1:1:1:1:1"}],
            ["ipv4_range", "198.51.100.1/16", {"target": "ip_range", "value": "198.51.100.1/16"}],
            ["ipv6_range", "2001:db8:1:1:1:1:1:1/48", {"target": "ip_range", "value": "2001:db8:1:1:1:1:1:1/48"}],
            ["asn", "as12345", {"target": "asn", "value": "as12345"}],
            ["country", "GB", {"target": "country", "value": "GB"}],
        ]
    )
    def test_set_configuration(self, test_name, input_params, expected):
        actual = set_configuration(input_params)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "invalid_ipv4_range",
                "198.51.100.1/10",
                "Invalid target was provided: 198.51.100.1/10.",
                "Only IPv4, IPv6, IP range, AS number and two-letter ISO-3166-1 alpha-2 country code are supported. For IP ranges, you can only use prefix lengths /16 and /24 for IPv4 ranges, and prefix lengths /32, /48, and /64 for IPv6 ranges.",
            ],
            [
                "invalid_ipv6_range",
                "2001:db8:1:1:1:1:1:1/30",
                "Invalid target was provided: 2001:db8:1:1:1:1:1:1/30.",
                "Only IPv4, IPv6, IP range, AS number and two-letter ISO-3166-1 alpha-2 country code are supported. For IP ranges, you can only use prefix lengths /16 and /24 for IPv4 ranges, and prefix lengths /32, /48, and /64 for IPv6 ranges.",
            ],
            [
                "invalid_target",
                "invalid_target",
                "Invalid target was provided: invalid_target.",
                "Only IPv4, IPv6, IP range, AS number and two-letter ISO-3166-1 alpha-2 country code are supported. For IP ranges, you can only use prefix lengths /16 and /24 for IPv4 ranges, and prefix lengths /32, /48, and /64 for IPv6 ranges.",
            ],
        ]
    )
    def test_set_configuration_bad(self, test_name, input_parameters, cause, assistance):
        with self.assertRaises(PluginException) as error:
            set_configuration(input_parameters)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
