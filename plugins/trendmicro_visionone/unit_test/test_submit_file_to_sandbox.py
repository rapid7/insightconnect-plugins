import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock, patch
import json
import logging
from icon_trendmicro_visionone.connection.connection import Connection
from icon_trendmicro_visionone.actions.submit_file_to_sandbox import SubmitFileToSandbox


class TestSubmitFileToSandbox(TestCase):
    def setUp(self):
        self.connection = Connection()
        self.connection.logger = logging.getLogger()
        self.connection.server = "tmv1-mock.trendmicro.com"
        self.connection.token_ = "Dummy-Secret-Token"
        self.connection.app = "TM-R7"

        self.action = SubmitFileToSandbox()
        self.action.connection = self.connection

    def test_integration_submit_file_to_sandbox(self):
        log = logging.getLogger("Test")
        test_conn = Connection()
        test_action = SubmitFileToSandbox()

        test_conn.logger = log
        test_action.logger = log

        try:
            with open("/python/src/tests/submit_file_to_sandbox.json") as file:
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
            "response": {"status": 200, "file_id": "12345", "sandbox_id": "67890"}
        }

        self.assertIn("id", results)

    @patch("pytmv1.client")
    def test_submit_file_to_sandbox_success(self, mock_pytmv1_client):
        mock_client_instance = MagicMock()
        mock_client_instance.submit_file_to_sandbox.side_effect = [
            MagicMock(
                result_code="Success",
                response=MagicMock(
                    dict=MagicMock(
                        return_value={
                            "status": 200,
                            "file_id": "12345",
                            "sandbox_id": "67890",
                        }
                    )
                ),
            ),
        ]

        mock_pytmv1_client.return_value = mock_client_instance

        params = {
            "archive_password": "",
            "arguments": "",
            "document_password": "",
            "file": {"content": "dGVzdA==", "filename": "r7-test11.bat"},
        }

        expected_output = {
            "status": 200,
            "file_id": "12345",
            "sandbox_id": "67890",
        }

        response = self.action.run(params)
        self.assertEqual(response, expected_output)

    @patch("pytmv1.client")
    def test_submit_file_to_sandbox_failure(self, mock_pytmv1_client):
        mock_client_instance = MagicMock()
        mock_client_instance.submit_file_to_sandbox.side_effect = Exception(
            "API request failed"
        )
        mock_pytmv1_client.return_value = mock_client_instance

        params = {
            "archive_password": "",
            "arguments": "",
            "document_password": "",
            "file": {"content": "dGVzdA==", "filename": "r7-test11.bat"},
        }

        with self.assertRaises(Exception) as context:
            self.action.run(params)

        self.assertTrue("API request failed" in str(context.exception))
