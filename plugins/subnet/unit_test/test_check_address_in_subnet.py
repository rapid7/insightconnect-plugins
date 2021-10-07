from unittest import TestCase
from komand_subnet.actions.check_address_in_subnet import CheckAddressInSubnet
from komand_subnet.actions.check_address_in_subnet.schema import Input, Output
from insightconnect_plugin_runtime.exceptions import PluginException
from parameterized import parameterized


class TestCheckAddressInSubnet(TestCase):
    @parameterized.expand(
        [
            ["ip_address_found", "10.1.10.150", "10.1.10.1/24", {"found": True}],
            ["ip_address_not_found", "10.1.20.0", "10.1.10.1/24", {"found": False}],
            ["subnet_in_netmask", "10.1.10.150", "10.1.10.1/255.255.255.0", {"found": True}],
            ["subnet_in_netmask_ip_address_not_found", "10.1.20.0", "10.1.10.1/255.255.255.0", {"found": False}],
            ["check_ip_address", "216.202.192.66", "216.202.192.1/255.255.252.0", {"found": True}],
            ["check_ip_address2", "216.202.192.66", "216.202.192.1/22", {"found": True}],
            ["check_ip_address3", "198.51.100.1", "198.51.100.0/30", {"found": True}],
            ["check_ip_address4", "198.51.100.1", "198.51.100.0/255.255.255.252", {"found": True}],
        ]
    )
    def test_check_address_in_subnet(self, name, ip, subnet, expected):
        action = CheckAddressInSubnet()
        actual = action.run({Input.IP_ADDRESS: ip, Input.SUBNET: subnet})
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "invalid_ip",
                "999.999.999.999",
                "10.1.10.1/24",
                "Invalid IP address.",
                "Please check that the provided IP address is correct and try again.",
            ],
            [
                "invalid_subnet",
                "10.1.20.0",
                "10.1.10.1/33",
                "Invalid subnet.",
                "Please check that the provided subnet is correct and try again.",
            ],
            [
                "invalid_subnet2",
                "10.1.10.150",
                "10.1.10.1/300.255.255.0",
                "Invalid subnet.",
                "Please check that the provided subnet is correct and try again.",
            ],
        ]
    )
    def test_check_address_in_subnet_invalid_inputs(self, name, ip, subnet, cause, assistance):
        action = CheckAddressInSubnet()
        with self.assertRaises(PluginException) as e:
            action.run({Input.IP_ADDRESS: ip, Input.SUBNET: subnet})
        self.assertEqual(e.exception.cause, cause)
        self.assertEqual(e.exception.assistance, assistance)
