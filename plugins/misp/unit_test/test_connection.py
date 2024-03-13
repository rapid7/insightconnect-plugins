import os
import sys
import unittest
from unittest.mock import patch, MagicMock

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))
from komand_misp.connection.connection import Connection


class TestConnection(unittest.TestCase):
    def setUp(self):
        self.mock_pymisp = MagicMock()
        self.connection = Connection()
        self.connection.logger = MagicMock()
        self.params = {"url": "https://example.com", "automation_code": {"secretKey": "dummykey"}, "ssl": True}

    @patch("pymisp.PyMISP", return_value=MagicMock())
    def test_connect_success(self, mock_pymisp):
        self.connection.connect(self.params)
        self.connection.logger.info.assert_any_call("Connect: Connecting...")
        self.connection.logger.info.assert_any_call("Connect: Connected!")
        self.assertIsInstance(self.connection.client, MagicMock)

    @patch("pymisp.PyMISP", side_effect=Exception("Connection Failed"))
    def test_connect_failure(self, mock_pymisp):
        with self.assertRaises(Exception) as context:
            self.connection.connect(self.params)
        self.assertTrue(PluginException.causes[PluginException.Preset.UNAUTHORIZED] == context.exception.cause)
        self.connection.logger.info.assert_called_with("Connect: Connecting...")
        self.connection.logger.error.assert_called_with("Connect: Not Connected")
