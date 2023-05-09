import sys
import os
import json
import logging

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock, patch

from icon_trendmicro_visionone.connection.connection import Connection
from icon_trendmicro_visionone.actions.add_to_exception_list import AddToExceptionList
import pytmv1


class TestAddToExceptionList(TestCase):
    def setUp(self):
        self.connection = Connection()
        self.connection.logger = logging.getLogger()
        self.connection.server = "tmv1-mock.trendmicro.com"
        self.connection.token_ = "Dummy-Secret-Token"
        self.connection.app = "TM-R7"

        self.action = AddToExceptionList()
        self.action.connection = self.connection

    def test_integration_add_to_exception_list(self):
        log = logging.getLogger("Test")
        test_conn = Connection()
        test_action = AddToExceptionList()

        test_conn.logger = log
        test_action.logger = log

        try:
            with open("/python/src/tests/add_to_exception_list.json") as file:
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
            "multi_response": [
                {
                    "task_id": "None",
                    "status": 201,
                },
            ],
        }

        self.assertEqual(results, expected_output)

    @patch("pytmv1.client")
    def test_add_to_exception_list_success(self, mock_pytmv1_client):
        mock_client_instance = MagicMock()
        mock_client_instance.add_to_exception_list.side_effect = [
            MagicMock(
                result_code="Success",
                response=MagicMock(
                    dict=MagicMock(
                        return_value={
                            "items": [
                                {
                                    "object_type": "IP",
                                    "object_value": "1.2.6.9",
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
            "block_object": [{"object_type": "IP", "object_value": "1.2.6.9"}],
        }

        expected_output = {
            "multi_response": [
                {"object_type": "IP", "object_value": "1.2.6.9", "task_id": "00000007"},
            ],
        }

        response = self.action.run(params)
        self.assertEqual(response, expected_output)

    @patch("pytmv1.client")
    def test_add_to_exception_list_failure(self, mock_pytmv1_client):
        mock_client_instance = MagicMock()
        mock_client_instance.add_to_exception_list.side_effect = [
            MagicMock(
                result_code="Error",
                errors={"error_message": "API Error", "error_code": 400},
            )
        ]
        mock_pytmv1_client.return_value = mock_client_instance

        params = {
            "block_object": [{"object_type": "IP", "object_value": "1.2.6.9"}],
        }

        expected_output = {"error_message": "API Error", "error_code": 400}

        response = self.action.run(params)
        self.assertEqual(response, expected_output)
