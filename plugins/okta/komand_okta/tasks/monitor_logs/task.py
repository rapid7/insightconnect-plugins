import json

import insightconnect_plugin_runtime
from .schema import MonitorLogsInput, MonitorLogsOutput, MonitorLogsState, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
from insightconnect_plugin_runtime.telemetry import monitor_task_delay
from komand_okta.util.exceptions import ApiException
from datetime import datetime, timedelta, timezone
from typing import Dict, Any, Tuple, Union, Optional
import re

DEFAULT_CUTOFF_HOURS = 168
DEFAULT_INITIAL_LOOKBACK = 24
DEFAULT_EVENTS_LIMIT = 1000


class MonitorLogs(insightconnect_plugin_runtime.Task):
    LAST_COLLECTION_TIMESTAMP = "last_collection_timestamp"
    LAST_SEARCH_END_TIMESTAMP = "last_search_end_timestamp"
    NEXT_PAGE_LINK = "next_page_link"
    STATUS_CODE = "status_code"
    EVENTS_LIMIT = "events_limit"
    RATE_LIMIT_RESET_EPOCH = "rate_limit_reset_epoch"

    def __init__(self):
        super(self.__class__, self).__init__(
            name="monitor_logs",
            description=Component.DESCRIPTION,
            input=MonitorLogsInput(),
            output=MonitorLogsOutput(),
            state=MonitorLogsState(),
        )

    @monitor_task_delay(timestamp_keys=[LAST_SEARCH_END_TIMESTAMP], default_delay_threshold="2d")
    def run(self, params={}, state={}, custom_config={}):  # pylint: disable=unused-argument
        self.connection.api_client.toggle_rate_limiting = False
        has_more_pages = False
        parameters = {}
        try:
            # Prepare the parameters
            filter_time, is_filter_datetime, events_limit = self._get_filter_parameters(state, custom_config)
            unadjusted_now = self.get_current_time()  # get current time before any adjustments
            now = unadjusted_now - timedelta(minutes=1)  # allow for latency of this being triggered
            rate_limited = self._check_rate_limit_reset(unadjusted_now, state)
            if rate_limited:
                return (
                    [],
                    state,
                    False,
                    429,
                    PluginException(
                        preset=PluginException.Preset.RATE_LIMIT,
                        data=f"Previous rate limit in effect until {datetime.fromtimestamp(state.get(self.RATE_LIMIT_RESET_EPOCH), timezone.utc)}. Skipping execution until rate limit reset time has passed.",
                    ),
                )

            now_iso = self.get_iso(now)
            # Whether to convert filter_time in hours to datetime
            if is_filter_datetime:
                filter_hours = filter_time
            else:
                # If false, we assume filter_time is an integer or string representing hours and get datetime
                filter_hours = self.get_iso(now - timedelta(hours=int(filter_time)))  # cutoff point, never query beyond
            next_page_link = state.get(self.NEXT_PAGE_LINK)
            if not state:
                self.logger.info("First run")
                parameters = {"since": filter_hours, "until": now_iso, "limit": events_limit}
                state[self.LAST_COLLECTION_TIMESTAMP] = filter_hours  # we only change this once we get new events
                state[self.LAST_SEARCH_END_TIMESTAMP] = now_iso
            else:
                if next_page_link:
                    state.pop(self.NEXT_PAGE_LINK)
                    self.logger.info("Getting the next page of results...")
                else:
                    parameters = {
                        "since": self.get_since(state, filter_hours, filter_time, is_filter_datetime),
                        "until": now_iso,
                        "limit": events_limit,
                    }
                    # Used to determine the next run time window start. If paginating, do not update this.
                    state[self.LAST_SEARCH_END_TIMESTAMP] = now_iso
                    self.logger.info("Subsequent run...")
            # Call the API
            try:
                self.logger.info(f"Calling Okta with parameters={parameters} and next_page={next_page_link}")
                new_logs_resp = (
                    self.connection.api_client.list_events(parameters)
                    if not next_page_link
                    else self.connection.api_client.get_next_page(next_page_link)
                )
                new_logs = self.get_events(
                    new_logs_resp.json(), state.get(self.LAST_COLLECTION_TIMESTAMP), next_page_link
                )
                next_page_link = self.get_next_page_link(new_logs_resp.headers)

                if next_page_link:
                    state[self.NEXT_PAGE_LINK] = next_page_link
                    has_more_pages = True
                state[self.LAST_COLLECTION_TIMESTAMP] = self.get_last_collection_timestamp(
                    new_logs, state.get(self.LAST_COLLECTION_TIMESTAMP)
                )
                return new_logs, state, has_more_pages, 200, None
            except ApiException as error:
                self.logger.info(f"An API Exception has been raised. Status code: {error.status_code}. Error: {error}")
                if error.status_code == 429:
                    state[self.RATE_LIMIT_RESET_EPOCH] = json.loads(error.data).get("x_rate_limit_reset", 0)
                return [], state, False, error.status_code, error
        except Exception as error:
            self.logger.info(f"An Exception has been raised. Error: {error}")
            return [], state, False, 500, PluginException(preset=PluginException.Preset.UNKNOWN, data=error)

    @staticmethod
    def get_current_time():
        return datetime.now(timezone.utc)

    @staticmethod
    def check_if_datetime(date_time: Any):
        """
        Check if passed value is a date_time, returning True or False
        :param date_time: date_time value, or int/string representing hours
        :return: boolean result based on date_time value type check
        """
        try:
            datetime.fromisoformat(str(date_time).rstrip("Z"))
            return True
        except ValueError:
            return False

    @staticmethod
    def get_iso(time: datetime) -> str:
        """
        Match the timestamp format used in old collector code and the format that Okta uses for 'published' to allow
        comparison in `get_events`. e.g. '2023-10-02T15:43:51.450Z'
        :param time: newly formatted time string value.
        :return: formatted time string.
        """
        return time.isoformat("T", "milliseconds").replace("+00:00", "Z")

    def get_since(self, state: dict, cut_off: str, filter_hours: int, is_date_time: bool) -> str:
        """
        If the customer has paused this task for an extended amount of time we don't want start polling events that
        exceed the cutoff hours. Check if the saved state is beyond this and revert to use the last cutoff hours time.
        Default CUTOFF value.
        :param state: saved state to check and update the time being used.
        :param cut_off: string time of now - default CUTOFF value.
        :param filter_hours: filter time in hours or timestamp
        :param is_date_time: is filter time datetime or hours
        :return: updated time string to use in the parameters.
        """
        saved_time = state.get(self.LAST_SEARCH_END_TIMESTAMP, state.get(self.LAST_COLLECTION_TIMESTAMP))
        if saved_time < cut_off:
            if is_date_time:
                self.logger.info(
                    f"Saved state {saved_time} is before the cut off date ({filter_hours})."
                    f" Reverting to use time: {cut_off}"
                )
            else:
                self.logger.info(
                    f"Saved state {saved_time} exceeds the cut off ({filter_hours} hours)."
                    f" Reverting to use time: {cut_off}"
                )
            state[self.LAST_SEARCH_END_TIMESTAMP] = cut_off
        return state.get(self.LAST_SEARCH_END_TIMESTAMP, state.get(self.LAST_COLLECTION_TIMESTAMP))

    @staticmethod
    def get_next_page_link(headers: dict) -> str:
        """
        Find the next page of results link from the response headers. Header example: `link: <url>; rel="next"`
        :param headers: response headers from the request to Okta.
        :return: next page link if available.
        """
        links = headers.get("link").split(", ")
        next_link = None
        for link in links:
            matched_link = re.match("<(.*?)>", link) if 'rel="next"' in link else None
            next_link = matched_link.group(1) if matched_link else None
        return next_link

    def get_events(self, logs: list, time: str, pagination: str) -> list:
        """
        In the collector code we would iterate over all events and drop any that match the 'since' parameter to make
        sure that we don't double ingest the same event from the previous run (see `get_last_collection_timestamp`).
        :param logs: response json including all returned events from Okta.
        :param time: Last log collection timestamp used for splitting the returned logs into duplicates and new logs.
        :param pagination: next_page_link value to determine if we need to filter
        :return: filtered_logs: removed any events that matched the query start time.
        """

        if pagination:  # we only want to filter on events if it's not a pagination call to Okta (PLGN-431)
            self.logger.info(f"next_page value used to poll from Okta. Returning {len(logs)} event(s) from response.")
            return logs

        # If Okta returns only 1 event (no new events occurred) returned in a previous run we want to remove this.
        if len(logs) == 1 and logs[0].get("published") == time:
            self.logger.info("No new events found since last execution.")
            return []

        log = "Returning {filtered} log event(s) from this iteration."
        # Pop index is instantiated as None to allow for 0 index to be used if needed.
        pop_index, filtered_logs = None, logs
        for index, event in enumerate(logs):
            published = event.get("published")
            if published and published > time:
                pop_index = index
                break
        if pop_index is None:
            # If we reach here then all returned events are older than the last saved event time.
            log += f" All {len(logs)} returned event log(s) are older than the last saved event time."
            filtered_logs = []
        elif pop_index:
            filtered_logs = logs[pop_index:]
            log += f" Removed {pop_index} event log(s) that should have been returned in previous iteration."
        self.logger.info(log.format(filtered=len(filtered_logs)))
        return filtered_logs

    def get_last_collection_timestamp(self, new_logs: list, existing_timestamp: str) -> str:
        """
        Mirror the behaviour in collector code to save the TS of the last parsed event.
        If no new events found then we want to keep the current last parsed event time the same.
        :param new_logs: event logs returned from Okta.
        :param existing_timestamp: string now time in ISO format to use as a fallback if no new logs were returned.
        :return: new time value to save as last collection time for logging purposes.
        """
        new_ts = ""
        if new_logs:  # make sure that logs were returned from Okta otherwise will get index error
            new_ts = new_logs[-1].get("published")
            self.logger.info(f"Saving the last record's published timestamp ({new_ts}).")
        if not new_ts:
            new_ts = existing_timestamp
            self.logger.warning(
                f"No record to use as last timestamp, retaining existing last collection timestamp: {existing_timestamp}"
            )
        return new_ts

    def _get_filter_parameters(self, state: Dict, custom_config: Dict) -> Tuple[Union[Optional[int], Any], bool, int]:
        """
        Apply custom_config params (if provided) to the task. If a lookback value exists, it should take
        precedence (this can allow a larger filter time), otherwise use the default_cutoff value.
        The default_cutoff value is set based on whether this is first run, or a subsequent run.
        :param state: access state dictionary to determine if this is the first run (no state).
        :param custom_config: dictionary passed containing `cutoff` or `lookback` values
        :return: filter_value to be applied in request to Okta
        :return: is_filter_datetime boolean value if filter_value is of type datetime
        :return: events_limit to be applied in request to Okta, defaults to 1000
        """
        filter_cutoff = custom_config.get("cutoff", {}).get("date")
        events_limit = custom_config.get(self.EVENTS_LIMIT, DEFAULT_EVENTS_LIMIT)
        if filter_cutoff is None:
            default_cutoff = DEFAULT_CUTOFF_HOURS
            if not state:
                default_cutoff = DEFAULT_INITIAL_LOOKBACK
            filter_cutoff = custom_config.get("cutoff", {}).get("hours", default_cutoff)

        filter_lookback = custom_config.get("lookback")
        filter_value = filter_lookback if filter_lookback else filter_cutoff
        is_filter_datetime = self.check_if_datetime(filter_value)
        if is_filter_datetime:
            self.logger.info(f"Task execution will be applying a lookback to {filter_value}...")
        else:
            self.logger.info(f"Task execution will be applying filter period of {filter_value} hours...")
        return filter_value, is_filter_datetime, events_limit

    def _check_rate_limit_reset(self, now: datetime, state: Dict) -> bool:
        """
        Check if we are currently rate limited based on saved state value, return a plugin exception if so.
        :param now: current datetime value.
        :param state: state dictionary to determine if this is the first run (no state).
        :return: boolean if currently rate limited.
        """
        rate_limit_reset_epoch = state.get(self.RATE_LIMIT_RESET_EPOCH)
        if rate_limit_reset_epoch:
            current_epoch = int(now.timestamp())
            if current_epoch <= rate_limit_reset_epoch:
                self.logger.info(
                    f"Currently rate limited until epoch time {rate_limit_reset_epoch}. Current epoch time is "
                    f"{current_epoch}."
                )
                return True
            state.pop(self.RATE_LIMIT_RESET_EPOCH)
        return False
