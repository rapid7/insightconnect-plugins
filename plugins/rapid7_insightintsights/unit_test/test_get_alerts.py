import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from unit_test.util import Util
from icon_rapid7_intsights.actions.get_alerts import GetAlerts
from icon_rapid7_intsights.actions.get_alerts.schema import Input


class TestAddManualAlert(TestCase):
    @classmethod
    @patch("requests.request", side_effect=Util.mock_request)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(GetAlerts())

    @patch("requests.request", side_effect=Util.mock_request)
    def test_get_alerts_success_with_empty_params(self, make_request):
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

    @patch("requests.request", side_effect=Util.mock_request)
    def test_get_alerts_success_with_params(self, make_request):
        actual = self.action.run({Input.SEVERITY: "High"})
        expected = {
            "alert_ids": [
                "7cafac7ec5adaebf62257a4c",
                "7cafac7ec5adaebf62257a4d",
                "7cafac7ec5adaebf62257a4e",
                "7cafac7ec5adaebf62257a4f",
            ]
        }
        self.assertEqual(expected, actual)

    @patch("requests.request", side_effect=Util.mock_request)
    def test_get_alerts_success_with_empty_response_list(self, make_request):
        actual = self.action.run({Input.ALERT_TYPE: ["Phishing"]})
        expected = {"alert_ids": []}
        self.assertEqual(expected, actual)

    @patch("requests.request", side_effect=Util.mock_request)
    def test_get_alerts_success_with_list_of_alert_types(self, make_request):
        actual = self.action.run({Input.ALERT_TYPE: ["Phishing", "AttackIndication"]})
        expected = {"alert_ids": ["7cafac7ec5adaebf62257a4a", "7cafac7ec5adaebf62257a4b"]}
        self.assertEqual(expected, actual)
