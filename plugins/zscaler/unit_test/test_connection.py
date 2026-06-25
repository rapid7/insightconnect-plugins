import os
import sys

sys.path.append(os.path.abspath("../"))

import logging
from unittest import TestCase
from unittest.mock import Mock, patch

from icon_zscaler.connection import Connection
from insightconnect_plugin_runtime.exceptions import ConnectionTestException, PluginException
from util import Util, STUB_CONNECTION


class TestConnection(TestCase):
    @patch("requests.request", side_effect=Util.mock_request)
    def setUp(self, mock_connection: Mock) -> None:
        self.connection = Connection()
        self.connection.logger = logging.getLogger("connection logger")
        self.connection.connect(STUB_CONNECTION)
        # Bypass JWT signing by pre-setting mock tokens
        self.connection.zia_client._token = "mock-access-token-12345"
        self.connection.zia_client._token_expiry = 9999999999
        self.connection.zpa_client._token = "mock-access-token-12345"
        self.connection.zpa_client._token_expiry = 9999999999

    @patch("requests.request", side_effect=Util.mock_request)
    def test_connection_ok(self, _mock_get: Mock) -> None:
        response = self.connection.test()
        expected_response = {"success": True}
        self.assertEqual(response, expected_response)

    @patch("requests.request", side_effect=Util.mock_request)
    def test_connection_zia_failure(self, _mock_get: Mock) -> None:
        with self.assertRaises(ConnectionTestException) as error:
            self.connection.zia_client.test = Mock(
                side_effect=PluginException(
                    cause="Failed to obtain OAuth 2.0 access token.",
                    assistance="Verify that client_id, private_key, vanity_domain, and cloud are correct.",
                    data="Authentication failed",
                )
            )
            self.connection.test()
        self.assertEqual(error.exception.cause, "Failed to obtain OAuth 2.0 access token.")
        self.assertEqual(
            error.exception.assistance, "Verify that client_id, private_key, vanity_domain, and cloud are correct."
        )
        self.assertEqual(error.exception.data, "Authentication failed")

    @patch("requests.request", side_effect=Util.mock_request)
    def test_connection_zpa_failure(self, _mock_get: Mock) -> None:
        with self.assertRaises(ConnectionTestException) as error:
            self.connection.zpa_client.test = Mock(
                side_effect=PluginException(
                    cause="Failed to obtain OAuth 2.0 access token.",
                    assistance="Verify that client_id, private_key, vanity_domain, and cloud are correct.",
                    data="ZPA authentication failed",
                )
            )
            self.connection.test()
        self.assertEqual(error.exception.cause, "Failed to obtain OAuth 2.0 access token.")
        self.assertEqual(
            error.exception.assistance, "Verify that client_id, private_key, vanity_domain, and cloud are correct."
        )
        self.assertEqual(error.exception.data, "ZPA authentication failed")
