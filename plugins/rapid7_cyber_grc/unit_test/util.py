import json
import logging
import os
import sys

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


def record(record_id: int, name: str = "Example") -> dict:
    """A record as the API returns it, including the annotation the client must strip."""
    return {
        "@odata.context": ODATA_CONTEXT,
        "id": record_id,
        "name": name,
        "modifiedDate": "2026-01-21T20:30:44.407Z",
        "createdDate": "2026-01-20T09:00:00.000Z",
    }


def collection(records: list, next_link: str = None) -> dict:
    body = {"@odata.context": ODATA_CONTEXT, "value": records}
    if next_link:
        body["@odata.nextLink"] = next_link
    return body


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
            return MockResponse(200, text="7")

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
        if entity == PAGED_ENTITY and "page2" not in url:
            return MockResponse(200, collection([record(1)], next_link=f"{BASE_URL}/api/v2/{entity}?page2=true"))
        if "page2" in url:
            return MockResponse(200, collection([record(2)]))
        return MockResponse(200, collection([record(1), record(2, "Second")]))
