import logging
from icon_cortex_v2.connection import Connection
from icon_cortex_v2.connection.schema import Input


class Util:
    @staticmethod
    def default_connector(action):
        default_connection = Connection()
        default_connection.logger = logging.getLogger("connection logger")
        params = {
            Input.API_KEY: {"secretKey": ""},
            Input.PROTOCOL: "HTTP",
            Input.HOST: "0.0.0.0",
            Input.PORT: 9999,
            Input.VERIFY: False,
        }
        default_connection.connect(params)
        action.connection = default_connection
        action.logger = logging.getLogger("action logger")
        return action

    # (self, method: str, path: str, params, **kwargs)
    @staticmethod
    def mocked_request(*args, **kwargs):
        class MockResponse:
            def __init__(self, status_code=None):
                self.status_code = status_code

        if args[1] == "one test case action full URL":
            return MockResponse(status_code=200)
        elif args[1] == "another test case but 404":
            return MockResponse(status_code=404)
        else:
            raise Exception("Not implemented")
