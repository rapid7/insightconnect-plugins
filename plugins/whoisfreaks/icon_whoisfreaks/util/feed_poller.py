import datetime
import random
import time
from dataclasses import dataclass
from typing import Callable, Optional

from insightconnect_plugin_runtime.exceptions import PluginException

from icon_whoisfreaks.util import constants, validators
from icon_whoisfreaks.util import feed as feed_util
from icon_whoisfreaks.util.errors import RETRYABLE_KINDS, Kind, WhoisFreaksError

STATE_VERSION = 2
PAGE_DELAY_SECONDS = 0.25
WAIT_SLICE_SECONDS = 10
STATUS_CACHE_SECONDS = 60
MAX_CONSECUTIVE_FAILURES = 20
FAILURE_BASE_DELAY_SECONDS = 30
FAILURE_MAX_DELAY_SECONDS = 1800
DATE_UNAVAILABLE_DELAY_SECONDS = 900
MAX_DATE_UNAVAILABLE_ATTEMPTS = 8
ENTITLEMENT_RECHECK_SECONDS = 24 * 3600

# The account cannot download this particular feed; other enabled feeds may still work
FEED_UNAVAILABLE_KINDS = frozenset({Kind.NOT_ENTITLED, Kind.PLAN_LIMIT, Kind.NO_CREDITS})


@dataclass
class FeedSettings:
    batch_size: int
    poll_interval_seconds: int
    start_date: Optional[datetime.date]
    catch_up: bool
    row_filter: Callable[[dict], bool]


def _clamp(logger, name: str, value, minimum: int, maximum: int, default: int) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        logger.warning("%s is not set, using %d", name, default)
        return default
    clamped = min(max(value, minimum), maximum)
    if clamped != value:
        logger.warning(
            "%s %d is outside the supported range %d to %d, using %d", name, value, minimum, maximum, clamped
        )
    return clamped


def _start_date(logger, value) -> Optional[datetime.date]:
    text = validators.optional_text(value)
    if text is None:
        return None
    try:
        return datetime.datetime.strptime(text, constants.DATE_FORMAT).date()
    except ValueError:
        logger.warning("Start Date '%s' is not a YYYY-MM-DD date, so the latest feed date is used", text)
        return None


def selected_feeds(choices: dict) -> list:
    """Return the feeds whose toggle is enabled. choices maps a toggle title to its FeedDefinition and value."""
    feeds = [definition for definition, enabled in choices.values() if enabled]
    if not feeds:
        raise PluginException(
            cause="No feed is enabled in the trigger configuration",
            assistance=f"Enable at least one of: {', '.join(choices)}",
        )
    return feeds


def build_settings(  # pylint: disable=too-many-arguments
    logger,
    feeds: list,
    batch_size=None,
    poll_interval_minutes=None,
    start_date=None,
    catch_up=False,
    domain_keywords=None,
    tld_filter=None,
    min_confidence=None,
) -> FeedSettings:
    if min_confidence is not None and not 0 <= min_confidence <= 1:
        raise PluginException(
            cause=f"Minimum Confidence {min_confidence} is out of range",
            assistance="Minimum Confidence must be between 0 and 1, for example 0.8",
        )
    poll_minutes = _clamp(
        logger,
        "Poll Interval Minutes",
        poll_interval_minutes,
        constants.MIN_POLL_INTERVAL_MINUTES,
        constants.MAX_POLL_INTERVAL_MINUTES,
        360,
    )
    filters = {
        definition.feed_id: feed_util.build_row_filter(
            definition, validators.keywords(domain_keywords), validators.tlds(tld_filter), min_confidence
        )
        for definition in feeds
    }

    def row_filter(row: dict, feed_id: str = "") -> bool:
        accept = filters.get(feed_id) or next(iter(filters.values()))
        return accept(row)

    return FeedSettings(
        batch_size=_clamp(logger, "Batch Size", batch_size, 1, constants.MAX_FEED_PAGE_SIZE, 500),
        poll_interval_seconds=poll_minutes * 60,
        start_date=_start_date(logger, start_date),
        catch_up=bool(catch_up),
        row_filter=row_filter,
    )


