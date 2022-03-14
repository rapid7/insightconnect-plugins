import logging
from icon_cortex_v2.connection import Connection


class MockClient:
    def __init__(self):
        self.service = "test"

    def execute(self):
        pass


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
