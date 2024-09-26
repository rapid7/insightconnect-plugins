import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict
from unittest import TestCase
from unittest.mock import MagicMock, patch

from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate
from komand_okta.actions.send_push import SendPush
from komand_okta.util.exceptions import ApiException
from parameterized import parameterized

from util import Util


@patch("requests.request", side_effect=Util.mock_request)
class TestSendPush(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(SendPush())

    @parameterized.expand(
        [
            [
                "success",
                Util.read_file_to_dict("inputs/send_push_success.json.inp"),
                Util.read_file_to_dict("expected/send_push_success.json.exp"),
            ],
            [
                "rejected",
                Util.read_file_to_dict("inputs/send_push_rejected.json.inp"),
                Util.read_file_to_dict("expected/send_push_rejected.json.exp"),
            ],
            [
                "timeout",
                Util.read_file_to_dict("inputs/send_push_timeout.json.inp"),
                Util.read_file_to_dict("expected/send_push_timeout.json.exp"),
            ],
        ]
    )
    def test_send_push(
        self, mock_request: MagicMock, test_name: str, input_params: Dict[str, Any], expected: Dict[str, Any]
    ) -> None:
        actual = self.action.run(input_params)
        validate(actual, self.action.output.schema)
        self.assertDictEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "factor_not_found",
                Util.read_file_to_dict("inputs/send_push_factor_not_found.json.inp"),
                "Invalid or unreachable endpoint provided.",
                "Verify your input is correct and not malformed and try again. If the issue persists, please contact support.",
            ],
            [
                "user_not_found",
                Util.read_file_to_dict("inputs/send_push_user_not_found.json.inp"),
                "Invalid or unreachable endpoint provided.",
                "Verify your input is correct and not malformed and try again. If the issue persists, please contact support.",
            ],
        ]
    )
    def test_send_push_raise_api_exception(
        self, mock_request: MagicMock, test_name: str, input_parameters: Dict[str, Any], cause: str, assistance: str
    ) -> None:
        with self.assertRaises(ApiException) as error:
            self.action.run(input_parameters)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)

    @parameterized.expand(
        [
            [
                "not_push_type",
                Util.read_file_to_dict("inputs/send_push_invalid_factor.json.inp"),
                "An error has occurred retrieving data from the Okta API.",
                "It looks like we didn't get data we were expecting back. Was "
                "the Factor ID supplied a push type and not something else, "
                "such as an SMS?",
            ]
        ]
    )
    def test_send_push_raise_plugin_exception(
        self, mock_request: MagicMock, test_name: str, input_parameters: Dict[str, Any], cause: str, assistance: str
    ) -> None:
        with self.assertRaises(PluginException) as error:
            self.action.run(input_parameters)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
