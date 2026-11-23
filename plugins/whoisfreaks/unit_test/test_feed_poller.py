import os
import sys

sys.path.append(os.path.abspath("../"))

import collections
import copy
import datetime
from unittest import TestCase
from unittest.mock import MagicMock

from insightconnect_plugin_runtime.exceptions import PluginException

from icon_whoisfreaks.util import constants, feed, feed_poller
from icon_whoisfreaks.util.errors import Kind, WhoisFreaksError
from icon_whoisfreaks.util.feed_poller import (
    FeedPoller,
    FeedSettings,
    build_settings,
    pick_next_date,
    selected_feeds,
)

LATEST = "2026-10-12"
THREAT_HEADER = ",".join(constants.THREAT_FEED_COLUMNS)
PHISHING = feed.threat_feed("phishing")
MALWARE = feed.threat_feed("malware")
GTLD = feed.nrd_feed("gtld", False)
CCTLD = feed.nrd_feed("cctld", False)


class FakeTrigger:
    """Stands in for the SDK trigger: records events and saved states, and runs on a simulated clock."""

    def __init__(self, state=None, state_file="/workspace/cache/trigger.json", budget=5000.0):
        self.logger = MagicMock()
        self.state = state if state is not None else {}
        self.state_file = state_file
        self.sent, self.saved = [], []
        self.clock, self.budget = 0.0, budget

    def send(self, event):
        self.sent.append(copy.deepcopy(event))

    def _save_state(self):
        self.saved.append(copy.deepcopy(self.state))

    @property
    def run_trigger(self):
        return self.clock < self.budget

    def sleep(self, seconds):
        self.clock += seconds

    def now(self):
        return self.clock

    @property
    def rows(self):
        return [row for event in self.sent for row in event["events"]]


class FakeFeedClient:
    """Serves synthetic pages the way the WhoisFreaks stream endpoints do. rows maps feed_id to {date: count}."""

    def __init__(self, rows, last_update=LATEST, available_from="2026-10-01"):
        self.rows = rows
        self.window = [available_from, last_update]
        self.errors = []
        self.page_calls = []
        self.status_calls = 0
        self.on_page = None

    def get_feed_status(self):
        self.status_calls += 1
        node = {"available_from": self.window[0], "last_update": self.window[1]}
        return {"newly": {"gtld": node, "cctld": node}, "threat_feed": {"phishing": node, "malware": node}}

    def get_feed_page(self, operation, path, params):
        definition = next(item for item in (PHISHING, MALWARE, GTLD, CCTLD) if item.path == path)
        self.page_calls.append(dict(params, feed=definition.feed_id))
        if self.on_page:
            self.on_page(params)
        for predicate, error in list(self.errors):
            if predicate(definition.feed_id, params, len(self.page_calls)):
                raise error
        return self._page(definition, params)

    def _page(self, definition, params):
        day, offset, limit = params["date"], params["offset"], params["limit"]
        total = self.rows.get(definition.feed_id, {}).get(day, 0)
        name = definition.feed_id.split(".")[1]
        domains = [f"d{index}-{day}-{name}.com" for index in range(offset, min(total, offset + limit))]
        if not definition.is_csv:
            # Past the end, the plain list repeats the last line of the previous page
            return "\n".join(domains) if domains else (f"d{total - 1}-{day}-{name}.com" if total else "")
        if not domains:
            return None
        rows = [
            f"{domain},{name},{'1.0' if index % 2 == 0 else '0.5'},,,t,f,f,,," for index, domain in enumerate(domains)
        ]
        return "\n".join([THREAT_HEADER] + rows)


def settings(batch_size=3, poll_minutes=60, start_date=None, catch_up=False):
    return FeedSettings(
        batch_size=batch_size,
        poll_interval_seconds=poll_minutes * 60,
        start_date=start_date,
        catch_up=catch_up,
        row_filter=lambda row, feed_id="": True,
    )


def error(kind):
    return WhoisFreaksError(kind, "Feed", 500)


def feed_state(trigger, definition=PHISHING):
    return trigger.state["feeds"][definition.identity]