def pick_next_date(window, last_completed, start_date, catch_up) -> tuple:
    """Choose the next feed date to ingest. Returns (date or None, warning or None)."""
    if last_completed is None:
        if start_date is None or window.contains(start_date):
            return start_date or window.last_update, None
        return window.last_update, (
            f"Start Date {start_date} is outside the feed availability window {window.available_from} to "
            f"{window.last_update}, so the latest date {window.last_update} is used"
        )
    if last_completed >= window.last_update:
        return None, None
    if catch_up:
        return max(last_completed + datetime.timedelta(days=1), window.available_from), None
    return window.last_update, None


def _as_date(value) -> Optional[datetime.date]:
    try:
        return datetime.datetime.strptime(str(value), constants.DATE_FORMAT).date()
    except ValueError:
        return None


def _fresh_feed_state() -> dict:
    return {
        "current_date": None,
        "offset": 0,
        "previous_last_line": None,
        "last_completed_date": None,
        "unavailable_attempts": 0,
    }


def _valid_feed_state(state) -> bool:
    if not isinstance(state, dict):
        return False
    dates_ok = all(
        state.get(key) is None or _as_date(state.get(key)) for key in ("current_date", "last_completed_date")
    )
    counters_ok = all(
        isinstance(state.get(key), int) and state.get(key) >= 0 for key in ("offset", "unavailable_attempts")
    )
    return dates_ok and counters_ok


class _StatusCache:
    """Shares one status document between the feeds of a trigger for a short time."""

    def __init__(self, client, clock: Callable[[], float]):
        self._client = client
        self._clock = clock
        self._data = None
        self._fetched_at = 0.0

    def get(self) -> dict:
        now = self._clock()
        if self._data is None or now - self._fetched_at >= STATUS_CACHE_SECONDS:
            self._data = self._client.get_feed_status()
            self._fetched_at = now
        return self._data

    def refresh(self) -> dict:
        self._data = None
        return self.get()


