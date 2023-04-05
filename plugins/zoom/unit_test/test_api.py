import logging
import unittest
from unittest import TestCase
from unittest.mock import patch

from icon_zoom.util.api import ZoomAPI, BearerAuth


REFRESH_OAUTH_TOKEN_PATH = "icon_zoom.util.api.ZoomAPI._refresh_oauth_token"
REQUESTS_PATH = "requests.request"


class MockResponse:
    def __init__(self, status_code: int):
        self.status_code = status_code

    def json(self) -> dict:
        return {}


class MyTestCase(TestCase):
    @patch(REFRESH_OAUTH_TOKEN_PATH)
    @patch(REQUESTS_PATH)
    def test_unauthenticated_first_run(self, mock_request, mock_refresh):
        mock_refresh.return_value = "blah"
        api = ZoomAPI(account_id="blah", client_id="blah", client_secret="blah", logger=logging.getLogger())

        mock_request.side_effect = [MockResponse(status_code=401), MockResponse(status_code=200)]
        result = api._call_api(method="POST", url="http://example.com")
        self.assertDictEqual(result, {})

    @patch(REFRESH_OAUTH_TOKEN_PATH)
    @patch(REQUESTS_PATH)
    def test_authenticated_first_run(self, mock_request, mock_refresh):
        mock_refresh.return_value = "blah"
        api = ZoomAPI(account_id="blah", client_id="blah", client_secret="blah", logger=logging.getLogger())

        mock_request.side_effect = [MockResponse(status_code=200)]
        result = api._call_api(method="POST", url="http://example.com")
        self.assertDictEqual(result, {})


if __name__ == "__main__":
    unittest.main()
