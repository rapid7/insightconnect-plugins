import os
import sys
from unittest import TestCase
from unittest.mock import MagicMock, patch
from datetime import datetime, UTC, timedelta

sys.path.append(os.path.abspath("../"))

from komand_rapid7_insightidr.triggers.get_new_investigations.trigger import (
    GetNewInvestigations,
    API_LATENCY_OVERLAP_MINUTES,
    INITIAL_LOOKBACK_MINUTES,
)
from komand_rapid7_insightidr.triggers.get_new_investigations.schema import Output
from parameterized import parameterized


class StopLoop(Exception):
    """Exception raised from mocked time.sleep to break trigger's while loop"""


@patch(
    "komand_rapid7_insightidr.triggers.get_new_investigations.trigger.GetNewInvestigations.get_current_time",
    return_value=datetime(2026, 8, 26, 12, 0, 0, tzinfo=UTC),
)
@patch("time.sleep", side_effect=StopLoop)
@patch("komand_rapid7_insightidr.triggers.get_new_investigations.trigger.GetNewInvestigations._call_search_api")
class TestGetNewInvestigationsTrigger(TestCase):
    def setUp(self) -> None:
        self.trigger = GetNewInvestigations()
        self.trigger.connection = MagicMock()
        self.trigger.logger = MagicMock()
        self.trigger.send = MagicMock()
        self.trigger._save_state = MagicMock()
        self.trigger.state = {}
        self.params = {"frequency": 15, "search": []}

    @parameterized.expand(
        [
            [
                "all new investigations",
                {},
                [
                    {"rrn": "rrn:investigation:1", "title": "Investigation 1"},
                    {"rrn": "rrn:investigation:2", "title": "Investigation 2"},
                ],
                2,
                {"rrn:investigation:1", "rrn:investigation:2"},
            ],
            [
                "all duplicate investigations",
                {"RRNs": ["rrn:investigation:1", "rrn:investigation:2"]},
                [
                    {"rrn": "rrn:investigation:1", "title": "Investigation 1"},
                    {"rrn": "rrn:investigation:2", "title": "Investigation 2"},
                ],
                0,
                {"rrn:investigation:1", "rrn:investigation:2"},
            ],
            [
                "mixed new and duplicate only sends the new investigations",
                {"RRNs": ["rrn:investigation:1"]},
                [
                    {"rrn": "rrn:investigation:1", "title": "Investigation 1"},
                    {"rrn": "rrn:investigation:2", "title": "Investigation 2"},
                    {"rrn": "rrn:investigation:3", "title": "Investigation 3"},
                ],
                2,
                {"rrn:investigation:1", "rrn:investigation:2", "rrn:investigation:3"},
            ],
            [
                "empty API response preserves state",
                {"RRNs": ["rrn:investigation:1", "rrn:investigation:2"]},
                [],
                0,
                {"rrn:investigation:1", "rrn:investigation:2"},
            ],
            [
                "investigation without rrn key missing are still sent",
                {},
                [
                    {"title": "Investigation without RRN", "status": "OPEN"},
                    {"rrn": None, "title": "Investigation with None RRN"},
                    {"rrn": "", "title": "Investigation with empty RRN"}
                ],
                3,
                set(),  # nothing to track for these
            ],
            [
                "duplicate rrn in same poll sends both - strange API quirk and we can't differentiate",
                {},
                [
                    {"rrn": "rrn:investigation:A", "title": "Investigation A first"},
                    {"rrn": "rrn:investigation:A", "title": "Investigation A second"},
                ],
                2,
                {"rrn:investigation:A"},  # state is a set so we only have the RRN once
            ],
        ]
    )
    def test_single_poll_deduplication(
        self,
        mock_call_search_api,
        _mock_sleep,
        _mock_get_current_time,
        _test_name,
        initial_state,
        api_response,
        expected_sends,
        expected_state,
    ):
        self.trigger.state = initial_state.copy()
        mock_call_search_api.return_value = {"data": api_response, "metadata": {"total_pages": 1}}

        # Compute expected RRNs: api_response - initial_state
        existing_rrns = set(initial_state.get("RRNs", []))
        expected_rrns = [inv.get("rrn") for inv in api_response if inv.get("rrn") and inv.get("rrn") not in existing_rrns]

        with self.assertRaises(StopLoop):
            self.trigger.run(self.params)

        self.assertEqual(self.trigger.send.call_count, expected_sends)

        # Verify correct RRNs were sent
        sent_rrns = []
        for call_args in self.trigger.send.call_args_list:
            if sent_rrn := call_args[0][0][Output.INVESTIGATION].get("rrn"):  # test data does not always hold an RRN
                sent_rrns.append(sent_rrn)

        self.assertEqual(sent_rrns, expected_rrns)

        actual_state = set(self.trigger.state.get("RRNs", []))
        self.assertEqual(actual_state, expected_state)
        self.trigger._save_state.assert_called_once()

    def test_multiple_poll_overlapping_window_deduplication(
        self, mock_call_search_api, mock_sleep, mock_get_current_time
    ):
        mock_sleep.side_effect = [None, None, StopLoop()]
        # get_current_time() called once initially + once per loop iteration
        mock_get_current_time.side_effect = [
            datetime(2026, 8, 26, 12, 0, 0, tzinfo=UTC),  # Initial last_poll_time
            datetime(2026, 8, 26, 12, 0, 0, tzinfo=UTC),  # Poll 1 current_time
            datetime(2026, 8, 26, 12, 0, 15, tzinfo=UTC),  # Poll 2 current_time
            datetime(2026, 8, 26, 12, 0, 30, tzinfo=UTC),  # Poll 3 current_time
        ]
        # Poll 1: API returns investigations A, B
        # Poll 2: Overlapping window returns B (duplicate) and C (new, late-indexed)
        # Poll 3: Overlapping window returns C (duplicate) and D (new)
        mock_call_search_api.side_effect = [
            {
                "data": [
                    {"rrn": "rrn:investigation:A", "title": "Investigation A"},
                    {"rrn": "rrn:investigation:B", "title": "Investigation B"},
                ],
                "metadata": {"total_pages": 1},
            },
            {
                "data": [
                    {"rrn": "rrn:investigation:B", "title": "Investigation B"},
                    {"rrn": "rrn:investigation:C", "title": "Investigation C"},
                ],
                "metadata": {"total_pages": 1},
            },
            {
                "data": [
                    {"rrn": "rrn:investigation:C", "title": "Investigation C"},
                    {"rrn": "rrn:investigation:D", "title": "Investigation D"},
                ],
                "metadata": {"total_pages": 1},
            },
        ]

        with self.assertRaises(StopLoop):
            self.trigger.run(self.params)

        # Verify total sends: A, B (poll 1) + C (poll 2) + D (poll 3) = 4
        self.assertEqual(self.trigger.send.call_count, 4)

        # Verify RRNs sent in order
        sent_rrns = [call_args[0][0][Output.INVESTIGATION]["rrn"] for call_args in self.trigger.send.call_args_list]
        self.assertEqual(
            sent_rrns, ["rrn:investigation:A", "rrn:investigation:B", "rrn:investigation:C", "rrn:investigation:D"]
        )

        # Verify final state contains only RRNs from last poll
        final_state = set(self.trigger.state.get("RRNs", []))
        self.assertEqual(final_state, {"rrn:investigation:C", "rrn:investigation:D"})

    def test_state_loaded_from_persistence_on_restart(self, mock_call_search_api, mock_sleep, mock_get_current_time):
        # Simulate persisted state from previous run
        self.trigger.state = {"RRNs": ["rrn:investigation:1", "rrn:investigation:2"]}

        # API returns investigations that were already processed
        mock_call_search_api.return_value = {
            "data": [
                {"rrn": "rrn:investigation:1", "title": "Investigation 1"},
                {"rrn": "rrn:investigation:2", "title": "Investigation 2"},
                {"rrn": "rrn:investigation:3", "title": "Investigation 3"},
            ],
            "metadata": {"total_pages": 1},
        }

        with self.assertRaises(StopLoop):
            self.trigger.run(self.params)

        self.trigger.send.assert_called_once()

        # State should now contain the new RRN
        actual_state = set(self.trigger.state.get("RRNs", []))
        self.assertEqual(actual_state, {"rrn:investigation:1", "rrn:investigation:2", "rrn:investigation:3"})

    def test_initial_lookback_window(self, mock_call_search_api, _mock_sleep, mock_get_current_time):
        mock_now = mock_get_current_time.return_value
        mock_call_search_api.return_value = {"data": [], "metadata": {"total_pages": 1}}

        with self.assertRaises(StopLoop):
            self.trigger.run(self.params)

        # Verify _call_search_api called with correct time window in payload
        call_args = mock_call_search_api.call_args
        payload = call_args[0][3]  # Fourth positional arg is payload (resource_helper, endpoint, method, payload)

        # First poll: start_time should be current_time - 10 minutes (INITIAL_LOOKBACK_MINUTES)
        expected_start = (mock_now - timedelta(minutes=INITIAL_LOOKBACK_MINUTES)).isoformat()
        # end_time should be current_time - 5 seconds
        expected_end = (mock_now - timedelta(seconds=5)).isoformat()

        self.assertEqual(payload["start_time"], expected_start)
        self.assertEqual(payload["end_time"], expected_end)

    def test_subsequent_poll_applies_5_minute_overlap(self, mock_call_search_api, mock_sleep, mock_get_current_time):
        """More in depth unit test of the dedupe logic that is being tested within the following unit test
        `test_multiple_poll_overlapping_window_deduplication` as this inspects the time params being sent"""
        # Define mock time progression
        initial_time = datetime(2026, 8, 26, 12, 0, 0, tzinfo=UTC)
        poll2_time = datetime(2026, 8, 26, 12, 0, 15, tzinfo=UTC)

        mock_sleep.side_effect = [None, StopLoop()]  # 2 calls before we end the trigger loop
        mock_get_current_time.side_effect = [
            initial_time,  # Initial last_poll_time - we set the baseline for the first poll
            initial_time,  # Poll 1 current_time - this is still the same time here
            poll2_time,  # Poll 2 current_time - we've applied a time.sleep() and on a second iteration
        ]
        mock_call_search_api.return_value = {"data": [], "metadata": {"total_pages": 1}}

        with self.assertRaises(StopLoop):
            self.trigger.run(self.params)

        self.assertEqual(mock_call_search_api.call_count, 2)

        # Extract payloads from both calls (4th positional arg)
        payload1 = mock_call_search_api.call_args_list[0][0][3]
        payload2 = mock_call_search_api.call_args_list[1][0][3]

        queried_start1 = datetime.fromisoformat(payload1["start_time"])
        queried_end1 = datetime.fromisoformat(payload1["end_time"])

        queried_start2 = datetime.fromisoformat(payload2["start_time"])
        queried_end2 = datetime.fromisoformat(payload2["end_time"])

        # expected first loop we do a lookback of now - 10 minutes
        exp_start1 = initial_time - timedelta(minutes=INITIAL_LOOKBACK_MINUTES)

        # expected end times, we take `get_current_time()` and minus 5 seconds for the API latency buffer
        exp_end1 = initial_time - timedelta(seconds=5)
        exp_end2 = poll2_time - timedelta(seconds=5)

        # this is the real test that on the second iteration we're applying the 5 minute overlap
        expected_start2 = exp_end1 - timedelta(minutes=API_LATENCY_OVERLAP_MINUTES)  # 5-minute overlap

        # start and end times should match for the first run
        self.assertEqual(queried_start1, exp_start1)
        self.assertEqual(queried_end1, exp_end1)

        # verify the second loop also has the correct start and end times, with the 5-minute overlap applied
        self.assertEqual(queried_start2, expected_start2)
        self.assertEqual(queried_end2, exp_end2)

        # verify overlap exists (the regression from 12.0.2 that we didn't overlap for allow for late indexing)
        self.assertLess(
            queried_start2, queried_end1, "Poll 2 must start before Poll 1 ends to catch late-indexed investigations"
        )

        # Verify overlap is exactly 5 minutes
        actual_overlap = queried_end1 - queried_start2
        self.assertEqual(actual_overlap, timedelta(minutes=API_LATENCY_OVERLAP_MINUTES))

    def test_api_latency_overlap_does_not_exceed_initial_lookback(
        self, _mock_call_search_api, _mock_sleep, _mock_get_current_time
    ):
        """Constraint check: API_LATENCY_OVERLAP_MINUTES must not exceed INITIAL_LOOKBACK_MINUTES
        to prevent expanding the window beyond the initial lookback on subsequent polls"""
        self.assertLessEqual(
            API_LATENCY_OVERLAP_MINUTES,
            INITIAL_LOOKBACK_MINUTES,
            "API_LATENCY_OVERLAP_MINUTES must not exceed INITIAL_LOOKBACK_MINUTES to prevent "
            "window expansion beyond initial lookback",
        )

    def test_pagination_fetches_all_pages(self, mock_call_search_api, _mock_sleep, _mock_get_current_time):
        test_page_count = 3
        mock_call_search_api.side_effect = [
            {"data": [{"rrn": "rrn:investigation:A", "title": "A"}], "metadata": {"total_pages": test_page_count}},
            {"data": [{"rrn": "rrn:investigation:B", "title": "B"}], "metadata": {"total_pages": test_page_count}},
            {"data": [{"rrn": "rrn:investigation:C", "title": "C"}], "metadata": {"total_pages": test_page_count}},
        ]

        with self.assertRaises(StopLoop):
            self.trigger.run(self.params)

        # API called 3 times
        self.assertEqual(mock_call_search_api.call_count, 3)

        # Verify index params: first call no index, subsequent calls have index
        # _call_search_api(request, endpoint, method, payload, params) - params is 5th arg (index 4)
        call_params = [call[0][4] for call in mock_call_search_api.call_args_list]
        self.assertNotIn("index", call_params[0])  # First call has no index
        self.assertEqual(call_params[1].get("index"), 1)
        self.assertEqual(call_params[2].get("index"), 2)

        # All 3 investigations sent
        self.assertEqual(self.trigger.send.call_count, test_page_count)
        sent_rrns = [call[0][0]["investigation"]["rrn"] for call in self.trigger.send.call_args_list]
        self.assertEqual(sent_rrns, ["rrn:investigation:A", "rrn:investigation:B", "rrn:investigation:C"])

    def test_restart_resumes_from_saved_poll_time(self, mock_call_search_api, _mock_sleep, mock_get_current_time):
        """On restart, trigger should resume from saved TIME_STATE_KEY instead of initial lookback"""
        saved_poll_time = datetime(2026, 8, 26, 11, 50, 0, tzinfo=UTC)
        current_time =  datetime(2026, 8, 26, 13, 0, 0, tzinfo=UTC)
        self.trigger.state = {
            "last_poll_time": saved_poll_time,
            "RRNs": ["rrn:investigation:old"],
        }

        mock_get_current_time.side_effect = [current_time]  # container restarted 1hr 10 mins since last poll

        mock_call_search_api.return_value = {
            "data": [{"rrn": "rrn:investigation:new", "title": "New Investigation"}],
            "metadata": {"total_pages": 1},
        }

        with self.assertRaises(StopLoop):
            self.trigger.run(self.params)

        # Verify restart log message
        log_calls = [call[0][0] for call in self.trigger.logger.info.call_args_list]
        self.assertTrue(any("Detected a container restart" in log for log in log_calls))
        self.assertFalse(any("Initial poll time set to" in log for log in log_calls))

        # Verify API call used saved time, not initial lookback
        payload = mock_call_search_api.call_args[0][3]
        self.assertEqual(payload["start_time"], saved_poll_time.isoformat())

        # we haven't lost the last poll and pulling the trigger forward losing investigations
        self.assertNotEquals(payload["start_time"], current_time.isoformat())

        # but our end time should be based on this - 5 seconds for API latency buffer
        self.assertEquals(payload["end_time"], (current_time - timedelta(seconds=5)).isoformat())

        # New investigation sent
        self.trigger.send.assert_called_once()
        sent_investigation = self.trigger.send.call_args[0][0]["investigation"]
        self.assertEqual(sent_investigation["rrn"], "rrn:investigation:new")
