import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock, patch
import json
import logging
from icon_trendmicro_visionone.connection.connection import Connection
from icon_trendmicro_visionone.actions.add_alert_note import AddAlertNote


class TestAddAlertNote(TestCase):
    def setUp(self):
        self.connection = Connection()
        self.connection.logger = logging.getLogger()
        self.connection.server = "tmv1-mock.trendmicro.com"
        self.connection.token_ = "Dummy-Secret-Token"
        self.connection.app = "TM-R7"

        self.action = AddAlertNote()
        self.action.connection = self.connection

    def test_integration_add_alert_note(self):
        log = logging.getLogger("Test")
        test_conn = Connection()
        test_action = AddAlertNote()

        test_conn.logger = log
        test_action.logger = log

        try:
            with open("/python/src/tests/add_alert_note.json") as file:
                test_json = json.loads(file.read()).get("body")
                connection_params = test_json.get("connection")
                action_params = test_json.get("input")
        except Exception as e:
            message = f"Error reading JSON file: {e}"
            self.fail(message)

        test_conn.connect(connection_params)
        test_action.connection = test_conn
        results = test_action.run(action_params)
        expected_output = {
            "result_code": "SUCCESS",
            "location": "http://tmv1-mock.trendmicro.com/v3/workbench/alerts/2345245/notes/1",
            "note_id": "1",
        }

        self.assertEqual(
            results,
            expected_output,
        )

    @patch("pytmv1.client")
    def test_add_alert_note_success(self, mock_pytmv1_client):
        mock_client_instance = MagicMock()
        mock_client_instance.add_alert_note.return_value = MagicMock(
            result_code="Success",
            response=MagicMock(location="https://example.com/alerts/12345/notes/67890"),
        )
        mock_pytmv1_client.return_value = mock_client_instance

        params = {
            "alert_id": "12345",
            "content": "Test note content",
        }

        expected_output = {
            "result_code": "Success",
            "location": "https://example.com/alerts/12345/notes/67890",
            "note_id": "67890",
        }

        response = self.action.run(params)
        self.assertEqual(response, expected_output)

    @patch("pytmv1.client")
    def test_add_alert_note_failure(self, mock_pytmv1_client):
        mock_client_instance = MagicMock()
        mock_client_instance.add_alert_note.return_value = MagicMock(
            result_code="Error",
            error="Failed to add note",
        )
        mock_pytmv1_client.return_value = mock_client_instance

        params = {
            "alert_id": "12345",
            "content": "Test note content",
        }

        expected_output = "Failed to add note"

        response = self.action.run(params)
        self.assertEqual(response, expected_output)
