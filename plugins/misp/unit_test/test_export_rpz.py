import base64
import os
import sys
import unittest
from unittest.mock import patch, MagicMock

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))
from komand_misp.actions.export_rpz.action import ExportRpz
from komand_misp.actions.export_rpz.schema import ExportRpzInput, ExportRpzOutput
from jsonschema import validate


class TestExportRpz(unittest.TestCase):
    def setUp(self):
        self.action = ExportRpz()
        self.action.connection = MagicMock()
        self.action.logger = MagicMock()
        self.mock_client = MagicMock()
        self.action.connection.key = "api_key"
        self.action.connection.url = "http://example.com"

        self.params = {"event_id": "event_id", "tags": ["tag1", "tag2"], "from": "2020-01-01", "to": "2020-12-31"}

    @patch("komand_misp.actions.export_rpz.action.requests.get")
    def test_export_rpz_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = "zone data"
        mock_get.return_value = mock_response

        validate(self.params, ExportRpzInput.schema)
        result = self.action.run(self.params)
        expected_rpz = base64.b64encode("zone data".encode("ascii")).decode("utf-8")
        self.assertEqual(result, {"rpz": expected_rpz})
        validate(result, ExportRpzOutput.schema)

    @patch("komand_misp.actions.export_rpz.action.requests.get")
    def test_export_rpz_failure(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_response.json.return_value = {"message": "Bad request"}
        mock_get.return_value = mock_response

        validate(self.params, ExportRpzInput.schema)
        with self.assertRaises(PluginException) as context:
            self.action.run(self.params)
        self.assertTrue(PluginException.causes[PluginException.Preset.BAD_REQUEST] in context.exception.cause)
