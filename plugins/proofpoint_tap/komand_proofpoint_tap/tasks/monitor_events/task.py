from datetime import datetime, timedelta, timezone
from hashlib import sha1

import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException

from komand_proofpoint_tap.util.api import Endpoint
from komand_proofpoint_tap.util.exceptions import ApiException
from komand_proofpoint_tap.util.util import SiemUtils
from .schema import MonitorEventsInput, MonitorEventsOutput, MonitorEventsState, Component


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

    def run(self, params={}, state={}):  # pylint: disable=unused-argument
        has_more_pages = False
        try:
            last_collection_date = state.get(self.LAST_COLLECTION_DATE)
            self.logger.info(f"Last collection date retrieved: {last_collection_date}")
            next_page_index = state.get(self.NEXT_PAGE_INDEX)
            now = self.get_current_time() - timedelta(minutes=1)
            max_allowed_lookback = now - timedelta(hours=3)
            # Don't allow collection to go back further than 3 hours max
            if last_collection_date and datetime.fromisoformat(last_collection_date) < max_allowed_lookback:
                last_collection_date = max_allowed_lookback.isoformat()
                if next_page_index:
                    next_page_index = None
                    state.pop(self.NEXT_PAGE_INDEX)
                self.logger.info(f"Last collection date reset to max lookback allowed: {last_collection_date}")

            previous_logs_hashes = state.get(self.PREVIOUS_LOGS_HASHES, [])
            query_params = {"format": "JSON"}

            if not state or not last_collection_date:
                self.logger.info("First run")
                last_hour = now - timedelta(hours=1)
                state[self.LAST_COLLECTION_DATE] = now.isoformat()
                parameters = SiemUtils.prepare_time_range(last_hour.isoformat(), now.isoformat(), query_params)
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
                self.logger.info(f"API Exception occurred: {error}")
                state[self.PREVIOUS_LOGS_HASHES] = []
                return [], state, False, error.status_code, error
        except Exception as error:
            self.logger.info(f"Exception occurred in monitor events task: {error}")
            state[self.PREVIOUS_LOGS_HASHES] = []
            return [], state, has_more_pages, 500, PluginException(preset=PluginException.Preset.UNKNOWN, data=error)

    @staticmethod
    def get_current_time():
        return datetime.now(timezone.utc)

    def parse_logs(self, unparsed_logs: list) -> list:
        parsed_logs = []
        for event_type in ["clicksBlocked", "clicksPermitted", "messagesBlocked", "messagesDelivered"]:
            parsed_logs.extend(self.prepare_log(log, event_type) for log in unparsed_logs.get(event_type, []))
        return parsed_logs

    @staticmethod
    def prepare_log(log: dict, value: str) -> dict:
        log["eventType"] = value

        # preventing random sorting of the list to ensure that the same hash is generated with each request
        if log.get("messageParts"):
            log["messageParts"] = sorted(log.get("messageParts", []), key=lambda part: part.get("md5", ""))
        return dict(sorted(log.items()))

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
