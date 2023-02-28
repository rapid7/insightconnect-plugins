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

STUB_IDENTIFIER = "identifier"
STUB_IDENTIFIER_NOT_UNIQUE = "identifier_not_unique"
STUB_IDENTIFIER_NONE = "no_identifier"


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
    if url == f"/api/odata/businessobject/incidents('{STUB_REC_ID_GOOD}')" and method == "DELETE":
        return MockResponse("delete_incident_good", 200)
    if url == f"/api/odata/businessobject/incidents('{STUB_REC_ID_ODD}')" and method == "DELETE":
        return MockResponse("delete_incident_odd", 200)

    if url == f"/api/odata/businessobject/incidents?$filter=IncidentNumber eq {STUB_INCIDENT_NUMBER_ODD}":
        return MockResponse("get_incident_odd", 200)
    if url == f"/api/odata/businessobject/incidents?$filter=IncidentNumber eq {STUB_INCIDENT_NUMBER_GOOD}":
        return MockResponse("get_incident_good", 200)
    if url == f"/api/odata/businessobject/incidents?$filter=IncidentNumber eq {STUB_INCIDENT_NUMBER_BAD}":
        return MockResponse("get_incident_bad", 400)

    if url == f"/api/odata/businessobject/employees?$search={STUB_IDENTIFIER}" and method == "GET":
        return MockResponse("search_employees_good", 200)
    if url == f"/api/odata/businessobject/employees?$search={STUB_IDENTIFIER_NOT_UNIQUE}" and method == "GET":
        return MockResponse("search_employees_not_unique", 200)
    if url == f"/api/odata/businessobject/employees?$search={STUB_IDENTIFIER_NONE}" and method == "GET":
        return MockResponse("search_employees_none", 200)

    if url == f"/api/odata/businessobject/servicereqtemplates?$search={STUB_IDENTIFIER}" and method == "GET":
        return MockResponse("search_employees_good", 200)
    if url == f"/api/odata/businessobject/servicereqtemplates?$search={STUB_IDENTIFIER_NOT_UNIQUE}" and method == "GET":
        return MockResponse("search_employees_not_unique", 200)
    if url == f"/api/odata/businessobject/servicereqtemplates?$search={STUB_IDENTIFIER_NONE}" and method == "GET":
        return MockResponse("search_employees_none", 200)

    if url == f"/api/odata/businessobject/incidents('{STUB_REC_ID_GOOD}')" and method == "PUT":
        return MockResponse("update_incident_good", 200)

    if url == "/api/odata/businessobject/journal__Notess" and method == "POST":
        return MockResponse("add_note_good", 200)

    if url == "/api/odata/businessobject/incidents" and method == "POST":
        return MockResponse("create_incident_good", 200)

    if url == "/api/odata/businessobject/servicereqs" and method == "POST":
        return MockResponse("create_service_request_good", 200)


