import os
import sys
import unittest
from unittest.mock import patch, MagicMock

sys.path.append(os.path.abspath("../"))
from komand_misp.actions.add_urls.action import AddUrls


class TestAddUrls(unittest.TestCase):
    def setUp(self):
        self.action = AddUrls()
        self.action.connection = MagicMock()
        self.action.logger = MagicMock()
        self.mock_client = MagicMock()
        self.action.connection.client = self.mock_client

        self.params = {
            "event": "event_id",
            "urls": ["http://example.com", "https://example.com"],
            "comment": "Test comment",
            "distribution": "This Organization",
            "proposal": False,
        }

    @patch("komand_misp.connection.connection.Connection")
    def test_add_urls_success(self, mock_connection_class):
        mock_connection = MagicMock()
        mock_connection.client = self.mock_client
        mock_connection_class.return_value = mock_connection

        self.mock_client.get_event.return_value = {"Event": {"uuid": "test_uuid"}}
        result = self.action.run(self.params)
        self.assertEqual(result, {"status": True})

    @patch("komand_misp.connection.connection.Connection")
    def test_add_urls_failure(self, mock_connection_class):
        mock_connection = MagicMock()
        mock_connection.client = self.mock_client
        mock_connection_class.return_value = mock_connection

        self.mock_client.get_event.return_value = {"Event": {"uuid": "test_uuid"}}
        self.mock_client.add_url.side_effect = Exception("Test exception")
        result = self.action.run(self.params)
        self.assertEqual(result, {"status": False})
        self.action.logger.error.assert_called()
