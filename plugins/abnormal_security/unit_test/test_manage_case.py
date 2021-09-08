import sys
import os
from unittest import TestCase
from icon_abnormal_security.actions.manage_case import ManageCase
from icon_abnormal_security.actions.manage_case.schema import Input, Output
from insightconnect_plugin_runtime.exceptions import PluginException
from unit_test.util import Util
from unittest.mock import patch

sys.path.append(os.path.abspath("../"))


class TestManageCase(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(ManageCase())

    @patch("requests.request", side_effect=Util.mocked_requests)
    def test_manage_case_not_an_attack(self, mock_post):
        actual = self.action.run(
            {
                Input.ACTION: "Acknowledge not an Attack",
                Input.CASE_ID: "12345",
            }
        )

        expected = {
            "response": {
                "actionId": "61e76395-40d3-4d78-b6a8-8b17634d0f5b",
                "statusUrl": "https://api.abnormalplatform.com/v1/cases/12345/actions/61e76395-40d3-4d78-b6a8-8b17634d0f5b",
            }
        }

        self.assertEqual(actual, expected)

    @patch("requests.request", side_effect=Util.mocked_requests)
    def test_manage_case_action_required(self, mock_post):
        actual = self.action.run(
            {
                Input.ACTION: "Action Required",
                Input.CASE_ID: "34567",
            }
        )

        expected = {
            "response": {
                "actionId": "74b2790c-56d1-0923-12bb-43b29901cc23",
                "statusUrl": "https://api.abnormalplatform.com/v1/cases/34567/actions/74b2790c-56d1-0923-12bb-43b29901cc23",
            }
        }

        self.assertEqual(actual, expected)

    @patch("requests.request", side_effect=Util.mocked_requests)
    def test_manage_case_in_progress(self, mock_post):
        actual = self.action.run(
            {
                Input.ACTION: "Acknowledge in Progress",
                Input.CASE_ID: "23456",
            }
        )

        expected = {
            "response": {
                "actionId": "45c9821a-331b-a097-3851-c28900a15572",
                "statusUrl": "https://api.abnormalplatform.com/v1/cases/23456/actions/45c9821a-331b-a097-3851-c28900a15572",
            }
        }

        self.assertEqual(actual, expected)

    @patch("requests.request", side_effect=Util.mocked_requests)
    def test_manage_case_resolved(self, mock_post):
        actual = self.action.run(
            {
                Input.ACTION: "Acknowledge Resolved",
                Input.CASE_ID: "45678",
            }
        )

        expected = {
            "response": {
                "actionId": "c2097726-3855-ba25-3ca1-2280b2c17bb2",
                "statusUrl": "https://api.abnormalplatform.com/v1/cases/45678/actions/c2097726-3855-ba25-3ca1-2280b2c17bb2",
            }
        }

        self.assertEqual(actual, expected)

    @patch("requests.request", side_effect=Util.mocked_requests)
    def test_manage_case_invalid_case_id(self, mock_post):
        with self.assertRaises(PluginException) as e:
            self.action.run(
                {
                    Input.ACTION: "Acknowledge Resolved",
                    Input.CASE_ID: "56789",
                }
            )
        self.assertEqual(
            e.exception.cause,
            "Invalid or unreachable endpoint provided.",
        )
        self.assertEqual(
            e.exception.assistance,
            "Verify the endpoint/URL/hostname configured in your plugin connection is correct.",
        )
        self.assertEqual(e.exception.data, 'Response was: {"message": "Case action does not exist"}')
