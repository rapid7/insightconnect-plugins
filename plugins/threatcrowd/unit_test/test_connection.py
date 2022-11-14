import os
import sys

sys.path.append(os.path.abspath("../"))
import logging
from typing import Callable
from unittest import TestCase

from icon_threatcrowd.connection.connection import Connection
from insightconnect_plugin_runtime.exceptions import ConnectionTestException
from parameterized import parameterized

from unit_test.mock import (
    STUB_CONNECTION,
    mock_request_200,
    mock_request_401,
    mock_request_404,
    mock_request_500,
    mock_request_503,
    mocked_request,
)


class TestConnection(TestCase):
    def setUp(self) -> None:
        self.connection = Connection()
        self.connection.logger = logging.getLogger("connection logger")
        self.connection.connect(STUB_CONNECTION)

    def test_connection_ok(self):
        mocked_request(mock_request_200)
        response = self.connection.test()
        expected_response = {"success": True}
        self.assertEqual(response, expected_response)

    @parameterized.expand(
        [(mock_request_401,), (mock_request_404,), (mock_request_500,), (mock_request_503,)],
    )
    def test_connection_exception(self, mock_request: Callable) -> None:
        mocked_request(mock_request)
        with self.assertRaises(ConnectionTestException) as context:
            self.connection.test()
        self.assertEqual(
            context.exception.cause,
            "An unexpected error occurred during the API request.",
        )
