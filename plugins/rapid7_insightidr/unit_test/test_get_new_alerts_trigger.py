import json
import os
import sys

sys.path.append(os.path.abspath("../"))

from datetime import UTC, datetime, timedelta
from typing import Any
from unittest import TestCase
from unittest.mock import MagicMock, patch

from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate
from komand_rapid7_insightidr.triggers.get_new_alerts.trigger import (
    MAX_NUMBER_OF_RETRIES,
    RETRY_DELAY_SECONDS,
    STATE_KEY,
    TIME_STATE_KEY,
    GetNewAlerts,
)
from komand_rapid7_insightidr.util.constants import TOTAL_SIZE
from parameterized import parameterized

CURRENT_TIME = datetime(2026, 10, 1, 2, 7, 0, tzinfo=UTC)
ALERTS_START = datetime(2026, 10, 1, 2, 0, 0, tzinfo=UTC)
REAL_MAKE_RESOURCE_REQUEST = GetNewAlerts.make_resource_request
NETWORK_ERROR = PluginException(cause="Error: Failed to retrieve alert results.", assistance="NameResolutionError")


class StopLoop(Exception):
    """Exception raised from mocked _save_state to break trigger's while loop"""


def _response(rrns: list[str]) -> dict[str, Any]:
    return {"alerts": [{"rrn": rrn} for rrn in rrns]}


def _created_at(number: int) -> str:
    return (ALERTS_START + timedelta(milliseconds=number)).isoformat(timespec="milliseconds").replace("+00:00", "Z")


def _alerts(start: int, stop: int) -> dict[str, Any]:
    return {"alerts": [{"rrn": f"rrn:{i}", "created_at": _created_at(i)} for i in range(start, stop)]}


