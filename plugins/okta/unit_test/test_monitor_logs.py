from unittest import TestCase
from komand_okta.tasks.monitor_logs.task import MonitorLogs
from util import Util
from unittest.mock import patch, call
from parameterized import parameterized
from datetime import datetime, timezone

import sys
import os

sys.path.append(os.path.abspath("../"))


@patch(
    "komand_okta.tasks.monitor_logs.task.MonitorLogs.get_current_time",
    return_value=datetime(2023, 4, 28, 8, 34, 46, 123156, timezone.utc),
)
@patch("requests.request", side_effect=Util.mock_request)
@patch("logging.Logger.warning")
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
            [
                "next_page_no_results",
                Util.read_file_to_dict("inputs/monitor_logs_next_page.json.inp"),
                Util.read_file_to_dict("expected/get_logs_next_empty.json.exp"),
            ],
            [
                "without_state_no_results",
                Util.read_file_to_dict("inputs/monitor_logs_without_state.json.inp"),
                Util.read_file_to_dict("expected/get_logs_empty_resp.json.exp"),
            ],
        ]
    )
    def test_monitor_logs(self, mocked_warn, mock_request, _mock_get_time, test_name, current_state, expected):
        # Tests and their workflow descriptions:
        # 1. without_state - first run, query from 24 hours ago until now and results returned.
        # 2. with_state - queries using the saved 'last_collection_timestamp' to pull new logs.
        # 3. next_page - state has `next_page_link` which returns more logs to parse.
        # 4. next_page_no_results -`next_page_link` but the output of this is no logs - we don't move the TS forward.
        # 5. without_state_no_results - first run but no results returned - save state as the 'since' parameter value

        if test_name in ["next_page_no_results", "without_state_no_results"]:
            mock_request.side_effect = Util.mock_empty_response

        actual, actual_state, has_more_pages, status_code, error = self.action.run(state=current_state)
        self.assertEqual(actual, expected.get("logs"))
        self.assertEqual(actual_state, expected.get("state"))
        self.assertEqual(has_more_pages, expected.get("has_more_pages"))

        # Check errors returned and logger warning only applied in tests 4 and 5.
        self.assertEqual(error, None)
        if mocked_warn.called:
            log_call = call(
                "No record to use as last timestamp, will not move checkpoint forward. "
                f"Keeping value of {expected.get('state').get('last_collection_timestamp')}"
            )
            self.assertIn(log_call, mocked_warn.call_args_list)

    @patch("logging.Logger.info")
    def test_monitor_logs_filters_events(self, mocked_logger, *_mocks):
        # Test the filtering of events returned in a previous iteration. Workflow being tested:
        # 1. C2C executed and queried for events until 8am however the last event time was '2023-04-27T08:49:21.764Z'
        # 2. The next execution will use this timestamp, meaning the last event will be returned again from Okta.
        # 3. This duplicate event should be removed so that it is not returned to IDR again.

        current_state = {"last_collection_timestamp": "2023-04-27T08:49:21.764Z"}
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
    def test_monitor_logs_filters_single_event(self, mocked_info_log, mocked_warn_log, *mocks):
        # Test filtering when a single event is returned that was in the previous iteration.

        # temp change mocked timestamp to be within the cutoff time without changing mocked response data.
        mocks[1].return_value = datetime(2023, 4, 27, 8, 45, 46, 123156, timezone.utc)
        now = "2023-04-28T08:33:46.123Z"  # Mocked value of 'now' - 1 minute
        current_state = {"last_collection_timestamp": "2023-04-27T07:49:21.777Z"}  # TS of the event in mocked response
        actual, actual_state, has_more_pages, status_code, error = self.action.run(state=current_state)
        self.assertEqual(actual_state, current_state)  # state has not changed because no new events.
        self.assertNotEqual(actual_state.get("last_collection_timestamp"), now)  # we have not moved the TS forward.
        self.assertEqual(has_more_pages, False)  # empty results so no next pages.

        # ensure sure that the mocked response contained a single entry that we discarded and logged this happening
        logger_info_call = call("No new events found since last execution.")
        logger_warn_call = call(
            f"No record to use as last timestamp, will not move checkpoint forward. "
            f'Keeping value of {current_state.get("last_collection_timestamp")}'
        )

        self.assertIn(logger_info_call, mocked_info_log.call_args_list)
        self.assertIn(logger_warn_call, mocked_warn_log.call_args_list)
        self.assertEqual(actual, [])  # no events returned after filtering

    @patch("logging.Logger.info")
    def test_monitor_logs_applies_cut_off(self, mocked_info_log, *_mocks):
        # Test the scenario that a customer has paused the collector for an extended amount of time to test when they
        # resume the task we should cut off, at a max 24 hours ago for since parameter.
        expected = Util.read_file_to_dict("expected/get_logs.json.exp")  # logs from last 24 hours

        paused_time = "2022-04-27T07:49:21.777Z"
        current_state = {"last_collection_timestamp": paused_time}  # Task has been paused for 1 year+
        actual, state, _has_more_pages, _status_code, _error = self.action.run(state=current_state)

        # Basic check that we match the same as a first test/run which returns logs from the last 24 hours
        self.assertEqual(actual, expected.get("logs"))
        self.assertEqual(state, expected.get("state"))

        # Check we called with the current parameters by looking at the info log
        logger = call(
            f"Saved state {paused_time} exceeds the cut off (24 hours). "
            f"Reverting to use time: 2023-04-27T08:33:46.123Z"
        )
        self.assertIn(logger, mocked_info_log.call_args_list)

    @patch("logging.Logger.info")
    def test_filter_on_pagination(self, mocked_info_log, *_mocks):
        # If we have made a call to Okta using the next_page_link state then we don't need to filter any events from
        # this response, as this can cause the loss of events that match the same timestamp but on the next page.

        logger = call("next_page value used to poll from Okta. Returning 1 event(s) from response.")
        first_ts = "2023-04-27T06:49:21.777Z"

        # Part one: call a normal next page workflow when we expect the TS to not exist in the response
        current_state = {"last_collection_timestamp": first_ts, "next_page_link": "https://example.com/nextLink?q=next"}
        actual, new_state, has_more_pages, _status_code, _error = self.action.run(state=current_state)
        self.assertEqual(1, len(actual))
        self.assertEqual(True, has_more_pages)
        self.assertIn(logger, mocked_info_log.call_args_list)

        # Part two: iterate again for the next page, we want to make sure the faked 'next' event with the same timestamp
        # in the previous run is not filtered out.
        mocked_info_log.call_args_list = []  # reset the call list
        self.assertNotEqual(first_ts, new_state["last_collection_timestamp"])  # we have moved TS forward...
        self.assertEqual(actual[0]["published"], new_state["last_collection_timestamp"])  # to the returned log TS
        new_logs, new_state_2, _has_more_pages, _status_code, _error = self.action.run(state=new_state)
        self.assertEqual(1, len(new_logs))
        self.assertEqual(new_state_2["last_collection_timestamp"], new_logs[0]["published"])
        self.assertIn(logger, mocked_info_log.call_args_list)
