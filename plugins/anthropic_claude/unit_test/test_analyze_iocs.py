import os
import sys
import unittest
from unittest.mock import patch

sys.path.append(os.path.abspath("../"))

from insightconnect_plugin_runtime.exceptions import PluginException
from parameterized import parameterized

from komand_anthropic_claude.actions.analyze_iocs.action import AnalyzeIocs
from komand_anthropic_claude.actions.analyze_iocs.schema import Input
from unit_test.util import MockResponse, default_connector


class TestAnalyzeIocs(unittest.TestCase):
    def setUp(self):
        self.action = default_connector(AnalyzeIocs())

    @parameterized.expand(
        [
            (
                "basic_iocs",
                {
                    Input.INDICATORS: ["192.168.1.100", "evil-domain.com", "44d88612fea8a8f36de82e1278abb02f"],
                    Input.MAX_TOKENS: 4096,
                },
                "analyze_iocs_success.json",
            ),
            (
                "iocs_with_context",
                {
                    Input.INDICATORS: ["10.0.0.5", "malware.exe"],
                    Input.CONTEXT: "Found in email attachment from unknown sender",
                    Input.MAX_TOKENS: 4096,
                },
                "analyze_iocs_success.json",
            ),
        ]
    )
    @patch("requests.Session.request")
    def test_analyze_iocs_success(self, _name, params, fixture, mock_request):
        mock_request.return_value = MockResponse(200, fixture)
        result = self.action.run(params)

        self.assertIn("analysis", result)
        self.assertIn("model", result)
        self.assertIsInstance(result["analysis"], str)
        self.assertTrue(len(result["analysis"]) > 0)
        self.assertEqual(result["model"], "claude-sonnet-4-6")

    @parameterized.expand(
        [
            ("unauthorized", 401),
            ("forbidden", 403),
            ("rate_limited", 429),
            ("server_error", 500),
        ]
    )
    @patch("requests.Session.request")
    def test_analyze_iocs_errors(self, _name, status_code, mock_request):
        mock_request.return_value = MockResponse(status_code)
        with self.assertRaises(PluginException):
            self.action.run(
                {
                    Input.INDICATORS: ["192.168.1.100"],
                    Input.MAX_TOKENS: 4096,
                }
            )


if __name__ == "__main__":
    unittest.main()
