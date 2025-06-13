from unittest.mock import MagicMock
from icon_matrix42.connection.connection import Connection
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
            def __init__(self, filename):
                self.filename = filename

            def raise_for_status(self):
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

        if url.endswith("ticket/create?activityType=6"):
            return MockResponse("create_service_request_ticket")

    @staticmethod
    def default_connection(action):
        connection = Connection()
        connection.api_url = "https://fake-url/"
        connection.api_key = "fake-key"
        connection.access_token = "mocked-access-token"
        action.connection = connection
        action.logger = MagicMock()
        return action