def page_counts(trigger, key):
    return dict(collections.Counter(event[key] for event in trigger.sent for _ in event["events"]))


class TestFeedPoller(TestCase):
    def run_poller(self, client, trigger, feed_settings=None, feeds=(PHISHING,)):
        poller = FeedPoller(trigger, client, list(feeds), feed_settings or settings(), trigger.sleep, trigger.now)
        poller.run()
        return poller

    def assert_no_duplicates(self, trigger, key="domain"):
        counts = collections.Counter(row[key] for row in trigger.rows)
        self.assertEqual([], [domain for domain, count in counts.items() if count > 1])

    def test_ingests_a_date_once(self):
        client, trigger = FakeFeedClient({PHISHING.feed_id: {LATEST: 7}}), FakeTrigger(budget=3000)
        self.run_poller(client, trigger)
        self.assertEqual([3, 3, 1], [event["count"] for event in trigger.sent])
        self.assertEqual([(0, 3), (3, 6), (6, 7)], [(e["offset"], e["next_offset"]) for e in trigger.sent])
        self.assertEqual({"threat_feed.phishing"}, {event["feed"] for event in trigger.sent})
        self.assertEqual({LATEST}, {event["feed_date"] for event in trigger.sent})
        self.assertEqual(7, len(trigger.rows))
        self.assertEqual(LATEST, feed_state(trigger)["last_completed_date"])
        self.assertIsNone(feed_state(trigger)["current_date"])
        self.assertEqual(3, len(client.page_calls))
        self.assertEqual(1, client.status_calls)

    def test_exact_multiple_of_batch_size_emits_no_garbage(self):
        client, trigger = FakeFeedClient({PHISHING.feed_id: {LATEST: 6}}), FakeTrigger()
        self.run_poller(client, trigger)
        self.assertEqual(6, len(trigger.rows))
        self.assertTrue(all(row["domain"].startswith("d") for row in trigger.rows))

    def test_plain_feed_repeated_last_line_is_not_emitted(self):
        client, trigger = FakeFeedClient({GTLD.feed_id: {LATEST: 6}}), FakeTrigger()
        self.run_poller(client, trigger, feeds=(GTLD,))
        self.assertEqual(6, len(trigger.rows))
        self.assert_no_duplicates(trigger, "domain_name")
        self.assertEqual(LATEST, feed_state(trigger, GTLD)["last_completed_date"])

    def test_transient_error_keeps_offset(self):
        client, trigger = FakeFeedClient({PHISHING.feed_id: {LATEST: 7}}), FakeTrigger()
        client.errors.append((lambda feed_id, params, call: call == 2, error(Kind.SERVER_ERROR)))
        self.run_poller(client, trigger)
        self.assertEqual(7, len(trigger.rows))
        self.assert_no_duplicates(trigger)
        self.assertEqual([0, 3, 3, 6], [call["offset"] for call in client.page_calls])
        trigger.logger.error.assert_called_once()

    def test_recurring_rate_limit_still_completes(self):
        client, trigger = FakeFeedClient({PHISHING.feed_id: {LATEST: 30}}), FakeTrigger(budget=50000)
        client.errors.append((lambda feed_id, params, call: call % 3 == 0, error(Kind.RATE_LIMITED)))
        self.run_poller(client, trigger)
        self.assertEqual(30, len(trigger.rows))
        self.assert_no_duplicates(trigger)
        self.assertEqual(LATEST, feed_state(trigger)["last_completed_date"])

    def test_new_date_published_mid_ingest_does_not_drop_rows(self):
        client, trigger = FakeFeedClient({PHISHING.feed_id: {LATEST: 12, "2026-10-13": 12}}), FakeTrigger()

        def publish_next_date(params):
            if len(client.page_calls) == 2:
                client.window[1] = "2026-10-13"

        client.on_page = publish_next_date
        self.run_poller(client, trigger)
        self.assertEqual({LATEST: 12, "2026-10-13": 12}, page_counts(trigger, "feed_date"))
        self.assertEqual("2026-10-13", feed_state(trigger)["last_completed_date"])

    def test_restart_resumes_mid_date(self):
        client = FakeFeedClient({PHISHING.feed_id: {LATEST: 9}})
        first = FakeTrigger(budget=0.4)
        self.run_poller(client, first)
        self.assertEqual(LATEST, feed_state(first)["current_date"])
        second = FakeTrigger(state=copy.deepcopy(first.saved[-1]))
        self.run_poller(client, second)
        rows = first.rows + second.rows
        self.assertEqual(9, len(rows))
        self.assertEqual(9, len({row["domain"] for row in rows}))

    def test_restart_after_completion_does_not_replay(self):
        client = FakeFeedClient({PHISHING.feed_id: {LATEST: 4}})
        first = FakeTrigger()
        self.run_poller(client, first)
        second = FakeTrigger(state=copy.deepcopy(first.saved[-1]))
        self.run_poller(client, second)
        self.assertEqual([], second.sent)

    def test_start_date_then_latest(self):
        client = FakeFeedClient({PHISHING.feed_id: {"2026-10-05": 2, LATEST: 2}})
        trigger = FakeTrigger()
        self.run_poller(client, trigger, settings(start_date=datetime.date(2026, 10, 5)))
        self.assertEqual(["2026-10-05", LATEST], sorted({event["feed_date"] for event in trigger.sent}))

    def test_start_date_outside_window_uses_latest(self):
        client, trigger = FakeFeedClient({PHISHING.feed_id: {LATEST: 2}}), FakeTrigger()
        self.run_poller(client, trigger, settings(start_date=datetime.date(2010, 10, 10)))
        self.assertEqual({LATEST}, {event["feed_date"] for event in trigger.sent})
        self.assertIn("outside the feed availability window", str(trigger.logger.warning.call_args_list))

    def test_catch_up_ingests_every_missed_date(self):
        rows = {PHISHING.feed_id: {"2026-10-10": 1, "2026-10-11": 1, LATEST: 1}}
        progress = dict(feed_poller._fresh_feed_state(), last_completed_date="2026-10-09")
        state = {"version": 2, "feeds": {PHISHING.identity: progress}}
        client, trigger = FakeFeedClient(rows), FakeTrigger(state=state)
        self.run_poller(client, trigger, settings(catch_up=True))
        self.assertEqual(["2026-10-10", "2026-10-11", LATEST], [event["feed_date"] for event in trigger.sent])

    def test_empty_date_completes(self):
        client, trigger = FakeFeedClient({}), FakeTrigger()
        self.run_poller(client, trigger)
        self.assertEqual([], trigger.sent)
        self.assertEqual(LATEST, feed_state(trigger)["last_completed_date"])
        self.assertEqual(1, len(client.page_calls))

    def test_account_errors_stop_the_trigger(self):
        for kind in (Kind.INVALID_CREDENTIALS, Kind.ACCOUNT_BLOCKED, Kind.BAD_REQUEST):
            with self.subTest(kind=kind):
                client, trigger = FakeFeedClient({PHISHING.feed_id: {LATEST: 9}}), FakeTrigger()
                client.errors.append((lambda feed_id, params, call: call == 2, error(kind)))
                with self.assertRaises(WhoisFreaksError):
                    self.run_poller(client, trigger)
                self.assertEqual(3, trigger.saved[-1]["feeds"][PHISHING.identity]["offset"])

    def test_single_feed_not_in_subscription_stops_with_clear_error(self):
        for kind in (Kind.NOT_ENTITLED, Kind.PLAN_LIMIT, Kind.NO_CREDITS):
            with self.subTest(kind=kind):
                client, trigger = FakeFeedClient({PHISHING.feed_id: {LATEST: 9}}), FakeTrigger()
                client.errors.append((lambda feed_id, params, call: True, error(kind)))
                with self.assertRaises(PluginException) as context:
                    self.run_poller(client, trigger)
                self.assertIn("None of the enabled feeds can be downloaded", context.exception.cause)

    def test_gives_up_after_consecutive_failures(self):
        client, trigger = FakeFeedClient({PHISHING.feed_id: {LATEST: 9}}), FakeTrigger(budget=10**9)
        client.errors.append((lambda feed_id, params, call: True, error(Kind.SERVER_ERROR)))
        with self.assertRaises(PluginException) as context:
            self.run_poller(client, trigger)
        self.assertIn("consecutive failures", context.exception.cause)
        self.assertEqual(feed_poller.MAX_CONSECUTIVE_FAILURES + 1, len(client.page_calls))

    def test_date_no_longer_available_is_skipped(self):
        client = FakeFeedClient({PHISHING.feed_id: {LATEST: 9, "2026-10-13": 1}})
        trigger = FakeTrigger()

        def expire(feed_id, params, call):
            if params["date"] == LATEST and call == 2:
                client.window = ["2026-10-13", "2026-10-13"]
                return True
            return False

        client.errors.append((expire, error(Kind.DATE_NOT_AVAILABLE)))
        self.run_poller(client, trigger)
        self.assertEqual(["2026-10-12", "2026-10-13"], [event["feed_date"] for event in trigger.sent])
        self.assertIn("no longer available", str(trigger.logger.warning.call_args_list))

    def test_date_listed_but_not_downloadable_is_retried(self):
        client, trigger = FakeFeedClient({PHISHING.feed_id: {LATEST: 2}}), FakeTrigger()
        client.errors.append((lambda feed_id, params, call: call == 1, error(Kind.DATE_NOT_AVAILABLE)))
        self.run_poller(client, trigger)
        self.assertEqual(2, len(trigger.rows))
        self.assertGreaterEqual(trigger.clock, feed_poller.DATE_UNAVAILABLE_DELAY_SECONDS)

    def test_date_never_downloadable_is_eventually_skipped(self):
        client, trigger = FakeFeedClient({PHISHING.feed_id: {LATEST: 2}}), FakeTrigger(budget=10**6)
        client.errors.append((lambda feed_id, params, call: True, error(Kind.DATE_NOT_AVAILABLE)))
        self.run_poller(client, trigger)
        self.assertEqual(LATEST, feed_state(trigger)["last_completed_date"])
        self.assertEqual(feed_poller.MAX_DATE_UNAVAILABLE_ATTEMPTS, len(client.page_calls))

    def test_feed_without_data_waits(self):
        client, trigger = FakeFeedClient({}, last_update="Not Available"), FakeTrigger(budget=7300)
        self.run_poller(client, trigger)
        self.assertEqual([], client.page_calls)
        self.assertEqual(3, client.status_calls)

    def test_row_filter(self):
        client, trigger = FakeFeedClient({PHISHING.feed_id: {LATEST: 7}}), FakeTrigger()
        feed_settings = build_settings(
            MagicMock(), [PHISHING], batch_size=3, poll_interval_minutes=60, min_confidence=0.8
        )
        self.run_poller(client, trigger, feed_settings)
        # confidence alternates 1.0, 0.5 within each page of 3, so pages keep 2, 2 and 1 rows
        self.assertEqual(5, len(trigger.rows))
        self.assertTrue(all(row["confidence"] >= 0.8 for row in trigger.rows))
        self.assertEqual(7, trigger.sent[-1]["next_offset"])

    def test_invalid_or_old_state_is_reset(self):
        states = (
            {"version": 1, "feed": PHISHING.identity, "current_date": None},
            {"version": 2, "feeds": {PHISHING.identity: {"offset": -1}}},
            {"version": 2, "feeds": "broken"},
        )
        for state in states:
            with self.subTest(state=state):
                client = FakeFeedClient({PHISHING.feed_id: {LATEST: 1}})
                trigger = FakeTrigger(state=copy.deepcopy(state))
                self.run_poller(client, trigger)
                self.assertEqual(1, len(trigger.rows))
                trigger.logger.warning.assert_called()

    def test_progress_of_disabled_feed_is_discarded(self):
        state = {"version": 2, "feeds": {MALWARE.identity: feed_poller._fresh_feed_state()}}
        client, trigger = FakeFeedClient({PHISHING.feed_id: {LATEST: 1}}), FakeTrigger(state=state)
        self.run_poller(client, trigger)
        self.assertEqual([PHISHING.identity], list(trigger.state["feeds"]))

    def test_stateless_trigger_does_not_save(self):
        client, trigger = FakeFeedClient({PHISHING.feed_id: {LATEST: 1}}), FakeTrigger(state_file="")
        self.run_poller(client, trigger)
        self.assertEqual([], trigger.saved)
        self.assertEqual(1, len(trigger.rows))

    def test_save_failure_does_not_stop_ingestion(self):
        client, trigger = FakeFeedClient({PHISHING.feed_id: {LATEST: 4}}), FakeTrigger()
        trigger._save_state = MagicMock(side_effect=OSError("disk full"))
        self.run_poller(client, trigger)
        self.assertEqual(4, len(trigger.rows))
        self.assertIn("Could not save trigger progress", str(trigger.logger.warning.call_args_list))

    def test_failing_shutdown_check_stops(self):
        class BrokenTrigger(FakeTrigger):
            @property
            def run_trigger(self):
                raise RuntimeError("flag directory missing")

        client, trigger = FakeFeedClient({PHISHING.feed_id: {LATEST: 4}}), BrokenTrigger()
        self.run_poller(client, trigger)
        self.assertEqual([], client.page_calls)

    def test_long_waits_are_sliced_for_shutdown(self):
        trigger = FakeTrigger(budget=25)
        client = FakeFeedClient({PHISHING.feed_id: {LATEST: 1}})
        sleeps = []

        def sleep(seconds):
            sleeps.append(seconds)
            trigger.sleep(seconds)

        FeedPoller(trigger, client, [PHISHING], settings(), sleep, trigger.now).run()
        self.assertTrue(all(seconds <= feed_poller.WAIT_SLICE_SECONDS for seconds in sleeps))
        self.assertLess(trigger.clock, 60)


