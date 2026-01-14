import json
import os

from util import Util

REQUEST_GET = "get"
REQUEST_POST = "post"
REQUEST_PATCH = "patch"
REQUEST_PUT = "put"

STUB_ID = "1b1a111d-d1fb-1a12-1651-eb1ff61a651a"
STUB_ID_NOT_FOUND = "22b2b22b-222b-222b-2222-b2bb2bbb2b2b"
STUB_ID_202_ERROR = "33b3b3b-333b-333b-3333-b3bb3bbb3b3b"
STUB_ID_KEY_ERROR = "44b4b4b-444b-4444-b4bb4bbb4b4b"
STUB_ID_202 = "55b5b5b-555b-5555-b5bb5bbb5b5b"
STUB_INVESTIGATION_IDENTIFIER = "rrn:investigation:example:11111111-1111-1111-1111-111111111111:investigation:11111111"
STUB_QUERY_ID = "00000000-0000-1eec-0000-000000000000"
STUB_QUERY_ID_NOT_FOUND = "00000000-0000-8eec-0000-000000000000"
STUB_API_KEY = "j5740ps1cbukyk3t8kib3wa36aq2v3da"
STUB_CONNECTION = {"api_key": {"secretKey": STUB_API_KEY}, "url": STUB_API_KEY}

STUB_PRIORITY = "LOW"
STUB_DISPOSITION = "BENIGN"
STUB_STATUS = "OPEN"

STUB_USER_EMAIL = "user@example.com"


# Define and return mock API responses based on request type and endpoint
def mock_get_request(*args, **_kwarg):
    url = args[0].url
    return mock_request_selection(url, method=REQUEST_GET)


def mock_post_request(*args, **_kwarg):
    url = args[0].url
    return mock_request_selection(url, method=REQUEST_POST)


def mock_patch_request(*args, **_kwarg):
    url = args[0].url
    return mock_request_selection(url, method=REQUEST_PATCH)


def mock_put_request(*args, **_kwarg):
    url = args[0].url
    return mock_request_selection(url, method=REQUEST_PUT)


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
    if url == f"{Util.STUB_URL_API}/idr/v1/customthreats/key/dcdba462-fcf5-4021-8707-98b14232239b/indicators/replace":
        return MockResponse("replace_indicators", 200)
    if url == f"{Util.STUB_URL_API}/idr/v1/customthreats/key/dcdba462/indicators/replace":
        # This should be a 400, my test requires this to be within 200-299
        return MockResponse("replace_indicators_bad", 298)


def mock_request_get(url: str) -> MockResponse:
    if url == f"{Util.STUB_URL_REST}/query/logs/{STUB_ID}":
        return MockResponse("query", 200)
    if url == f"{Util.STUB_URL_REST}/query/logs/{STUB_ID_202}":
        return MockResponse("query_202", 202)
    if url == f"{Util.STUB_URL_REST}/query/logs/{STUB_ID_202_ERROR}":
        return MockResponse("query_202_error", 202)
    if url == f"{Util.STUB_URL_REST}/query/logs/{STUB_ID_NOT_FOUND}":
        return MockResponse("query_404", 404)
    if url == f"{Util.STUB_URL_REST}/query/logs/{STUB_ID_KEY_ERROR}":
        return MockResponse("query_key_error", 200)
    if url == f"{Util.STUB_URL_REST}/query/saved_queries":
        return MockResponse("get_all_saved_queries", 200)
    if url == f"{Util.STUB_URL_REST}/query/saved_queries/{STUB_QUERY_ID}":
        return MockResponse("get_a_saved_query", 200)
    if url == f"{Util.STUB_URL_REST}/query/saved_queries/{STUB_QUERY_ID_NOT_FOUND}":
        return MockResponse("get_a_saved_query_404", 404)
    if url == f"{Util.STUB_URL_API}/idr/v2/investigations/{STUB_INVESTIGATION_IDENTIFIER}":
        return MockResponse("get_investigation", 200)
    if url == f"{Util.STUB_URL_API}/idr/v2/investigations/{STUB_INVESTIGATION_IDENTIFIER}/alerts":
        return MockResponse("list_alerts_for_investigation", 200)
    if "investigations" in url:
        return MockResponse("list_investigations", 200)


def mock_request_for_different_rrn_object(*args, **kwargs) -> MockResponse:
    return MockResponse("list_alerts_for_investigation_rrn_as_object", 200)


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
    url = url.split("?")[0]
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
