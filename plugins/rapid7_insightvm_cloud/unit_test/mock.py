import json
import os

STUB_ASSET_ID = "5058b0b4-701a-414e-9630-430d2cddbf4d"
STUB_BAD_ASSET_ID = "5058b0b4-701a-414e-9630-430d2cddbf4e"
STUB_SEARCH_ID = "86a8abc0-95f3-4353-adf5-abb631c1f824"
STUB_BAD_ASSET_CRITERIA = "invalid asset criteria"
STUB_BAD_VULN_CRITERIA = "invalid vuln criteria"
STUB_SCAN_ID = "5058b0b4-701a-414e-9630-430d2cddbf4d"
STUB_BAD_SCAN_ID = "invalid scan id"
STUB_BAD_SECRET_KEY = "secret_key_invalid"
STUB_SECRET_KEY_SERVER_ERROR = "secret_key_server_error"
STUB_SCAN_NAME = "TestScan"
STUB_SCAN_NAME_NO_ASSET_IDS = "TestScanNoAssetIDs"
STUB_SCAN_NAME_INVALID_ASSET_IDS = "TestScanInvalidAssetIDs"
STUB_REGION = "us"
REQUEST_GET = "GET"
REQUEST_POST = "POST"


# Define and return mock API responses based on request type and endpoint
def mock_request(*args, **_kwarg):
    return mock_request_selection(
        args[0], args[1], _kwarg.get("params"), _kwarg.get("headers"), json.loads(_kwarg.get("data"))
    )


class MockResponse:
    def __init__(self, filename: str, status_code: int) -> None:
        self.filename = filename
        self.status_code = status_code
        if filename:
            with open(
                os.path.join(os.path.dirname(os.path.realpath(__file__)), f"payloads/{filename}.json.resp")
            ) as file:
                self.text = file.read()
        else:
            self.text = ""

    def json(self):
        return json.loads(self.text)


def mock_request_post(url, params, headers, data):
    if headers.get("x-api-key") == STUB_BAD_SECRET_KEY:
        return MockResponse("unauthorized", 401)
    if headers.get("x-api-key") == STUB_SECRET_KEY_SERVER_ERROR:
        return MockResponse("server_error", 500)
    if url == f"https://{STUB_REGION}.api.insight.rapid7.com/vm/v4/integration/assets":
        if data.get("asset") == STUB_BAD_ASSET_CRITERIA:
            return MockResponse("asset_search_invalid_asset_criteria", 400)
        if data.get("vulnerability") == STUB_BAD_VULN_CRITERIA:
            return MockResponse("asset_search_invalid_vuln_criteria", 400)
        return MockResponse("asset_search", 200)
    if url == f"https://{STUB_REGION}.api.insight.rapid7.com/vm/v4/integration/vulnerabilities":
        if data.get("asset") == STUB_BAD_ASSET_CRITERIA:
            return MockResponse("asset_search_invalid_asset_criteria", 400)
        if data.get("vulnerability") == STUB_BAD_VULN_CRITERIA:
            return MockResponse("asset_search_invalid_vuln_criteria", 400)
        return MockResponse("vuln_search", 200)
    if url == f"https://{STUB_REGION}.api.insight.rapid7.com/vm/v4/integration/scan/{STUB_SCAN_ID}/stop":
        return MockResponse("stop_scan", 202)
    if url == f"https://{STUB_REGION}.api.insight.rapid7.com/vm/v4/integration/scan/{STUB_BAD_SCAN_ID}/stop":
        return MockResponse("stop_scan", 202)
    if url == f"https://{STUB_REGION}.api.insight.rapid7.com/vm/v4/integration/scan":
        if data.get("name") == STUB_SCAN_NAME_NO_ASSET_IDS:
            return MockResponse("start_scan_no_asset_ids", 400)
        if data.get("name") == STUB_SCAN_NAME_INVALID_ASSET_IDS:
            return MockResponse("start_scan_invalid_asset_ids", 400)
        return MockResponse("start_scan", 200)
    raise Exception("Response has been not implemented")


def mock_request_get(url, params, headers, data):
    if headers.get("x-api-key") == STUB_BAD_SECRET_KEY:
        return MockResponse("unauthorized", 401)
    if headers.get("x-api-key") == STUB_SECRET_KEY_SERVER_ERROR:
        return MockResponse("server_error", 500)
    if url == f"https://{STUB_REGION}.api.insight.rapid7.com/vm/v4/integration/assets/{STUB_ASSET_ID}":
        if params.get("includeSame"):
            return MockResponse("get_asset_include_vulns", 200)
        return MockResponse("get_asset", 200)
    if url == f"https://{STUB_REGION}.api.insight.rapid7.com/vm/v4/integration/assets/{STUB_BAD_ASSET_ID}":
        return MockResponse("get_asset_404", 404)
    if url == f"https://{STUB_REGION}.api.insight.rapid7.com/vm/v4/integration/scan/{STUB_SCAN_ID}":
        return MockResponse("get_scan", 200)
    if url == f"https://{STUB_REGION}.api.insight.rapid7.com/vm/v4/integration/scan/{STUB_BAD_SCAN_ID}":
        return MockResponse("get_scan_invalid_scan_id", 200)

    raise Exception("Response has been not implemented")


def mock_request_selection(method, url, params, headers, data):
    # Check reqeust type and endpoint. Return appropriate file name to be loaded and response code
    if method == REQUEST_POST:
        return mock_request_post(url, params, headers, data)
    elif method == REQUEST_GET:
        return mock_request_get(url, params, headers, data)
    raise Exception("Response has been not implemented")
