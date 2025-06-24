from unittest.mock import MagicMock
from icon_matrix42.connection.connection import Connection
from insightconnect_plugin_runtime.exceptions import PluginException
import json
import os


class Util:
    @staticmethod
    def read_file_to_string(filename):
        with open(filename) as my_file:
            return my_file.read()

    @staticmethod
    def load_parameters(filename):
        return json.loads(
            Util.read_file_to_string(
                os.path.join(os.path.dirname(os.path.realpath(__file__)), f"parameters/{filename}.json.resp")
            )
        )

    @staticmethod
    def mocked_requests(*args, **kwargs):
        class MockResponse:
            def __init__(self, filename, status_code=200):
                self.filename = filename
                self.status_code = status_code

            def raise_for_status(self):
                if self.status_code != 200:
                    raise PluginException(
                        cause="Failed to create ticket in Matrix42.",
                        assistance="Please check your Matrix42 connection, credentials, and input parameters.",
                        data=f"Mock request failed with status code {self.status_code}",
                    )
                return None

            def json(self):
                return json.loads(
                    Util.read_file_to_string(
                        os.path.join(
                            os.path.dirname(os.path.realpath(__file__)), f"responses/{self.filename}.json.resp"
                        )
                    )
                )

        url = kwargs.get("url")

        if kwargs.get("json", {}).get("Subject") == 1:
            return MockResponse("bad request", 400)

        if url.endswith("ticket/create?activityType=6"):
            return MockResponse("create_service_request_ticket")

    @staticmethod
    def default_connection(action):
        connection = Connection()
        connection.api_url = "https://fake-url/"
        connection.api_key = "fake-key"
        connection.access_token = "mocked-access-token"
        connection.request_header = {
            "Authorization": f"Bearer {connection.access_token}",
            "Accept": "application/json",
            "Content-Type": "application/json",
        }
        action.connection = connection
        action.logger = MagicMock()
        return action
