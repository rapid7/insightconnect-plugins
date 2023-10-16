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
                "The user valid_id has been deleted",
            ]
        ]
    )
    def test_delete_user_by_id_valid(self, mock_request: MagicMock, test_name: str, input_params: dict, expected: dict):
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "missing_params_invalid",
                {},
                "Missing required paramaters",
                "Please ensure a valid 'email' and 'id' is provided",
            ]
        ]
    )
    def test_missing_params_invalid(
        self, mock_request: MagicMock, test_name: str, input_params: dict, cause: str, assistance: str
    ):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_params)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)

    @parameterized.expand(
        [
            [
                "delete_valid",
                {"id": "invalid_id", "email": "test@test.com"},
                "Invalid or unreachable endpoint provided.",
                "Verify the endpoint/URL/hostname configured in your plugin connection is correct.",
            ]
        ]
    )
    def test_delete_user_by_id_invalid(
        self, mock_request: MagicMock, test_name: str, input_params: dict, cause: str, assistance: str
    ):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_params)

        print(cause)
        print(error.exception.cause)

        print(assistance)
        print(error.exception.assistance)

        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
