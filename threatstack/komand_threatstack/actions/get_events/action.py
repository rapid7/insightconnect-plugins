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
        events = clean([self._add_miscellaneous_values(event=event) for event in events])

        return {Output.EVENTS: events, Output.COUNT: len(events)}

    def _add_miscellaneous_values(self, event: dict) -> dict:
        """
        Extract miscellaneous output (data that is not found across all events) and add it back to the event
        :param event: Raw event data
        :return: Event with dynamic output added under the 'miscellaneous' key
        """

        # Create a set of standardized values to ignore during parsing
        standard_values = set(self.output.schema["definitions"]["event"]["properties"].keys())
        standard_values.remove("miscellaneous")

        # Get non-standard data/keys from the event
        misc_data = set(event.keys()).difference(standard_values)

        # Create dictionary of miscellaneous data using elements from the misc_data set
        event["miscellaneous"] = {key: event.pop(key) for key in misc_data}

        return event

