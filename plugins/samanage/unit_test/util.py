import logging
import sys
import os

import insightconnect_plugin_runtime

sys.path.append(os.path.abspath("../"))

from komand_samanage.connection.connection import Connection
from komand_samanage.connection.schema import Input
import json


class Util:
    @staticmethod
    def default_connector(action: insightconnect_plugin_runtime.Action):
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        # params = {
        #     Input.APIKEY: {"secretKey": "api_key"},
        #     Input.AUTHCODE: {"secretKey": "auth_code"},
        #     Input.SUBDOMAIN: "example",
        # }
        params = {
            "phone": "12345",
            "mobile_phone": "1234567",
            "name": "ExampleUser",
            "token": {"secretKey": "Examplesecretkey"},
            "email": "example@user.com",
            "role": "Example role",
            "department": "Example department",

        }
        default_connection.connect(params)
        action.connection = default_connection
        action.logger = logging.getLogger("action logger")
        return action

    @staticmethod
    def read_file_to_string(filename: str) -> str:
        with open(filename) as my_file:
            return my_file.read()

    @staticmethod
    def load_parameters(filename: str) -> dict:
        return json.loads(
            Util.read_file_to_string(
                os.path.join(os.path.dirname(os.path.realpath(__file__)), f"parameters/{filename}.json.resp")
            )
        )

    @staticmethod
    def mocked_requests(*args, **kwargs):
        class MockResponse:
            def __init__(self, filename: str, status_code: int):
                print("DL DEBUG Mock requests init")
                self.filename = filename
                self.status_code = status_code
                self.text = None

            def json(self):
                return json.loads(
                    Util.read_file_to_string(
                        os.path.join(
                            os.path.dirname(os.path.realpath(__file__)), f"parameters/{self.filename}.json.resp"
                        )
                    )
                )

            def raise_for_status(self):
                pass

        print("DLDEBUG In mocked requests function: kwards{}".format(kwargs))
        if kwargs.get("url") == "https://api.samanage.com/incidents.json":
            return MockResponse("get_ticket_custom_fields", 200)
        if kwargs.get("url") == "https://example.happyfox.com/api/1.1/json/ticket_custom_fields/":
            return MockResponse("get_ticket_custom_fields", 200)
        if kwargs.get("url") == "https://example.happyfox.com/api/1.1/json/user_custom_fields/":
            return MockResponse("get_contact_custom_fields", 200)
        if kwargs.get("files") == [
            ("attachments", ("text.txt", b"test", "text/plain")),
            ("attachments", ("text2", b"test", "text/plain")),
        ]:
            return MockResponse("create_ticket_with_attachments", 200)
        if kwargs.get("files") == [("attachments", ("text.txt", b"test", "text/plain"))]:
            return MockResponse("create_ticket_with_attachments2", 200)
        if kwargs.get("data") == {
            "name": "Test Contact",
            "email": "user@example.com",
            "subject": "New Ticket",
            "text": "Example description",
            "category": 1,
        }:
            return MockResponse("create_ticket", 200)
        if kwargs.get("json") == {
            "name": "Test Contact",
            "email": "user@example.com",
            "phone": "111111111",
            "subject": "New Ticket 3",
            "text": "Example description",
            "category": 1,
            "priority": 4,
            "assignee": 1,
            "tags": "tag1,tag2",
            "cc": "user@example.com",
            "bcc": "user@example.com",
            "due_date": "2023-01-21",
            "visible_only_staff": False,
            "t-cf-1": "test value",
            "t-cf-2": "test value",
        }:
            return MockResponse("create_ticket3", 200)
        if kwargs.get("json") == {
            "name": "Test Contact",
            "email": "user@example.com",
            "phone": "111111111",
            "subject": "New Ticket 2",
            "html": "<strong>Example description</strong>",
            "category": 1,
            "priority": 4,
            "tags": "tag1,tag2",
            "cc": "user@example.com",
            "bcc": "user@example.com",
            "due_date": "2023-01-21",
            "visible_only_staff": True,
            "t-cf-1": "test value",
        }:
            return MockResponse("create_ticket2", 200)
        if kwargs.get("json") == {
            "name": "Test Contact",
            "email": "user@example.com",
            "subject": "New Ticket",
            "text": "Example description",
            "category": 1,
        }:
            return MockResponse("create_ticket", 200)
        if kwargs.get("url") == "https://example.happyfox.com/api/1.1/json/ticket/10/delete":
            return MockResponse("delete_ticket", 200)
        if kwargs.get("url") == "https://example.happyfox.com/api/1.1/json/ticket/20/delete":
            return MockResponse("ticket_not_found", 400)
        if kwargs.get("files") == [("file", ("text.png", b"test", "image/png"))]:
            return MockResponse("create_inline_attachment", 200)
        if kwargs.get("files") == [("file", ("text.txt", b"test", "text/plain"))]:
            return MockResponse("invalid_file", 400)
        if kwargs.get("params", {}) == {"minify_response": "false", "status": 2, "sort": "categorya"}:
            return MockResponse("list_tickets_empty", 200)
        if kwargs.get("params", {}) == {"minify_response": "true", "status": 2, "sort": "clientd"}:
            return MockResponse("list_ticket_ids_empty", 200)
        if kwargs.get("params", {}).get("minify_response") == "false":
            return MockResponse("list_tickets", 200)
        if kwargs.get("params", {}).get("minify_response") == "true":
            return MockResponse("list_ticket_ids", 200)
        raise Exception("Not implemented")


def mock_request_200(*args, **kwargs):
    return Util.mocked_requests(url=args[1], status_code=200)
