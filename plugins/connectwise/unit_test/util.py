import json
import logging
import sys
import os

sys.path.append(os.path.abspath("../"))

import insightconnect_plugin_runtime
from icon_connectwise.connection import Connection
from icon_connectwise.connection.schema import Input


class Util:
    @staticmethod
    def default_connector(action: insightconnect_plugin_runtime.Action, params=None):
        params = {
            Input.CLIENT_ID: {"secretKey": "fake-client-id-for-connectwise"},
            Input.COMPANY: "companyname",
            Input.PRIVATE_KEY: {"secretKey": "fakeprivatekey"},
            Input.PUBLIC_KEY: "fakepublickey",
            Input.REGION: "na",
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
            def __init__(self, status_code: int, filename: str = None):
                self.status_code = status_code
                self.text = ""
                if filename:
                    self.text = Util.read_file_to_string(f"responses/{filename}")

            def json(self):
                return json.loads(self.text)

        if kwargs.get("json"):
            json_data = kwargs.get("json", {})
            if json_data.get("summary") == "create_ticket_many_parameters":
                return MockResponse(201, "create_ticket_many_parameters.json.resp")
            if json_data.get("summary") == "create_ticket_few_parameters":
                return MockResponse(201, "create_ticket_few_parameters.json.resp")
            if json_data.get("summary") == "update_ticket_many_parameters":
                return MockResponse(200, "update_ticket_many_parameters.json.resp")
            if json_data.get("summary") == "update_ticket_few_parameters":
                return MockResponse(200, "update_ticket_few_parameters.json.resp")
            if json_data.get("company", {}).get("id") == 404:
                return MockResponse(400, "company_not_found.json.resp")
            if json_data.get("text") == "create_ticket_note_many_parameters":
                return MockResponse(201, "create_ticket_note_many_parameters.json.resp")
            if json_data.get("text") == "create_ticket_note_few_parameters":
                return MockResponse(201, "create_ticket_note_few_parameters.json.resp")
            if json_data.get("text") == "create_ticket_note_no_flag":
                return MockResponse(400, "create_ticket_note_no_flag.json.resp")
            if json_data.get("text") == "update ticket note":
                return MockResponse(200, "update_ticket_note.json.resp")
        if "tickets/404" in kwargs.get("url"):
            return MockResponse(404, "ticket_not_found.json.resp")
        if "notes/404" in kwargs.get("url"):
            return MockResponse(404, "note_not_found.json.resp")
        if "companies/404" in kwargs.get("url"):
            return MockResponse(404, "company_not_found.json.resp")
        if "companies/200" in kwargs.get("url"):
            return MockResponse(200, "get_company.json.resp")
        if kwargs.get("method") == "DELETE":
            if "tickets/204/notes/2004" in kwargs.get("url"):
                return MockResponse(204)
            if "tickets/204" in kwargs.get("url"):
                return MockResponse(204)
        if "tickets/200/notes" in kwargs.get("url"):
            return MockResponse(200, "get_ticket_notes_many_parameters.json.resp")
        if "tickets/200" in kwargs.get("url"):
            return MockResponse(200, "get_ticket_by_id.json.resp")
        if "tickets/201/notes" in kwargs.get("url"):
            return MockResponse(200, "get_ticket_notes_few_parameters.json.resp")
        if kwargs.get("params"):
            request_params = kwargs.get("params", {})
            if request_params.get("conditions") == "ticket condition = invalid":
                return MockResponse(400, "get_tickets_invalid_conditions.json.resp")
            if request_params.get("conditions") == "note condition = invalid":
                return MockResponse(400, "get_ticket_notes_invalid_conditions.json.resp")
            if (
                kwargs.get("url") == "https://api-na.myconnectwise.net/v4_6_release/apis/3.0/service/tickets"
                and kwargs.get("method") == "GET"
            ):
                return MockResponse(200, "get_tickets_many_parameters.json.resp")
        if (
            kwargs.get("url") == "https://api-na.myconnectwise.net/v4_6_release/apis/3.0/service/tickets"
            and kwargs.get("method") == "GET"
        ):
            return MockResponse(200, "get_tickets_no_parameters.json.resp")

        raise NotImplementedError("Not implemented", kwargs)
