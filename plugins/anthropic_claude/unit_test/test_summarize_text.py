import os
import sys
import unittest
from unittest.mock import patch

sys.path.append(os.path.abspath("../"))

from insightconnect_plugin_runtime.exceptions import PluginException
from parameterized import parameterized

from komand_anthropic_claude.actions.summarize_text.action import SummarizeText
from komand_anthropic_claude.actions.summarize_text.schema import Input
from unit_test.util import MockResponse, default_connector


class TestSummarizeText(unittest.TestCase):
    def setUp(self):
        self.action = default_connector(SummarizeText())

    @parameterized.expand(
        [
            (
                "basic_summary",
                {
                    Input.TEXT: "Multiple failed login attempts detected from IP 10.0.0.5 targeting user accounts.",
                    Input.MAX_TOKENS: 2048,
                },
                "summarize_text_success.json",
            ),
            (
                "summary_with_focus",
                {
                    Input.TEXT: "Multiple failed login attempts detected from IP 10.0.0.5 targeting user accounts.",
                    Input.FOCUS: "key findings and recommended actions",
                    Input.MAX_TOKENS: 2048,
                },
                "summarize_text_success.json",
            ),
        ]
    )
    @patch("requests.Session.request")
    def test_summarize_text_success(self, _name, params, fixture, mock_request):
        mock_request.return_value = MockResponse(200, fixture)
        result = self.action.run(params)

        self.assertIn("summary", result)
        self.assertIn("model", result)
        self.assertIsInstance(result["summary"], str)
        self.assertTrue(len(result["summary"]) > 0)
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
    def test_summarize_text_errors(self, _name, status_code, mock_request):
        mock_request.return_value = MockResponse(status_code)
        with self.assertRaises(PluginException):
            self.action.run(
                {
                    Input.TEXT: "test text to summarize",
                    Input.MAX_TOKENS: 2048,
                }
            )


if __name__ == "__main__":
    unittest.main()
