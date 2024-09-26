import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict
from unittest import TestCase
from unittest.mock import MagicMock, patch

from jsonschema import validate
from komand_okta.actions.get_factors import GetFactors
from komand_okta.util.exceptions import ApiException
from parameterized import parameterized

from util import Util


@patch("requests.request", side_effect=Util.mock_request)
class TestGetFactors(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetFactors())

    @parameterized.expand(
        [
            [
                "existing_user",
                Util.read_file_to_dict("inputs/get_factors_existing_user.json.inp"),
                Util.read_file_to_dict("expected/get_factors_existing_user.json.exp"),
            ],
            [
                "existing_user_without_factors",
                Util.read_file_to_dict("inputs/get_factors_existing_user_without_factors.json.inp"),
                Util.read_file_to_dict("expected/get_factors_existing_user_without_factors.json.exp"),
            ],
        ]
    )
    def test_get_factors(
        self, mock_request: MagicMock, test_name: str, input_params: Dict[str, Any], expected: Dict[str, Any]
    ) -> None:
        actual = self.action.run(input_params)
        validate(actual, self.action.output.schema)
        self.assertDictEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "user_not_found",
                Util.read_file_to_dict("inputs/get_factors_user_not_found.json.inp"),
                "Invalid or unreachable endpoint provided.",
                "Verify your input is correct and not malformed and try again. If the issue persists, please contact support.",
            ],
        ]
    )
    def test_get_factors_raise_exception(
        self, mock_request: MagicMock, test_name: str, input_parameters: Dict[str, Any], cause: str, assistance: str
    ) -> None:
        with self.assertRaises(ApiException) as error:
            self.action.run(input_parameters)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
