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


def mock_request(url: str) -> MockResponse:
    if url == f"odata/businessobject/incidents?$filter=IncidentNumber eq {STUB_INCIDENT_NUMBER_GOOD}":
        return MockResponse("delete_incident_good", 200)
    if url == f"odata/businessobject/incidents?$filter=IncidentNumber eq {STUB_INCIDENT_NUMBER_GOOD}":
        return MockResponse("delete_incident_bad", 400)
