import insightconnect_plugin_runtime
from .schema import RetrieveUserActivityEventsInput, RetrieveUserActivityEventsOutput, RetrieveUserActivityEventsState, Input, Output, Component
# Custom imports below
from datetime import datetime, timedelta


class RetrieveUserActivityEvents(insightconnect_plugin_runtime.Task):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='retrieve_user_activity_events',
                description=Component.DESCRIPTION,
                input=RetrieveUserActivityEventsInput(),
                output=RetrieveUserActivityEventsOutput(),
                state=RetrieveUserActivityEventsState())

    def run(self, params={}):
        activity_type = params.get(Input.ACTIVITY_TYPE, "All")
        page_size = 1000
        last_event_time = params.get("last_event_time", None)

        if last_event_time is None:
            # Pull events for past week to start
            now = datetime.utcnow()
            week_ago = now - timedelta(days=7)
            last_event_time = week_ago.strftime("%Y-%m-%dT%H:%M:%SZ")

        self.logger.info(f"Retrieving user activity events; only events after {last_event_time} will be retrieved")

        # Zoom doesn't document max page_size; setting to 1000 with ability to increase in future
        events = self.connection.zoom_api.get_user_activity_events(last_event_time, page_size=page_size)

        new_events = []
        # Process events from oldest to newest; returned newest to oldest
        for event in reversed(events):
            # Zoom API only lets you limit results based on date and not datetime;
            # must compare to make sure we only process new events based on last_event_time
            if event.get("time") > last_event_time:
                last_event_time = event.get("time")
            else:
                # Event is older than last event time, don't process
                continue

            if activity_type == "All" or activity_type == event.get("type"):
                new_events.append(event)

        return {Output.USER_ACTIVITY_EVENTS: new_events}, {"last_event_time": last_event_time}
