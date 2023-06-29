import json
import logging
import os
import sys
from komand_vmray.connection.connection import Connection
from komand_vmray.connection.schema import Input

sys.path.append(os.path.abspath("../"))


class Util:
    @staticmethod
    def default_connector(action, connect_params: object = None):
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        if connect_params:
            params = connect_params
        else:
            params = {
                Input.URL: {},
                Input.API_KEY: ""
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
    def load_data(filename, path="payloads"):
        return json.loads(
            Util.read_file_to_string(
                os.path.join(os.path.dirname(os.path.realpath(__file__)), f"{path}/{filename}.json.resp")
            )
        )

    @staticmethod
    def mocked_requests(*args, **kwargs):
        class MockResponse:
            def __init__(self, filename, status_code):
                self.filename = filename
                self.status_code = status_code
                self.headers = Util.load_data(self.filename).get("headers", {})
                if self.filename == "not_found":
                    self.text = 'Response was: {"message": "Not Found"}'
                elif self.filename == "already_exists":
                    self.text = 'Response was: {"message": "Already Exists"}'
                else:
                    self.text = str(self.json())

            def json(self):
                return Util.load_data(self.filename).get("json", {})

            def raise_for_status(self):
                return

        data = kwargs.get("data")
        url = kwargs.get("url")
        if url == "https://www.example.com/post":
            return MockResponse("post", 200)
        if url == "https://www.example.com/get":
            return MockResponse("get", 200)
        if url == "https://www.example.com/put" and data == None:
            return MockResponse("put_json_empty_body", 200)
        if url == "https://www.example.com/put" and data == b'{"example": "value"}':
            return MockResponse("put_json_body", 200)
        if url == "https://www.example.com/put" and data == b"example=xwwwf":
            return MockResponse("put_json_body_x_www_form_urlencoded", 200)
        if url == "https://www.example.com/put" and data == b'{"example": "\\nv\xc3\xa1l\xc3\xbc\xc3\xa9\\n"}':
            return MockResponse("put_json_non_latin", 200)
        if url == "https://www.example.com/put" and data == b"example":
            return MockResponse("put_plain_text", 200)
        if url == "https://www.example.com/put" and data == b'{"example": "404_false"}':
            return MockResponse("put_404_false_failure", 404)
        if url == "https://www.example.com/put_401":
            return MockResponse("put_error", 401)
        if url == "https://www.example.com/put_403":
            return MockResponse("put_error", 403)
        if url == "https://www.example.com/put_404":
            return MockResponse("put_error", 404)
        if url == "https://www.example.com/put_400":
            return MockResponse("put_error", 400)
        if url == "https://www.example.com/put_500":
            return MockResponse("put_error", 500)
        if url == "https://www.example.com/delete":
            return MockResponse("delete", 200)
        if url == "https://www.example.com/patch":
            return MockResponse("patch", 200)
        if url == "https://www.example.com":
            return MockResponse("connection_test", 200)
        raise Exception("Not implemented")
