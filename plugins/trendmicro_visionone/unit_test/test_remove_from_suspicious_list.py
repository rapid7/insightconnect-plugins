import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock, patch
import json
import logging
from icon_trendmicro_visionone.connection.connection import Connection
from icon_trendmicro_visionone.actions.remove_from_suspicious_list import (
    RemoveFromSuspiciousList,
)


class TestRemoveFromSuspiciousList(TestCase):
    def setUp(self):
        self.connection = Connection()
        self.connection.logger = logging.getLogger()
        self.connection.server = "tmv1-mock.trendmicro.com"
        self.connection.token_ = "Dummy-Secret-Token"
        self.connection.app = "TM-R7"

        self.action = RemoveFromSuspiciousList()
        self.action.connection = self.connection

    def test_integration_remove_from_suspicious_list(self):
        log = logging.getLogger("Test")
        test_conn = Connection()
        test_action = RemoveFromSuspiciousList()

        test_conn.logger = log
        test_action.logger = log

        try:
            with open("/python/src/tests/remove_from_suspicious_list.json") as file:
                test_json = json.loads(file.read()).get("body")
                connection_params = test_json.get("connection")
                action_params = test_json.get("input")
        except Exception as e:
            message = f"Error reading JSON file: {e}"
            self.fail(message)

        test_conn.connect(connection_params)
        test_action.connection = test_conn
        results = test_action.run(action_params)
        expected_output = {"multi_response": [{"status": 204, "task_id": "None"}]}

        self.assertEqual(results, expected_output)

    @patch("pytmv1.client")
    def test_remove_from_suspicious_list_success(self, mock_pytmv1_client):
        mock_client_instance = MagicMock()
        mock_client_instance.remove_from_suspicious_list.side_effect = [
            MagicMock(
                result_code="Success",
                response=MagicMock(
                    dict=MagicMock(
                        return_value={"items": [{"status": 204, "task_id": "None"}]}
                    )
                ),
            ),
        ]

        mock_pytmv1_client.return_value = mock_client_instance

        params = {"block_object": [{"object_type": "ip", "object_value": "6.6.6.4"}]}

        expected_output = {"multi_response": [{"status": 204, "task_id": "None"}]}

        response = self.action.run(params)
        self.assertEqual(response, expected_output)

    @patch("pytmv1.client")
    def test_remove_from_suspicious_list_failure(self, mock_pytmv1_client):
        mock_client_instance = MagicMock()
        mock_client_instance.remove_from_suspicious_list.side_effect = Exception(
            "API request failed"
        )
        mock_pytmv1_client.return_value = mock_client_instance

        params = {"block_object": [{"object_type": "ip", "object_value": "6.6.6.4"}]}

        with self.assertRaises(Exception) as context:
            self.action.run(params)

        self.assertTrue("API request failed" in str(context.exception))
