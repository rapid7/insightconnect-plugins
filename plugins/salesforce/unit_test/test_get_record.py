import sys
import os

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_salesforce.actions.get_record import GetRecord
from util import Util
from unittest.mock import patch
from parameterized import parameterized


@patch("requests.request", side_effect=Util.mock_request)
class TestGetRecord(TestCase):
    @classmethod
    @patch("requests.request", side_effect=Util.mock_request)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(GetRecord())

    @parameterized.expand(
        [
            [
                "valid_text",
                Util.read_file_to_dict("inputs/get_record_valid.json.inp"),
                Util.read_file_to_dict("expected/get_record_valid.json.exp"),
            ]
        ]
    )
    def test_get_record(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "not_found",
                Util.read_file_to_dict("inputs/get_record_not_found.json.inp"),
                "No results found.",
                "Please provide valid inputs and try again.",
            ]
        ]
    )
    def test_get_record_raise_exception(self, mock_request, test_name, input_params, cause, assistance):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_params)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
