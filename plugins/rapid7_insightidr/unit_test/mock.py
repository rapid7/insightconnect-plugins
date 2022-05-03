import json
import os
from unit_test.util import Util


REQUEST_GET = "get"
REQUEST_POST = "post"
STUB_QUERY_ID = "00000000-0000-9eec-0000-000000000000"
STUB_QUERY_ID_NOT_FOUND = "00000000-0000-8eec-0000-000000000000"
STUB_URL = "http://url"
STUB_API_KEY = "j5740ps1cbukyk3t8kib3wa36aq2v3da"
STUB_CONNECTION = {"api_key": {"secretKey": STUB_API_KEY}, "url": STUB_API_KEY}

# Define and return mock API responses based on request type and endpoint
def mock_request(*args, **_kwarg):
    return mock_request_selection(args[0], _kwarg.get("url"))


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


def mock_request_post(url):
    if url == f"{STUB_URL}/query/saved_queries/{STUB_QUERY_ID}":
        return MockResponse("get_a_saved_query", 200)


def mock_request_get(url):
    if url == f"{STUB_URL}/query/saved_queries/{STUB_QUERY_ID}":
        return MockResponse("get_a_saved_query", 200)
    if url == f"{STUB_URL}/query/saved_queries/{STUB_QUERY_ID_NOT_FOUND}":
        return MockResponse("get_a_saved_query_404", 404)


def mock_request_selection(method, url):
    # Check reqeust type and endpoint. Return appropriate file name to be loaded and response code
    if method == REQUEST_POST:
        return mock_request_post(url)
    elif method == REQUEST_GET:
        return mock_request_get(url)
    raise Exception("Response has been not implemented")
