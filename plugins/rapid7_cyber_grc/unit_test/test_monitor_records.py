import os
import sys

sys.path.append(os.path.abspath("../"))

import tempfile
from datetime import datetime, timedelta, timezone
from pathlib import Path
from unittest import TestCase
from unittest.mock import MagicMock, patch

from icon_rapid7_cyber_grc.triggers import MonitorRecords
from util import MockResponse, Util, collection, record


class StopPolling(Exception):
    """Raised from the patched sleep so run() returns after a known number of polls."""


def stop_after(polls: int):
    remaining = {"count": polls}

    def sleeper(_seconds):
        remaining["count"] -= 1
        if remaining["count"] <= 0:
            raise StopPolling()

    return sleeper


@patch("requests.Session.request", side_effect=Util.mock_request)
@patch("time.sleep", side_effect=stop_after(1))
class TestMonitorRecords(TestCase):
    def setUp(self):
        Util.calls = []
        self.cache_dir = tempfile.TemporaryDirectory()
        self.trigger = Util.default_connector(MonitorRecords())
        self.trigger.cache_path = Path(self.cache_dir.name) / "monitor_records_cache.json"
        self.trigger.send = MagicMock()

    def tearDown(self):
        self.cache_dir.cleanup()

    def params(self, **overrides):
        params = {
            "record_type": "Incidents",
            "timestamp_field": "modifiedDate",
            "interval": 300,
            "first_run_lookback_minutes": 60,
            "filter": None,
            "expand": None,
        }
        params.update(overrides)
        return params

    def run_trigger(self, **overrides):
        with self.assertRaises(StopPolling):
            self.trigger.run(self.params(**overrides))

    def test_first_poll_looks_back_by_the_configured_window(self, mock_sleep, mock_request):
        self.run_trigger()

        sent_filter = Util.calls[0]["params"]["$filter"]
        self.assertTrue(sent_filter.startswith("modifiedDate gt "))
        lower_bound = datetime.fromisoformat(sent_filter.split(" gt ")[1].replace("Z", "+00:00"))
        expected = datetime.now(timezone.utc) - timedelta(minutes=60)
        self.assertLess(abs((lower_bound - expected).total_seconds()), 60)

    def test_records_are_emitted_with_a_count(self, mock_sleep, mock_request):
        self.run_trigger()

        self.trigger.send.assert_called_once()
        emitted = self.trigger.send.call_args[0][0]
        self.assertEqual(emitted["count"], 2)
        self.assertEqual([item["id"] for item in emitted["records"]], [1, 2])

    def test_records_are_ordered_by_the_watched_timestamp(self, mock_sleep, mock_request):
        self.run_trigger(timestamp_field="createdDate")

        self.assertEqual(Util.calls[0]["params"]["$orderby"], "createdDate asc")
        self.assertTrue(Util.calls[0]["params"]["$filter"].startswith("createdDate gt "))

    def test_a_user_filter_is_combined_with_the_timestamp_filter(self, mock_sleep, mock_request):
        self.run_trigger(filter="statusID eq 3")

        self.assertTrue(Util.calls[0]["params"]["$filter"].endswith(" and statusID eq 3"))

    def test_the_position_advances_past_the_newest_record(self, mock_sleep, mock_request):
        self.run_trigger()

        # The newest record in the fixture carries modifiedDate 2026-01-21T20:30:44.407Z,
        # so the next poll must resume from one millisecond later.
        self.assertIn("2026-01-21T20:30:44.408Z", self.trigger.cache_path.read_text())

    def test_a_stored_position_is_used_instead_of_the_lookback_window(self, mock_sleep, mock_request):
        self.trigger.cache_path.write_text('{"Incidents:modifiedDate": "2026-05-01T00:00:00.000Z"}')

        self.run_trigger()

        self.assertEqual(Util.calls[0]["params"]["$filter"], "modifiedDate gt 2026-05-01T00:00:00.000Z")

    def test_a_stored_position_for_another_record_type_is_ignored(self, mock_sleep, mock_request):
        self.trigger.cache_path.write_text('{"Risks:modifiedDate": "2026-05-01T00:00:00.000Z"}')

        self.run_trigger()

        self.assertNotIn("2026-05-01", Util.calls[0]["params"]["$filter"])

    def test_a_corrupt_cache_falls_back_to_the_lookback_window(self, mock_sleep, mock_request):
        self.trigger.cache_path.write_text("not json")

        self.run_trigger()

        self.trigger.send.assert_called_once()

    def test_nothing_is_emitted_when_no_records_changed(self, mock_sleep, mock_request):
        mock_request.side_effect = lambda *args, **kwargs: MockResponse(200, collection([]))

        self.run_trigger()

        self.trigger.send.assert_not_called()

    def test_the_position_holds_when_the_records_carry_no_timestamp(self, mock_sleep, mock_request):
        untimed = {key: value for key, value in record(1).items() if key != "modifiedDate"}
        mock_request.side_effect = lambda *args, **kwargs: MockResponse(200, collection([untimed]))

        self.run_trigger()

        self.trigger.send.assert_called_once()
        self.assertFalse(self.trigger.cache_path.exists())
