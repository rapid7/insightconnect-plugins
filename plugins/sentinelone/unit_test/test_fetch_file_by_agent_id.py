import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest.mock import patch
from util import Util
from unittest import TestCase
from komand_sentinelone.actions.fetch_file_by_agent_id import FetchFileByAgentId
from komand_sentinelone.actions.fetch_file_by_agent_id.schema import (
    FetchFileByAgentIdOutput,
)
from insightconnect_plugin_runtime.exceptions import PluginException
from parameterized import parameterized
from jsonschema import validate


@patch("requests.request", side_effect=Util.mocked_requests_get)
class TestFetchFileByAgentId(TestCase):
    @classmethod
    @patch("requests.post", side_effect=Util.mocked_requests_get)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(FetchFileByAgentId())

    @parameterized.expand(
        [
            [
                "success",
                Util.read_file_to_dict("inputs/fetch_file_by_agent_id_success.json.inp"),
                Util.read_file_to_dict("expected/fetch_file_by_agent_id_success.json.exp"),
            ],
        ]
    )
    def test_fetch_file_by_agent_id(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertEqual(expected, actual)
        validate(actual, FetchFileByAgentIdOutput.schema)

    @parameterized.expand(
        [
            [
                "invalid_agent_id",
                Util.read_file_to_dict("inputs/fetch_file_by_agent_id_invalid_agent_id.json.inp"),
                "Resource not found.",
                "Please provide valid inputs and try again.",
            ],
            [
                "invalid_password_missing_special_character",
                Util.read_file_to_dict("inputs/fetch_file_by_agent_id_invalid_password_1.json.inp"),
                "Invalid password.",
                "The password must be 10 or more characters with a mix of upper and lower case letters, numbers, "
                "and symbols.",
            ],
            [
                "invalid_password_missing_number",
                Util.read_file_to_dict("inputs/fetch_file_by_agent_id_invalid_password_2.json.inp"),
                "Invalid password.",
                "The password must be 10 or more characters with a mix of upper and lower case letters, numbers, "
                "and symbols.",
            ],
            [
                "invalid_password_missing_uppercase_letter",
                Util.read_file_to_dict("inputs/fetch_file_by_agent_id_invalid_password_3.json.inp"),
                "Invalid password.",
                "The password must be 10 or more characters with a mix of upper and lower case letters, numbers, "
                "and symbols.",
            ],
            [
                "invalid_password_missing_lowercase_letter",
                Util.read_file_to_dict("inputs/fetch_file_by_agent_id_invalid_password_4.json.inp"),
                "Invalid password.",
                "The password must be 10 or more characters with a mix of upper and lower case letters, numbers, "
                "and symbols.",
            ],
            [
                "invalid_password_too_short",
                Util.read_file_to_dict("inputs/fetch_file_by_agent_id_invalid_password_5.json.inp"),
                "Invalid password.",
                "The password must be 10 or more characters with a mix of upper and lower case letters, numbers, "
                "and symbols.",
            ],
        ]
    )
    def test_fetch_file_by_agent_id_raise_exception(self, mock_request, test_name, input_params, cause, assistance):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_params)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
