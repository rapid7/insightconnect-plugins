import os
import sys
import unittest
from unittest.mock import patch, MagicMock

from insightconnect_plugin_runtime.exceptions import PluginException
from requests.exceptions import HTTPError

sys.path.append(os.path.abspath("../"))
from komand_misp.actions.download_attachment.action import DownloadAttachment


class TestDownloadAttachment(unittest.TestCase):
    def setUp(self):
        self.action = DownloadAttachment()
        self.action.connection = MagicMock()
        self.action.logger = MagicMock()
        self.action.connection.url = "http://example.com"
        self.action.connection.key = "api_key"

        self.params = {"attribute_id": "12345"}

    @patch("komand_misp.actions.download_attachment.action.requests.get")
    def test_download_attachment_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.content = b"test attachment data"
        mock_response.json.return_value = {"message": "Success"}
        mock_get.return_value = mock_response

        result = self.action.run(self.params)
        self.assertEqual(result, {"attachment": "dGVzdCBhdHRhY2htZW50IGRhdGE="})

    @patch("komand_misp.actions.download_attachment.action.requests.get")
    def test_download_attachment_not_found(self, mock_get):
        mock_response = MagicMock()
        mock_response.json.return_value = {"message": "Attribute ID did not contain an attachment"}
        mock_get.return_value = mock_response
        mock_get.side_effect = ValueError("Attribute ID did not contain an attachment")

        with self.assertRaises(PluginException) as context:
            self.action.run(self.params)
        self.assertEqual(context.exception.cause, "Invalid or unreachable endpoint provided.")

    @patch("komand_misp.actions.download_attachment.action.requests.get")
    def test_download_attachment_http_error(self, mock_get):
        mock_response = MagicMock()
        mock_response.raise_for_status.side_effect = HTTPError("HTTP Error")
        mock_get.return_value = mock_response

        with self.assertRaises(PluginException) as context:
            self.action.run(self.params)
        self.assertTrue(PluginException.causes[PluginException.Preset.UNKNOWN] in context.exception.cause)
