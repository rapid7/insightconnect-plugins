import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_salesforce.actions.delete_record.action import DeleteRecord
from unittest.mock import patch
from parameterized import parameterized
from komand_salesforce.util.exceptions import ApiException
from util import Util


@patch("requests.request", side_effect=Util.mock_request)
class TestDeleteRecord(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(DeleteRecord())

    @parameterized.expand(
        [
            [
                "success",
                Util.read_file_to_dict("inputs/delete_record_success.json.inp"),
                Util.read_file_to_dict("expected/delete_record_success.json.exp"),
            ],
        ]
    )
    def test_delete_record(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "invalid_record_id",
                Util.read_file_to_dict("inputs/delete_record_invalid_record_id.json.inp"),
                "No results found.",
                "Please provide valid inputs and try again.",
            ],
            [
                "invalid_object_name",
                Util.read_file_to_dict("inputs/delete_record_invalid_object_name.json.inp"),
                "No results found.",
                "Please provide valid inputs and try again.",
            ],
        ]
    )
    def test_delete_record_raise_api_exception(self, mock_request, test_name, input_params, cause, assistance):
        with self.assertRaises(ApiException) as error:
            self.action.run(input_params)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
