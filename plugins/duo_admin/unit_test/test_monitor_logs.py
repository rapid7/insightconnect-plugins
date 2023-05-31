import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_duo_admin.tasks.monitor_logs.task import MonitorLogs
from unit_test.util import Util
from unittest.mock import patch
from parameterized import parameterized
from datetime import datetime


@patch(
    "komand_duo_admin.tasks.monitor_logs.task.MonitorLogs.get_current_time",
    return_value=datetime.strptime("2023-05-01T08:34:46", "%Y-%m-%dT%H:%M:%S"),
)
@patch("requests.request", side_effect=Util.mock_request)
class TestMonitorLogs(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(MonitorLogs())

    @parameterized.expand(
        [
            [
                "without_state",
                Util.read_file_to_dict("inputs/monitor_logs_without_state.json.inp"),
                Util.read_file_to_dict("expected/monitor_logs.json.exp"),
            ],
            [
                "with_state",
                Util.read_file_to_dict("inputs/monitor_logs_with_state.json.inp"),
                Util.read_file_to_dict("expected/monitor_logs_2.json.exp"),
            ],
            [
                "bad_request",
                Util.read_file_to_dict("inputs/monitor_logs_bad_request.json.inp"),
                Util.read_file_to_dict("expected/monitor_logs_bad_request.json.exp"),
            ],
            [
                "server_error",
                Util.read_file_to_dict("inputs/monitor_logs_server_error.json.inp"),
                Util.read_file_to_dict("expected/monitor_logs_server_error.json.exp"),
            ],
        ]
    )
    def test_monitor_logs(self, mock_request, mock_get_time, test_name, current_state, expected):
        actual, actual_state, has_more_pages = self.action.run(state=current_state)
        self.assertEqual(actual, expected.get("logs"))
        self.assertEqual(actual_state, expected.get("state"))
