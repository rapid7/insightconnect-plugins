from unittest import TestCase
from unittest.mock import patch

from insightconnect_plugin_runtime.exceptions import PluginException
from requests.exceptions import ConnectionError as RequestsConnectionError
from requests.exceptions import Timeout

from icon_ipgeolocation_io.util.api import IPGeolocationAPI
from icon_ipgeolocation_io.util.constants import MAX_RETRIES
from unit_test.mock import (
    IP_MALFORMED_BODY,
    IP_RATE_LIMITED,
    IP_SERVER_ERROR,
    IP_UNKNOWN,
    MockResponse,
    STUB_API_KEY,
    mock_request,
)
import os
import sys

sys.path.append(os.path.abspath("../"))

import logging


def build_api() -> IPGeolocationAPI:
    return IPGeolocationAPI(api_key=STUB_API_KEY, logger=logging.getLogger("test-api"))


@patch("icon_ipgeolocation_io.util.api.time.sleep", return_value=None)
class TestApiTransport(TestCase):
    @patch("requests.Session.request", side_effect=mock_request)
    def test_api_key_is_sent_as_query_parameter(self, mocked, _sleep):
        build_api().ip_security({"ip": "2.56.188.34"})

        self.assertEqual(mocked.call_args.kwargs["params"]["apiKey"], STUB_API_KEY)

    @patch("requests.Session.request", side_effect=mock_request)
    def test_api_key_is_never_logged(self, _, _sleep):
        logger = logging.getLogger("test-api-redaction")
        api = IPGeolocationAPI(api_key=STUB_API_KEY, logger=logger)

        with self.assertLogs(logger, level="INFO") as captured:
            api.ip_security({"ip": "2.56.188.34"})

        self.assertNotIn(STUB_API_KEY, "\n".join(captured.output))

    @patch("requests.Session.request", side_effect=mock_request)
    def test_none_valued_parameters_are_dropped(self, mocked, _sleep):
        build_api().ip_geolocation({"ip": "8.8.8.8", "include": None, "lang": None})

        params = mocked.call_args.kwargs["params"]
        self.assertNotIn("include", params)
        self.assertNotIn("lang", params)

    @patch("requests.Session.request", side_effect=mock_request)
    def test_404_maps_to_not_found_message(self, _, _sleep):
        with self.assertRaises(PluginException) as context:
            build_api().ip_security({"ip": IP_UNKNOWN})

        self.assertIn("no record", context.exception.cause)
        self.assertIn("not found in our database", context.exception.cause)

    @patch("requests.Session.request", side_effect=mock_request)
    def test_rate_limit_is_retried_then_raised(self, mocked, _sleep):
        with self.assertRaises(PluginException) as context:
            build_api().ip_security({"ip": IP_RATE_LIMITED})

        self.assertEqual(mocked.call_count, MAX_RETRIES)
        self.assertIn("usage limit", context.exception.cause)

    @patch("requests.Session.request", side_effect=mock_request)
    def test_server_error_is_retried_then_raised(self, mocked, _sleep):
        with self.assertRaises(PluginException) as context:
            build_api().ip_security({"ip": IP_SERVER_ERROR})

        self.assertEqual(mocked.call_count, MAX_RETRIES)
        self.assertIn("server error (500)", context.exception.cause)

    @patch("requests.Session.request", side_effect=mock_request)
    def test_unparsable_body_raises_invalid_json(self, _, _sleep):
        with self.assertRaises(PluginException) as context:
            build_api().ip_security({"ip": IP_MALFORMED_BODY})

        self.assertIn("<html>gateway</html>", context.exception.data)

    def test_transient_server_error_recovers_on_retry(self, _sleep):
        responses = [
            MockResponse(status_code=503, payload={"message": "Service Unavailable"}),
            MockResponse(status_code=200, payload={"ip": "8.8.8.8", "security": {"threat_score": 0}}),
        ]

        with patch("requests.Session.request", side_effect=responses) as mocked:
            result = build_api().ip_security({"ip": "8.8.8.8"})

        self.assertEqual(mocked.call_count, 2)
        self.assertEqual(result["ip"], "8.8.8.8")

    def test_timeout_is_retried_then_raised(self, _sleep):
        with patch("requests.Session.request", side_effect=Timeout("timed out")) as mocked:
            with self.assertRaises(PluginException) as context:
                build_api().ip_security({"ip": "8.8.8.8"})

        self.assertEqual(mocked.call_count, MAX_RETRIES)
        self.assertIn("timed out", context.exception.cause.lower())

    def test_connection_error_is_retried_then_raised(self, _sleep):
        with patch("requests.Session.request", side_effect=RequestsConnectionError("no route")) as mocked:
            with self.assertRaises(PluginException):
                build_api().ip_security({"ip": "8.8.8.8"})

        self.assertEqual(mocked.call_count, MAX_RETRIES)

    def test_retry_after_header_is_honoured(self, sleep_mock):
        responses = [
            MockResponse(status_code=429, payload={"message": "slow down"}, headers={"Retry-After": "7"}),
            MockResponse(status_code=200, payload={"ip": "8.8.8.8", "security": {}}),
        ]

        with patch("requests.Session.request", side_effect=responses):
            build_api().ip_security({"ip": "8.8.8.8"})

        sleep_mock.assert_called_once_with(7)

    def test_absurd_retry_after_is_capped(self, sleep_mock):
        responses = [
            MockResponse(status_code=429, payload={"message": "slow down"}, headers={"Retry-After": "99999"}),
            MockResponse(status_code=200, payload={"ip": "8.8.8.8", "security": {}}),
        ]

        with patch("requests.Session.request", side_effect=responses):
            build_api().ip_security({"ip": "8.8.8.8"})

        sleep_mock.assert_called_once_with(60)
