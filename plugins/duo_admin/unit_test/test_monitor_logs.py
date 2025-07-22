import sys
import os
from time import time

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
        cls.task = Util.default_connector(MonitorLogs())
        cls.custom_config = {"cutoff": {"date": "2023-04-30T08:34:46.000Z"}, "lookback": "2023-04-30T08:34:46.000Z"}

    @parameterized.expand(
        [
            [
                "without_state",
                Util.read_file_to_dict("inputs/monitor_logs_without_state.json.inp"),
                Util.read_file_to_dict("expected/monitor_logs.json.exp"),
                {
                    "filter_cutoff_auth_logs": {"date": "2023-04-30T08:34:46.000Z"},
                    "filter_cutoff_admin_logs": {"date": "2023-04-30T08:34:46.000Z"},
                    "filter_cutoff_trust_monitor_events_logs": {"date": "2023-04-30T08:34:46.000Z"},
                    "lookback": "2023-04-30T08:34:46.000Z",
                },
            ],
            [
                "with_rate_limit",
                Util.read_file_to_dict("inputs/monitor_logs_with_rate_limit.json.inp"),
                Util.read_file_to_dict("expected/monitor_logs_rate_limit.json.exp"),
                {},
            ],
            [
                "with_state",
                Util.read_file_to_dict("inputs/monitor_logs_with_state.json.inp"),
                Util.read_file_to_dict("expected/monitor_logs_2.json.exp"),
                {
                    "filter_cutoff_auth_logs": {"date": "2023-04-30T08:34:46.000Z"},
                    "filter_cutoff_admin_logs": {"date": "2023-04-30T08:34:46.000Z"},
                    "filter_cutoff_trust_monitor_events_logs": {"date": "2023-04-30T08:34:46.000Z"},
                    "lookback": "2023-04-30T08:34:46.000Z",
                },
            ],
            [
                "next_page",
                Util.read_file_to_dict("inputs/monitor_logs_next_page.json.inp"),
                Util.read_file_to_dict("expected/monitor_logs_3.json.exp"),
                {
                    "filter_cutoff_auth_logs": {"date": "2023-04-30T08:34:46.000Z"},
                    "filter_cutoff_admin_logs": {"date": "2023-04-30T08:34:46.000Z"},
                    "filter_cutoff_trust_monitor_events_logs": {"date": "2023-04-30T08:34:46.000Z"},
                    "lookback": "2023-04-30T08:34:46.000Z",
                },
            ],
            [
                "bad_request",
                Util.read_file_to_dict("inputs/monitor_logs_bad_request.json.inp"),
                Util.read_file_to_dict("expected/monitor_logs_bad_request.json.exp"),
                {
                    "filter_cutoff_auth_logs": {"date": "2023-04-30T08:34:46.000Z"},
                    "filter_cutoff_admin_logs": {"date": "2023-04-30T08:34:46.000Z"},
                    "filter_cutoff_trust_monitor_events_logs": {"date": "2023-04-30T08:34:46.000Z"},
                    "lookback": 72,
                },
            ],
            [
                "server_error",
                Util.read_file_to_dict("inputs/monitor_logs_server_error.json.inp"),
                Util.read_file_to_dict("expected/monitor_logs_server_error.json.exp"),
                {
                    "filter_cutoff_auth_logs": {"date": "2023-04-30T08:34:46.000Z"},
                    "filter_cutoff_admin_logs": {"date": "2023-04-30T08:34:46.000Z"},
                    "filter_cutoff_trust_monitor_events_logs": {"date": "2023-04-30T08:34:46.000Z"},
                    "lookback": 72,
                },
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
        actual, actual_state, has_more_pages, status_code, _ = self.task.run(state=current_state, custom_config=config)
        self.assertEqual(expected.get("logs"), actual)
        self.assertEqual(expected.get("state"), actual_state)
        self.assertEqual(expected.get("status_code"), status_code)

    def test_monitor_logs_with_rate_limit_whole_flow(
        self, mock_request, mock_request_instance, mock_get_headers, mock_get_time
    ):
        future_time_state = {"rate_limit_datetime": time() + 600}
        passed_time_state = {"rate_limit_datetime": time() - 600}

        actual, new_state, has_more_pages, status_code, _ = self.task.run(state=future_time_state, custom_config={})

        self.assertEqual(actual, [])
        self.assertEqual(future_time_state, new_state)
        self.assertEqual(has_more_pages, False)
        self.assertEqual(status_code, 429)

        actual_2, new_state_2, _, status_code_2, _ = self.task.run(state=passed_time_state, custom_config={})

        self.assertTrue(actual_2)
        self.assertTrue(new_state_2)
        self.assertEqual(status_code_2, 200)
