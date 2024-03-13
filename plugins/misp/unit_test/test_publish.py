import os
import sys
import unittest
from unittest.mock import patch, MagicMock

from insightconnect_plugin_runtime.exceptions import PluginException

sys.path.append(os.path.abspath("../"))
from komand_misp.actions.publish.action import Publish


class TestPublish(unittest.TestCase):
    def setUp(self):
        self.action = Publish()
        self.action.connection = MagicMock()
        self.action.logger = MagicMock()
        self.mock_client = MagicMock()
        self.action.connection.client = self.mock_client

        self.params = {"event": "1"}

    @patch("komand_misp.connection.connection.Connection")
    def test_publish_success(self, mock_connection):
        mock_published = {"id": "1", "message": "Event published successfully"}
        mock_connection.client = self.mock_client
        self.mock_client.get_event.return_value = {"Event": {"id": "1"}}
        self.mock_client.publish.return_value = mock_published

        result = self.action.run(self.params)
        self.assertEqual(result, {"published": mock_published})

    @patch("komand_misp.connection.connection.Connection")
    def test_publish_failure(self, mock_connection):
        mock_connection.client = self.mock_client
        self.mock_client.get_event.return_value = {"Event": {"id": "1"}}
        self.mock_client.publish.return_value = {"errors": ["Error publishing event"]}

        with self.assertRaises(PluginException) as context:
            self.action.run(self.params)
        self.assertTrue(PluginException.causes[PluginException.Preset.BAD_REQUEST] == context.exception.cause)
