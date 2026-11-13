import logging
import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock, patch

import requests

from icon_whoisfreaks.util import constants
from icon_whoisfreaks.util.client import FEED_RETRY, LOOKUP_RETRY, WhoisFreaksClient
from icon_whoisfreaks.util.errors import Kind, WhoisFreaksError
from util import API_KEY, FakeSession, MockResponse


def make_client(*responses) -> tuple:
    client = WhoisFreaksClient(API_KEY, logging.getLogger("client"), sleep=MagicMock())
    session = FakeSession(*responses)
    client._session = lambda: session
    return client, session


class TestLookupRequests(TestCase):
    def test_key_only_in_header_and_redirects_disabled(self):
        client, session = make_client(MockResponse(200, {"ok": True}))
        result = client.lookup("Test", "GET", "/v1.0/test", {"a": None, "b": "", "c": True, "d": 0})
        call = session.calls[0]
        self.assertEqual({"c": "true", "d": 0}, call["params"])
        self.assertEqual(API_KEY, call["headers"]["X-API-KEY"])
        self.assertFalse(call["allow_redirects"])
        self.assertTrue(call["stream"])
        self.assertEqual(constants.LOOKUP_TIMEOUT, call["timeout"])
        self.assertEqual({"ok": True}, result.data)

    def test_retries_server_errors_then_succeeds(self):
        client, session = make_client(MockResponse(503), MockResponse(502), MockResponse(200, {"ok": 1}))
        self.assertTrue(client.lookup("Test", "GET", "/x").found)
        self.assertEqual(3, len(session.calls))
        self.assertEqual(2, client._sleep.call_count)

    def test_gives_up_after_max_attempts(self):
        client, session = make_client(MockResponse(500, {"message": "Internal error"}))
        with self.assertRaises(WhoisFreaksError) as context:
            client.lookup("Test", "GET", "/x")
        self.assertEqual(Kind.SERVER_ERROR, context.exception.kind)
        self.assertEqual(LOOKUP_RETRY.max_attempts, len(session.calls))

    def test_rate_limit_waits_for_reset_header(self):
        headers = {"X-RateLimit-Remaining-Time": "7500000000", "X-RateLimit-Remaining-Requests": "0"}
        client, _ = make_client(MockResponse(429, {"message": "slow down"}, headers), MockResponse(200, {}))
        client.lookup("Test", "GET", "/x")
        delay = client._sleep.call_args_list[0][0][0]
        self.assertGreaterEqual(delay, 7.5)
        self.assertLess(delay, 8.6)

    def test_retry_after_header_and_cap(self):
        client, _ = make_client(MockResponse(429, {}, {"Retry-After": "9999"}), MockResponse(200, {}))
        client.lookup("Test", "GET", "/x")
        self.assertLessEqual(client._sleep.call_args_list[0][0][0], LOOKUP_RETRY.max_delay + 1)

    def test_non_retryable_errors_are_raised_immediately(self):
        client, session = make_client(MockResponse(400, {"message": "Invalid domain"}))
        with self.assertRaises(WhoisFreaksError) as context:
            client.lookup("Test", "GET", "/x")
        self.assertEqual(Kind.BAD_REQUEST, context.exception.kind)
        self.assertEqual(1, len(session.calls))
        self.assertIn("Invalid domain", context.exception.cause)

    def test_not_found_is_returned(self):
        client, _ = make_client(MockResponse(404, "plain text"))
        result = client.lookup("Test", "GET", "/x")
        self.assertFalse(result.found)
        self.assertEqual("plain text", result.message)

    def test_route_missing_is_an_error(self):
        client, _ = make_client(MockResponse(404, {"message": "Internal Server Error occurred"}))
        with self.assertRaises(WhoisFreaksError) as context:
            client.lookup("Test", "GET", "/x")
        self.assertEqual(Kind.SERVER_ERROR, context.exception.kind)

    def test_redirect_is_not_followed(self):
        client, session = make_client(MockResponse(302, "", {"Location": "https://elsewhere.example"}))
        with self.assertRaises(WhoisFreaksError) as context:
            client.lookup("Test", "GET", "/x")
        self.assertEqual(Kind.REDIRECT, context.exception.kind)
        self.assertEqual(1, len(session.calls))

    def test_invalid_json(self):
        client, _ = make_client(MockResponse(200, "<html>"))
        with self.assertRaises(WhoisFreaksError) as context:
            client.lookup("Test", "GET", "/x")
        self.assertEqual(Kind.INVALID_RESPONSE, context.exception.kind)

    def test_body_size_limit(self):
        client, _ = make_client(MockResponse(200, b"x" * 70000))
        with patch.object(constants, "MAX_LOOKUP_BODY_BYTES", 65536), self.assertRaises(WhoisFreaksError) as context:
            client.lookup("Test", "GET", "/x")
        self.assertEqual(Kind.INVALID_RESPONSE, context.exception.kind)

    def test_api_key_is_redacted_from_messages(self):
        body = {"message": f"bad key {API_KEY}", "path": f"/x?apiKey={API_KEY}"}
        client, _ = make_client(MockResponse(401, body))
        with self.assertRaises(WhoisFreaksError) as context:
            client.lookup("Test", "GET", "/x")
        self.assertNotIn(API_KEY, str(context.exception))
        self.assertEqual(Kind.INVALID_CREDENTIALS, context.exception.kind)

    def test_proactive_throttle(self):
        headers = {"X-RateLimit-Remaining-Requests": "0", "X-RateLimit-Remaining-Time": "3000000000"}
        client, _ = make_client(MockResponse(200, {}, headers))
        client.lookup("Test", "GET", "/x")
        client.lookup("Test", "GET", "/x")
        self.assertEqual(1, client._sleep.call_count)
        self.assertGreater(client._sleep.call_args[0][0], 2)

    def test_malformed_rate_limit_headers_are_ignored(self):
        headers = {"X-RateLimit-Remaining-Requests": "none", "X-RateLimit-Remaining-Time": "soon", "Retry-After": "x"}
        client, _ = make_client(MockResponse(200, {}, headers))
        client.lookup("Test", "GET", "/x")
        client.lookup("Test", "GET", "/x")
        client._sleep.assert_not_called()


