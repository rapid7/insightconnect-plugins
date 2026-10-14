import insightconnect_plugin_runtime
import time
from .schema import MonitorRecordsInput, MonitorRecordsOutput, Input, Output, Component

# Custom imports below
import json
import os
from insightconnect_plugin_runtime.exceptions import PluginException
from datetime import datetime, timedelta, timezone
from pathlib import Path
from tempfile import gettempdir

CACHE_FILE = "monitor_records_cache.json"
# The directory the Dockerfile creates for the plugin cache, which InsightConnect backs
# with a volume that outlives the container because the plugin sets enable_cache. The
# temporary directory does not survive the container being rescheduled, so a position
# stored there is lost every time that happens, and the trigger then resumes from the
# moment it restarted, silently skipping whatever changed while it was away.
CACHE_DIR = Path("/workspace/cache")
# The API stores timestamps to the millisecond, so resume from just after the newest
# record already emitted rather than re-sending it every poll.
RESUME_OFFSET = timedelta(milliseconds=1)
# The two timestamps every record carries. createdDate is stamped once and never moves.
# modifiedDate is null until something edits the record, and every edit moves it: the API
# does not set it at creation. A creation is therefore visible only in createdDate, which
# is why Any has to watch both fields rather than modifiedDate alone.
CREATED = "createdDate"
MODIFIED = "modifiedDate"
# The Event Type options, and the timestamps each one has to watch to find its events.
CREATED_ONLY = "Created"
UPDATED_ONLY = "Updated"
WATCHED_FIELDS = {CREATED_ONLY: (CREATED,), UPDATED_ONLY: (MODIFIED,)}
BOTH_FIELDS = (CREATED, MODIFIED)


