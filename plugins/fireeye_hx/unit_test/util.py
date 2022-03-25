import logging
import os
from icon_fireeye_hx.connection.connection import Connection
from icon_fireeye_hx.connection.schema import Input
import json


class Util:
    @staticmethod
    def default_connector(action):
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        params = {
            Input.URL: "https://example.com",
            Input.USERNAME_PASSWORD: {"password": "password", "username": "user"},
            Input.SSL_VERIFY: True,
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
    def mocked_requests(*args, **kwargs):
        class MockResponse:
            def __init__(self, filename, status_code):
                self.filename = filename
                self.status_code = status_code
                self.text = ""

                if self.filename == "not_found":
                    self.text = '{"message": "Not Found"}'

            def json(self):
                return json.loads(
                    Util.read_file_to_string(
                        os.path.join(os.path.dirname(os.path.realpath(__file__)), f"payloads/{self.filename}.json.resp")
                    )
                )

        params = kwargs.get("params")
        url = kwargs.get("url")
        method = kwargs.get("method")

        if params == {"search": "example_hostname"}:
            return MockResponse("get_host_id", 200)
        if params == {"search": "invalid_hostname"}:
            return MockResponse("get_host_id2", 200)
        if method == "POST" and url == "https://example.com/hx/api/v3/hosts/1111111111/containment":
            return MockResponse("send_request_for_host_containment", 202)
        if method == "PATCH" and url == "https://example.com/hx/api/v3/hosts/1111111111/containment":
            return MockResponse("approve_request_for_host_containment", 201)
        if method == "DELETE" and url == "https://example.com/hx/api/v3/hosts/1111111111/containment":
            return MockResponse("delete_host_containment", 204)
        if method == "GET" and url == "https://example.com/hx/api/v3/hosts/1111111111/containment":
            return MockResponse("get_containment_state", 200)
        if url == "https://example.com/hx/api/v3/hosts/invalid_host_id/containment":
            return MockResponse("not_found", 404)
        raise Exception("Not implemented")
