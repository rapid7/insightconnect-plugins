import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock, patch
import json
import logging
from icon_trendmicro_visionone.connection.connection import Connection
from icon_trendmicro_visionone.actions.get_sandbox_submission_status import (
    GetSandboxSubmissionStatus,
)


class TestGetSandboxSubmissionStatus(TestCase):
    def setUp(self):
        self.connection = Connection()
        self.connection.logger = logging.getLogger()
        self.connection.server = "tmv1-mock.trendmicro.com"
        self.connection.token_ = "Dummy-Secret-Token"
        self.connection.app = "TM-R7"

        self.action = GetSandboxSubmissionStatus()
        self.action.connection = self.connection

    def test_integration_get_sandbox_submission_status(self):
        log = logging.getLogger("Test")
        test_conn = Connection()
        test_action = GetSandboxSubmissionStatus()

        test_conn.logger = log
        test_action.logger = log

        try:
            with open("/python/src/tests/get_sandbox_submission_status.json") as file:
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
            "status": "SUCCESS",
            "task": {"id": "234234", "status": "completed"},
        }

        self.assertIn("id", results)

    @patch("pytmv1.client")
    def test_get_sandbox_submission_status_success(self, mock_pytmv1_client):
        mock_client_instance = MagicMock()
        mock_client_instance.get_sandbox_submission_status.return_value = MagicMock(
            result_code="SUCCESS",
            response=MagicMock(dict=lambda: {"status": "completed"}),
        )
        mock_pytmv1_client.return_value = mock_client_instance

        params = {"task_id": "234234"}

        expected_output = {"status": "completed"}

        response = self.action.run(params)
        self.assertEqual(response, expected_output)

    @patch("pytmv1.client")
    def test_get_sandbox_submission_status_failure(self, mock_pytmv1_client):
        mock_client_instance = MagicMock()
        mock_client_instance.get_sandbox_submission_status.return_value = MagicMock(
            result_code="ERROR", response=MagicMock(dict=lambda: {"status": "failed"})
        )
        mock_pytmv1_client.return_value = mock_client_instance

        params = {"task_id": "234234"}

        expected_output = {"status": "failed"}

        response = self.action.run(params)
        self.assertEqual(response.response.dict(), expected_output)
