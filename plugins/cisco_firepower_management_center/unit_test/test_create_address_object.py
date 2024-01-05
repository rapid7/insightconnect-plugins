import os
import sys

sys.path.append(os.path.abspath("../"))
from unittest import TestCase
from unittest.mock import MagicMock, patch

from icon_cisco_firepower_management_center.actions.create_address_object import CreateAddressObject
from icon_cisco_firepower_management_center.actions.create_address_object.schema import Input
from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate
from parameterized import parameterized

from util import Util


@patch("requests.post", side_effect=Util.mocked_requests)
@patch("requests.request", side_effect=Util.mocked_requests)
@patch("ssl.SSLSocket._create", side_effect=Util.MockSSLSocket)
class TestCreateAddressObject(TestCase):
    @parameterized.expand(Util.load_parameters("create_address_object").get("parameters"))
    def test_create_address_object(
        self,
        mock_post: MagicMock,
        mock_request: MagicMock,
        mock_create: MagicMock,
        name: str,
        address_name: str,
        address: str,
        skip_private: bool,
        whitelist: str,
        expected: str,
    ) -> None:
        action = Util.default_connector(CreateAddressObject())
        actual = action.run(
            {
                Input.ADDRESS_OBJECT: address_name,
                Input.ADDRESS: address,
                Input.SKIP_PRIVATE_ADDRESS: skip_private,
                Input.WHITELIST: whitelist,
            }
        )
        validate(actual, action.output.schema)
        self.assertEqual(actual, expected)
        mock_post.assert_called()
        mock_request.assert_called()
        mock_create.assert_called()

    @parameterized.expand(Util.load_parameters("create_address_object_bad").get("parameters"))
    def test_create_address_object_bad(
        self,
        mock_post: MagicMock,
        mock_request: MagicMock,
        mock_create: MagicMock,
        name: str,
        address_name: str,
        address: str,
        skip_private: bool,
        whitelist: str,
        cause: str,
        assistance: str,
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
        mock_post.assert_called()
        mock_request.assert_called()
        mock_create.assert_called()
