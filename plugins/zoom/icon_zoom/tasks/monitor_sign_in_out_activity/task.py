import insightconnect_plugin_runtime
from .schema import MonitorSignInOutActivityInput, MonitorSignInOutActivityOutput, MonitorSignInOutActivityState, Input, Output, Component, State
# Custom imports below
from datetime import datetime, timedelta

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
    PREVIOUS_EVENTS = "previous_events"

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

        return output, new_state

    def subsequent_run(self, state: dict) -> ([dict], dict):
        now = self._get_datetime_now()
        now_for_zoom = self._format_datetime_for_zoom(dt=now)

        new_events: [dict] = self.connection.zoom_api.get_user_activity_events(
            start_date=state.get(self.LAST_EVENT_TIME),
            end_date=now_for_zoom
        )

        try:
            new_latest_event_time = new_events[0]["time"]
            self.logger.info(f"Latest event time is: {new_latest_event_time}")
        except IndexError:
            self.logger.info("Unable to get latest event time, no new events found!")
            return [], {
                self.PREVIOUS_EVENTS: [],
                self.LAST_EVENT_TIME: self._format_datetime_for_zoom(self._get_datetime_now())
            }

        # Convert lists of event dicts to sets of Event to de-dupe
        new_events: {Event} = {Event(**e) for e in new_events}
        previous_events = state.get(self.PREVIOUS_EVENTS, [])
        previous_events: {Event} = {Event(**e) for e in previous_events}

        # remove duplicates
        unique_events: {Event} = new_events - previous_events
        unique_events = [e.__dict__ for e in unique_events]

        # update state
        state[self.PREVIOUS_EVENTS] = unique_events
        state[self.LAST_EVENT_TIME] = new_latest_event_time

        return unique_events, state

    def first_run(self, state: dict) -> ([dict], dict):
        now = self._get_datetime_now()
        last_24_hours = self._get_datetime_last_24_hours()
        now_for_zoom = self._format_datetime_for_zoom(dt=now)
        last_24_hours_for_zoom = self._format_datetime_for_zoom(dt=last_24_hours)
        self.logger.info("Got times!")

        new_events: [dict] = self.connection.zoom_api.get_user_activity_events(
            start_date=last_24_hours_for_zoom,
            end_date=now_for_zoom
        )
        self.logger.info(f"Got events: {new_events}")

        try:
            new_latest_event_time = new_events[0]["time"]
            self.logger.info(f"Latest event time is: {new_latest_event_time}")
        except IndexError:
            self.logger.info("Unable to get latest event time, no new events found!")
            return [], {
                self.PREVIOUS_EVENTS: [],
                self.LAST_EVENT_TIME: self._format_datetime_for_zoom(self._get_datetime_now())
            }

        # update state
        state[self.PREVIOUS_EVENTS] = new_events
        state[self.LAST_EVENT_TIME] = new_latest_event_time
        self.logger.info(f"Updated state, state is now: {state}")

        return new_events, state

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


class Event:

    def __init__(self, client_type: str, email: str, ip_address: str, time: str, type_: str, version: str):
        self.client_type = client_type
        self.email = email
        self.ip_address = ip_address
        self.time = time
        self.type_ = type_
        self.version = version

    def __eq__(self, other):
        return self.client_type == other.client_type \
               and self.email == other.email \
               and self.ip_address == other.ip_address \
               and self.time == other.time \
               and self.type_ == other.type_ \
               and self.version == other.version
