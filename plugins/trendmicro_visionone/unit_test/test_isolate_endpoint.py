import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock, patch
import json
import logging
from icon_trendmicro_visionone.connection.connection import Connection
from icon_trendmicro_visionone.actions.isolate_endpoint import IsolateEndpoint


class TestIsolateEndpoint(TestCase):
    def setUp(self):
        self.connection = Connection()
        self.connection.logger = logging.getLogger()
        self.connection.server = "tmv1-mock.trendmicro.com"
        self.connection.token_ = "Dummy-Secret-Token"
        self.connection.app = "TM-R7"
        self.action = IsolateEndpoint()
        self.action.connection = self.connection

    def test_integration_isolate_endpoint(self):
        log = logging.getLogger("Test")
        test_conn = Connection()
        test_action = IsolateEndpoint()

        test_conn.logger = log
        test_action.logger = log

        try:
            with open("/python/src/tests/isolate_endpoint.json") as file:
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
            "multi_response": [{"status": 202, "task_id": "00000004"}],
        }

        self.assertEqual(
            results,
            expected_output,
        )

    @patch("pytmv1.client")
    def test_isolate_endpoint_success(self, mock_pytmv1_client):
        response_items = [
            {
                "status": 202,
                "task_id": "00000004",
            }
        ]

        mock_client_instance = MagicMock()
        mock_client_instance.isolate_endpoint.return_value = MagicMock(
            result_code="Success",
            response=MagicMock(dict=lambda: {"items": response_items}),
            errors=None,
        )
        mock_pytmv1_client.return_value = mock_client_instance

        params = {
            "endpoint_identifiers": [
                {
                    "endpoint": "client1",
                    "description": "TEST isolate endpoint",
                }
            ],
        }

        expected_output = {"multi_response": response_items}

        response = self.action.run(params)
        self.assertEqual(response, expected_output)

    @patch("pytmv1.client")
    def test_isolate_endpoint_failure(self, mock_pytmv1_client):
        def side_effect(endpoint_task):
            return MagicMock(
                result_code="Error",
                errors="Failed to isolate endpoint",
            )

        mock_client_instance = MagicMock()
        mock_client_instance.isolate_endpoint.side_effect = side_effect
        mock_pytmv1_client.return_value = mock_client_instance

        params = {
            "endpoint_identifiers": [
                {
                    "endpoint": "client1",
                    "description": "TEST isolate endpoint",
                }
            ],
        }

        expected_output = "Failed to isolate endpoint"

        response = self.action.run(params)
        self.assertEqual(response, expected_output)
