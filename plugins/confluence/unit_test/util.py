import logging
import os
import sys
import json

from atlassian.errors import ApiPermissionError

from komand_confluence.util.api import ConfluenceAPI

sys.path.append(os.path.abspath("../"))


class MockConnection:
    def __init__(self):
        self.url = ("https://test.atlassian.net",)
        self.client = ConfluenceAPI()

    def get_headers(self):
        return


class Util:
    @staticmethod
    def default_connector(action, connect_params: object = None):
        default_connection = MockConnection()
        default_connection.logger = logging.getLogger("connection logger")
        action.connection = default_connection
        action.logger = logging.getLogger("action logger")
        return action

    @staticmethod
    def read_file_to_string(filename):
        with open(filename) as my_file:
            return my_file.read()

    @staticmethod
    def load_data(filename, directory="responses"):
        return json.loads(
            Util.read_file_to_string(
                os.path.join(
                    os.path.dirname(os.path.realpath(__file__)),
                    f"{directory}/{filename}.json.resp",
                )
            )
        )

    @staticmethod
    def mocked_requests(*args, **kwargs):
        if (
            kwargs.get("title") == "Test Page New"
            and kwargs.get("body") == "<p>Test Content</p>"
        ):
            return Util.load_data("store_page_content_new")
        if kwargs.get("title") == "Test Page New":
            return False
        if (
            kwargs.get("page_id") == "100001"
            and kwargs.get("title") == "Test Page"
            and kwargs.get("body") == "<p>Test Content</p>"
        ):
            return Util.load_data("store_page_content")
        if (
            kwargs.get("page_id") == "100001"
            and kwargs.get("title") == "Test Page"
            and kwargs.get("body") == "<p>Test Content Failure</p>"
        ):
            raise ApiPermissionError
        if kwargs.get("title") == "Test Page" and kwargs.get("space") == "Test Space":
            return "100001"
        if (
            kwargs.get("title") == "Test Home Page"
            and kwargs.get("space") == "Test Space"
        ):
            return "100002"
        if (
            kwargs.get("title") == "Test Not Found"
            and kwargs.get("space") == "Test Space"
        ):
            return None
        if (
            kwargs.get("title") == "Test Page"
            and kwargs.get("space") == "Test Not Found"
        ):
            raise ApiPermissionError
        if kwargs.get("page_id") == "100001":
            return Util.load_data("get_page")
        if kwargs.get("page_id") == "100002":
            return Util.load_data("get_page_home")
