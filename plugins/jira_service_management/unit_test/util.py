import json
import logging
import os

from icon_jira_service_management.connection.connection import Connection
from icon_jira_service_management.connection.schema import Input


class Util:
    @staticmethod
    def default_connector(action, connect_params: object = None):
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        if connect_params:
            params = connect_params
        else:
            params = {
                Input.API_TOKEN: {"secretKey": "1234567890abcdef1234567890abcdef"},
                Input.EMAIL: "test@test.com",
                Input.CLOUD_ID: "123456789",
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
    def read_file_to_bytes(filename):
        with open(filename, "rb") as my_file:
            return my_file.read()

    @staticmethod
    def read_file_to_dict(filename):
        return json.loads(Util.read_file_to_string(os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)))

    @staticmethod
    def mocked_requests(*args, **kwargs):
        class MockResponse:
            def __init__(self, filename, status_code, headers=None):
                if headers is None:
                    headers = {"Content-Type": "application/json"}
                self.status_code = status_code
                self.headers = headers
                if filename:
                    self.content = Util.read_file_to_bytes(
                        os.path.join(os.path.dirname(os.path.realpath(__file__)), f"payloads/{filename}.resp")
                    )
                    self.text = self.content.decode("UTF-8")

            def json(self):
                return json.loads(self.text)

            def raise_for_status(self):
                if self.status_code >= 400:
                    raise Exception(f"HTTP {self.status_code}")

        url = args[0].url

        if url == "https://api.atlassian.com/jsm/ops/api/123456789/v1/alerts":
            return MockResponse("create_alert_request.json", 200)
        elif (
            url
            == "https://api.atlassian.com/jsm/ops/api/123456789/v1/alerts/requests/12345678-d325-4xx9-1234-8ee2c35e4606"
        ):
            return MockResponse("get_request_status_request.json", 200)

        raise Exception("Not implemented")
