import insightconnect_plugin_runtime
from .schema import MonitorLogsInput, MonitorLogsOutput, MonitorLogsState, Component

# Custom imports below
from insightconnect_plugin_runtime.exceptions import PluginException
from komand_okta.util.exceptions import ApiException
from datetime import datetime, timedelta, timezone
import re


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

    def run(self, params={}, state={}):  # pylint: disable=unused-argument
        self.connection.api_client.toggle_rate_limiting = False
        has_more_pages = False
        parameters = {}
        try:
            now = self.get_current_time() - timedelta(minutes=1)  # allow for latency of this being triggered
            now_iso = now.isoformat()
            next_page_link = state.get(self.NEXT_PAGE_LINK)
            if not state:
                self.logger.info("First run")
                last_24_hours = now - timedelta(hours=24)
                parameters = {"since": last_24_hours.isoformat(), "until": now_iso, "limit": 1000}
                state[self.LAST_COLLECTION_TIMESTAMP] = now_iso
            else:
                if next_page_link:
                    state.pop(self.NEXT_PAGE_LINK)
                    self.logger.info("Getting the next page of results...")
                else:
                    parameters = {"since": state.get(self.LAST_COLLECTION_TIMESTAMP), "until": now_iso, "limit": 1000}
                    self.logger.info("Subsequent run...")
            try:
                self.logger.info(f"Calling Okta with parameters={parameters} and next_page={next_page_link}")
                new_logs_resp = (
                    self.connection.api_client.list_events(parameters)
                    if not next_page_link
                    else self.connection.api_client.get_next_page(next_page_link)
                )
                next_page_link, new_logs = self.get_next_page_link(new_logs_resp.headers), new_logs_resp.json()
                if next_page_link:
                    state[self.NEXT_PAGE_LINK] = next_page_link
                    has_more_pages = True
                state[self.LAST_COLLECTION_TIMESTAMP] = self.get_last_collection_timestamp(now_iso, new_logs)
                return new_logs, state, has_more_pages, 200, None
            except ApiException as error:
                return [], state, False, error.status_code, error
        except Exception as error:
            return [], state, False, 500, PluginException(preset=PluginException.Preset.UNKNOWN, data=error)

    @staticmethod
    def get_current_time():
        return datetime.now(timezone.utc)

    @staticmethod
    def get_next_page_link(headers: dict) -> str:
        links = headers.get("link").split(", ")
        next_link = None
        for link in links:
            matched_link = re.match("<(.*?)>", link) if 'rel="next"' in link else None
            next_link = matched_link.group(1) if matched_link else None
        return next_link

    def get_last_collection_timestamp(self, now: str, new_logs: list) -> str:
        new_ts = ""
        # Mirror the behaviour in collector code to save the TS of the last parsed event as the 'since' time checkpoint.
        if new_logs:  # make sure that logs were returned from Okta otherwise will get index error
            new_ts = new_logs[-1].get("published")
        if not new_ts:
            self.logger.warn(f'No published record to use as last timestamp, reverting to use "now" ({now})')
            new_ts = now

        return new_ts
