import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_okta.tasks.monitor_logs.task import MonitorLogs
from unit_test.util import Util
from unittest.mock import patch
from parameterized import parameterized
from datetime import datetime


@patch(
    "komand_okta.tasks.monitor_logs.task.MonitorLogs.get_current_time",
    return_value=datetime.strptime("2023-04-28T08:34:46", "%Y-%m-%dT%H:%M:%S"),
)
@patch("requests.request", side_effect=Util.mock_request)
class TestSendPush(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(MonitorLogs())

    @parameterized.expand(
        [
            [
                "without_state",
                Util.read_file_to_dict("inputs/monitor_logs_without_state.json.inp"),
                Util.read_file_to_dict("expected/get_logs.json.exp"),
            ],
            [
                "with_state",
                Util.read_file_to_dict("inputs/monitor_logs_with_state.json.inp"),
                Util.read_file_to_dict("expected/get_logs_all_pages.json.exp"),
            ],
        ]
    )
    def test_monitor_logs(self, mock_request, mock_get_time, test_name, current_state, expected):
        actual, actual_state = self.action.run(state=current_state)
        self.assertEqual(actual, expected.get("logs"))
        self.assertEqual(actual_state, expected.get("state"))
