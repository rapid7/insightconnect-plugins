import json

from icon_ibm_qradar.connection import Connection


class MockResponse:
    """Mock response class."""

    def __init__(self, status_code: int, data: dict):
        """
        Initialize mock response.

        :param status_code: http status code
        :param data: mock response data
        """
        self.status_code = status_code
        data["status_code"] = status_code
        self.text = json.dumps(data)

    def json(self):
        """To convert text to json."""
        return json.loads(self.text)


class Helper:
    """Helper class for the unit test cases."""

    @staticmethod
    def default_connector(action, connect_params: object = None):
        """Get the default connector for unit testing."""
        default_connection = Connection()
        if connect_params:
            params = connect_params
        else:
            params = {
                "host_url": "http://host_url",
                "credentials": {"username": "user1", "password": "password"},
                "verify_ssl": False,
            }
        default_connection.connect(params)
        action.connection = default_connection
        return action
