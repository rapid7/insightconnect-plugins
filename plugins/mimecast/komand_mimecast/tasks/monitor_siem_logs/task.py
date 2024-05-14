from operator import itemgetter
from time import time
from datetime import datetime, date

import insightconnect_plugin_runtime
from typing import Dict, List, Any

from insightconnect_plugin_runtime.exceptions import PluginException
from insightconnect_plugin_runtime.helper import get_time_hours_ago

from .schema import MonitorSiemLogsInput, MonitorSiemLogsOutput, MonitorSiemLogsState, Component
from ...util.constants import IS_LAST_TOKEN_FIELD
from ...util.event import EventLogs
from ...util.exceptions import ApiClientException

FIRST_RUN_CUTOFF = 24
NORMAL_RUNNING_CUTOFF = 24 * 7


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
            normal_running_cutoff = state.get("normal_running_cutoff", False)
            filter_time = self._get_filter_time(custom_config, normal_running_cutoff=normal_running_cutoff)

            if not header_next_token:
                self.logger.info("First run...")
            else:
                self.logger.info("Subsequent run using header_next_token...")

            limit_time = time() + 30
            while time() < limit_time:
                try:
                    output, headers, status_code = self.connection.client.get_siem_logs(header_next_token)
                    header_next_token = headers.get(self.HEADER_NEXT_TOKEN, header_next_token)
                    if not output:
                        self.logger.info("No new logs returned from Mimecast")
                        break
                except ApiClientException as error:
                    self.logger.error(
                        f"An exception has been raised during retrieval of siem logs. Status code: {error.status_code} "
                        f"Error: {error}, returning state={state}, has_more_pages={has_more_pages}"
                    )
                    return [], state, has_more_pages, error.status_code, error
                output = self._filter_and_sort_recent_events(output, filter_time)
                if output:
                    break

            if header_next_token:
                self.logger.info(f"The token will be set to '{header_next_token}' in the state.")
                state[self.NEXT_TOKEN] = header_next_token
                # Mimecast API only returns isLastToken in the headers if no more pages, so if it is not present then
                # we know that there are no more pages to be consumed.
                has_more_pages = IS_LAST_TOKEN_FIELD not in headers

                # if we have reached the last page then we have caught up to `now`
                # as result we now then want to use a longer cut off incase the task gets stopped
                if headers.get(IS_LAST_TOKEN_FIELD) and state.get("normal_running_cutoff") is None:
                    state["normal_running_cutoff"] = True

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

    def _filter_and_sort_recent_events(
        self, task_output: List[Dict[str, Any]], filter_time: datetime
    ) -> List[Dict[str, Any]]:
        """
        Filters and sorts a list of events to retrieve only the recent events.

        :param task_output: A list of dictionaries representing the task output to be filtered and sorted.
        :type: List[Dict[str, Any]]

        :param filter_time: how far back in time we filter events from
        :type: datetime

        :return: A new list of dictionaries representing the filtered and sorted recent events.
        :rtype: List[Dict[str, Any]]
        """

        self.logger.info(f"Number of raw logs returned from Mimecast: {len(task_output)}")
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

        if len(task_output) > 0:
            self.logger.info(f"Number of returned logs after filtering performed: {len(task_output)}")
        else:
            self.logger.info("None of the raw logs returned from Mimecast where with in filter timerange")
        if task_output:
            self.logger.info(f"Latest event time returned from Mimecast logs: {latest_time}")
        return task_output

    def _get_filter_time(self, custom_config: Dict[str, int], normal_running_cutoff: bool = False) -> int:
        """
        Apply custom_config params (if provided) to the task. If a lookback value exists, it should take
        precedence (this can allow a larger filter time), In the initial running we want to use a cutoff of
        24 hrs, but for normal running we want to use a look back of 7 days in the event that the task is
        stuck or in an error state for more than 24hrs. Otherwise use the default value.
        :param custom_config: dictionary passed containing `default` or `lookback` values
        :param normal_running_cutoff: if this is the initial run of the Mimecast tasks
        :return: filter time to be applied in `_filter_and_sort_recent_events`
        """

        # if there is a custom config we first check for a custom date, then custom hours back and will use that first
        if custom_config:

            if custom_config.get("lookback", {}):
                filter_time = datetime(
                    custom_config.get("lookback").get("year", date.today().year),
                    custom_config.get("lookback").get("month", 1),
                    custom_config.get("lookback").get("day", 1),
                    custom_config.get("lookback").get("hour", 0),
                    custom_config.get("lookback").get("minute", 0),
                    custom_config.get("lookback").get("second", 0),
                )

            elif custom_config.get("cutoff", {}).get("date"):
                filter_time = datetime(
                    custom_config.get("cutoff", {}).get("date").get("year", date.today().year),
                    custom_config.get("cutoff", {}).get("date").get("month", 1),
                    custom_config.get("cutoff", {}).get("date").get("day", 1),
                    custom_config.get("cutoff", {}).get("date").get("hour", 0),
                    custom_config.get("cutoff", {}).get("date").get("minute", 0),
                    custom_config.get("cutoff", {}).get("date").get("second", 0),
                )

            elif custom_config.get("cutoff", {}).get("hours"):
                filter_time = get_time_hours_ago(hours_ago=int(custom_config.get("cutoff", {}).get("hours")))

        # if this is normal running after its been initally caught up we use  cut off time od 7 days
        elif normal_running_cutoff:
            filter_time = get_time_hours_ago(hours_ago=NORMAL_RUNNING_CUTOFF)

        # If there is no custom config time or its the first run use 24hs
        else:
            filter_time = get_time_hours_ago(hours_ago=FIRST_RUN_CUTOFF)

        self.logger.info(f"The following filter time time will be used: {filter_time}")

        return filter_time
