import os
import sys

sys.path.append(os.path.abspath("../"))

import logging
from unittest import TestCase
from unittest.mock import MagicMock, patch

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

    @patch("time.sleep", return_value=None)
    @patch("requests.Session.send")
    def test_resource_request_retries_5xx_then_succeeds(self, mock_send: MagicMock, mock_sleep: MagicMock) -> None:
        mock_send.side_effect = [_make_response(500), _make_response(200, '{"data": "ok"}')]

        result = self.helper.resource_request(self.endpoint, method="post")

        self.assertEqual(result["status"], 200)
        self.assertEqual(mock_send.call_count, 2)
        mock_sleep.assert_called_once()

    @patch("time.sleep", return_value=None)
    @patch("requests.Session.send")
    def test_resource_request_persistent_5xx_raises_after_max_attempts(
        self, mock_send: MagicMock, mock_sleep: MagicMock
    ) -> None:
        mock_send.return_value = _make_response(500, '{"message": "boom"}')

        with self.assertRaises(PluginException):
            self.helper.resource_request(self.endpoint, method="post")

        self.assertEqual(mock_send.call_count, RETRY_MAX_ATTEMPTS)
        self.assertEqual(mock_sleep.call_count, RETRY_MAX_ATTEMPTS - 1)

    @patch("time.sleep", return_value=None)
    @patch("requests.Session.send")
    def test_resource_request_4xx_not_retried(self, mock_send: MagicMock, mock_sleep: MagicMock) -> None:
        mock_send.return_value = _make_response(404, '{"message": "nope"}')

        with self.assertRaises(PluginException):
            self.helper.resource_request(self.endpoint, method="get")

        self.assertEqual(mock_send.call_count, 1)
        mock_sleep.assert_not_called()

    @patch("time.sleep", return_value=None)
    @patch("requests.Session.send")
    def test_make_request_retries_5xx_then_succeeds(self, mock_send: MagicMock, mock_sleep: MagicMock) -> None:
        mock_send.side_effect = [_make_response(503), _make_response(200, '{"data": "ok"}')]

        result = self.helper.make_request(self.endpoint, method="POST")

        self.assertEqual(result, {"data": "ok"})
        self.assertEqual(mock_send.call_count, 2)
        mock_sleep.assert_called_once()

    @patch("time.sleep", return_value=None)
    @patch("requests.Session.send")
    def test_make_request_persistent_5xx_raises_after_max_attempts(
        self, mock_send: MagicMock, mock_sleep: MagicMock
    ) -> None:
        mock_send.return_value = _make_response(502, "gateway error")

        with self.assertRaises(PluginException):
            self.helper.make_request(self.endpoint, method="POST")

        self.assertEqual(mock_send.call_count, RETRY_MAX_ATTEMPTS)
        self.assertEqual(mock_sleep.call_count, RETRY_MAX_ATTEMPTS - 1)

    @patch("time.sleep", return_value=None)
    @patch("requests.Session.send")
    def test_make_request_4xx_not_retried(self, mock_send: MagicMock, mock_sleep: MagicMock) -> None:
        mock_send.return_value = _make_response(400, "bad request")

        with self.assertRaises(PluginException):
            self.helper.make_request(self.endpoint, method="POST")

        self.assertEqual(mock_send.call_count, 1)
        mock_sleep.assert_not_called()

    @patch("time.sleep", return_value=None)
    @patch("requests.Session.send")
    def test_non_idempotent_post_5xx_not_retried(self, mock_send: MagicMock, mock_sleep: MagicMock) -> None:
        # A create POST (not a search) must not be retried on 5xx to avoid duplicate writes.
        create_endpoint = "https://us.api.insight.rapid7.com/idr/v2/investigations"
        mock_send.return_value = _make_response(500, '{"message": "boom"}')

        with self.assertRaises(PluginException):
            self.helper.make_request(create_endpoint, method="POST")

        self.assertEqual(mock_send.call_count, 1)
        mock_sleep.assert_not_called()
