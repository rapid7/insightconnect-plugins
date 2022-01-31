import sys
import os

from unittest import TestCase
from icon_fortinet_fortigate.actions.add_address_object_to_address_group import AddAddressObjectToAddressGroup
from icon_fortinet_fortigate.actions.add_address_object_to_address_group.schema import Input, Output
from unit_test.util import Util
from unittest.mock import patch
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))


@patch("requests.Session.request", side_effect=Util.mocked_requests)
class TestAddAddressObjectToAddressGroup(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(AddAddressObjectToAddressGroup())

    @parameterized.expand(
        [
            [
                "add_address_ipv4",
                "1.1.1.1",
                "Address Object Group",
                "IPv6 Address Object Group",
                {
                    "result_object": {
                        "build": 1066,
                        "http_method": "PUT",
                        "http_status": 200,
                        "mkey": "Address Object Group",
                        "name": "addrgrp",
                        "old_revision": "24672d1fabce76df50acf6442f2109c0",
                        "path": "firewall",
                        "revision": "30b53592bb7296648e9dd4b2233e9ff3",
                        "revision_changed": True,
                        "serial": "FGVM02TM20001791",
                        "status": "success",
                        "vdom": "root",
                        "version": "v6.2.3",
                    },
                    "success": True,
                },
            ],
            [
                "add_address_domain",
                "test.com",
                "Address Object Group",
                "IPv6 Address Object Group",
                {
                    "result_object": {
                        "build": 1066,
                        "http_method": "PUT",
                        "http_status": 200,
                        "mkey": "Address Object Group",
                        "name": "addrgrp",
                        "old_revision": "24672d1fabce76df50acf6442f2109c0",
                        "path": "firewall",
                        "revision": "30b53592bb7296648e9dd4b2233e9ff3",
                        "revision_changed": True,
                        "serial": "FGVM02TM20001791",
                        "status": "success",
                        "vdom": "root",
                        "version": "v6.2.3",
                    },
                    "success": True,
                },
            ],
            [
                "add_address_ipv6",
                "1111:2222:3333:4444:5555:6666:7777:8888",
                "Address Object Group",
                "IPv6 Address Object Group",
                {
                    "result_object": {
                        "http_method": "PUT",
                        "revision": "4e94295089e615016db1d22229f011a5",
                        "revision_changed": True,
                        "old_revision": "d1464c520d6e938fe64062f4f057dc4f",
                        "mkey": "IPv6 Address Object Group",
                        "status": "success",
                        "http_status": 200,
                        "vdom": "root",
                        "path": "firewall",
                        "name": "addrgrp6",
                        "serial": "FGVM02TM20001791",
                        "version": "v6.2.3",
                        "build": 1066,
                    },
                    "success": True,
                },
            ],
        ]
    )
    def test_add_address_object_to_address_group(self, mock_request, name, address, group, ipv6_group, expected):
        actual = self.action.run({Input.GROUP: group, Input.IPV6_GROUP: ipv6_group, Input.ADDRESS_OBJECT: address})
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "address_object_not_found",
                "invalid_object",
                "Address Object Group",
                "IPv6 Address Object Group",
                "Resource Not Found: Unable to find the specified resource.",
                "Data was requested but not found. Check that inputs are correct.",
                'Response was: {"message": "Not Found"}',
            ],
            [
                "address_group_not_found",
                "1.1.1.1",
                "Invalid Group",
                "IPv6 Address Object Group",
                "Resource Not Found: Unable to find the specified resource.",
                "Data was requested but not found. Check that inputs are correct.",
                'Response was: {"message": "Not Found"}',
            ],
        ]
    )
    def test_add_address_object_to_address_group_bad(
        self, mock_request, name, address, group, ipv6_group, cause, assistance, data
    ):
        with self.assertRaises(PluginException) as e:
            self.action.run({Input.GROUP: group, Input.IPV6_GROUP: ipv6_group, Input.ADDRESS_OBJECT: address})
        self.assertEqual(e.exception.cause, cause)
        self.assertEqual(e.exception.assistance, assistance)
        self.assertEqual(e.exception.data, data)
