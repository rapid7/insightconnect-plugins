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

    @patch("requests.request", side_effect=Util.mock_request)
    def test_connection_ok(self, _mock_get: Mock) -> None:
        response = self.connection.test()
        expected_response = {"success": True}
        self.assertEqual(response, expected_response)

    @patch("requests.request", side_effect=Util.mock_request)
    def test_connection_bad_json(self, _mock_get: Mock) -> None:
        with self.assertRaises(ConnectionTestException) as error:
            mock_response = Mock()
            mock_response.json.side_effect = ValueError("Invalid JSON")
            self.connection.client.get_status = Mock(return_value=mock_response)
            self.connection.test()
        self.assertEqual(error.exception.cause, PluginException.causes[PluginException.Preset.INVALID_JSON])
        self.assertEqual(error.exception.assistance, PluginException.assistances[PluginException.Preset.SERVER_ERROR])
        self.assertEqual(error.exception.data, "Invalid JSON response from Zscaler API")

    @patch("requests.request", side_effect=Util.mock_request)
    def test_connection_missing_status_field(self, _mock_get: Mock) -> None:
        with self.assertRaises(ConnectionTestException) as error:
            mock_response = Mock()
            mock_response.json.return_value = {}
            self.connection.client.get_status = Mock(return_value=mock_response)
            self.connection.test()
        self.assertEqual(error.exception.cause, PluginException.causes[PluginException.Preset.INVALID_JSON])
        self.assertEqual(error.exception.assistance, PluginException.assistances[PluginException.Preset.SERVER_ERROR])
        self.assertEqual(error.exception.data, "Missing 'status' field in Zscaler API response")
