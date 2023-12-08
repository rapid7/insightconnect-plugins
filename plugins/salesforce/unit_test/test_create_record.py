import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict
from unittest import TestCase
from unittest.mock import MagicMock, patch

from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate
from komand_salesforce.actions.create_record.action import CreateRecord
from komand_salesforce.actions.create_record.schema import CreateRecordOutput
from komand_salesforce.util.exceptions import ApiException
from parameterized import parameterized

from util import Util


@patch("requests.request", side_effect=Util.mock_request)
class TestCreateRecord(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(CreateRecord())

    @parameterized.expand(
        [
            [
                "success_account",
                Util.read_file_to_dict("inputs/create_record_success_account.json.inp"),
                Util.read_file_to_dict("expected/create_record_success_account.json.exp"),
            ],
            [
                "success_document",
                Util.read_file_to_dict("inputs/create_record_success_document.json.inp"),
                Util.read_file_to_dict("expected/create_record_success_document.json.exp"),
            ],
        ]
    )
    def test_create_record(
        self, mock_request: MagicMock, test_name: str, input_params: Dict[str, Any], expected: str
    ) -> None:
        actual = self.action.run(input_params)
        validate(actual, CreateRecordOutput.schema)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "invalid_object_data",
                Util.read_file_to_dict("inputs/create_record_invalid_object_data.json.inp"),
                PluginException.causes[PluginException.Preset.BAD_REQUEST],
                PluginException.assistances[PluginException.Preset.BAD_REQUEST],
            ],
            [
                "invalid_object_name",
                Util.read_file_to_dict("inputs/create_record_invalid_object_name.json.inp"),
                PluginException.causes[PluginException.Preset.NOT_FOUND],
                PluginException.assistances[PluginException.Preset.NOT_FOUND],
            ],
            [
                "duplicated_resource",
                Util.read_file_to_dict("inputs/create_record_duplicated_resource.json.inp"),
                PluginException.causes[PluginException.Preset.BAD_REQUEST],
                PluginException.assistances[PluginException.Preset.BAD_REQUEST],
            ],
        ]
    )
    def test_create_record_raise_api_exception(
        self, mock_request: MagicMock, test_name: str, input_params: Dict[str, Any], cause: str, assistance: str
    ) -> None:
        with self.assertRaises(ApiException) as error:
            self.action.run(input_params)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