class MonitorRecords(insightconnect_plugin_runtime.Trigger):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="monitor_records",
            description=Component.DESCRIPTION,
            input=MonitorRecordsInput(),
            output=MonitorRecordsOutput(),
        )
        self.cache_path = self._cache_dir() / CACHE_FILE

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        event_type = params.get(Input.EVENT_TYPE)
        filter_ = params.get(Input.FILTER)
        interval = params.get(Input.INTERVAL)
        record_type = params.get(Input.RECORD_TYPE)
        # END INPUT BINDING - DO NOT REMOVE

        # Which timestamps find the wanted events, and therefore what the stored position
        # refers to. The position is keyed by them, so switching Event Type on a running
        # trigger starts a fresh position rather than resuming from one that measures
        # different fields.
        watched = WATCHED_FIELDS.get(event_type, BOTH_FIELDS)
        cache_key = f"{record_type}:{','.join(watched)}"
        self.logger.info(f"Storing the trigger position in {self.cache_path}")
        watermark = self._load_watermark(cache_key)
        if watermark is None:
            # Nothing has been emitted for this record type yet, so start from now: the
            # trigger reports what happens from the moment it starts, and does not open
            # with a batch of history the workflow has no reason to act on.
            watermark = self._server_now()
            self.logger.info(f"No stored position for {cache_key}, starting from {self._to_odata(watermark)}")

        while True:
            since = self._to_odata(watermark)
            time_filter = " or ".join(f"{field} gt {since}" for field in watched)
            # Both halves are parenthesised because an unparenthesised or in either half
            # would bind looser than the and, letting records older than the watermark
            # back into every poll and re-emitting them forever.
            combined = f"({time_filter}) and ({filter_})" if filter_ else time_filter
            try:
                records = self.connection.client.list_records(
                    record_type,
                    filter_=combined,
                    # Oldest first, so that if the API returns more than the client will
                    # page through, the records left behind are the newest ones, which
                    # are still above the position and so arrive on a later poll.
                    order_by=f"{watched[0]} asc",
                )
            except PluginException as error:
                # A trigger that raises stops polling for good, and a rate limit or a
                # restart of the API should not take the workflow down with it. The
                # stored position means nothing is missed once the API recovers.
                self.logger.error(
                    f"Polling {record_type} failed, retrying in {abs(interval)} seconds. "
                    f"{error.cause} {error.assistance}"
                )
                time.sleep(abs(interval))
                continue

            if records:
                # The position advances past every record the query matched, including any
                # this Event Type discards, so a discarded record is not reconsidered on
                # the next poll.
                newest = self._newest_timestamp(records, watched)
                if newest:
                    watermark = newest + RESUME_OFFSET
                    self._save_watermark(cache_key, watermark)
                if event_type == UPDATED_ONLY:
                    records = [record for record in records if self._was_changed(record)]

            if records:
                self.logger.info(f"Emitting {len(records)} {record_type} {event_type} record(s)")
                self.send({Output.RECORDS: records, Output.COUNT: len(records)})
            else:
                self.logger.info(f"No new {record_type} records since {self._to_odata(watermark)}")

            time.sleep(abs(interval))

    def _server_now(self):
        """Now, on the clock that stamps the records this trigger compares against.

        The position is measured against timestamps Cyber GRC writes, so it has to come
        from Cyber GRC's clock. If this container's clock ran ahead of the server's, the
        opening position would sit in the server's future and everything created in the
        difference between them would be passed over silently.
        """
        server_time = self.connection.client.server_time()
        if server_time:
            return server_time
        self.logger.info(
            "Cyber GRC did not report its clock, so the starting position is this container's own time. If the two "
            "clocks differ, records created in the first moments after startup may be missed."
        )
        return datetime.now(timezone.utc)

    def _was_changed(self, record):
        """Whether a record has been edited since it was created.

        A record carries no modifiedDate until something edits it, so one without a
        modifiedDate has only ever been created. Where both timestamps are present they
        are compared as well, so that a record type which does stamp modifiedDate at
        creation does not report every creation as a change. A record carrying a
        modifiedDate but no createdDate cannot be judged and is emitted rather than
        dropped, because losing a real change is the worse of the two failures.
        """
        modified = self._parse(record.get(MODIFIED))
        if not modified:
            return False
        created = self._parse(record.get(CREATED))
        if not created:
            self.logger.info(f"Record {record.get('id')} carries no createdDate, so it is emitted as a change")
            return True
        return created != modified

    def _newest_timestamp(self, records, watched):
        """Highest parseable timestamp across the watched fields, or None if none carry one."""
        stamps = []
        for record in records:
            for field in watched:
                parsed = self._parse(record.get(field))
                if parsed:
                    stamps.append(parsed)
        if not stamps:
            self.logger.warning(
                f"None of the returned records carried a usable {' or '.join(watched)}; "
                "the trigger position has not advanced."
            )
            return None
        return max(stamps)

    @staticmethod
    def _parse(value):
        if not isinstance(value, str):
            return None
        try:
            parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
        except ValueError:
            return None
        # The API sends UTC, but not every field carries the offset. Attaching it here
        # keeps the batch comparable: mixing naive and aware datetimes raises a
        # TypeError, and treating a naive value as local time would move the watermark.
        if parsed.tzinfo is None:
            return parsed.replace(tzinfo=timezone.utc)
        return parsed

    @staticmethod
    def _to_odata(moment):
        """OData v4 wants an unquoted datetimeoffset literal, e.g. 2026-01-21T20:30:44.407Z."""
        return moment.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"

    @staticmethod
    def _cache_dir():
        """The persistent cache directory, falling back to a temporary one.

        The fallback matters when the trigger runs outside the plugin container, such as
        under the unit tests, where /workspace/cache does not exist.
        """
        if CACHE_DIR.is_dir() and os.access(CACHE_DIR, os.W_OK):
            return CACHE_DIR
        return Path(gettempdir())  # nosec

    def _load_watermark(self, cache_key):
        try:
            stored = json.loads(self.cache_path.read_text()).get(cache_key)
        except (OSError, ValueError, AttributeError):
            # An unreadable or corrupt cache means the trigger starts from now again,
            # which is far better than it refusing to start at all.
            return None
        return self._parse(stored)

    def _save_watermark(self, cache_key, moment):
        try:
            cache = json.loads(self.cache_path.read_text())
        except (OSError, ValueError):
            cache = {}
        if not isinstance(cache, dict):
            cache = {}
        cache[cache_key] = self._to_odata(moment)
        try:
            self.cache_path.write_text(json.dumps(cache))
        except OSError as error:
            # A lost cache only costs duplicate records after a restart, so keep polling.
            self.logger.warning(f"Could not persist the trigger position: {error}")
