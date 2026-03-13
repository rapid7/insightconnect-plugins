import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase, mock
from unittest.mock import patch

from icon_jira_service_management.actions.create_alert import CreateAlert
from icon_jira_service_management.actions.create_alert.schema import CreateAlertOutput
from jsonschema import validate

from util import Util


@patch("requests.sessions.Session.send")
class TestCreateAlert(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(CreateAlert())

    def test_create_alert_success(self, mock_send: mock.Mock) -> None:
        mock_send.side_effect = [
            Util.MockResponse("create_alert_request.json", 200),
            Util.MockResponse("get_request_status_request.json", 200),
        ]

        input_params = {
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
            "note": ""
        }

        expected = {
            "alertId": "f111ea16-9999-4ec2-8067-acde6abc040-1111123123",
            "elapsed_time": 0.009,
            "requestId": "12345678-d325-4xx9-1234-8ee2c35e4606",
            "result": "Request will be processed"
        }

        actual = self.action.run(input_params)
        validate(actual, CreateAlertOutput.schema)
        self.assertEqual(actual, expected)
