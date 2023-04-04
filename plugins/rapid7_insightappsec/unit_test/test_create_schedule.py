import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_rapid7_insightappsec.actions.create_schedule import CreateSchedule
from unit_test.util import Util
from unittest.mock import patch
from parameterized import parameterized
from insightconnect_plugin_runtime.exceptions import PluginException


@patch("requests.sessions.Session.post", side_effect=Util.mock_request)
class TestCreateSchedule(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(CreateSchedule())

    @parameterized.expand(
        [
            [
                "enabled",
                Util.read_file_to_dict("inputs/create_schedule_enabled.json.inp"),
                Util.read_file_to_dict("expected/success.json.exp"),
            ],
            [
                "disabled",
                Util.read_file_to_dict("inputs/create_schedule_disabled.json.inp"),
                Util.read_file_to_dict("expected/success.json.exp"),
            ],
            [
                "daily",
                Util.read_file_to_dict("inputs/create_schedule_daily.json.inp"),
                Util.read_file_to_dict("expected/success.json.exp"),
            ],
            [
                "weekly",
                Util.read_file_to_dict("inputs/create_schedule_weekly.json.inp"),
                Util.read_file_to_dict("expected/success.json.exp"),
            ],
            [
                "monthly",
                Util.read_file_to_dict("inputs/create_schedule_monthly.json.inp"),
                Util.read_file_to_dict("expected/success.json.exp"),
            ],
            [
                "recurrence_rule",
                Util.read_file_to_dict("inputs/create_schedule_recurrence_rule.json.inp"),
                Util.read_file_to_dict("expected/success.json.exp"),
            ],
            [
                "recurrence_rule2",
                Util.read_file_to_dict("inputs/create_schedule_recurrence_rule2.json.inp"),
                Util.read_file_to_dict("expected/success.json.exp"),
            ],
        ]
    )
    def test_create_schedule(self, mock_request, test_name, input_params, expected):
        actual = self.action.run(input_params)
        self.assertEqual(actual, expected)

    @parameterized.expand(
        [
            [
                "without_frequency_and_recurrence_rule",
                Util.read_file_to_dict("inputs/create_schedule_without_frequency_and_recurrence_rule.json.inp"),
                "Frequency and recurrence rule are not provided.",
                "Please provide the frequency or recurrence rule and try again.",
            ]
        ]
    )
    def test_create_schedule_bad(self, mock_request, test_name, input_parameters, cause, assistance):
        with self.assertRaises(PluginException) as error:
            self.action.run(input_parameters)
        self.assertEqual(error.exception.cause, cause)
        self.assertEqual(error.exception.assistance, assistance)
