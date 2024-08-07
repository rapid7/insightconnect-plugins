import os
import sys
import unittest
from unittest.mock import patch, MagicMock

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))
from komand_misp.actions.remove_tag.action import RemoveTag
from komand_misp.actions.remove_tag.schema import RemoveTagInput, RemoveTagOutput
from jsonschema import validate


class TestRemoveTag(unittest.TestCase):
    def setUp(self):
        self.action = RemoveTag()
        self.action.connection = MagicMock()
        self.action.logger = MagicMock()
        self.mock_client = MagicMock()
        self.action.connection.client = self.mock_client

        self.params = {"event": "1", "tag": "test-tag"}

    @patch("komand_misp.connection.connection.Connection")
    def test_remove_tag_success(self, mock_connection):
        mock_response = {"name": "tag successfully removed"}
        mock_connection.client = self.mock_client
        self.mock_client.get_event.return_value = {"Event": {"uuid": "test-uuid"}}
        self.mock_client.untag.return_value = mock_response

        validate(self.params, RemoveTagInput.schema)
        result = self.action.run(self.params)
        self.assertEqual(result, {"status": True})
        validate(result, RemoveTagOutput.schema)

    @patch("komand_misp.connection.connection.Connection")
    def test_remove_tag_failure(self, mock_connection):
        mock_connection.client = self.mock_client
        self.mock_client.get_event.return_value = {"Event": {"uuid": "test-uuid"}}
        self.mock_client.untag.return_value = {"name": "Failed to remove tag"}

        validate(self.params, RemoveTagInput.schema)
        result = self.action.run(self.params)
        self.assertEqual(result, {"status": False})
        validate(result, RemoveTagOutput.schema)

    @patch("komand_misp.connection.connection.Connection")
    def test_event_not_found(self, mock_connection):
        mock_connection.client = self.mock_client
        self.mock_client.get_event.side_effect = PluginException(preset=PluginException.Preset.NOT_FOUND)

        validate(self.params, RemoveTagInput.schema)
        with self.assertRaises(PluginException) as context:
            self.action.run(self.params)
        self.assertEqual(context.exception.preset, PluginException.Preset.NOT_FOUND)
