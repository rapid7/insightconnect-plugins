import sys
import os

from unittest import TestCase
from icon_fortinet_fortigate.actions.get_address_objects import GetAddressObjects
from icon_fortinet_fortigate.actions.get_address_objects.schema import Input, Output
from unit_test.util import Util
from unittest.mock import patch
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))


@patch("requests.Session.request", side_effect=Util.mocked_requests)
class TestGetAddressObjects(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetAddressObjects())

    @parameterized.expand(
        [
            [
                "get_address_objects_all",
                None,
                None,
                None,
                None,
                {
                    "address_objects": [
                        {
                            "name": "test.com",
                            "q_origin_key": "test.com",
                            "uuid": "9db45558-f60d-51eb-a7f8-32bdbc2b980e",
                            "type": "fqdn",
                            "sub-type": "sdn",
                            "clearpass-spt": "unknown",
                            "start-mac": "00:00:00:00:00:00",
                            "end-mac": "00:00:00:00:00:00",
                            "fqdn": "test.com",
                            "cache-ttl": 0,
                            "fsso-group": [],
                            "visibility": "enable",
                            "color": 0,
                            "sdn-addr-type": "private",
                            "list": [],
                            "tagging": [],
                            "allow-routing": "disable",
                        },
                        {
                            "name": "1.1.1.1",
                            "q_origin_key": "1.1.1.1",
                            "uuid": "5d0cb376-025a-51eb-6130-f201926180c8",
                            "subnet": "1.1.1.1/32",
                            "type": "ipmask",
                            "sub-type": "sdn",
                            "clearpass-spt": "unknown",
                            "start-mac": "00:00:00:00:00:00",
                            "end-mac": "00:00:00:00:00:00",
                            "cache-ttl": 0,
                            "fsso-group": [],
                            "visibility": "enable",
                            "color": 0,
                            "sdn-addr-type": "private",
                            "list": [],
                            "tagging": [],
                            "allow-routing": "disable",
                        },
                    ],
                    "ipv6_address_objects": [
                        {
                            "name": "1111:2222:3333:4444:5555:6666:7777:8888",
                            "q_origin_key": "1111:2222:3333:4444:5555:6666:7777:8888",
                            "uuid": "2dfbc876-1ba2-51ec-235c-e80fafc76aeb",
                            "type": "ipprefix",
                            "ip6": "1111:2222:3333:4444:5555:6666:7777:8888/128",
                            "end-ip": "::",
                            "cache-ttl": 0,
                            "visibility": "enable",
                            "color": 0,
                            "list": [],
                            "tagging": [],
                            "subnet-segment": [],
                            "host-type": "any",
                        },
                    ],
                },
            ],
            [
                "get_address_objects_by_name",
                "1.1.1.1",
                None,
                None,
                None,
                {
                    "address_objects": [
                        {
                            "name": "1.1.1.1",
                            "q_origin_key": "1.1.1.1",
                            "uuid": "5d0cb376-025a-51eb-6130-f201926180c8",
                            "subnet": "1.1.1.1/32",
                            "type": "ipmask",
                            "sub-type": "sdn",
                            "clearpass-spt": "unknown",
                            "start-mac": "00:00:00:00:00:00",
                            "end-mac": "00:00:00:00:00:00",
                            "cache-ttl": 0,
                            "fsso-group": [],
                            "visibility": "enable",
                            "color": 0,
                            "sdn-addr-type": "private",
                            "list": [],
                            "tagging": [],
                            "allow-routing": "disable",
                        },
                    ],
                    "ipv6_address_objects": [],
                },
            ],
            [
                "get_address_objects_by_fqdn",
                "test.com",
                None,
                "test.com",
                None,
                {
                    "address_objects": [
                        {
                            "name": "test.com",
                            "q_origin_key": "test.com",
                            "uuid": "9db45558-f60d-51eb-a7f8-32bdbc2b980e",
                            "type": "fqdn",
                            "sub-type": "sdn",
                            "clearpass-spt": "unknown",
                            "start-mac": "00:00:00:00:00:00",
                            "end-mac": "00:00:00:00:00:00",
                            "fqdn": "test.com",
                            "cache-ttl": 0,
                            "fsso-group": [],
                            "visibility": "enable",
                            "color": 0,
                            "sdn-addr-type": "private",
                            "list": [],
                            "tagging": [],
                            "allow-routing": "disable",
                        },
                    ],
                    "ipv6_address_objects": [],
                },
            ],
            [
                "get_address_objects_by_subnet",
                "1.1.1.1",
                "1.1.1.1/32",
                None,
                None,
                {
                    "address_objects": [
                        {
                            "name": "1.1.1.1",
                            "q_origin_key": "1.1.1.1",
                            "uuid": "5d0cb376-025a-51eb-6130-f201926180c8",
                            "subnet": "1.1.1.1/32",
                            "type": "ipmask",
                            "sub-type": "sdn",
                            "clearpass-spt": "unknown",
                            "start-mac": "00:00:00:00:00:00",
                            "end-mac": "00:00:00:00:00:00",
                            "cache-ttl": 0,
                            "fsso-group": [],
                            "visibility": "enable",
                            "color": 0,
                            "sdn-addr-type": "private",
                            "list": [],
                            "tagging": [],
                            "allow-routing": "disable",
                        },
                    ],
                    "ipv6_address_objects": [],
                },
            ],
            [
                "get_address_objects_by_ip6",
                "1111:2222:3333:4444:5555:6666:7777:8888",
                None,
                None,
                "1111:2222:3333:4444:5555:6666:7777:8888/128",
                {
                    "address_objects": [],
                    "ipv6_address_objects": [
                        {
                            "name": "1111:2222:3333:4444:5555:6666:7777:8888",
                            "q_origin_key": "1111:2222:3333:4444:5555:6666:7777:8888",
                            "uuid": "2dfbc876-1ba2-51ec-235c-e80fafc76aeb",
                            "type": "ipprefix",
                            "ip6": "1111:2222:3333:4444:5555:6666:7777:8888/128",
                            "end-ip": "::",
                            "cache-ttl": 0,
                            "visibility": "enable",
                            "color": 0,
                            "list": [],
                            "tagging": [],
                            "subnet-segment": [],
                            "host-type": "any",
                        },
                    ],
                },
            ],
        ]
    )
    def test_get_address_objects(
        self, mock_request, name, name_filter, subnet_filter, fqdn_filter, ipv6_subnet_filter, expected
    ):
        actual = self.action.run(
            {
                Input.NAME_FILTER: name_filter,
                Input.SUBNET_FILTER: subnet_filter,
                Input.FQDN_FILTER: fqdn_filter,
                Input.IPV6_SUBNET_FILTER: ipv6_subnet_filter,
            }
        )
        self.assertEqual(actual, expected)
