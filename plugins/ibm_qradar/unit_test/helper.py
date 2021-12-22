"""Helper file for unit test cases."""
import json

import requests

from icon_ibm_qradar.connection.connection import Connection
import logging

from icon_ibm_qradar.util.constants.constant import SUCCESS_RESPONSE_CODE


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
        default_connection.logger = logging.getLogger("connection logger")
        if connect_params:
            params = connect_params
        else:
            params = {
                "hostname": "hostname",
                "username": "username",
                "password": "password",
            }
        default_connection.connect(params)
        action.connection = default_connection
        action.logger = logging.getLogger("action logger")
        return action

    @staticmethod
    def mock_request(*args, **kwargs):
        """To mock the requests.request method for unit test."""
        if kwargs.get("auth")[0] == "wrong":
            return MockResponse(401, data={})
        if kwargs.get("auth")[1] == "wrong":
            return MockResponse(401, data={})

        if kwargs.get("url") == "https://hostname/api/ariel/searches?query_expression=Select * from events":
            return MockResponse(SUCCESS_RESPONSE_CODE[1], data={"cursor_id": "test_cursor_id"})

        if kwargs.get("url") == "https://wrong/api/ariel/searches?query_expression=Select * from events":
            raise requests.exceptions.ConnectionError()

        if kwargs.get("url") == "https://hostname/api/ariel/searches?query_expression=wrong":
            return MockResponse(422, data={"description": "wrong aql"})

        if kwargs.get("url") == "https://hostname/api/ariel/searches/search_id":
            return MockResponse(SUCCESS_RESPONSE_CODE[0], data={"cursor_id": "test_cursor_id"})

        if kwargs.get("url") == "https://hostname/api/ariel/searches/internalServerError":
            return MockResponse(500, {})

        if kwargs.get("url") == "https://wrong/api/ariel/searches/search_id":
            raise requests.exceptions.ConnectionError()

        if kwargs.get("url") == "https://hostname/api/ariel/searches/wrong":
            return MockResponse(404, data={"description": "Search Id Does not exist"})

        raise NotImplementedError("Not implemented", kwargs)
