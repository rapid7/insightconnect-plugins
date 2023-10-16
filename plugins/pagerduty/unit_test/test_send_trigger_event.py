import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase

from komand_pagerduty.actions.send_trigger_event import SendTriggerEvent
from unittest.mock import patch, MagicMock
from parameterized import parameterized
from util import Util
from insightconnect_plugin_runtime.exceptions import PluginException


@patch("requests.Session.request", side_effect=Util.mock_request)
class TestSendTriggerEvent(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(SendTriggerEvent())

    @parameterized.expand(
        [
            [
                "minimum_valid",
                Util.read_file_to_dict("inputs/trigger_event_minimum_fields.json.inp"),
                Util.read_file_to_dict("expected/trigger_event_minimum_fields.json.exp"),
            ],
            [
                "additional_fields_escalation_valid",
                Util.read_file_to_dict("inputs/trigger_event_additional_fields_escalation.json.inp"),
                Util.read_file_to_dict("expected/trigger_event_additional_fields_escalation.json.exp"),
            ],
            [
                "additional_fields_assignments_valid",
                Util.read_file_to_dict("inputs/trigger_event_additional_fields_assignments.json.inp"),
                Util.read_file_to_dict("expected/trigger_event_additional_fields_assignments.json.exp"),
            ],
        ]
    )
    def test_send_trigger_event(self, mock_request: MagicMock, test_name: str, input_params: dict, expected: dict):
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "missing_params_invalid",
                {},
                "Missing required paramaters",
                "Please ensure a valid 'email' and 'incident_id' is provided",
            ]
        ]
    )
    def test_missing_params_invalid(
        self, mock_request: MagicMock, test_name: str, input_params: dict, cause: str, assistance: str
    ):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_params)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)

    @parameterized.expand(
        [
            [
                "both_escalation_policy_and_assignments_invalid",
                Util.read_file_to_dict("inputs/send_trigger_both_esc_asg_invalid.json.inp"),
                "Invalid paramaters",
                "Invalid input only one of 'escalation_policy' or 'assignments' can be used at one time",
            ]
        ]
    )
    def test_missing_params_invalid(
        self, mock_request: MagicMock, test_name: str, input_params: dict, cause: str, assistance: str
    ):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_params)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
