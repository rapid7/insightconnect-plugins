import json
import logging
import os
import sys
from email.utils import formatdate

import insightconnect_plugin_runtime

from icon_rapid7_cyber_grc.connection import Connection
from icon_rapid7_cyber_grc.connection.schema import Input

sys.path.append(os.path.abspath("../"))

BASE_URL = "https://app-example-std-use2-api-01.azurewebsites.net"
API_KEY = "cpyl_0000000000000000000000000000000000000000000000"
ODATA_CONTEXT = f"{BASE_URL}/api/v2/$metadata#Risks"

# Two pages so the @odata.nextLink branch is exercised; every other collection is
# returned in a single response, which is how the live API behaves today.
PAGED_ENTITY = "Tasks"

# The assignee of each paged task, which is the field the Get Tasks owner match reads.
TASK_ASSIGNEES = {1: ("Alice@Example.com", 11), 2: ("bob@example.com", 22)}


class Meta:
    version = "0.0.0"


class MockResponse:
    def __init__(self, status_code: int, body=None, text: str = None, headers: dict = None):
        self.status_code = status_code
        self.ok = 200 <= status_code < 400
        if text is not None:
            self.text = text
        elif body is not None:
            self.text = json.dumps(body)
        else:
            self.text = ""
        self.content = self.text.encode("utf-8")
        # The client inspects Content-Type to tell an API response from a web page, and
        # Retry-After to tell the user how long to wait after a rate limit.
        self.headers = headers or {"Content-Type": "application/json" if body is not None else "text/plain"}

    def json(self):
        return json.loads(self.text)


def metrics_record(control_set_id: int, compliance: float, linked: float, automated: float, calculated: str) -> dict:
    """A ControlSetMetrics row as the API returns it."""
    return {
        "id": control_set_id * 100,
        "controlSetID": control_set_id,
        "compliance": compliance,
        "linkedControlsPercentage": linked,
        "automatedControlsPercentage": automated,
        "dateCalculated": calculated,
    }


def record(record_id: int, name: str = "Example") -> dict:
    """A record as the API returns it, including the annotation the client must strip."""
    return {
        "@odata.context": ODATA_CONTEXT,
        "id": record_id,
        "name": name,
        "modifiedDate": "2026-01-21T20:30:44.407Z",
        "createdDate": "2026-01-20T09:00:00.000Z",
    }


def created_record(record_id: int, name: str = "Example") -> dict:
    """A record nothing has edited yet, as the API returns it.

    The API does not stamp modifiedDate at creation, it leaves it null until something
    edits the record, so this is the shape every newly created record arrives in.
    """
    return {**record(record_id, name), "modifiedDate": None}


def collection(records: list, next_link: str = None) -> dict:
    body = {"@odata.context": ODATA_CONTEXT, "value": records}
    if next_link:
        body["@odata.nextLink"] = next_link
    return body


def task(record_id: int) -> dict:
    """A task carrying the nested assignee the Get Tasks owner match reads."""
    body = record(record_id)
    email, users_id = TASK_ASSIGNEES[record_id]
    body["assignedTo"] = {"userEmail": email, "usersID": users_id}
    return body


# Control sets as Get Compliance Score reads them: two live frameworks, one retired, and
# one live framework that has never been scored.
CONTROL_SETS = [
    {"id": 1, "name": "SOC 2", "enabled": True, "isArchived": False},
    {"id": 2, "name": "ISO 27001", "enabled": True, "isArchived": False},
    {"id": 3, "name": "PCI DSS", "enabled": False, "isArchived": True},
    {"id": 4, "name": "HIPAA", "enabled": True, "isArchived": False},
]

# Deliberately not in date order, and control set 1 has an older calculation that must
# lose to its newer one.
CONTROL_SET_METRICS = [
    metrics_record(2, 60.0, 70.0, 20.0, "2026-08-01T00:00:00.000Z"),
    metrics_record(1, 80.0, 50.0, 40.0, "2026-09-01T00:00:00.000Z"),
    metrics_record(1, 10.0, 5.0, 1.0, "2026-01-01T00:00:00.000Z"),
    metrics_record(3, 5.0, 5.0, 5.0, "2026-08-15T00:00:00.000Z"),
]


