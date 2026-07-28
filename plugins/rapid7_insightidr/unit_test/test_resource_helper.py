import os
import sys

sys.path.append(os.path.abspath("../"))

import logging
from unittest import TestCase
from unittest.mock import patch

import requests
from insightconnect_plugin_runtime.exceptions import PluginException
from komand_rapid7_insightidr.util.constants import RETRY_MAX_ATTEMPTS
from komand_rapid7_insightidr.util.resource_helper import ResourceHelper


def _make_response(status_code: int, body: str = "{}") -> requests.Response:
    response = requests.Response()
    response.status_code = status_code
    response._content = body.encode("utf-8")
    return response


class TestResourceHelperRetry(TestCase):
    def setUp(self) -> None:
        self.helper = ResourceHelper({}, logging.getLogger("test"))
        self.endpoint = "https://us.api.insight.rapid7.com/idr/v2/investigations/_search"

        self.mock_sleep = patch("time.sleep", return_value=None).start()
        self.mock_send = patch("requests.Session.send").start()
        self.addCleanup(patch.stopall)

    def test_resource_request_retries_5xx_then_succeeds(self) -> None:
        self.mock_send.side_effect = [_make_response(500), _make_response(200, '{"data": "ok"}')]

        result = self.helper.resource_request(self.endpoint, method="post")

        self.assertEqual(result["status"], 200)
        self.assertEqual(self.mock_send.call_count, 2)
        self.mock_sleep.assert_called_once()

    def test_resource_request_persistent_5xx_raises_after_max_attempts(self) -> None:
        self.mock_send.return_value = _make_response(500, '{"message": "boom"}')

        with self.assertRaises(PluginException):
            self.helper.resource_request(self.endpoint, method="post")

        self.assertEqual(self.mock_send.call_count, RETRY_MAX_ATTEMPTS)
        self.assertEqual(self.mock_sleep.call_count, RETRY_MAX_ATTEMPTS - 1)

    def test_resource_request_4xx_not_retried(self) -> None:
        self.mock_send.return_value = _make_response(404, '{"message": "nope"}')

        with self.assertRaises(PluginException):
            self.helper.resource_request(self.endpoint, method="get")

        self.assertEqual(self.mock_send.call_count, 1)
        self.mock_sleep.assert_not_called()

    def test_make_request_retries_5xx_then_succeeds(self) -> None:
        self.mock_send.side_effect = [_make_response(503), _make_response(200, '{"data": "ok"}')]

        result = self.helper.make_request(self.endpoint, method="POST")

        self.assertEqual(result, {"data": "ok"})
        self.assertEqual(self.mock_send.call_count, 2)
        self.mock_sleep.assert_called_once()

    def test_make_request_persistent_5xx_raises_after_max_attempts(self) -> None:
        self.mock_send.return_value = _make_response(502, "gateway error")

        with self.assertRaises(PluginException):
            self.helper.make_request(self.endpoint, method="POST")

        self.assertEqual(self.mock_send.call_count, RETRY_MAX_ATTEMPTS)
        self.assertEqual(self.mock_sleep.call_count, RETRY_MAX_ATTEMPTS - 1)

    def test_make_request_4xx_not_retried(self) -> None:
        self.mock_send.return_value = _make_response(400, "bad request")

        with self.assertRaises(PluginException):
            self.helper.make_request(self.endpoint, method="POST")

        self.assertEqual(self.mock_send.call_count, 1)
        self.mock_sleep.assert_not_called()

    def test_non_idempotent_post_5xx_not_retried(self) -> None:
        # A create POST (not a search) must not be retried on 5xx to avoid duplicate writes.
        create_endpoint = "https://us.api.insight.rapid7.com/idr/v2/investigations"
        self.mock_send.return_value = _make_response(500, '{"message": "boom"}')

        with self.assertRaises(PluginException):
            self.helper.make_request(create_endpoint, method="POST")

        self.assertEqual(self.mock_send.call_count, 1)
        self.mock_sleep.assert_not_called()
