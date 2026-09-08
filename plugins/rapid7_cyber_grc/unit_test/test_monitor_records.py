import os
import sys

sys.path.append(os.path.abspath("../"))

import tempfile
from datetime import datetime, timezone
from pathlib import Path
from unittest import TestCase
from unittest.mock import MagicMock, patch

from parameterized import parameterized

from icon_rapid7_cyber_grc.triggers import MonitorRecords
from util import MockResponse, Util, collection, created_record, record


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
            "event_type": "Any",
            "interval": 300,
            "filter": None,
            "expand": None,
        }
        params.update(overrides)
        return params

    @staticmethod
    def poll_params():
        """Query options of the first poll.

        The trigger opens by reading the server's clock, so that request comes before the
        first poll and is not what these assertions are about.
        """
        return next(call["params"] for call in Util.calls if "$count" not in call["url"])

    def run_trigger(self, **overrides):
        with self.assertRaises(StopPolling):
            self.trigger.run(self.params(**overrides))

    def test_the_first_poll_starts_from_now(self, mock_sleep, mock_request):
        # A trigger with no stored position reports what happens from the moment it
        # starts, rather than opening with a batch of history nobody asked for.
        self.run_trigger()

        sent_filter = self.poll_params()["$filter"]
        self.assertTrue(sent_filter.startswith("createdDate gt "))
        lower_bound = datetime.fromisoformat(sent_filter.split(" gt ")[1].split(" or ")[0].replace("Z", "+00:00"))
        self.assertLess(abs((lower_bound - datetime.now(timezone.utc)).total_seconds()), 60)

    def test_the_starting_position_is_measured_on_the_cyber_grc_clock(self, mock_sleep, mock_request):
        # The position is compared against timestamps Cyber GRC writes, so a container
        # clock running ahead of the server's would put it in the server's future and
        # pass over everything created in the difference between the two.
        def serve(method, url, **kwargs):
            Util.calls.append({"method": method, "url": url, **kwargs})
            if "$count" in url:
                return MockResponse(
                    200, text="7", headers={"Content-Type": "text/plain", "Date": "Wed, 01 Jul 2026 12:00:00 GMT"}
                )
            return MockResponse(200, collection([]))

        mock_request.side_effect = serve

        self.run_trigger()

        self.assertEqual(self.poll_params()["$filter"].split(" or ")[0], "createdDate gt 2026-07-01T12:00:00.000Z")

    def test_the_container_clock_is_used_when_cyber_grc_does_not_report_its_own(self, mock_sleep, mock_request):
        def serve(method, url, **kwargs):
            Util.calls.append({"method": method, "url": url, **kwargs})
            if "$count" in url:
                return MockResponse(200, text="7", headers={})
            return MockResponse(200, collection([]))

        mock_request.side_effect = serve
        self.trigger.logger = MagicMock()

        self.run_trigger()

        lower_bound = datetime.fromisoformat(
            self.poll_params()["$filter"].split(" or ")[0].split(" gt ")[1].replace("Z", "+00:00")
        )
        self.assertLess(abs((lower_bound - datetime.now(timezone.utc)).total_seconds()), 60)
        logged = [call[0][0] for call in self.trigger.logger.info.call_args_list]
        self.assertTrue(any("did not report its clock" in message for message in logged), logged)

    def test_the_clock_is_not_read_when_a_position_is_already_stored(self, mock_sleep, mock_request):
        # Resuming needs no clock: the stored position already says where to carry on.
        self.trigger.cache_path.write_text('{"Incidents:createdDate,modifiedDate": "2026-05-01T00:00:00.000Z"}')

        self.run_trigger()

        self.assertFalse([call for call in Util.calls if "$count" in call["url"]])

    def test_records_are_emitted_with_a_count(self, mock_sleep, mock_request):
        self.run_trigger()

        self.trigger.send.assert_called_once()
        emitted = self.trigger.send.call_args[0][0]
        self.assertEqual(emitted["count"], 2)
        self.assertEqual([item["id"] for item in emitted["records"]], [1, 2])

    def test_created_events_are_found_by_the_creation_timestamp(self, mock_sleep, mock_request):
        # createdDate never moves, so a record matches this query once and once only.
        self.run_trigger(event_type="Created")

        self.assertEqual(self.poll_params()["$orderby"], "createdDate asc")
        self.assertTrue(self.poll_params()["$filter"].startswith("createdDate gt "))

    def test_change_events_are_found_by_the_modification_timestamp(self, mock_sleep, mock_request):
        self.run_trigger(event_type="Updated")

        self.assertEqual(self.poll_params()["$orderby"], "modifiedDate asc")
        self.assertTrue(self.poll_params()["$filter"].startswith("modifiedDate gt "))

    def test_any_looks_at_both_timestamps(self, mock_sleep, mock_request):
        # A creation is only ever visible in createdDate, because the API leaves
        # modifiedDate null until something edits the record. Watching modifiedDate alone
        # would report every change and miss every creation.
        self.run_trigger(event_type="Any")

        sent_filter = self.poll_params()["$filter"]
        self.assertIn("createdDate gt ", sent_filter)
        self.assertIn(" or modifiedDate gt ", sent_filter)

    def test_any_emits_a_creation_that_carries_no_modification_timestamp(self, mock_sleep, mock_request):
        # The record shape a creation really arrives in. A null modifiedDate can never
        # satisfy "modifiedDate gt <position>", so watching that field alone left this
        # record out of the query entirely and Any never reported a new record at all.
        def only_when_creation_is_queried(*args, **kwargs):
            sent_filter = (kwargs.get("params") or {}).get("$filter", "")
            found = [created_record(1)] if "createdDate gt " in sent_filter else []
            return MockResponse(200, collection(found))

        mock_request.side_effect = only_when_creation_is_queried

        self.run_trigger(event_type="Any")

        emitted = self.trigger.send.call_args[0][0]
        self.assertEqual([item["id"] for item in emitted["records"]], [1])

    def test_a_creation_carrying_no_modification_timestamp_is_not_an_update(self, mock_sleep, mock_request):
        mock_request.side_effect = lambda *args, **kwargs: MockResponse(
            200, collection([created_record(1), record(2, "Changed")])
        )

        self.run_trigger(event_type="Updated")

        emitted = self.trigger.send.call_args[0][0]
        self.assertEqual([item["id"] for item in emitted["records"]], [2])

    def test_a_record_that_has_never_changed_is_not_an_update(self, mock_sleep, mock_request):
        # Creating a record sets both timestamps to the same instant, which is what tells
        # a creation apart from a change when only changes were asked for.
        created_only = dict(record(1), createdDate="2026-01-21T20:30:44.407Z")
        mock_request.side_effect = lambda *args, **kwargs: MockResponse(
            200, collection([created_only, record(2, "Changed")])
        )

        self.run_trigger(event_type="Updated")

        emitted = self.trigger.send.call_args[0][0]
        self.assertEqual([item["id"] for item in emitted["records"]], [2])
        self.assertEqual(emitted["count"], 1)

    def test_nothing_is_emitted_when_every_record_was_only_created(self, mock_sleep, mock_request):
        created_only = dict(record(1), createdDate="2026-01-21T20:30:44.407Z")
        mock_request.side_effect = lambda *args, **kwargs: MockResponse(200, collection([created_only]))

        self.run_trigger(event_type="Updated")

        self.trigger.send.assert_not_called()

    def test_a_discarded_record_does_not_come_back_on_the_next_poll(self, mock_sleep, mock_request):
        # The position has to advance past a record the Event Type discarded, or every
        # poll re-reads it forever.
        created_only = dict(record(1), createdDate="2026-01-21T20:30:44.407Z")
        mock_request.side_effect = lambda *args, **kwargs: MockResponse(200, collection([created_only]))

        self.run_trigger(event_type="Updated")

        self.assertIn("2026-01-21T20:30:44.408Z", self.trigger.cache_path.read_text())

    def test_a_record_missing_a_timestamp_is_emitted_rather_than_discarded(self, mock_sleep, mock_request):
        # Neither timestamp is guaranteed by the API, and losing a real change is worse
        # than emitting a creation the workflow can ignore.
        untimed = {key: value for key, value in record(1).items() if key != "createdDate"}
        mock_request.side_effect = lambda *args, **kwargs: MockResponse(200, collection([untimed]))

        self.run_trigger(event_type="Updated")

        self.trigger.send.assert_called_once()

    def test_the_position_is_kept_separately_for_each_event_type(self, mock_sleep, mock_request):
        # The two positions measure different fields, so resuming one from the other
        # would either replay records or skip them.
        self.run_trigger(event_type="Created")

        stored = self.trigger.cache_path.read_text()
        self.assertIn("Incidents:createdDate", stored)
        self.assertNotIn("createdDate,modifiedDate", stored)

    def test_a_user_filter_is_combined_with_the_timestamp_filter(self, mock_sleep, mock_request):
        self.run_trigger(filter="statusID eq 3")

        self.assertTrue(self.poll_params()["$filter"].endswith(") and (statusID eq 3)"))

    def test_a_user_filter_containing_or_cannot_escape_the_timestamp_filter(self, mock_sleep, mock_request):
        # Unparenthesised, "ts gt W and a eq 1 or b eq 2" binds as "(ts gt W and a eq 1)
        # or b eq 2", so records older than the position return on every single poll.
        self.run_trigger(filter="statusID eq 3 or statusID eq 4")

        sent_filter = self.poll_params()["$filter"]
        self.assertTrue(sent_filter.startswith("(createdDate gt "))
        self.assertTrue(sent_filter.endswith(") and (statusID eq 3 or statusID eq 4)"))

    def test_polling_continues_after_the_api_fails(self, mock_sleep, mock_request):
        # A trigger that lets an exception out stops polling for good, so a rate limit or
        # a brief API outage would silently take the workflow down.
        mock_request.side_effect = [
            # The clock read the trigger opens with, then the two polls under test.
            MockResponse(200, text="7"),
            MockResponse(429, {"error": "slow down"}),
            MockResponse(200, collection([record(1)])),
        ]
        mock_sleep.side_effect = stop_after(2)

        self.run_trigger()

        self.trigger.send.assert_called_once()

    def test_a_failed_poll_is_logged_with_the_reason(self, mock_sleep, mock_request):
        mock_request.side_effect = lambda *args, **kwargs: MockResponse(403, {"error": "denied"})
        self.trigger.logger = MagicMock()

        self.run_trigger()

        logged = self.trigger.logger.error.call_args[0][0]
        self.assertIn("Polling Incidents failed", logged)
        self.assertIn("Forbidden.", logged)

    def test_a_timestamp_without_an_offset_is_treated_as_utc(self, mock_sleep, mock_request):
        # Comparing a naive datetime with an aware one raises a TypeError, and reading a
        # naive value as local time would move the position by the orchestrator's offset.
        naive = dict(record(1), modifiedDate="2026-01-21T20:30:44.407")
        mock_request.side_effect = lambda *args, **kwargs: MockResponse(200, collection([naive, record(2)]))

        self.run_trigger()

        self.assertIn("2026-01-21T20:30:44.408Z", self.trigger.cache_path.read_text())

    def test_the_position_advances_past_the_newest_record(self, mock_sleep, mock_request):
        self.run_trigger()

        # The newest record in the fixture carries modifiedDate 2026-01-21T20:30:44.407Z,
        # so the next poll must resume from one millisecond later.
        self.assertIn("2026-01-21T20:30:44.408Z", self.trigger.cache_path.read_text())

    def test_a_stored_position_is_used_instead_of_starting_from_now(self, mock_sleep, mock_request):
        self.trigger.cache_path.write_text('{"Incidents:createdDate,modifiedDate": "2026-05-01T00:00:00.000Z"}')

        self.run_trigger()

        self.assertEqual(
            self.poll_params()["$filter"],
            "createdDate gt 2026-05-01T00:00:00.000Z or modifiedDate gt 2026-05-01T00:00:00.000Z",
        )

    def test_a_stored_position_for_another_record_type_is_ignored(self, mock_sleep, mock_request):
        self.trigger.cache_path.write_text('{"Risks:modifiedDate": "2026-05-01T00:00:00.000Z"}')

        self.run_trigger()

        self.assertNotIn("2026-05-01", self.poll_params()["$filter"])

    @parameterized.expand([["not_json", "not json"], ["not_an_object", "[]"], ["empty", ""]])
    def test_a_corrupt_cache_falls_back_to_starting_from_now(self, mock_sleep, mock_request, _name, contents):
        self.trigger.cache_path.write_text(contents)

        self.run_trigger()

        self.trigger.send.assert_called_once()
        self.assertIn("modifiedDate gt ", self.poll_params()["$filter"])

    def test_a_cache_that_is_not_an_object_is_replaced_rather_than_failing_the_poll(self, mock_sleep, mock_request):
        self.trigger.cache_path.write_text("[]")

        self.run_trigger()

        self.assertIn("Incidents:createdDate,modifiedDate", self.trigger.cache_path.read_text())

    def test_the_position_holds_when_a_timestamp_cannot_be_parsed(self, mock_sleep, mock_request):
        unparseable = dict(record(1), createdDate="last Monday", modifiedDate="last Tuesday")
        mock_request.side_effect = lambda *args, **kwargs: MockResponse(200, collection([unparseable]))

        self.run_trigger()

        self.trigger.send.assert_called_once()
        self.assertFalse(self.trigger.cache_path.exists())

    def test_polling_continues_when_the_position_cannot_be_written(self, mock_sleep, mock_request):
        # A lost position only costs duplicate records after a restart.
        self.trigger.cache_path = Path(self.cache_dir.name) / "no-such-directory" / "cache.json"
        self.trigger.logger = MagicMock()

        self.run_trigger()

        self.trigger.send.assert_called_once()
        self.assertIn("Could not persist", self.trigger.logger.warning.call_args[0][0])

    def test_nothing_is_emitted_when_no_records_changed(self, mock_sleep, mock_request):
        mock_request.side_effect = lambda *args, **kwargs: MockResponse(200, collection([]))

        self.run_trigger()

        self.trigger.send.assert_not_called()

    def test_the_position_holds_when_the_records_carry_no_timestamp(self, mock_sleep, mock_request):
        untimed = {key: value for key, value in record(1).items() if key not in ("createdDate", "modifiedDate")}
        mock_request.side_effect = lambda *args, **kwargs: MockResponse(200, collection([untimed]))

        self.run_trigger()

        self.trigger.send.assert_called_once()
        self.assertFalse(self.trigger.cache_path.exists())


class TestCacheLocation(TestCase):
    """Where the trigger keeps its position.

    A position in a temporary directory is lost when the container is rescheduled, which
    means the trigger silently skips whatever changed while it was away, so the
    persistent cache directory the Dockerfile creates is preferred whenever it is there
    to be written to.
    """

    CACHE_DIR = "icon_rapid7_cyber_grc.triggers.monitor_records.trigger.CACHE_DIR"

    def test_the_plugin_cache_directory_is_used_when_it_exists(self):
        with tempfile.TemporaryDirectory() as persistent:
            with patch(self.CACHE_DIR, Path(persistent)):
                trigger = MonitorRecords()

            self.assertEqual(trigger.cache_path, Path(persistent) / "monitor_records_cache.json")

    def test_a_temporary_directory_is_used_when_the_cache_directory_is_absent(self):
        with patch(self.CACHE_DIR, Path("/no-such-plugin-cache-directory")):
            trigger = MonitorRecords()

        self.assertEqual(trigger.cache_path, Path(tempfile.gettempdir()) / "monitor_records_cache.json")
