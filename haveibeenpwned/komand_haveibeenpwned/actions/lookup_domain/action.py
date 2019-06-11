import komand
from .schema import LookupDomainInput, LookupDomainOutput
# Custom imports below
from komand_haveibeenpwned.util.util import HaveIBeenPwned


class LookupDomain(komand.Action):

    _BASE_URL = 'https://haveibeenpwned.com/api/v2/breaches'

    def __init__(self):
        super(self.__class__, self).__init__(
            name='lookup_domain',
            description='List domain breaches',
            input=LookupDomainInput(),
            output=LookupDomainOutput())

    def run(self, params={}):
        hibp = HaveIBeenPwned(self.logger)
        domain_name = params.get('domain')
        if domain_name:
            querystring = {"domain": domain_name}
        else:
            querystring = None

        results = hibp.get_request(url=self._BASE_URL, params=querystring)
        if results:
            return {'found': True, 'breaches': results}
        return {'found': False}
