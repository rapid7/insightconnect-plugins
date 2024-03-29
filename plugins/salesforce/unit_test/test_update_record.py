import os
import sys

sys.path.append(os.path.abspath("../"))

from typing import Any, Dict
from unittest import TestCase
from unittest.mock import MagicMock, patch

from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate
from komand_salesforce.actions.update_record.action import UpdateRecord
from komand_salesforce.actions.update_record.schema import UpdateRecordOutput
from komand_salesforce.util.exceptions import ApiException
from parameterized import parameterized

from util import Util


@patch("requests.request", side_effect=Util.mock_request)
class TestUpdateRecord(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(UpdateRecord())

    @parameterized.expand(
        [
            [
                "success",
                Util.read_file_to_dict("inputs/update_record_success.json.inp"),
                Util.read_file_to_dict("expected/update_record_success.json.exp"),
            ],
        ]
    )
    def test_update_record(
        self, mock_request: MagicMock, test_name: str, input_params: Dict[str, Any], expected: Dict[str, Any]
    ) -> None:
        actual = self.action.run(input_params)
        validate(actual, UpdateRecordOutput.schema)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "invalid_object_data",
                Util.read_file_to_dict("inputs/update_record_invalid_object_data.json.inp"),
                PluginException.causes[PluginException.Preset.BAD_REQUEST],
                PluginException.assistances[PluginException.Preset.BAD_REQUEST],
            ],
            [
                "invalid_object_name",
                Util.read_file_to_dict("inputs/update_record_invalid_object_name.json.inp"),
                PluginException.causes[PluginException.Preset.NOT_FOUND],
                PluginException.assistances[PluginException.Preset.NOT_FOUND],
            ],
            [
                "invalid_record_id",
                Util.read_file_to_dict("inputs/update_record_invalid_record_id.json.inp"),
                PluginException.causes[PluginException.Preset.NOT_FOUND],
                PluginException.assistances[PluginException.Preset.NOT_FOUND],
            ],
        ]
    )
    def test_update_record_raise_api_exception(
        self, mock_request: MagicMock, test_name: str, input_params: Dict[str, Any], cause: str, assistance: str
    ) -> None:
        with self.assertRaises(ApiException) as error:
            self.action.run(input_params)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
