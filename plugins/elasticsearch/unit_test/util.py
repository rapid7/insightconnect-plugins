import json
import logging
import os

from insightconnect_plugin_runtime.exceptions import PluginException
from komand_elasticsearch.connection import Connection
from komand_elasticsearch.connection.schema import Input


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
                Input.CREDENTIALS: {"username": "user", "password": "pass"},
                Input.USE_AUTHENTICATION: True,
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
    def mocked_requests_get(*args, **kwargs):
        class MockResponse:
            def __init__(self, filename, status_code):
                self.filename = filename
                self.status_code = status_code
                self.text = "This is some error text"

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

        if args[1] == "https://rapid7.com/":
            return MockResponse("main_page", 200)
        elif "wrong_object/_search" in args[1]:
            return MockResponse("search_document_wrong_object", 200)
        elif "test-index/_doc" in args[1]:
            return MockResponse("index_without_id", 201)
        elif "test-index2/_doc" in args[1]:
            return MockResponse("index_with_id", 200)
        elif "empty" in args[1]:
            return MockResponse("empty", 200)
        elif "TriggerError" in args[1]:
            return MockResponse("error", 200)
        elif "search-without-route" in args[1]:
            return MockResponse("search_without_route", 200)
        elif "search/_search" in args[1] or "trigger-index" in args[1]:
            return MockResponse("search_document", 200)
        elif "UpdateError" in args[1]:
            return MockResponse("update_document_error", 400)
        elif "update" in args[1]:
            return MockResponse("update_document", 200)

        return MockResponse("cluster_health", 200)
