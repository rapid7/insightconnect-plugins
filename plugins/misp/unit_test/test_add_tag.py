import os
import sys
import unittest
from unittest.mock import patch, MagicMock

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))
from komand_misp.actions.add_tag.action import AddTag
from komand_misp.actions.add_tag.schema import AddTagInput, AddTagOutput
from jsonschema import validate


class TestAddTag(unittest.TestCase):
    def setUp(self):
        self.action = AddTag()
        self.action.connection = MagicMock()
        self.action.logger = MagicMock()
        self.mock_client = MagicMock()
        self.action.connection.client = self.mock_client

        self.params = {"event": "event_id", "tag": "Test Tag"}

    @patch("komand_misp.connection.connection.Connection")
    def test_add_tag_success(self, mock_connection_class):
        mock_connection = MagicMock()
        mock_connection.client = self.mock_client
        mock_connection_class.return_value = mock_connection

        self.mock_client.get_event.return_value = {"Event": {"uuid": "test_uuid"}}
        self.mock_client.tag.return_value = {"name": "tag successfully added"}
        validate(self.params, AddTagInput.schema)
        result = self.action.run(self.params)
        self.assertEqual(result, {"status": True})
        validate(result, AddTagOutput.schema)

    @patch("komand_misp.connection.connection.Connection")
    def test_add_tag_failure(self, mock_connection_class):
        mock_connection = MagicMock()
        mock_connection.client = self.mock_client
        mock_connection_class.return_value = mock_connection

        self.mock_client.get_event.return_value = {"Event": {"uuid": "test_uuid"}}
        self.mock_client.tag.return_value = {"name": "failed to add tag"}
        validate(self.params, AddTagInput.schema)
        with self.assertRaises(PluginException):
            self.action.run(self.params)
        self.action.logger.error.assert_called()

    @patch("komand_misp.connection.connection.Connection")
    def test_add_tag_exception(self, mock_connection_class):
        mock_connection = MagicMock()
        mock_connection.client = self.mock_client
        mock_connection_class.return_value = mock_connection

        self.mock_client.get_event.return_value = {"Event": {"uuid": "test_uuid"}}
        self.mock_client.tag.side_effect = Exception("Test exception")
        validate(self.params, AddTagInput.schema)
        with self.assertRaises(PluginException):
            self.action.run(self.params)
        self.action.logger.error.assert_called()
