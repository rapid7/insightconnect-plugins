import os
import sys

sys.path.append(os.path.abspath("../"))
import logging
from unittest import TestCase, mock

from insightconnect_plugin_runtime.exceptions import ConnectionTestException

from icon_armorblox.connection.connection import Connection
from icon_armorblox.connection.schema import Input


class TestConnection(TestCase):
    def setUp(self) -> None:
        self.connection = Connection()
        self.connection.logger = logging.getLogger("connection logger")

    def test_connection_ok(self):
        self.connection.connect(
            {
                Input.API_KEY: "9de5069c5afe602b2ea0a04b66beb2c0",
                Input.TENANT_NAME: "outbound-integrations",
            }
        )
        response = self.connection.test()
        expected_response = []
        self.assertEqual(response, expected_response)