class TestMultipleFeeds(TestCase):
    def run_feeds(self, client, trigger, feeds):
        FeedPoller(trigger, client, feeds, settings(), trigger.sleep, trigger.now).run()

    def test_feeds_are_interleaved_and_tracked_separately(self):
        client = FakeFeedClient({GTLD.feed_id: {LATEST: 9}, CCTLD.feed_id: {LATEST: 4}})
        trigger = FakeTrigger(budget=3000)
        self.run_feeds(client, trigger, [GTLD, CCTLD])
        # 9 gTLD rows are an exact multiple of the batch size, so gTLD needs one extra request to see the end
        self.assertEqual(
            ["newly.gtld", "newly.cctld", "newly.gtld", "newly.cctld", "newly.gtld", "newly.gtld"],
            [call["feed"] for call in client.page_calls],
        )
        self.assertEqual({"newly.gtld": 9, "newly.cctld": 4}, page_counts(trigger, "feed"))
        for definition in (GTLD, CCTLD):
            self.assertEqual(LATEST, trigger.state["feeds"][definition.identity]["last_completed_date"])
        self.assertEqual(1, client.status_calls)

    def test_feed_not_in_subscription_is_skipped_while_others_continue(self):
        client = FakeFeedClient({PHISHING.feed_id: {LATEST: 4}, MALWARE.feed_id: {LATEST: 4}})
        client.errors.append((lambda feed_id, params, call: feed_id == MALWARE.feed_id, error(Kind.NOT_ENTITLED)))
        trigger = FakeTrigger(budget=feed_poller.ENTITLEMENT_RECHECK_SECONDS + 100)
        self.run_feeds(client, trigger, [PHISHING, MALWARE])
        self.assertEqual({"threat_feed.phishing": 4}, page_counts(trigger, "feed"))
        malware_calls = [call for call in client.page_calls if call["feed"] == MALWARE.feed_id]
        self.assertEqual(2, len(malware_calls))
        self.assertIn("Malware threat feed", str(trigger.logger.warning.call_args_list))

    def test_feed_recovers_after_subscription_is_added(self):
        client = FakeFeedClient({PHISHING.feed_id: {LATEST: 1}, MALWARE.feed_id: {LATEST: 2}})
        client.errors.append(
            (lambda feed_id, params, call: feed_id == MALWARE.feed_id and call <= 2, error(Kind.NOT_ENTITLED))
        )
        trigger = FakeTrigger(budget=feed_poller.ENTITLEMENT_RECHECK_SECONDS + 100)
        self.run_feeds(client, trigger, [PHISHING, MALWARE])
        self.assertEqual({"threat_feed.phishing": 1, "threat_feed.malware": 2}, page_counts(trigger, "feed"))

    def test_every_feed_not_in_subscription_stops(self):
        client = FakeFeedClient({PHISHING.feed_id: {LATEST: 4}, MALWARE.feed_id: {LATEST: 4}})
        client.errors.append((lambda feed_id, params, call: True, error(Kind.NOT_ENTITLED)))
        with self.assertRaises(PluginException) as context:
            self.run_feeds(client, FakeTrigger(), [PHISHING, MALWARE])
        self.assertEqual(2, context.exception.cause.count("not included in the WhoisFreaks subscription"))


