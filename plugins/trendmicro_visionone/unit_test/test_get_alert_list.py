import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock, patch
import json
import logging
from icon_trendmicro_visionone.connection.connection import Connection
from icon_trendmicro_visionone.actions.get_alert_list import GetAlertList


class TestGetAlertList(TestCase):
    def setUp(self):
        self.connection = Connection()
        self.connection.logger = logging.getLogger()
        self.connection.server = "tmv1-mock.trendmicro.com"
        self.connection.token_ = "Dummy-Secret-Token"
        self.connection.app = "TM-R7"

        self.action = GetAlertList()
        self.action.connection = self.connection

    def test_integration_get_alert_list(self):
        log = logging.getLogger("Test")
        test_conn = Connection()
        test_action = GetAlertList()

        test_conn.logger = log
        test_action.logger = log

        try:
            with open("/python/src/tests/get_alert_list.json") as file:
                test_json = json.loads(file.read()).get("body")
                connection_params = test_json.get("connection")
                action_params = test_json.get("input")
        except Exception as e:
            message = f"Error reading JSON file: {e}"
            self.fail(message)

        test_conn.connect(connection_params)
        test_action.connection = test_conn
        results = test_action.run(action_params)

        self.assertIn("total_count", results)
        self.assertIn("alerts", results)

    @patch("pytmv1.client")
    def test_get_alert_list_success(self, mock_pytmv1_client):
        mock_client_instance = MagicMock()
        mock_client_instance.consume_alert_list.return_value = [
            {"id": "1", "name": "Alert 1"},
            {"id": "2", "name": "Alert 2"},
        ]
        mock_pytmv1_client.return_value = mock_client_instance

        params = {
            "start_date_time": "2020-06-15T10:00:00Z",
            "end_date_time": "2020-07-15T10:00:00Z",
        }

        expected_output = {
            "total_count": 0,
            "alerts": [],
        }

        response = self.action.run(params)
        self.assertEqual(response, expected_output)

    @patch("pytmv1.client")
    def test_get_alert_list_failure(self, mock_pytmv1_client):
        mock_client_instance = MagicMock()
        mock_client_instance.consume_alert_list.side_effect = Exception(
            "Failed to get alert list"
        )
        mock_pytmv1_client.return_value = mock_client_instance

        params = {
            "start_date_time": "2020-06-15T10:00:00Z",
            "end_date_time": "2023-06-15",
        }

        expected_output = "Failed to get alert list"

        response = self.action.run(params)
        self.assertIn(expected_output, str(response))
