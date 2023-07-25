import insightconnect_plugin_runtime
from insightconnect_plugin_runtime.exceptions import PluginException

from .schema import (
    MonitorSignInOutActivityInput,
    MonitorSignInOutActivityOutput,
    MonitorSignInOutActivityState,
    Component,
)

# Custom imports below
from datetime import datetime, timedelta, timezone
from typing import Optional

from icon_zoom.util.api import AuthenticationRetryLimitError, AuthenticationError
from icon_zoom.util.event import Event


class TaskOutput:
    def __init__(
        self, output: [Event], state: dict, has_more_pages: bool, status_code: int, error: Optional[PluginException]
    ):
        self.output = output
        self.state = state
        self.has_more_pages = has_more_pages
        self.status_code = status_code
        self.error = error


class MonitorSignInOutActivity(insightconnect_plugin_runtime.Task):
    LAST_REQUEST_TIMESTAMP = "last_request_timestamp"
    BOUNDARY_EVENTS = "boundary_events"
    LATEST_EVENT_TIMESTAMP = "latest_event_timestamp"
    STATUS_CODE = "status_code"
    NEXT_PAGE_TOKEN = "next_page_token"

    ZOOM_TIME_FORMAT = "%Y-%m-%dT%H:%M:%SZ"

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

    def __init__(self):
        super(self.__class__, self).__init__(
            name="monitor_sign_in_out_activity",
            description=Component.DESCRIPTION,
            input=MonitorSignInOutActivityInput(),
            output=MonitorSignInOutActivityOutput(),
            state=MonitorSignInOutActivityState(),
        )

    # pylint: disable=unused-argument
    def run(self, params={}, state={}):
        try:
            # Check if first run
            # First run is either NO timestamp for last request, OR no timestamp for last request BUT a next page token
            # exists, which means it is continuation of a first run
            if not state.get(self.LAST_REQUEST_TIMESTAMP) or (
                not state.get(self.LAST_REQUEST_TIMESTAMP) and state.get(self.NEXT_PAGE_TOKEN)
            ):
                self.logger.info("First run")
                task_output: TaskOutput = self.first_run(state=state)
            else:
                # Subsequent run
                self.logger.info("Subsequent run")
                task_output: TaskOutput = self.subsequent_run(state=state)

            # Turn events list back into a list of dicts
            output = [event.__dict__ for event in task_output.output]
            return output, task_output.state, task_output.has_more_pages, task_output.status_code, task_output.error

        except Exception as error:
            self.logger.error(f"Unhandled exception occurred during {self.name} task: {error}")
            return [], {}, False, 500, PluginException(preset=PluginException.Preset.UNKNOWN, data=error)

    def first_run(self, state: dict) -> TaskOutput:
        # Get time boundaries for first event set
        now = self._get_datetime_now()
        last_24_hours = self._get_datetime_last_24_hours()

        # Default has_more_pages for external pagination to False
        has_more_pages = False

        # now_for_zoom is the start time for the Zoom API but also used to track requests across task runs via state
        now_for_zoom = self._format_datetime_for_zoom(dt=now)
        last_24_hours_for_zoom = self._format_datetime_for_zoom(dt=last_24_hours)

        # Get fully consumed paginated event set, using previous run latest event time
        try:
            self.logger.info(f"Getting events from {last_24_hours_for_zoom} until {now_for_zoom}")

            # Call API, returning any new events and pagination token if present
            new_events, pagination_token = self.connection.zoom_api.get_user_activity_events_task(
                start_date=last_24_hours_for_zoom,
                end_date=now_for_zoom,
                page_size=1000,
                next_page_token=state.get(self.NEXT_PAGE_TOKEN),
            )
            if pagination_token:
                has_more_pages = True

        except (AuthenticationRetryLimitError, AuthenticationError) as error:
            self.logger.error(
                f"{self.AUTHENTICATION_RETRY_LIMIT_ERROR_MESSAGE_CAUSE} "
                f"{self.AUTHENTICATION_RETRY_LIMIT_ERROR_MESSAGE_ASSISTANCE}"
                if isinstance(error, AuthenticationRetryLimitError)
                else self.AUTHENTICATION_ERROR_MESSAGE
            )
            return TaskOutput(
                output=[],
                state={
                    self.BOUNDARY_EVENTS: [],
                    self.LAST_REQUEST_TIMESTAMP: now_for_zoom,
                    self.LATEST_EVENT_TIMESTAMP: None,
                    self.NEXT_PAGE_TOKEN: None,
                },
                has_more_pages=False,
                status_code=401,
                error=PluginException(
                    cause=self.AUTHENTICATION_RETRY_LIMIT_ERROR_MESSAGE_CAUSE,
                    assistance=self.AUTHENTICATION_RETRY_LIMIT_ERROR_MESSAGE_ASSISTANCE,
                ),
            )
        except PluginException as error:
            # Add additional information to aid customer if correct permissions are not set in the Zoom App
            if "Invalid access token, does not contain scope" in error.data:
                self.logger.error(self.PERMISSIONS_ERROR_MESSAGE)
                return TaskOutput(
                    output=[],
                    state={
                        self.BOUNDARY_EVENTS: [],
                        self.LAST_REQUEST_TIMESTAMP: now_for_zoom,
                        self.LATEST_EVENT_TIMESTAMP: None,
                        self.NEXT_PAGE_TOKEN: None,
                    },
                    has_more_pages=False,
                    status_code=403,
                    error=PluginException(
                        cause="Insufficient permissions.", assistance=self.PERMISSIONS_ERROR_MESSAGE, data=error.data
                    ),
                )
            else:
                raise  # TODO: Do we need to do something else here?

        try:
            new_events = sorted([Event(**event) for event in new_events], reverse=True)
        except TypeError as error:
            self.logger.error(f"Zoom API endpoint output has changed, unable to parse events: {error}")
            return TaskOutput(
                output=[],
                state={
                    self.BOUNDARY_EVENTS: [],
                    self.LAST_REQUEST_TIMESTAMP: now_for_zoom,
                    self.LATEST_EVENT_TIMESTAMP: None,
                    self.NEXT_PAGE_TOKEN: None,
                },
                has_more_pages=False,
                status_code=500,
                error=PluginException(
                    cause=self.API_CHANGED_ERROR_MESSAGE_CAUSE, assistance=self.API_CHANGED_ERROR_MESSAGE_ASSISTANCE
                ),
            )

        self.logger.info(f"Got {len(new_events)} events from Zoom!")

        # Get latest event time (last in response from Zoom) as well as boundary hashes.
        # These are to be used for de-duping future event sets
        try:
            new_latest_event_time = new_events[0].time
            self.logger.info(f"Latest event time is: {new_latest_event_time}")
            boundary_event_hashes: [str] = self._get_boundary_event_hashes(
                latest_event_time=new_latest_event_time, events=new_events
            )
        except IndexError:
            self.logger.info("Unable to get latest event time, no new events found!")
            return TaskOutput(
                output=[],
                state={
                    self.BOUNDARY_EVENTS: [],
                    self.LAST_REQUEST_TIMESTAMP: now_for_zoom,
                    self.LATEST_EVENT_TIMESTAMP: None,
                    self.NEXT_PAGE_TOKEN: None,
                },
                has_more_pages=False,
                status_code=200,
                error=None,
            )

        # update state
        state[self.BOUNDARY_EVENTS] = boundary_event_hashes
        state[self.LAST_REQUEST_TIMESTAMP] = now_for_zoom
        state[self.LATEST_EVENT_TIMESTAMP] = new_latest_event_time
        state[self.NEXT_PAGE_TOKEN] = pagination_token

        self.logger.info(f"Updated state, state is now: {state}")
        return TaskOutput(output=new_events, state=state, has_more_pages=has_more_pages, status_code=200, error=None)

    def subsequent_run(self, state: dict) -> TaskOutput:
        # now_for_zoom is the start time for the Zoom API but also used to track requests across task runs via state
        now = self._get_datetime_now()
        now_for_zoom = self._format_datetime_for_zoom(dt=now)
        last_request_timestamp = state.get(self.LAST_REQUEST_TIMESTAMP)

        # Default has_more_pages for external pagination to False
        has_more_pages = False

        # Get first set of events, fully consumed pagination
        try:
            # Get fully consumed paginated event set, using previous run latest event time
            self.logger.info(f"Getting events from {last_request_timestamp} until {now_for_zoom}")
            new_events, has_more_pages = self.connection.zoom_api.get_user_activity_events_task(
                start_date=last_request_timestamp,
                end_date=now_for_zoom,
                page_size=1000,
                next_page_token=state.get(self.NEXT_PAGE_TOKEN),
            )
        except (AuthenticationRetryLimitError, AuthenticationError) as error:
            self.logger.error(
                f"{self.AUTHENTICATION_RETRY_LIMIT_ERROR_MESSAGE_CAUSE} "
                f"{self.AUTHENTICATION_RETRY_LIMIT_ERROR_MESSAGE_ASSISTANCE}"
                if isinstance(error, AuthenticationRetryLimitError)
                else self.AUTHENTICATION_ERROR_MESSAGE
            )
            return TaskOutput(
                output=[],
                state={
                    self.BOUNDARY_EVENTS: [],
                    self.LAST_REQUEST_TIMESTAMP: now_for_zoom,
                    self.LATEST_EVENT_TIMESTAMP: None,
                    self.NEXT_PAGE_TOKEN: False,
                },
                has_more_pages=False,
                status_code=401,
                error=PluginException(
                    cause=self.AUTHENTICATION_RETRY_LIMIT_ERROR_MESSAGE_CAUSE,
                    assistance=self.AUTHENTICATION_RETRY_LIMIT_ERROR_MESSAGE_ASSISTANCE,
                ),
            )
        except PluginException as error:
            # Add additional information to aid customer if correct permissions are not set in the Zoom App
            if "Invalid access token, does not contain scope" in error.data:
                self.logger.error(self.PERMISSIONS_ERROR_MESSAGE)
                return TaskOutput(
                    output=[],
                    state={
                        self.BOUNDARY_EVENTS: [],
                        self.LAST_REQUEST_TIMESTAMP: now_for_zoom,
                        self.LATEST_EVENT_TIMESTAMP: None,
                        self.NEXT_PAGE_TOKEN: False,
                    },
                    has_more_pages=False,
                    status_code=403,
                    error=PluginException(
                        cause="Insufficient permissions.", assistance=self.PERMISSIONS_ERROR_MESSAGE, data=error.data
                    ),
                )
            else:
                raise
        try:
            new_events = sorted([Event(**event) for event in new_events], reverse=True)
        except TypeError as error:
            self.logger.error(f"Zoom API endpoint output has changed, unable to parse events: {error}")
            return TaskOutput(
                output=[],
                state={
                    self.BOUNDARY_EVENTS: [],
                    self.LAST_REQUEST_TIMESTAMP: now_for_zoom,
                    self.LATEST_EVENT_TIMESTAMP: None,
                    self.NEXT_PAGE_TOKEN: False,
                },
                has_more_pages=False,
                status_code=500,
                error=PluginException(
                    cause=self.API_CHANGED_ERROR_MESSAGE_CAUSE, assistance=self.API_CHANGED_ERROR_MESSAGE_ASSISTANCE
                ),
            )

        self.logger.info(f"Got {len(new_events)} events from Zoom!")

        # Get latest event time (last in response from Zoom), to be used for determining boundary event hashes
        try:
            new_latest_event = new_events[0]
            self.logger.info(f"Latest event time is: {new_latest_event.time}")
        except IndexError:
            self.logger.info("Unable to get latest event time, no new events found!")
            return TaskOutput(
                output=[],
                state={
                    self.BOUNDARY_EVENTS: [],
                    self.LAST_REQUEST_TIMESTAMP: now_for_zoom,
                    self.LATEST_EVENT_TIMESTAMP: None,
                    self.NEXT_PAGE_TOKEN: False,
                },
                has_more_pages=False,
                status_code=200,
                error=None,
            )

        # De-dupe events using boundary event hashes from previous run
        deduped_events = self._dedupe_events(
            boundary_event_hashes=state[self.BOUNDARY_EVENTS],
            all_events=new_events,
            latest_event_timestamp=state.get(self.LATEST_EVENT_TIMESTAMP),
        )
        self.logger.info(f"{len(deduped_events)} unique events were found!")

        # Determine new boundary event hashes using latest time from newly retrieved event set and latest event time
        # from the new set.

        boundary_event_hashes = state.get(self.BOUNDARY_EVENTS)
        if len(deduped_events) > 0:
            boundary_event_hashes = self._get_boundary_event_hashes(
                latest_event_time=new_latest_event.time, events=deduped_events
            )

        # update state
        state[self.BOUNDARY_EVENTS] = boundary_event_hashes
        state[self.LAST_REQUEST_TIMESTAMP] = now_for_zoom
        state[self.LATEST_EVENT_TIMESTAMP] = new_latest_event.time
        state[self.NEXT_PAGE_TOKEN] = not has_more_pages

        self.logger.info(f"Updated state, state is now: {state}")
        return TaskOutput(
            output=deduped_events, state=state, has_more_pages=has_more_pages, status_code=200, error=None
        )

    @staticmethod
    def _dedupe_events(
        boundary_event_hashes: [str], all_events: [Event], latest_event_timestamp: Optional[str]
    ) -> [Event]:
        if latest_event_timestamp is None:
            return all_events

        deduped_events: [Event] = []

        for event in all_events:
            if event.time > latest_event_timestamp or (
                event.time == latest_event_timestamp and event.sha1() not in boundary_event_hashes
            ):
                deduped_events.append(event)

        return deduped_events  # make sure sort order is correct here

    @staticmethod
    def _get_boundary_event_hashes(latest_event_time: str, events: [Event]) -> [str]:
        """
        Creates a list of SHA1 hashes containing hashes of all events with a timestamp matching latest_event_time
        """
        # Hashes for events that can land on a time boundary
        hashes = [event.sha1() for event in events if event.time == latest_event_time]

        return hashes

    @staticmethod
    def _get_datetime_now() -> datetime:
        now = datetime.now(timezone.utc)

        return now

    @staticmethod
    def _get_datetime_last_24_hours() -> datetime:
        now = datetime.now(timezone.utc)
        last_24 = now - timedelta(hours=24)

        return last_24

    def _format_datetime_for_zoom(self, dt: datetime) -> str:
        formatted = dt.strftime(self.ZOOM_TIME_FORMAT)
        return formatted
