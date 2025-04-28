from operator import itemgetter
from time import time
from datetime import datetime, date
import hashlib

import insightconnect_plugin_runtime
from typing import Dict, List, Any, Tuple

from insightconnect_plugin_runtime.exceptions import PluginException, APIException
from insightconnect_plugin_runtime.helper import get_time_hours_ago
from requests import Response

from .schema import MonitorSiemLogsInput, MonitorSiemLogsOutput, MonitorSiemLogsState, Component
from komand_mimecast.util.constants import IS_LAST_TOKEN_FIELD, RATE_LIMIT_ASSISTANCE
from komand_mimecast.util.event import EventLogs
from komand_mimecast.util.exceptions import ApiClientException
from komand_mimecast.util.util import Utils

FIRST_RUN_CUTOFF = 24
NORMAL_RUNNING_CUTOFF = 24 * 7
MAX_EVENTS_PER_RUN_DEFAULT = 7500


class MonitorSiemLogs(insightconnect_plugin_runtime.Task):
    NEXT_TOKEN = "next_token"  # nosec
    HEADER_NEXT_TOKEN = "mc-siem-token"  # nosec
    STATUS_CODE = "status_code"  # nosec
    RATE_LIMIT_DATETIME = "rate_limit_datetime"

    NORMAL_RUNNING_CUTOFF = "normal_running_cutoff"  # nosec
    LAST_LOG_LINE = "last_log_line"  # nosec
    LAST_RUNS_FILTER_TIME = "last_runs_filter_time"  # nosec
    PREVIOUS_FILE_HASH = "previous_file_hash"  # nosec
    CUSTOM_LOG_MESSAGE = "custom_log_message"  # nosec
    CUSTOM_STATUS = "custom_status"  # nosec
    CUSTOM_ASSISTANCE = "custom_assistance"  # nosec

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
            self.check_for_messages(custom_config)
            rate_limited = self.check_rate_limit(state)
            if rate_limited:
                return [], state, False, 429, rate_limited
            has_more_pages = False
            header_next_token = state.get(self.NEXT_TOKEN, "")
            normal_running_cutoff = state.get(self.NORMAL_RUNNING_CUTOFF, False)

            last_log_line = state.get(self.LAST_LOG_LINE, 0)
            last_runs_filter_time = state.get(self.LAST_RUNS_FILTER_TIME)
            previous_file_hash = state.get(self.PREVIOUS_FILE_HASH, "")

            max_events_per_run = custom_config.get("max_events_per_run", MAX_EVENTS_PER_RUN_DEFAULT)

            if last_runs_filter_time:
                # we need to pin the filter time so the same filtering occurs between runs on the same file
                filter_time = datetime.fromisoformat(last_runs_filter_time)
            else:
                filter_time = self._get_filter_time(custom_config, normal_running_cutoff=normal_running_cutoff)

            if not header_next_token:
                self.logger.info("First run...")
            elif last_log_line > 0:
                self.logger.info("Subsequent run, continuing to process the previous file...")
            else:
                self.logger.info("Subsequent run using header_next_token...")

            limit_time = time() + 30
            while time() < limit_time:
                try:
                    output, headers, status_code, file_name_list = self.connection.client.get_siem_logs(
                        header_next_token
                    )
                    header_next_token = headers.get(self.HEADER_NEXT_TOKEN, header_next_token)
                    if not output:
                        self.logger.info("No new logs returned from Mimecast")
                        last_log_line = 0
                        break
                except ApiClientException as error:
                    self.logger.error(
                        f"An exception has been raised during retrieval of siem logs. Status code: {error.status_code} "
                        f"Error: {error}, returning state={state}, has_more_pages={has_more_pages}"
                    )
                    status_code, error, has_more_pages = self.check_rate_limit_error(
                        error, error.response, error.status_code, state
                    )
                    return [], state, has_more_pages, status_code, error

                # check if the hashed file list from the previous run is the same as this run
                if len(output) > max_events_per_run:
                    current_file_hash = self._check_hash_of_file_names(file_name_list)

                    # if the hash lists don't match then we want to reset the last log to 0 and start again
                    if last_log_line > 0 and current_file_hash != previous_file_hash:
                        self.logger.info(
                            "The hashes between the current run and previous runs do not match, resetting the last log line to 0."
                        )
                        last_log_line = 0
                else:
                    last_log_line = 0

                output, last_log_line = self._filter_and_sort_recent_events(
                    output, filter_time, last_log_line, max_events_per_run
                )
                if output:
                    break

            if header_next_token and last_log_line == 0:
                self.logger.info(f"The token will be set to '{header_next_token}' in the state.")
                state[self.NEXT_TOKEN] = header_next_token
                # Mimecast API only returns isLastToken in the headers if no more pages, so if it is not present then
                # we know that there are no more pages to be consumed.
                has_more_pages = IS_LAST_TOKEN_FIELD not in headers

                # if we have reached the last page then we have caught up to `now`
                # as result we now then want to use a longer cut off incase the task gets stopped
                if headers.get(IS_LAST_TOKEN_FIELD) and state.get("normal_running_cutoff") is None:
                    self.logger.info("Caught up, saving 'normal_running_cutoff' as 'True' to the state")
                    state["normal_running_cutoff"] = True

            state[self.LAST_LOG_LINE] = last_log_line

            if last_log_line > 0:
                state[self.LAST_RUNS_FILTER_TIME] = filter_time.isoformat()
                state[self.PREVIOUS_FILE_HASH] = current_file_hash
                has_more_pages = True
            else:
                state.pop(self.LAST_RUNS_FILTER_TIME, None)
                state.pop(self.PREVIOUS_FILE_HASH, None)

            return output, state, has_more_pages, status_code, None
        except APIException as api_error:
            self.logger.error("An exception has been raised.")
            self.logger.info(f"Error cause: {api_error.cause}")
            self.logger.info(f"Error assistance: {api_error.assistance}")
            return [], state, False, api_error.status_code, api_error
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
        self, task_output: List[Dict[str, Any]], filter_time: datetime, last_log_line: int, max_events_per_run: int
    ) -> Tuple[List[Dict[str, Any]], int]:
        """
        Filters and sorts a list of events to retrieve only the recent events.

        :param task_output: A list of dictionaries representing the task output to be filtered and sorted.
        :type: List[Dict[str, Any]]

        :param filter_time: how far back in time we filter events from
        :type: datetime

        :param last_log_line: how may lines of the log file has already been processed
        :type: int

        :param max_events_per_run: The max number of events to parse in a run
        :type: int

        :return: A tuple containing, a new list of dictionaries representing the filtered and sorted recent events and a number of processed log lines.
        :rtype: Tuple[List[Dict[str, Any]], int]
        """

        self.logger.info(f"Number of raw logs returned from Mimecast: {len(task_output)}")
        task_output = sorted(
            map(
                lambda event: event.get_dict(),
                filter(
                    lambda event: event.compare_datetime(filter_time),
                    [EventLogs(data=event, logger=self.logger) for event in task_output],
                ),
            ),
            key=itemgetter(EventLogs.FILTER_DATETIME),
        )

        if len(task_output) > max_events_per_run:
            start_point = last_log_line
            end_point = start_point + max_events_per_run

            if end_point > len(task_output) - 1:
                end_point = len(task_output) - 1
                last_log_line = 0
            else:
                last_log_line = end_point

            self.logger.info(
                f"Number of returned logs after filtering performed was greater than {max_events_per_run}, limiting to {max_events_per_run}.\n"
                f"fetching logs from {start_point} to {end_point}, using the filter time of {filter_time}"
            )

            task_output = task_output[start_point:end_point]

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
        return task_output, last_log_line

    def _check_hash_of_file_names(self, file_name_list: List[str]) -> str:
        file_name_list = sorted(file_name_list)
        return hashlib.md5(str(file_name_list).encode("utf-8")).hexdigest()  # nosec B324

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

            custom_config_lookback = custom_config.get("lookback", {})
            custom_config_date = custom_config.get("cutoff", {}).get("date", {})
            custom_config_hours = custom_config.get("cutoff", {}).get("hours")

            if custom_config_lookback:
                filter_time = datetime(
                    custom_config_lookback.get("year", date.today().year),
                    custom_config_lookback.get("month", 1),
                    custom_config_lookback.get("day", 1),
                    custom_config_lookback.get("hour", 0),
                    custom_config_lookback.get("minute", 0),
                    custom_config_lookback.get("second", 0),
                )

            elif custom_config_date:
                filter_time = datetime(
                    custom_config_date.get("year", date.today().year),
                    custom_config_date.get("month", 1),
                    custom_config_date.get("day", 1),
                    custom_config_date.get("hour", 0),
                    custom_config_date.get("minute", 0),
                    custom_config_date.get("second", 0),
                )

            elif custom_config_hours:
                filter_time = get_time_hours_ago(hours_ago=int(custom_config_hours))

        # if this is normal running after its been initially caught up we use  cut off time od 7 days
        elif normal_running_cutoff:
            filter_time = get_time_hours_ago(hours_ago=NORMAL_RUNNING_CUTOFF)

        # If there is no custom config time or its the first run use 24hs
        else:
            filter_time = get_time_hours_ago(hours_ago=FIRST_RUN_CUTOFF)

        self.logger.info(f"The following filter time will be used: {filter_time}")

        return filter_time

    def check_rate_limit(self, state: Dict):
        rate_limited = state.get(self.RATE_LIMIT_DATETIME)
        now = time()
        if rate_limited:
            rate_limit_string = Utils.convert_epoch_to_readable(rate_limited)
            log_msg = f"Rate limit value stored in state: {rate_limit_string}. "
            if rate_limited > now:
                log_msg += "Still within rate limiting period, skipping task execution..."
                self.logger.info(log_msg)
                error = PluginException(
                    cause=PluginException.causes.get(PluginException.Preset.RATE_LIMIT),
                    assistance=RATE_LIMIT_ASSISTANCE,
                )
                return error

            log_msg += "However no longer in rate limiting period, so task can be executed..."
            del state[self.RATE_LIMIT_DATETIME]
            self.logger.info(log_msg)

    def check_rate_limit_error(
        self, error: ApiClientException, response: Response, status_code: int, state: dict
    ) -> Tuple[int, Any, bool]:
        if status_code == 429:
            new_run_time = time() + 600  # default to wait 10 minutes before the next run
            try:
                # This value should be the amount of time in milliseconds until the next call is allowed
                rate_limit_response_time = response.headers.get("X-RateLimit-Reset")
                if rate_limit_response_time:
                    self.logger.info(f"Got X-RateLimit-Reset value from headers: {rate_limit_response_time}")
                    new_run_time = time() + (int(rate_limit_response_time) / 1000)
                new_run_time_string = Utils.convert_epoch_to_readable(new_run_time)
                self.logger.error(f"A rate limit error has occurred, task will resume after {new_run_time_string}")
                state[self.RATE_LIMIT_DATETIME] = new_run_time
            except Exception as err:
                self.logger.error(
                    f"Unable to calculate new run time, no rate limiting applied to the state. Error: {repr(err)}",
                    exc_info=True,
                )
            return 200, None, True
        return status_code, error, False

    def check_for_messages(self, custom_config: Dict[str, Any]) -> None:
        custom_log_message = custom_config.get(self.CUSTOM_LOG_MESSAGE)
        custom_status = custom_config.get(self.CUSTOM_STATUS, 200)
        if custom_status != 200:
            raise APIException(
                cause=custom_log_message,
                assistance=custom_config.get(
                    self.CUSTOM_ASSISTANCE, PluginException.assistances.get(PluginException.Preset.UNKNOWN)
                ),
                status_code=custom_status,
            )
        if custom_log_message:
            self.logger.info(custom_log_message)
