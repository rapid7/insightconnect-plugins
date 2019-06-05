import komand
from .schema import SearchEventsInput, SearchEventsOutput
# Custom imports below
from requests import exceptions as rexceptions
from threatqsdk import exceptions as texceptions


class SearchEvents(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='search_events',
                description='List all events',
                input=SearchEventsInput(),
                output=SearchEventsOutput())

    def run(self, params={}):
        """run searches for events in Threat Quotient"""
        try:
            clean_params = komand.helper.clean_dict(params['event'])
            events = {}
            results = self.connection.threatq.get('/api/events', params=clean_params)
            events['total'] = results['total']
            events['data'] = []
            for hit in results['data']:
                events['data'].append({str(k):(str(v) if isinstance(v, unicode) else v) for k,v in hit.items()})
            return { "events": events }
        except texceptions.APIError as apie:
            err = 'ThreatQ SDK: APIError: reason %s' % apie.message
            self.logger.error(err)
        except rexceptions.HTTPError as httpe:
            err = 'ThreatQ SDK: HTTPError: reason %s' % httpe.message
            self.logger.error(err)
        raise Exception('ThreatQ SDK call failed')

    def test(self):
        """TODO: Test action"""
        if self.connection.threatq:
            return {}
