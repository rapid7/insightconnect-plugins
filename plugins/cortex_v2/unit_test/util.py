import sys
import os.path
import json
import logging

sys.path.append(os.path.abspath('../'))
from icon_cortex_v2.connection import Connection
from icon_cortex_v2.connection.schema import Input


class Util:
    @staticmethod
    def default_connector(action):
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        action.connection = default_connection
        action.logger = logging.getLogger("action logger")
        return action

    @staticmethod
    def load_json(filename):
        with open((os.path.join(os.path.dirname(os.path.realpath(__file__)), filename))) as file:
            return json.loads(file.read())

    @staticmethod
    def mocked_request(*args, **kwargs):
        class MockResponse:
            def __init__(self, filename: str = None):
                self.filename = filename

            def json(self):
                return Util.load_json(f"responses/{self.filename}")

        if kwargs.get("method") == "DELETE" \
                and kwargs.get("url") == "http://host.docker.internal:9999/api/job/4izwIIEBz1WePCeJBqGk":
            return MockResponse("delete_job.resp.json")
