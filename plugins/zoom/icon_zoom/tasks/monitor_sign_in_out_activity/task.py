import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException
from insightconnect_plugin_runtime.telemetry import monitor_task_delay

from .schema import (
    MonitorSignInOutActivityInput,
    MonitorSignInOutActivityOutput,
    MonitorSignInOutActivityState,
    Component,
)

# Custom imports below
from datetime import datetime, timedelta, timezone, date
from typing import Optional

from icon_zoom.tasks.enums import RunState
from icon_zoom.tasks.dataclasses import TaskOutput
from icon_zoom.util.api import AuthenticationRetryLimitError, AuthenticationError
from icon_zoom.util.event import Event
from typing import Dict, Any


class MonitorSignInOutActivity(insightconnect_plugin_runtime.Task):
    MAX_PAGE_SIZE = 300
    # State constants
    LAST_REQUEST_TIMESTAMP = "last_request_timestamp"
    LATEST_EVENT_TIMESTAMP = "latest_event_timestamp"
    # Latch is used to identify the latest timestamp between pages
    # Once pagination is complete, the latest_event_timestamp may become the latest_event_timestamp_latch
    LATEST_EVENT_TIMESTAMP_LATCH = "latest_event_timestamp_latch"
    STATUS_CODE = "status_code"
    PREVIOUS_RUN_STATE = "previous_run_state"
    PREVIOUS_COMPLETED_QUERY_DATE = "previous_completed_query_date"
    # State constants related to pagination
    NEXT_PAGE_TOKEN = "next_page_token"  # nosec
    PARAM_START_DATE = "param_start_date"
    PARAM_END_DATE = "param_end_date"

    # Constants for time formatting and event date logic
    ZOOM_TIME_FORMAT = "%Y-%m-%dT%H:%M:%SZ"
    ZERO_DATE = "0001-01-01T00:00:00Z"

    AUTHENTICATION_RETRY_LIMIT_ERROR_MESSAGE_CAUSE = "OAuth authentication retry limit was met."
    AUTHENTICATION_RETRY_LIMIT_ERROR_MESSAGE_ASSISTANCE = (
        "Ensure your OAuth connection credentials are valid. If running a large number of "
        "integrations with Zoom, consider increasing the OAuth authentication "
        "retry limit to accommodate."
    )
    AUTHENTICATION_ERROR_MESSAGE = (
        "The OAuth token credentials provided in the connection "
        "configuration is invalid. Please verify the credentials are correct "
        "and try again."
    )
    API_CHANGED_ERROR_MESSAGE_CAUSE = "The Zoom API has changed and is no longer supported by this plugin."
    API_CHANGED_ERROR_MESSAGE_ASSISTANCE = "Please contact support for assistance."
    PERMISSIONS_ERROR_MESSAGE = (
        "Health check failed. An error occurred during event collection: insufficient permissions for this action. "
        "Please ensure you add all required scopes for the Rapid7 app in Zoom."
    )
    PERMISSIONS_ERROR_MESSAGE_USER = (
        "Health check failed. An error occurred during event collection: insufficient permissions for this action. "
        "Please ensure you add all required user permissions for the Rapid7 app in Zoom."
    )
    # Default cutoff hours for query params
    DEFAULT_CUTOFF_HOURS = 168
    DEFAULT_INITIAL_LOOKBACK = 24

    def __init__(self):
        super(self.__class__, self).__init__(
            name="monitor_sign_in_out_activity",
            description=Component.DESCRIPTION,
            input=MonitorSignInOutActivityInput(),
            output=MonitorSignInOutActivityOutput(),
            state=MonitorSignInOutActivityState(),
        )

    # pylint: disable=unused-argument
    @monitor_task_delay(timestamp_keys=[LATEST_EVENT_TIMESTAMP], default_delay_threshold="2d")
    def run(self, params={}, state={}, custom_config={}):
        try:
            task_output: TaskOutput = self.loop(state=state, custom_config=custom_config)

            # Turn events list back into a list of dicts
            output = [event.__dict__ for event in task_output.output]
            return output, task_output.state, task_output.has_more_pages, task_output.status_code, task_output.error

        except Exception as error:
            self.logger.error(
                f"An Exception has been raised. Unhandled exception occurred during {self.name} task: {error}"
            )
            return [], {}, False, 500, PluginException(preset=PluginException.Preset.UNKNOWN, data=error)

    def loop(self, state: Dict[str, Any], custom_config: Dict[str, Any]):  # noqa: C901
        now = self._format_datetime_for_zoom(dt=self._get_datetime_now())
        run_state = self.determine_runstate(state=state)
        self.logger.info(f"Current runstate is: {run_state.value}")

        cutoff = custom_config.get("cutoff", {})
        cutoff_date = cutoff.get("date")
        cutoff_hours = cutoff.get("hours")
        lookback = custom_config.get("lookback")

        start_time = self.get_start_time(lookback, cutoff_date, cutoff_hours, run_state)

        start_date_params = {
            RunState.starting: start_time,
            RunState.paginating: state.get(self.PARAM_START_DATE),
            RunState.continuing: self._get_last_valid_timestamp(start_time, state.get(self.LAST_REQUEST_TIMESTAMP)),
        }

        end_date_params = {
            RunState.starting: now,
            RunState.paginating: state.get(self.PARAM_END_DATE),
            RunState.continuing: now,
        }

        param_request_start_date = start_date_params[run_state]
        param_request_end_date = end_date_params[run_state]

        range_previously_queried = self.check_if_previously_queried(
            state.get(self.PREVIOUS_COMPLETED_QUERY_DATE), param_request_end_date
        )

        self.logger.info(
            f"Getting events for timeframe {param_request_start_date} to {param_request_end_date}. "
            f"Currently paginating: {run_state == RunState.paginating}"
        )

        try:
            next_page_token = state.get(self.NEXT_PAGE_TOKEN)
            if next_page_token:
                self.logger.info(f"About to paginate with token: {next_page_token}")

            new_events, pagination_token = self.connection.zoom_api.get_user_activity_events_task(
                start_date=param_request_start_date,
                end_date=param_request_end_date,
                page_size=self.MAX_PAGE_SIZE,
                next_page_token=next_page_token,
            )
        except Exception as exception:
            if hasattr(exception, "data") and "The next page token is invalid or expired." in exception.data:
                return self.handle_pagination_token_error(exception=exception, state=state)
            else:
                self.logger.error(f"An Exception has been raised. Error: {exception}, returning state={state}")
                return self.handle_request_exception(exception=exception, now=now)

        try:
            new_events = sorted([Event(**event) for event in new_events])
        except TypeError as exception:
            self.logger.error(
                f"A TypeError has been raised. Zoom API endpoint output has changed, unable to parse events: {exception}"
            )
            return self.handle_api_changed_exception(now=now)

        # Latest event is used for boundary hash calculation and de-duping if needed
        self.logger.info(f"Got {len(new_events)} raw events from Zoom (pre-deduping)!")
        try:
            latest_event = new_events[-1]
            self.logger.info(f"Latest event from raw event set is {latest_event.time}")
        except IndexError:
            self.logger.info("Unable to get latest event time, no new events found!")
            return self.handle_no_new_events_found(now=now, query_end_date=param_request_end_date)

        # Dedupe if the date range has been previously queried to completion as no new events earlier than the latest
        # event timestamp will be added on subsequent requests
        if range_previously_queried:
            dedupe_timestamp = state.get(self.LATEST_EVENT_TIMESTAMP)
            self.logger.info("Event set requires de-duping")
            self.logger.info(f"Event timestamp being used to de-dupe: {dedupe_timestamp}")
            # De-dupe events using boundary event hashes from previous run
            deduped_events = self._dedupe_events(
                all_events=new_events,
                latest_event_timestamp=dedupe_timestamp,
            )
            self.logger.info(f"After de-duping, total event count is {len(deduped_events)}")
            new_events = deduped_events

        query_completed = self.determine_next_run_params(
            pagination_token, state, param_request_start_date, param_request_end_date, run_state
        )
        self.prepare_state_timestamp(run_state, state, query_completed, latest_event)
        state[self.LAST_REQUEST_TIMESTAMP] = now
        state[self.PREVIOUS_RUN_STATE] = run_state.value
        self.logger.info(f"Updated state, state is now: {state}")
        has_more_pages = not query_completed
        return TaskOutput(output=new_events, state=state, has_more_pages=has_more_pages, status_code=200, error=None)

    def determine_next_run_params(
        self,
        pagination_token: str,
        state: Dict[str, Any],
        param_request_start_date: str,
        param_request_end_date: str,
        run_state: str,
    ) -> bool:
        """
        Determine the next run parameters based on the pagination token and state.
        :param pagination_token: The pagination token returned by the Zoom API
        :param state: The current state dictionary
        :param param_request_start_date: The start date for the request
        :param param_request_end_date: The end date for the request
        :param run_state: The current run state of the task
        """
        # Depending on if we get a pagination token, we need to either persist our current query OR reset it
        if pagination_token:
            self.logger.info(f"Pagination token returned by Zoom API ({pagination_token}) - storing pagination info")
            query_completed = False
            state[self.NEXT_PAGE_TOKEN] = pagination_token
            # Retain start and end date for next request, changes to these values while paginating will result in an
            # error from the Zoom API
            state[self.PARAM_START_DATE] = param_request_start_date
            state[self.PARAM_END_DATE] = param_request_end_date
        else:
            # We have completed the entire query for this date range as we have received no pagination token
            # Set the previous_completed_query_date in state to enable de-duping for next run on this date range
            self.logger.info("No pagination token returned by Zoom API - all pages have been consumed")
            query_completed = True
            state[self.PREVIOUS_COMPLETED_QUERY_DATE] = param_request_end_date
            if run_state == RunState.paginating:
                del state[self.NEXT_PAGE_TOKEN]
                del state[self.PARAM_START_DATE]
                del state[self.PARAM_END_DATE]
        return query_completed

    def prepare_state_timestamp(
        self, run_state: str, state: Dict[str, Any], query_completed: bool, latest_event: Event
    ):
        """
        Prepare the state timestamp based on the run state and latest event.
        :param run_state: The current run state of the task
        :param state: The current state dictionary
        :param query_completed: Boolean indicating if the query has completed
        :param latest_event: The latest event object containing the time
        :return: None
        """
        latest_event_timestamp = state.get(self.LATEST_EVENT_TIMESTAMP, self.ZERO_DATE)
        latest_event_timestamp_latch = state.get(self.LATEST_EVENT_TIMESTAMP_LATCH, latest_event.time)
        if run_state == RunState.paginating:
            # If we have no more pages, then we set the latest event time to the current latest event time only if
            # it is greater than the saved event time
            if query_completed:
                # Check if the current latest event time is greater than the latch event time
                latest_event_timestamp_latch = max(latest_event_timestamp_latch, latest_event.time)
                # Set the latest event timestamp in state to the new latest event time
                latest_event_timestamp = max(latest_event_timestamp, latest_event_timestamp_latch)
                state[self.LATEST_EVENT_TIMESTAMP] = latest_event_timestamp
            # If we have more pages, set the latest latch timestamp as the latest_event.time if it is newer
            else:
                if latest_event.time >= latest_event_timestamp_latch:
                    state[self.LATEST_EVENT_TIMESTAMP_LATCH] = latest_event.time

        else:
            if latest_event.time > latest_event_timestamp:
                state[self.LATEST_EVENT_TIMESTAMP] = latest_event.time

    def check_if_previously_queried(self, last_completed_end_time: str, current_query_end_time: str) -> bool:
        """
        Determine if a query has been run previously by comparing the dates associated to the last completed query's
        end time and the current query end time
        :param last_completed_end_time: Date time associated with the last fully completed query
        :param current_query_end_time: Current Date time associated with the query params we are about to use
        :return: bool
        """
        if last_completed_end_time is None:
            return False
        # The API uses year, month, and day as it's lowest level of granularity
        last_completed_end_time = datetime.strptime(last_completed_end_time, self.ZOOM_TIME_FORMAT)
        current_query_end_time = datetime.strptime(current_query_end_time, self.ZOOM_TIME_FORMAT)
        last_completed_end_date = last_completed_end_time.strftime("%Y-%m-%d")
        current_query_end_date = current_query_end_time.strftime("%Y-%m-%d")
        if current_query_end_date == last_completed_end_date:
            self.logger.info(f"Timerange to {current_query_end_date} previously queried...")
            return True
        return False

    def get_start_time(self, lookback: dict, cutoff_date: dict, cutoff_hours: str, run_state: RunState) -> str:
        """
        Determine the correct start time for the query to the Zoom API
        :param lookback: Lookback object from custom config containing date and time value
        :param cutoff_date: Cutoff date from custom config containing date and time value
        :param cutoff_hours: Cutoff hours from custom config containing time in hours to subtract from run time
        :param run_state: The current run state of the task to determine which start time to use
        :return: str value of the determined start time
        """
        if lookback is not None:
            self.logger.info("Setting min start time (lookback manually applied)")
            start_time = self._format_datetime_for_zoom(
                # a default of up to 12 months is used to allow for this to always run if there is missing value in the custom config
                # as if the request is larger than 30 days, the api will only return 30 days worth of data
                datetime(
                    lookback.get("year", date.today().year),
                    lookback.get("month", 1),
                    lookback.get("day", 1),
                    lookback.get("hour", 0),
                    lookback.get("minute", 0),
                    lookback.get("second", 0),
                )
            )
            self.logger.info(f"A custom start time of {start_time} will be used")
        else:
            if cutoff_date is not None:
                self.logger.info("Setting min start time (cutoff date manually applied)")
                start_time = self._format_datetime_for_zoom(
                    # a default of up to 12 months is used to allow for this to always run if there is missing value in the custom config
                    # as if the request is larger than 30 days, the api will only return 30 days worth of data
                    datetime(
                        cutoff_date.get("year", date.today().year),
                        cutoff_date.get("month", 1),
                        cutoff_date.get("day", 1),
                        cutoff_date.get("hour", 0),
                        cutoff_date.get("minute", 0),
                        cutoff_date.get("second", 0),
                    )
                )
            elif cutoff_hours is not None:
                self.logger.info(f"Setting min start time (cutoff: {cutoff_hours} hours manually applied)")
                start_time = self._format_datetime_for_zoom(dt=self._get_datetime_last_x_hours(cutoff_hours))
            else:
                if run_state == RunState.starting:
                    # no previous timestamp - this is considered first time through, use an initial lookback cutoff
                    self.logger.info(
                        "Setting min start time: No manual cutoff applied and no last request timestamp. "
                        f"Use default initial lookback cutoff: {self.DEFAULT_INITIAL_LOOKBACK} hours"
                    )
                    start_time = self._format_datetime_for_zoom(
                        dt=self._get_datetime_last_x_hours(self.DEFAULT_INITIAL_LOOKBACK)
                    )
                else:
                    # Not the first run, ensure a max cutoff is applied if necessary
                    self.logger.info(
                        "Setting min start time: No manual cutoff applied, last request timestamp exists. "
                        f"Use default lookback cutoff: {self.DEFAULT_CUTOFF_HOURS} hours"
                    )
                    start_time = self._format_datetime_for_zoom(
                        dt=self._get_datetime_last_x_hours(self.DEFAULT_CUTOFF_HOURS)
                    )
        return start_time

    def _get_last_valid_timestamp(self, start_time: str, last_request_timestamp: str = None) -> Optional[str]:
        """
        Get the last valid timestamp based on the provided start_time and state.

        This method checks if the last request timestamp in the 'state' dictionary is earlier
        than 'start_time' and returns 'start_time' if true, or returns the last request timestamp
        from the 'state' dictionary if it is later.

        Args:
            start_time (str): The last day to compare against.
            last_request_timestamp: The last request timestamp.
        Returns:
            int: The last valid timestamp.
        """
        if not last_request_timestamp:
            self.logger.info(f"No last request timestamp in state. Reverting to use time: {start_time}")
            return start_time
        if last_request_timestamp < start_time:
            self.logger.info(
                f"Saved state {last_request_timestamp} exceeds the cut off. Reverting to use time: {start_time}"
            )
            return start_time
        else:
            return last_request_timestamp

    def determine_runstate(self, state: Dict[str, Any]) -> RunState:
        # First run, clean state, need to calculate start and end times
        if not state.get(self.LAST_REQUEST_TIMESTAMP) and not state.get(self.NEXT_PAGE_TOKEN):
            rs: RunState = RunState.starting

        # 'n' run, no need to calculate start and end times due to continuation of pagination
        elif state.get(self.NEXT_PAGE_TOKEN):
            rs = RunState.paginating

        # 'n' run, no pagination occurring, needs to use latest request timestamp
        else:
            rs = RunState.continuing

        return rs

    def handle_no_new_events_found(self, now: str, query_end_date: str) -> TaskOutput:
        return TaskOutput(
            output=[],
            state={
                self.PREVIOUS_COMPLETED_QUERY_DATE: query_end_date,
                self.LAST_REQUEST_TIMESTAMP: now,
            },
            has_more_pages=False,
            status_code=200,
            error=None,
        )

    def handle_api_changed_exception(self, now: str) -> TaskOutput:
        return TaskOutput(
            output=[],
            state={
                self.LAST_REQUEST_TIMESTAMP: now,
            },
            has_more_pages=False,
            status_code=500,
            error=PluginException(
                cause=PluginException.causes[PluginException.Preset.SERVER_ERROR],
                assistance=self.API_CHANGED_ERROR_MESSAGE_ASSISTANCE,
            ),
        )

    def handle_pagination_token_error(self, exception: Exception, state: {} = None) -> TaskOutput:
        # In this instance, we clear the current pagination token and begin a continuing state
        # Do not set the latest event time as newer pages may have events with a later event time
        self.logger.error("Invalid or expired pagination token received, exiting pagination.")
        self.logger.error(f"Error received {exception.data}")

        del state[self.NEXT_PAGE_TOKEN]
        state[self.PREVIOUS_RUN_STATE] = RunState.paginating.value

        return TaskOutput(
            output=[],
            state=state,
            has_more_pages=True,
            status_code=200,
            error=None,
        )

    def handle_request_exception(self, exception: Exception, now: str) -> TaskOutput:
        if isinstance(exception, (AuthenticationRetryLimitError, AuthenticationError)):
            self.logger.error(
                f"{self.AUTHENTICATION_RETRY_LIMIT_ERROR_MESSAGE_CAUSE} "
                f"{self.AUTHENTICATION_RETRY_LIMIT_ERROR_MESSAGE_ASSISTANCE}"
                if isinstance(exception, AuthenticationRetryLimitError)
                else self.AUTHENTICATION_ERROR_MESSAGE
            )
            return TaskOutput(
                output=[],
                state={
                    self.LAST_REQUEST_TIMESTAMP: now,
                },
                has_more_pages=False,
                status_code=401,
                error=PluginException(
                    cause=PluginException.causes[PluginException.Preset.API_KEY],
                    assistance=self.AUTHENTICATION_RETRY_LIMIT_ERROR_MESSAGE_ASSISTANCE,
                ),
            )

        elif isinstance(exception, PluginException):
            # Add additional information to aid customer if correct permissions are not set in the Zoom App
            if hasattr(exception, "data") and "Invalid access token, does not contain scope" in exception.data:
                self.logger.error(self.PERMISSIONS_ERROR_MESSAGE)
                return TaskOutput(
                    output=[],
                    state={
                        self.LAST_REQUEST_TIMESTAMP: now,
                    },
                    has_more_pages=False,
                    status_code=403,
                    error=PluginException(
                        cause=PluginException.causes[PluginException.Preset.UNAUTHORIZED],
                        assistance=self.PERMISSIONS_ERROR_MESSAGE,
                        data=exception.data,
                    ),
                )
            elif hasattr(exception, "data") and (
                "No permission." in exception.data or "Only available for" in exception.data
            ):
                self.logger.error(self.PERMISSIONS_ERROR_MESSAGE_USER)
                return TaskOutput(
                    output=[],
                    state={
                        self.LAST_REQUEST_TIMESTAMP: now,
                    },
                    has_more_pages=False,
                    status_code=403,
                    error=PluginException(
                        cause=PluginException.causes[PluginException.Preset.UNAUTHORIZED],
                        assistance=self.PERMISSIONS_ERROR_MESSAGE_USER,
                        data=exception.data,
                    ),
                )
            else:
                return TaskOutput(
                    output=[],
                    state={
                        self.LAST_REQUEST_TIMESTAMP: now,
                    },
                    has_more_pages=False,
                    status_code=500,
                    error=exception,
                )
        else:
            plugin_exception = PluginException(preset=PluginException.Preset.UNKNOWN, data=exception)
            return TaskOutput(
                output=[],
                state={
                    self.LAST_REQUEST_TIMESTAMP: now,
                },
                has_more_pages=False,
                status_code=500,
                error=plugin_exception,
            )

    @staticmethod
    def _dedupe_events(all_events: [Event], latest_event_timestamp: Optional[str] = None) -> [Event]:
        if latest_event_timestamp is None:
            return all_events
        return list(filter(lambda event: event.time > latest_event_timestamp, all_events))

    @staticmethod
    def _get_datetime_now() -> datetime:
        return datetime.now(timezone.utc)

    def _get_datetime_last_x_hours(self, hours: int) -> datetime:
        return self._get_datetime_now() - timedelta(hours=hours)

    def _format_datetime_for_zoom(self, dt: datetime) -> str:
        return dt.strftime(self.ZOOM_TIME_FORMAT)
