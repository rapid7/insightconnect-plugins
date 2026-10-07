import os
import sys

sys.path.append(os.path.abspath("../"))

from datetime import UTC, datetime, timedelta
from typing import Any
from unittest import TestCase
from unittest.mock import MagicMock, patch

from freezegun import freeze_time
from insightconnect_plugin_runtime.exceptions import PluginException
from jsonschema import validate
from komand_rapid7_insightidr.triggers.get_new_alerts.trigger import (
    MAX_NUMBER_OF_RETRIES,
    STATE_KEY,
    TIME_STATE_KEY,
    GetNewAlerts,
)
from parameterized import parameterized

CURRENT_TIME = datetime(2026, 10, 1, 2, 7, 0, tzinfo=UTC)
NETWORK_ERROR = PluginException(cause="Error: Failed to retrieve alert results.", assistance="NameResolutionError")


class StopLoop(Exception):
    """Exception raised from mocked _save_state to break trigger's while loop"""


def _response(rrns: list[str]) -> dict[str, Any]:
    return {"alerts": [{"rrn": rrn} for rrn in rrns], "metadata": {"total_items": len(rrns)}}


@freeze_time(CURRENT_TIME)
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

    def test_restart_looks_back_from_last_poll_time(self, mock_request: MagicMock, _mock_sleep: MagicMock) -> None:
        # Set up mock to return empty results, then run trigger
        last_poll_time = CURRENT_TIME - timedelta(hours=2)
        self.trigger.state = {STATE_KEY: [], TIME_STATE_KEY: last_poll_time.isoformat()}
        mock_request.return_value = _response([])

        # This is a little awkward, but we need to stop the trigger after one run to inspect its behavior
        with self.assertRaises(StopLoop):
            self.trigger.run(self.params)

        # Verify that the trigger looks back 20 minutes from the last poll time
        start_time = mock_request.call_args.args[0]["search"]["start_time"]
        self.assertEqual(start_time, (last_poll_time - timedelta(minutes=20)).strftime("%Y-%m-%dT%H:%M:%SZ"))

    def test_network_error_is_retried(self, mock_request: MagicMock, mock_sleep: MagicMock) -> None:
        # Set up mock to simulate a network error, then run trigger
        self.trigger.state = {STATE_KEY: [], TIME_STATE_KEY: CURRENT_TIME.isoformat()}
        mock_request.side_effect = [NETWORK_ERROR, _response(["rrn:1"])]

        # Stopping the trigger after one run to inspect behavior
        with self.assertRaises(StopLoop):
            self.trigger.run(self.params)

        # Verify retry behavior
        mock_sleep.assert_called_once_with(15)
        self.trigger.send.assert_called_once()

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

        # Verify that state was not saved
        self.trigger._save_state.assert_not_called()
