import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock, patch
import json
import logging
from icon_trendmicro_visionone.connection.connection import Connection
from icon_trendmicro_visionone.actions.get_task_result import GetTaskResult


class TestGetTaskResult(TestCase):
    def setUp(self):
        self.connection = Connection()
        self.connection.logger = logging.getLogger()
        self.connection.server = "tmv1-mock.trendmicro.com"
        self.connection.token_ = "Dummy-Secret-Token"
        self.connection.app = "TM-R7"

        self.action = GetTaskResult()
        self.action.connection = self.connection

    def test_integration_get_task_result(self):
        log = logging.getLogger("Test")
        test_conn = Connection()
        test_action = GetTaskResult()

        test_conn.logger = log
        test_action.logger = log

        try:
            with open("/python/src/tests/get_task_result.json") as file:
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
            "task_result": {
                "id": "234234",
                "status": "completed",
                "message": "Task completed successfully.",
            }
        }

        self.assertIn("action", results)

    @patch("pytmv1.client")
    def test_get_task_result_success(self, mock_pytmv1_client):
        mock_client_instance = MagicMock()
        mock_client_instance.get_base_task_result.side_effect = [
            MagicMock(
                result_code="Success",
                response=MagicMock(
                    dict=MagicMock(
                        return_value={
                            "task_result": {
                                "id": "234234",
                                "status": "completed",
                                "message": "Task completed successfully.",
                            },
                        }
                    )
                ),
            ),
        ]

        mock_pytmv1_client.return_value = mock_client_instance

        params = {"task_id": "00002194", "poll": False, "poll_time_sec": 0}

        expected_output = {
            "task_result": {
                "id": "234234",
                "status": "completed",
                "message": "Task completed successfully.",
            }
        }

        response = self.action.run(params)
        self.assertEqual(response, expected_output)

    @patch("pytmv1.client")
    def test_get_task_result_failure(self, mock_pytmv1_client):
        mock_client_instance = MagicMock()
        mock_client_instance.get_base_task_result.side_effect = Exception(
            "API request failed"
        )
        mock_pytmv1_client.return_value = mock_client_instance

        params = {"task_id": "234234", "poll": True, "poll_time_sec": 5.0}

        with self.assertRaises(Exception) as context:
            self.action.run(params)

        self.assertTrue("API request failed" in str(context.exception))
