import logging
import os
import json
from icon_ipstack.connection import Connection
from icon_ipstack.connection.schema import Input

from insightconnect_plugin_runtime.exceptions import PluginException


class Util:
    @staticmethod
    def read_file_to_string(filename):
        with open(filename, "rt") as my_file:
            return my_file.read()

    @staticmethod
    def mocked_requests_get(*args, **kwargs):
        class MockResponse:
            def __init__(self, filename):
                self.filename = filename

            def read(self):
                if self.filename == "error":
                    raise PluginException(preset=PluginException.Preset.SERVER_ERROR)
                if self.filename == "empty":
                    return {}
                file_path = os.path.join(
                    os.path.dirname(os.path.realpath(__file__)), "example_output", f"{self.filename}.json.resp"
                )
                file_text = Util.read_file_to_string(file_path)
                return file_text

        if "BADTOKEN" in args[0]:
            return MockResponse("bad_access_key")
        elif "rapid7.com" in args[0]:
            return MockResponse("tested_rapid7_output")
        elif "ipstack_features" in args[0]:
            return MockResponse("ipstack_doc_example")
        elif "unauthorized_user" in args[0]:
            return MockResponse("unauthorized_user")
        elif "rapid7.typocom" in args[0]:
            return MockResponse("invalid_address")
        elif "limit_hit" in args[0]:
            return MockResponse("max_monthly_lookups_hit")
        elif "user_inactive" in args[0]:
            return MockResponse("user_account_not_active")
        elif "generic_error" in args[0]:
            return MockResponse("generic_error")
        elif "404" in args[0]:
            return MockResponse("url_changed")
        else:
            return MockResponse("error")

    @staticmethod
    def default_connector(action, connect_params: object = None):
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        if connect_params:
            params = connect_params
        else:
            params = {Input.CRED_TOKEN: {"secretKey": "ExampleAuthToken"}}
        default_connection.connect(params)
        action.connection = default_connection
        action.logger = logging.getLogger("action logger")
        return action
