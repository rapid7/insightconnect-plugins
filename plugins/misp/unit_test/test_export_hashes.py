import base64
import os
import sys
import unittest
from unittest.mock import patch, MagicMock

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))
from komand_misp.actions.export_hashes.action import ExportHashes


class TestExportHashes(unittest.TestCase):
    def setUp(self):
        self.action = ExportHashes()
        self.action.connection = MagicMock()
        self.action.logger = MagicMock()
        self.mock_client = MagicMock()
        self.action.connection.key = "api_key"
        self.action.connection.url = "http://example.com"

        self.params = {"format": "md5", "tags": ["testTag"], "from": "2020-01-01", "to": "2020-12-31", "last": "5d"}

    @patch("komand_misp.actions.export_hashes.action.requests.get")
    def test_export_hashes_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = "hash1,hash2,hash3"
        mock_get.return_value = mock_response

        result = self.action.run(self.params)
        expected_hashes = base64.b64encode("hash1,hash2,hash3".encode("ascii")).decode("utf-8")
        self.assertEqual(result, {"hashes": expected_hashes})

    @patch("komand_misp.actions.export_hashes.action.requests.get")
    def test_export_hashes_failure(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_response.json.return_value = {"message": "Bad request"}
        mock_get.return_value = mock_response

        with self.assertRaises(PluginException) as context:
            self.action.run(self.params)
        self.assertTrue(PluginException.causes[PluginException.Preset.BAD_REQUEST] in context.exception.cause)
