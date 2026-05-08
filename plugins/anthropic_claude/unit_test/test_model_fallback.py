import json
import logging
import os
import sys
import unittest
from unittest.mock import patch

sys.path.append(os.path.abspath("../"))

from insightconnect_plugin_runtime.exceptions import PluginException
from parameterized import parameterized

from komand_anthropic_claude.actions.send_prompt.action import SendPrompt
from komand_anthropic_claude.actions.send_prompt.schema import Input
from komand_anthropic_claude.connection.connection import Connection
from komand_anthropic_claude.connection.schema import Input as ConnectionInput
from komand_anthropic_claude.util.constants import FALLBACK_MODEL
from unit_test.util import MockResponse


def connector_with_model(action, model):
    """Create a connector with a specific model for testing fallback behavior."""
    connection = Connection()
    connection.logger = logging.getLogger("test")
    params = {
        ConnectionInput.API_KEY: {"secretKey": "sk-ant-api03-test-key"},
        ConnectionInput.MODEL: model,
    }
    connection.connect(params)
    action.connection = connection
    action.logger = connection.logger
    return action


class TestModelFallback(unittest.TestCase):
    def setUp(self):
        self.action = connector_with_model(SendPrompt(), "claude-3-opus-20240229")

    @patch("requests.Session.request")
    def test_fallback_on_invalid_model(self, mock_request):
        """When the configured model is invalid, the plugin should fall back to the latest alias."""
        model_error_response = MockResponse(404, "model_not_found.json")
        success_response = MockResponse(200, "send_prompt_success.json")
        mock_request.side_effect = [model_error_response, success_response]

        result = self.action.run(
            {
                Input.PROMPT: "test prompt",
                Input.MAX_TOKENS: 4096,
            }
        )

        self.assertIn("response", result)
        self.assertEqual(mock_request.call_count, 2)

        # Verify the second call used the fallback model
        second_call_body = mock_request.call_args_list[1][1].get("json", {})
        self.assertEqual(second_call_body.get("model"), FALLBACK_MODEL)

    @patch("requests.Session.request")
    def test_no_fallback_when_model_is_valid(self, mock_request):
        """When the configured model works, no fallback should occur."""
        mock_request.return_value = MockResponse(200, "send_prompt_success.json")

        result = self.action.run(
            {
                Input.PROMPT: "test prompt",
                Input.MAX_TOKENS: 4096,
            }
        )

        self.assertIn("response", result)
        self.assertEqual(mock_request.call_count, 1)

    @patch("requests.Session.request")
    def test_no_fallback_when_already_using_fallback_model(self, mock_request):
        """When the fallback model itself fails, don't retry infinitely."""
        self.action = connector_with_model(SendPrompt(), FALLBACK_MODEL)
        mock_request.return_value = MockResponse(404, "model_not_found.json")

        with self.assertRaises(PluginException):
            self.action.run(
                {
                    Input.PROMPT: "test prompt",
                    Input.MAX_TOKENS: 4096,
                }
            )

        # Should only try once since we're already on the fallback model
        self.assertEqual(mock_request.call_count, 1)

    @patch("requests.Session.request")
    def test_non_model_error_does_not_trigger_fallback(self, mock_request):
        """Auth errors and other non-model errors should not trigger fallback."""
        mock_request.return_value = MockResponse(401)

        with self.assertRaises(PluginException):
            self.action.run(
                {
                    Input.PROMPT: "test prompt",
                    Input.MAX_TOKENS: 4096,
                }
            )

        # Should only try once — auth errors are not model errors
        self.assertEqual(mock_request.call_count, 1)

    @patch("requests.Session.request")
    def test_new_model_works_without_update(self, mock_request):
        """A brand new model (e.g., claude-opus-5) should work if the API accepts it."""
        self.action = connector_with_model(SendPrompt(), "claude-opus-5-20260115")
        mock_request.return_value = MockResponse(200, "send_prompt_success.json")

        result = self.action.run(
            {
                Input.PROMPT: "test prompt",
                Input.MAX_TOKENS: 4096,
            }
        )

        self.assertIn("response", result)
        self.assertEqual(mock_request.call_count, 1)

        # Verify it used the new model, not the fallback
        call_body = mock_request.call_args[1].get("json", {})
        self.assertEqual(call_body.get("model"), "claude-opus-5-20260115")


if __name__ == "__main__":
    unittest.main()
