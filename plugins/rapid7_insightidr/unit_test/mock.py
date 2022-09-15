import json
import os

from util import Util

REQUEST_GET = "get"
REQUEST_POST = "post"
REQUEST_PATCH = "patch"
REQUEST_PUT = "put"

STUB_INVESTIGATION_IDENTIFIER = "rrn:investigation:example:11111111-1111-1111-1111-111111111111:investigation:11111111"
STUB_QUERY_ID = "00000000-0000-1eec-0000-000000000000"
STUB_QUERY_ID_NOT_FOUND = "00000000-0000-8eec-0000-000000000000"
STUB_API_KEY = "j5740ps1cbukyk3t8kib3wa36aq2v3da"
STUB_CONNECTION = {"api_key": {"secretKey": STUB_API_KEY}, "url": STUB_API_KEY}

STUB_PRIORITY = "LOW"
STUB_DISPOSITION = "BENING"
STUB_STATUS = "OPEN"

STUB_USER_EMAIL = "user@example.com"

# Define and return mock API responses based on request type and endpoint
def mock_get_request(*args, **_kwarg):
    return mock_request_selection(_kwarg.get("url"), method=REQUEST_GET)


def mock_post_request(*args, **_kwarg):
    return mock_request_selection(_kwarg.get("url"), method=REQUEST_POST)


def mock_patch_request(*args, **_kwarg):
    return mock_request_selection(_kwarg.get("url"), method=REQUEST_PATCH)


def mock_put_request(*args, **_kwarg):
    return mock_request_selection(_kwarg.get("url"), method=REQUEST_PUT)


class MockResponse:
    def __init__(self, filename: str, status_code: int) -> None:
        self.status_code = status_code
        if filename:
            self.text = Util.read_file_to_string(
                os.path.join(os.path.dirname(os.path.realpath(__file__)), f"payloads/{filename}.json.resp")
            )
        else:
            self.text = ""

    def json(self):
        return json.loads(self.text)


def mock_request_post(url: str) -> MockResponse:
    if url == f"{Util.STUB_URL_API}/query/saved_queries/{STUB_QUERY_ID}":
        return MockResponse("get_a_saved_query", 200)
    if url == f"{Util.STUB_URL_API}/idr/v2/investigations":
        return MockResponse("create_investigation", 201)
    if url == f"{Util.STUB_URL_API}/idr/v2/investigations/_search":
        return MockResponse("search_investigations", 200)


def mock_request_get(url: str) -> MockResponse:
    if url == f"{Util.STUB_URL_REST}/query/saved_queries":
        return MockResponse("get_all_saved_queries", 200)
    if url == f"{Util.STUB_URL_API}/query/saved_queries/{STUB_QUERY_ID}":
        return MockResponse("get_a_saved_query", 200)
    if url == f"{Util.STUB_URL_API}/query/saved_queries/{STUB_QUERY_ID_NOT_FOUND}":
        return MockResponse("get_a_saved_query_404", 404)
    if url == f"{Util.STUB_URL_API}/idr/v2/investigations/{STUB_INVESTIGATION_IDENTIFIER}":
        return MockResponse("get_investigation", 200)
    if url == f"{Util.STUB_URL_API}/idr/v2/investigations/{STUB_INVESTIGATION_IDENTIFIER}/alerts":
        return MockResponse("list_alerts_for_investigation", 200)
    if "investigations" in url:
        return MockResponse("list_investigations", 200)


def mock_request_patch(url: str) -> MockResponse:
    if url == f"{Util.STUB_URL_API}/idr/v2/investigations/{STUB_INVESTIGATION_IDENTIFIER}":
        return MockResponse("update_investigation", 200)


def mock_request_put(url: str) -> MockResponse:
    if url == f"{Util.STUB_URL_API}/idr/v2/investigations/{STUB_INVESTIGATION_IDENTIFIER}/priority/{STUB_PRIORITY}":
        return MockResponse("update_investigation", 200)
    if url == f"{Util.STUB_URL_API}/idr/v2/investigations/{STUB_INVESTIGATION_IDENTIFIER}/status/{STUB_STATUS}":
        return MockResponse("update_investigation", 200)
    if (
        url
        == f"{Util.STUB_URL_API}/idr/v2/investigations/{STUB_INVESTIGATION_IDENTIFIER}/disposition/{STUB_DISPOSITION}"
    ):
        return MockResponse("update_investigation", 200)
    if url == f"{Util.STUB_URL_API}/idr/v2/investigations/{STUB_INVESTIGATION_IDENTIFIER}/assignee":
        return MockResponse("update_investigation", 200)


def mock_request_selection(url, method="get"):
    # Check reqeust type and endpoint. Return appropriate file name to be loaded and response code
    if method == REQUEST_POST:
        return mock_request_post(url)
    elif method == REQUEST_GET:
        return mock_request_get(url)
    elif method == REQUEST_PATCH:
        return mock_request_patch(url)
    elif method == REQUEST_PUT:
        return mock_request_put(url)
    raise Exception("Response has been not implemented")
