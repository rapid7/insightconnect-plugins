import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock, patch
import json
import logging
import pytmv1
from icon_trendmicro_visionone.connection.connection import Connection
from icon_trendmicro_visionone.actions.add_to_block_list import AddToBlockList


class TestAddToBlockList(TestCase):
    def setUp(self):
        self.connection = Connection()
        self.connection.logger = logging.getLogger()
        self.connection.server = "tmv1-mock.trendmicro.com"
        self.connection.token_ = "Dummy-Secret-Token"
        self.connection.app = "TM-R7"

        self.action = AddToBlockList()
        self.action.connection = self.connection

    def test_integration_add_to_block_list(self):
        log = logging.getLogger("Test")
        test_conn = Connection()
        test_action = AddToBlockList()

        test_conn.logger = log
        test_action.logger = log

        try:
            with open("/python/src/tests/add_to_block_list.json") as file:
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
                {"status": 202, "task_id": "00000007"},
                {"status": 202, "task_id": "00000007"},
            ],
        }

        self.assertEqual(results, expected_output)

    @patch("pytmv1.client")
    def test_add_to_block_list_success(self, mock_pytmv1_client):
        mock_client_instance = MagicMock()
        mock_client_instance.add_to_block_list.side_effect = [
            MagicMock(
                result_code="Success",
                response=MagicMock(
                    dict=MagicMock(
                        return_value={
                            "items": [
                                {
                                    "object_type": "IP",
                                    "object_value": "6.6.6.6",
                                    "description": "block",
                                },
                            ]
                        }
                    )
                ),
            ),
            MagicMock(
                result_code="Success",
                response=MagicMock(
                    dict=MagicMock(
                        return_value={
                            "items": [
                                {
                                    "object_type": "IP",
                                    "object_value": "6.6.6.7",
                                    "description": "block",
                                },
                            ]
                        }
                    )
                ),
            ),
        ]
        mock_pytmv1_client.return_value = mock_client_instance

        params = {
            "block_object": [
                {
                    "object_type": "IP",
                    "object_value": "6.6.6.6",
                    "description": "block",
                },
                {
                    "object_type": "IP",
                    "object_value": "6.6.6.7",
                    "description": "block",
                },
            ],
        }

        expected_output = {
            "multi_response": [
                {
                    "object_type": "IP",
                    "object_value": "6.6.6.6",
                    "description": "block",
                },
                {
                    "object_type": "IP",
                    "object_value": "6.6.6.7",
                    "description": "block",
                },
            ],
        }

        response = self.action.run(params)
        self.assertEqual(response, expected_output)

    @patch("pytmv1.client")
    def test_add_to_block_list_failure(self, mock_pytmv1_client):
        mock_client_instance = MagicMock()
        mock_client_instance.add_to_block_list.return_value = MagicMock(
            result_code="Error",
            errors="Failed to add block object",
        )
        mock_pytmv1_client.return_value = mock_client_instance

        params = {
            "block_object": [
                {
                    "object_type": "IP",
                    "object_value": "6.6.6.6",
                    "description": "block",
                },
                {
                    "object_type": "IP",
                    "object_value": "6.6.6.7",
                    "description": "block",
                },
            ],
        }

        expected_output = "Failed to add block object"

        response = self.action.run(params)
        self.assertEqual(response, expected_output)
