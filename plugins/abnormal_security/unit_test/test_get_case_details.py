import sys
import os
from unittest import TestCase
from icon_abnormal_security.actions.get_case_details import GetCaseDetails
from icon_abnormal_security.actions.get_case_details.schema import Input, Output
from unit_test.util import Util
from unittest.mock import patch

sys.path.append(os.path.abspath("../"))


class TestGetCases(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetCaseDetails())

    @patch("requests.request", side_effect=Util.mocked_requests)
    def test_manage_case(self, mock_post):
        actual = self.action.run(
            {
                Input.CASE_ID: "19377",
            }
        )

        expected = {
            "case_details": {
                "affectedEmployee": "FirstName LastName",
                "caseId": "19377",
                "firstObserved": "2020-06-09T17:42:59Z",
                "severity": "Potential Account Takeover",
            }
        }

        self.assertEqual(actual, expected)

    @patch("requests.request", side_effect=Util.mocked_requests)
    def test_manage_case2(self, mock_post):
        actual = self.action.run(
            {
                Input.CASE_ID: "19300",
            }
        )

        expected = {
            "case_details": {
                "affectedEmployee": "Example User",
                "caseId": "19300",
                "firstObserved": "2020-07-19T13:42:59Z",
                "severity": "Potential Account Takeover",
            }
        }

        self.assertEqual(actual, expected)
