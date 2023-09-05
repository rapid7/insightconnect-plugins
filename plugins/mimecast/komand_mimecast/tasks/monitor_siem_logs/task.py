from operator import itemgetter
from time import time

import insightconnect_plugin_runtime
from typing import Dict, List

from insightconnect_plugin_runtime.exceptions import PluginException
from insightconnect_plugin_runtime.helper import get_time_hours_ago

from .schema import MonitorSiemLogsInput, MonitorSiemLogsOutput, MonitorSiemLogsState, Component
from ...util.event import EventLogs
from ...util.exceptions import ApiClientException


class MonitorSiemLogs(insightconnect_plugin_runtime.Task):
    NEXT_TOKEN = "next_token"  # nosec
    HEADER_NEXT_TOKEN = "mc-siem-token"  # nosec
    STATUS_CODE = "status_code"  # nosec
    TOKEN = "token"  # nosec

    def __init__(self):
        super(self.__class__, self).__init__(
            name="monitor_siem_logs",
            description=Component.DESCRIPTION,
            input=MonitorSiemLogsInput(),
            output=MonitorSiemLogsOutput(),
            state=MonitorSiemLogsState(),
        )

    def run(self, params={}, state={}) -> (List[Dict], Dict):
        try:
            has_more_pages = False
            header_next_token = state.get(self.NEXT_TOKEN, "")
            if not header_next_token:
                self.logger.info("First run")
            else:
                self.logger.info("Subsequent run")
                params[self.TOKEN] = header_next_token

            limit_time = time() + 60
            while time() < limit_time:
                try:
                    output, headers, status_code = self.connection.client.get_siem_logs(params)
                except ApiClientException as error:
                    return [], state, has_more_pages, error.status_code, error
                header_next_token = headers.get(self.HEADER_NEXT_TOKEN)
                params[self.TOKEN] = header_next_token
                if not output:
                    break
                output = self._filter_and_sort_recent_events(output)
                if len(output) > 0:
                    break

            if header_next_token:
                state[self.NEXT_TOKEN] = header_next_token
                has_more_pages = True

            return output, state, has_more_pages, status_code, None
        except Exception as error:
            return [], state, has_more_pages, 500, PluginException(preset=PluginException.Preset.UNKNOWN, data=error)

    def _filter_and_sort_recent_events(self, output: List[dict]) -> List[dict]:
        """
        Filters and sorts a list of events to retrieve only the recent events.

        Args:
            events (list): A list of event objects to be filtered and sorted.

        Returns:
            list: The filtered and sorted list of recent events.

        """
        output = [EventLogs(data=event) for event in output]
        output = sorted(
            [event.get_dict() for event in output if event.compare_datetime(get_time_hours_ago(hours_ago=24))],
            key=itemgetter(EventLogs.FILTER_DATETIME),
        )

        for event in output:
            event.pop(EventLogs.FILTER_DATETIME, None)

        return output
