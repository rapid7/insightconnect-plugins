import sys
import os

sys.path.append(os.path.abspath("../"))

from unittest import TestCase
from komand_okta.tasks.monitor_logs.task import MonitorLogs
from util import Util
from unittest.mock import patch, call
from parameterized import parameterized
from datetime import datetime, timezone


@patch(
    "komand_okta.tasks.monitor_logs.task.MonitorLogs.get_current_time",
    return_value=datetime(2023, 4, 28, 8, 34, 46, 123156, timezone.utc),
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
                Util.read_file_to_dict("expected/get_logs.json.exp"),
            ],
            [
                "with_state",
                Util.read_file_to_dict("inputs/monitor_logs_with_state.json.inp"),
                Util.read_file_to_dict("expected/get_logs.json.exp"),
            ],
            [
                "next_page",
                Util.read_file_to_dict("inputs/monitor_logs_next_page.json.inp"),
                Util.read_file_to_dict("expected/get_logs_next_page.json.exp"),
            ],
        ]
    )
    def test_monitor_logs(self, mock_request, mock_get_time, test_name, current_state, expected):
        actual, actual_state, has_more_pages, status_code, error = self.action.run(state=current_state)
        self.assertEqual(actual, expected.get("logs"))
        self.assertEqual(actual_state, expected.get("state"))
        self.assertEqual(has_more_pages, expected.get("has_more_pages"))

    @patch("logging.Logger.info")
    def test_monitor_logs_filters_events(self, mocked_logger, *mocks):
        # Test the filtering of events returned in a previous iteration. Workflow being tested:
        # 1. C2C executed and queried for events until 8am however the last event time was '2023-04-27T07:49:21.764Z'
        # 2. The next execution will use this timestamp, meaning the last event will be returned again from Okta.
        # 3. This duplicate event should be removed so that it is not returned to IDR again.

        current_state = {"last_collection_timestamp": "2023-04-27T07:49:21.764Z"}
        expected = Util.read_file_to_dict("expected/get_logs_filtered.json.exp")
        actual, actual_state, has_more_pages, status_code, error = self.action.run(state=current_state)
        self.assertEqual(actual_state, expected.get("state"))
        self.assertEqual(has_more_pages, expected.get("has_more_pages"))

        # make sure that the mocked response contained 2 log entries and that 1 is filtered out in `get_events`
        expected_logs = expected.get("logs")
        logger_call = call(
            "Returning 1 log event(s) from this iteration. Removed 1 event log(s) that should have "
            "been returned in previous iteration."
        )

        self.assertIn(logger_call, mocked_logger.call_args_list)
        self.assertEqual(len(actual), len(expected_logs))
        self.assertEqual(actual, expected_logs)

    @patch("logging.Logger.info")
    @patch("logging.Logger.warning")
    def test_monitor_logs_filters_single_event(self, mocked_warn_log, mocked_info_log, *mocks):
        # Test filtering when a single event is returned that was in the previous iteration.

        now = "2023-04-28T08:33:46.123Z"  # Mocked value of 'now' - 1 minute
        current_state = {"last_collection_timestamp": "2023-04-27T07:49:21.777Z"}  # TS of the event in mocked response
        expected = {"last_collection_timestamp": now}
        actual, actual_state, has_more_pages, status_code, error = self.action.run(state=current_state)
        self.assertEqual(actual_state, expected)
        self.assertEqual(has_more_pages, False)  # empty results so no next pages

        # make sure that the mocked response contained a single entry that we discarded and logged this happening
        logger_info_call = call("No new events found since last execution.")
        logger_warn_call = call(f'No published record to use as last timestamp, reverting to use "now" ({now})')

        self.assertIn(logger_info_call, mocked_info_log.call_args_list)
        self.assertIn(logger_warn_call, mocked_warn_log.call_args_list)
        self.assertEqual(actual, [])  # no events returned after filtering
