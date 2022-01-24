import insightconnect_plugin_runtime
import time
from .schema import GetEventsInput, GetEventsOutput, Input, Output, Component

# Custom imports below
import copy


class GetEvents(insightconnect_plugin_runtime.Trigger):
    def __init__(self):
        super(self.__class__, self).__init__(
            name="get_events", description=Component.DESCRIPTION, input=GetEventsInput(), output=GetEventsOutput()
        )

    def run(self, params={}):
        """Run the trigger"""
        # Pull first page of events at start of trigger
        init_events = self.connection.automox_api.get_events(params.get(Input.ORG_ID), params.get(Input.EVENT_TYPE))

        # Identify the most recent event and record
        if len(init_events) > 0:
            last_event_id = init_events[0].get("id")
        else:
            last_event_id = 0

        self.logger.info(f"Trigger started; most recent {params.get(Input.EVENT_TYPE)} event ID is {last_event_id}")

        while True:
            page = 0
            cont = True
            new_last_event_id = copy.copy(last_event_id)
            # Continue fetching events while trigger is running, sleep 5 minutes in between pulls
            while cont:
                events = self.connection.automox_api.get_events(
                    params.get(Input.ORG_ID), params.get(Input.EVENT_TYPE), page
                )

                for event in events:
                    if event.get("id") == last_event_id:
                        cont = False  # Don't continue paging since we've reached the most recent event ID
                        last_event_id = new_last_event_id  # Store most recent event ID for the next time trigger runs
                        break

                    # Keep track of the most recent event ID through pages
                    if event.get("id") > last_event_id:
                        new_last_event_id = event.get("id")
                    self.send({Output.EVENT: event})

                page += 1

            # Sleep for 5 minutes between retrieval of events
            time.sleep(params.get("interval", 300))
