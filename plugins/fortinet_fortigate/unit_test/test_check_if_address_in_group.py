import sys
import os

from unittest import TestCase
from icon_fortinet_fortigate.actions.check_if_address_in_group import CheckIfAddressInGroup
from icon_fortinet_fortigate.actions.check_if_address_in_group.schema import Input, Output
from unit_test.util import Util
from unittest.mock import patch
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))


@patch("requests.Session.request", side_effect=Util.mocked_requests)
class TestCheckIfAddressInGroup(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(CheckIfAddressInGroup())

    @parameterized.expand(
        [
            [
                "check_object_ipv4",
                "1.1.1.1",
                "Address Object Group",
                "IPv6 Address Object Group",
                True,
                {"found": True, "address_objects": ["1.1.1.1/32"]},
            ],
            [
                "check_object_domain",
                "example.com",
                "Address Object Group",
                "IPv6 Address Object Group",
                True,
                {"found": True, "address_objects": ["example.com"]},
            ],
            [
                "check_object_ipv6",
                "1111:2222:3333:4444:5555:6666:7777:8888",
                "Address Object Group",
                "IPv6 Address Object Group",
                True,
                {"found": True, "address_objects": ["1111:2222:3333:4444:5555:6666:7777:8888/128"]},
            ],
            [
                "check_object_ipv4_without_search",
                "1.1.1.1",
                "Address Object Group",
                "IPv6 Address Object Group",
                False,
                {"found": True, "address_objects": ["1.1.1.1"]},
            ],
            [
                "check_object_domain_without_search",
                "example.com",
                "Address Object Group",
                "IPv6 Address Object Group",
                False,
                {"found": True, "address_objects": ["example.com"]},
            ],
            [
                "check_object_ipv6_without_search",
                "1111:2222:3333:4444:5555:6666:7777:8888",
                "Address Object Group",
                "IPv6 Address Object Group",
                False,
                {"found": True, "address_objects": ["1111:2222:3333:4444:5555:6666:7777:8888"]},
            ],
            [
                "check_object_not_found",
                "Invalid Object",
                "Address Object Group",
                "IPv6 Address Object Group",
                True,
                {"found": False, "address_objects": []},
            ],
            [
                "check_object_not_found2",
                "Invalid Object",
                "Address Object Group",
                "IPv6 Address Object Group",
                False,
                {"found": False, "address_objects": []},
            ],
        ]
    )
    def test_check_if_address_in_group(self, mock_request, name, address, group, ipv6_group, enable_search, expected):
        actual = self.action.run(
            {
                Input.GROUP: group,
                Input.IPV6_GROUP: ipv6_group,
                Input.ADDRESS: address,
                Input.ENABLE_SEARCH: enable_search,
            }
        )
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "address_group_not_found",
                "1.1.1.1",
                "Invalid Group",
                "IPv6 Address Object Group",
                True,
                "Resource Not Found: Unable to find the specified resource.",
                "Data was requested but not found. Check that inputs are correct.",
                'Response was: {"message": "Not Found"}',
            ],
        ]
    )
    def test_check_if_address_in_group_bad(
        self, mock_request, name, address, group, ipv6_group, enable_search, cause, assistance, data
    ):
        with self.assertRaises(PluginException) as e:
            self.action.run(
                {
                    Input.GROUP: group,
                    Input.IPV6_GROUP: ipv6_group,
                    Input.ADDRESS: address,
                    Input.ENABLE_SEARCH: enable_search,
                }
            )
        self.assertEqual(e.exception.cause, cause)
        self.assertEqual(e.exception.assistance, assistance)
        self.assertEqual(e.exception.data, data)
