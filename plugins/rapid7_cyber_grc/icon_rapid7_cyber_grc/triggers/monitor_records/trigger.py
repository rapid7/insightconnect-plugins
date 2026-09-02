import insightconnect_plugin_runtime
import time
from .schema import MonitorRecordsInput, MonitorRecordsOutput, Input, Output, Component

# Custom imports below
import json
from insightconnect_plugin_runtime.exceptions import PluginException
from datetime import datetime, timedelta, timezone
from pathlib import Path
from tempfile import gettempdir

CACHE_FILE = "monitor_records_cache.json"
# The API stores timestamps to the millisecond, so resume from just after the newest
# record already emitted rather than re-sending it every poll.
RESUME_OFFSET = timedelta(milliseconds=1)


class MonitorRecords(insightconnect_plugin_runtime.Trigger):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="monitor_records",
            description=Component.DESCRIPTION,
            input=MonitorRecordsInput(),
            output=MonitorRecordsOutput(),
        )
        self.cache_path = Path(gettempdir()) / CACHE_FILE  # nosec

    def run(self, params={}):
        # START INPUT BINDING - DO NOT REMOVE - ANY INPUTS BELOW WILL UPDATE WITH YOUR PLUGIN SPEC AFTER REGENERATION
        expand = params.get(Input.EXPAND)
        filter = params.get(Input.FILTER)
        first_run_lookback_minutes = params.get(Input.FIRST_RUN_LOOKBACK_MINUTES)
        interval = params.get(Input.INTERVAL)
        record_type = params.get(Input.RECORD_TYPE)
        timestamp_field = params.get(Input.TIMESTAMP_FIELD)
        # END INPUT BINDING - DO NOT REMOVE

        cache_key = f"{record_type}:{timestamp_field}"
        watermark = self._load_watermark(cache_key)
        if watermark is None:
            watermark = datetime.now(timezone.utc) - timedelta(minutes=abs(first_run_lookback_minutes))
            self.logger.info(f"No stored position for {cache_key}, looking back to {self._to_odata(watermark)}")

        while True:
            time_filter = f"{timestamp_field} gt {self._to_odata(watermark)}"
            # Both halves are parenthesised because an unparenthesised or in the user's
            # filter would bind looser than the and, letting records older than the
            # watermark back into every poll and re-emitting them forever.
            combined = f"({time_filter}) and ({filter})" if filter else time_filter
            try:
                records = self.connection.client.list_records(
                    record_type,
                    filter_=combined,
                    expand=expand,
                    order_by=f"{timestamp_field} asc",
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
                newest = self._newest_timestamp(records, timestamp_field)
                if newest:
                    watermark = newest + RESUME_OFFSET
                    self._save_watermark(cache_key, watermark)
                self.logger.info(f"Emitting {len(records)} {record_type} record(s)")
                self.send({Output.RECORDS: records, Output.COUNT: len(records)})
            else:
                self.logger.info(f"No new {record_type} records since {self._to_odata(watermark)}")

            time.sleep(abs(interval))

    def _newest_timestamp(self, records, timestamp_field):
        """Highest parseable timestamp in the batch, or None if the field is absent."""
        stamps = []
        for record in records:
            parsed = self._parse(record.get(timestamp_field))
            if parsed:
                stamps.append(parsed)
        if not stamps:
            self.logger.warning(
                f"None of the returned records carried a usable {timestamp_field}; "
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

    def _load_watermark(self, cache_key):
        try:
            stored = json.loads(self.cache_path.read_text()).get(cache_key)
        except (OSError, ValueError, AttributeError):
            # An unreadable or corrupt cache costs a replay of the lookback window, which
            # is far better than the trigger refusing to start.
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
