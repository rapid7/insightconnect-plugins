from datetime import datetime, timedelta, timezone
from hashlib import sha1
from typing import Dict

import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException

from komand_proofpoint_tap.util.api import Endpoint
from komand_proofpoint_tap.util.exceptions import ApiException
from komand_proofpoint_tap.util.util import SiemUtils
from .schema import MonitorEventsInput, MonitorEventsOutput, MonitorEventsState, Component

INITIAL_LOOKBACK_HOURS = 24  # Lookback time in hours for first run
SUBSEQUENT_LOOKBACK_HOURS = 24 * 7  # Lookback time in hours for subsequent runs
API_MAX_LOOKBACK = 24 * 7  # API limits to 7 days ago
END_TIME_MINUTES = 60  # End time window of 60 minutes from now


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

    def run(self, params={}, state={}, custom_config={}):  # pylint: disable=unused-argument
        existing_state = state.copy()
        self.connection.client.toggle_rate_limiting = False
        has_more_pages = False
        end_time_minutes = custom_config.get("end_time_minutes", END_TIME_MINUTES)
        try:
            now = self.get_current_time() - timedelta(minutes=1)
            last_collection_date = state.get(self.LAST_COLLECTION_DATE)
            if last_collection_date:
                last_collection_date = datetime.fromisoformat(last_collection_date)
            next_page_index = state.get(self.NEXT_PAGE_INDEX)
            previous_logs_hashes = state.get(self.PREVIOUS_LOGS_HASHES, [])

            first_run = not state
            is_paginating = (not first_run) and next_page_index

            api_limit = self._get_api_limit_date_time(is_paginating, API_MAX_LOOKBACK, now)
            start_time = self._determine_start_time(now, first_run, is_paginating, last_collection_date)
            if custom_config and first_run:
                custom_api_limit, start_time = self._apply_custom_config(
                    now, custom_config, API_MAX_LOOKBACK, start_time
                )
                self.logger.info(
                    f"Attempting to use custom value of {start_time} for start time and {custom_api_limit} for API limit"
                )
                api_limit, _ = self._apply_api_limit(api_limit, custom_api_limit, 0, "custom_api_limit")
            start_time, next_page_index = self._apply_api_limit(api_limit, start_time, next_page_index, "start_time")
            end_time = self._check_end_time((start_time + timedelta(minutes=end_time_minutes)), now).isoformat()
            start_time = start_time.isoformat()
            query_params = {"format": "JSON"}
            parameters = SiemUtils.prepare_time_range(start_time, end_time, query_params)
            self.logger.info(f"Using following parameters in query: {parameters}")

            try:
                parsed_logs = self.parse_logs(
                    self.connection.client.siem_action(Endpoint.get_all_threats(), parameters)
                )
                self.logger.info(f"Retrieved {len(parsed_logs)} total parsed events in time interval")

                current_page_index = next_page_index if next_page_index else 0
                # Send back a maximum of SPLIT_SIZE events at a time (use page index to track this in state)
                new_unique_logs, new_logs_hashes = self.compare_hashes(
                    previous_logs_hashes,
                    parsed_logs[current_page_index * self.SPLIT_SIZE : (current_page_index + 1) * self.SPLIT_SIZE],
                )

                state, has_more_pages = self.determine_page_and_state_values(
                    next_page_index, parsed_logs, has_more_pages, state, parameters, now
                )

                # PLGN-811: reduce the number of pages of hashes we store to prevent hitting DynamoDB limits
                state[self.PREVIOUS_LOGS_HASHES] = (
                    [*previous_logs_hashes[-self.SPLIT_SIZE :], *new_logs_hashes]
                    if current_page_index > 0
                    else new_logs_hashes
                )

                state[self.LAST_COLLECTION_DATE] = end_time

                self.logger.info(f"Retrieved {len(new_unique_logs)} events. Returning has_more_pages={has_more_pages}")
                return new_unique_logs, state, has_more_pages, 200, None

            except ApiException as error:
                if "The requested interval is too short" in error.data:
                    self.logger.info("The requested interval is too short. Retrying in next run.")
                    return [], existing_state, False, 200, None
                if "The requested start time is too far into the past." in error.data:
                    self.logger.info("The requested start time is too far into the past. Resetting state.")
                    return [], {}, False, 200, None

                self.logger.info(f"API Exception occurred: status_code: {error.status_code}, error: {error}")
                state[self.PREVIOUS_LOGS_HASHES] = []
                return [], existing_state, False, error.status_code, error
        except Exception as error:
            self.logger.info(f"Exception occurred in monitor events task: {error}", exc_info=True)
            return (
                [],
                existing_state,
                has_more_pages,
                500,
                PluginException(preset=PluginException.Preset.UNKNOWN, data=error),
            )

    def determine_page_and_state_values(
        self,
        next_page_index: int,
        parsed_logs: list,
        has_more_pages: bool,
        state: Dict[str, str],
        query_params: Dict[str, str],
        now: datetime,
    ) -> (dict, bool):
        # Determine pagination based on the response from API or if we've queried until now.
        if (not next_page_index and len(parsed_logs) > self.SPLIT_SIZE) or (
            next_page_index and (next_page_index + 1) * self.SPLIT_SIZE < len(parsed_logs)
        ):
            state[self.NEXT_PAGE_INDEX] = next_page_index + 1 if next_page_index else 1
            has_more_pages = True
            self.logger.info(
                f"Set next page index to {state[self.NEXT_PAGE_INDEX]} and has more pages to True for the next run"
            )
        else:
            end_str, now_str = query_params.get("interval").split("/")[1], now.isoformat().replace("z", "")

            if now_str != end_str:  # we want to force more pages if the end query time is not 'now'
                self.logger.info("Setting has more pages to True as interval params is not querying until now")
                if state.get(self.NEXT_PAGE_INDEX):
                    state.pop(self.NEXT_PAGE_INDEX)
                has_more_pages = True
        if not has_more_pages and state.get(self.NEXT_PAGE_INDEX):
            state.pop(self.NEXT_PAGE_INDEX)
        return state, has_more_pages

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
        hash_ = sha1(usedforsecurity=False)  # nosec B303
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

    def _check_end_time(self, end_time, now):
        end_time = min(end_time, now)
        return end_time

    def _get_api_limit_date_time(self, is_paginating, limit_delta_hours, now):
        if is_paginating:
            api_limit_date_time = now - timedelta(hours=limit_delta_hours) + timedelta(minutes=5)
        else:
            api_limit_date_time = now - timedelta(hours=limit_delta_hours) + timedelta(minutes=15)
        return api_limit_date_time

    def _apply_api_limit(self, api_limit, time_to_check, next_page_index, time_name):
        if api_limit >= time_to_check:
            self.logger.info(f"Supplied a {time_name} further than allowed. Moving this to {api_limit}")
            time_to_check = api_limit
            if time_to_check == "start_time":
                next_page_index = 0
        return time_to_check, next_page_index

    def _apply_custom_config(self, now, custom_config, default_lookback_hours, start_time):
        cutoff_values = custom_config.get("cutoff", {"hours": default_lookback_hours})
        cutoff_date, cutoff_hours = cutoff_values.get("date", {}), cutoff_values.get("hours")
        if cutoff_date:
            cutoff_date_time = datetime(**cutoff_date, tzinfo=timezone.utc)
        else:
            cutoff_date_time = now - timedelta(hours=cutoff_hours)

        # if using env var we need to convert to dict from string, CPS API will return us a dict.
        specific_date = custom_config.get("lookback")
        if specific_date:
            specific_date = datetime(**specific_date, tzinfo=timezone.utc)
        else:
            specific_date = start_time
        return cutoff_date_time, specific_date

    def _determine_start_time(self, now, first_run, is_paginating, last_collection_date) -> int:
        if first_run:
            integration_status = "First run"
            start_time = now - timedelta(hours=1)
        elif is_paginating:
            integration_status = "Pagination run"
            start_time = last_collection_date - timedelta(hours=1)
        else:
            integration_status = "Subsequent run"
            start_time = last_collection_date
        self.logger.info(f"Integration status: {integration_status}")
        return start_time
