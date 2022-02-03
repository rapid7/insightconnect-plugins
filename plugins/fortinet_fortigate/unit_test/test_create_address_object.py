import sys
import os

from unittest import TestCase
from icon_fortinet_fortigate.actions.create_address_object import CreateAddressObject
from icon_fortinet_fortigate.actions.create_address_object.schema import Input, Output
from unit_test.util import Util
from unittest.mock import patch
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))


@patch("requests.Session.request", side_effect=Util.mocked_requests)
class TestCreateAddressObject(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(CreateAddressObject())

    @parameterized.expand(
        [
            [
                "create_object_ipv4",
                "1.1.1.1",
                "1.1.1.1",
                [],
                True,
                {
                    "success": True,
                    "response_object": {
                        "http_method": "POST",
                        "revision": "7740a1424b9e690e459c37fa209ab309",
                        "revision_changed": True,
                        "old_revision": "99faf4ed01eaa2e9ea2a0939b468c1df",
                        "mkey": "1.1.1.1",
                        "status": "success",
                        "http_status": 200,
                        "vdom": "root",
                        "path": "firewall",
                        "name": "address",
                        "serial": "FGVM02TM20001791",
                        "version": "v6.2.3",
                        "build": 1066,
                    },
                },
            ],
            [
                "create_object_ipv6",
                "1111:2222:3333:4444:5555:6666:7777:8888",
                "1111:2222:3333:4444:5555:6666:7777:8888",
                [],
                True,
                {
                    "success": True,
                    "response_object": {
                        "http_method": "POST",
                        "revision": "135705de48dac5b8417e4b95176c59c4",
                        "revision_changed": True,
                        "old_revision": "f922dec65c043c7e1e196e2e99d67bf8",
                        "mkey": "1111:2222:3333:4444:5555:6666:7777:8888",
                        "status": "success",
                        "http_status": 200,
                        "vdom": "root",
                        "path": "firewall",
                        "name": "address6",
                        "serial": "FGVM02TM20001791",
                        "version": "v6.2.3",
                        "build": 1066,
                    },
                },
            ],
            [
                "create_object_domain",
                "example.com",
                "example.com",
                [],
                True,
                {
                    "success": True,
                    "response_object": {
                        "http_method": "POST",
                        "revision": "47de64fb6bbc46f7e42e9d7c0046fe61",
                        "revision_changed": True,
                        "old_revision": "b9b80c92ba7aa603a6539274a4e03820",
                        "mkey": "example.com",
                        "status": "success",
                        "http_status": 200,
                        "vdom": "root",
                        "path": "firewall",
                        "name": "address",
                        "serial": "FGVM02TM20001791",
                        "version": "v6.2.3",
                        "build": 1066,
                    },
                },
            ],
            [
                "create_object_without_address_name",
                "example.com",
                None,
                [],
                True,
                {
                    "success": True,
                    "response_object": {
                        "http_method": "POST",
                        "revision": "47de64fb6bbc46f7e42e9d7c0046fe61",
                        "revision_changed": True,
                        "old_revision": "b9b80c92ba7aa603a6539274a4e03820",
                        "mkey": "example.com",
                        "status": "success",
                        "http_status": 200,
                        "vdom": "root",
                        "path": "firewall",
                        "name": "address",
                        "serial": "FGVM02TM20001791",
                        "version": "v6.2.3",
                        "build": 1066,
                    },
                },
            ],
            [
                "private_address",
                "192.168.0.0",
                None,
                [],
                True,
                {
                    "success": False,
                    "response_object": {
                        "message": "The IP address specified (192.168.0.0/32) is private and will be ignored as per the action configuration."
                    },
                },
            ],
            [
                "whitelisted",
                "1.1.1.1",
                None,
                ["1.1.1.1"],
                True,
                {
                    "success": False,
                    "response_object": {"message": "Host matched whitelist, skipping creating an address object."},
                },
            ],
        ]
    )
    def test_create_address_object(
        self, mock_request, name, address, address_object, whitelist, skip_rfc1918, expected
    ):
        actual = self.action.run(
            {
                Input.ADDRESS: address,
                Input.ADDRESS_OBJECT: address_object,
                Input.WHITELIST: whitelist,
                Input.SKIP_RFC1918: skip_rfc1918,
            }
        )
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "invalid_address_type",
                "invalid_address",
                None,
                [],
                True,
                "The type could not be determined for the given address: invalid_address.",
                "Please check that provided address is correct and try again.",
            ],
            [
                "already_exists",
                "2.2.2.2",
                None,
                [],
                True,
                "Internal Server Error: Internal error when processing the request.",
                "Something went wrong and the API did not provide a reason. This can happen when an object you're trying to create already exists or when an object you're trying to remove doesn't exist. If the issue persists contact support for additional assistance.",
            ],
        ]
    )
    def test_check_if_address_in_group_bad(
        self, mock_request, name, address, address_object, whitelist, skip_rfc1918, cause, assistance
    ):
        with self.assertRaises(PluginException) as e:
            self.action.run(
                {
                    Input.ADDRESS: address,
                    Input.ADDRESS_OBJECT: address_object,
                    Input.WHITELIST: whitelist,
                    Input.SKIP_RFC1918: skip_rfc1918,
                }
            )
        self.assertEqual(e.exception.cause, cause)
        self.assertEqual(e.exception.assistance, assistance)
