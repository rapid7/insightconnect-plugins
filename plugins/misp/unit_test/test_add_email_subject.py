import os
import sys
import unittest
from unittest.mock import patch, MagicMock

sys.path.append(os.path.abspath("../"))
from komand_misp.actions.add_email_subject.action import AddEmailSubject


class TestAddEmailSubject(unittest.TestCase):
    def setUp(self):
        self.action = AddEmailSubject()
        self.action.connection = MagicMock()
        self.action.logger = MagicMock()
        self.mock_client = MagicMock()
        self.action.connection.client = self.mock_client

        self.params = {
            "event": "event_id",
            "subject": "Test Subject",
            "comment": "Test comment",
            "distribution": "This Organization",
            "proposal": False,
        }

    @patch("komand_misp.connection.connection.Connection")
    def test_add_email_subject_success(self, mock_connection):
        mock_connection.client = self.mock_client
        self.mock_client.get_event.return_value = {"event": "test_event"}
        result = self.action.run(self.params)
        self.assertEqual(result, {"status": True})

    @patch("komand_misp.connection.connection.Connection")
    def test_add_email_subject_failure(self, mock_connection):
        mock_connection.client = self.mock_client
        self.mock_client.get_event.side_effect = Exception("Test exception")
        result = self.action.run(self.params)
        self.assertEqual(result, {"status": False})
        self.action.logger.error.assert_called()
