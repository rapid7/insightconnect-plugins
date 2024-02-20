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

    def run(  # pylint: disable=unused-argument # noqa: MC0001
        self, params={}, state={}, custom_config={}
    ) -> (List[Dict], Dict, Dict):
        try:
            has_more_pages = False
            header_next_token = state.get(self.NEXT_TOKEN, "")
            filter_time = self._get_filter_time(custom_config)

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
                output = self._filter_and_sort_recent_events(output, filter_time)
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

    def _filter_and_sort_recent_events(self, task_output: List[Dict[str, Any]], cut_off: int) -> List[Dict[str, Any]]:
        """
        Filters and sorts a list of events to retrieve only the recent events.

        :param task_output: A list of dictionaries representing the task output to be filtered and sorted.
        :type: List[Dict[str, Any]]

        :param cut_off: integer specifying how far back in time we filter events from
        :type: integer

        :return: A new list of dictionaries representing the filtered and sorted recent events.
        :rtype: List[Dict[str, Any]]
        """

        self.logger.info(f"Number of raw logs returned from Mimecast: {len(task_output)}")
        filter_time = get_time_hours_ago(hours_ago=cut_off)
        task_output = sorted(
            map(
                lambda event: event.get_dict(),
                filter(
                    lambda event: event.compare_datetime(filter_time),
                    [EventLogs(data=event) for event in task_output],
                ),
            ),
            key=itemgetter(EventLogs.FILTER_DATETIME),
        )
        latest_time = filter_time
        for event in task_output:
            event_date_time = event.get(EventLogs.FILTER_DATETIME)
            latest_time = event_date_time if event_date_time > latest_time else latest_time
            event.pop(EventLogs.FILTER_DATETIME, None)
        self.logger.info(f"Number of returned logs after filtering performed: {len(task_output)}")
        if task_output:
            self.logger.info(f"Latest event time returned from Mimecast logs: {latest_time}")
        return task_output

    def _get_filter_time(self, custom_config: Dict[str, int]) -> int:
        """
        We want to apply the custom_config params if provided to the task. The logic is that if
        a lookback value exists, this should take precedence to allow a larger filter time and only
        once this no longer exists do we want to use the default value.
        :param custom_config: dictionary passed containing `default` or `lookback` values
        :return: filter time to be applied in `_filter_and_sort_recent_events`
        """

        default, lookback = custom_config.get("default", CUTOFF), custom_config.get("lookback")
        filter_value = lookback if lookback else default
        self.logger.info(f"Task execution will be applying filter period of {filter_value} hours...")
        return int(filter_value)
