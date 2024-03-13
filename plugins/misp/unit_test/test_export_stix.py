import base64
import os
import sys
import unittest
from unittest.mock import patch, MagicMock

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))
from komand_misp.actions.export_stix.action import ExportStix


class TestExportStix(unittest.TestCase):
    def setUp(self):
        self.action = ExportStix()
        self.action.connection = MagicMock()
        self.action.logger = MagicMock()
        self.mock_client = MagicMock()
        self.action.connection.key = "api_key"
        self.action.connection.url = "http://example.com"

        self.params = {
            "event_id": "1",
            "encode_attachments": False,
            "tags": ["tag1", "tag2"],
            "from": "2020-01-01",
            "to": "2020-12-31",
            "last": "5d",
        }

    @patch("komand_misp.actions.export_stix.action.requests.post")
    def test_export_stix_success(self, mock_post):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = "<stix></stix>"
        mock_post.return_value = mock_response

        result = self.action.run(self.params)
        expected_stix = base64.b64encode("<stix></stix>".encode("ascii")).decode("utf-8")
        self.assertEqual(result, {"stix": expected_stix})

    @patch("komand_misp.actions.export_stix.action.requests.post")
    def test_export_stix_failure(self, mock_post):
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_response.json.return_value = {"message": "Bad request"}
        mock_post.return_value = mock_response

        with self.assertRaises(PluginException) as context:
            self.action.run(self.params)
        self.assertTrue(PluginException.causes[PluginException.Preset.BAD_REQUEST] == context.exception.cause)
