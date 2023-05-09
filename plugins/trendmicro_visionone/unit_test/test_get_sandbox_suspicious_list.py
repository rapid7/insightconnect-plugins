import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock, patch
import json
import logging
from icon_trendmicro_visionone.connection.connection import Connection
from icon_trendmicro_visionone.actions.get_sandbox_suspicious_list import (
    GetSandboxSuspiciousList,
)


class TestGetSandboxSuspiciousList(TestCase):
    def setUp(self):
        self.connection = Connection()
        self.connection.logger = logging.getLogger()
        self.connection.server = "tmv1-mock.trendmicro.com"
        self.connection.token_ = "Dummy-Secret-Token"
        self.connection.app = "TM-R7"

        self.action = GetSandboxSuspiciousList()
        self.action.connection = self.connection

    def test_integration_get_sandbox_suspicious_list(self):
        log = logging.getLogger("Test")
        test_conn = Connection()
        test_action = GetSandboxSuspiciousList()

        test_conn.logger = log
        test_action.logger = log

        try:
            with open("/python/src/tests/get_sandbox_suspicious_list.json") as file:
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
            "sandbox_suspicious_list_resp": [
                {"id": "1", "status": "completed", "score": 80}
            ]
        }

        self.assertIn("sandbox_suspicious_list_resp", results)

    @patch("pytmv1.client")
    def test_get_sandbox_suspicious_list_success(self, mock_pytmv1_client):
        mock_client_instance = MagicMock()
        mock_client_instance.get_sandbox_suspicious_list.return_value = MagicMock(
            result_code="SUCCESS",
            response=MagicMock(
                dict=lambda: {
                    "items": [{"id": "1", "status": "completed", "score": 80}]
                }
            ),
        )
        mock_pytmv1_client.return_value = mock_client_instance

        params = {
            "id": "7a7402b1-bca8-4fbf-a73c-8f981d3c778f",
            "poll": True,
            "poll_time_sec": 5.0,
        }

        expected_output = {
            "sandbox_suspicious_list_resp": [
                {"id": "1", "status": "completed", "score": 80}
            ]
        }

        response = self.action.run(params)
        self.assertEqual(response, expected_output)

    @patch("pytmv1.client")
    def test_get_sandbox_suspicious_list_failure(self, mock_pytmv1_client):
        mock_client_instance = MagicMock()
        mock_client_instance.get_sandbox_suspicious_list.return_value = MagicMock(
            result_code="ERROR", error="API request failed"
        )
        mock_pytmv1_client.return_value = mock_client_instance

        params = {
            "id": "7a7402b1-bca8-4fbf-a73c-8f981d3c778f",
            "poll": True,
            "poll_time_sec": 5.0,
        }

        expected_output = "API request failed"

        response = self.action.run(params)
        self.assertEqual(response, expected_output)
