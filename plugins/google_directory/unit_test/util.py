import json
import logging
import os
import sys

sys.path.append(os.path.abspath("../"))

from icon_google_directory.connection.connection import Connection


class MockClient:
    def __init__(self):
        self.filename = None

    def users(self):
        return self

    def list(self, domain, orderBy):
        if domain == "example.com":
            self.filename = "get_users"
        if domain == "empty_list":
            self.filename = "get_users_empty_list"
        return self

    def list_next(self, request, result):
        return None

    def update(self, userKey, body):
        if body == {"suspended": True}:
            self.filename = "suspend_user"
        if body == {"suspended": False}:
            self.filename = "unsuspend_user"
        return self

    def execute(self):
        response = json.loads(
            Util.read_file_to_string(
                os.path.join(os.path.dirname(os.path.realpath(__file__)), f"responses/{self.filename}.json.resp")
            )
        )
        self.filename = None
        return response


class MockConnection:
    def __init__(self):
        self.service = MockClient()


class Util:
    @staticmethod
    def default_connector(action):
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        action.connection = MockConnection()
        action.logger = logging.getLogger("action logger")
        return action

    @staticmethod
    def read_file_to_string(filename):
        with open(filename) as my_file:
            return my_file.read()
