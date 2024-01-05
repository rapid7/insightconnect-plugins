import os
import sys

sys.path.append(os.path.abspath("../"))
from typing import Any, Dict
from unittest import TestCase
from unittest.mock import MagicMock, patch

from icon_cisco_firepower_management_center.actions.check_if_address_in_group import CheckIfAddressInGroup
from icon_cisco_firepower_management_center.actions.check_if_address_in_group.schema import Input
from jsonschema import validate
from parameterized import parameterized

from util import Util


@patch("requests.post", side_effect=Util.mocked_requests)
@patch("requests.request", side_effect=Util.mocked_requests)
@patch("ssl.SSLSocket._create", side_effect=Util.MockSSLSocket)
class TestCheckIfAddressInGroup(TestCase):
    @parameterized.expand(Util.load_parameters("check_if_address_in_group").get("parameters"))
    def test_check_if_address_in_group(
        self,
        mock_post: MagicMock,
        mock_request: MagicMock,
        mock_create: MagicMock,
        name: str,
        address: str,
        group: str,
        enable_search: bool,
        expected: Dict[str, Any],
    ) -> None:
        action = Util.default_connector(CheckIfAddressInGroup())
        actual = action.run({Input.ADDRESS: address, Input.GROUP: group, Input.ENABLE_SEARCH: enable_search})
        validate(actual, action.output.schema)
        self.assertEqual(actual, expected)
        mock_post.assert_called()
        mock_request.assert_called()
        mock_create.assert_called()
