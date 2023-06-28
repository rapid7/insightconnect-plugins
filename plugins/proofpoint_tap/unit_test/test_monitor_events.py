import sys
import os

from unittest.mock import patch
from komand_proofpoint_tap.tasks.monitor_events.task import MonitorEvents
from test_util import Util
from unittest import TestCase
from parameterized import parameterized
from datetime import datetime, timezone

sys.path.append(os.path.abspath("../"))


@patch(
    "komand_proofpoint_tap.tasks.monitor_events.task.MonitorEvents.get_current_time",
    return_value=datetime.strptime("2023-04-04T08:00:00", "%Y-%m-%dT%H:%M:%S").replace(tzinfo=timezone.utc),
)
@patch("komand_proofpoint_tap.tasks.monitor_events.task.MonitorEvents.SPLIT_SIZE", new=2)
@patch("requests.request", side_effect=Util.mocked_requests_get)
class TestMonitorEvents(TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.action = Util.default_connector(MonitorEvents())

    @parameterized.expand(
        [
            [
                "first_run",
                Util.read_file_to_dict("inputs/monitor_events_first_run.json.inp"),
                Util.read_file_to_dict("expected/monitor_events_first_run.json.exp"),
            ],
            [
                "next_page",
                Util.read_file_to_dict("inputs/monitor_events_next_page.json.inp"),
                Util.read_file_to_dict("expected/monitor_events_next_page.json.exp"),
            ],
            [
                "last_page",
                Util.read_file_to_dict("inputs/monitor_events_next_page.json.inp"),
                Util.read_file_to_dict("expected/monitor_events_next_page.json.exp"),
            ],
            [
                "subsequent_run",
                Util.read_file_to_dict("inputs/monitor_events_subsequent_run.json.inp"),
                Util.read_file_to_dict("expected/monitor_events_subsequent_run.json.exp"),
            ],
            [
                "duplicated_event",
                Util.read_file_to_dict("inputs/monitor_events_duplicated_event.json.inp"),
                Util.read_file_to_dict("expected/monitor_events_duplicated_event.json.exp"),
            ],
            [
                "bad_request",
                Util.read_file_to_dict("inputs/monitor_events_bad_request.json.inp"),
                Util.read_file_to_dict("expected/monitor_events_bad_request.json.exp"),
            ],
            [
                "server_error",
                Util.read_file_to_dict("inputs/monitor_events_server_error.json.inp"),
                Util.read_file_to_dict("expected/monitor_events_server_error.json.exp"),
            ],
        ]
    )
    def test_monitor_events(self, mock_request, mock_get_time, test_name, current_state, expected):
        actual, actual_state, has_more_pages = self.action.run(state=current_state)
        self.assertEqual(actual, expected.get("events"))
        self.assertEqual(actual_state, expected.get("state"))
