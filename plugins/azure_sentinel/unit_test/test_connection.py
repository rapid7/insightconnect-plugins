import os
import sys

sys.path.append(os.path.abspath("../"))
import logging
from unittest import TestCase, mock

from icon_azure_sentinel.connection.connection import Connection
from icon_azure_sentinel.connection.schema import Input
from insightconnect_plugin_runtime.exceptions import ConnectionTestException
from unit_test.mock import mock_request_200, mock_request_500


class TestConnection(TestCase):
    def setUp(self) -> None:
        self.connection = Connection()
        self.connection.logger = logging.getLogger("connection logger")

    @mock.patch("requests.request", side_effect=mock_request_200)
    def test_connection_ok(self, mock_get):
        self.connection.connect(
            {
                Input.API_VERSION: "2016-04-30-preview",
                Input.CLIENT_ID: "123456",
                Input.CLIENT_SECRET: {"privateKey": "123456"},
                Input.HOST: "https://management.azure.com",
                Input.TENANT_ID: "123456",
            }
        )
        response = self.connection.test()
        expected_response = None
        self.assertEqual(response, expected_response)

    @mock.patch("requests.request", side_effect=mock_request_500)
    def test_connection_exception(self, exception):
        with self.assertRaises(ConnectionTestException) as context:
            self.connection.connect(
                {
                    Input.API_VERSION: "2016-04-30-preview",
                    Input.CLIENT_ID: "123456",
                    Input.CLIENT_SECRET: {"privateKey": "123456"},
                    Input.HOST: "https://management.azure.com",
                    Input.TENANT_ID: "123456",
                }
            )
            self.assertEqual(
                context.exception.cause,
                "Unable to authorize against Microsoft graph API.",
            )

    def test_test_raises(self):
        with self.assertRaises(ConnectionTestException) as context:
            self.connection.test()
            self.assertEqual(
                context.exception.cause,
                "Unable to authorize against Microsoft graph API.",
            )

    def test_get_headers(self):
        headers = self.connection.get_headers("1234")
        self.assertEqual(headers, {"Content-type": "application/json", "Authorization": "Bearer 1234"})
