import ast
import re
from operator import itemgetter

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
        if not state:
            self.logger.info("First run")
        else:
            self.logger.info("Subsequent run")
            params[self.TOKEN] = state.get(self.NEXT_TOKEN)

        has_more_pages = False

        while True:
            try:
                output, headers, status_code = self.connection.client.get_siem_logs(params)
            except ApiClientException as error:
                state[self.STATUS_CODE] = error.status_code
                return [], state, has_more_pages
            header_next_token = headers.get(self.HEADER_NEXT_TOKEN)
            params[self.TOKEN] = header_next_token
            if not output:
                break

            output = self._filter_and_sort_recent_events(output)
            if len(output) > 0:
                break

        if header_next_token:
            state[self.NEXT_TOKEN] = headers.get(self.HEADER_NEXT_TOKEN)
            state[self.STATUS_CODE] = status_code
            has_more_pages = True

        return output, state, has_more_pages

    def _filter_and_sort_recent_events(self, output: List[dict]) -> List[dict]:
        """
        Filters and sorts a list of events to retrieve only the recent events.

        Args:
            events (list): A list of event objects to be filtered and sorted.

        Returns:
            list: The filtered and sorted list of recent events.

        """
        output = [EventLogs(data=event) for event in output]
        return sorted(
            [event.get_dict() for event in output if event.compare_datetime(get_time_hours_ago(hours_ago=24))],
            key=itemgetter("datetime"),
        )
