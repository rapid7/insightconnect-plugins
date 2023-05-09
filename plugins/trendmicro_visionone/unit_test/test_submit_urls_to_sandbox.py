import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock, patch
import json
import logging
from icon_trendmicro_visionone.connection.connection import Connection
from icon_trendmicro_visionone.actions.submit_urls_to_sandbox import SubmitUrlsToSandbox


class TestSubmitUrlsToSandbox(TestCase):
    def setUp(self):
        self.connection = Connection()
        self.connection.logger = logging.getLogger()
        self.connection.server = "tmv1-mock.trendmicro.com"
        self.connection.token_ = "Dummy-Secret-Token"
        self.connection.app = "TM-R7"

        self.action = SubmitUrlsToSandbox()
        self.action.connection = self.connection

    def test_integration_submit_urls_to_sandbox(self):
        log = logging.getLogger("Test")
        test_conn = Connection()
        test_action = SubmitUrlsToSandbox()

        test_conn.logger = log
        test_action.logger = log

        try:
            with open("/python/src/tests/submit_urls_to_sandbox.json") as file:
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
            "submit_urls_resp": [
                {"status": 200, "url_id": "12345"},
                {"status": 200, "url_id": "67890"},
            ]
        }

        self.assertIn("status", str(results))

    @patch("pytmv1.client")
    def test_submit_urls_to_sandbox_success(self, mock_pytmv1_client):
        mock_client_instance = MagicMock()
        mock_client_instance.submit_urls_to_sandbox.side_effect = [
            MagicMock(
                result_code="Success",
                response=MagicMock(
                    dict=MagicMock(
                        return_value={"items": [{"status": 200, "url_id": "12345"}]}
                    )
                ),
            ),
            MagicMock(
                result_code="Success",
                response=MagicMock(
                    dict=MagicMock(
                        return_value={"items": [{"status": 200, "url_id": "67890"}]}
                    )
                ),
            ),
        ]

        mock_pytmv1_client.return_value = mock_client_instance

        params = {"url": ["http://www.google.com", "http://www.yahoo.com"]}

        expected_output = {
            "submit_urls_resp": [
                {"status": 200, "url_id": "12345"},
                {"status": 200, "url_id": "67890"},
            ]
        }

        response = self.action.run(params)
        self.assertEqual(response, expected_output)

    @patch("pytmv1.client")
    def test_submit_urls_to_sandbox_failure(self, mock_pytmv1_client):
        mock_client_instance = MagicMock()
        mock_client_instance.submit_urls_to_sandbox.side_effect = Exception(
            "API request failed"
        )
        mock_pytmv1_client.return_value = mock_client_instance

        params = {"url": ["http://www.google.com", "http://www.yahoo.com"]}

        with self.assertRaises(Exception) as context:
            self.action.run(params)

        self.assertTrue("API request failed" in str(context.exception))
