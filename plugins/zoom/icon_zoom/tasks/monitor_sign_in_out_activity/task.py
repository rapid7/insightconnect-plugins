import insightconnect_plugin_runtime
from .schema import (
    MonitorSignInOutActivityInput,
    MonitorSignInOutActivityOutput,
    MonitorSignInOutActivityState,
    Component,
)

# Custom imports below
from datetime import datetime, timedelta, timezone
from icon_zoom.util.event import Event


class MonitorSignInOutActivity(insightconnect_plugin_runtime.Task):

    LAST_REQUEST_TIMESTAMP = "last_request_timestamp"
    BOUNDARY_EVENTS = "boundary_events"
    LATEST_EVENT_TIMESTAMP = "latest_event_timestamp"

    ZOOM_TIME_FORMAT = "%Y-%m-%dT%H:%M:%SZ"

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

        # Check if first run
        if not state.get(self.LAST_REQUEST_TIMESTAMP):
            self.logger.info("First run")
            output, new_state = self.first_run(state=state)
        else:
            # Subsequent run
            self.logger.info("Subsequent run")
            output, new_state = self.subsequent_run(state=state)

        # Turn events list back into a list of dicts
        output = [event.__dict__ for event in output]
        return output, new_state

    def first_run(self, state: dict) -> ([dict], dict):
        # Get time boundaries for first event set
        now = self._get_datetime_now()
        last_24_hours = self._get_datetime_last_24_hours()

        # now_for_zoom is the start time for the Zoom API but also used to track requests across task runs via state
        now_for_zoom = self._format_datetime_for_zoom(dt=now)
        last_24_hours_for_zoom = self._format_datetime_for_zoom(dt=last_24_hours)

        # Get first set of events, fully consumed pagination
        self.logger.info(f"First run, getting events from {last_24_hours_for_zoom} until {now_for_zoom}")
        new_events: [dict] = self.connection.zoom_api.get_user_activity_events(
            start_date=last_24_hours_for_zoom, end_date=now_for_zoom, page_size=1000
        )

        try:
            new_events = sorted([Event(**event) for event in new_events], reverse=True)
        except TypeError as error:
            self.logger.error(f"Zoom API endpoint output has changed, unable to parse events: {error}")
            return [], {
                self.BOUNDARY_EVENTS: [],
                self.LAST_REQUEST_TIMESTAMP: now_for_zoom,
            }

        self.logger.info(f"Got {len(new_events)} events!")

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
            return [], {
                self.BOUNDARY_EVENTS: [],
                self.LAST_REQUEST_TIMESTAMP: now_for_zoom,
            }

        # update state
        state[self.BOUNDARY_EVENTS] = boundary_event_hashes
        state[self.LAST_REQUEST_TIMESTAMP] = now_for_zoom
        state[self.LATEST_EVENT_TIMESTAMP] = new_latest_event_time
        self.logger.info(f"Updated state, state is now: {state}")

        return new_events, state

    def subsequent_run(self, state: dict) -> ([dict], dict):
        # now_for_zoom is the start time for the Zoom API but also used to track requests across task runs via state
        now = self._get_datetime_now()
        now_for_zoom = self._format_datetime_for_zoom(dt=now)
        last_request_timestamp = state.get(self.LAST_REQUEST_TIMESTAMP)

        # Get fully consumed paginated event set, using previous run latest event time
        self.logger.info(f"Getting events from {last_request_timestamp} until {now_for_zoom}")
        new_events: [dict] = self.connection.zoom_api.get_user_activity_events(
            start_date=last_request_timestamp, end_date=now_for_zoom, page_size=1000
        )
        try:
            new_events = sorted([Event(**event) for event in new_events], reverse=True)
        except TypeError as error:
            self.logger.error(f"Zoom API endpoint output has changed, unable to parse events: {error}")
            return [], {
                self.BOUNDARY_EVENTS: [],
                self.LAST_REQUEST_TIMESTAMP: now_for_zoom,
            }

        self.logger.info(f"Got {len(new_events)} events!")

        # Get latest event time (last in response from Zoom), to be used for determining boundary event hashes
        try:
            new_latest_event = new_events[0]
            self.logger.info(f"Latest event time is: {new_latest_event.time}")
        except IndexError:
            self.logger.info("Unable to get latest event time, no new events found!")
            return [], {
                self.BOUNDARY_EVENTS: [],
                self.LAST_REQUEST_TIMESTAMP: now_for_zoom,
            }

        # De-dupe events using boundary event hashes from previous run
        deduped_events = self._dedupe_events(boundary_event_hashes=state[self.BOUNDARY_EVENTS],
                                             all_events=new_events,
                                             latest_event_timestamp=state[self.LATEST_EVENT_TIMESTAMP])

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

        return deduped_events, state

    @staticmethod
    def _dedupe_events(boundary_event_hashes: [str], all_events: [Event], latest_event_timestamp: str) -> [Event]:
        deduped_events: [Event] = []

        for event in all_events:
            if \
                    event.time > latest_event_timestamp or \
                    (event.time == latest_event_timestamp and event.sha1() not in boundary_event_hashes):
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
