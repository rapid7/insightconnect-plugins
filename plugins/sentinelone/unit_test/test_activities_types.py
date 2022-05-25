import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest.mock import patch
from komand_sentinelone.actions.activities_types import ActivitiesTypes
from unit_test.util import Util
from unittest import TestCase


class TestActivitiesTypes(TestCase):
    @classmethod
    @patch("requests.post", side_effect=Util.mocked_requests_get)
    def setUpClass(cls, mock_request) -> None:
        cls.action = Util.default_connector(ActivitiesTypes())
        Util.mock_response_params = {}

    @patch("requests.post", side_effect=Util.mocked_requests_get)
    @patch("requests.request", side_effect=Util.mocked_requests_get)
    def test_should_success_without_inputs(self, mock_request, mock_request_post):
        actual = self.action.run()
        expected = {
            "activity_types": [
                {
                    "action": "Account Created",
                    "descriptionTemplate": "The management user {{ username }} created {{ account_name }} account.",
                    "id": 5040,
                },
                {
                    "action": "Account Deleted",
                    "descriptionTemplate": "The management user {{ username }} deleted the account {{ account_name }}",
                    "id": 5042,
                },
                {
                    "action": "Account Expired",
                    "descriptionTemplate": "The account {{ account_name }} expired automatically at "
                    "{{ account_expiration | datetime}} because the expiration day was over",
                    "id": 5043,
                },
                {
                    "action": "Account marked as Expired",
                    "descriptionTemplate": "The management user {{ username }} marked account {{ account_name }} as expired",
                    "id": 5045,
                },
            ]
        }
        self.assertEqual(expected, actual)
