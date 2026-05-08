import os
import sys
import unittest
from unittest.mock import patch

sys.path.append(os.path.abspath("../"))

from insightconnect_plugin_runtime.exceptions import PluginException
from parameterized import parameterized

from komand_anthropic_claude.actions.count_tokens.action import CountTokens
from komand_anthropic_claude.actions.count_tokens.schema import Input
from unit_test.util import MockResponse, default_connector


class TestCountTokens(unittest.TestCase):
    def setUp(self):
        self.action = default_connector(CountTokens())

    @parameterized.expand(
        [
            (
                "basic_count",
                {
                    Input.PROMPT: "Analyze this log file for suspicious activity",
                },
                "count_tokens_success.json",
            ),
            (
                "count_with_system_prompt",
                {
                    Input.PROMPT: "Analyze this log file for suspicious activity",
                    Input.SYSTEM_PROMPT: "You are a security analyst",
                },
                "count_tokens_success.json",
            ),
        ]
    )
    @patch("requests.Session.request")
    def test_count_tokens_success(self, _name, params, fixture, mock_request):
        mock_request.return_value = MockResponse(200, fixture)
        result = self.action.run(params)

        self.assertIn("input_tokens", result)
        self.assertIsInstance(result["input_tokens"], int)
        self.assertGreater(result["input_tokens"], 0)

    @parameterized.expand(
        [
            ("unauthorized", 401),
            ("forbidden", 403),
            ("rate_limited", 429),
            ("server_error", 500),
        ]
    )
    @patch("requests.Session.request")
    def test_count_tokens_errors(self, _name, status_code, mock_request):
        mock_request.return_value = MockResponse(status_code)
        with self.assertRaises(PluginException):
            self.action.run(
                {
                    Input.PROMPT: "test prompt",
                }
            )


if __name__ == "__main__":
    unittest.main()
