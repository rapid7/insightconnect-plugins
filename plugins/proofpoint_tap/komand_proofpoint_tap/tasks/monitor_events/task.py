from datetime import datetime, timedelta, timezone
from hashlib import sha1
from json import loads
from os import getenv
from typing import Dict

import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException

from komand_proofpoint_tap.util.api import Endpoint
from komand_proofpoint_tap.util.exceptions import ApiException
from komand_proofpoint_tap.util.util import SiemUtils
from .schema import MonitorEventsInput, MonitorEventsOutput, MonitorEventsState, Component

MAX_ALLOWED_LOOKBACK_HOURS = 24
SPECIFIC_DATE = getenv("SPECIFIC_DATE")


class MonitorEvents(insightconnect_plugin_runtime.Task):
    LAST_COLLECTION_DATE = "last_collection_date"
    NEXT_PAGE_INDEX = "next_page_index"
    STATUS_CODE = "status_code"
    SPLIT_SIZE = 1000
    PREVIOUS_LOGS_HASHES = "previous_logs_hashes"

    def __init__(self):
        super(self.__class__, self).__init__(
            name="monitor_events",
            description=Component.DESCRIPTION,
            input=MonitorEventsInput(),
            output=MonitorEventsOutput(),
            state=MonitorEventsState(),
        )

    def run(self, params={}, state={}, custom_config={}):  # noqa: MC0001
        self.connection.client.toggle_rate_limiting = False
        has_more_pages = False
        try:
            last_collection_date = state.get(self.LAST_COLLECTION_DATE)
            self.logger.info(f"Last collection date retrieved: {last_collection_date}")
            next_page_index = state.get(self.NEXT_PAGE_INDEX)
            now = self.get_current_time() - timedelta(minutes=1)

            max_allowed_lookback, backfill_date = self._apply_custom_timings(custom_config, now)

            # [PLGN-727] skip comparison check if first run of a backfill, next run should specify lookback to match.
            if not backfill_date:
                # Don't allow collection to go back further than MAX_ALLOWED_LOOKBACK_HOURS (24) hours max
                # Unless otherwise defined externally and passed in via custom_config parameter.
                if last_collection_date and datetime.fromisoformat(last_collection_date) < max_allowed_lookback:
                    last_collection_date = max_allowed_lookback.isoformat()
                    if next_page_index:
                        next_page_index = None
                        state.pop(self.NEXT_PAGE_INDEX)
                    self.logger.info(f"Last collection date reset to max lookback allowed: {last_collection_date}")

            previous_logs_hashes = state.get(self.PREVIOUS_LOGS_HASHES, [])
            query_params = {"format": "JSON"}

            if not state or not last_collection_date:
                task_start = "First run... "
                first_time = now - timedelta(hours=1)
                if backfill_date:
                    first_time = datetime(**backfill_date, tzinfo=timezone.utc)  # PLGN-727: allow backfill
                    task_start += f"Using custom value of {backfill_date}"
                self.logger.info(task_start)
                last_time = first_time + timedelta(hours=1)
                state[self.LAST_COLLECTION_DATE] = last_time.isoformat()
                parameters = SiemUtils.prepare_time_range(first_time.isoformat(), last_time.isoformat(), query_params)
            else:
                if next_page_index:
                    state.pop(self.NEXT_PAGE_INDEX)
                    self.logger.info(f"Getting the next page (page index {next_page_index}) of results...")
                    parameters = SiemUtils.prepare_time_range(
                        (datetime.fromisoformat(last_collection_date) - timedelta(hours=1)).isoformat(),
                        last_collection_date,
                        query_params,
                    )
                else:
                    self.logger.info("Subsequent run")
                    start_time = last_collection_date
                    end_time = (datetime.fromisoformat(last_collection_date) + timedelta(hours=1)).isoformat()
                    if end_time > now.isoformat():
                        self.logger.info(
                            f"End time for lookup reset from {end_time} to {now.isoformat()} to avoid going out of range"
                        )
                        end_time = now.isoformat()

                    # If the resulting time interval is invalid, do not query API this time around
                    query_delta = datetime.fromisoformat(end_time) - datetime.fromisoformat(start_time)
                    if start_time >= end_time or query_delta < timedelta(minutes=1):
                        self.logger.info(f"Query delta: {query_delta} Time delta allowed: {timedelta(minutes=1)}")
                        self.logger.info(
                            f"Start time > End time or Insufficient interval between start time {start_time} and end time {end_time} to avoid going out of query range"
                        )
                        self.logger.info("Do not query API this time round")
                        return [], state, has_more_pages, 200, None
                    else:
                        state[self.LAST_COLLECTION_DATE] = end_time
                        parameters = SiemUtils.prepare_time_range(start_time, end_time, query_params)

            self.logger.info(f"Parameters used to query endpoint: {parameters}")
            try:
                parsed_logs = self.parse_logs(
                    self.connection.client.siem_action(Endpoint.get_all_threats(), parameters)
                )
                self.logger.info(f"Retrieved {len(parsed_logs)} total parsed events in time interval")
                if (not next_page_index and len(parsed_logs) > self.SPLIT_SIZE) or (
                    next_page_index and (next_page_index + 1) * self.SPLIT_SIZE < len(parsed_logs)
                ):
                    state[self.NEXT_PAGE_INDEX] = next_page_index + 1 if next_page_index else 1
                    has_more_pages = True
                    self.logger.info(
                        f"Set next page index to {state[self.NEXT_PAGE_INDEX]} and has more pages to True for the next run"
                    )
                current_page_index = next_page_index if next_page_index else 0
                # Send back a maximum of SPLIT_SIZE events at a time (use page index to track this in state)
                new_unique_logs, new_logs_hashes = self.compare_hashes(
                    previous_logs_hashes,
                    parsed_logs[current_page_index * self.SPLIT_SIZE : (current_page_index + 1) * self.SPLIT_SIZE],
                )
                state[self.PREVIOUS_LOGS_HASHES] = (
                    [*previous_logs_hashes, *new_logs_hashes] if current_page_index > 0 else new_logs_hashes
                )
                self.logger.info(f"Retrieved {len(new_unique_logs)} events")
                return new_unique_logs, state, has_more_pages, 200, None

            except ApiException as error:
                self.logger.info(f"API Exception occurred: status_code: {error.status_code}, error: {error}")
                state[self.PREVIOUS_LOGS_HASHES] = []
                return [], state, False, error.status_code, error
        except Exception as error:
            self.logger.info(f"Exception occurred in monitor events task: {error}", exc_info=True)
            state[self.PREVIOUS_LOGS_HASHES] = []
            return [], state, has_more_pages, 500, PluginException(preset=PluginException.Preset.UNKNOWN, data=error)

    @staticmethod
    def get_current_time():
        return datetime.now(timezone.utc)

    def parse_logs(self, unparsed_logs: dict) -> list:
        parsed_logs = []
        for event_type in ["clicksBlocked", "clicksPermitted", "messagesBlocked", "messagesDelivered"]:
            parsed_logs.extend(self.prepare_log(log, event_type) for log in unparsed_logs.get(event_type, []))
        return parsed_logs

    def prepare_log(self, log: dict, value: str) -> dict:
        log["eventType"] = value

        # preventing random sorting of the list to ensure that the same hash is generated with each request
        try:
            if log.get("messageParts"):
                log["messageParts"] = sorted(log.get("messageParts", []), key=lambda part: part.get("md5", None) or "")
            return dict(sorted(log.items()))
        except Exception as error:
            self.logger.error(
                "Hit an unexpected exception when preparing log. Dropping this single log to "
                f"continue parsing timeframe. Error: {error}",
                exc_info=True,
            )
            return {}

    @staticmethod
    def sha1(log: dict) -> str:
        hash_ = sha1()  # nosec B303
        for key, value in log.items():
            hash_.update(f"{key}{value}".encode("utf-8"))
        return hash_.hexdigest()

    def compare_hashes(self, previous_logs_hashes: list, new_logs: list):
        new_logs_hashes = []
        logs_to_return = []
        for log in new_logs:
            hash_ = self.sha1(log)
            if hash_ not in previous_logs_hashes:
                new_logs_hashes.append(hash_)
                logs_to_return.append(log)
        if new_logs:
            self.logger.info(
                f"Original number of events: {len(new_logs)}. Number of events after de-duplication: {len(logs_to_return)} "
            )
        return logs_to_return, new_logs_hashes

    def _apply_custom_timings(self, custom_config: Dict[str, Dict], now: datetime) -> (datetime, int):
        """
        If a custom_config is supplied to the plugin we can modify our timing logic.
        Lookback is applied for the first run with no state.
        Default is applied to the max look back hours being enforced on the parameters.
        """
        cutoff_values = custom_config.get("cutoff", {"hours": MAX_ALLOWED_LOOKBACK_HOURS})
        cutoff_date, cutoff_hours = cutoff_values.get("date", {}), cutoff_values.get("hours")
        if cutoff_date:
            max_lookback = datetime(**cutoff_date, tzinfo=timezone.utc)
        else:
            max_lookback = now - timedelta(hours=cutoff_hours)

        # if using env var we need to convert to dict from string, CPS API will return us a dict.
        env_var_date = loads(SPECIFIC_DATE) if SPECIFIC_DATE else None
        specific_date = custom_config.get("lookback", env_var_date)
        self.logger.info(
            "Plugin task execution will apply the following restrictions. "
            f"Max lookback={max_lookback}, specific date={specific_date}"
        )
        return max_lookback, specific_date
