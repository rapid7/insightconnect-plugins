import os
import sys

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict
from unittest import TestCase
from unittest.mock import MagicMock, patch

from jsonschema import validate
from komand_salesforce.actions.get_record import GetRecord
from komand_salesforce.actions.get_record.schema import GetRecordOutput
from parameterized import parameterized

from util import Util


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
    def test_get_record(
        self, mock_request: MagicMock, test_name: str, input_params: Dict[str, Any], expected: Dict[str, Any]
    ) -> None:
        actual = self.action.run(input_params)
        validate(actual, GetRecordOutput.schema)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "not_found",
                Util.read_file_to_dict("inputs/get_record_not_found.json.inp"),
                PluginException.causes[PluginException.Preset.NOT_FOUND],
                PluginException.assistances[PluginException.Preset.NOT_FOUND],
            ]
        ]
    )
    def test_get_record_raise_exception(
        self, mock_request: MagicMock, test_name: str, input_params: Dict[str, Any], cause: str, assistance: str
    ) -> None:
        with self.assertRaises(PluginException) as error:
            self.action.run(input_params)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
