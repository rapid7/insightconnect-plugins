import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock, patch
import json
import logging
from icon_trendmicro_visionone.connection.connection import Connection
from icon_trendmicro_visionone.actions.quarantine_email_message import (
    QuarantineEmailMessage,
)


class TestQuarantineEmailMessage(TestCase):
    def setUp(self):
        self.connection = Connection()
        self.connection.logger = logging.getLogger()
        self.connection.server = "tmv1-mock.trendmicro.com"
        self.connection.token_ = "Dummy-Secret-Token"
        self.connection.app = "TM-R7"

        self.action = QuarantineEmailMessage()
        self.action.connection = self.connection

    def test_integration_quarantine_email_message(self):
        log = logging.getLogger("Test")
        test_conn = Connection()
        test_action = QuarantineEmailMessage()

        test_conn.logger = log
        test_action.logger = log

        try:
            with open("/python/src/tests/quarantine_email_message.json") as file:
                test_json = json.loads(file.read()).get("body")
                connection_params = test_json.get("connection")
                action_params = test_json.get("input")
        except Exception as e:
            message = f"Error reading JSON file: {e}"
            self.fail(message)

        test_conn.connect(connection_params)
        test_action.connection = test_conn
        results = test_action.run(action_params)
        expected_output = {"multi_response": [{"status": 202, "task_id": "00000002"}]}

        self.assertEqual(results, expected_output)

    @patch("pytmv1.client")
    def test_quarantine_email_message_success(self, mock_pytmv1_client):
        response_items = [
            {
                "status": 202,
                "task_id": "00000002",
            }
        ]

        mock_client_instance = MagicMock()
        mock_client_instance.quarantine_email_message.return_value = MagicMock(
            result_code="Success",
            response=MagicMock(dict=lambda: {"items": response_items}),
            errors=None,
        )
        mock_pytmv1_client.return_value = mock_client_instance

        params = {
            "email_identifiers": [
                {
                    "description": "quarantine email message r7",
                    "mailbox": "jdoe@testemailtest.com",
                    "message_id": "AAkALgAAAAAAHYQDEapmEc2byACqAC-EWg0AAhCCNvg5sEua0nNjgfLS2AABNpgTSQAA",
                }
            ]
        }

        expected_output = {"multi_response": response_items}

        response = self.action.run(params)
        self.assertEqual(response, expected_output)

    @patch("pytmv1.client")
    def test_quarantine_email_message_failure(self, mock_pytmv1_client):
        mock_client_instance = MagicMock()
        mock_client_instance.quarantine_email_message.side_effect = Exception(
            "API request failed"
        )
        mock_pytmv1_client.return_value = mock_client_instance

        params = {
            "email_identifiers": [
                {
                    "description": "quarantine email message r7",
                    "mailbox": "jdoe@testemailtest.com",
                    "message_id": "AAkALgAAAAAAHYQDEapmEc2byACqAC-EWg0AAhCCNvg5sEua0nNjgfLS2AABNpgTSQAA",
                }
            ]
        }

        with self.assertRaises(Exception) as context:
            self.action.run(params)

        self.assertTrue("API request failed" in str(context.exception))
