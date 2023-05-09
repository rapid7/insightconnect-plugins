import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock, patch
import json
import logging
from icon_trendmicro_visionone.connection.connection import Connection
from icon_trendmicro_visionone.actions.get_endpoint_data import GetEndpointData


class TestGetEndpointData(TestCase):
    def setUp(self):
        self.connection = Connection()
        self.connection.logger = logging.getLogger()
        self.connection.server = "tmv1-mock.trendmicro.com"
        self.connection.token_ = "Dummy-Secret-Token"
        self.connection.app = "TM-R7"

        self.action = GetEndpointData()
        self.action.connection = self.connection

    def test_integration_get_endpoint_data(self):
        log = logging.getLogger("Test")
        test_conn = Connection()
        test_action = GetEndpointData()

        test_conn.logger = log
        test_action.logger = log

        try:
            with open("/python/src/tests/get_endpoint_data.json") as file:
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
            "endpoint_data": [
                {"id": "1", "name": "Endpoint Data 1"},
                {"id": "2", "name": "Endpoint Data 2"},
            ],
        }

        self.assertIn("endpoint_data", results)

    @patch("pytmv1.client")
    def test_get_endpoint_data_success(self, mock_pytmv1_client):
        mock_client_instance = MagicMock()
        mock_client_instance.consume_endpoint_data.return_value = [
            {"id": "1", "name": "Endpoint Data 1"},
            {"id": "2", "name": "Endpoint Data 2"},
        ]
        mock_pytmv1_client.return_value = mock_client_instance

        params = {
            "endpoint": "workstation1",
            "query_op": " or ",
        }

        expected_output = {
            "endpoint_data": [],
        }

        response = self.action.run(params)
        self.assertEqual(response, expected_output)

    @patch("pytmv1.client")
    def test_get_endpoint_data_failure(self, mock_pytmv1_client):
        mock_client_instance = MagicMock()
        mock_client_instance.consume_endpoint_data.side_effect = Exception(
            "Failed to get endpoint data"
        )
        mock_pytmv1_client.return_value = mock_client_instance

        params = {
            "endpoint": "client1",
            "query_op": " or ",
        }

        expected_output = "Failed to get endpoint data"

        response = self.action.run(params)
        self.assertIn(expected_output, str(response))
