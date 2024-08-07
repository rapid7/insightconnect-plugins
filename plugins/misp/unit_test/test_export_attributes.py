import base64
import os
import sys
import unittest
from unittest.mock import patch, MagicMock

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))
from komand_misp.actions.export_attributes.action import ExportAttributes
from komand_misp.actions.export_attributes.schema import ExportAttributesInput, ExportAttributesOutput
from jsonschema import validate


class TestExportAttributes(unittest.TestCase):
    def setUp(self):
        self.action = ExportAttributes()
        self.action.connection = MagicMock()
        self.action.logger = MagicMock()
        self.mock_client = MagicMock()
        self.action.connection.key = "api_key"
        self.action.connection.url = "http://example.com"

        self.params = {
            "event_id": ["event_id"],
            "include": True,
            "tags": ["tag1", "tag2"],
            "category": "category",
            "type": "type",
            "include_context": True,
            "from": "2020-01-01",
            "to": "2020-12-31",
            "last": "5d",
        }

    @patch("komand_misp.actions.export_attributes.action.requests.post")
    def test_export_attributes_success(self, mock_post):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = "attribute1,attribute2,attribute3"
        mock_post.return_value = mock_response

        validate(self.params, ExportAttributesInput.schema)
        result = self.action.run(self.params)
        expected_attributes = base64.b64encode("attribute1,attribute2,attribute3".encode("ascii")).decode("utf-8")
        self.assertEqual(result, {"attributes": expected_attributes})
        validate(result, ExportAttributesOutput.schema)

    @patch("komand_misp.actions.export_attributes.action.requests.post")
    def test_export_attributes_failure(self, mock_post):
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_response.json.return_value = {"message": "Bad request"}
        mock_post.return_value = mock_response

        validate(self.params, ExportAttributesInput.schema)
        with self.assertRaises(PluginException) as context:
            self.action.run(self.params)
        self.assertTrue(PluginException.causes[PluginException.Preset.BAD_REQUEST] in context.exception.cause)
