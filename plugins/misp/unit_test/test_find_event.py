import os
import sys
import unittest
from unittest.mock import patch, MagicMock

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))
from komand_misp.actions.find_event.action import FindEvent
from komand_misp.actions.find_event.schema import FindEventInput, FindEventOutput
from jsonschema import validate


class TestFindEvent(unittest.TestCase):
    def setUp(self):
        self.action = FindEvent()
        self.action.connection = MagicMock()
        self.action.logger = MagicMock()
        self.mock_client = MagicMock()
        self.action.connection.client = self.mock_client

        self.params = {"event_id": "1"}

    @patch("komand_misp.connection.connection.Connection")
    def test_find_event_success(self, mock_connection):
        mock_event = {"Event": {"id": "1", "info": "Test Event"}}
        mock_connection.client = self.mock_client
        self.mock_client.get_event.return_value = mock_event

        validate(self.params, FindEventInput.schema)
        result = self.action.run(self.params)
        self.assertEqual(result, {"event": mock_event["Event"], "message": "Event found.", "errors": ["No errors."]})
        validate(result, FindEventOutput.schema)

    @patch("komand_misp.connection.connection.Connection")
    def test_find_event_not_found(self, mock_connection):
        mock_response = None
        mock_connection.client = self.mock_client
        self.mock_client.get_event.return_value = mock_response

        validate(self.params, FindEventInput.schema)
        with self.assertRaises(PluginException) as context:
            self.action.run(self.params)
        self.assertTrue(PluginException.causes[PluginException.Preset.NOT_FOUND] == context.exception.cause)

    @patch("komand_misp.connection.connection.Connection")
    def test_find_event_error(self, mock_connection):
        mock_connection.client = self.mock_client
        self.mock_client.get_event.side_effect = Exception("Test exception")

        validate(self.params, FindEventInput.schema)
        with self.assertRaises(PluginException) as context:
            self.action.run(self.params)
        self.assertTrue(PluginException.causes[PluginException.Preset.NOT_FOUND] == context.exception.cause)
