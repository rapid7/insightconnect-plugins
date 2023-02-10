import json
import logging
import os
from requests.models import Response
from insightconnect_plugin_runtime.exceptions import PluginException
from icon_cybereason.connection import Connection
from icon_cybereason.connection.schema import Input


class Util:
    @staticmethod
    def default_connector(action, connect_params: object = None):
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        if connect_params:
            params = connect_params
        else:
            params = {
                Input.HOSTNAME: "rapid7.com",
                Input.CREDENTIALS: {"username": "username", "password": "password"},
                Input.PORT: 8443,
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
    def mocked_requests_session(*args, **kwargs):
        class MockResponse:
            def __init__(self, filename, status_code):
                self.filename = filename
                self.status_code = status_code
                self.text = "This is some error text"
                self.content = None
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
        print(f"args: {args}")
        if "/login.html" in args[0]:
            return MockResponse("empty", 200)
        elif "/rest/sensors/query" in args[1]:
            _filter = kwargs["json"]["filters"]
            if _filter == [{'fieldName': 'internalIpAddress', 'operator': 'ContainsIgnoreCase', 'values': ['10.100.229.174']}]:
                return MockResponse("get_sensor", 200)
            return MockResponse("sensor_details", 200)
        elif "/rest/crimes/unified" and "/rest/sensors/query" and "/rest/remediate" in args[1]:
            print("GODDARN IT ACC WORKED")
            return None
        elif "/rest/crimes/unified" in args[1]:
            return MockResponse("malop_data", 200)
        elif "/rest/monitor/global/commands/isolate" in args[1]:
            return MockResponse("isolate_machine", 200)
        elif "/rest/monitor/global/commands/un-isolate" in args[1]:
            return MockResponse("isolate_machine", 200)
        elif "/rest/remediate" in args[1]:
            print(f"kwargs: {kwargs}")
            if kwargs["json"] == "":
                return MockResponse("quarantine_file", 200)
            return MockResponse("remediate_items", 200)
        elif "/rest/sensors/action/fileSearch" in args[1]:
            return MockResponse("search_for_files", 200)
        elif "/rest/visualsearch/query/simple" in args[1]:
            payload_malop = kwargs["json"]["queryPath"][0]["guidList"]
            if payload_malop == ["11.2189746432167327222"]:
                return MockResponse("malop_details", 200)
            elif payload_malop == ["invalid_malop_id"]:
                return MockResponse("malop_details_bad_malop", 200)
            elif payload_malop == ["malop_without_machine"]:
                return MockResponse("malop_details_bad_machine", 200)
        elif "/rest/sensors/action/archive" in args[1]:
            return MockResponse("archive_sensor", 200)
