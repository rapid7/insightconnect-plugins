import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import MagicMock, patch
import json
import logging
from icon_trendmicro_visionone.connection.connection import Connection
from icon_trendmicro_visionone.actions.get_exception_list import GetExceptionList


class TestGetExceptionList(TestCase):
    def setUp(self):
        self.connection = Connection()
        self.connection.logger = logging.getLogger()
        self.connection.server = "tmv1-mock.trendmicro.com"
        self.connection.token_ = "Dummy-Secret-Token"
        self.connection.app = "TM-R7"

        self.action = GetExceptionList()
        self.action.connection = self.connection

    def test_integration_get_exception_list(self):
        log = logging.getLogger("Test")
        test_conn = Connection()
        test_action = GetExceptionList()

        test_conn.logger = log
        test_action.logger = log

        try:
            with open("/python/src/tests/get_exception_list.json") as file:
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
            "exception_objects": [
                {
                    "description": "object description",
                    "last_modified_date_time": "2023-05-04T15:53:47Z",
                    "type": "url",
                    "value": "https://*.example.com/path1/*",
                }
            ],
        }

        self.assertIn("exception_objects", results)

    @patch("pytmv1.client")
    def test_get_exception_list_success(self, mock_pytmv1_client):
        mock_client_instance = MagicMock()
        mock_client_instance.consume_exception_list.return_value = [
            {"id": "1", "name": "Exception 1", "description": ""},
            {"id": "2", "name": "Exception 2", "description": "Test description"},
        ]
        mock_pytmv1_client.return_value = mock_client_instance

        params = {}

        expected_output = {
            "exception_objects": [],
        }

        response = self.action.run(params)
        self.assertEqual(response, expected_output)

    @patch("pytmv1.client")
    def test_get_exception_list_failure(self, mock_pytmv1_client):
        mock_client_instance = MagicMock()
        mock_client_instance.consume_exception_list.side_effect = Exception(
            "Failed to get exception list"
        )
        mock_pytmv1_client.return_value = mock_client_instance

        params = {}

        expected_output = "Failed to get exception list"

        response = self.action.run(params)
        self.assertIn(expected_output, str(response))
