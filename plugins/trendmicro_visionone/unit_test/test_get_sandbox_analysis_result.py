import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock, patch
import json
import logging
from icon_trendmicro_visionone.connection.connection import Connection
from icon_trendmicro_visionone.actions.get_sandbox_analysis_result import (
    GetSandboxAnalysisResult,
)


class TestGetSandboxAnalysisResult(TestCase):
    def setUp(self):
        self.connection = Connection()
        self.connection.logger = logging.getLogger()
        self.connection.server = "tmv1-mock.trendmicro.com"
        self.connection.token_ = "Dummy-Secret-Token"
        self.connection.app = "TM-R7"

        self.action = GetSandboxAnalysisResult()
        self.action.connection = self.connection

    def test_integration_get_sandbox_analysis_result(self):
        log = logging.getLogger("Test")
        test_conn = Connection()
        test_action = GetSandboxAnalysisResult()

        test_conn.logger = log
        test_action.logger = log

        try:
            with open("/python/src/tests/get_sandbox_analysis_result.json") as file:
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
            "report": {"id": "234234", "status": "completed", "result": "clean"},
        }

        self.assertIn("risk_level", results)

    @patch("pytmv1.client")
    def test_get_sandbox_analysis_result_success(self, mock_pytmv1_client):
        mock_client_instance = MagicMock()
        mock_client_instance.get_sandbox_analysis_result.return_value = MagicMock(
            result_code="SUCCESS",
            response=MagicMock(dict=lambda: {"status": "completed", "result": "clean"}),
        )
        mock_pytmv1_client.return_value = mock_client_instance

        params = {"report_id": "234234", "poll": True, "poll_time_sec": 5.0}

        expected_output = {"status": "completed", "result": "clean"}

        response = self.action.run(params)
        self.assertEqual(response, expected_output)

    @patch("pytmv1.client")
    def test_get_sandbox_analysis_result_failure(self, mock_pytmv1_client):
        mock_client_instance = MagicMock()
        mock_client_instance.get_sandbox_analysis_result.return_value = MagicMock(
            result_code="ERROR",
            response=MagicMock(dict=lambda: {"status": "failed", "result": "error"}),
        )
        mock_pytmv1_client.return_value = mock_client_instance

        params = {"report_id": "234234", "poll": True, "poll_time_sec": 5.0}

        expected_output = {"status": "failed", "result": "error"}

        response = self.action.run(params)
        self.assertEqual(response.response.dict(), expected_output)
