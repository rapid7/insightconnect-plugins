import logging
import os

from komand_get_url.connection.connection import Connection


class MockResponse:
    def __init__(self, filename, status_code):
        self.filename = filename
        self.code = status_code
        self.headers = {"etag": "test", "last-modified": "test"}

    def read(self):
        return Util.read_file_to_bytes(
            os.path.join(os.path.dirname(os.path.realpath(__file__)), f"payloads/{self.filename}")
        )


class Util:
    @staticmethod
    def default_connector(action):
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        action.connection = default_connection
        action.logger = logging.getLogger("action logger")
        return action

    @staticmethod
    def read_file_to_bytes(filename):
        with open(filename, "rb") as my_file:
            return my_file.read()

    @staticmethod
    def mocked_request(*args, **kwargs):
        if args[0].full_url == "https://test.com/v1/test.pdf":
            return MockResponse("test.pdf", 200)
        elif args[0].full_url == "https://test.com/v1/test.txt":
            return MockResponse("test.txt", 200)

    @staticmethod
    def mocked_url_open(*args, **kwargs):
        return MockResponse("test.txt", 200)

    @staticmethod
    def mock_for_cache_creation(*args, **kwargs):
        class MockCache:
            def write(self, content):
                pass

            def close(self):
                pass

        return MockCache()
