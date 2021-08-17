import insightconnect_plugin_runtime
from .schema import (
    MonitorAlertEventsInput,
    MonitorAlertEventsOutput,
    MonitorAlertEventsState,
    Output,
    Component,
    State,
)
# Custom imports below

from ...util.util import Util

INITIAL_HISTORICAL_LOOK_BACK_MS = 1 * 60 * 60 * 1000
INCIDENT_TIME_FIELD = "creation_time"


class MonitorAlertEvents(insightconnect_plugin_runtime.Task):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="monitor_alert_events",
            description=Component.DESCRIPTION,
            input=MonitorAlertEventsInput(),
            output=MonitorAlertEventsOutput(),
            state=MonitorAlertEventsState(),
        )

    def run(self, params={}, state={}):
        now = Util.now_ms()
        last_event_time = state.get(State.LAST_EVENT_TIME, None)
        if last_event_time is None:
            last_event_time = now - INITIAL_HISTORICAL_LOOK_BACK_MS
        last_event_time = int(last_event_time)
        self.logger.info(f"Retrieving Cortex XDR alert events since {last_event_time}.")
        alert_events = self.connection.xdr_api.get_incidents(from_time=last_event_time, to_time=now)
        new_events = [x for x in alert_events if x.get(INCIDENT_TIME_FIELD, -1) > last_event_time]
        new_events.sort(key=lambda x: x.get(INCIDENT_TIME_FIELD, -1))
        self.logger.info(f"Finished retrieving {len(new_events)} new alert events this iteration.")
        return {Output.EVENTS: new_events}, {State.LAST_EVENT_TIME: str(now)}
