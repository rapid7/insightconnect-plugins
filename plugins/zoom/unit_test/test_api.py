import sys

sys.path.append("../")

import logging
import unittest
from unittest import TestCase
from unittest.mock import MagicMock, patch

from icon_zoom.util.api import AuthenticationRetryLimitError, ZoomAPI

REFRESH_OAUTH_TOKEN_PATH = "icon_zoom.util.api.ZoomAPI._refresh_oauth_token"
REQUESTS_PATH = "requests.request"


class MockResponse:
    def __init__(self, status_code: int, headers: dict = {}):
        self.status_code = status_code
        self.headers = headers

    def json(self) -> dict:
        return {}


class TestAPI(TestCase):
    @patch(REFRESH_OAUTH_TOKEN_PATH)
    @patch(REQUESTS_PATH)
    def test_unauthenticated_first_run_oauth(self, mock_request: MagicMock, mock_refresh: MagicMock) -> None:
        mock_refresh.return_value = "blah"
        api = ZoomAPI(account_id="blah", client_id="blah", client_secret="blah", logger=logging.getLogger())

        mock_request.side_effect = [MockResponse(status_code=401), MockResponse(status_code=200)]
        result = api._call_api(method="POST", url="http://example.com")
        self.assertDictEqual(result, {})

    @patch(REFRESH_OAUTH_TOKEN_PATH)
    @patch(REQUESTS_PATH)
    def test_unauthenticated_first_run_oauth_retry_limit_met_1_attempt(
        self, mock_request: MagicMock, mock_refresh: MagicMock
    ) -> None:
        mock_refresh.return_value = "blah"
        api = ZoomAPI(
            account_id="blah", client_id="blah", client_secret="blah", oauth_retry_limit=1, logger=logging.getLogger()
        )

        mock_request.side_effect = [MockResponse(status_code=401), MockResponse(status_code=200)]

        with self.assertRaises(AuthenticationRetryLimitError):
            api._call_api(method="POST", url="http://example.com")

    @patch(REFRESH_OAUTH_TOKEN_PATH)
    @patch(REQUESTS_PATH)
    def test_unauthenticated_first_run_oauth_retry_limit_met_50_attempts(
        self, mock_request: MagicMock, mock_refresh: MagicMock
    ) -> None:
        num_retries = 50
        mock_refresh.return_value = "blah"
        api = ZoomAPI(
            account_id="blah",
            client_id="blah",
            client_secret="blah",
            oauth_retry_limit=num_retries,
            logger=logging.getLogger(),
        )

        mock_request.side_effect = [MockResponse(status_code=401) for _ in range(0, num_retries)]

        with self.assertRaises(AuthenticationRetryLimitError):
            api._call_api(method="POST", url="http://example.com")

    @patch(REFRESH_OAUTH_TOKEN_PATH)
    @patch(REQUESTS_PATH)
    def test_authenticated_first_run_oauth(self, mock_request: MagicMock, mock_refresh: MagicMock) -> None:
        mock_refresh.return_value = "blah"
        api = ZoomAPI(account_id="blah", client_id="blah", client_secret="blah", logger=logging.getLogger())
        mock_request.side_effect = [MockResponse(status_code=200)]
        result = api._call_api(method="POST", url="http://example.com")
        self.assertDictEqual(result, {})
