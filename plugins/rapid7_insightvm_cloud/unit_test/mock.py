import json
import os
import logging
from unit_test.utils import Utils

STUB_ASSET_ID = "5058b0b4-701a-414e-9630-430d2cddbf4d"
STUB_SEARCH_ID = "86a8abc0-95f3-4353-adf5-abb631c1f824"
STUB_REGION = "us"
SUB_BAD_REGION = "us_invalid"
REQUEST_GET = "GET"
REQUEST_POST = "POST"


# Define and return mock API responses based on request type and endpoint
def mock_request(*args, **_kwarg):
    return mock_request_selection(args[0], args[1])


class MockResponse:
    def __init__(self, filename: str, status_code: int) -> None:
        self.status_code = status_code
        if filename:
            self.text = Utils.read_file_to_string(
                os.path.join(os.path.dirname(os.path.realpath(__file__)), f"payloads/{filename}.json.resp")
            )
        else:
            self.text = ""

    def json(self):
        return json.loads(self.text)


def mock_request_post(url):
    if url == f"https://{STUB_REGION}.api.insight.rapid7.com/vm/v4/integration/assets/{STUB_ASSET_ID}":
        return MockResponse("get_asset", 200)
    raise Exception("Response has been not implemented")


def mock_request_get(url):
    if url == f"https://{STUB_REGION}.api.insight.rapid7.com/vm/v4/integration/assets/{STUB_ASSET_ID}":
        return MockResponse("get_asset", 200)
    raise Exception("Response has been not implemented")


def mock_request_selection(method, url):
    # Check reqeust type and endpoint. Return appropriate file name to be loaded and response code
    if method == REQUEST_POST:
        return mock_request_post(url)
    elif method == REQUEST_GET:
        return mock_request_get(url)
    raise Exception("Response has been not implemented")
