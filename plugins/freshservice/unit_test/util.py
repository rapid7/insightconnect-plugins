import logging
import sys
import os

sys.path.append(os.path.abspath("../"))

from icon_freshservice.connection.connection import Connection
from icon_freshservice.connection.schema import Input
import json


class Util:
    @staticmethod
    def default_connector(action):
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        params = {
            Input.APIKEY: {"secretKey": "api_key"},
            Input.SUBDOMAIN: "example",
        }
        default_connection.connect(params)
        action.connection = default_connection
        action.logger = logging.getLogger("action logger")
        return action

    @staticmethod
    def read_file_to_string(filename):
        with open(filename) as my_file:
            return my_file.read()

    @staticmethod
    def load_parameters(filename):
        return json.loads(
            Util.read_file_to_string(
                os.path.join(os.path.dirname(os.path.realpath(__file__)), f"parameters/{filename}.json.resp")
            )
        )

    @staticmethod
    def mocked_requests(*args, **kwargs):
        class MockResponse:
            def __init__(self, filename, status_code):
                self.filename = filename
                self.status_code = status_code
                self.text = None

            def json(self):
                return json.loads(
                    Util.read_file_to_string(
                        os.path.join(
                            os.path.dirname(os.path.realpath(__file__)), f"responses/{self.filename}.json.resp"
                        )
                    )
                )

        if kwargs.get("url") == "https://example.freshservice.com/api/v2/groups":
            return MockResponse("list_all_groups", 200)
        if kwargs.get("url") == "https://example.freshservice.com/api/v2/agents" and kwargs.get("params") == {
            "email": "user@example.com",
            "mobile_phone_number": None,
            "work_phone_number": "11111111",
            "active": "false",
            "state": "fulltime",
        }:
            return MockResponse("list_all_agents2", 200)
        if kwargs.get("url") == "https://example.freshservice.com/api/v2/agents" and kwargs.get("params") == {
            "email": "user2@example.com",
            "mobile_phone_number": "22222222",
            "work_phone_number": None,
            "active": "true",
            "state": "fulltime",
        }:
            return MockResponse("list_all_agents3", 200)
        if kwargs.get("url") == "https://example.freshservice.com/api/v2/agents" and kwargs.get("params") == {
            "email": "user@example.com",
            "mobile_phone_number": "22222222",
            "work_phone_number": None,
            "active": None,
            "state": "occasional",
        }:
            return MockResponse("list_all_agents_empty", 200)
        if kwargs.get("url") == "https://example.freshservice.com/api/v2/agents":
            return MockResponse("list_all_agents", 200)
        if kwargs.get("url") == "https://example.freshservice.com/api/v2/tickets/1/tasks":
            return MockResponse("create_ticket_task", 201)
        if kwargs.get("url") == "https://example.freshservice.com/api/v2/tickets/2/tasks":
            return MockResponse("create_ticket_task2", 201)
        if kwargs.get("url") == "https://example.freshservice.com/api/v2/tickets/3/tasks":
            return MockResponse("ticket_not_found", 404)
        if (
            kwargs.get("method") == "DELETE"
            and kwargs.get("url") == "https://example.freshservice.com/api/v2/tickets/1/tasks/1"
        ):
            return MockResponse("success", 204)
        if (
            kwargs.get("method") == "DELETE"
            and kwargs.get("url") == "https://example.freshservice.com/api/v2/tickets/2/tasks/1"
        ):
            return MockResponse("ticket_not_found", 404)
        if (
            kwargs.get("method") == "DELETE"
            and kwargs.get("url") == "https://example.freshservice.com/api/v2/tickets/1/tasks/2"
        ):
            return MockResponse("task_not_found", 404)
        if kwargs.get("url") == "https://example.freshservice.com/api/v2/tickets/1/tasks/1":
            return MockResponse("update_ticket_task", 200)
        if kwargs.get("url") == "https://example.freshservice.com/api/v2/tickets/1/tasks/2":
            return MockResponse("update_ticket_task2", 200)
        if kwargs.get("url") == "https://example.freshservice.com/api/v2/tickets/2/tasks/1":
            return MockResponse("ticket_not_found", 404)
        if kwargs.get("url") == "https://example.freshservice.com/api/v2/tickets/1/tasks/3":
            return MockResponse("task_not_found", 404)
        if (
            kwargs.get("method") == "DELETE"
            and kwargs.get("url") == "https://example.freshservice.com/api/v2/tickets/1"
        ):
            return MockResponse("success", 204)
        if (
            kwargs.get("method") == "DELETE"
            and kwargs.get("url") == "https://example.freshservice.com/api/v2/tickets/2"
        ):
            return MockResponse("ticket_not_found", 404)
        if kwargs.get("url") == "https://example.freshservice.com/api/v2/tickets" and kwargs.get("json") == {
            "requester_id": 987654321,
            "subject": "New Ticket",
            "description": "Example description",
            "status": 2,
            "priority": 1,
        }:
            return MockResponse("create_ticket", 200)
        if kwargs.get("url") == "https://example.freshservice.com/api/v2/tickets" and kwargs.get("json") == {
            "email": "user@example.com",
            "subject": "New Ticket",
            "description": "Example description",
            "status": 2,
            "priority": 1,
        }:
            return MockResponse("create_ticket", 200)
        if kwargs.get("url") == "https://example.freshservice.com/api/v2/tickets/1":
            return MockResponse("update_ticket", 200)
        if kwargs.get("url") == "https://example.freshservice.com/api/v2/tickets/2":
            return MockResponse("update_ticket2", 200)
        if kwargs.get("url") == "https://example.freshservice.com/api/v2/tickets/3":
            return MockResponse("ticket_not_found", 404)
        if kwargs.get("files") == {"attachments[]": ("test.txt", b"test", "text/plain")}:
            return MockResponse("create_ticket2", 200)
        if kwargs.get("url") == "https://example.freshservice.com/api/v2/tickets" and kwargs.get("params") == {
            "filter": "new_and_my_open",
            "requester_id": 987654321,
            "email": None,
            "updated_since": "2022-11-24T10:00:00Z",
            "type": None,
            "order_type": "asc",
            "page": 1,
            "per_page": 20,
        }:
            return MockResponse("list_tickets2", 200)
        if kwargs.get("url") == "https://example.freshservice.com/api/v2/tickets" and kwargs.get("params") == {
            "filter": "watching",
            "requester_id": 123456789,
            "email": "user@example.com",
            "updated_since": None,
            "type": "Incident",
            "order_type": "desc",
            "page": None,
            "per_page": 100,
        }:
            return MockResponse("list_tickets3", 200)
        if kwargs.get("url") == "https://example.freshservice.com/api/v2/tickets" and kwargs.get("params") == {
            "filter": "deleted",
            "requester_id": None,
            "email": None,
            "updated_since": None,
            "type": "Service Request",
            "order_type": None,
            "page": 1,
            "per_page": 100,
        }:
            return MockResponse("list_tickets_empty", 200)
        if kwargs.get("url") == "https://example.freshservice.com/api/v2/tickets":
            return MockResponse("list_tickets", 200)
        raise Exception("Not implemented")
