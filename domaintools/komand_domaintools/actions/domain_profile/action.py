import komand
from .schema import DomainProfileInput, DomainProfileOutput
# Custom imports below
from komand_domaintools.util import util


class DomainProfile(komand.Action):
    def __init__(self):
        super(self.__class__, self).__init__(
                name='domain_profile',
                description='Provides basic domain name registration details and a preview of additional data ',
                input=DomainProfileInput(),
                output=DomainProfileOutput())

    def run(self, params={}):
        query = params.get('domain')
        response = utils.make_request(self.connection.api.domain_profile, query)
        return self._cleanup_response(response)

    def _cleanup_response(self, response):
        # Workaround for integer fields that return NULL/empty values
        # As integer fields, this fails the validation test
        history = response['response']['history']
        if not history['name_server']['timespan_in_years']:
            history['name_server']['timespan_in_years'] = 0

        if not history['ip_address']['timespan_in_years']:
            history['ip_address']['timespan_in_years'] = 0

        response['response']['history'] = history
        return response

    def test(self):
        """TODO: Test action"""
        return {}