class TestTransportErrors(TestCase):
    def check(self, exception, kind, method="GET", expected_calls=LOOKUP_RETRY.max_attempts):
        client, session = make_client(exception)
        with self.assertRaises(WhoisFreaksError) as context:
            client.lookup("Test", method, "/x", body={"a": 1} if method == "POST" else None)
        self.assertEqual(kind, context.exception.kind)
        self.assertEqual(expected_calls, len(session.calls))
        self.assertNotIn(API_KEY, str(context.exception))
        self.assertNotIn("https://", context.exception.cause)

    def test_connection_error(self):
        self.check(requests.exceptions.ConnectionError("Max retries exceeded with url: /x"), Kind.NETWORK)

    def test_tls_error_is_not_retried(self):
        self.check(requests.exceptions.SSLError("certificate verify failed"), Kind.TLS, expected_calls=1)

    def test_read_timeout(self):
        self.check(requests.exceptions.ReadTimeout("read timed out"), Kind.TIMEOUT)

    def test_post_read_timeout_is_not_retried(self):
        self.check(requests.exceptions.ReadTimeout("read timed out"), Kind.TIMEOUT, "POST", 1)

    def test_post_connect_timeout_is_retried(self):
        self.check(requests.exceptions.ConnectTimeout("connect timed out"), Kind.TIMEOUT, "POST")

    def test_post_new_connection_error_is_retried(self):
        self.check(requests.exceptions.ConnectionError("NewConnectionError(refused)"), Kind.NETWORK, "POST")

    def test_too_many_redirects(self):
        self.check(requests.exceptions.TooManyRedirects("loop"), Kind.REDIRECT, expected_calls=1)

    def test_error_while_reading_body(self):
        response = MockResponse(200, {})
        response.iter_content = MagicMock(side_effect=requests.exceptions.ChunkedEncodingError("broken"))
        self.check(response, Kind.NETWORK)


class TestFeedRequests(TestCase):
    def test_status_is_public(self):
        client, session = make_client(MockResponse(200, {"newly": {}}))
        self.assertEqual({"newly": {}}, client.get_feed_status())
        self.assertNotIn("X-API-KEY", session.calls[0]["headers"])
        self.assertEqual("https://files.whoisfreaks.com/v3.4/status", session.calls[0]["url"])

    def test_status_must_be_an_object(self):
        client, _ = make_client(MockResponse(200, []))
        with self.assertRaises(WhoisFreaksError):
            client.get_feed_status()

    def test_page_text(self):
        client, session = make_client(MockResponse(200, "﻿a.com\nb.com\n"))
        text = client.get_feed_page("Feed", "/v3.3/stream/domainer/gtld", {"date": "2026-11-01", "limit": 2})
        self.assertEqual("a.com\nb.com\n", text)
        self.assertEqual(API_KEY, session.calls[0]["headers"]["X-API-KEY"])
        self.assertEqual(constants.FEED_TIMEOUT, session.calls[0]["timeout"])

    def test_end_of_data_status(self):
        client, _ = make_client(MockResponse(401, {"status": 401, "message": "Api record not found."}))
        self.assertIsNone(client.get_feed_page("Feed", "/p", {}))

    def test_json_error_inside_http_200(self):
        cases = (
            ({"status": 403, "message": "No subscription"}, Kind.NOT_ENTITLED),
            (
                {"status": 413, "message": "Please upgrade your plans.This Plan does not have the access"},
                Kind.NOT_ENTITLED,
            ),
            ({"message": "Please pass valid apiKey param value"}, Kind.INVALID_CREDENTIALS),
            ({"status": 404, "message": "File is not available of this date."}, Kind.DATE_NOT_AVAILABLE),
            (["unexpected"], Kind.BAD_REQUEST),
        )
        for body, kind in cases:
            with self.subTest(body=body):
                client, _ = make_client(MockResponse(200, body))
                with self.assertRaises(WhoisFreaksError) as context:
                    client.get_feed_page("Feed", "/p", {})
                self.assertEqual(kind, context.exception.kind)

    def test_json_end_of_data_inside_http_200(self):
        client, _ = make_client(MockResponse(200, {"status": 401, "message": "Api record not found."}))
        self.assertIsNone(client.get_feed_page("Feed", "/p", {}))

    def test_malformed_json_error(self):
        client, _ = make_client(MockResponse(200, "{not json"))
        with self.assertRaises(WhoisFreaksError) as context:
            client.get_feed_page("Feed", "/p", {})
        self.assertEqual(Kind.INVALID_RESPONSE, context.exception.kind)

    def test_feed_retry_policy(self):
        client, session = make_client(MockResponse(503))
        with self.assertRaises(WhoisFreaksError):
            client.get_feed_page("Feed", "/p", {})
        self.assertEqual(FEED_RETRY.max_attempts, len(session.calls))

    def test_real_session_is_created_per_thread(self):
        client = WhoisFreaksClient(API_KEY, logging.getLogger("client"))
        self.assertIs(client._session(), client._session())
