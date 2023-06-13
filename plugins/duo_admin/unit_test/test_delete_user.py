import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_duo_admin.actions.delete_user.action import DeleteUser
from util import Util
from unittest.mock import patch
from parameterized import parameterized
from komand_duo_admin.util.exceptions import ApiException
from komand_duo_admin.util.constants import Cause, Assistance


@patch("requests.request", side_effect=Util.mock_request)
class TestDeleteUser(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(DeleteUser())

    @parameterized.expand(
        [
            [
                "existing_user",
                Util.read_file_to_dict("inputs/delete_user_success.json.inp"),
                Util.read_file_to_dict("expected/delete_user_success.json.exp"),
            ],
        ]
    )
    def test_delete_user(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "invalid_user_id",
                Util.read_file_to_dict("inputs/delete_user_invalid_id.json.inp"),
                Cause.NOT_FOUND,
                Assistance.VERIFY_INPUT,
            ],
        ]
    )
    def test_delete_user_raise_api_exception(self, mock_request, test_name, input_parameters, cause, assistance):
        with self.assertRaises(ApiException) as error:
            self.action.run(input_parameters)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
