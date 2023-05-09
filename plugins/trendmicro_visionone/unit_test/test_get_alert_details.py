import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock, patch
import json
import logging
from icon_trendmicro_visionone.connection.connection import Connection
from icon_trendmicro_visionone.actions.get_alert_details import GetAlertDetails


class TestGetAlertDetails(TestCase):
    def setUp(self):
        self.connection = Connection()
        self.connection.logger = logging.getLogger()
        self.connection.server = "tmv1-mock.trendmicro.com"
        self.connection.token_ = "Dummy-Secret-Token"
        self.connection.app = "TM-R7"

        self.action = GetAlertDetails()
        self.action.connection = self.connection

    def test_integration_get_alert_details(self):
        log = logging.getLogger("Test")
        test_conn = Connection()
        test_action = GetAlertDetails()

        test_conn.logger = log
        test_action.logger = log

        try:
            with open("/python/src/tests/get_alert_details.json") as file:
                test_json = json.loads(file.read()).get("body")
                connection_params = test_json.get("connection")
                action_params = test_json.get("input")
        except Exception as e:
            message = f"Error reading JSON file: {e}"
            self.fail(message)

        test_conn.connect(connection_params)
        test_action.connection = test_conn
        results = test_action.run(action_params)

        # Check the presence of some keys to determine if it's a passing test
        self.assertIn("etag", results)
        self.assertIn("alert_details", results)
        self.assertIn("alert", results["alert_details"])

    @patch("pytmv1.client")
    def test_get_alert_details_success(self, mock_pytmv1_client):
        mock_client_instance = MagicMock()
        mock_client_instance.get_alert_details.return_value = MagicMock(
            result_code="Success",
            response=MagicMock(
                etag="33a64df551425fcc55e4d42a148795d9f25f89d4",
                alert=MagicMock(
                    json=lambda: {
                        "id": "WB-20837-20221222-00000",
                        "status": "open",
                        "severity": "high",
                        "description": "Test alert",
                    }
                ),
            ),
        )
        mock_pytmv1_client.return_value = mock_client_instance

        params = {
            "alert_id": "WB-20837-20221222-00000",
        }

        expected_output = {
            "etag": "33a64df551425fcc55e4d42a148795d9f25f89d4",
            "alert_details": {
                "alert": {
                    "id": "WB-20837-20221222-00000",
                    "status": "open",
                    "severity": "high",
                    "description": "Test alert",
                }
            },
        }

        response = self.action.run(params)
        self.assertEqual(response, expected_output)

    @patch("pytmv1.client")
    def test_get_alert_details_failure(self, mock_pytmv1_client):
        mock_client_instance = MagicMock()
        mock_client_instance.get_alert_details.return_value = MagicMock(
            result_code="Error",
            errors={"error_message": "API Error", "error_code": 400},
        )
        mock_pytmv1_client.return_value = mock_client_instance

        params = {
            "alert_id": "WblooperB-20837-20221222-00000",
        }

        expected_output = {"error_message": "API Error", "error_code": 400}

        response = self.action.run(params)
        self.assertEqual(response.errors, expected_output)
