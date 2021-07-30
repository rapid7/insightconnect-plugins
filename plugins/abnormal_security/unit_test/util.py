import json
import logging
import os
from insightconnect_plugin_runtime.exceptions import PluginException
from icon_abnormal_security.connection.connection import Connection
from icon_abnormal_security.connection.schema import Input


class Util:
    @staticmethod
    def default_connector(action, connect_params: object = None):
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        if connect_params:
            params = connect_params
        else:
            params = {
                Input.URL: "https://rapid7.com",
                Input.API_KEY: {"secretKey": "9de5069c5afe602b2ea0a04b66beb2c0"},
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
                self.content = None
                self.text = "This is some error text"

                if self.filename not in ["error", "empty"]:
                    self.content = Util.read_file_to_string(
                        os.path.join(os.path.dirname(os.path.realpath(__file__)), f"payloads/{self.filename}.json.resp")
                    )

            def json(self):
                if self.filename == "error":
                    raise PluginException(preset=PluginException.Preset.SERVER_ERROR)
                if self.filename == "empty":
                    return {}

                return json.loads(
                    Util.read_file_to_string(
                        os.path.join(os.path.dirname(os.path.realpath(__file__)), f"payloads/{self.filename}.json.resp")
                    )
                )

        if args[1] == "https://rapid7.com/v1/cases/19377":
            return MockResponse("get_case_details", 200)
        elif args[1] == "https://rapid7.com/v1/cases/19300":
            return MockResponse("get_case_details2", 200)
        elif args[1] == "https://rapid7.com/v1/cases":
            return MockResponse("get_cases", 200)
        elif args[1] == "https://rapid7.com/v1/threats":
            return MockResponse("get_threats", 200)

        raise Exception("Not implemented")
