import komand
from .schema import SearchEventsInput, SearchEventsOutput
# Custom imports below


class SearchEvents(komand.Action):

    _THREAT_LEVELS = {"Don't search on": None,
                      'Undefined': 1,
                      'Low': 2,
                      'Medium': 3,
                      'High': 4}

    _ANALYSIS_LEVEL = {"Don't search on": None,
                       'Initial': 0,
                       'Ongoing': 1,
                       'Completed': 2}

    _PUBLISHED = {"Don't search on": None,
                  'False': 0,
                  'True': 1}

    def __init__(self):
        super(self.__class__, self).__init__(
                name='search_events',
                description='Search for events',
                input=SearchEventsInput(),
                output=SearchEventsOutput())

    def run(self, params={}):
        # Set blank strings to None
        for k, v in params.items():
            if not params[k]:
                params[k] = None

        event = params.get('event')
        tag = params.get('tag')
        date_from = params.get('date_from')
        date_until = params.get('date_until')
        threat_level = params.get('threat_level')
        published = params.get('published')
        organization = params.get('organization')
        analysis = params.get('analysis')
        self.logger.info(threat_level)

        client = self.connection.client

        # Set threat level
        threat_level = self._THREAT_LEVELS[threat_level]
        # Set analysis
        analysis = self._ANALYSIS_LEVEL[analysis]
        # Set published
        published = self._PUBLISHED[published]

        events = client.search_index(published=published, analysis=analysis, threatlevel=threat_level, org=organization,
                                     dateuntil=date_until, datefrom=date_from, tag=tag, eventid=event)
        try:
            events = events['response']
        except KeyError:
            self.logger.error('Returned events were not formatted correctly, ' + events)
            raise
        event_id = []
        for event in events:
            try:
                event_id.append(event['id'])
            except KeyError:
                self.logger.error('No ID in event, ' + event)
                raise

        return {'event_list': event_id}

    def test(self):
        client = self.connection.client
        output = client.test_connection()
        self.logger.info(output)
        return {"status": True}
