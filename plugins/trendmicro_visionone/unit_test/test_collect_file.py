import sys
import os
import json
import logging

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock, patch

from icon_trendmicro_visionone.connection.connection import Connection
from icon_trendmicro_visionone.actions.collect_file import CollectFile
import pytmv1


class TestCollectFile(TestCase):
    def setUp(self):
        self.connection = Connection()
        self.connection.logger = logging.getLogger()
        self.connection.server = "tmv1-mock.trendmicro.com"
        self.connection.token_ = "Dummy-Secret-Token"
        self.connection.app = "TM-R7"

        self.action = CollectFile()
        self.action.connection = self.connection

    def test_integration_collect_file(self):
        log = logging.getLogger("Test")
        test_conn = Connection()
        test_action = CollectFile()

        test_conn.logger = log
        test_action.logger = log

        try:
            with open("/python/src/tests/collect_file.json") as file:
                test_json = json.loads(file.read()).get("body")
                connection_params = test_json.get("connection")
                action_params = test_json.get("input")
                collect_files = action_params.get("collect_files")
        except Exception as e:
            message = f"Error reading JSON file: {e}"
            self.fail(message)

        if collect_files is None:
            message = "Error: collect_files is None"
            self.fail(message)

        test_conn.connect(connection_params)
        test_action.connection = test_conn
        results = test_action.run({"collect_files": collect_files})
        expected_output = {
            "multi_response": [
                {
                    "task_id": "00000003",
                    "status": 202,
                },
            ],
        }

        self.assertEqual(results, expected_output)

    @patch("pytmv1.client")
    def test_collect_file_success(self, mock_pytmv1_client):
        mock_client_instance = MagicMock()
        mock_client_instance.collect_file.side_effect = [
            MagicMock(
                result_code="Success",
                response=MagicMock(
                    dict=MagicMock(
                        return_value={
                            "items": [
                                {
                                    "endpointName": "client1",
                                    "filePath": "C:/virus.exe",
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
            "collect_files": [
                {
                    "endpoint": "client1",
                    "file_path": "C:/virus.exe",
                    "description": "collect malicious file",
                },
            ],
        }

        expected_output = {
            "multi_response": [
                {
                    "endpointName": "client1",
                    "filePath": "C:/virus.exe",
                    "task_id": "00000007",
                },
            ],
        }

        response = self.action.run(params)
        self.assertEqual(response, expected_output)

    @patch("pytmv1.client")
    def test_collect_file_failure(self, mock_pytmv1_client):
        mock_client_instance = MagicMock()
        mock_client_instance.collect_file.side_effect = [
            MagicMock(
                result_code="Error",
                errors={"error_message": "API Error", "error_code": 400},
            )
        ]
        mock_pytmv1_client.return_value = mock_client_instance

        params = {
            "collect_files": [
                {
                    "endpoint": "client1",
                    "file_path": "C:/virus.exe",
                    "description": "collect malicious file",
                },
            ],
        }

        expected_output = {"error_message": "API Error", "error_code": 400}

        response = self.action.run(params)
        self.assertEqual(response, expected_output)