class Util:
    # Requests the mock server received, so tests can assert on URLs and query options.
    calls = []
    # Names written by PUT, so a read-back after a 204 reflects the update.
    updated = {}

    @staticmethod
    def default_connector(component):
        connection = Connection()
        connection.logger = logging.getLogger("connection logger")
        connection.meta = Meta()
        connection.connect(
            {
                Input.URL: BASE_URL,
                Input.API_KEY: {"secretKey": API_KEY},
                Input.SSL_VERIFY: True,
            }
        )
        component.connection = connection
        component.logger = logging.getLogger("component logger")
        return component

    @staticmethod
    def mock_request(method: str, url: str, **kwargs) -> MockResponse:
        Util.calls.append({"method": method, "url": url, **kwargs})
        path = url.replace(BASE_URL, "")
        params = kwargs.get("params") or {}

        if path == "/api/flatfile-integrations":
            body = kwargs.get("json") or {}
            if not body.get("FileName"):
                return MockResponse(400, {"error": "FileName is required"})
            return MockResponse(200, {"success": True, "fileName": body["FileName"]})

        if not path.startswith("/api/v2/"):
            return MockResponse(404, {"error": "not found"})

        segments = path[len("/api/v2/") :].split("/")
        entity = segments[0]

        if entity == "Missing":
            return MockResponse(404, {"error": "not found"})
        if entity == "Broken":
            return MockResponse(500, {"error": "server error"})
        if entity == "Garbled":
            # How the web interface answers an API path: its sign-in page, with a 200.
            return MockResponse(200, text="<!DOCTYPE html><html><head><title>Rapid7</title></head></html>")
        if entity == "Truncated":
            return MockResponse(200, text='{"value": [')

        if len(segments) == 2 and segments[1] == "$count":
            if params.get("$filter") == "invalid":
                return MockResponse(400, {"error": {"message": "invalid filter"}})
            if entity == "Uncountable":
                return MockResponse(200, text="not-a-number")
            # Every real response carries a Date, which is where the trigger reads the
            # server's clock from before its first poll.
            return MockResponse(200, text="7", headers={"Content-Type": "text/plain", "Date": formatdate(usegmt=True)})

        if len(segments) == 3 and segments[2] == "History":
            return MockResponse(200, collection([record(int(segments[1]), "Older"), record(int(segments[1]))]))

        if len(segments) == 2:
            record_id = int(segments[1])
            if method == "DELETE":
                # The live API answers a successful delete with 204 and no body.
                return MockResponse(204)
            if method == "PUT":
                # The live API answers a successful update with 204 and no body.
                Util.updated[(entity, record_id)] = (kwargs.get("json") or {}).get("name", "Updated")
                return MockResponse(204)
            return MockResponse(200, record(record_id, Util.updated.get((entity, record_id), "Example")))

        if method == "POST":
            return MockResponse(201, record(99, (kwargs.get("json") or {}).get("name", "Created")))

        if params.get("$filter") == "invalid":
            return MockResponse(400, {"error": {"message": "invalid filter"}})
        # Only Get Compliance Score reads the control sets this narrowly, and the
        # Get Control Sets cases rely on the generic collection below.
        if entity == "ControlSets" and params.get("$select") == "id,name,enabled,isArchived":
            return MockResponse(200, collection(CONTROL_SETS))
        if entity == "ControlSetMetrics":
            wanted = (params.get("$filter") or "").replace("controlSetID eq ", "")
            rows = [row for row in CONTROL_SET_METRICS if not wanted or str(row["controlSetID"]) == wanted]
            # The scoring history is only useful newest first, and the caller asks for
            # one row, so both have to behave here as they do on the API.
            if "dateCalculated desc" in (params.get("$orderby") or ""):
                rows = sorted(rows, key=lambda row: row["dateCalculated"], reverse=True)
            if params.get("$top"):
                rows = rows[: int(params["$top"])]
            return MockResponse(200, collection(rows))
        if entity == PAGED_ENTITY and "page2" not in url:
            return MockResponse(200, collection([task(1)], next_link=f"{BASE_URL}/api/v2/{entity}?page2=true"))
        if "page2" in url:
            return MockResponse(200, collection([task(2)]))
        return MockResponse(200, collection([record(1), record(2, "Second")]))
