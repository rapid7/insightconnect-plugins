import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase, mock
from unittest.mock import patch

from icon_jira_service_management.actions.close_alert import CloseAlert
from icon_jira_service_management.actions.close_alert.schema import CloseAlertOutput
from jsonschema import validate

from util import Util


@patch("requests.sessions.Session.send")
class TestCloseAlert(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(CloseAlert())

    def test_close_alert_success(self, mock_send: mock.Mock) -> None:
        mock_send.side_effect = [
            Util.MockResponse("close_alert_request.json", 202),
        ]

        input_params = {
            "identifier": "111111-9999-4ec2-8067-acde6abc040-1111123123",
        }

        expected = {
            "elapsed_time": 0.029,
            "requestId": "12345678-d325-4xx9-1234-8ee2c35e4606",
            "result": "Request will be processed",
        }

        actual = self.action.run(input_params)

        validate(actual, CloseAlertOutput.schema)
        self.assertEqual(actual, expected)
