from unittest import TestCase
from komand_subnet.actions.calculate import Calculate
from komand_subnet.actions.calculate.schema import Input, Output
from insightconnect_plugin_runtime.exceptions import PluginException
from parameterized import parameterized


class TestCalculate(TestCase):
    @parameterized.expand(
        [
            [
                "calculate",
                "192.168.0.0/24",
                {
                    "ip": "192.168.0.0",
                    "netmask": "255.255.255.0",
                    "wildcard": "0.0.0.255",
                    "cidr": "/24",
                    "binary_netmask": "11111111111111111111111100000000",
                    "ip_class": "C",
                    "subnets": 1,
                    "hosts": 254,
                    "subnet_id": "192.168.0.0",
                    "host_range": "192.168.0.1 - 192.168.0.254",
                    "broadcast": "192.168.0.255",
                },
            ],
            [
                "calculate2",
                "192.168.0.0/30",
                {
                    "ip": "192.168.0.0",
                    "netmask": "255.255.255.252",
                    "wildcard": "0.0.0.3",
                    "cidr": "/30",
                    "binary_netmask": "11111111111111111111111111111100",
                    "ip_class": "C",
                    "subnets": 64,
                    "hosts": 2,
                    "subnet_id": "192.168.0.0",
                    "host_range": "192.168.0.1 - 192.168.0.2",
                    "broadcast": "192.168.0.3",
                },
            ],
            [
                "calculate3",
                "192.168.0.0/31",
                {
                    "ip": "192.168.0.0",
                    "netmask": "255.255.255.254",
                    "wildcard": "0.0.0.1",
                    "cidr": "/31",
                    "binary_netmask": "11111111111111111111111111111110",
                    "ip_class": "C",
                    "subnets": 128,
                    "hosts": 0,
                    "subnet_id": "192.168.0.0",
                    "host_range": "",
                    "broadcast": "192.168.0.1",
                },
            ],
            [
                "calculate4",
                "192.168.0.0/32",
                {
                    "ip": "192.168.0.0",
                    "netmask": "255.255.255.255",
                    "wildcard": "0.0.0.0",
                    "cidr": "/32",
                    "binary_netmask": "11111111111111111111111111111111",
                    "ip_class": "C",
                    "subnets": 256,
                    "hosts": 0,
                    "subnet_id": "192.168.0.0",
                    "host_range": "",
                    "broadcast": "192.168.0.0",
                },
            ],
            [
                "calculate5",
                "128.0.0.0/20",
                {
                    "ip": "128.0.0.0",
                    "netmask": "255.255.240.0",
                    "wildcard": "0.0.15.255",
                    "cidr": "/20",
                    "binary_netmask": "11111111111111111111000000000000",
                    "ip_class": "B",
                    "subnets": 16,
                    "hosts": 4094,
                    "subnet_id": "128.0.0.0",
                    "host_range": "128.0.0.1 - 128.0.15.254",
                    "broadcast": "128.0.15.255",
                },
            ],
            [
                "calculate6",
                "99.99.99.99/8",
                {
                    "ip": "99.99.99.99",
                    "netmask": "255.0.0.0",
                    "wildcard": "0.255.255.255",
                    "cidr": "/8",
                    "binary_netmask": "11111111000000000000000000000000",
                    "ip_class": "A",
                    "subnets": 1,
                    "hosts": 16777214,
                    "subnet_id": "99.0.0.0",
                    "host_range": "99.0.0.1 - 99.255.255.254",
                    "broadcast": "99.255.255.255",
                },
            ],
        ]
    )
    def test_calculate(self, name, cidr, expected):
        action = Calculate()
        actual = action.run({Input.CIDR: cidr})
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "invalid_ip",
                "999.1.1.1/32",
                "Provided network 999.1.1.1/32 is not in CIDR notation.",
                "Please check that the provided network is correct and try again.",
            ],
            [
                "invalid_network",
                "192.168.1.0/33",
                "Provided network 192.168.1.0/33 is not in CIDR notation.",
                "Please check that the provided network is correct and try again.",
            ],
            [
                "input_as_ip",
                "192.168.1.0",
                "Provided network 192.168.1.0 is not in CIDR notation.",
                "Please check that the provided network is correct and try again.",
            ],
            [
                "ip_in_reserved_range",
                "224.0.0.0/32",
                "IP address 224.0.0.0 resides in reserved range.",
                "Please provide an IP address outside the reserved range.",
            ],
            [
                "invalid_mask",
                "100.10.0.0/2",
                "Invalid mask for network class.",
                "Please provide a valid mask for the network class.",
            ],
        ]
    )
    def test_calculate_bad(self, name, cidr, cause, assistance):
        action = Calculate()
        with self.assertRaises(PluginException) as e:
            actual = action.run({Input.CIDR: cidr})
        self.assertEqual(e.exception.cause, cause)
        self.assertEqual(e.exception.assistance, assistance)
