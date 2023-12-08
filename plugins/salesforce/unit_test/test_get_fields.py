import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict
from unittest import TestCase
from unittest.mock import MagicMock, patch

from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate
from komand_salesforce.actions.get_fields import GetFields
from komand_salesforce.actions.get_fields.schema import GetFieldsOutput
from komand_salesforce.util.exceptions import ApiException
from parameterized import parameterized

from util import Util


@patch("requests.request", side_effect=Util.mock_request)
class TestGetFields(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetFields())

    @parameterized.expand(
        [
            [
                "few_fields",
                Util.read_file_to_dict("inputs/get_fields_1.json.inp"),
                Util.read_file_to_dict("expected/get_fields_1.json.exp"),
            ],
            [
                "one_field",
                Util.read_file_to_dict("inputs/get_fields_2.json.inp"),
                Util.read_file_to_dict("expected/get_fields_2.json.exp"),
            ],
            [
                "with_empty_field",
                Util.read_file_to_dict("inputs/get_fields_3.json.inp"),
                Util.read_file_to_dict("expected/get_fields_1.json.exp"),
            ],
        ]
    )
    def test_get_fields(
        self, mock_request: MagicMock, test_name: str, input_params: Dict[str, Any], expected: Dict[str, Any]
    ) -> None:
        actual = self.action.run(input_params)
        validate(actual, GetFieldsOutput.schema)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "invalid_record_id",
                Util.read_file_to_dict("inputs/get_fields_invalid_record_id.json.inp"),
                PluginException.causes[PluginException.Preset.NOT_FOUND],
                PluginException.assistances[PluginException.Preset.NOT_FOUND],
            ],
            [
                "invalid_object_name",
                Util.read_file_to_dict("inputs/get_fields_invalid_object.json.inp"),
                PluginException.causes[PluginException.Preset.NOT_FOUND],
                PluginException.assistances[PluginException.Preset.NOT_FOUND],
            ],
            [
                "invalid_field",
                Util.read_file_to_dict("inputs/get_fields_invalid_field.json.inp"),
                PluginException.causes[PluginException.Preset.BAD_REQUEST],
                PluginException.assistances[PluginException.Preset.BAD_REQUEST],
            ],
        ]
    )
    def test_get_fields_raise_api_exception(
        self, mock_request: MagicMock, test_name: str, input_params: Dict[str, Any], cause: str, assistance: str
    ) -> None:
        with self.assertRaises(ApiException) as error:
            self.action.run(input_params)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
