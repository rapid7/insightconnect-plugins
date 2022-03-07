import sys
import os

from unittest import TestCase
from icon_cisco_firepower_management_center.actions.create_address_object import CreateAddressObject
from icon_cisco_firepower_management_center.actions.create_address_object.schema import Input
from unit_test.util import Util
from unittest.mock import patch
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))


@patch("requests.post", side_effect=Util.mocked_requests)
@patch("requests.request", side_effect=Util.mocked_requests)
@patch("ssl.SSLSocket.write", side_effect=Util.mock_write)
@patch("ssl.SSLSocket.connect", side_effect=Util.mock_connect)
@patch("ssl.SSLSocket.recv", side_effect=Util.mock_recv)
class TestCreateAddressObject(TestCase):
    @parameterized.expand(Util.load_parameters("create_address_object").get("parameters"))
    def test_create_address_object(
        self,
        mock_post,
        mock_request,
        mock_write,
        mock_connect,
        mock_recv,
        name,
        address_name,
        address,
        skip_private,
        whitelist,
        expected,
    ):
        action = Util.default_connector(CreateAddressObject())
        actual = action.run(
            {
                Input.ADDRESS_OBJECT: address_name,
                Input.ADDRESS: address,
                Input.SKIP_PRIVATE_ADDRESS: skip_private,
                Input.WHITELIST: whitelist,
            }
        )
        self.assertEqual(actual, expected)

    @parameterized.expand(Util.load_parameters("create_address_object_bad").get("parameters"))
    def test_create_address_object_bad(
        self,
        mock_post,
        mock_request,
        mock_write,
        mock_connect,
        mock_recv,
        name,
        address_name,
        address,
        skip_private,
        whitelist,
        cause,
        assistance,
    ):
        action = Util.default_connector(CreateAddressObject())
        with self.assertRaises(PluginException) as error:
            action.run(
                {
                    Input.ADDRESS_OBJECT: address_name,
                    Input.ADDRESS: address,
                    Input.SKIP_PRIVATE_ADDRESS: skip_private,
                    Input.WHITELIST: whitelist,
                }
            )
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
