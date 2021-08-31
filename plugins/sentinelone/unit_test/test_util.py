import sys
import os

sys.path.append(os.path.abspath("../"))


from komand_sentinelone.connection.connection import Connection
import json
import logging

from insightconnect_plugin_runtime.exceptions import PluginException
from komand_sentinelone.connection.schema import Input


class Util:
    @staticmethod
    def default_connector(action, connect_params: object = None):
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        if connect_params:
            params = connect_params
        else:
            params = {Input.URL: "rapid7.com", Input.CREDENTIALS: {"username": "username", "password": "password"}}
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

        if args[0] == "rapid7.com/web/api/v2.1/users/login":
            return MockResponse("get_token", 200)
        elif args[0] == "rapid7.com/web/api/v2.1/agents?networkInterfaceInet__contains=10.10.10.10":
            return MockResponse("none_in_location", 200)
        elif args[0] == args[0] == "rapid7.com/web/api/v2.1/agents?externalIp__contains=10.10.10.10":
            return MockResponse("none_in_location", 404)
        elif args[0] == args[0] == "rapid7.com/web/api/v2.1/agents?externalIp__contains=10.10.10.11":
            return MockResponse("good_response", 200)
        return MockResponse("error", 404)
