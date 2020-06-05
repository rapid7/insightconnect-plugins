import insightconnect_plugin_runtime
import time
from .schema import UserActivityEventInput, UserActivityEventOutput, Input, Output, Component
# Custom imports below
from datetime import datetime


class UserActivityEvent(insightconnect_plugin_runtime.Trigger):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='user_activity_event',
                description=Component.DESCRIPTION,
                input=UserActivityEventInput(),
                output=UserActivityEventOutput())

    def run(self, params={}):
        activity_type = params.get(Input.ACTIVITY_TYPE, "All")
        page_size = 1000
        sleep_interval_min = 5

        # Get current time in UTC as starting point of trigger events
        now = datetime.utcnow()
        last_event_time = now.strftime("%Y-%m-%dT%H:%M:%SZ")
        self.logger.info(f"Initializing trigger, only events after {last_event_time} will be processed")

        # Keep processing until trigger is shut down
        while True:
            # Zoom doesn't document max page_size; setting to 1000 with ability to increase in future
            events = self.connection.zoom_api.get_user_activity_events(last_event_time, page_size=page_size)

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
                    self.send({Output.USER_ACTIVITY: event})

            # Reports API doesn't let you scope by datetime - only date - so don't request too often since
            # all current date events will be returned each time
            time.sleep(sleep_interval_min * 60)
