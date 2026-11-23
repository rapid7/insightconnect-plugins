import sys
import os

sys.path.append(os.path.abspath("../"))

import logging
from unittest import TestCase
from unittest.mock import patch

import requests
from insightconnect_plugin_runtime.exceptions import PluginException

from icon_bitdefender_gravityzone.util.api import (
    DEFAULT_RETRY_AFTER,
    MAX_ERROR_BODY_LENGTH,
    MAX_RATE_LIMIT_RETRIES,
    BitdefenderGravityZoneAPI,
)
from util import STUB_API_KEY, STUB_URL, Util


@patch("icon_bitdefender_gravityzone.util.api.time.sleep")
@patch("requests.Session.send")
class TestApi(TestCase):
    def setUp(self) -> None:
        self.api = BitdefenderGravityZoneAPI(STUB_URL, STUB_API_KEY, logging.getLogger("api logger"))

    def test_rate_limit_is_retried_after_retry_after(self, mock_send, mock_sleep):
        mock_send.side_effect = [
            Util.response(status_code=429, text="Too many requests", headers={"Retry-After": "2"}),
            Util.payload_response("get_endpoints_list.json.resp"),
        ]

        result = self.api.get_endpoints_list()

        self.assertEqual(2, result["total"])
        self.assertEqual(2, mock_send.call_count)
        mock_sleep.assert_called_once_with(2)

    def test_rate_limit_retry_after_fallback(self, mock_send, mock_sleep):
        cases = [("missing header", {}), ("not a number", {"Retry-After": "soon"})]
        for name, headers in cases:
            with self.subTest(name):
                mock_send.reset_mock(side_effect=True)
                mock_sleep.reset_mock()
                mock_send.side_effect = [
                    Util.response(status_code=429, text="Too many requests", headers=headers),
                    Util.payload_response("get_endpoints_list.json.resp"),
                ]

                self.api.get_endpoints_list()

                mock_sleep.assert_called_once_with(DEFAULT_RETRY_AFTER)

    def test_rate_limit_retries_are_bounded(self, mock_send, mock_sleep):
        mock_send.return_value = Util.response(
            status_code=429, text="Rate limit exceeded", headers={"Retry-After": "1"}
        )

        with self.assertRaises(PluginException) as context:
            self.api.get_endpoints_list()

        self.assertEqual(MAX_RATE_LIMIT_RETRIES + 1, mock_send.call_count)
        self.assertEqual(MAX_RATE_LIMIT_RETRIES, mock_sleep.call_count)
        self.assertEqual("GravityZone rate limit exceeded (HTTP 429).", context.exception.cause)
        self.assertEqual("Rate limit exceeded", context.exception.data)

    def test_rate_limit_with_long_retry_after_is_not_retried(self, mock_send, mock_sleep):
        mock_send.return_value = Util.response(
            status_code=429, text="Rate limit exceeded", headers={"Retry-After": "120"}
        )

        with self.assertRaises(PluginException) as context:
            self.api.get_endpoints_list()

        self.assertEqual(1, mock_send.call_count)
        mock_sleep.assert_not_called()
        self.assertEqual("GravityZone rate limit exceeded (HTTP 429).", context.exception.cause)

    def test_http_errors_carry_the_response_body(self, mock_send, mock_sleep):
        cases = [
            ("forbidden", 403, "Forbidden", "The API key is not allowed to use this GravityZone API (HTTP 403)."),
            ("not found", 404, "Not Found", "The GravityZone API was not found at the configured URL (HTTP 404)."),
            ("server error", 500, '{"error": "internal"}', "GravityZone returned HTTP 500."),
            ("bad gateway", 502, "<html>Bad Gateway</html>", "GravityZone returned HTTP 502."),
        ]
        for name, status_code, body, expected_cause in cases:
            with self.subTest(name):
                mock_send.return_value = Util.response(status_code=status_code, text=body)

                with self.assertRaises(PluginException) as context:
                    self.api.get_endpoints_list()

                self.assertEqual(expected_cause, context.exception.cause)
                self.assertTrue(context.exception.assistance)
                self.assertEqual(body, context.exception.data)
        mock_sleep.assert_not_called()

    def test_long_error_body_is_truncated(self, mock_send, mock_sleep):
        body = "x" * (MAX_ERROR_BODY_LENGTH + 500)
        mock_send.return_value = Util.response(status_code=500, text=body)

        with self.assertRaises(PluginException) as context:
            self.api.get_endpoints_list()

        self.assertTrue(context.exception.data.startswith("x" * MAX_ERROR_BODY_LENGTH + "... (truncated"))
        self.assertLess(len(context.exception.data), len(body))

    def test_invalid_responses(self, mock_send, mock_sleep):
        cases = [
            ("not JSON", "<html>login</html>", "GravityZone returned a response that is not JSON."),
            ("JSON but not an object", "[1, 2]", "GravityZone returned a response that is not a JSON-RPC object."),
        ]
        for name, body, expected_cause in cases:
            with self.subTest(name):
                mock_send.return_value = Util.response(status_code=200, text=body)

                with self.assertRaises(PluginException) as context:
                    self.api.get_endpoints_list()

                self.assertEqual(expected_cause, context.exception.cause)
                self.assertEqual(body, context.exception.data)

    def test_transport_errors(self, mock_send, mock_sleep):
        cases = [
            ("timeout", requests.exceptions.ReadTimeout("read timed out"), "The request to GravityZone timed out."),
            ("connection", requests.exceptions.ConnectionError("refused"), "Unable to connect to GravityZone."),
            ("other", requests.exceptions.InvalidURL("bad url"), "The request to GravityZone failed."),
        ]
        for name, error, expected_cause in cases:
            with self.subTest(name):
                mock_send.side_effect = error

                with self.assertRaises(PluginException) as context:
                    self.api.get_endpoints_list()

                self.assertEqual(expected_cause, context.exception.cause)
                self.assertEqual(str(error), context.exception.data)

    def test_json_rpc_errors(self, mock_send, mock_sleep):
        cases = [
            ("authorization", -32001, "Authorization error.", "Network API and the Incidents API"),
            ("not found", -32002, "Resource not found", "endpoint ID is correct"),
            ("invalid params", -32602, "Invalid params", "GravityZone rejected one of the parameters"),
            ("other code", -32000, "Server error", "Check the action input and the API key permissions"),
        ]
        for name, code, message, expected_assistance in cases:
            with self.subTest(name):
                mock_send.return_value = Util.rpc_error(code, message, "details from GravityZone")

                with self.assertRaises(PluginException) as context:
                    self.api.get_endpoints_list()

                self.assertEqual(f"GravityZone API error {code}: {message.rstrip('.')}.", context.exception.cause)
                self.assertIn(expected_assistance, context.exception.assistance)
                self.assertIn("details from GravityZone", context.exception.data)
