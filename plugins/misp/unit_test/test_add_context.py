import os
import sys
import unittest
from unittest.mock import patch, MagicMock

sys.path.append(os.path.abspath("../"))
from komand_misp.actions.add_context.action import AddContext


class TestAddContext(unittest.TestCase):
    def setUp(self):
        self.action = AddContext()
        self.action.connection = MagicMock()
        self.action.logger = MagicMock()
        self.mock_client = MagicMock()
        self.action.connection.client = self.mock_client

        self.params = {
            "comment": {
                "event": "1",
                "comment_in": "Some internal comment",
                "comment": "This is a test comment",
                "distribution": "This Organization",
            },
            "link": {
                "event": "2",
                "link": "http://example.com",
                "comment": "This is a test link",
                "distribution": "This Community",
            },
            "other": {
                "event": "3",
                "other": "Other info",
                "comment": "This is a test other",
                "distribution": "Connected Communities",
            },
            "text": {
                "event": "4",
                "text": "Text info",
                "comment": "This is a test text",
                "distribution": "All Communities",
            },
            "proposal": False,
        }

    @patch("komand_misp.connection.connection.Connection")
    def test_add_context_success(self, mock_connection):
        mock_connection.client = self.mock_client
        self.mock_client.get_event.return_value = {"event": "mock_event"}
        result = self.action.run(self.params)
        self.assertEqual(result, {"status": True})

    @patch("komand_misp.connection.connection.Connection")
    def test_add_context_failure(self, mock_connection):
        mock_connection.client = self.mock_client
        self.mock_client.get_event.side_effect = Exception("Test exception")
        result = self.action.run(self.params)
        self.assertEqual(result, {"status": False})
        self.action.logger.error.assert_called()
