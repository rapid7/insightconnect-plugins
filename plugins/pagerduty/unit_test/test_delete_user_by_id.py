import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_pagerduty.actions.delete_user_by_id import DeleteUserById
from unittest.mock import patch, MagicMock
from parameterized import parameterized
from util import Util
from insightconnect_plugin_runtime.exceptions import PluginException


@patch("requests.Session.request", side_effect=Util.mock_request)
class TestDeleteUserById(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(DeleteUserById())

    @parameterized.expand(
        [
            [
                "delete_valid",
                {"id": "valid_id", "email": "test@test.com"},
                {"success": "The user valid_id has been deleted"},
            ]
        ]
    )
    def test_delete_user_by_id_valid(
        self, _mock_request: MagicMock, _test_name: str, input_params: dict, expected: dict
    ):
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "delete_invalid",
                {"id": "invalid_id", "email": "test@test.com"},
                "Invalid or unreachable endpoint provided.",
                "Verify the URLs or endpoints in your configuration are correct.",
            ]
        ]
    )
    def test_delete_user_by_id_invalid(
        self, _mock_request: MagicMock, _test_name: str, input_params: dict, cause: str, assistance: str
    ):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_params)

        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
