import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_salesforce.actions.get_blob_data import GetBlobData
from unittest.mock import patch
from parameterized import parameterized
from komand_salesforce.util.exceptions import ApiException
from util import Util
from insightconnect_plugin_runtime.exceptions import PluginException


@patch("requests.request", side_effect=Util.mock_request)
class TestGetBlobData(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetBlobData())

    @parameterized.expand(
        [
            [
                "document",
                Util.read_file_to_dict("inputs/get_blob_data_document.json.inp"),
                Util.read_file_to_dict("expected/get_blob_data.json.exp"),
            ],
            [
                "attachment",
                Util.read_file_to_dict("inputs/get_blob_data_attachment.json.inp"),
                Util.read_file_to_dict("expected/get_blob_data.json.exp"),
            ],
        ]
    )
    def test_get_blob_data(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "invalid_record_id",
                Util.read_file_to_dict("inputs/get_blob_data_invalid_record_id.json.inp"),
                PluginException.causes[PluginException.Preset.NOT_FOUND],
                PluginException.assistances[PluginException.Preset.NOT_FOUND],
            ],
            [
                "invalid_object_name",
                Util.read_file_to_dict("inputs/get_blob_data_invalid_object.json.inp"),
                PluginException.causes[PluginException.Preset.NOT_FOUND],
                PluginException.assistances[PluginException.Preset.NOT_FOUND],
            ],
        ]
    )
    def test_get_blob_data_raise_api_exception(self, mock_request, test_name, input_params, cause, assistance):
        with self.assertRaises(ApiException) as error:
            self.action.run(input_params)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
