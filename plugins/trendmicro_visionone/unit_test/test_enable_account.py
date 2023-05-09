import sys
import os
import json
import logging

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock, patch

from icon_trendmicro_visionone.connection import Connection
from icon_trendmicro_visionone.actions.enable_account import (
    EnableAccount,
)


class TestEnableAccount(TestCase):
    def setUp(self):
        self.connection = Connection()
        self.connection.logger = logging.getLogger()
        self.connection.server = "tmv1-mock.trendmicro.com"
        self.connection.token_ = "Dummy-Secret-Token"
        self.connection.app = "Rapid7-InsightConnect"

        self.action = EnableAccount()
        self.action.connection = self.connection

    def test_integration_enable_account(self):
        log = logging.getLogger("Test")
        test_conn = Connection()
        test_action = EnableAccount()

        test_conn.logger = log
        test_action.logger = log

        with open("/python/src/tests/enable_account.json") as file:
            test_json = json.loads(file.read()).get("body")
            connection_params = test_json.get("connection")
            action_params = test_json.get("input")

        test_conn.connect(connection_params)
        test_action.connection = test_conn
        results = test_action.run(action_params)
        self.assertIsInstance(results, dict)
        self.assertIn("multi_response", results)

    @patch("pytmv1.client")
    def test_enable_account_success(self, mock_pytmv1_client):
        mock_client_instance = MagicMock()
        mock_client_instance.enable_account.side_effect = [
            MagicMock(
                result_code="Success",
                response=MagicMock(
                    dict=MagicMock(
                        return_value={"items": [{"status": 202, "task_id": "00000010"}]}
                    )
                ),
            )
        ]
        mock_pytmv1_client.return_value = mock_client_instance

        params = {
            "account_identifiers": [
                {
                    "account_name": "jdoe@testemailtest.com",
                    "description": "enable jdoe account, r7 test",
                }
            ],
        }

        expected_output = {
            "multi_response": [
                {"status": 202, "task_id": "00000010"},
            ],
        }

        response = self.action.run(params)
        self.assertEqual(response, expected_output)

    @patch("pytmv1.client")
    def test_enable_account_failure(self, mock_pytmv1_client):
        mock_client_instance = MagicMock()
        mock_response = MagicMock(
            result_code="Error",
            errors={"error_message": "API Error", "error_code": 400},
        )
        mock_client_instance.enable_account.return_value = mock_response
        mock_pytmv1_client.return_value = mock_client_instance

        params = {
            "account_identifiers": [
                {
                    "account_name": "user1",
                    "description": "TEST enable account",
                }
            ],
        }

        expected_output = {"error_message": "API Error", "error_code": 400}

        response = self.action.run(params)
        self.assertEqual(response, expected_output)
