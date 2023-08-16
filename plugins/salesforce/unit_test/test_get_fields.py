import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_salesforce.actions.get_fields import GetFields
from unittest.mock import patch
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException
from komand_salesforce.util.exceptions import ApiException
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
    def test_get_fields(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
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
    def test_get_fields_raise_api_exception(self, mock_request, test_name, input_params, cause, assistance):
        with self.assertRaises(ApiException) as error:
            self.action.run(input_params)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
