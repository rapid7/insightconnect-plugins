import logging
import sys
import os

sys.path.append(os.path.abspath("../"))

from icon_easyvista.connection.connection import Connection
from icon_easyvista.connection.schema import Input
import json


class Util:
    @staticmethod
    def default_connector(action):
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        params = {
            Input.CLIENT_LOGIN: {"username": "user", "password": "password"},
            Input.ACCOUNT: 50004,
            Input.URL: "https://example.easyvista.com",
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
                self.text = ""
                if self.filename in [
                    "create_ticket_invalid_impact_id",
                    "create_ticket_invalid_urgency_id",
                    "update_ticket_nothing_to_update",
                    "update_ticket_invalid_input",
                ]:
                    self.text = Util.read_file_to_string(
                        os.path.join(os.path.dirname(os.path.realpath(__file__)), f"responses/{filename}.json.resp")
                    )

            def json(self):
                return json.loads(
                    Util.read_file_to_string(
                        os.path.join(
                            os.path.dirname(os.path.realpath(__file__)), f"responses/{self.filename}.json.resp"
                        )
                    )
                )

        if kwargs.get("json") == {"requests": [{"catalog_guid": "44D88612-FEA8-A8F3-6DE8-2E1278ABB02F"}]}:
            return MockResponse("ticket_2", 201)
        if kwargs.get("json") == {
            "requests": [{"impact_id": "0", "catalog_guid": "44D88612-FEA8-A8F3-6DE8-2E1278ABB02F"}]
        }:
            return MockResponse("create_ticket_invalid_impact_id", 590)
        if kwargs.get("json") == {
            "requests": [{"urgency_id": "0", "catalog_guid": "44D88612-FEA8-A8F3-6DE8-2E1278ABB02F"}]
        }:
            return MockResponse("create_ticket_invalid_urgency_id", 590)
        if kwargs.get("json") == {"rfc_number": "I2210526_000003"}:
            return MockResponse("update_ticket_nothing_to_update", 590)
        if kwargs.get("json") == {"rfc_number": "I2210526_000001", "urgency_id": "0"}:
            return MockResponse("update_ticket_invalid_input", 590)
        if kwargs.get("url") == "https://example.easyvista.com/api/v1/50004/requests":
            return MockResponse("ticket", 201)
        if kwargs.get("url") == "https://example.easyvista.com/api/v1/50004/requests/I2210526_000001":
            return MockResponse("ticket", 201)
        if kwargs.get("url") == "https://example.easyvista.com/api/v1/50004/requests/I2210526_000099":
            return MockResponse("not_found", 404)
        if kwargs.get("url") == "https://example.easyvista.com/api/v1/50004/requests?search=I2210520_000001":
            return MockResponse("search_ticket", 200)
        if kwargs.get("url") == "https://example.easyvista.com/api/v1/50004/requests?search=I2210520_000009":
            return MockResponse("search_ticket_not_found", 200)
        raise Exception("Not implemented")
