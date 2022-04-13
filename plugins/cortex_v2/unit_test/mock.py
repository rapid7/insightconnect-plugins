import logging
from icon_cortex_v2.connection import Connection
from icon_cortex_v2.connection.schema import Input


class MockResponse:
    def __init__(self, status_code: int = 0, content=None):
        self.status_code = status_code
        self.content = content

    def json(self):
        return {"status_code": self.status_code, "content": self.content}


class Mock:
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

    @staticmethod
    def mocked_request(method: str, path: str, params={}):
        if method == "GET" and path == "status":
            return MockResponse(status_code=200, content='{"versions":{"Cortex":"1.1.4"},"config":{"authType":"none"}}')
        elif method == "GET" and path == "another test case but 404":
            return MockResponse(status_code=404)
        else:
            raise Exception("Not implemented")
