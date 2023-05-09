import sys
import os
import json
import logging

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock, patch

from icon_trendmicro_visionone.connection import Connection
from icon_trendmicro_visionone.actions.edit_alert_status import (
    EditAlertStatus,
)


class TestEditAlertStatus(TestCase):
    def setUp(self):
        self.connection = Connection()
        self.connection.logger = logging.getLogger()
        self.connection.server = "tmv1-mock.trendmicro.com"
        self.connection.token_ = "Dummy-Secret-Token"
        self.connection.app = "Rapid7-InsightConnect"

        self.action = EditAlertStatus()
        self.action.connection = self.connection

    def test_integration_edit_alert_status(self):
        log = logging.getLogger("Test")
        test_conn = Connection()
        test_action = EditAlertStatus()

        test_conn.logger = log
        test_action.logger = log

        try:
            with open("/python/src/tests/edit_alert_status.json") as file:
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
        self.assertIn("result_code", results)

    @patch("pytmv1.client")
    def test_edit_alert_status_success(self, mock_pytmv1_client):
        mock_client_instance = MagicMock()
        mock_response = MagicMock(result_code="Success")
        mock_client_instance.edit_alert_status.return_value = mock_response
        mock_pytmv1_client.return_value = mock_client_instance

        params = {
            "id": "WB-14-20190709-00003",
            "status": "new",
            "if_match": "gw34g5435",
        }

        response = self.action.run(params)
        self.assertIsInstance(response, dict)
        self.assertIn("result_code", response)

    @patch("pytmv1.client")
    def test_edit_alert_status_failure(self, mock_pytmv1_client):
        mock_client_instance = MagicMock()
        mock_response = MagicMock(
            result_code="Error",
            errors={"error_message": "API Error", "error_code": 400},
        )
        mock_client_instance.edit_alert_status.return_value = mock_response
        mock_pytmv1_client.return_value = mock_client_instance

        params = {
            "id": "WB-14-20190709-00003",
            "status": "new",
            "if_match": "gw34g5435",
        }

        expected_output = {"error_message": "API Error", "error_code": 400}

        response = self.action.run(params)
        self.assertEqual(response.errors, expected_output)
