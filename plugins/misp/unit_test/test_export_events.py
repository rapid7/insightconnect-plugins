import base64
import os
import sys
import unittest
from unittest.mock import patch, MagicMock

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))
from komand_misp.actions.export_events.action import ExportEvents


class TestExportEvents(unittest.TestCase):
    def setUp(self):
        self.action = ExportEvents()
        self.action.connection = MagicMock()
        self.action.logger = MagicMock()
        self.mock_client = MagicMock()
        self.action.connection.key = "api_key"
        self.action.connection.url = "http://example.com"

        self.params = {
            "event_id": "event_id",
            "encode_attachments": True,
            "tags": "tag1,tag2",
            "from": "2020-01-01",
            "to": "2020-12-31",
            "last": "5d",
        }

    @patch("komand_misp.actions.export_events.action.requests.post")
    def test_export_events_success(self, mock_post):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = "<events></events>"
        mock_post.return_value = mock_response

        result = self.action.run(self.params)
        expected_events = base64.b64encode("<events></events>".encode("ascii")).decode("utf-8")
        self.assertEqual(result, {"events": expected_events})

    @patch("komand_misp.actions.export_events.action.requests.post")
    def test_export_events_failure(self, mock_post):
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_response.json.return_value = {"message": "Bad request"}
        mock_post.return_value = mock_response

        with self.assertRaises(PluginException) as context:
            self.action.run(self.params)
        self.assertTrue(PluginException.causes[PluginException.Preset.BAD_REQUEST] in context.exception.cause)
