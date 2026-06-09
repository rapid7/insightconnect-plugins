import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict
from unittest import TestCase
from unittest.mock import MagicMock, patch

from icon_azure_ad_admin.actions.get_user_memberships import GetUserMemberships
from insightconnect_plugin_runtime.exceptions import PluginException
from parameterized import parameterized

from util import Util


@patch("requests.request", side_effect=Util.mocked_requests)
class TestGetUserMemberships(TestCase):
    @classmethod
    @patch("requests.post", side_effect=Util.mocked_requests)
    def setUpClass(cls, mock_request: MagicMock) -> None:
        cls.action = Util.default_connector(GetUserMemberships())

    @parameterized.expand(
        [
            [
                "valid_user",
                Util.read_file_to_dict("inputs/get_user_memberships.json.inp"),
                Util.read_file_to_dict("expected/get_user_memberships.json.exp"),
            ],
        ]
    )
    def test_get_user_memberships(
        self, mock_request: MagicMock, test_name: str, input_params: Dict[str, Any], expected: Dict[str, Any]
    ) -> None:
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "invalid_user",
                Util.read_file_to_dict("inputs/get_user_memberships_invalid_user.json.inp"),
                "Resource not found.",
                "Please provide valid inputs and try again.",
            ],
        ]
    )
    def test_get_user_memberships_raise_exception(
        self, mock_request: MagicMock, test_name: str, input_params: Dict[str, Any], cause: str, assistance: str
    ) -> None:
        with self.assertRaises(PluginException) as error:
            self.action.run(input_params)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
