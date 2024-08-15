import os
import sys
import unittest
from unittest.mock import patch, MagicMock

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))
from komand_misp.actions.create_an_event.action import CreateAnEvent
from komand_misp.actions.create_an_event.schema import CreateAnEventInput, CreateAnEventOutput
from jsonschema import validate


class TestCreateAnEvent(unittest.TestCase):
    def setUp(self):
        self.action = CreateAnEvent()
        self.action.connection = MagicMock()
        self.action.logger = MagicMock()
        self.mock_client = MagicMock()
        self.action.connection.client = self.mock_client

        self.params = {
            "distribution": "This Organization",
            "threat_level_id": "1",
            "analysis": "0",
            "info": "Test event",
            "published": False,
            "orgc_id": "",
            "org_id": "",
            "sharing_group_id": "",
        }

    @patch("komand_misp.connection.connection.Connection")
    def test_create_an_event_success(self, mock_connection_class):
        mock_connection = MagicMock()
        mock_connection.client = self.mock_client
        mock_connection_class.return_value = mock_connection

        self.mock_client.add_event.return_value = {"Event": {"info": "Test event"}}
        validate(self.params, CreateAnEventInput.schema)
        result = self.action.run(self.params)
        self.assertEqual(result, {"info": "Test event"})
        validate(result, CreateAnEventOutput.schema)

    @patch("komand_misp.connection.connection.Connection")
    def test_create_an_event_failure(self, mock_connection_class):
        mock_connection = MagicMock()
        mock_connection.client = self.mock_client
        mock_connection_class.return_value = mock_connection

        self.mock_client.add_event.side_effect = Exception("Test exception")
        validate(self.params, CreateAnEventInput.schema)
        with self.assertRaises(PluginException):
            self.action.run(self.params)
        self.action.logger.error.assert_called()
