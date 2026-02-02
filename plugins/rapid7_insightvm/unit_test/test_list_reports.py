import os
import sys

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from unittest.mock import patch

from komand_rapid7_insightvm.actions.list_reports import ListReports
from komand_rapid7_insightvm.actions.list_reports.schema import Input
from parameterized import parameterized

from util import Util


@patch("requests.sessions.Session.get", side_effect=Util.mocked_requests)
class TestGetExpiringVulnerabilityExceptions(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(ListReports())

    @parameterized.expand(
        [
            ["not_found", "Invalid Report Name", "Ascending", {"found": False, "list": []}],
            ["found", "Report", "Ascending", {"found": True, "list": [{"id": 1, "name": "Report"}]}],
            [
                "all_reports",
                None,
                "Ascending",
                {"found": True, "list": [{"id": 1, "name": "Report"}, {"id": 2, "name": "Report_2"}]},
            ],
        ]
    )
    def test_list_reports(self, mock_get, name, report_name, sort, expected) -> None:
        actual = self.action.run({Input.NAME: report_name, Input.SORT: sort})
        self.assertEqual(actual, expected)
