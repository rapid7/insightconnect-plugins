import insightconnect_plugin_runtime
from .schema import MonitorLogsInput, MonitorLogsOutput, MonitorLogsState, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
from komand_okta.util.exceptions import ApiException
from datetime import datetime, timedelta, timezone
from typing import Dict
import re

CUTOFF = 24


class MonitorLogs(insightconnect_plugin_runtime.Task):
    LAST_COLLECTION_TIMESTAMP = "last_collection_timestamp"
    NEXT_PAGE_LINK = "next_page_link"
    STATUS_CODE = "status_code"

    def __init__(self):
        super(self.__class__, self).__init__(
            name="monitor_logs",
            description=Component.DESCRIPTION,
            input=MonitorLogsInput(),
            output=MonitorLogsOutput(),
            state=MonitorLogsState(),
        )

    def run(self, params={}, state={}, custom_config={}):  # pylint: disable=unused-argument
        self.connection.api_client.toggle_rate_limiting = False
        has_more_pages = False
        parameters = {}
        try:
            filter_time = self._get_filter_time(custom_config)
            now = self.get_current_time() - timedelta(minutes=1)  # allow for latency of this being triggered
            now_iso = self.get_iso(now)
            filter_hours = self.get_iso(now - timedelta(hours=filter_time))  # cut off point - never query beyond
            # cutoff hours
            next_page_link = state.get(self.NEXT_PAGE_LINK)
            if not state:
                self.logger.info("First run")
                parameters = {"since": filter_hours, "until": now_iso, "limit": 1000}
                state[self.LAST_COLLECTION_TIMESTAMP] = filter_hours  # we only change this once we get new events
            else:
                if next_page_link:
                    state.pop(self.NEXT_PAGE_LINK)
                    self.logger.info("Getting the next page of results...")
                else:
                    parameters = {
                        "since": self.get_since(state, filter_hours, filter_time),
                        "until": now_iso,
                        "limit": 1000,
                    }
                    self.logger.info("Subsequent run...")
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
                state[self.LAST_COLLECTION_TIMESTAMP] = self.get_last_collection_timestamp(new_logs, state)
                return new_logs, state, has_more_pages, 200, None
            except ApiException as error:
                self.logger.info(f"An API Exception has been raised. Status code: {error.status_code}. Error: {error}")
                return [], state, False, error.status_code, error
        except Exception as error:
            self.logger.info(f"An Exception has been raised. Error: {error}")
            return [], state, False, 500, PluginException(preset=PluginException.Preset.UNKNOWN, data=error)

    @staticmethod
    def get_current_time():
        return datetime.now(timezone.utc)

    @staticmethod
    def get_iso(time: datetime) -> str:
        """
        Match the timestamp format used in old collector code and the format that Okta uses for 'published' to allow
        comparison in `get_events`. e.g. '2023-10-02T15:43:51.450Z'
        :param time: newly formatted time string value.
        :return: formatted time string.
        """
        return time.isoformat("T", "milliseconds").replace("+00:00", "Z")

    def get_since(self, state: dict, cut_off: str, filter_hours: int) -> str:
        """
        If the customer has paused this task for an extended amount of time we don't want start polling events that
        exceed the cutoff hours. Check if the saved state is beyond this and revert to use the last cutoff hours time.
        Default 24 hours.
        :param state: saved state to check and update the time being used.
        :param cut_off: string time of now - default 24 hours.
        :param filter_hours: filter time in hours
        :return: updated time string to use in the parameters.
        """
        saved_time = state.get(self.LAST_COLLECTION_TIMESTAMP)

        if saved_time < cut_off:
            self.logger.info(
                f"Saved state {saved_time} exceeds the cut off ({filter_hours} hours)."
                f" Reverting to use time: {cut_off}"
            )
            state[self.LAST_COLLECTION_TIMESTAMP] = cut_off

        return state[self.LAST_COLLECTION_TIMESTAMP]

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
        :param time: 'since' parameter being used to query Okta.
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
        pop_index, filtered_logs = 0, logs

        for index, event in enumerate(logs):
            published = event.get("published")
            if published and published > time:
                pop_index = index
                break
        if pop_index:
            filtered_logs = logs[pop_index:]
            log += f" Removed {pop_index} event log(s) that should have been returned in previous iteration."
        self.logger.info(log.format(filtered=len(filtered_logs)))
        return filtered_logs

    def get_last_collection_timestamp(self, new_logs: list, state: dict) -> str:
        """
        Mirror the behaviour in collector code to save the TS of the last parsed event as the 'since' time checkpoint.
        If no new events found then we want to keep the current checkpoint the same.
        :param new_logs: event logs returned from Okta.
        :param state: access state dictionary to get the current checkpoint in time if no new logs.
        :return: new time value to save as the checkpoint to query 'since' on the next run.
        """
        new_ts = ""
        if new_logs:  # make sure that logs were returned from Okta otherwise will get index error
            new_ts = new_logs[-1].get("published")
            self.logger.info(f"Saving the last record's published timestamp ({new_ts}) as checkpoint.")
        if not new_ts:
            state_time = state.get(self.LAST_COLLECTION_TIMESTAMP)
            self.logger.warning(
                f"No record to use as last timestamp, will not move checkpoint forward. "
                f"Keeping value of {state_time}"
            )
            new_ts = state_time

        return new_ts

    def _get_filter_time(self, custom_config: Dict[str, int]) -> int:
        """
        Apply custom_config params (if provided) to the task. If a lookback value exists, it should take
        precedence (this can allow a larger filter time), otherwise use the default value.
        :param custom_config: dictionary passed containing `default` or `lookback` values
        :return: filter time to be applied in `_filter_and_sort_recent_events`
        """

        default, lookback = custom_config.get("default", CUTOFF), custom_config.get("lookback")
        filter_value = lookback if lookback else default
        self.logger.info(f"Task execution will be applying filter period of {filter_value} hours...")
        return int(filter_value)
