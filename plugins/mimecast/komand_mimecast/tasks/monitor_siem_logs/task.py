from operator import itemgetter
from time import time

import insightconnect_plugin_runtime
from typing import Dict, List, Any

from insightconnect_plugin_runtime.exceptions import PluginException
from insightconnect_plugin_runtime.helper import get_time_hours_ago

from .schema import MonitorSiemLogsInput, MonitorSiemLogsOutput, MonitorSiemLogsState, Component
from ...util.constants import IS_LAST_TOKEN_FIELD
from ...util.event import EventLogs
from ...util.exceptions import ApiClientException

CUTOFF = 24


class MonitorSiemLogs(insightconnect_plugin_runtime.Task):
    NEXT_TOKEN = "next_token"  # nosec
    HEADER_NEXT_TOKEN = "mc-siem-token"  # nosec
    STATUS_CODE = "status_code"  # nosec

    def __init__(self):
        super(self.__class__, self).__init__(
            name="monitor_siem_logs",
            description=Component.DESCRIPTION,
            input=MonitorSiemLogsInput(),
            output=MonitorSiemLogsOutput(),
            state=MonitorSiemLogsState(),
        )

    def run(self, params={}, state={}) -> (List[Dict], Dict):  # pylint: disable=unused-argument # noqa: MC0001
        try:
            has_more_pages = False
            header_next_token = state.get(self.NEXT_TOKEN, "")

            if not header_next_token:
                self.logger.info("First run...")
            else:
                self.logger.info("Subsequent run using header_next_token...")

            limit_time = time() + 30
            while time() < limit_time:
                try:
                    output, headers, status_code = self.connection.client.get_siem_logs(header_next_token)
                    if not output:
                        break
                except ApiClientException as error:
                    self.logger.error(
                        f"An exception has been raised during retrieval of siem logs. Status code: {error.status_code} "
                        f"Error: {error}, returning state={state}, has_more_pages={has_more_pages}"
                    )
                    return [], state, has_more_pages, error.status_code, error
                header_next_token = headers.get(self.HEADER_NEXT_TOKEN)
                output = self._filter_and_sort_recent_events(output)
                if output:
                    break

            if header_next_token:
                state[self.NEXT_TOKEN] = header_next_token
                has_more_pages = IS_LAST_TOKEN_FIELD not in headers

            return output, state, has_more_pages, status_code, None
        except Exception as gen_error:
            gen_info, exp = f"Error: {gen_error}, returning state={state}, has_more_pages={has_more_pages}", None
            if "negative seek" in str(gen_error):
                # this seems to be intermittent on what Mimecast returns, don't log with word `error`
                self.logger.debug(f"Found negative seek. {gen_info}", exc_info=True)
            else:
                self.logger.error(f"An exception has been raised. {gen_info}", exc_info=True)
                exp = PluginException(preset=PluginException.Preset.UNKNOWN, data=gen_error)
            return [], state, has_more_pages, 500, exp

    def _filter_and_sort_recent_events(self, task_output: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Filters and sorts a list of events to retrieve only the recent events.

        :param task_output: A list of dictionaries representing the task output to be filtered and sorted.
        :type: List[Dict[str, Any]]

        :return: A new list of dictionaries representing the filtered and sorted recent events.
        :rtype: List[Dict[str, Any]]
        """

        self.logger.info(f"Number of raw logs returned from Mimecast: {len(task_output)}")
        task_output = sorted(
            map(
                lambda event: event.get_dict(),
                filter(
                    lambda event: event.compare_datetime(get_time_hours_ago(hours_ago=CUTOFF)),
                    [EventLogs(data=event) for event in task_output],
                ),
            ),
            key=itemgetter(EventLogs.FILTER_DATETIME),
        )

        for event in task_output:
            event.pop(EventLogs.FILTER_DATETIME, None)
        self.logger.info(f"Number of returned logs after filtering performed: {len(task_output)}")

        return task_output
