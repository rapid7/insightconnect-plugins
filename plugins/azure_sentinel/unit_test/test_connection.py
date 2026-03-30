import os
import sys
from unittest import TestCase, mock
from unittest.mock import Mock

sys.path.append(os.path.abspath("../"))
import logging

from icon_azure_sentinel.connection.connection import Connection
from icon_azure_sentinel.connection.schema import Input
from insightconnect_plugin_runtime.exceptions import ConnectionTestException

from mock_util import mock_request_200, mock_request_500


class TestConnection(TestCase):
    def setUp(self) -> None:
        self.connection = Connection()
        self.connection.logger = logging.getLogger("connection logger")

    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_connection_ok(self, mock_get: Mock) -> None:
        self.connection.connect(
            {
                Input.CLIENT_ID: "123456",
                Input.CLIENT_SECRET: {"privateKey": "123456"},
                Input.TENANT_ID: "123456",
            }
        )
        response = self.connection.test()
        expected_response = {"success": True}
        self.assertEqual(response, expected_response)

    @mock.patch("requests.request", side_effect=mock_request_500)
    def test_connection_exception(self, exception: Mock) -> None:
        with self.assertRaises(ConnectionTestException) as context:
            self.connection.connect(
                {
                    Input.CLIENT_ID: "123456",
                    Input.CLIENT_SECRET: {"privateKey": "123456"},
                    Input.TENANT_ID: "123456",
                }
            )
            self.assertEqual(
                context.exception.cause,
                "Unable to authorize against Microsoft graph API.",
            )

    def test_test_raises(self) -> None:
        with self.assertRaises(ConnectionTestException) as context:
            self.connection.test()
            self.assertEqual(
                context.exception.cause,
                "Unable to authorize against Microsoft graph API.",
            )
