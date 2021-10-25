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

parameters = Util.load_data("get_address_object_parameters").get("parameters")


@patch("requests.Session.request", side_effect=Util.mocked_requests)
class TestGetAddressObjects(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetAddressObjects())

    @parameterized.expand(parameters)
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