class FeedWorker:  # pylint: disable=too-many-instance-attributes
    """Ingests one feed. step() performs one unit of work and returns the seconds until the next unit.

    The date in progress is pinned until it is fully ingested, even when a newer date is published meanwhile,
    and the offset survives transient failures and restarts.
    """

    def __init__(self, feed, state: dict, client, status: _StatusCache, settings: FeedSettings, hooks: dict):
        self.feed = feed
        self.state = state
        self.unavailable_reason = None
        self._client = client
        self._status = status
        self._settings = settings
        self._logger = hooks["logger"]
        self._emit = hooks["emit"]
        self._save = hooks["save"]
        self._failures = 0

    def step(self) -> float:
        try:
            delay = self._cycle()
        except WhoisFreaksError as error:
            if error.kind not in RETRYABLE_KINDS:
                raise
            return self._on_transient_failure(error)
        self._failures = 0
        self.unavailable_reason = None
        return delay

    def _cycle(self) -> float:
        if not self.state["current_date"]:
            next_date = self._choose_next_date()
            if next_date is None:
                return self._settings.poll_interval_seconds
            self._begin_date(next_date)
        return self._ingest_page()

    def _window(self, refresh: bool = False):
        status = self._status.refresh() if refresh else self._status.get()
        return feed_util.resolve_window(status, self.feed.status_path)

    def _choose_next_date(self) -> Optional[datetime.date]:
        window = self._window()
        if window is None:
            self._logger.warning(
                "%s: the WhoisFreaks status endpoint reports no available data, checking again in %d minutes",
                self.feed.label,
                self._settings.poll_interval_seconds // 60,
            )
            return None
        last_completed = _as_date(self.state["last_completed_date"])
        next_date, warning = pick_next_date(window, last_completed, self._settings.start_date, self._settings.catch_up)
        if warning:
            self._logger.warning("%s: %s", self.feed.label, warning)
        if next_date is None:
            self._logger.info(
                "%s: date %s is the latest available and is ingested, checking again in %d minutes",
                self.feed.label,
                last_completed,
                self._settings.poll_interval_seconds // 60,
            )
        return next_date

    def _begin_date(self, day: datetime.date) -> None:
        self.state.update(current_date=day.isoformat(), offset=0, previous_last_line=None, unavailable_attempts=0)
        self._save()
        self._logger.info("%s: ingesting feed date %s", self.feed.label, day)

    def _ingest_page(self) -> float:
        day, offset = self.state["current_date"], self.state["offset"]
        params = dict(self.feed.params, date=day, limit=self._settings.batch_size, offset=offset)
        try:
            text = self._client.get_feed_page(self.feed.label, self.feed.path, params)
        except WhoisFreaksError as error:
            if error.kind == Kind.DATE_NOT_AVAILABLE:
                return self._on_date_unavailable(day)
            raise
        page = feed_util.parse_page(text, self.feed, self.state["previous_last_line"])
        self._report_anomalies(page, day, offset)
        rows = [row for row in page.rows if self._settings.row_filter(row, self.feed.feed_id)]
        next_offset = offset + page.raw_count
        if rows:
            self._emit(self.feed, rows, day, offset, next_offset)
        self.state.update(offset=next_offset, previous_last_line=page.last_line, unavailable_attempts=0)
        if page.raw_count < self._settings.batch_size:
            self._complete_date(day)
            return 0
        self._save()
        return PAGE_DELAY_SECONDS

    def _complete_date(self, day: str) -> None:
        previous = self.state["last_completed_date"]
        self.state.update(
            last_completed_date=max(day, previous) if previous else day,
            current_date=None,
            offset=0,
            previous_last_line=None,
            unavailable_attempts=0,
        )
        self._save()
        self._logger.info("%s: feed date %s is complete", self.feed.label, day)

    def _report_anomalies(self, page, day: str, offset: int) -> None:
        if page.header_missing:
            self._logger.warning(
                "%s: page at row %d of %s had no header row, the documented columns were used",
                self.feed.label,
                offset,
                day,
            )
        if page.invalid_lines:
            self._logger.warning(
                "%s: skipped %d lines that are not domain names at row %d of %s",
                self.feed.label,
                page.invalid_lines,
                offset,
                day,
            )

    def _on_date_unavailable(self, day: str) -> float:
        attempts = self.state["unavailable_attempts"] + 1
        self.state["unavailable_attempts"] = attempts
        window = self._window(refresh=True)
        still_listed = window is not None and window.contains(_as_date(day))
        if not still_listed or attempts >= MAX_DATE_UNAVAILABLE_ATTEMPTS:
            self._logger.warning(
                "%s: feed date %s is no longer available from WhoisFreaks, skipping it after row %d",
                self.feed.label,
                day,
                self.state["offset"],
            )
            self._complete_date(day)
            return 0
        self._save()
        self._logger.warning(
            "%s: feed date %s is listed by the status endpoint but not yet downloadable, retrying in %d minutes",
            self.feed.label,
            day,
            DATE_UNAVAILABLE_DELAY_SECONDS // 60,
        )
        return DATE_UNAVAILABLE_DELAY_SECONDS

    def _on_transient_failure(self, error: WhoisFreaksError) -> float:
        self._failures += 1
        self._save()
        if self._failures > MAX_CONSECUTIVE_FAILURES:
            raise PluginException(
                cause=f"{self.feed.label}: stopped after {MAX_CONSECUTIVE_FAILURES} consecutive failures. "
                f"Last error: {error.cause}",
                assistance=f"{error.assistance}. Progress is saved and the trigger resumes from it when restarted",
                data=error.data,
            )
        delay = min(FAILURE_BASE_DELAY_SECONDS * (2 ** (self._failures - 1)), FAILURE_MAX_DELAY_SECONDS)
        delay += random.uniform(0, FAILURE_BASE_DELAY_SECONDS)  # nosec B311 - jitter only
        self._logger.error(
            "%s: %s. Retry %d of %d in %d seconds, progress is kept",
            self.feed.label,
            error.cause,
            self._failures,
            MAX_CONSECUTIVE_FAILURES,
            delay,
        )
        return delay


