import komand
from .schema import SearchIndicatorsInput, SearchIndicatorsOutput
# Custom imports below
from requests import exceptions as rexceptions
from threatqsdk import exceptions as texceptions


class SearchIndicators(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='search_indicators',
                description='Search for a specific indicator',
                input=SearchIndicatorsInput(),
                output=SearchIndicatorsOutput())

    def run(self, params={}):
        """run searches for indicators in Threat Quotient"""
        try:
            clean_params = komand.helper.clean_dict(params['indicator'])
            indicators = {}
            results = self.connection.threatq.get('/api/indicators', params=clean_params)
            indicators['total'] = results['total']
            indicators['data'] = []
            for hit in results['data']:
                indicators['data'].append({str(k):(str(v) if isinstance(v, unicode) else v) for k,v in hit.items()})
            return { "indicators": indicators }
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
