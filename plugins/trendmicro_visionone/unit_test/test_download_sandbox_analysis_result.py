import sys
import os
import json
import logging
import base64

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock, patch

from icon_trendmicro_visionone.connection.connection import Connection
from icon_trendmicro_visionone.actions.download_sandbox_analysis_result import (
    DownloadSandboxAnalysisResult,
)


class TestDownloadSandboxAnalysisResult(TestCase):
    def setUp(self):
        self.connection = Connection()
        self.connection.logger = logging.getLogger()
        self.connection.server = "tmv1-mock.trendmicro.com"
        self.connection.token_ = "Dummy-Secret-Token"
        self.connection.app = "TM-R7"

        self.action = DownloadSandboxAnalysisResult()
        self.action.connection = self.connection

    def test_integration_download_sandbox_analysis_result(self):
        log = logging.getLogger("Test")
        test_conn = Connection()
        test_action = DownloadSandboxAnalysisResult()

        test_conn.logger = log
        test_action.logger = log

        try:
            with open(
                "/python/src/tests/download_sandbox_analysis_result.json"
            ) as file:
                test_json = json.loads(file.read()).get("body")
                connection_params = test_json.get("connection")
                action_params = test_json.get("input")
        except Exception as e:
            message = f"Error reading JSON file: {e}"
            self.fail(message)

        test_conn.connect(connection_params)
        test_action.connection = test_conn
        results = test_action.run(action_params)
        self.assertIsInstance(results, dict)
        self.assertIn("file", results)
        self.assertIn("content", results["file"])
        self.assertIn("filename", results["file"])

    @patch("pytmv1.client")
    def test_download_sandbox_analysis_result_success(self, mock_pytmv1_client):
        mock_client_instance = MagicMock()
        mock_response = MagicMock(
            response=MagicMock(content=base64.b64encode(b"File content"))
        )
        mock_client_instance.download_sandbox_analysis_result.return_value = (
            mock_response
        )
        mock_pytmv1_client.return_value = mock_client_instance

        params = {
            "id": "2345431",
            "poll": True,
            "poll_time_sec": 5.0,
        }

        response = self.action.run(params)
        self.assertIsInstance(response, dict)
        self.assertIn("file", response)
        self.assertIn("content", response["file"])
        self.assertIn("filename", response["file"])

    @patch("pytmv1.client")
    def test_download_sandbox_analysis_result_failure(self, mock_pytmv1_client):
        mock_client_instance = MagicMock()
        mock_response = MagicMock(
            result_code="Error",
            errors={"error_message": "API Error", "error_code": 400},
        )
        mock_client_instance.download_sandbox_analysis_result.return_value = (
            mock_response
        )
        mock_pytmv1_client.return_value = mock_client_instance

        params = {
            "id": "2345431",
            "poll": True,
            "poll_time_sec": 5.0,
        }

        expected_output = {"error_message": "API Error", "error_code": 400}

        response = self.action.run(params)
        self.assertEqual(response.errors, expected_output)
