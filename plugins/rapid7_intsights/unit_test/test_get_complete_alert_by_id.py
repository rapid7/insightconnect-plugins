import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch
from unit_test.util import Util
from icon_rapid7_intsights.actions.get_complete_alert_by_id import GetCompleteAlertById
from icon_rapid7_intsights.actions.get_complete_alert_by_id.schema import Input


class TestAddManualAlert(TestCase):
    @classmethod
    @patch("requests.request", side_effect=Util.mock_request)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(GetCompleteAlertById())

    @patch("requests.request", side_effect=Util.mock_request)
    def test_get_complete_alert_by_id_should_success(self, make_request):
        actual = self.action.run({Input.ALERT_ID: "123"})
        expected = {
            "assets": [],
            "assignees": [],
            "details": {
                "Description": "APIDescription",
                "Images": [],
                "Severity": "High",
                "Source": {"NetworkType": "ClearWeb", "Type": "Application Store", "URL": "http://www.rapid7.com"},
                "SubType": "SuspiciousEmailAddress",
                "Tags": [],
                "Title": "Alerttest3",
                "Type": "Phishing",
            },
            "found_date": "2021-09-30T19:35:42.441Z",
            "id": "7cafac7ec5adaebf62257a4c",
            "is_closed": False,
            "is_flagged": False,
            "takedown_status": "NotSent",
            "update_date": "2021-09-30T19:35:42.441Z",
        }
        self.assertEqual(expected, actual)
