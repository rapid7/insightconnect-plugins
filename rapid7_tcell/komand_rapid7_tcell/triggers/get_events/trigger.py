import komand
import time
from .schema import GetEventsInput, GetEventsOutput
# Custom imports below
from datetime import datetime
from komand.helper import clean


class GetEvents(komand.Trigger):

    def __init__(self):
        super(self.__class__, self).__init__(
                name='get_events',
                description='Fetch events of the provided type',
                input=GetEventsInput(),
                output=GetEventsOutput())

    def run(self, params={}):
        """Run the trigger"""
        app_id = params.get('app_id')
        source = params.get('source')
        frequency = params.get('frequency', 5)
        filter_ = params.get('filter')

        while True:
            from_ = datetime.now()

            events = self.connection.api.get_events(
                app_id, source, filter_, from_
            ).get('table', [])

            if not events:
                self.logger.info('No new events found')
            for event in events:
                self.logger.info('New event found: ' + event.get('id'))
                # Unnest the location object
                # "location": { "location": { "country": "United States" } }
                #  ->
                # "location": { "country": "United States" }
                if 'location' in event:
                    if 'location' in event['location']:
                        location = event.pop('location').pop('location')
                        event['location'] = location
                self.send({'event': clean(event)})
            time.sleep(frequency)

    def test(self):
        return {}
