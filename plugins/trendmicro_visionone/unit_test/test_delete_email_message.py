import sys
import os
import json
import logging

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock, patch

from icon_trendmicro_visionone.connection.connection import Connection
from icon_trendmicro_visionone.actions.delete_email_message import DeleteEmailMessage
import pytmv1


class TestDeleteEmailMessage(TestCase):
    def setUp(self):
        self.connection = Connection()
        self.connection.logger = logging.getLogger()
        self.connection.server = "tmv1-mock.trendmicro.com"
        self.connection.token_ = "Dummy-Secret-Token"
        self.connection.app = "TM-R7"

        self.action = DeleteEmailMessage()
        self.action.connection = self.connection

    def test_integration_delete_email_message(self):
        log = logging.getLogger("Test")
        test_conn = Connection()
        test_action = DeleteEmailMessage()

        test_conn.logger = log
        test_action.logger = log

        try:
            with open("/python/src/tests/delete_email_message.json") as file:
                test_json = json.loads(file.read()).get("body")
                connection_params = test_json.get("connection")
                action_params = test_json.get("input")
                email_identifiers = [
                    {
                        "message_id": action_params.get("message_id"),
                        "mailbox": action_params.get("mailbox"),
                        "description": action_params.get("description"),
                    }
                ]
        except Exception as e:
            message = f"Error reading JSON file: {e}"
            self.fail(message)

        test_conn.connect(connection_params)
        test_action.connection = test_conn
        results = test_action.run({"email_identifiers": email_identifiers})
        expected_output = {
            "multi_response": [
                {"status": 202, "task_id": "00000001"},
            ],
        }

        self.assertEqual(results, expected_output)

    @patch("pytmv1.client")
    def test_delete_email_message_success(self, mock_pytmv1_client):
        mock_client_instance = MagicMock()
        mock_client_instance.delete_email_message.side_effect = [
            MagicMock(
                result_code="Success",
                response=MagicMock(
                    dict=MagicMock(
                        return_value={
                            "items": [
                                {
                                    "task_id": "00000007",
                                }
                            ]
                        }
                    )
                ),
            )
        ]
        mock_pytmv1_client.return_value = mock_client_instance

        params = {
            "email_identifiers": [
                {
                    "message_id": "234523",
                    "mailbox": "test@email.com",
                    "description": "TEST delete email msg",
                },
            ],
        }

        expected_output = {
            "multi_response": [
                {
                    "task_id": "00000007",
                },
            ],
        }

        response = self.action.run(params)
        self.assertEqual(response, expected_output)

    @patch("pytmv1.client")
    def test_delete_email_message_failure(self, mock_pytmv1_client):
        mock_client_instance = MagicMock()
        mock_client_instance.delete_email_message.side_effect = [
            MagicMock(
                result_code="Error",
                errors={"error_message": "API Error", "error_code": 400},
            )
        ]
        mock_pytmv1_client.return_value = mock_client_instance

        params = {
            "email_identifiers": [
                {
                    "message_id": "234523",
                    "mailbox": "test@email.com",
                    "description": "TEST delete email msg",
                },
            ],
        }

        expected_output = {"error_message": "API Error", "error_code": 400}

        response = self.action.run(params)
        self.assertEqual(response, expected_output)
