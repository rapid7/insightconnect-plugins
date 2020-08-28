import json

import komand
from .schema import SearchEventsInput, SearchEventsOutput, Input, Component


# Custom imports below


class SearchEvents(komand.Action):
    _THREAT_LEVELS = {"Do not search on": None,
                      'Undefined': 1,
                      'Low': 2,
                      'Medium': 3,
                      'High': 4}

    _ANALYSIS_LEVEL = {"Do not search on": None,
                       'Initial': 0,
                       'Ongoing': 1,
                       'Completed': 2}

    _PUBLISHED = {"Do not search on": None,
                  'False': 0,
                  'True': 1}

    def __init__(self):
        super(self.__class__, self).__init__(
            name='search_events',
            description=Component.DESCRIPTION,
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
        values = params.get(Input.VALUES)
        type_attribute = params.get(Input.TYPE_ATTRIBUTE)
        category = params.get(Input.CATEGORY)
        self.logger.info(threat_level)

        client = self.connection.client

        # Set threat level
        if threat_level:
            threat_level = self._THREAT_LEVELS[threat_level]
        # Set analysis
        if analysis:
            analysis = self._ANALYSIS_LEVEL[analysis]
        # Set published
        if published:
            published = self._PUBLISHED[published]

        search_index_event_id = []
        search_event_id = []
        should_search_index = published or analysis or threat_level or organization or date_until or date_from or tag or event
        should_search = values or type_attribute or category

        if should_search_index:
            search_index_events = client.search_index(published=published, analysis=analysis, threatlevel=threat_level,
                                                      org=organization, dateuntil=date_until, datefrom=date_from,
                                                      tag=tag,
                                                      eventid=event)
            try:
                search_index_events = search_index_events['response']
            except KeyError:
                self.logger.error('Returned events were not formatted correctly, ' + json.dumps(search_index_events))
                raise
            for event in search_index_events:
                try:
                    search_index_event_id.append(event['id'])
                except KeyError:
                    self.logger.error('No ID in event, ' + event)
                    raise

        if should_search:
            search_events = client.search(values=values, type_attribute=type_attribute, category=category)
            try:
                search_events = search_events['response']
            except KeyError:
                self.logger.error('Returned events were not formatted correctly, ' + json.dumps(search_events))
                raise
            for eventWrapper in search_events:
                try:
                    event = eventWrapper['Event']
                except KeyError:
                    self.logger.error('Event was not formatted correctly, ' + json.dumps(eventWrapper))
                    raise
                try:
                    search_event_id.append(event['id'])
                except KeyError:
                    self.logger.error('No ID in event, ' + json.dumps(event))
                    raise
        if should_search and should_search_index:
            event_id = list(set(search_event_id).intersection(search_index_event_id))
            return {'event_list': event_id}
        if should_search:
            return {'event_list': search_event_id}
        return {'event_list': search_index_event_id}
