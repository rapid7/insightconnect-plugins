import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase, mock
from unittest.mock import call, patch

import requests
from icon_jira_service_management.actions.create_alert import CreateAlert
from icon_jira_service_management.actions.create_alert.schema import CreateAlertOutput
from icon_jira_service_management.util.api import MAX_STATUS_TRIES
from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate

from util import Util


@patch("requests.sessions.Session.send")
class TestCreateAlert(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(CreateAlert())

    INPUT_PARAMS = {
        "message": "Test",
        "alias": "",
        "description": "",
        "responders": [],
        "visibleTo": [],
        "actions": [],
        "tags": [],
        "details": {},
        "entity": "",
        "source": "Rapid7 Automation",
        "priority": "P3",
        "user": "",
        "note": "",
    }

    EXPECTED = {
        "alertId": "f111ea16-9999-4ec2-8067-acde6abc040-1111123123",
        "elapsed_time": 0.009,
        "requestId": "12345678-d325-4xx9-1234-8ee2c35e4606",
        "result": "Request will be processed",
    }

    def test_create_alert_success(self, mock_send: mock.Mock) -> None:
        mock_send.side_effect = [
            Util.MockResponse("create_alert_request.json", 200),
            Util.MockResponse("get_request_status_request.json", 200),
        ]

        actual = self.action.run(self.INPUT_PARAMS)
        validate(actual, CreateAlertOutput.schema)
        self.assertEqual(actual, self.EXPECTED)

    @patch("time.sleep")
    def test_create_alert_retries_while_request_not_processed(
        self, mock_sleep: mock.Mock, mock_send: mock.Mock
    ) -> None:
        # 404: not processed yet, 408: timeout, 429: rate limited, 5xx: server errors (502 has no status code in the SDK)
        for status_code in (404, 408, 429, 500, 502, 503):
            with self.subTest(status_code=status_code):
                mock_send.reset_mock()
                mock_sleep.reset_mock()
                mock_send.side_effect = [
                    Util.MockResponse("create_alert_request.json", 200),
                    Util.MockResponse("get_request_status_not_found.json", status_code),
                    Util.MockResponse("get_request_status_not_found.json", status_code),
                    Util.MockResponse("get_request_status_request.json", 200),
                ]

                actual = self.action.run(self.INPUT_PARAMS)
                validate(actual, CreateAlertOutput.schema)
                self.assertEqual(actual, self.EXPECTED)
                self.assertEqual(mock_send.call_count, 4)
                self.assertEqual(mock_sleep.call_args_list, [call(0), call(1), call(2)])

    @patch("time.sleep")
    def test_create_alert_retries_on_connection_error(self, mock_sleep: mock.Mock, mock_send: mock.Mock) -> None:
        mock_send.side_effect = [
            Util.MockResponse("create_alert_request.json", 200),
            requests.exceptions.ConnectionError(),
            requests.exceptions.Timeout(),
            Util.MockResponse("get_request_status_request.json", 200),
        ]

        actual = self.action.run(self.INPUT_PARAMS)
        self.assertEqual(actual, self.EXPECTED)
        self.assertEqual(mock_send.call_count, 4)
        self.assertEqual(mock_sleep.call_args_list, [call(0), call(1), call(2)])

    @patch("time.sleep")
    def test_create_alert_request_never_processed(self, mock_sleep: mock.Mock, mock_send: mock.Mock) -> None:
        mock_send.side_effect = [Util.MockResponse("create_alert_request.json", 200)] + [
            Util.MockResponse("get_request_status_not_found.json", 404) for _ in range(MAX_STATUS_TRIES)
        ]

        with self.assertRaises(PluginException) as context:
            self.action.run(self.INPUT_PARAMS)

        self.assertIn("12345678-d325-4xx9-1234-8ee2c35e4606", context.exception.cause)
        self.assertIn("not processed", context.exception.cause)
        self.assertIn("Last error:", context.exception.data)
        self.assertEqual(mock_send.call_count, 1 + MAX_STATUS_TRIES)
        self.assertEqual(mock_sleep.call_count, MAX_STATUS_TRIES)

    @patch("time.sleep")
    def test_create_alert_status_error_is_not_retried(self, mock_sleep: mock.Mock, mock_send: mock.Mock) -> None:
        for status_code in (400, 401, 403):
            with self.subTest(status_code=status_code):
                mock_send.reset_mock()
                mock_sleep.reset_mock()
                mock_send.side_effect = [
                    Util.MockResponse("create_alert_request.json", 200),
                    Util.MockResponse("get_request_status_not_found.json", status_code),
                ]

                with self.assertRaises(PluginException):
                    self.action.run(self.INPUT_PARAMS)

                self.assertEqual(mock_send.call_count, 2)
                self.assertEqual(mock_sleep.call_args_list, [call(0)])

    def test_create_alert_request_failed(self, mock_send: mock.Mock) -> None:
        mock_send.side_effect = [
            Util.MockResponse("create_alert_request.json", 200),
            Util.MockResponse("get_request_status_failed.json", 200),
        ]

        with self.assertRaises(PluginException) as context:
            self.action.run(self.INPUT_PARAMS)

        self.assertIn("Alert rejected by JSM", context.exception.data)
        self.assertEqual(mock_send.call_count, 2)
