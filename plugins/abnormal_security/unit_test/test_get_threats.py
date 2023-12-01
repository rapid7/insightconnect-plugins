import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from icon_abnormal_security.actions.get_threats import GetThreats
from icon_abnormal_security.actions.get_threats.schema import Input, GetThreatsInput, GetThreatsOutput
from util import Util
from unittest.mock import patch
from jsonschema import validate


class TestGetCases(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(GetThreats())

    @patch("requests.request", side_effect=Util.mocked_requests)
    def test_manage_case(self, mock_post):
        test_input = {
            Input.FROM_DATE: "2021-03-01 21:11:38",
            Input.TO_DATE: "2021-03-11 21:11:38",
        }
        validate(test_input, GetThreatsInput.schema)
        actual = self.action.run(test_input)

        expected = {"threats": [{"threatId": "184712ab-6d8b-47b3-89d3-a314efef79e2"}]}

        self.assertEqual(actual, expected)
        validate(expected, GetThreatsOutput.schema)

    @patch("requests.request", side_effect=Util.mocked_requests)
    def test_manage_case2(self, mock_post):
        test_input = {
            Input.FROM_DATE: "2021-03-01T21:11:38Z",
            Input.TO_DATE: "2021-03-11T21:11:38Z",
        }
        validate(test_input, GetThreatsInput.schema)
        actual = self.action.run(test_input)

        expected = {"threats": [{"threatId": "184712ab-6d8b-47b3-89d3-a314efef79e2"}]}

        self.assertEqual(actual, expected)
        validate(expected, GetThreatsOutput.schema)
