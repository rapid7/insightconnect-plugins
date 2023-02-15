import logging
import sys
import os

import insightconnect_plugin_runtime

sys.path.append(os.path.abspath("../"))

from komand_samanage.connection.connection import Connection
from komand_samanage.connection.schema import Input
import json


class Util:
    @staticmethod
    def default_connector(action: insightconnect_plugin_runtime.Action):
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        # params = {
        #     Input.APIKEY: {"secretKey": "api_key"},
        #     Input.AUTHCODE: {"secretKey": "auth_code"},
        #     Input.SUBDOMAIN: "example",
        # }
        params = {
            "phone": "12345",
            "mobile_phone": "1234567",
            "name": "ExampleUser",
            "token": {"secretKey": "Examplesecretkey"},
            "email": "example@user.com",
            "role": "Example role",
            "department": "Example department",

        }
        default_connection.connect(params)
        action.connection = default_connection
        action.logger = logging.getLogger("action logger")
        return action

    @staticmethod
    def read_file_to_string(filename: str) -> str:
        with open(filename) as my_file:
            return my_file.read()

    @staticmethod
    def load_parameters(filename: str) -> dict:
        return json.loads(
            Util.read_file_to_string(
                os.path.join(os.path.dirname(os.path.realpath(__file__)), f"parameters/{filename}.json.resp")
            )
        )

    @staticmethod
    def mocked_requests(*args, **kwargs):
        class MockResponse:
            def __init__(self, filename: str, status_code: int):
                print("DL DEBUG Mock requests init")
                self.filename = filename
                self.status_code = status_code
                self.text = None

            def json(self):
                return json.loads(
                    Util.read_file_to_string(
                        os.path.join(
                            os.path.dirname(os.path.realpath(__file__)), f"responses/{self.filename}.json.resp"
                        )
                    )
                )

            def raise_for_status(self):
                pass

        print("DLDEBUG In mocked requests function: kwards{}".format(kwargs))
        if kwargs.get("url") == "https://api.samanage.com/incidents.json":
            return MockResponse("list_incidents", 200)
        if kwargs.get("url") == "https://api.samanage.com/users.json":
            return MockResponse("list_users", 200)
        if kwargs.get("url") == "https://api.samanage.com/incidents/12345.json":
            return MockResponse("get_incident", 200)
        if kwargs.get("url") == "https://api.samanage.com/incidents/6789/comments.json":
            return MockResponse("get_comments", 200)
        raise Exception("Not implemented")


def mock_request_200(*args, **kwargs):
    breakpoint()
    return Util.mocked_requests(url=args[1], status_code=200)
