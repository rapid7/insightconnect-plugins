import base64
import os
import sys
import unittest
from unittest.mock import patch, MagicMock

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))
from komand_misp.actions.export_rules.action import ExportRules


class TestExportRules(unittest.TestCase):
    def setUp(self):
        self.action = ExportRules()
        self.action.connection = MagicMock()
        self.action.logger = MagicMock()
        self.mock_client = MagicMock()
        self.action.connection.key = "api_key"
        self.action.connection.url = "http://example.com"

        self.params = {
            "format": "snort",
            "event_id": "event_id",
            "frame": "frame",
            "tags": ["tag1", "tag2"],
            "from": "2020-01-01",
            "to": "2020-12-31",
            "last": "5d",
        }

    @patch("komand_misp.actions.export_rules.action.requests.get")
    def test_export_rules_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = "rule1\nrule2\nrule3"
        mock_get.return_value = mock_response

        result = self.action.run(self.params)
        expected_rules = base64.b64encode("rule1\nrule2\nrule3".encode("ascii")).decode("utf-8")
        self.assertEqual(result, {"rules": expected_rules})

    @patch("komand_misp.actions.export_rules.action.requests.get")
    def test_export_rules_failure(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 400
        mock_response.json.return_value = {"message": "Bad request"}
        mock_get.return_value = mock_response

        with self.assertRaises(PluginException) as context:
            self.action.run(self.params)
        self.assertTrue(PluginException.causes[PluginException.Preset.BAD_REQUEST] in context.exception.cause)
