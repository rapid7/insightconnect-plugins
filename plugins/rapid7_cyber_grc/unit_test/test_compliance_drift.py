"""Covers the Monitor Compliance Drift trigger.

Cyber GRC publishes a score, not a change, so the trigger's whole job is to remember
the last score it saw per framework and work out what moved. These cases drive it one
poll at a time against a changing set of metrics, which is what exercises that memory.
"""

import os
import sys

sys.path.append(os.path.abspath("../"))

import json
import tempfile
from pathlib import Path
from unittest import TestCase
from unittest.mock import MagicMock, patch

from icon_rapid7_cyber_grc.triggers import MonitorComplianceDrift
from util import CONTROL_SETS, MockResponse, Util, collection, metrics_record

CACHE_FILE = "monitor_compliance_drift_cache.json"

# The two live, scored frameworks from the shared control sets: 1 is SOC 2, 2 is
# ISO 27001. Control set 3 is archived and 4 has never been scored.
SOC2, ISO = 1, 2


class StopPolling(Exception):
    """Raised from the patched sleep so run() returns after a single poll."""


def one_poll(_seconds):
    raise StopPolling()


def serve(scores: dict, status: int = 200):
    """A request mock answering with the given {control set ID: compliance} scores."""

    def handler(_method, url, **kwargs):
        if status != 200:
            return MockResponse(status, {"error": {"message": "unavailable"}})
        if "ControlSetMetrics" in url:
            # The scores are asked for one framework at a time, so a framework this case
            # gave no score for has never been scored and answers with nothing.
            wanted = ((kwargs.get("params") or {}).get("$filter") or "").replace("controlSetID eq ", "")
            rows = [
                metrics_record(set_id, compliance, 50.0, compliance / 2, f"2026-09-0{set_id}T00:00:00.000Z")
                for set_id, compliance in scores.items()
                if not wanted or str(set_id) == wanted
            ]
            return MockResponse(200, collection(rows))
        return MockResponse(200, collection(CONTROL_SETS))

    return handler


