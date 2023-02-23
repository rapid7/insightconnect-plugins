import insightconnect_plugin_runtime
from .schema import MonitorSignInOutActivityInput, MonitorSignInOutActivityOutput, MonitorSignInOutActivityState, Input, Output, Component, State
# Custom imports below
from datetime import datetime, timedelta
from icon_zoom.util.event import Event

"""
Task logic:
- First run? Start time will be "now - 24 hours". End time will be current time at start of run.
  Store most recent event time in state.
    
- Subsequent run? Start time is the most recent events publish time and the End time will be "now"
  Duplicates can occur on time boundaries, eg from=0 to=10, next run is from=10 and to=20 due to lack of ms precision
  Solve by hashing events and removing previously seen hashes from list
"""


class MonitorSignInOutActivity(insightconnect_plugin_runtime.Task):

    LAST_EVENT_TIME = "last_event_time"
    BOUNDARY_EVENTS = "boundary_events"

    ZOOM_TIME_FORMAT = "%Y-%m-%dT%H:%M:%SZ"

    def __init__(self):
        super(self.__class__, self).__init__(
                name='monitor_sign_in_out_activity',
                description=Component.DESCRIPTION,
                input=MonitorSignInOutActivityInput(),
                output=MonitorSignInOutActivityOutput(),
                state=MonitorSignInOutActivityState())

    def run(self, params={}, state={}):

        # Check if first run
        if not state.get(self.LAST_EVENT_TIME):
            self.logger.info("First run")
            output, new_state = self.first_run(state=state)
        else:
            # Subsequent run
            self.logger.info("Subsequent run")
            output, new_state = self.subsequent_run(state=state)

        # Turn events list back into a list of dicts
        output = [e.__dict__ for e in output]
        return output, new_state

    def subsequent_run(self, state: dict) -> ([dict], dict):
        # Get time boundaries for new event set retrieval
        now = self._get_datetime_now()
        now_for_zoom = self._format_datetime_for_zoom(dt=now)

        # Get fully consumed paginated event set, using previous run latest event time
        new_events: [dict] = self.connection.zoom_api.get_user_activity_events(
            start_date=state.get(self.LAST_EVENT_TIME),
            end_date=now_for_zoom,
            page_size=1000
        )
        new_events = [Event(**e) for e in new_events]

        # Get latest event time, to be used for determining boundary event hashes
        try:
            new_latest_event_time = new_events[0].time
            self.logger.info(f"Latest event time is: {new_latest_event_time}")
        except IndexError:
            self.logger.info("Unable to get latest event time, no new events found!")
            return [], {
                self.BOUNDARY_EVENTS: [],
                self.LAST_EVENT_TIME: self._format_datetime_for_zoom(self._get_datetime_now())
            }

        # De-dupe events using boundary event hashes from previous run
        deduped_events = self._dedupe_events(boundary_event_hashes=state[self.BOUNDARY_EVENTS], new_events=new_events)

        # Determine new boundary event hashes using latest time from newly retrieved event set and latest event time
        # from the new set.
        boundary_event_hashes = self._get_boundary_event_hashes(latest_event_time=new_latest_event_time,
                                                                events=deduped_events)

        # update state
        state[self.BOUNDARY_EVENTS] = boundary_event_hashes
        state[self.LAST_EVENT_TIME] = new_latest_event_time

        return deduped_events, state

    def first_run(self, state: dict) -> ([dict], dict):
        # Get time boundaries for first event set
        now = self._get_datetime_now()
        last_24_hours = self._get_datetime_last_24_hours()
        now_for_zoom = self._format_datetime_for_zoom(dt=now)
        last_24_hours_for_zoom = self._format_datetime_for_zoom(dt=last_24_hours)
        self.logger.info("Got times!")

        # Get first set of events, fully consumed pagination
        new_events: [dict] = self.connection.zoom_api.get_user_activity_events(
            start_date=last_24_hours_for_zoom,
            end_date=now_for_zoom,
            page_size=1000
        )
        new_events = [Event(**e) for e in new_events]
        self.logger.info(f"Got {len(new_events)} events!")

        # Get latest event time as well as boundary hashes. These are to be used for de-duping future event sets
        try:
            new_latest_event_time = new_events[0].time
            self.logger.info(f"Latest event time is: {new_latest_event_time}")
            boundary_event_hashes: [str] = self._get_boundary_event_hashes(latest_event_time=new_latest_event_time,
                                                                           events=new_events)
        except IndexError:
            self.logger.info("Unable to get latest event time, no new events found!")
            return [], {
                self.BOUNDARY_EVENTS: [],
                self.LAST_EVENT_TIME: self._format_datetime_for_zoom(self._get_datetime_now())
            }

        # update state
        state[self.BOUNDARY_EVENTS] = boundary_event_hashes
        state[self.LAST_EVENT_TIME] = new_latest_event_time
        self.logger.info(f"Updated state, state is now: {state}")

        return new_events, state

    @staticmethod
    def _dedupe_events(boundary_event_hashes: [str], new_events: [Event]) -> [Event]:
        new_events: [Event] = [e for e in new_events if e.sha1() not in boundary_event_hashes]

        return new_events

    @staticmethod
    def _get_boundary_event_hashes(latest_event_time: str, events: [Event]) -> [str]:
        # Hashes for events that can land on a time boundary
        hashes = [e.sha1() for e in events if e.time == latest_event_time]

        return hashes

    def _get_datetime_from_zoom_timestamp(self, ts: str) -> datetime:
        dt = datetime.strptime(ts, self.ZOOM_TIME_FORMAT)

        return dt

    @staticmethod
    def _get_datetime_now() -> datetime:
        now = datetime.now()

        return now

    @staticmethod
    def _get_datetime_last_24_hours() -> datetime:
        now = datetime.now()
        last_24 = now - timedelta(hours=24)

        return last_24

    def _format_datetime_for_zoom(self, dt: datetime) -> str:
        formatted = dt.strftime(self.ZOOM_TIME_FORMAT)
        return formatted
