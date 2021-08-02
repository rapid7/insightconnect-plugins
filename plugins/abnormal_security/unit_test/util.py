import json
import logging
import os
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
                if self.filename == "manage_threat_invalid_id":
                    self.text = 'Response was: {"message": "Threat action does not exist"}'
                elif self.filename == "manage_case_invalid_id":
                    self.text = 'Response was: {"message": "Case action does not exist"}'
                else:
                    self.text = "Error message"

            def json(self):
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
        elif args[1] == "https://rapid7.com/v1/threats/a456b27b-6d7c-362a-efef-b22489d379e2":
            return MockResponse("manage_threat_remediate", 202)
        elif args[1] == "https://rapid7.com/v1/threats/763ab210-6d8b-220c-89d3-10aa87524bba":
            return MockResponse("manage_threat_unremediate", 202)
        elif args[1] == "https://rapid7.com/v1/threats/53ca2899-d987-22aa-30a7-22aa987c4319":
            return MockResponse("manage_threat_invalid_id", 404)
        elif args[1] == "https://rapid7.com/v1/cases/12345":
            return MockResponse("manage_case_not_an_attack", 202)
        elif args[1] == "https://rapid7.com/v1/cases/34567":
            return MockResponse("manage_case_action_required", 202)
        elif args[1] == "https://rapid7.com/v1/cases/23456":
            return MockResponse("manage_case_in_progress", 202)
        elif args[1] == "https://rapid7.com/v1/cases/45678":
            return MockResponse("manage_case_resolved", 202)
        elif args[1] == "https://rapid7.com/v1/cases/56789":
            return MockResponse("manage_case_invalid_id", 404)

        raise Exception("Not implemented")
