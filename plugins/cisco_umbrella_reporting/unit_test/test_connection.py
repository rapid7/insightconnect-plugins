import os
import sys

sys.path.append(os.path.abspath("../"))

import logging
from unittest import TestCase, mock
from unittest.mock import Mock

from icon_cisco_umbrella_reporting.connection.connection import Connection
from insightconnect_plugin_runtime.clients.oauth import OAuth20ClientMessages
from insightconnect_plugin_runtime.exceptions import ConnectionTestException
from parameterized import parameterized

from unit_test.mock import STUB_CONNECTION, mock_request_200, mock_request_400, mocked_request


class TestConnection(TestCase):
    @mock.patch("requests.Session.request", side_effect=mock_request_200)
    def setUp(self, mock_post: Mock) -> None:
        self.connection = Connection()
        self.connection.logger = logging.getLogger("connection logger")
        self.connection.connect(STUB_CONNECTION)

    @mock.patch("requests.Session.request", side_effect=mock_request_200)
    def test_connection_ok(self, mock_get: Mock) -> None:
        response = self.connection.test()
        expected_response = {"success": True}
        self.assertEqual(expected_response, response)

    @parameterized.expand(
        [
            (
                mock_request_400,
                OAuth20ClientMessages.PLUGIN_EXCEPTION_CAUSE,
                OAuth20ClientMessages.PLUGIN_EXCEPTION_ASSISTANCE,
            ),
        ],
    )
    def test_connection_exceptions(self, mock_request: Mock, cause: str, assistance: str) -> None:
        mocked_request(mock_request)
        with self.assertRaises(ConnectionTestException) as context:
            self.connection.test()
        self.assertEqual(context.exception.cause, cause)
        self.assertEqual(context.exception.assistance, assistance)
