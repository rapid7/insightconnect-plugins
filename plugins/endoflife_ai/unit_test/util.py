import json
import logging
import os
import sys

sys.path.append(os.path.abspath("../"))

from icon_endoflife_ai.connection.connection import Connection
from icon_endoflife_ai.connection.schema import Input

BASE_URL = "https://api.endoflife.ai"

STUB_CONNECTION_ANONYMOUS = {Input.URL: BASE_URL}
STUB_CONNECTION_WITH_KEY = {Input.URL: BASE_URL, Input.API_KEY: {"secretKey": "test-key"}}


def read_file_to_string(filename):
    with open(filename) as my_file:
        return my_file.read()


def payload(name):
    # Since this is folder down from the base unit_test folder, the base path may change on us if we're
    # running the whole suite, or just these tests.
    actual_path = os.path.dirname(os.path.realpath(__file__))
    return read_file_to_string(os.path.join(actual_path, f"payloads/{name}.json"))


class MockResponse:
    def __init__(self, json_data, status_code):
        self.json_data = json_data
        self.status_code = status_code
        self.text = json_data if isinstance(json_data, str) else "This is some error text"

    def json(self):
        if self.json_data is None:
            raise json.decoder.JSONDecodeError("no body", "", 0)
        return json.loads(self.json_data) if isinstance(self.json_data, str) else self.json_data


# This method will be used by the mock to replace requests.request
def mocked_requests_request(method, url, **kwargs):
    if method == "GET" and url == f"{BASE_URL}/v1/score/nodejs/20":
        return MockResponse(payload("get_version_status_data"), 200)
    if method == "GET" and url == f"{BASE_URL}/v1/score/nodejs/99":
        return MockResponse(payload("get_version_status_not_found"), 404)
    if method == "GET" and url == f"{BASE_URL}/v1/score/nodejs/8.0":
        return MockResponse(payload("get_version_status_data"), 200)
    if method == "GET" and url == f"{BASE_URL}/v1/product/nodejs":
        return MockResponse(payload("get_product_data"), 200)
    if method == "GET" and url == f"{BASE_URL}/v1/product/not-a-product":
        return MockResponse(payload("get_product_not_found"), 404)
    if method == "GET" and url == f"{BASE_URL}/v1/score/nodejs/limited":
        return MockResponse('{"error": "Rate limit exceeded."}', 429)
    if method == "GET" and url == f"{BASE_URL}/v1/score/nodejs/broken":
        return MockResponse("<html>outage</html>", 502)
    if method == "POST" and url == f"{BASE_URL}/v1/batch":
        products = (kwargs.get("json") or {}).get("products") or []
        full = json.loads(payload("check_batch_data"))
        by_key = {}
        for result in full["results"]:
            key = (result.get("product") or result.get("slug"), result.get("version"))
            by_key[key] = result
            by_key[(key[0], None)] = by_key.get((key[0], None), result)
        results = []
        for item in products:
            key = (item.get("slug"), item.get("version"))
            results.append(
                by_key.get(key)
                or by_key.get((item.get("slug"), None))
                or {"slug": item.get("slug"), "error": "Product not found"}
            )
        return MockResponse({"count": len(results), "results": results, "tier": "anon", "docs": full["docs"]}, 200)

    print(f"mocked_requests_request failed looking for: {method} {url}")
    return MockResponse(None, 404)


# This method will be used by the mock to replace requests.get in the connection test
def mocked_requests_get(url, **kwargs):
    if url == f"{BASE_URL}/v1":
        return MockResponse(payload("connection_test_data"), 200)
    if url == "https://example.invalid/v1":
        return MockResponse('{"hello": "world"}', 200)
    print(f"mocked_requests_get failed looking for: {url}")
    return MockResponse(None, 404)


def connection(params=STUB_CONNECTION_ANONYMOUS):
    test_connection = Connection()
    test_connection.logger = logging.getLogger("connection logger")
    test_connection.connect(params)
    return test_connection


def default_connector(action, params=STUB_CONNECTION_ANONYMOUS):
    action.connection = connection(params)
    action.logger = logging.getLogger("action logger")
    return action
