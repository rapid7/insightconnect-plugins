import insightconnect_plugin_runtime
from .schema import MonitorEventsInput, MonitorEventsOutput, MonitorEventsState, Component

# Custom imports below
from datetime import datetime, timedelta, timezone
from komand_proofpoint_tap.util.api import Endpoint
from komand_proofpoint_tap.util.util import SiemUtils
from komand_proofpoint_tap.util.exceptions import ApiException
from hashlib import sha1
from komand_proofpoint_tap.util.helpers import clean


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
        last_collection_date = state.get(self.LAST_COLLECTION_DATE)
        next_page_index = state.get(self.NEXT_PAGE_INDEX)
        previous_logs_hashes = state.get(self.PREVIOUS_LOGS_HASHES, [])
        has_more_pages = False

        query_params = {"format": "JSON"}

        if not state:
            self.logger.info("First run")
            now = self.get_current_time() - timedelta(minutes=1)
            last_hour = now - timedelta(hours=1)
            state[self.LAST_COLLECTION_DATE] = now.isoformat()
            parameters = SiemUtils.prepare_time_range(last_hour.isoformat(), now.isoformat(), query_params)
        else:
            if next_page_index:
                state.pop(self.NEXT_PAGE_INDEX)
                self.logger.info("Getting the next page of results...")
                parameters = SiemUtils.prepare_time_range(
                    (datetime.fromisoformat(last_collection_date) - timedelta(hours=1)).isoformat(),
                    last_collection_date,
                    query_params,
                )
            else:
                self.logger.info("Subsequent run")
                now = self.get_current_time() - timedelta(minutes=1)
                state[self.LAST_COLLECTION_DATE] = now.isoformat()
                last_hour = now - timedelta(hours=1)
                parameters = SiemUtils.prepare_time_range(last_hour.isoformat(), now.isoformat(), query_params)
        try:
            parsed_logs = self.parse_logs(
                clean(self.connection.client.siem_action(Endpoint.get_all_threats(), parameters))
            )

            if (not next_page_index and len(parsed_logs) > self.SPLIT_SIZE) or (
                next_page_index and (next_page_index + 1) * self.SPLIT_SIZE < len(parsed_logs)
            ):
                state[self.NEXT_PAGE_INDEX] = next_page_index + 1 if next_page_index else 1
                has_more_pages = True

            state[self.STATUS_CODE] = 200
            current_page_index = next_page_index if next_page_index else 0
            new_unique_logs, new_logs_hashes = self.compare_hashes(
                previous_logs_hashes,
                parsed_logs[current_page_index * self.SPLIT_SIZE : (current_page_index + 1) * self.SPLIT_SIZE],
            )
            state[self.PREVIOUS_LOGS_HASHES] = (
                [*previous_logs_hashes, *new_logs_hashes] if current_page_index > 0 else new_logs_hashes
            )
            return new_unique_logs, state, has_more_pages

        except ApiException as error:
            state[self.STATUS_CODE] = error.status_code
            state[self.PREVIOUS_LOGS_HASHES] = []
            return [], state, False

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
        return logs_to_return, new_logs_hashes
