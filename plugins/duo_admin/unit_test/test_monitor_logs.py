import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_duo_admin.tasks.monitor_logs.task import MonitorLogs
from util import Util
from unittest.mock import patch
from parameterized import parameterized
from datetime import datetime, timezone


@patch(
    "komand_duo_admin.tasks.monitor_logs.task.MonitorLogs.get_current_time",
    return_value=datetime.strptime("2023-05-01T08:34:46", "%Y-%m-%dT%H:%M:%S").replace(tzinfo=timezone.utc),
)
@patch("requests.request", side_effect=Util.mock_request)
@patch("komand_duo_admin.util.api.isinstance", return_value=True)
@patch("komand_duo_admin.util.api.DuoAdminAPI.get_headers", return_value={})
class TestMonitorLogs(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(MonitorLogs())
        cls.custom_config = {"cutoff": {"date": "2023-04-30T08:34:46.000Z"}, "lookback": "2023-04-30T08:34:46.000Z"}

    @parameterized.expand(
        [
            [
                "without_state",
                Util.read_file_to_dict("inputs/monitor_logs_without_state.json.inp"),
                Util.read_file_to_dict("expected/monitor_logs.json.exp"),
                {"cutoff": {"date": "2023-04-30T08:34:46.000Z"}, "lookback": "2023-04-30T08:34:46.000Z"},
            ],
            [
                "with_state",
                Util.read_file_to_dict("inputs/monitor_logs_with_state.json.inp"),
                Util.read_file_to_dict("expected/monitor_logs_2.json.exp"),
                {"cutoff": {"date": "2023-04-30T08:34:46.000Z"}, "lookback": "2023-04-30T08:34:46.000Z"},
            ],
            [
                "next_page",
                Util.read_file_to_dict("inputs/monitor_logs_next_page.json.inp"),
                Util.read_file_to_dict("expected/monitor_logs_3.json.exp"),
                {"cutoff": {"date": "2023-04-30T08:34:46.000Z"}, "lookback": "2023-04-30T08:34:46.000Z"},
            ],
            [
                "bad_request",
                # TODO WORK OUT WHICH REQUEST SHOULD BE BAD and how to make it fail
                Util.read_file_to_dict("inputs/monitor_logs_bad_request.json.inp"),
                Util.read_file_to_dict("expected/monitor_logs_bad_request.json.exp"),
                {"cutoff": {"date": "2023-04-30T08:34:46.000Z"}, "lookback": 72},
            ],
            [
                "server_error",
                Util.read_file_to_dict("inputs/monitor_logs_server_error.json.inp"),
                Util.read_file_to_dict("expected/monitor_logs_server_error.json.exp"),
                {"cutoff": {"date": "2023-04-30T08:34:46.000Z"}, "lookback": "2023-03-30T08:34:46.000Z"},
            ],
        ]
    )
    def test_monitor_logs(
        self,
        mock_request,
        mock_request_instance,
        mock_get_headers,
        mock_get_time,
        test_name,
        current_state,
        expected,
        config,
    ):
        actual, actual_state, has_more_pages, status_code, _ = self.action.run(
            state=current_state, custom_config=config
        )
        self.assertEqual(actual, expected.get("logs"))
        self.assertEqual(actual_state, expected.get("state"))
        self.assertEqual(status_code, expected.get("status_code"))
