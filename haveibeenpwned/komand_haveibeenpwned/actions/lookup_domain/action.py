import komand
from .schema import LookupDomainInput, LookupDomainOutput, Input, Output
# Custom imports below
from komand_haveibeenpwned.util.util import HaveIBeenPwned


class LookupDomain(komand.Action):

    _BASE_URL = 'https://haveibeenpwned.com/api/v3/breaches'

    def __init__(self):
        super(self.__class__, self).__init__(
            name='lookup_domain',
            description='List domain breaches',
            input=LookupDomainInput(),
            output=LookupDomainOutput())
            

    def run(self, params={}):
        hibp = HaveIBeenPwned(self.logger)
        domain_name = params.get('domain')
        include_unverified = params.get(Input.INCLUDE_UNVERIFIED)
        truncate_response = params.get(Input.TRUNCATE_RESPONSE)
        querystring = dict()

        if domain_name:
            querystring["domain"] = domain_name
        querystring["includeUnverified"] = include_unverified
        querystring["truncateResponse"] = truncate_response
        if not querystring.keys():
            querystring = None

        results = hibp.get_request(url=self._BASE_URL, params=querystring, key=self.connection.api_key)
        if results:
            return {'found': True, 'breaches': results}
        return {'found': False}
