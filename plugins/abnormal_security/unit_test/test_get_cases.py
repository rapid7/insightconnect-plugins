import sys
import os
from unittest import TestCase
from icon_abnormal_security.actions.get_cases import GetCases
from icon_abnormal_security.actions.get_cases.schema import Input, Output
from unit_test.util import Util
from unittest.mock import patch

sys.path.append(os.path.abspath("../"))


class TestGetCases(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetCases())

    @patch("requests.request", side_effect=Util.mocked_requests)
    def test_manage_case(self, mock_post):
        actual = self.action.run()

        expected = {"cases": [{"caseId": "1234", "severity": "Potential Account Takeover"}]}

        self.assertEqual(actual, expected)

    @patch("requests.request", side_effect=Util.mocked_requests)
    def test_manage_case_2(self, mock_post):
        actual = self.action.run(
            {
                Input.FROM_DATE: "2021-03-01 21:11:38",
                Input.TO_DATE: "2021-03-11 21:11:38",
            }
        )

        expected = {"cases": [{"caseId": "1234", "severity": "Potential Account Takeover"}]}

        self.assertEqual(actual, expected)

    @patch("requests.request", side_effect=Util.mocked_requests)
    def test_manage_case_3(self, mock_post):
        actual = self.action.run(
            {
                Input.FROM_DATE: "2021-03-01T21:11:38Z",
                Input.TO_DATE: "2021-03-11T21:11:38Z",
            }
        )

        expected = {"cases": [{"caseId": "1234", "severity": "Potential Account Takeover"}]}

        self.assertEqual(actual, expected)
