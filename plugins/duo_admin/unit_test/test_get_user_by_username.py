import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_duo_admin.actions.get_user_by_username import GetUserByUsername
from util import Util
from unittest.mock import patch
from parameterized import parameterized
from komand_duo_admin.util.exceptions import ApiException
from komand_duo_admin.util.constants import Assistance, Cause


@patch("requests.request", side_effect=Util.mock_request)
@patch("komand_duo_admin.util.api.isinstance", return_value=True)
class TestGetUserByUsername(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetUserByUsername())

    @parameterized.expand(
        [
            [
                "valid_username_1",
                Util.read_file_to_dict("inputs/get_user_by_username_1.json.inp"),
                Util.read_file_to_dict("expected/get_user_by_username_1.json.exp"),
            ],
            [
                "valid_username_2",
                Util.read_file_to_dict("inputs/get_user_by_username_2.json.inp"),
                Util.read_file_to_dict("expected/get_user_by_username_2.json.exp"),
            ],
        ]
    )
    def test_get_user_by_username(self, mock_request, mock_request_instance, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertDictEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "username_not_found",
                Util.read_file_to_dict("inputs/get_user_by_username_bad.json.inp"),
                Cause.NOT_FOUND,
                Assistance.VERIFY_INPUT,
            ],
        ]
    )
    def test_get_user_by_username_raise_api_exception(
        self, mock_request, mock_request_instance, test_name, input_parameters, cause, assistance
    ):
        with self.assertRaises(ApiException) as error:
            self.action.run(input_parameters)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
