import komand
from .schema import GetEventsInput, GetEventsOutput, Input, Output, Component
# Custom imports below
from komand.helper import clean


class GetEvents(komand.Action):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_events',
                description=Component.DESCRIPTION,
                input=GetEventsInput(),
                output=GetEventsOutput())

    def run(self, params={}):
        alert_id = params.get(Input.ALERT_ID)

        events = self.connection.client.alerts.events(alert_id=alert_id).get("events", [])
        events = clean([event for event in events])

        return {Output.EVENTS: events, Output.COUNT: len(events)}
