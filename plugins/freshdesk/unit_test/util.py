import json
import logging
import sys
import os

import insightconnect_plugin_runtime
from requests import HTTPError

sys.path.append(os.path.abspath("../"))

from icon_freshdesk.connection import Connection
from icon_freshdesk.connection.schema import Input


class Util:
    @staticmethod
    def default_connector(action: insightconnect_plugin_runtime.Action, params=None):
        if not params:
            params = {
                Input.APIKEY: {"secretKey": "my-api-key"},
                Input.DOMAINNAME: "exampledomain",
            }
        action.connection = Connection()
        action.connection.meta = "{}"
        action.connection.logger = logging.getLogger("connection logger")
        action.connection.connect(params)
        action.logger = logging.getLogger("action logger")
        return action

    @staticmethod
    def read_file_to_string(filename: str) -> str:
        with open(
            os.path.join(os.path.dirname(os.path.realpath(__file__)), filename), "r", encoding="utf-8"
        ) as file_reader:
            return file_reader.read()

    @staticmethod
    def read_file_to_dict(filename: str) -> dict:
        return json.loads(Util.read_file_to_string(filename))

    @staticmethod
    def mock_request(*args, **kwargs):
        class MockResponse:
            def __init__(self, status_code: int, filename: str = None, url: str = ""):
                self.status_code = status_code
                self.text = ""
                self.url = url
                if filename:
                    self.text = Util.read_file_to_string(f"responses/{filename}")

            def json(self):
                return json.loads(self.text)

            def text(self):
                return self.text

            def raise_for_status(self):
                if self.status_code > 300:
                    raise HTTPError(f"{self.status_code} Client Error", response=self)

        json_data = kwargs.get("json", {})
        params = kwargs.get("params", {})
        files = kwargs.get("files", {})
        url = kwargs.get("url")
        method = kwargs.get("method")
        if url == "https://exampledomain.freshdesk.com/api/v2/search/tickets":
            if params == {"query": '"group_id:123456789 AND status:99"', "page": 2}:
                return MockResponse(400, "filter_tickets_error.json.resp")
            return MockResponse(200, "filter_tickets.json.resp")
        if url == "https://exampledomain.freshdesk.com/api/v2/ticket_fields":
            return MockResponse(200, "get_ticket_fields.json.resp")
        if url == "https://exampledomain.freshdesk.com/api/v2/tickets/404":
            return MockResponse(404, "")
        if url.startswith("https://exampledomain.freshdesk.com/api/v2/tickets/113"):
            return MockResponse(200, "get_ticket_by_id.json.resp")
        if url == ("https://exampledomain.freshdesk.com/api/v2/tickets") and method == "GET":
            if params.get("company_id") == "404":
                return MockResponse(400, "get_tickets_invalid_company_id.json.resp")
            elif params:
                return MockResponse(200, "get_tickets_many_parameters.json.resp")
            else:
                return MockResponse(200, "get_tickets_no_parameters.json.resp")
        if json_data:
            if json_data.get("subject") == "Create ticket many parameters":
                return MockResponse(201, "create_ticket_many_parameters.json.resp")
            if json_data.get("subject") == "Create ticket few parameters":
                return MockResponse(201, "create_ticket_few_parameters.json.resp")
            if json_data.get("subject") == "update ticket few parameters":
                return MockResponse(201, "update_ticket_few_parameters.json.resp")
            if json_data.get("subject") == "update ticket many parameters":
                return MockResponse(201, "update_ticket_many_parameters.json.resp")
            if json_data.get("subject") == "Invalid related ticket ids":
                return MockResponse(400, "invalid_related_ticket_ids.json.resp")
        if files:
            if "create.png" in files[0][1]:
                return MockResponse(201, "create_ticket_many_parameters_add_attachment.json.resp")
            if "update.png" in files[0][1]:
                return MockResponse(201, "update_ticket_many_parameters_add_attachment.json.resp")

        raise NotImplementedError("Not implemented", kwargs)
