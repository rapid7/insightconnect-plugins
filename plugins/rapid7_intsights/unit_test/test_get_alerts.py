import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from util import Util
from icon_rapid7_intsights.actions.get_alerts import GetAlerts
from icon_rapid7_intsights.actions.get_alerts.schema import Input, GetAlertsInput, GetAlertsOutput
from jsonschema import validate


class TestAddManualAlert(TestCase):
    @classmethod
    @patch("requests.request", side_effect=Util.mock_request)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(GetAlerts())

    @patch("requests.request", side_effect=Util.mock_request)
    def test_get_alerts_success_with_empty_params(self, make_request):
        validate({}, GetAlertsInput.schema)
        actual = self.action.run({})
        expected = {
            "alert_ids": [
                "7cafac7ec5adaebf62257a4c",
                "7cafac7ec5adaebf62257a4d",
                "7cafac7ec5adaebf62257a4e",
                "7cafac7ec5adaebf62257a4f",
            ]
        }
        self.assertEqual(expected, actual)
        validate(actual, GetAlertsOutput.schema)

    @patch("requests.request", side_effect=Util.mock_request)
    def test_get_alerts_success_with_params(self, make_request):
        input_params = {Input.SEVERITY: ["High"]}
        validate(input_params, GetAlertsInput.schema)
        actual = self.action.run(input_params)
        expected = {
            "alert_ids": [
                "7cafac7ec5adaebf62257a4c",
                "7cafac7ec5adaebf62257a4d",
                "7cafac7ec5adaebf62257a4e",
                "7cafac7ec5adaebf62257a4f",
            ]
        }
        self.assertEqual(expected, actual)
        validate(actual, GetAlertsOutput.schema)

    @patch("requests.request", side_effect=Util.mock_request)
    def test_get_alerts_success_with_empty_response_list(self, make_request):
        input_params = {Input.ALERT_TYPE: ["Phishing"]}
        validate(input_params, GetAlertsInput.schema)
        actual = self.action.run(input_params)
        expected = {"alert_ids": []}
        self.assertEqual(expected, actual)
        validate(actual, GetAlertsOutput.schema)

    @patch("requests.request", side_effect=Util.mock_request)
    def test_get_alerts_success_with_list_of_alert_types(self, make_request):
        input_params = {Input.ALERT_TYPE: ["Phishing", "AttackIndication"]}
        validate(input_params, GetAlertsInput.schema)
        actual = self.action.run(input_params)
        expected = {"alert_ids": ["7cafac7ec5adaebf62257a4a", "7cafac7ec5adaebf62257a4b"]}
        self.assertEqual(expected, actual)
        validate(actual, GetAlertsOutput.schema)
