import os
import sys

sys.path.append(os.path.abspath("../"))
from unittest import TestCase
from unittest.mock import patch, MagicMock

from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate
from komand_palo_alto_pan_os.actions.set_address_object import SetAddressObject
from komand_palo_alto_pan_os.actions.set_address_object.schema import (
    Input,
    SetAddressObjectInput,
    SetAddressObjectOutput,
)
from parameterized import parameterized

from util import Util


@patch("requests.sessions.Session.get", side_effect=Util.mocked_requests)
@patch("requests.sessions.Session.post", side_effect=Util.mocked_requests)
class TestSetAddressObject(TestCase):
    @parameterized.expand(
        [
            [
                "domain",
                "example.com",
                "Domain",
                "Test",
                "test",
                False,
                [],
                {"message": "command succeeded", "status": "success", "code": "20"},
            ],
            [
                "domain_whitelisted",
                "example.com",
                "Domain Whitelisted",
                "Test",
                "test",
                False,
                ["example.com"],
                {"message": "Address object matched whitelist.", "status": "error", "code": ""},
            ],
            [
                "ipv4",
                "198.51.100.1",
                "IPv4",
                "Test",
                "test",
                False,
                [],
                {"message": "command succeeded", "status": "success", "code": "20"},
            ],
            [
                "ipv4_cidr",
                "198.51.100.1/32",
                "IPv4 CIDR",
                "Test",
                "test",
                False,
                [],
                {"message": "command succeeded", "status": "success", "code": "20"},
            ],
            [
                "ipv4_range",
                "198.51.100.1-198.51.100.2",
                "IPv4 Range",
                "Test",
                "test",
                False,
                [],
                {"message": "command succeeded", "status": "success", "code": "20"},
            ],
            [
                "ipv4_private",
                "192.168.0.0",
                "IPv4 Private",
                "Test",
                "test",
                True,
                [],
                {"message": "Address object was RFC 1918 (private).", "status": "error", "code": ""},
            ],
            [
                "ipv4_whitelisted",
                "198.51.100.1",
                "IPv4 Whitelisted",
                "Test",
                "test",
                False,
                ["198.51.100.1"],
                {"message": "Address object matched whitelist.", "status": "error", "code": ""},
            ],
            [
                "ipv6",
                "abcd:123:4::1",
                "IPv6",
                "Test",
                "test",
                False,
                [],
                {"message": "command succeeded", "status": "success", "code": "20"},
            ],
            [
                "ipv6_cidr",
                "abcd:123:4::1/128",
                "IPv6 CIDR",
                "Test",
                "test",
                False,
                [],
                {"message": "command succeeded", "status": "success", "code": "20"},
            ],
            [
                "ipv6_range",
                "abcd:123:4::1-abcd:123:4::2",
                "IPv6 Range",
                "Test",
                "test",
                False,
                [],
                {"message": "command succeeded", "status": "success", "code": "20"},
            ],
            [
                "ipv6_private",
                "fd12:3456:789a:1::1",
                "IPv6 Private",
                "Test",
                "test",
                True,
                [],
                {"message": "Address object was RFC 1918 (private).", "status": "error", "code": ""},
            ],
            [
                "ipv6_whitelisted",
                "abcd:123:4::1",
                "IPv6 Whitelisted",
                "Test",
                "test",
                False,
                ["abcd:123:4::1"],
                {"message": "Address object matched whitelist.", "status": "error", "code": ""},
            ],
        ]
    )
    def test_set_address_object(
        self,
        mock_get: MagicMock,
        mock_post: MagicMock,
        name: str,
        address: str,
        address_object: str,
        description: str,
        tags: str,
        skip_rfc1918: bool,
        whitelist: list,
        expected: dict,
    ) -> None:
        action = Util.default_connector(SetAddressObject())
        input_data = {
            Input.ADDRESS: address,
            Input.ADDRESS_OBJECT: address_object,
            Input.DESCRIPTION: description,
            Input.TAGS: tags,
            Input.SKIP_RFC1918: skip_rfc1918,
            Input.WHITELIST: whitelist,
        }
        validate(input_data, SetAddressObjectInput.schema)
        actual = action.run(input_data)
        self.assertEqual(actual, expected)
        validate(actual, SetAddressObjectOutput.schema)

    @parameterized.expand(
        [
            [
                "invalid_address",
                "test",
                "Invalid Address",
                "Test",
                "test",
                False,
                [],
                "Unable to determine type for the given address: test.",
                "Please provide a valid address.",
            ],
        ]
    )
    def test_set_address_object_bad(
        self,
        mock_get: MagicMock,
        mock_post: MagicMock,
        name: str,
        address: str,
        address_object: str,
        description: str,
        tags: str,
        skip_rfc1918: bool,
        whitelist: list,
        cause: str,
        assistance: str,
    ) -> None:
        action = Util.default_connector(SetAddressObject())
        input_data = {
            Input.ADDRESS: address,
            Input.ADDRESS_OBJECT: address_object,
            Input.DESCRIPTION: description,
            Input.TAGS: tags,
            Input.SKIP_RFC1918: skip_rfc1918,
            Input.WHITELIST: whitelist,
        }
        validate(input_data, SetAddressObjectInput.schema)
        with self.assertRaises(PluginException) as e:
            action.run(input_data)
        self.assertEqual(e.exception.cause, cause)
        self.assertEqual(e.exception.assistance, assistance)

    def test_in_whitelist(self, mock_get: MagicMock, mock_post: MagicMock) -> None:
        test_action = SetAddressObject()

        self.assertTrue(test_action.match_whitelist("1.1.1.1", ["1.1.1.1/32"], "ip-netmask"))
        self.assertTrue(test_action.match_whitelist("1.1.1.1/32", ["1.1.1.1/32"], "ip-netmask"))
        self.assertFalse(test_action.match_whitelist("1.1.1.2", ["1.1.1.1/32"], "ip-netmask"))
        self.assertTrue(
            test_action.match_whitelist("1.1.1.1", ["www.google.com", "5.5.5.5", "1.1.1.1/32"], "ip-netmask")
        )
        self.assertTrue(
            test_action.match_whitelist("www.google.com", ["www.google.com", "5.5.5.5", "1.1.1.1/32"], "fqdn")
        )
        self.assertFalse(
            test_action.match_whitelist("aadroid.net", ["www.google.com", "5.5.5.5", "1.1.1.1/32"], "fqdn")
        )
        self.assertTrue(test_action.match_whitelist("1.1.1.1", ["1.1.1.1"], "ip-range"))
        self.assertFalse(test_action.match_whitelist("1.1.1.1/24", ["1.1.1.1"], "ip-range"))

    def test_cidr_vs_cidr_in_whitelist(self, mock_get: MagicMock, mock_post: MagicMock) -> None:
        test_action = SetAddressObject()

        self.assertTrue(test_action.match_whitelist("1.1.1.1/24", ["1.1.1.1", "1.1.1.1/24"], "ip-netmask"))
        self.assertTrue(test_action.match_whitelist("1.1.1.1", ["1.1.1.1/24"], "ip-netmask"))
        self.assertFalse(test_action.match_whitelist("1.1.1.1/24", ["1.1.1.1", "1.1.1.1/32"], "ip-netmask"))

    def test_get_address_type(self, mock_get: MagicMock, mock_post: MagicMock) -> None:
        test_action = SetAddressObject()

        self.assertEqual(test_action.determine_address_type("1.1.1.1"), "ip-netmask")
        self.assertEqual(test_action.determine_address_type("1.1.1.1/32"), "ip-netmask")
        self.assertEqual(test_action.determine_address_type("www.google.com"), "fqdn")
        self.assertEqual(test_action.determine_address_type("10.1.1.1-10.1.1.255"), "ip-range")
        self.assertEqual(test_action.determine_address_type("1:2:3:4:5:6:7:8"), "ip-netmask")
        self.assertEqual(
            test_action.determine_address_type("2001:0db8:85a3:0000:0000:8a2e:0370:7334"),
            "ip-netmask",
        )

    def test_check_if_private(self, mock_get: MagicMock, mock_post: MagicMock) -> None:
        test_action = SetAddressObject()

        self.assertTrue(test_action.check_if_private("192.168.1.1"))
        self.assertTrue(test_action.check_if_private("192.168.1.1/32"))
        self.assertTrue(test_action.check_if_private("fd12:3456:789a:1aa2:22b::1"))
        self.assertTrue(test_action.check_if_private("192.168.1.1-192.168.1.100"))
        self.assertFalse(test_action.check_if_private("1.1.1.1"))