class TestSettings(TestCase):
    def test_defaults_and_clamping(self):
        logger = MagicMock()
        for batch, expected in ((None, 500), (0, 1), (5000, 1000), (250, 250)):
            with self.subTest(batch=batch):
                self.assertEqual(expected, build_settings(logger, [PHISHING], batch_size=batch).batch_size)
        for minutes, expected in ((None, 360), (0, 60), (99999, 10080)):
            with self.subTest(minutes=minutes):
                result = build_settings(logger, [PHISHING], poll_interval_minutes=minutes)
                self.assertEqual(expected * 60, result.poll_interval_seconds)

    def test_start_date(self):
        logger = MagicMock()
        self.assertEqual(
            datetime.date(2026, 9, 14), build_settings(logger, [PHISHING], start_date="2026-09-14").start_date
        )
        self.assertIsNone(build_settings(logger, [PHISHING], start_date="14-09-2026").start_date)
        self.assertIsNone(build_settings(logger, [PHISHING], start_date=" ").start_date)
        logger.warning.assert_called()

    def test_filters_follow_the_feed(self):
        result = build_settings(MagicMock(), [PHISHING, GTLD], domain_keywords=["brand"], min_confidence=0.5)
        self.assertTrue(result.row_filter({"domain": "brand.com", "confidence": 0.5}, PHISHING.feed_id))
        self.assertFalse(result.row_filter({"domain_name": "other.com"}, GTLD.feed_id))
        self.assertTrue(result.row_filter({"domain": "brand.com", "confidence": 0.9}))
        with self.assertRaises(PluginException):
            build_settings(MagicMock(), [PHISHING], min_confidence=1.5)

    def test_selected_feeds(self):
        self.assertEqual([MALWARE], selected_feeds({"Phishing": (PHISHING, False), "Malware": (MALWARE, True)}))
        with self.assertRaises(PluginException) as context:
            selected_feeds({"Include Phishing": (PHISHING, None), "Include Malware": (MALWARE, False)})
        self.assertIn("Include Phishing, Include Malware", context.exception.assistance)

    def test_pick_next_date(self):
        window = feed.FeedWindow(datetime.date(2026, 10, 1), datetime.date(2026, 10, 12))
        cases = [
            ((None, None, False), datetime.date(2026, 10, 12)),
            ((None, datetime.date(2026, 10, 5), False), datetime.date(2026, 10, 5)),
            ((datetime.date(2026, 10, 12), None, True), None),
            ((datetime.date(2026, 10, 5), None, False), datetime.date(2026, 10, 12)),
            ((datetime.date(2026, 10, 5), None, True), datetime.date(2026, 10, 6)),
            ((datetime.date(2026, 9, 1), None, True), datetime.date(2026, 10, 1)),
        ]
        for (last, start, catch_up), expected in cases:
            with self.subTest(last=last, start=start, catch_up=catch_up):
                self.assertEqual(expected, pick_next_date(window, last, start, catch_up)[0])
