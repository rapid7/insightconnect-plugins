import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict
from unittest import TestCase
from unittest.mock import MagicMock, patch

from icon_cisco_firepower_management_center.actions.delete_address_object import DeleteAddressObject
from icon_cisco_firepower_management_center.actions.delete_address_object.schema import Input
from jsonschema import validate
from parameterized import parameterized

from util import Util


@patch("requests.post", side_effect=Util.mocked_requests)
@patch("requests.request", side_effect=Util.mocked_requests)
@patch("ssl.SSLSocket._create", side_effect=Util.MockSSLSocket)
class TestDeleteAddressObject(TestCase):
    @parameterized.expand(Util.load_parameters("delete_address_object").get("parameters"))
    def test_delete_address_object(
        self,
        mock_post: MagicMock,
        mock_request: MagicMock,
        mock_create: MagicMock,
        name: str,
        address_object: str,
        expected: Dict[str, Any],
    ) -> None:
        action = Util.default_connector(DeleteAddressObject())
        actual = action.run({Input.ADDRESS_OBJECT: address_object})
        validate(actual, action.output.schema)
        self.assertEqual(actual, expected)
        mock_post.assert_called()
        mock_request.assert_called()
        mock_create.assert_called()