class FeedPoller:
    """Runs the enabled feeds of a trigger side by side and keeps their progress in the trigger state.

    The state is saved after every emitted batch, so a restart resumes every feed at its next batch. Pages of
    the enabled feeds are interleaved so that a large feed does not delay the others.
    """

    def __init__(  # pylint: disable=too-many-arguments
        self,
        trigger,
        client,
        feeds: list,
        settings: FeedSettings,
        sleep: Optional[Callable[[float], None]] = None,
        clock: Optional[Callable[[], float]] = None,
    ):
        self._trigger = trigger
        self._client = client
        self._feeds = feeds
        self._settings = settings
        self._sleep = sleep or time.sleep
        self._clock = clock or time.monotonic
        self._logger = trigger.logger
        self._stopped = False
        self._workers = []
        self.state = {}

    def run(self) -> None:
        self._load_state()
        status = _StatusCache(self._client, self._clock)
        hooks = {"logger": self._logger, "emit": self._emit, "save": self._save}
        self._workers = [
            FeedWorker(feed, self.state["feeds"][feed.identity], self._client, status, self._settings, hooks)
            for feed in self._feeds
        ]
        next_run = [self._clock()] * len(self._workers)
        while self._should_continue():
            index = min(range(len(self._workers)), key=next_run.__getitem__)
            wait = next_run[index] - self._clock()
            if wait > 0:
                self._wait(wait)
                continue
            next_run[index] = self._clock() + self._step(self._workers[index])

    def _step(self, worker: FeedWorker) -> float:
        try:
            return worker.step()
        except WhoisFreaksError as error:
            if error.kind not in FEED_UNAVAILABLE_KINDS:
                self._save()
                raise
            return self._on_feed_unavailable(worker, error)

    def _on_feed_unavailable(self, worker: FeedWorker, error: WhoisFreaksError) -> float:
        worker.unavailable_reason = error.cause
        self._save()
        if all(item.unavailable_reason for item in self._workers):
            reasons = "; ".join(item.unavailable_reason for item in self._workers)
            raise PluginException(
                cause=f"None of the enabled feeds can be downloaded with this WhoisFreaks account: {reasons}",
                assistance=f"{error.assistance}. Disable the feeds that are not in the subscription",
                data=error.data,
            )
        self._logger.warning(
            "%s is skipped: %s The other enabled feeds continue, and this feed is checked again in %d hours",
            worker.feed.label,
            error.cause,
            ENTITLEMENT_RECHECK_SECONDS // 3600,
        )
        return ENTITLEMENT_RECHECK_SECONDS

    def _emit(self, feed, rows: list, day: str, offset: int, next_offset: int) -> None:
        self._trigger.send(
            {
                "events": rows,
                "feed": feed.feed_id,
                "feed_date": day,
                "offset": offset,
                "next_offset": next_offset,
                "count": len(rows),
            }
        )
        self._logger.info("%s: emitted %d rows of %s (rows %d to %d)", feed.label, len(rows), day, offset, next_offset)

    # State, waiting and shutdown

    def _load_state(self) -> None:
        state = self._trigger.state if isinstance(getattr(self._trigger, "state", None), dict) else {}
        if state.get("version") != STATE_VERSION or not isinstance(state.get("feeds"), dict):
            if state:
                self._logger.warning("Saved trigger progress has an unsupported format, starting over")
            state.clear()
            state.update(version=STATE_VERSION, feeds={})
        saved = state["feeds"]
        enabled = {feed.identity for feed in self._feeds}
        for identity in [identity for identity in saved if identity not in enabled]:
            self._logger.info("Discarding saved progress of %s, which is no longer enabled", identity)
            del saved[identity]
        for feed in self._feeds:
            self._load_feed_state(saved, feed)
        self._trigger.state = state
        self.state = state

    def _load_feed_state(self, saved: dict, feed) -> None:
        feed_state = saved.get(feed.identity)
        if _valid_feed_state(feed_state):
            self._logger.info(
                "%s: resuming saved progress, date in progress %s at row %s, last completed date %s",
                feed.label,
                feed_state.get("current_date"),
                feed_state.get("offset"),
                feed_state.get("last_completed_date"),
            )
            return
        if feed_state is not None:
            self._logger.warning("%s: saved progress is invalid, starting over", feed.label)
        saved[feed.identity] = _fresh_feed_state()

    def _save(self) -> None:
        if not getattr(self._trigger, "state_file", ""):
            return
        try:
            self._trigger._save_state()  # pylint: disable=protected-access
        except Exception as error:  # noqa: BLE001 - losing a checkpoint must not stop ingestion
            self._logger.warning("Could not save trigger progress (%s)", type(error).__name__)

    def _should_continue(self) -> bool:
        if self._stopped:
            return False
        try:
            keep_running = bool(self._trigger.run_trigger)
        except Exception as error:  # noqa: BLE001 - treat a failing shutdown check as a shutdown request
            self._logger.warning("Trigger shutdown check failed (%s)", type(error).__name__)
            keep_running = False
        if not keep_running:
            self._stopped = True
            self._logger.info("Shutdown requested, trigger progress is saved")
        return keep_running

    def _wait(self, seconds: float) -> None:
        remaining = seconds
        while remaining > 0:
            step = min(remaining, WAIT_SLICE_SECONDS)
            self._sleep(step)
            remaining -= step
            if remaining > 0 and not self._should_continue():
                return
