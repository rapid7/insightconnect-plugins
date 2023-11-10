import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_duo_admin.actions.get_user_by_id import GetUserById
from util import Util
from unittest.mock import patch
from parameterized import parameterized
from komand_duo_admin.util.exceptions import ApiException
from komand_duo_admin.util.constants import Assistance, Cause


@patch("requests.request", side_effect=Util.mock_request)
@patch("komand_duo_admin.util.api.isinstance", return_value=True)
class TestGetUserById(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetUserById())

    @parameterized.expand(
        [
            [
                "user_found",
                Util.read_file_to_dict("inputs/get_user_by_id.json.inp"),
                Util.read_file_to_dict("expected/get_user_by_id.json.exp"),
            ],
        ]
    )
    def test_get_user_by_id(self, mock_request, mock_request_instance, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertDictEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "user_not_found",
                Util.read_file_to_dict("inputs/get_user_by_id_bad.json.inp"),
                Cause.NOT_FOUND,
                Assistance.VERIFY_INPUT,
            ],
        ]
    )
    def test_get_user_by_id_raise_api_exception(
        self, mock_request, mock_request_instance, test_name, input_parameters, cause, assistance
    ):
        with self.assertRaises(ApiException) as error:
            self.action.run(input_parameters)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
