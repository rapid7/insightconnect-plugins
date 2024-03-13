import os
import sys
import unittest
from unittest.mock import patch, MagicMock

sys.path.append(os.path.abspath("../"))
from komand_misp.actions.add_attachment.action import AddAttachment


class TestAddAttachment(unittest.TestCase):
    def setUp(self):
        self.action = AddAttachment()

        self.action.connection = MagicMock()
        self.action.logger = MagicMock()
        self.mock_client = MagicMock()
        self.action.connection.client = self.mock_client

        self.params = {"attachment": "c29tZV9iYXNlNjRfZW5jb2RlZF9kYXRh", "filename": "example.txt", "event": "event_id"}

    @patch("tempfile.mkdtemp", return_value="/tmp/mockdir")
    @patch("builtins.open", new_callable=MagicMock)
    @patch("shutil.rmtree")
    def test_add_attachment(self, mock_rmtree, mock_open, mock_mkdtemp):
        self.mock_client.get_event.return_value = "mock_event"
        self.mock_client.add_attachment.return_value = "mock_response"

        result = self.action.run(self.params)

        self.mock_client.get_event.assert_called_with("event_id")
        self.mock_client.add_attachment.assert_called_with(
            "mock_event", attachment="/tmp/mockdir/tmp.txt", filename="example.txt"
        )
        mock_open.assert_called_with("/tmp/mockdir/tmp.txt", "w", encoding="utf-8")
        self.assertEqual(result, {"status": True})