@patch(
    "komand_rapid7_insightidr.triggers.get_new_alerts.trigger.GetNewAlerts.get_current_time",
    new=MagicMock(return_value=CURRENT_TIME),
)
@patch("komand_rapid7_insightidr.triggers.get_new_alerts.trigger.time.sleep")
@patch("komand_rapid7_insightidr.triggers.get_new_alerts.trigger.GetNewAlerts.make_resource_request")
class TestGetNewAlertsTrigger(TestCase):
    def setUp(self) -> None:
        self.trigger = GetNewAlerts()
        self.trigger.connection = MagicMock()
        self.trigger.logger = MagicMock()
        self.trigger.send = MagicMock()
        self.trigger._save_state = MagicMock(side_effect=StopLoop)
        self.trigger.state_file = "/workspace/cache/trigger_id.json"
        self.trigger.state = {}
        self.params = {"frequency": 15}

    @parameterized.expand(
        [
            ["first run sends nothing", {}, []],
            [
                "restart sends only new alerts",
                {STATE_KEY: ["rrn:1"], TIME_STATE_KEY: CURRENT_TIME.isoformat()},
                ["rrn:2"],
            ],
        ]
    )
    def test_deduplication(
        self,
        mock_request: MagicMock,
        _mock_sleep: MagicMock,
        _name: str,
        state: dict[str, Any],
        expected_sent: list[str],
    ) -> None:
        # Set up mock and run trigger
        self.trigger.state = state
        mock_request.return_value = _response(["rrn:1", "rrn:2"])

        # This is a little awkward, but we need to stop the trigger after one run to inspect its behavior
        with self.assertRaises(StopLoop):
            self.trigger.run(self.params)

        # Verify results and validate outputs via JSON schema
        sent = [call.args[0] for call in self.trigger.send.call_args_list]
        for output in sent:
            validate(output, self.trigger.output.schema)

        # Verify that only new alerts were sent
        self.assertEqual([output["alert"]["rrn"] for output in sent], expected_sent)
        self.assertEqual(set(self.trigger.state[STATE_KEY]), {"rrn:1", "rrn:2"})
        self.assertEqual(self.trigger.state[TIME_STATE_KEY], CURRENT_TIME.isoformat())

    @parameterized.expand(
        [
            [
                "consecutive polls send only new alerts",
                {},
                [["rrn:1"], ["rrn:1", "rrn:2"], ["rrn:1", "rrn:2", "rrn:3"]],
                ["rrn:2", "rrn:3"],
                [["rrn:1"], ["rrn:1", "rrn:2"], ["rrn:1", "rrn:2", "rrn:3"]],
            ],
            [
                "alerts leaving the window are dropped from state",
                {},
                [["rrn:1", "rrn:2"], ["rrn:2", "rrn:3"], ["rrn:3"]],
                ["rrn:3"],
                [["rrn:1", "rrn:2"], ["rrn:2", "rrn:3"], ["rrn:3"]],
            ],
            [
                "alert re-entering the window is sent again",
                {},
                [["rrn:1", "rrn:2"], ["rrn:2"], ["rrn:1", "rrn:2"]],
                ["rrn:1"],
                [["rrn:1", "rrn:2"], ["rrn:2"], ["rrn:1", "rrn:2"]],
            ],
            [
                "failed poll keeps previous state",
                {},
                [["rrn:1"], NETWORK_ERROR, ["rrn:1", "rrn:2"]],
                ["rrn:2"],
                [["rrn:1"], ["rrn:1", "rrn:2"]],
            ],
            [
                "duplicate RRN within one poll is sent once",
                {},
                [["rrn:1"], ["rrn:1", "rrn:2", "rrn:2"]],
                ["rrn:2"],
                [["rrn:1"], ["rrn:1", "rrn:2"]],
            ],
            [
                "restart resumes dedupe from saved RRNs",
                {STATE_KEY: ["rrn:1"], TIME_STATE_KEY: CURRENT_TIME.isoformat()},
                [["rrn:1", "rrn:2"], ["rrn:2", "rrn:3"]],
                ["rrn:2", "rrn:3"],
                [["rrn:1", "rrn:2"], ["rrn:2", "rrn:3"]],
            ],
        ]
    )
    def test_dedupe_across_polls(
        self,
        mock_request: MagicMock,
        _mock_sleep: MagicMock,
        _name: str,
        initial_state: dict[str, Any],
        responses: list[list[str] | PluginException],
        expected_sent: list[str],
        expected_states: list[list[str]],
    ) -> None:
        # Set up mock responses (an exception simulates a failed poll)
        self.trigger.state = dict(initial_state)
        mock_request.side_effect = [
            response if isinstance(response, Exception) else _response(response) for response in responses
        ]

        # Record the saved RRNs after every successful poll and stop the trigger after the last expected one
        saved_states = []

        # This is a little awkward, but we need to stop the trigger after the last expected state change
        def save_state() -> None:
            saved_states.append(sorted(self.trigger.state[STATE_KEY]))
            if len(saved_states) == len(expected_states):
                raise StopLoop

        # Set up the trigger to save state after each successful poll
        self.trigger._save_state = MagicMock(side_effect=save_state)

        # Stop the trigger after the last expected state change
        with self.assertRaises(StopLoop):
            self.trigger.run(self.params)

        # Verify outputs, the alerts sent over all polls, and the state saved after each poll
        sent = [call.args[0] for call in self.trigger.send.call_args_list]
        for output in sent:
            validate(output, self.trigger.output.schema)
        self.assertEqual([output["alert"]["rrn"] for output in sent], expected_sent)
        self.assertEqual(saved_states, expected_states)

    @parameterized.expand(
        [
            ["looks back 20 minutes from last poll", timedelta(hours=2), timedelta(hours=2, minutes=20)],
            ["look-back is capped at 24 hours", timedelta(days=3), timedelta(hours=24)],
        ]
    )
    def test_restart_start_time(
        self,
        mock_request: MagicMock,
        _mock_sleep: MagicMock,
        _name: str,
        last_poll_age: timedelta,
        expected_start_age: timedelta,
    ) -> None:
        # Set up mock to return empty results, then run trigger
        self.trigger.state = {STATE_KEY: [], TIME_STATE_KEY: (CURRENT_TIME - last_poll_age).isoformat()}
        mock_request.return_value = _response([])

        # This is a little awkward, but we need to stop the trigger after one run to inspect its behavior
        with self.assertRaises(StopLoop):
            self.trigger.run(self.params)

        # Verify the start of the search window
        start_time = mock_request.call_args.args[0]["search"]["start_time"]
        self.assertEqual(start_time, (CURRENT_TIME - expected_start_age).strftime("%Y-%m-%dT%H:%M:%SZ"))

        # Verify the skipped part of the window is logged only when the cap applies
        cap_log = (
            f"Get Alerts: last poll {(CURRENT_TIME - last_poll_age).isoformat()} is older than 24 hours, "
            f"alerts created before {(CURRENT_TIME - timedelta(hours=24)).isoformat()} are skipped"
        )
        logged = [call.args[0] for call in self.trigger.logger.info.call_args_list]
        self.assertEqual(cap_log in logged, last_poll_age - timedelta(minutes=20) > timedelta(hours=24))

    def test_network_error_is_retried(self, mock_request: MagicMock, mock_sleep: MagicMock) -> None:
        # Set up mock to simulate a network error, then run trigger
        self.trigger.state = {STATE_KEY: [], TIME_STATE_KEY: CURRENT_TIME.isoformat()}
        mock_request.side_effect = [NETWORK_ERROR, _response(["rrn:1"])]

        # Stopping the trigger after one run to inspect behavior
        with self.assertRaises(StopLoop):
            self.trigger.run(self.params)

        # Verify retry behavior (fixed retry delay, independent of the customer's frequency)
        mock_sleep.assert_called_once_with(RETRY_DELAY_SECONDS)
        self.trigger.send.assert_called_once()

    def test_walk_error_restarts_from_first_slice(self, mock_request: MagicMock, mock_sleep: MagicMock) -> None:
        # A full slice succeeds, the next slice fails, then the retry has to collect everything again from the start
        self.trigger.state = {STATE_KEY: [], TIME_STATE_KEY: CURRENT_TIME.isoformat()}
        full_slice = _alerts(0, TOTAL_SIZE)
        # The next slice starts inclusively at the last created_at, so it repeats the last alert of the full slice
        last_slice = _alerts(TOTAL_SIZE - 1, TOTAL_SIZE + 1)
        mock_request.side_effect = [full_slice, NETWORK_ERROR, full_slice, last_slice]

        # Stopping the trigger after one run to inspect behavior
        with self.assertRaises(StopLoop):
            self.trigger.run(self.params)

        # Verify the walk restarted from the beginning after the failure
        window_start = (CURRENT_TIME - timedelta(minutes=20)).strftime("%Y-%m-%dT%H:%M:%SZ")
        last_created_at = _created_at(TOTAL_SIZE - 1)

        # Verify the start times of the requests
        payloads = [call.args[0] for call in mock_request.call_args_list]
        for payload in payloads:
            self.assertEqual(payload["sorts"], [{"field_id": "alert.created_at", "order": "ASCENDING_NULLS_LAST"}])
        self.assertEqual(
            [payload["search"]["start_time"] for payload in payloads],
            [window_start, last_created_at, window_start, last_created_at],
        )

        # Verify that nothing was sent from the failed attempt and each alert was sent exactly once
        mock_sleep.assert_called_once_with(RETRY_DELAY_SECONDS)
        sent = [call.args[0] for call in self.trigger.send.call_args_list]
        for output in sent:
            validate(output, self.trigger.output.schema)
        self.assertEqual([output["alert"]["rrn"] for output in sent], [f"rrn:{i}" for i in range(TOTAL_SIZE + 1)])
        self.assertEqual(len(self.trigger.state[STATE_KEY]), TOTAL_SIZE + 1)

    def test_walk_skips_past_crowded_timestamp(self, mock_request: MagicMock, _mock_sleep: MagicMock) -> None:
        # A full slice where every alert has the same created_at can't move start_time, so the walk steps 1 ms past it
        self.trigger.state = {STATE_KEY: [], TIME_STATE_KEY: CURRENT_TIME.isoformat()}
        same_time = {"alerts": [{"rrn": f"rrn:{i}", "created_at": _created_at(0)} for i in range(TOTAL_SIZE)]}
        later = {"alerts": [{"rrn": "rrn:later", "created_at": _created_at(5)}]}
        mock_request.side_effect = [same_time, same_time, later]

        # Stopping the trigger after one run to inspect behavior
        with self.assertRaises(StopLoop):
            self.trigger.run(self.params)

        # Verify the walk moved past the crowded timestamp and warned about the skipped alerts
        start_times = [call.args[0].get("search", {}).get("start_time") for call in mock_request.call_args_list]
        self.assertEqual(start_times[1:], [_created_at(0), _created_at(1)])
        self.trigger.logger.info.assert_any_call(
            f"Get Alerts: more than {TOTAL_SIZE} alerts created at {_created_at(0)}, skipping the rest of them"
        )

        # Verify that the repeated alerts and the later alert were each sent once
        sent = [call.args[0].get("alert", {}).get("rrn") for call in self.trigger.send.call_args_list]
        self.assertEqual(sent, [f"rrn:{i}" for i in range(TOTAL_SIZE)] + ["rrn:later"])

    def test_walk_stops_when_start_time_does_not_advance(self, mock_request: MagicMock, _mock_sleep: MagicMock) -> None:
        # The API ignores the bumped start_time and keeps returning the same full slice, so the walk has to stop
        self.trigger.state = {STATE_KEY: [], TIME_STATE_KEY: CURRENT_TIME.isoformat()}
        # Bounded, so a broken stall guard fails the test instead of looping forever
        mock_request.side_effect = [
            {"alerts": [{"rrn": f"rrn:{i}", "created_at": _created_at(0)} for i in range(TOTAL_SIZE)]}
        ] * 3

        # Stopping the trigger after one run to inspect behavior
        with self.assertRaises(StopLoop):
            self.trigger.run(self.params)

        # Verify the walk gave up after the bumped start_time didn't move the results
        window_start = (CURRENT_TIME - timedelta(minutes=20)).strftime("%Y-%m-%dT%H:%M:%SZ")
        start_times = [call.args[0].get("search", {}).get("start_time") for call in mock_request.call_args_list]
        self.assertEqual(start_times, [window_start, _created_at(0), _created_at(1)])
        self.trigger.logger.info.assert_any_call(
            f"Get Alerts: paging stalled at {_created_at(0)}, skipping the rest of the alerts"
        )

        # Verify that each alert was sent once
        sent = [call.args[0] for call in self.trigger.send.call_args_list]
        for output in sent:
            validate(output, self.trigger.output.schema)
        self.assertEqual(
            [output.get("alert", {}).get("rrn") for output in sent], [f"rrn:{i}" for i in range(TOTAL_SIZE)]
        )

    def test_persistent_error_raises_after_max_retries(self, mock_request: MagicMock, _mock_sleep: MagicMock) -> None:
        # Set up mock to simulate a persistent network error
        mock_request.side_effect = NETWORK_ERROR

        # Verify that the trigger raises an exception after max retries
        with self.assertRaises(PluginException) as context:
            self.trigger.run(self.params)

        # Verify exception details
        self.assertEqual(context.exception.cause, f"Failed to retrieve alerts after {MAX_NUMBER_OF_RETRIES} retries.")
        self.assertEqual(context.exception.data, str(NETWORK_ERROR))
        self.assertEqual(mock_request.call_count, MAX_NUMBER_OF_RETRIES + 1)

    def test_alert_without_rrn_is_skipped(self, mock_request: MagicMock, _mock_sleep: MagicMock) -> None:
        # If an alert doesn't have an RRN, it should be skipped
        self.trigger.state = {STATE_KEY: [], TIME_STATE_KEY: CURRENT_TIME.isoformat()}
        mock_request.return_value = {"alerts": [{"title": "No RRN"}, {"rrn": "rrn:1"}]}

        # Stop the trigger after one run to inspect behavior
        with self.assertRaises(StopLoop):
            self.trigger.run(self.params)

        # Verify that only the alert with an RRN was sent
        self.trigger.send.assert_called_once()
        self.assertEqual(self.trigger.state[STATE_KEY], ["rrn:1"])

    def test_stateless_trigger_does_not_save_state(self, mock_request: MagicMock, mock_sleep: MagicMock) -> None:
        # Without a trigger ID there is no state file, so the trigger keeps polling without saving state
        self.trigger.state_file = ""
        mock_request.return_value = _response(["rrn:1"])
        mock_sleep.side_effect = StopLoop

        # Stop the trigger after one run to inspect behavior
        with self.assertRaises(StopLoop):
            self.trigger.run(self.params)

        # Verify that the poll succeeded (frequency sleep, not the retry sleep) and state was not saved
        mock_sleep.assert_called_once_with(self.params.get("frequency"))
        self.trigger._save_state.assert_not_called()

    def test_walk_stops_when_full_page_has_no_created_at(self, mock_request: MagicMock, _mock_sleep: MagicMock) -> None:
        # Without a created_at on the last alert of a full page the walk can't move start_time, so it stops and logs
        self.trigger.state = {STATE_KEY: [], TIME_STATE_KEY: CURRENT_TIME.isoformat()}
        full_page = _alerts(0, TOTAL_SIZE)
        full_page.get("alerts")[-1].pop("created_at")
        mock_request.return_value = full_page

        # Stopping the trigger after one run to inspect behavior
        with self.assertRaises(StopLoop):
            self.trigger.run(self.params)

        # Verify a single request was made, the stop was logged and the page was sent
        self.assertEqual(mock_request.call_count, 1)
        self.trigger.logger.info.assert_any_call(
            "Get Alerts: last alert on a full page has no created_at, stopping paging"
        )
        self.assertEqual(self.trigger.send.call_count, TOTAL_SIZE)

    @patch("komand_rapid7_insightidr.triggers.get_new_alerts.trigger.ResourceHelper.resource_request")
    def test_request_sends_size_as_query_param(
        self, mock_resource_request: MagicMock, mock_request: MagicMock, _mock_sleep: MagicMock
    ) -> None:
        # The API ignores paging fields in the body, so size has to go as a query param and index must not be sent
        mock_resource_request.return_value = {"resource": json.dumps({"alerts": []})}
        mock_request.side_effect = lambda data: REAL_MAKE_RESOURCE_REQUEST(self.trigger, data)

        self.trigger.get_alerts({"search": {"start_time": "2026-10-01T01:47:00Z"}})

        # Verify the request shape that reaches the helper
        call = mock_resource_request.call_args
        payload = call.kwargs.get("payload", {})
        self.assertEqual(call.args[1], "post")
        self.assertEqual(call.kwargs.get("params"), {"size": TOTAL_SIZE})
        self.assertNotIn("index", payload)
        self.assertNotIn("index", payload.get("search", {}))
        self.assertEqual(payload.get("sorts"), [{"field_id": "alert.created_at", "order": "ASCENDING_NULLS_LAST"}])
