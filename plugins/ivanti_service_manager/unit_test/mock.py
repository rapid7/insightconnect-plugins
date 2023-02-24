import json
import os

from util import Util

REQUEST_GET = "get"
REQUEST_POST = "post"
REQUEST_PATCH = "patch"
REQUEST_PUT = "put"
REQUEST_DELETE = "delete"

STUB_INCIDENT_NUMBER_GOOD = 12345
STUB_INCIDENT_NUMBER_BAD = 54321
STUB_INCIDENT_NUMBER_ODD = 15243

STUB_REC_ID_GOOD = "085867F47547496783005D95CB82D557"
STUB_REC_ID_ODD = "00000000000000000000000000000000"


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


def mock_request(method, url, json, params, headers, verify) -> MockResponse:
    if str(STUB_REC_ID_GOOD) in url:
        return MockResponse("delete_incident_good", 200)
    if str(STUB_INCIDENT_NUMBER_BAD) in url:
        return MockResponse("delete_incident_bad", 400)
    if str(STUB_REC_ID_ODD) in url:
        return MockResponse("delete_incident_odd", 200)
    if str(STUB_INCIDENT_NUMBER_ODD) in url:
        return MockResponse("get_incident_odd", 200)
    if str(STUB_INCIDENT_NUMBER_GOOD) in url:
        return MockResponse("get_incident_good", 200)