@patch("time.sleep", side_effect=one_poll)
class TestMonitorComplianceDrift(TestCase):
    def setUp(self):
        self.cache_dir = tempfile.TemporaryDirectory()
        self.trigger = Util.default_connector(MonitorComplianceDrift())
        self.trigger.cache_path = Path(self.cache_dir.name) / CACHE_FILE
        self.trigger.send = MagicMock()

    def tearDown(self):
        self.cache_dir.cleanup()

    def poll(self, scores, status=200, **overrides):
        """Run one poll against the given scores and return what was emitted."""
        params = {"control_set_id": 0, "drop_threshold": 5, "minimum_compliance": 0, "interval": 3600}
        params.update(overrides)
        with patch("requests.Session.request", side_effect=serve(scores, status)):
            with self.assertRaises(StopPolling):
                self.trigger.run(params)
        if not self.trigger.send.called:
            return []
        emitted = self.trigger.send.call_args[0][0]
        self.trigger.send.reset_mock()
        return emitted["drifts"]

    def test_the_first_poll_only_records_the_baseline(self, _sleep):
        self.assertEqual(self.poll({SOC2: 80.0, ISO: 60.0}), [])

    def test_the_baseline_is_stored_for_the_next_poll(self, _sleep):
        self.poll({SOC2: 80.0, ISO: 60.0})

        self.assertEqual(
            json.loads(self.trigger.cache_path.read_text()),
            {
                "1": {"compliance": 80.0, "automated_controls_percentage": 40.0},
                "2": {"compliance": 60.0, "automated_controls_percentage": 30.0},
            },
        )

    def test_a_fall_past_the_threshold_is_reported(self, _sleep):
        self.poll({SOC2: 95.0})
        drifts = self.poll({SOC2: 70.0})

        self.assertEqual(len(drifts), 1)
        self.assertEqual(drifts[0]["control_set_id"], SOC2)
        self.assertEqual(drifts[0]["name"], "SOC 2")
        self.assertEqual(drifts[0]["reason"], "Drop")
        self.assertEqual(drifts[0]["previous_compliance"], 95.0)
        self.assertEqual(drifts[0]["current_compliance"], 70.0)
        self.assertEqual(drifts[0]["compliance_change"], -25.0)

    def test_the_automated_controls_percentage_is_reported_alongside(self, _sleep):
        self.poll({SOC2: 95.0})
        drifts = self.poll({SOC2: 70.0})

        self.assertEqual(drifts[0]["previous_automated_controls_percentage"], 47.5)
        self.assertEqual(drifts[0]["current_automated_controls_percentage"], 35.0)

    def test_a_fall_short_of_the_threshold_is_not_reported(self, _sleep):
        self.poll({SOC2: 95.0})

        self.assertEqual(self.poll({SOC2: 91.0}), [])

    def test_a_zero_threshold_reports_every_fall(self, _sleep):
        self.poll({SOC2: 95.0}, drop_threshold=0)

        self.assertEqual(len(self.poll({SOC2: 94.9}, drop_threshold=0)), 1)

    def test_a_rise_is_not_reported(self, _sleep):
        self.poll({SOC2: 60.0})

        self.assertEqual(self.poll({SOC2: 90.0}), [])

    def test_an_unchanged_score_is_not_reported(self, _sleep):
        self.poll({SOC2: 60.0})

        self.assertEqual(self.poll({SOC2: 60.0}), [])

    def test_the_floor_reports_a_failing_framework_on_the_first_poll(self, _sleep):
        drifts = self.poll({SOC2: 95.0, ISO: 60.0}, minimum_compliance=80)

        self.assertEqual([drift["control_set_id"] for drift in drifts], [ISO])
        self.assertEqual(drifts[0]["reason"], "Below Minimum")

    def test_a_framework_parked_below_the_floor_is_only_reported_once(self, _sleep):
        self.poll({ISO: 60.0}, minimum_compliance=80)

        self.assertEqual(self.poll({ISO: 60.0}, minimum_compliance=80), [])

    def test_crossing_under_the_floor_is_reported(self, _sleep):
        # A three point fall is short of the five point threshold, so the floor is the
        # only thing that can report this one.
        self.poll({SOC2: 82.0}, minimum_compliance=80)
        drifts = self.poll({SOC2: 79.0}, minimum_compliance=80)

        self.assertEqual(drifts[0]["reason"], "Below Minimum")
        self.assertEqual(drifts[0]["compliance_change"], -3.0)

    def test_a_fall_that_also_breaches_the_floor_is_reported_as_a_drop(self, _sleep):
        self.poll({SOC2: 95.0}, minimum_compliance=80)

        self.assertEqual(self.poll({SOC2: 70.0}, minimum_compliance=80)[0]["reason"], "Drop")

    def test_no_floor_reports_nothing_on_the_first_poll(self, _sleep):
        self.assertEqual(self.poll({SOC2: 1.0, ISO: 2.0}), [])

    def test_the_worst_fall_is_reported_first(self, _sleep):
        self.poll({SOC2: 90.0, ISO: 90.0})
        drifts = self.poll({SOC2: 80.0, ISO: 50.0})

        self.assertEqual([drift["control_set_id"] for drift in drifts], [ISO, SOC2])

    def test_an_archived_framework_is_not_watched(self, _sleep):
        self.poll({SOC2: 90.0, 3: 90.0})
        drifts = self.poll({SOC2: 40.0, 3: 10.0})

        self.assertEqual([drift["control_set_id"] for drift in drifts], [SOC2])

    def test_a_named_framework_is_watched_whatever_its_state(self, _sleep):
        self.poll({3: 90.0}, control_set_id=3)
        drifts = self.poll({3: 10.0}, control_set_id=3)

        self.assertEqual(drifts[0]["name"], "PCI DSS")

    def test_a_failed_poll_is_retried_rather_than_raised(self, _sleep):
        self.assertEqual(self.poll({SOC2: 90.0}, status=500), [])
        self.assertFalse(self.trigger.cache_path.exists())


class TestCacheLocation(TestCase):
    """Where the trigger keeps the previous scores.

    Scores in a temporary directory are lost when the container is rescheduled, and the
    first poll after that has no baseline to measure a fall against, so the persistent
    cache directory the Dockerfile creates is preferred whenever it is writable.
    """

    CACHE_DIR = "icon_rapid7_cyber_grc.triggers.monitor_compliance_drift.trigger.CACHE_DIR"

    def test_the_plugin_cache_directory_is_used_when_it_exists(self):
        with tempfile.TemporaryDirectory() as persistent:
            with patch(self.CACHE_DIR, Path(persistent)):
                trigger = MonitorComplianceDrift()

            self.assertEqual(trigger.cache_path, Path(persistent) / CACHE_FILE)

    def test_a_temporary_directory_is_used_when_the_cache_directory_is_absent(self):
        with patch(self.CACHE_DIR, Path("/no-such-plugin-cache-directory")):
            trigger = MonitorComplianceDrift()

        self.assertEqual(trigger.cache_path, Path(tempfile.gettempdir()) / CACHE_FILE)
