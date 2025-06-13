from unittest.mock import MagicMock
from icon_matrix42.connection.connection import Connection

class Util:
    @staticmethod
    def mocked_requests(*args, **kwargs):
        class MockResponse:
            def __init__(self):
                self.text = '"3db8e0a1-1d53-f011-1887-000d3aed261c"'
            def raise_for_status(self):
                return None
        return MockResponse()

    @staticmethod
    def default_connection(action):
        connection = Connection()
        connection.api_url = "https://fake-url/"
        connection.api_key = "fake-key"
        connection.access_token = "mocked-access-token"
        action.connection = connection
        action.logger = MagicMock()
        return action
