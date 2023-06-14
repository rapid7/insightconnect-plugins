import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_duo_admin.actions.get_phones_by_user_id.action import GetPhonesByUserId
from util import Util
from unittest.mock import patch
from parameterized import parameterized
from komand_duo_admin.util.exceptions import ApiException
from komand_duo_admin.util.constants import Cause, Assistance


@patch("requests.request", side_effect=Util.mock_request)
class TestGetPhonesByUserId(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetPhonesByUserId())

    @parameterized.expand(
        [
            [
                "existing_user_with_no_phones",
                Util.read_file_to_dict("inputs/get_phones_by_user_id_no_phones.json.inp"),
                Util.read_file_to_dict("expected/get_phones_by_user_id_no_phones.json.exp"),
            ],
            [
                "existing_user_with_phones",
                Util.read_file_to_dict("inputs/get_phones_by_user_id_existing_phones.json.inp"),
                Util.read_file_to_dict("expected/get_phones_by_user_id_existing_phones.json.exp"),
            ],
        ]
    )
    def test_get_phones_by_user_id(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "invalid_user_id",
                Util.read_file_to_dict("inputs/get_phones_by_user_id_invalid_id.json.inp"),
                Cause.NOT_FOUND,
                Assistance.VERIFY_INPUT,
            ],
        ]
    )
    def test_get_phones_by_user_id_raise_api_exception(
        self, mock_request, test_name, input_parameters, cause, assistance
    ):
        with self.assertRaises(ApiException) as error:
            self.action.run(input_parameters)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
