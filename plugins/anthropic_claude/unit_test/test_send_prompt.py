import os
import sys
import unittest
from unittest.mock import patch

sys.path.append(os.path.abspath("../"))

from insightconnect_plugin_runtime.exceptions import PluginException
from parameterized import parameterized

from komand_anthropic_claude.actions.send_prompt.action import SendPrompt
from komand_anthropic_claude.actions.send_prompt.schema import Input
from unit_test.util import MockResponse, default_connector


class TestSendPrompt(unittest.TestCase):
    def setUp(self):
        self.action = default_connector(SendPrompt())

    @parameterized.expand(
        [
            (
                "basic_prompt",
                {
                    Input.PROMPT: "Analyze this suspicious email header",
                    Input.MAX_TOKENS: 4096,
                },
                "send_prompt_success.json",
            ),
            (
                "with_system_prompt",
                {
                    Input.PROMPT: "Analyze this suspicious email header",
                    Input.SYSTEM_PROMPT: "You are a senior SOC analyst",
                    Input.MAX_TOKENS: 4096,
                },
                "send_prompt_success.json",
            ),
        ]
    )
    @patch("requests.Session.request")
    def test_send_prompt_success(self, _name, params, fixture, mock_request):
        mock_request.return_value = MockResponse(200, fixture)
        result = self.action.run(params)

        self.assertIn("response", result)
        self.assertIn("model", result)
        self.assertIsInstance(result["response"], str)
        self.assertTrue(len(result["response"]) > 0)
        self.assertEqual(result["model"], "claude-sonnet-4-6")

    @parameterized.expand(
        [
            ("unauthorized", 401),
            ("forbidden", 403),
            ("not_found", 404),
            ("rate_limited", 429),
            ("server_error", 500),
            ("service_unavailable", 503),
        ]
    )
    @patch("requests.Session.request")
    def test_send_prompt_errors(self, _name, status_code, mock_request):
        mock_request.return_value = MockResponse(status_code)
        with self.assertRaises(PluginException):
            self.action.run(
                {
                    Input.PROMPT: "test prompt",
                    Input.MAX_TOKENS: 4096,
                }
            )


if __name__ == "__main__":
    unittest.main()
